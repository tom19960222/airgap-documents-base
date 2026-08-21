---
collection: kernel
version: "6.8"
title: "Landlock LSM: kernel documentation"
source_url: https://www.kernel.org/doc/html/v6.8/security/landlock.html
fetched_at: 2026-08-21T03:39:53+00:00
---
# Landlock LSM: kernel documentation

Author
:   Mickaël Salaün

Date
:   December 2022

Landlock's goal is to create scoped access-control (i.e. sandboxing). To
harden a whole system, this feature should be available to any process,
including unprivileged ones. Because such process may be compromised or
backdoored (i.e. untrusted), Landlock's features must be safe to use from the
kernel and other processes point of view. Landlock's interface must therefore
expose a minimal attack surface.

Landlock is designed to be usable by unprivileged processes while following the
system security policy enforced by other access control mechanisms (e.g. DAC,
LSM). Indeed, a Landlock rule shall not interfere with other access-controls
enforced on the system, only add more restrictions.

Any user can enforce Landlock rulesets on their processes. They are merged and
evaluated according to the inherited ones in a way that ensures that only more
constraints can be added.

User space documentation can be found here:
[Landlock: unprivileged access control](../userspace-api/landlock.md).

## Guiding principles for safe access controls

- A Landlock rule shall be focused on access control on kernel objects instead
  of syscall filtering (i.e. syscall arguments), which is the purpose of
  seccomp-bpf.
- To avoid multiple kinds of side-channel attacks (e.g. leak of security
  policies, CPU-based attacks), Landlock rules shall not be able to
  programmatically communicate with user space.
- Kernel access check shall not slow down access request from unsandboxed
  processes.
- Computation related to Landlock operations (e.g. enforcing a ruleset) shall
  only impact the processes requesting them.
- Resources (e.g. file descriptors) directly obtained from the kernel by a
  sandboxed process shall retain their scoped accesses (at the time of resource
  acquisition) whatever process use them.
  Cf. [File descriptor access rights](landlock.md#file-descriptor-access-rights).

## Design choices

### Inode access rights

All access rights are tied to an inode and what can be accessed through it.
Reading the content of a directory does not imply to be allowed to read the
content of a listed inode. Indeed, a file name is local to its parent
directory, and an inode can be referenced by multiple file names thanks to
(hard) links. Being able to unlink a file only has a direct impact on the
directory, not the unlinked inode. This is the reason why
`LANDLOCK_ACCESS_FS_REMOVE_FILE` or `LANDLOCK_ACCESS_FS_REFER` are not
allowed to be tied to files but only to directories.

### File descriptor access rights

Access rights are checked and tied to file descriptors at open time. The
underlying principle is that equivalent sequences of operations should lead to
the same results, when they are executed under the same Landlock domain.

Taking the `LANDLOCK_ACCESS_FS_TRUNCATE` right as an example, it may be
allowed to open a file for writing without being allowed to
*ftruncate* the resulting file descriptor if the related file
hierarchy doesn't grant such access right. The following sequences of
operations have the same semantic and should then have the same result:

- `truncate(path);`
- `int fd = open(path, O_WRONLY); ftruncate(fd); close(fd);`

Similarly to file access modes (e.g. `O_RDWR`), Landlock access rights
attached to file descriptors are retained even if they are passed between
processes (e.g. through a Unix domain socket). Such access rights will then be
enforced even if the receiving process is not sandboxed by Landlock. Indeed,
this is required to keep a consistent access control over the whole system, and
this avoids unattended bypasses through file descriptor passing (i.e. confused
deputy attack).

## Tests

Userspace tests for backward compatibility, ptrace restrictions and filesystem
support can be found here: [tools/testing/selftests/landlock/](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/tools/testing/selftests/landlock/).

## Kernel structures

### Object

struct landlock_object_underops
:   Operations on an underlying object

**Definition**:

```
struct landlock_object_underops {
    void (*release)(struct landlock_object *const object) __releases(object->lock);
};
```

**Members**

`release`
:   Releases the underlying object (e.g. [`iput()`](../filesystems/api-summary.md#c.iput "iput") for an inode).

struct landlock_object
:   Security blob tied to a kernel object

**Definition**:

```
struct landlock_object {
    refcount_t usage;
    spinlock_t lock;
    void *underobj;
    union {
        struct rcu_head rcu_free;
        const struct landlock_object_underops *underops;
    };
};
```

**Members**

`usage`
:   This counter is used to tie an object to the rules matching
    it or to keep it alive while adding a new rule. If this counter
    reaches zero, this struct must not be modified, but this counter can
    still be read from within an RCU read-side critical section. When
    adding a new rule to an object with a usage counter of zero, we must
    wait until the pointer to this object is set to NULL (or recycled).

`lock`
:   Protects against concurrent modifications. This lock must be
    held from the time **usage** drops to zero until any weak references
    from **underobj** to this object have been cleaned up.

    Lock ordering: inode->i_lock nests inside this.

`underobj`
:   Used when cleaning up an object and to mark an object as
    tied to its underlying kernel structure. This pointer is protected
    by **lock**. Cf. landlock_release_inodes() and release_inode().

`{unnamed_union}`
:   anonymous

`rcu_free`
:   Enables lockless use of **usage**, **lock** and
    **underobj** from within an RCU read-side critical section.
    **rcu_free** and **underops** are only used by
    landlock_put_object().

`underops`
:   Enables landlock_put_object() to release the
    underlying object (e.g. inode).

**Description**

The goal of this structure is to enable to tie a set of ephemeral access
rights (pertaining to different domains) to a kernel object (e.g an inode)
in a safe way. This implies to handle concurrent use and modification.

The lifetime of a [`struct landlock_object`](landlock.md#c.landlock_object "landlock_object") depends on the rules referring to
it.

### Filesystem

struct landlock_inode_security
:   Inode security blob

**Definition**:

```
struct landlock_inode_security {
    struct landlock_object __rcu *object;
};
```

**Members**

`object`
:   Weak pointer to an allocated object. All assignments of a
    new object are protected by the underlying inode->i_lock. However,
    atomically disassociating **object** from the inode is only protected
    by **object->lock**, from the time **object**'s usage refcount drops to
    zero to the time this pointer is nulled out (cf. release_inode() and
    hook_sb_delete()). Indeed, such disassociation doesn't require
    inode->i_lock thanks to the careful [`rcu_access_pointer()`](../core-api/kernel-api.md#c.rcu_access_pointer "rcu_access_pointer") check
    performed by get_inode_object().

**Description**

Enable to reference a [`struct landlock_object`](landlock.md#c.landlock_object "landlock_object") tied to an inode (i.e.
underlying object).

struct landlock_file_security
:   File security blob

**Definition**:

```
struct landlock_file_security {
    access_mask_t allowed_access;
};
```

**Members**

`allowed_access`
:   Access rights that were available at the time of
    opening the file. This is not necessarily the full set of access
    rights available at that time, but it's the necessary subset as
    needed to authorize later operations on the open file.

**Description**

This information is populated when opening a file in hook_file_open, and
tracks the relevant Landlock access rights that were available at the time
of opening the file. Other LSM hooks use these rights in order to authorize
operations on already opened files.

struct landlock_superblock_security
:   Superblock security blob

**Definition**:

```
struct landlock_superblock_security {
    atomic_long_t inode_refs;
};
```

**Members**

`inode_refs`
:   Number of pending inodes (from this superblock) that
    are being released by release_inode().
    Cf. struct super_block->s_fsnotify_inode_refs .

**Description**

Enable hook_sb_delete() to wait for concurrent calls to release_inode().

### Ruleset and domain

A domain is a read-only ruleset tied to a set of subjects (i.e. tasks'
credentials). Each time a ruleset is enforced on a task, the current domain is
duplicated and the ruleset is imported as a new layer of rules in the new
domain. Indeed, once in a domain, each rule is tied to a layer level. To
grant access to an object, at least one rule of each layer must allow the
requested action on the object. A task can then only transit to a new domain
that is the intersection of the constraints from the current domain and those
of a ruleset provided by the task.

The definition of a subject is implicit for a task sandboxing itself, which
makes the reasoning much easier and helps avoid pitfalls.

struct landlock_layer
:   Access rights for a given layer

**Definition**:

```
struct landlock_layer {
    u16 level;
    access_mask_t access;
};
```

**Members**

`level`
:   Position of this layer in the layer stack.

`access`
:   Bitfield of allowed actions on the kernel object. They are
    relative to the object type (e.g. `LANDLOCK_ACTION_FS_READ`).

union landlock_key
:   Key of a ruleset's red-black tree

**Definition**:

```
union landlock_key {
    struct landlock_object *object;
    uintptr_t data;
};
```

**Members**

`object`
:   Pointer to identify a kernel object (e.g. an inode).

`data`
:   Raw data to identify an arbitrary 32-bit value
    (e.g. a TCP port).

enum landlock_key_type
:   Type of [`union landlock_key`](landlock.md#c.landlock_key "landlock_key")

**Constants**

`LANDLOCK_KEY_INODE`
:   Type of [`landlock_ruleset.root_inode`](landlock.md#c.landlock_ruleset "landlock_ruleset")'s node
    keys.

`LANDLOCK_KEY_NET_PORT`
:   Type of [`landlock_ruleset.root_net_port`](landlock.md#c.landlock_ruleset "landlock_ruleset")'s
    node keys.

struct landlock_id
:   Unique rule identifier for a ruleset

**Definition**:

```
struct landlock_id {
    union landlock_key key;
    const enum landlock_key_type type;
};
```

**Members**

`key`
:   Identifies either a kernel object (e.g. an inode) or
    a raw value (e.g. a TCP port).

`type`
:   Type of a landlock_ruleset's root tree.

struct landlock_rule
:   Access rights tied to an object

**Definition**:

```
struct landlock_rule {
    struct rb_node node;
    union landlock_key key;
    u32 num_layers;
    struct landlock_layer layers[] ;
};
```

**Members**

`node`
:   Node in the ruleset's red-black tree.

`key`
:   A union to identify either a kernel object (e.g. an inode) or
    a raw data value (e.g. a network socket port). This is used as a key
    for this ruleset element. The pointer is set once and never
    modified. It always points to an allocated object because each rule
    increments the refcount of its object.

`num_layers`
:   Number of entries in **layers**.

`layers`
:   Stack of layers, from the latest to the newest, implemented
    as a flexible array member (FAM).

struct landlock_hierarchy
:   Node in a ruleset hierarchy

**Definition**:

```
struct landlock_hierarchy {
    struct landlock_hierarchy *parent;
    refcount_t usage;
};
```

**Members**

`parent`
:   Pointer to the parent node, or NULL if it is a root
    Landlock domain.

`usage`
:   Number of potential children domains plus their parent
    domain.

struct landlock_ruleset
:   Landlock ruleset

**Definition**:

```
struct landlock_ruleset {
    struct rb_root root_inode;
#if IS_ENABLED(CONFIG_INET);
    struct rb_root root_net_port;
#endif ;
    struct landlock_hierarchy *hierarchy;
    union {
        struct work_struct work_free;
        struct {
            struct mutex lock;
            refcount_t usage;
            u32 num_rules;
            u32 num_layers;
            access_masks_t access_masks[];
        };
    };
};
```

**Members**

`root_inode`
:   Root of a red-black tree containing [`struct
    landlock_rule`](landlock.md#c.landlock_rule "landlock_rule") nodes with inode object. Once a ruleset is tied to a
    process (i.e. as a domain), this tree is immutable until **usage**
    reaches zero.

`root_net_port`
:   Root of a red-black tree containing [`struct
    landlock_rule`](landlock.md#c.landlock_rule "landlock_rule") nodes with network port. Once a ruleset is tied to a
    process (i.e. as a domain), this tree is immutable until **usage**
    reaches zero.

`hierarchy`
:   Enables hierarchy identification even when a parent
    domain vanishes. This is needed for the ptrace protection.

`{unnamed_union}`
:   anonymous

`work_free`
:   Enables to free a ruleset within a lockless
    section. This is only used by
    landlock_put_ruleset_deferred() when **usage** reaches zero.
    The fields **lock**, **usage**, **num_rules**, **num_layers** and
    **access_masks** are then unused.

`{unnamed_struct}`
:   anonymous

`lock`
:   Protects against concurrent modifications of
    **root**, if **usage** is greater than zero.

`usage`
:   Number of processes (i.e. domains) or file
    descriptors referencing this ruleset.

`num_rules`
:   Number of non-overlapping (i.e. not for
    the same object) rules in this ruleset.

`num_layers`
:   Number of layers that are used in this
    ruleset. This enables to check that all the layers
    allow an access request. A value of 0 identifies a
    non-merged ruleset (i.e. not a domain).

`access_masks`
:   Contains the subset of filesystem and
    network actions that are restricted by a ruleset.
    A domain saves all layers of merged rulesets in a
    stack (FAM), starting from the first layer to the
    last one. These layers are used when merging
    rulesets, for user space backward compatibility
    (i.e. future-proof), and to properly handle merged
    rulesets without overlapping access rights. These
    layers are set once and never changed for the
    lifetime of the ruleset.

**Description**

This data structure must contain unique entries, be updatable, and quick to
match an object.

---
collection: kernel
version: "6.17"
title: "Landlock: unprivileged access control"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/landlock.html
fetched_at: 2026-09-16T16:23:34+00:00
---
# Landlock: unprivileged access control

Author:
:   Mickaël Salaün

Date:
:   March 2025

The goal of Landlock is to enable restriction of ambient rights (e.g. global
filesystem or network access) for a set of processes. Because Landlock
is a stackable LSM, it makes it possible to create safe security sandboxes as
new security layers in addition to the existing system-wide access-controls.
This kind of sandbox is expected to help mitigate the security impact of bugs or
unexpected/malicious behaviors in user space applications. Landlock empowers
any process, including unprivileged ones, to securely restrict themselves.

We can quickly make sure that Landlock is enabled in the running system by
looking for “landlock: Up and running” in kernel logs (as root):
`dmesg | grep landlock || journalctl -kb -g landlock` .
Developers can also easily check for Landlock support with a
[related system call](landlock.md#landlock-abi-versions).
If Landlock is not currently supported, we need to
[configure the kernel appropriately](landlock.md#kernel-support).

## Landlock rules

A Landlock rule describes an action on an object which the process intends to
perform. A set of rules is aggregated in a ruleset, which can then restrict
the thread enforcing it, and its future children.

The two existing types of rules are:

Filesystem rules
:   For these rules, the object is a file hierarchy,
    and the related filesystem actions are defined with
    filesystem access rights.

Network rules (since ABI v4)
:   For these rules, the object is a TCP port,
    and the related actions are defined with network access rights.

### Defining and enforcing a security policy

We first need to define the ruleset that will contain our rules.

For this example, the ruleset will contain rules that only allow filesystem
read actions and establish a specific TCP connection. Filesystem write
actions and other TCP actions will be denied.

The ruleset then needs to handle both these kinds of actions. This is
required for backward and forward compatibility (i.e. the kernel and user
space may not know each other’s supported restrictions), hence the need
to be explicit about the denied-by-default access rights.

```c
struct landlock_ruleset_attr ruleset_attr = {
    .handled_access_fs =
        LANDLOCK_ACCESS_FS_EXECUTE |
        LANDLOCK_ACCESS_FS_WRITE_FILE |
        LANDLOCK_ACCESS_FS_READ_FILE |
        LANDLOCK_ACCESS_FS_READ_DIR |
        LANDLOCK_ACCESS_FS_REMOVE_DIR |
        LANDLOCK_ACCESS_FS_REMOVE_FILE |
        LANDLOCK_ACCESS_FS_MAKE_CHAR |
        LANDLOCK_ACCESS_FS_MAKE_DIR |
        LANDLOCK_ACCESS_FS_MAKE_REG |
        LANDLOCK_ACCESS_FS_MAKE_SOCK |
        LANDLOCK_ACCESS_FS_MAKE_FIFO |
        LANDLOCK_ACCESS_FS_MAKE_BLOCK |
        LANDLOCK_ACCESS_FS_MAKE_SYM |
        LANDLOCK_ACCESS_FS_REFER |
        LANDLOCK_ACCESS_FS_TRUNCATE |
        LANDLOCK_ACCESS_FS_IOCTL_DEV,
    .handled_access_net =
        LANDLOCK_ACCESS_NET_BIND_TCP |
        LANDLOCK_ACCESS_NET_CONNECT_TCP,
    .scoped =
        LANDLOCK_SCOPE_ABSTRACT_UNIX_SOCKET |
        LANDLOCK_SCOPE_SIGNAL,
};
```

Because we may not know which kernel version an application will be executed
on, it is safer to follow a best-effort security approach. Indeed, we
should try to protect users as much as possible whatever the kernel they are
using.

To be compatible with older Linux versions, we detect the available Landlock ABI
version, and only use the available subset of access rights:

```c
int abi;

abi = landlock_create_ruleset(NULL, 0, LANDLOCK_CREATE_RULESET_VERSION);
if (abi < 0) {
    /* Degrades gracefully if Landlock is not handled. */
    perror("The running kernel does not enable to use Landlock");
    return 0;
}
switch (abi) {
case 1:
    /* Removes LANDLOCK_ACCESS_FS_REFER for ABI < 2 */
    ruleset_attr.handled_access_fs &= ~LANDLOCK_ACCESS_FS_REFER;
    __attribute__((fallthrough));
case 2:
    /* Removes LANDLOCK_ACCESS_FS_TRUNCATE for ABI < 3 */
    ruleset_attr.handled_access_fs &= ~LANDLOCK_ACCESS_FS_TRUNCATE;
    __attribute__((fallthrough));
case 3:
    /* Removes network support for ABI < 4 */
    ruleset_attr.handled_access_net &=
        ~(LANDLOCK_ACCESS_NET_BIND_TCP |
          LANDLOCK_ACCESS_NET_CONNECT_TCP);
    __attribute__((fallthrough));
case 4:
    /* Removes LANDLOCK_ACCESS_FS_IOCTL_DEV for ABI < 5 */
    ruleset_attr.handled_access_fs &= ~LANDLOCK_ACCESS_FS_IOCTL_DEV;
    __attribute__((fallthrough));
case 5:
    /* Removes LANDLOCK_SCOPE_* for ABI < 6 */
    ruleset_attr.scoped &= ~(LANDLOCK_SCOPE_ABSTRACT_UNIX_SOCKET |
                             LANDLOCK_SCOPE_SIGNAL);
}
```

This enables the creation of an inclusive ruleset that will contain our rules.

```c
int ruleset_fd;

ruleset_fd = landlock_create_ruleset(&ruleset_attr, sizeof(ruleset_attr), 0);
if (ruleset_fd < 0) {
    perror("Failed to create a ruleset");
    return 1;
}
```

We can now add a new rule to this ruleset thanks to the returned file
descriptor referring to this ruleset. The rule will only allow reading the
file hierarchy `/usr`. Without another rule, write actions would then be
denied by the ruleset. To add `/usr` to the ruleset, we open it with the
`O_PATH` flag and fill the &[`struct landlock_path_beneath_attr`](landlock.md#c.landlock_path_beneath_attr "landlock_path_beneath_attr") with this file
descriptor.

```c
int err;
struct landlock_path_beneath_attr path_beneath = {
    .allowed_access =
        LANDLOCK_ACCESS_FS_EXECUTE |
        LANDLOCK_ACCESS_FS_READ_FILE |
        LANDLOCK_ACCESS_FS_READ_DIR,
};

path_beneath.parent_fd = open("/usr", O_PATH | O_CLOEXEC);
if (path_beneath.parent_fd < 0) {
    perror("Failed to open file");
    close(ruleset_fd);
    return 1;
}
err = landlock_add_rule(ruleset_fd, LANDLOCK_RULE_PATH_BENEATH,
                        &path_beneath, 0);
close(path_beneath.parent_fd);
if (err) {
    perror("Failed to update ruleset");
    close(ruleset_fd);
    return 1;
}
```

It may also be required to create rules following the same logic as explained
for the ruleset creation, by filtering access rights according to the Landlock
ABI version. In this example, this is not required because all of the requested
`allowed_access` rights are already available in ABI 1.

For network access-control, we can add a set of rules that allow to use a port
number for a specific action: HTTPS connections.

```c
struct landlock_net_port_attr net_port = {
    .allowed_access = LANDLOCK_ACCESS_NET_CONNECT_TCP,
    .port = 443,
};

err = landlock_add_rule(ruleset_fd, LANDLOCK_RULE_NET_PORT,
                        &net_port, 0);
```

The next step is to restrict the current thread from gaining more privileges
(e.g. through a SUID binary). We now have a ruleset with the first rule
allowing read access to `/usr` while denying all other handled accesses for
the filesystem, and a second rule allowing HTTPS connections.

```c
if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0)) {
    perror("Failed to restrict privileges");
    close(ruleset_fd);
    return 1;
}
```

The current thread is now ready to sandbox itself with the ruleset.

```c
if (landlock_restrict_self(ruleset_fd, 0)) {
    perror("Failed to enforce ruleset");
    close(ruleset_fd);
    return 1;
}
close(ruleset_fd);
```

If the `landlock_restrict_self` system call succeeds, the current thread is
now restricted and this policy will be enforced on all its subsequently created
children as well. Once a thread is landlocked, there is no way to remove its
security policy; only adding more restrictions is allowed. These threads are
now in a new Landlock domain, which is a merger of their parent one (if any)
with the new ruleset.

Full working code can be found in [samples/landlock/sandboxer.c](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/samples/landlock/sandboxer.c).

### Good practices

It is recommended to set access rights to file hierarchy leaves as much as
possible. For instance, it is better to be able to have `~/doc/` as a
read-only hierarchy and `~/tmp/` as a read-write hierarchy, compared to
`~/` as a read-only hierarchy and `~/tmp/` as a read-write hierarchy.
Following this good practice leads to self-sufficient hierarchies that do not
depend on their location (i.e. parent directories). This is particularly
relevant when we want to allow linking or renaming. Indeed, having consistent
access rights per directory enables changing the location of such directories
without relying on the destination directory access rights (except those that
are required for this operation, see `LANDLOCK_ACCESS_FS_REFER`
documentation).

Having self-sufficient hierarchies also helps to tighten the required access
rights to the minimal set of data. This also helps avoid sinkhole directories,
i.e. directories where data can be linked to but not linked from. However,
this depends on data organization, which might not be controlled by developers.
In this case, granting read-write access to `~/tmp/`, instead of write-only
access, would potentially allow moving `~/tmp/` to a non-readable directory
and still keep the ability to list the content of `~/tmp/`.

### Layers of file path access rights

Each time a thread enforces a ruleset on itself, it updates its Landlock domain
with a new layer of policy. This complementary policy is stacked with any
other rulesets potentially already restricting this thread. A sandboxed thread
can then safely add more constraints to itself with a new enforced ruleset.

One policy layer grants access to a file path if at least one of its rules
encountered on the path grants the access. A sandboxed thread can only access
a file path if all its enforced policy layers grant the access as well as all
the other system access controls (e.g. filesystem DAC, other LSM policies,
etc.).

### Bind mounts and OverlayFS

Landlock enables restricting access to file hierarchies, which means that these
access rights can be propagated with bind mounts (cf.
[Shared Subtrees](../filesystems/sharedsubtree.md)) but not with
[Overlay Filesystem](../filesystems/overlayfs.md).

A bind mount mirrors a source file hierarchy to a destination. The destination
hierarchy is then composed of the exact same files, on which Landlock rules can
be tied, either via the source or the destination path. These rules restrict
access when they are encountered on a path, which means that they can restrict
access to multiple file hierarchies at the same time, whether these hierarchies
are the result of bind mounts or not.

An OverlayFS mount point consists of upper and lower layers. These layers are
combined in a merge directory, and that merged directory becomes available at
the mount point. This merge hierarchy may include files from the upper and
lower layers, but modifications performed on the merge hierarchy only reflect
on the upper layer. From a Landlock policy point of view, all OverlayFS layers
and merge hierarchies are standalone and each contains their own set of files
and directories, which is different from bind mounts. A policy restricting an
OverlayFS layer will not restrict the resulted merged hierarchy, and vice versa.
Landlock users should then only think about file hierarchies they want to allow
access to, regardless of the underlying filesystem.

### Inheritance

Every new thread resulting from a *clone(2)* inherits Landlock domain
restrictions from its parent. This is similar to seccomp inheritance (cf.
[Seccomp BPF (SECure COMPuting with filters)](seccomp_filter.md)) or any other LSM dealing with
task’s *credentials(7)*. For instance, one process’s thread may apply
Landlock rules to itself, but they will not be automatically applied to other
sibling threads (unlike POSIX thread credential changes, cf.
*nptl(7)*).

When a thread sandboxes itself, we have the guarantee that the related security
policy will stay enforced on all this thread’s descendants. This allows
creating standalone and modular security policies per application, which will
automatically be composed between themselves according to their runtime parent
policies.

### Ptrace restrictions

A sandboxed process has less privileges than a non-sandboxed process and must
then be subject to additional restrictions when manipulating another process.
To be allowed to use *ptrace(2)* and related syscalls on a target
process, a sandboxed process should have a superset of the target process’s
access rights, which means the tracee must be in a sub-domain of the tracer.

### IPC scoping

Similar to the implicit [Ptrace restrictions](landlock.md#ptrace-restrictions), we may want to further restrict
interactions between sandboxes. Therefore, at ruleset creation time, each
Landlock domain can restrict the scope for certain operations, so that these
operations can only reach out to processes within the same Landlock domain or in
a nested Landlock domain (the “scope”).

The operations which can be scoped are:

`LANDLOCK_SCOPE_SIGNAL`
:   This limits the sending of signals to target processes which run within the
    same or a nested Landlock domain.

`LANDLOCK_SCOPE_ABSTRACT_UNIX_SOCKET`
:   This limits the set of abstract *unix(7)* sockets to which we can
    *connect(2)* to socket addresses which were created by a process in
    the same or a nested Landlock domain.

    A *sendto(2)* on a non-connected datagram socket is treated as if
    it were doing an implicit *connect(2)* and will be blocked if the
    remote end does not stem from the same or a nested Landlock domain.

    A *sendto(2)* on a socket which was previously connected will not
    be restricted. This works for both datagram and stream sockets.

IPC scoping does not support exceptions via *landlock_add_rule(2)*.
If an operation is scoped within a domain, no rules can be added to allow access
to resources or processes outside of the scope.

### Truncating files

The operations covered by `LANDLOCK_ACCESS_FS_WRITE_FILE` and
`LANDLOCK_ACCESS_FS_TRUNCATE` both change the contents of a file and sometimes
overlap in non-intuitive ways. It is recommended to always specify both of
these together.

A particularly surprising example is *creat(2)*. The name suggests
that this system call requires the rights to create and write files. However,
it also requires the truncate right if an existing file under the same name is
already present.

It should also be noted that truncating files does not require the
`LANDLOCK_ACCESS_FS_WRITE_FILE` right. Apart from the *truncate(2)*
system call, this can also be done through *open(2)* with the flags
`O_RDONLY | O_TRUNC`.

The truncate right is associated with the opened file (see below).

### Rights associated with file descriptors

When opening a file, the availability of the `LANDLOCK_ACCESS_FS_TRUNCATE` and
`LANDLOCK_ACCESS_FS_IOCTL_DEV` rights is associated with the newly created
file descriptor and will be used for subsequent truncation and ioctl attempts
using *ftruncate(2)* and *ioctl(2)*. The behavior is similar
to opening a file for reading or writing, where permissions are checked during
*open(2)*, but not during the subsequent *read(2)* and
*write(2)* calls.

As a consequence, it is possible that a process has multiple open file
descriptors referring to the same file, but Landlock enforces different things
when operating with these file descriptors. This can happen when a Landlock
ruleset gets enforced and the process keeps file descriptors which were opened
both before and after the enforcement. It is also possible to pass such file
descriptors between processes, keeping their Landlock properties, even when some
of the involved processes do not have an enforced Landlock ruleset.

## Compatibility

### Backward and forward compatibility

Landlock is designed to be compatible with past and future versions of the
kernel. This is achieved thanks to the system call attributes and the
associated bitflags, particularly the ruleset’s `handled_access_fs`. Making
handled access rights explicit enables the kernel and user space to have a clear
contract with each other. This is required to make sure sandboxing will not
get stricter with a system update, which could break applications.

Developers can subscribe to the [Landlock mailing list](https://subspace.kernel.org/lists.linux.dev.html) to knowingly update and
test their applications with the latest available features. In the interest of
users, and because they may use different kernel versions, it is strongly
encouraged to follow a best-effort security approach by checking the Landlock
ABI version at runtime and only enforcing the supported features.

### Landlock ABI versions

The Landlock ABI version can be read with the [`sys_landlock_create_ruleset()`](landlock.md#c.sys_landlock_create_ruleset "sys_landlock_create_ruleset")
system call:

```c
int abi;

abi = landlock_create_ruleset(NULL, 0, LANDLOCK_CREATE_RULESET_VERSION);
if (abi < 0) {
    switch (errno) {
    case ENOSYS:
        printf("Landlock is not supported by the current kernel.\n");
        break;
    case EOPNOTSUPP:
        printf("Landlock is currently disabled.\n");
        break;
    }
    return 0;
}
if (abi >= 2) {
    printf("Landlock supports LANDLOCK_ACCESS_FS_REFER.\n");
}
```

The following kernel interfaces are implicitly supported by the first ABI
version. Features only supported from a specific version are explicitly marked
as such.

## Kernel interface

### Access rights

A set of actions on kernel objects may be defined by an attribute (e.g.
[`struct landlock_path_beneath_attr`](landlock.md#c.landlock_path_beneath_attr "landlock_path_beneath_attr")) including a bitmask of access.

#### Filesystem flags

These flags enable to restrict a sandboxed process to a set of actions on
files and directories. Files or directories opened before the sandboxing
are not subject to these restrictions.

The following access rights apply only to files:

- `LANDLOCK_ACCESS_FS_EXECUTE`: Execute a file.
- `LANDLOCK_ACCESS_FS_WRITE_FILE`: Open a file with write access. When
  opening files for writing, you will often additionally need the
  `LANDLOCK_ACCESS_FS_TRUNCATE` right. In many cases, these system calls
  truncate existing files when overwriting them (e.g., *creat(2)*).
- `LANDLOCK_ACCESS_FS_READ_FILE`: Open a file with read access.
- `LANDLOCK_ACCESS_FS_TRUNCATE`: Truncate a file with *truncate(2)*,
  *ftruncate(2)*, *creat(2)*, or *open(2)* with
  `O_TRUNC`. This access right is available since the third version of the
  Landlock ABI.

Whether an opened file can be truncated with *ftruncate(2)* or used
with ioctl(2) is determined during *open(2)*, in the same way as
read and write permissions are checked during *open(2)* using
`LANDLOCK_ACCESS_FS_READ_FILE` and `LANDLOCK_ACCESS_FS_WRITE_FILE`.

A directory can receive access rights related to files or directories. The
following access right is applied to the directory itself, and the
directories beneath it:

- `LANDLOCK_ACCESS_FS_READ_DIR`: Open a directory or list its content.

However, the following access rights only apply to the content of a
directory, not the directory itself:

- `LANDLOCK_ACCESS_FS_REMOVE_DIR`: Remove an empty directory or rename one.
- `LANDLOCK_ACCESS_FS_REMOVE_FILE`: Unlink (or rename) a file.
- `LANDLOCK_ACCESS_FS_MAKE_CHAR`: Create (or rename or link) a character
  device.
- `LANDLOCK_ACCESS_FS_MAKE_DIR`: Create (or rename) a directory.
- `LANDLOCK_ACCESS_FS_MAKE_REG`: Create (or rename or link) a regular file.
- `LANDLOCK_ACCESS_FS_MAKE_SOCK`: Create (or rename or link) a UNIX domain
  socket.
- `LANDLOCK_ACCESS_FS_MAKE_FIFO`: Create (or rename or link) a named pipe.
- `LANDLOCK_ACCESS_FS_MAKE_BLOCK`: Create (or rename or link) a block device.
- `LANDLOCK_ACCESS_FS_MAKE_SYM`: Create (or rename or link) a symbolic link.
- `LANDLOCK_ACCESS_FS_REFER`: Link or rename a file from or to a different
  directory (i.e. reparent a file hierarchy).

  This access right is available since the second version of the Landlock
  ABI.

  This is the only access right which is denied by default by any ruleset,
  even if the right is not specified as handled at ruleset creation time.
  The only way to make a ruleset grant this right is to explicitly allow it
  for a specific directory by adding a matching rule to the ruleset.

  In particular, when using the first Landlock ABI version, Landlock will
  always deny attempts to reparent files between different directories.

  In addition to the source and destination directories having the
  `LANDLOCK_ACCESS_FS_REFER` access right, the attempted link or rename
  operation must meet the following constraints:

  - The reparented file may not gain more access rights in the destination
    directory than it previously had in the source directory. If this is
    attempted, the operation results in an `EXDEV` error.
  - When linking or renaming, the `LANDLOCK_ACCESS_FS_MAKE_*` right for the
    respective file type must be granted for the destination directory.
    Otherwise, the operation results in an `EACCES` error.
  - When renaming, the `LANDLOCK_ACCESS_FS_REMOVE_*` right for the
    respective file type must be granted for the source directory. Otherwise,
    the operation results in an `EACCES` error.

  If multiple requirements are not met, the `EACCES` error code takes
  precedence over `EXDEV`.

The following access right applies both to files and directories:

- `LANDLOCK_ACCESS_FS_IOCTL_DEV`: Invoke *ioctl(2)* commands on an opened
  character or block device.

  This access right applies to all ioctl(2) commands implemented by device
  drivers. However, the following common IOCTL commands continue to be
  invokable independent of the `LANDLOCK_ACCESS_FS_IOCTL_DEV` right:

  - IOCTL commands targeting file descriptors (`FIOCLEX`, `FIONCLEX`),
  - IOCTL commands targeting file descriptions (`FIONBIO`, `FIOASYNC`),
  - IOCTL commands targeting file systems (`FIFREEZE`, `FITHAW`,
    `FIGETBSZ`, `FS_IOC_GETFSUUID`, `FS_IOC_GETFSSYSFSPATH`)
  - Some IOCTL commands which do not make sense when used with devices, but
    whose implementations are safe and return the right error codes
    (`FS_IOC_FIEMAP`, `FICLONE`, `FICLONERANGE`, `FIDEDUPERANGE`)

  This access right is available since the fifth version of the Landlock
  ABI.

> **Warning:**
>
> It is currently not possible to restrict some file-related actions
> accessible through these syscall families: *chdir(2)*,
> *stat(2)*, *flock(2)*, *chmod(2)*,
> *chown(2)*, *setxattr(2)*, *utime(2)*,
> *fcntl(2)*, *access(2)*.
> Future Landlock evolutions will enable to restrict them.

#### Network flags

These flags enable to restrict a sandboxed process to a set of network
actions.

This is supported since Landlock ABI version 4.

The following access rights apply to TCP port numbers:

- `LANDLOCK_ACCESS_NET_BIND_TCP`: Bind a TCP socket to a local port.
- `LANDLOCK_ACCESS_NET_CONNECT_TCP`: Connect an active TCP socket to
  a remote port.

#### Scope flags

These flags enable to isolate a sandboxed process from a set of IPC actions.
Setting a flag for a ruleset will isolate the Landlock domain to forbid
connections to resources outside the domain.

This is supported since Landlock ABI version 6.

Scopes:

- `LANDLOCK_SCOPE_ABSTRACT_UNIX_SOCKET`: Restrict a sandboxed process from
  connecting to an abstract UNIX socket created by a process outside the
  related Landlock domain (e.g., a parent domain or a non-sandboxed process).
- `LANDLOCK_SCOPE_SIGNAL`: Restrict a sandboxed process from sending a signal
  to another process outside the domain.

### Creating a new ruleset

long sys_landlock_create_ruleset(const struct [landlock_ruleset_attr](landlock.md#c.landlock_ruleset_attr "landlock_ruleset_attr") __user \*const attr, const size_t size, const __u32 flags)
:   Create a new ruleset

**Parameters**

`const struct landlock_ruleset_attr __user *const attr`
:   Pointer to a [`struct landlock_ruleset_attr`](landlock.md#c.landlock_ruleset_attr "landlock_ruleset_attr") identifying the scope of
    the new ruleset.

`const size_t size`
:   Size of the pointed [`struct landlock_ruleset_attr`](landlock.md#c.landlock_ruleset_attr "landlock_ruleset_attr") (needed for
    backward and forward compatibility).

`const __u32 flags`
:   Supported values:

**Description**

> - `LANDLOCK_CREATE_RULESET_VERSION`
> - `LANDLOCK_CREATE_RULESET_ERRATA`

This system call enables to create a new Landlock ruleset, and returns the
related file descriptor on success.

If `LANDLOCK_CREATE_RULESET_VERSION` or `LANDLOCK_CREATE_RULESET_ERRATA` is
set, then **attr** must be NULL and **size** must be 0.

Possible returned errors are:

- `EOPNOTSUPP`: Landlock is supported by the kernel but disabled at boot time;
- `EINVAL`: unknown **flags**, or unknown access, or unknown scope, or too small **size**;
- `E2BIG`: **attr** or **size** inconsistencies;
- `EFAULT`: **attr** or **size** inconsistencies;
- `ENOMSG`: empty [`landlock_ruleset_attr.handled_access_fs`](landlock.md#c.landlock_ruleset_attr "landlock_ruleset_attr").

**Flags**

`LANDLOCK_CREATE_RULESET_VERSION`
:   Get the highest supported Landlock ABI version (starting at 1).

`LANDLOCK_CREATE_RULESET_ERRATA`
:   Get a bitmask of fixed issues for the current Landlock ABI version.

struct landlock_ruleset_attr
:   Ruleset definition.

**Definition**:

```
struct landlock_ruleset_attr {
    __u64 handled_access_fs;
    __u64 handled_access_net;
    __u64 scoped;
};
```

**Members**

`handled_access_fs`
:   Bitmask of handled filesystem actions
    (cf. [Filesystem flags](landlock.md#filesystem-flags)).

`handled_access_net`
:   Bitmask of handled network actions (cf. [Network
    flags](landlock.md#network-flags)).

`scoped`
:   Bitmask of scopes (cf. [Scope flags](landlock.md#scope-flags))
    restricting a Landlock domain from accessing outside
    resources (e.g. IPCs).

**Description**

Argument of [`sys_landlock_create_ruleset()`](landlock.md#c.sys_landlock_create_ruleset "sys_landlock_create_ruleset").

This structure defines a set of *handled access rights*, a set of actions on
different object types, which should be denied by default when the ruleset is
enacted. Vice versa, access rights that are not specifically listed here are
not going to be denied by this ruleset when it is enacted.

For historical reasons, the `LANDLOCK_ACCESS_FS_REFER` right is always denied
by default, even when its bit is not set in **handled_access_fs**. In order to
add new rules with this access right, the bit must still be set explicitly
(cf. [Filesystem flags](landlock.md#filesystem-flags)).

The explicit listing of *handled access rights* is required for backwards
compatibility reasons. In most use cases, processes that use Landlock will
*handle* a wide range or all access rights that they know about at build time
(and that they have tested with a kernel that supported them all).

This structure can grow in future Landlock versions.

### Extending a ruleset

long sys_landlock_add_rule(const int ruleset_fd, const enum [landlock_rule_type](landlock.md#c.landlock_rule_type "landlock_rule_type") rule_type, const void __user \*const rule_attr, const __u32 flags)
:   Add a new rule to a ruleset

**Parameters**

`const int ruleset_fd`
:   File descriptor tied to the ruleset that should be extended
    with the new rule.

`const enum landlock_rule_type rule_type`
:   Identify the structure type pointed to by **rule_attr**:
    `LANDLOCK_RULE_PATH_BENEATH` or `LANDLOCK_RULE_NET_PORT`.

`const void __user *const rule_attr`
:   Pointer to a rule (matching the **rule_type**).

`const __u32 flags`
:   Must be 0.

**Description**

This system call enables to define a new rule and add it to an existing
ruleset.

Possible returned errors are:

- `EOPNOTSUPP`: Landlock is supported by the kernel but disabled at boot time;
- `EAFNOSUPPORT`: **rule_type** is `LANDLOCK_RULE_NET_PORT` but TCP/IP is not
  supported by the running kernel;
- `EINVAL`: **flags** is not 0;
- `EINVAL`: The rule accesses are inconsistent (i.e.
  [`landlock_path_beneath_attr.allowed_access`](landlock.md#c.landlock_path_beneath_attr "landlock_path_beneath_attr") or
  [`landlock_net_port_attr.allowed_access`](landlock.md#c.landlock_net_port_attr "landlock_net_port_attr") is not a subset of the ruleset
  handled accesses)
- `EINVAL`: [`landlock_net_port_attr.port`](landlock.md#c.landlock_net_port_attr "landlock_net_port_attr") is greater than 65535;
- `ENOMSG`: Empty accesses (e.g. [`landlock_path_beneath_attr.allowed_access`](landlock.md#c.landlock_path_beneath_attr "landlock_path_beneath_attr") is
  0);
- `EBADF`: **ruleset_fd** is not a file descriptor for the current thread, or a
  member of **rule_attr** is not a file descriptor as expected;
- `EBADFD`: **ruleset_fd** is not a ruleset file descriptor, or a member of
  **rule_attr** is not the expected file descriptor type;
- `EPERM`: **ruleset_fd** has no write access to the underlying ruleset;
- `EFAULT`: **rule_attr** was not a valid address.

enum landlock_rule_type
:   Landlock rule type

**Constants**

`LANDLOCK_RULE_PATH_BENEATH`
:   Type of a [`struct
    landlock_path_beneath_attr`](landlock.md#c.landlock_path_beneath_attr "landlock_path_beneath_attr") .

`LANDLOCK_RULE_NET_PORT`
:   Type of a [`struct
    landlock_net_port_attr`](landlock.md#c.landlock_net_port_attr "landlock_net_port_attr") .

**Description**

Argument of [`sys_landlock_add_rule()`](landlock.md#c.sys_landlock_add_rule "sys_landlock_add_rule").

struct landlock_path_beneath_attr
:   Path hierarchy definition

**Definition**:

```
struct landlock_path_beneath_attr {
    __u64 allowed_access;
    __s32 parent_fd;
};
```

**Members**

`allowed_access`
:   Bitmask of allowed actions for this file hierarchy
    (cf. [Filesystem flags](landlock.md#filesystem-flags)).

`parent_fd`
:   File descriptor, preferably opened with `O_PATH`,
    which identifies the parent directory of a file hierarchy, or just a
    file.

**Description**

Argument of [`sys_landlock_add_rule()`](landlock.md#c.sys_landlock_add_rule "sys_landlock_add_rule").

struct landlock_net_port_attr
:   Network port definition

**Definition**:

```
struct landlock_net_port_attr {
    __u64 allowed_access;
    __u64 port;
};
```

**Members**

`allowed_access`
:   Bitmask of allowed network actions for a port
    (cf. [Network flags](landlock.md#network-flags)).

`port`
:   Network port in host endianness.

    It should be noted that port 0 passed to *bind(2)* will bind
    to an available port from the ephemeral port range. This can be
    configured with the `/proc/sys/net/ipv4/ip_local_port_range` sysctl
    (also used for IPv6).

    A Landlock rule with port 0 and the `LANDLOCK_ACCESS_NET_BIND_TCP`
    right means that requesting to bind on port 0 is allowed and it will
    automatically translate to binding on the related port range.

**Description**

Argument of [`sys_landlock_add_rule()`](landlock.md#c.sys_landlock_add_rule "sys_landlock_add_rule").

### Enforcing a ruleset

long sys_landlock_restrict_self(const int ruleset_fd, const __u32 flags)
:   Enforce a ruleset on the calling thread

**Parameters**

`const int ruleset_fd`
:   File descriptor tied to the ruleset to merge with the target.

`const __u32 flags`
:   Supported values:

**Description**

> - `LANDLOCK_RESTRICT_SELF_LOG_SAME_EXEC_OFF`
> - `LANDLOCK_RESTRICT_SELF_LOG_NEW_EXEC_ON`
> - `LANDLOCK_RESTRICT_SELF_LOG_SUBDOMAINS_OFF`

This system call enables to enforce a Landlock ruleset on the current
thread. Enforcing a ruleset requires that the task has `CAP_SYS_ADMIN` in its
namespace or is running with no_new_privs. This avoids scenarios where
unprivileged tasks can affect the behavior of privileged children.

Possible returned errors are:

- `EOPNOTSUPP`: Landlock is supported by the kernel but disabled at boot time;
- `EINVAL`: **flags** contains an unknown bit.
- `EBADF`: **ruleset_fd** is not a file descriptor for the current thread;
- `EBADFD`: **ruleset_fd** is not a ruleset file descriptor;
- `EPERM`: **ruleset_fd** has no read access to the underlying ruleset, or the
  current thread is not running with no_new_privs, or it doesn’t have
  `CAP_SYS_ADMIN` in its namespace.
- `E2BIG`: The maximum number of stacked rulesets is reached for the current
  thread.

**Flags**

By default, denied accesses originating from programs that sandbox themselves
are logged via the audit subsystem. Such events typically indicate unexpected
behavior, such as bugs or exploitation attempts. However, to avoid excessive
logging, access requests denied by a domain not created by the originating
program are not logged by default. The rationale is that programs should know
their own behavior, but not necessarily the behavior of other programs. This
default configuration is suitable for most programs that sandbox themselves.
For specific use cases, the following flags allow programs to modify this
default logging behavior.

The `LANDLOCK_RESTRICT_SELF_LOG_SAME_EXEC_OFF` and
`LANDLOCK_RESTRICT_SELF_LOG_NEW_EXEC_ON` flags apply to the newly created
Landlock domain.

`LANDLOCK_RESTRICT_SELF_LOG_SAME_EXEC_OFF`
:   Disables logging of denied accesses originating from the thread creating
    the Landlock domain, as well as its children, as long as they continue
    running the same executable code (i.e., without an intervening
    *execve(2)* call). This is intended for programs that execute
    unknown code without invoking *execve(2)*, such as script
    interpreters. Programs that only sandbox themselves should not set this
    flag, so users can be notified of unauthorized access attempts via system
    logs.

`LANDLOCK_RESTRICT_SELF_LOG_NEW_EXEC_ON`
:   Enables logging of denied accesses after an *execve(2)* call,
    providing visibility into unauthorized access attempts by newly executed
    programs within the created Landlock domain. This flag is recommended
    only when all potential executables in the domain are expected to comply
    with the access restrictions, as excessive audit log entries could make
    it more difficult to identify critical events.

`LANDLOCK_RESTRICT_SELF_LOG_SUBDOMAINS_OFF`
:   Disables logging of denied accesses originating from nested Landlock
    domains created by the caller or its descendants. This flag should be set
    according to runtime configuration, not hardcoded, to avoid suppressing
    important security events. It is useful for container runtimes or
    sandboxing tools that may launch programs which themselves create
    Landlock domains and could otherwise generate excessive logs. Unlike
    `LANDLOCK_RESTRICT_SELF_LOG_SAME_EXEC_OFF`, this flag only affects
    future nested domains, not the one being created. It can also be used
    with a **ruleset_fd** value of -1 to mute subdomain logs without creating a
    domain.

## Current limitations

### Filesystem topology modification

Threads sandboxed with filesystem restrictions cannot modify filesystem
topology, whether via *mount(2)* or *pivot_root(2)*.
However, *chroot(2)* calls are not denied.

### Special filesystems

Access to regular files and directories can be restricted by Landlock,
according to the handled accesses of a ruleset. However, files that do not
come from a user-visible filesystem (e.g. pipe, socket), but can still be
accessed through `/proc/<pid>/fd/*`, cannot currently be explicitly
restricted. Likewise, some special kernel filesystems such as nsfs, which can
be accessed through `/proc/<pid>/ns/*`, cannot currently be explicitly
restricted. However, thanks to the [ptrace restrictions](landlock.md#ptrace-restrictions), access to such
sensitive `/proc` files are automatically restricted according to domain
hierarchies. Future Landlock evolutions could still enable to explicitly
restrict such paths with dedicated ruleset flags.

### Ruleset layers

There is a limit of 16 layers of stacked rulesets. This can be an issue for a
task willing to enforce a new ruleset in complement to its 16 inherited
rulesets. Once this limit is reached, [`sys_landlock_restrict_self()`](landlock.md#c.sys_landlock_restrict_self "sys_landlock_restrict_self") returns
E2BIG. It is then strongly suggested to carefully build rulesets once in the
life of a thread, especially for applications able to launch other applications
that may also want to sandbox themselves (e.g. shells, container managers,
etc.).

### Memory usage

Kernel memory allocated to create rulesets is accounted and can be restricted
by the [Memory Resource Controller](../admin-guide/cgroup-v1/memory.md).

### IOCTL support

The `LANDLOCK_ACCESS_FS_IOCTL_DEV` right restricts the use of
*ioctl(2)*, but it only applies to *newly opened* device files. This
means specifically that pre-existing file descriptors like stdin, stdout and
stderr are unaffected.

Users should be aware that TTY devices have traditionally permitted to control
other processes on the same TTY through the `TIOCSTI` and `TIOCLINUX` IOCTL
commands. Both of these require `CAP_SYS_ADMIN` on modern Linux systems, but
the behavior is configurable for `TIOCSTI`.

On older systems, it is therefore recommended to close inherited TTY file
descriptors, or to reopen them from `/proc/self/fd/*` without the
`LANDLOCK_ACCESS_FS_IOCTL_DEV` right, if possible.

Landlock’s IOCTL support is coarse-grained at the moment, but may become more
fine-grained in the future. Until then, users are advised to establish the
guarantees that they need through the file hierarchy, by only allowing the
`LANDLOCK_ACCESS_FS_IOCTL_DEV` right on files where it is really required.

## Previous limitations

### File renaming and linking (ABI < 2)

Because Landlock targets unprivileged access controls, it needs to properly
handle composition of rules. Such property also implies rules nesting.
Properly handling multiple layers of rulesets, each one of them able to
restrict access to files, also implies inheritance of the ruleset restrictions
from a parent to its hierarchy. Because files are identified and restricted by
their hierarchy, moving or linking a file from one directory to another implies
propagation of the hierarchy constraints, or restriction of these actions
according to the potentially lost constraints. To protect against privilege
escalations through renaming or linking, and for the sake of simplicity,
Landlock previously limited linking and renaming to the same directory.
Starting with the Landlock ABI version 2, it is now possible to securely
control renaming and linking thanks to the new `LANDLOCK_ACCESS_FS_REFER`
access right.

### File truncation (ABI < 3)

File truncation could not be denied before the third Landlock ABI, so it is
always allowed when using a kernel that only supports the first or second ABI.

Starting with the Landlock ABI version 3, it is now possible to securely control
truncation thanks to the new `LANDLOCK_ACCESS_FS_TRUNCATE` access right.

### TCP bind and connect (ABI < 4)

Starting with the Landlock ABI version 4, it is now possible to restrict TCP
bind and connect actions to only a set of allowed ports thanks to the new
`LANDLOCK_ACCESS_NET_BIND_TCP` and `LANDLOCK_ACCESS_NET_CONNECT_TCP`
access rights.

### Device IOCTL (ABI < 5)

IOCTL operations could not be denied before the fifth Landlock ABI, so
*ioctl(2)* is always allowed when using a kernel that only supports an
earlier ABI.

Starting with the Landlock ABI version 5, it is possible to restrict the use of
*ioctl(2)* on character and block devices using the new
`LANDLOCK_ACCESS_FS_IOCTL_DEV` right.

### Abstract UNIX socket (ABI < 6)

Starting with the Landlock ABI version 6, it is possible to restrict
connections to an abstract *unix(7)* socket by setting
`LANDLOCK_SCOPE_ABSTRACT_UNIX_SOCKET` to the `scoped` ruleset attribute.

### Signal (ABI < 6)

Starting with the Landlock ABI version 6, it is possible to restrict
*signal(7)* sending by setting `LANDLOCK_SCOPE_SIGNAL` to the
`scoped` ruleset attribute.

### Logging (ABI < 7)

Starting with the Landlock ABI version 7, it is possible to control logging of
Landlock audit events with the `LANDLOCK_RESTRICT_SELF_LOG_SAME_EXEC_OFF`,
`LANDLOCK_RESTRICT_SELF_LOG_NEW_EXEC_ON`, and
`LANDLOCK_RESTRICT_SELF_LOG_SUBDOMAINS_OFF` flags passed to
[`sys_landlock_restrict_self()`](landlock.md#c.sys_landlock_restrict_self "sys_landlock_restrict_self"). See [Landlock: system-wide management](../admin-guide/LSM/landlock.md)
for more details on audit.

## Kernel support

### Build time configuration

Landlock was first introduced in Linux 5.13 but it must be configured at build
time with `CONFIG_SECURITY_LANDLOCK=y`. Landlock must also be enabled at boot
time like other security modules. The list of security modules enabled by
default is set with `CONFIG_LSM`. The kernel configuration should then
contain `CONFIG_LSM=landlock,[...]` with `[...]` as the list of other
potentially useful security modules for the running system (see the
`CONFIG_LSM` help).

### Boot time configuration

If the running kernel does not have `landlock` in `CONFIG_LSM`, then we can
enable Landlock by adding `lsm=landlock,[...]` to
[The kernel’s command-line parameters](../admin-guide/kernel-parameters.md) in the boot loader
configuration.

For example, if the current built-in configuration is:

```console
$ zgrep -h "^CONFIG_LSM=" "/boot/config-$(uname -r)" /proc/config.gz 2>/dev/null
CONFIG_LSM="lockdown,yama,integrity,apparmor"
```

...and if the cmdline doesn’t contain `landlock` either:

```console
$ sed -n 's/.*\(\<lsm=\S\+\).*/\1/p' /proc/cmdline
lsm=lockdown,yama,integrity,apparmor
```

...we should configure the boot loader to set a cmdline extending the `lsm`
list with the `landlock,` prefix:

```
lsm=landlock,lockdown,yama,integrity,apparmor
```

After a reboot, we can check that Landlock is up and running by looking at
kernel logs:

```console
# dmesg | grep landlock || journalctl -kb -g landlock
[    0.000000] Command line: [...] lsm=landlock,lockdown,yama,integrity,apparmor
[    0.000000] Kernel command line: [...] lsm=landlock,lockdown,yama,integrity,apparmor
[    0.000000] LSM: initializing lsm=lockdown,capability,landlock,yama,integrity,apparmor
[    0.000000] landlock: Up and running.
```

The kernel may be configured at build time to always load the `lockdown` and
`capability` LSMs. In that case, these LSMs will appear at the beginning of
the `LSM: initializing` log line as well, even if they are not configured in
the boot loader.

### Network support

To be able to explicitly allow TCP operations (e.g., adding a network rule with
`LANDLOCK_ACCESS_NET_BIND_TCP`), the kernel must support TCP
(`CONFIG_INET=y`). Otherwise, [`sys_landlock_add_rule()`](landlock.md#c.sys_landlock_add_rule "sys_landlock_add_rule") returns an
`EAFNOSUPPORT` error, which can safely be ignored because this kind of TCP
operation is already not possible.

## Questions and answers

### What about user space sandbox managers?

Using user space processes to enforce restrictions on kernel resources can lead
to race conditions or inconsistent evaluations (i.e. [Incorrect mirroring of
the OS code and state](https://www.ndss-symposium.org/ndss2003/traps-and-pitfalls-practical-problems-system-call-interposition-based-security-tools/)).

### What about namespaces and containers?

Namespaces can help create sandboxes but they are not designed for
access-control and then miss useful features for such use case (e.g. no
fine-grained restrictions). Moreover, their complexity can lead to security
issues, especially when untrusted processes can manipulate them (cf.
[Controlling access to user namespaces](https://lwn.net/Articles/673597/)).

### How to disable Landlock audit records?

You might want to put in place filters as explained here:
[Landlock: system-wide management](../admin-guide/LSM/landlock.md)

## Additional documentation

- [Landlock: system-wide management](../admin-guide/LSM/landlock.md)
- [Landlock LSM: kernel documentation](../security/landlock.md)
- <https://landlock.io>

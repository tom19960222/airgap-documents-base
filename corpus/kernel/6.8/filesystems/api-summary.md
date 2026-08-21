---
collection: kernel
version: "6.8"
title: "Linux Filesystems API summary"
source_url: https://www.kernel.org/doc/html/v6.8/filesystems/api-summary.html
fetched_at: 2026-08-21T03:38:14+00:00
---
# Linux Filesystems API summary

This section contains API-level documentation, mostly taken from the source
code itself.

## The Linux VFS

### The Filesystem types

enum positive_aop_returns
:   aop return codes with specific semantics

**Constants**

`AOP_WRITEPAGE_ACTIVATE`
:   Informs the caller that page writeback has
    completed, that the page is still locked, and
    should be considered active. The VM uses this hint
    to return the page to the active list -- it won't
    be a candidate for writeback again in the near
    future. Other callers must be careful to unlock
    the page if they get this return. Returned by
    writepage();

`AOP_TRUNCATED_PAGE`
:   The AOP method that was handed a locked page has
    unlocked it and the page might have been truncated.
    The caller should back up to acquiring a new page and
    trying again. The aop will be taking reasonable
    precautions not to livelock. If the caller held a page
    reference, it should drop it before retrying. Returned
    by read_folio().

**Description**

address_space_operation functions return these large constants to indicate
special semantics to the caller. These are much larger than the bytes in a
page to allow for functions that return the number of bytes operated on in a
given page.

struct address_space
:   Contents of a cacheable, mappable object.

**Definition**:

```
struct address_space {
    struct inode            *host;
    struct xarray           i_pages;
    struct rw_semaphore     invalidate_lock;
    gfp_t gfp_mask;
    atomic_t i_mmap_writable;
#ifdef CONFIG_READ_ONLY_THP_FOR_FS;
    atomic_t nr_thps;
#endif;
    struct rb_root_cached   i_mmap;
    unsigned long           nrpages;
    pgoff_t writeback_index;
    const struct address_space_operations *a_ops;
    unsigned long           flags;
    struct rw_semaphore     i_mmap_rwsem;
    errseq_t wb_err;
    spinlock_t i_private_lock;
    struct list_head        i_private_list;
    void *                  i_private_data;
};
```

**Members**

`host`
:   Owner, either the inode or the block_device.

`i_pages`
:   Cached pages.

`invalidate_lock`
:   Guards coherency between page cache contents and
    file offset->disk block mappings in the filesystem during invalidates.
    It is also used to block modification of page cache contents through
    memory mappings.

`gfp_mask`
:   Memory allocation flags to use for allocating pages.

`i_mmap_writable`
:   Number of VM_SHARED, VM_MAYWRITE mappings.

`nr_thps`
:   Number of THPs in the pagecache (non-shmem only).

`i_mmap`
:   Tree of private and shared mappings.

`nrpages`
:   Number of page entries, protected by the i_pages lock.

`writeback_index`
:   Writeback starts here.

`a_ops`
:   Methods.

`flags`
:   Error bits and flags (AS_\*).

`i_mmap_rwsem`
:   Protects **i_mmap** and **i_mmap_writable**.

`wb_err`
:   The most recent error which has occurred.

`i_private_lock`
:   For use by the owner of the address_space.

`i_private_list`
:   For use by the owner of the address_space.

`i_private_data`
:   For use by the owner of the address_space.

struct file_ra_state
:   Track a file's readahead state.

**Definition**:

```
struct file_ra_state {
    pgoff_t start;
    unsigned int size;
    unsigned int async_size;
    unsigned int ra_pages;
    unsigned int mmap_miss;
    loff_t prev_pos;
};
```

**Members**

`start`
:   Where the most recent readahead started.

`size`
:   Number of pages read in the most recent readahead.

`async_size`
:   Numer of pages that were/are not needed immediately
    and so were/are genuinely "ahead". Start next readahead when
    the first of these pages is accessed.

`ra_pages`
:   Maximum size of a readahead request, copied from the bdi.

`mmap_miss`
:   How many mmap accesses missed in the page cache.

`prev_pos`
:   The last byte in the most recent read request.

**Description**

When this structure is passed to ->readahead(), the "most recent"
readahead means the current readahead.

vfsuid_t i_uid_into_vfsuid(struct mnt_idmap \*idmap, const struct [inode](api-summary.md#c.i_uid_into_vfsuid "inode") \*inode)
:   map an inode's i_uid down according to an idmapping

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`const struct inode *inode`
:   inode to map

**Return**

whe inode's i_uid mapped down according to **idmap**.
If the inode's i_uid has no mapping INVALID_VFSUID is returned.

bool i_uid_needs_update(struct mnt_idmap \*idmap, const struct iattr \*attr, const struct [inode](api-summary.md#c.i_uid_needs_update "inode") \*inode)
:   check whether inode's i_uid needs to be updated

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`const struct iattr *attr`
:   the new attributes of **inode**

`const struct inode *inode`
:   the inode to update

**Description**

Check whether the $inode's i_uid field needs to be updated taking idmapped
mounts into account if the filesystem supports it.

**Return**

true if **inode**'s i_uid field needs to be updated, false if not.

void i_uid_update(struct mnt_idmap \*idmap, const struct iattr \*attr, struct [inode](api-summary.md#c.i_uid_update "inode") \*inode)
:   update **inode**'s i_uid field

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`const struct iattr *attr`
:   the new attributes of **inode**

`struct inode *inode`
:   the inode to update

**Description**

Safely update **inode**'s i_uid field translating the vfsuid of any idmapped
mount into the filesystem kuid.

vfsgid_t i_gid_into_vfsgid(struct mnt_idmap \*idmap, const struct [inode](api-summary.md#c.i_gid_into_vfsgid "inode") \*inode)
:   map an inode's i_gid down according to an idmapping

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`const struct inode *inode`
:   inode to map

**Return**

the inode's i_gid mapped down according to **idmap**.
If the inode's i_gid has no mapping INVALID_VFSGID is returned.

bool i_gid_needs_update(struct mnt_idmap \*idmap, const struct iattr \*attr, const struct [inode](api-summary.md#c.i_gid_needs_update "inode") \*inode)
:   check whether inode's i_gid needs to be updated

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`const struct iattr *attr`
:   the new attributes of **inode**

`const struct inode *inode`
:   the inode to update

**Description**

Check whether the $inode's i_gid field needs to be updated taking idmapped
mounts into account if the filesystem supports it.

**Return**

true if **inode**'s i_gid field needs to be updated, false if not.

void i_gid_update(struct mnt_idmap \*idmap, const struct iattr \*attr, struct [inode](api-summary.md#c.i_gid_update "inode") \*inode)
:   update **inode**'s i_gid field

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`const struct iattr *attr`
:   the new attributes of **inode**

`struct inode *inode`
:   the inode to update

**Description**

Safely update **inode**'s i_gid field translating the vfsgid of any idmapped
mount into the filesystem kgid.

void inode_fsuid_set(struct [inode](api-summary.md#c.inode_fsuid_set "inode") \*inode, struct mnt_idmap \*idmap)
:   initialize inode's i_uid field with callers fsuid

**Parameters**

`struct inode *inode`
:   inode to initialize

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

**Description**

Initialize the i_uid field of **inode**. If the inode was found/created via
an idmapped mount map the caller's fsuid according to **idmap**.

void inode_fsgid_set(struct [inode](api-summary.md#c.inode_fsgid_set "inode") \*inode, struct mnt_idmap \*idmap)
:   initialize inode's i_gid field with callers fsgid

**Parameters**

`struct inode *inode`
:   inode to initialize

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

**Description**

Initialize the i_gid field of **inode**. If the inode was found/created via
an idmapped mount map the caller's fsgid according to **idmap**.

bool fsuidgid_has_mapping(struct super_block \*sb, struct mnt_idmap \*idmap)
:   check whether caller's fsuid/fsgid is mapped

**Parameters**

`struct super_block *sb`
:   the superblock we want a mapping in

`struct mnt_idmap *idmap`
:   idmap of the relevant mount

**Description**

Check whether the caller's fsuid and fsgid have a valid mapping in the
s_user_ns of the superblock **sb**. If the caller is on an idmapped mount map
the caller's fsuid and fsgid according to the **idmap** first.

**Return**

true if fsuid and fsgid is mapped, false if not.

struct timespec64 inode_set_ctime(struct [inode](api-summary.md#c.inode_set_ctime "inode") \*inode, time64_t sec, long nsec)
:   set the ctime in the inode

**Parameters**

`struct inode *inode`
:   inode in which to set the ctime

`time64_t sec`
:   tv_sec value to set

`long nsec`
:   tv_nsec value to set

**Description**

Set the ctime in **inode** to { **sec**, **nsec** }

int __sb_write_started(const struct super_block \*sb, int level)
:   check if sb freeze level is held

**Parameters**

`const struct super_block *sb`
:   the super we write to

`int level`
:   the freeze level

**Description**

- > 0 - sb freeze level is held
- 0 - sb freeze level is not held
- < 0 - !CONFIG_LOCKDEP/LOCK_STATE_UNKNOWN

bool sb_write_started(const struct super_block \*sb)
:   check if SB_FREEZE_WRITE is held

**Parameters**

`const struct super_block *sb`
:   the super we write to

**Description**

May be false positive with !CONFIG_LOCKDEP/LOCK_STATE_UNKNOWN.

bool sb_write_not_started(const struct super_block \*sb)
:   check if SB_FREEZE_WRITE is not held

**Parameters**

`const struct super_block *sb`
:   the super we write to

**Description**

May be false positive with !CONFIG_LOCKDEP/LOCK_STATE_UNKNOWN.

bool file_write_started(const struct [file](api-summary.md#c.file_write_started "file") \*file)
:   check if SB_FREEZE_WRITE is held

**Parameters**

`const struct file *file`
:   the file we write to

**Description**

May be false positive with !CONFIG_LOCKDEP/LOCK_STATE_UNKNOWN.
May be false positive with !S_ISREG, because [`file_start_write()`](api-summary.md#c.file_start_write "file_start_write") has
no effect on !S_ISREG.

bool file_write_not_started(const struct [file](api-summary.md#c.file_write_not_started "file") \*file)
:   check if SB_FREEZE_WRITE is not held

**Parameters**

`const struct file *file`
:   the file we write to

**Description**

May be false positive with !CONFIG_LOCKDEP/LOCK_STATE_UNKNOWN.
May be false positive with !S_ISREG, because [`file_start_write()`](api-summary.md#c.file_start_write "file_start_write") has
no effect on !S_ISREG.

void sb_end_write(struct super_block \*sb)
:   drop write access to a superblock

**Parameters**

`struct super_block *sb`
:   the super we wrote to

**Description**

Decrement number of writers to the filesystem. Wake up possible waiters
wanting to freeze the filesystem.

void sb_end_pagefault(struct super_block \*sb)
:   drop write access to a superblock from a page fault

**Parameters**

`struct super_block *sb`
:   the super we wrote to

**Description**

Decrement number of processes handling write page fault to the filesystem.
Wake up possible waiters wanting to freeze the filesystem.

void sb_end_intwrite(struct super_block \*sb)
:   drop write access to a superblock for internal fs purposes

**Parameters**

`struct super_block *sb`
:   the super we wrote to

**Description**

Decrement fs-internal number of writers to the filesystem. Wake up possible
waiters wanting to freeze the filesystem.

void sb_start_write(struct super_block \*sb)
:   get write access to a superblock

**Parameters**

`struct super_block *sb`
:   the super we write to

**Description**

When a process wants to write data or metadata to a file system (i.e. dirty
a page or an inode), it should embed the operation in a [`sb_start_write()`](api-summary.md#c.sb_start_write "sb_start_write") -
[`sb_end_write()`](api-summary.md#c.sb_end_write "sb_end_write") pair to get exclusion against file system freezing. This
function increments number of writers preventing freezing. If the file
system is already frozen, the function waits until the file system is
thawed.

Since freeze protection behaves as a lock, users have to preserve
ordering of freeze protection and other filesystem locks. Generally,
freeze protection should be the outermost lock. In particular, we have:

sb_start_write
:   -> i_mutex (write path, truncate, directory ops, ...)
    -> s_umount (freeze_super, thaw_super)

void sb_start_pagefault(struct super_block \*sb)
:   get write access to a superblock from a page fault

**Parameters**

`struct super_block *sb`
:   the super we write to

**Description**

When a process starts handling write page fault, it should embed the
operation into [`sb_start_pagefault()`](api-summary.md#c.sb_start_pagefault "sb_start_pagefault") - [`sb_end_pagefault()`](api-summary.md#c.sb_end_pagefault "sb_end_pagefault") pair to get
exclusion against file system freezing. This is needed since the page fault
is going to dirty a page. This function increments number of running page
faults preventing freezing. If the file system is already frozen, the
function waits until the file system is thawed.

Since page fault freeze protection behaves as a lock, users have to preserve
ordering of freeze protection and other filesystem locks. It is advised to
put [`sb_start_pagefault()`](api-summary.md#c.sb_start_pagefault "sb_start_pagefault") close to mmap_lock in lock ordering. Page fault
handling code implies lock dependency:

mmap_lock
:   -> sb_start_pagefault

void sb_start_intwrite(struct super_block \*sb)
:   get write access to a superblock for internal fs purposes

**Parameters**

`struct super_block *sb`
:   the super we write to

**Description**

This is the third level of protection against filesystem freezing. It is
free for use by a filesystem. The only requirement is that it must rank
below sb_start_pagefault.

For example filesystem can call [`sb_start_intwrite()`](api-summary.md#c.sb_start_intwrite "sb_start_intwrite") when starting a
transaction which somewhat eases handling of freezing for internal sources
of filesystem changes (internal fs threads, discarding preallocation on file
close, etc.).

struct renamedata
:   contains all information required for renaming

**Definition**:

```
struct renamedata {
    struct mnt_idmap *old_mnt_idmap;
    struct inode *old_dir;
    struct dentry *old_dentry;
    struct mnt_idmap *new_mnt_idmap;
    struct inode *new_dir;
    struct dentry *new_dentry;
    struct inode **delegated_inode;
    unsigned int flags;
};
```

**Members**

`old_mnt_idmap`
:   idmap of the old mount the inode was found from

`old_dir`
:   parent of source

`old_dentry`
:   source

`new_mnt_idmap`
:   idmap of the new mount the inode was found from

`new_dir`
:   parent of destination

`new_dentry`
:   destination

`delegated_inode`
:   returns an inode needing a delegation break

`flags`
:   rename flags

enum freeze_holder
:   holder of the freeze

**Constants**

`FREEZE_HOLDER_KERNEL`
:   kernel wants to freeze or thaw filesystem

`FREEZE_HOLDER_USERSPACE`
:   userspace wants to freeze or thaw filesystem

`FREEZE_MAY_NEST`
:   whether nesting freeze and thaw requests is allowed

**Description**

Indicate who the owner of the freeze or thaw request is and whether
the freeze needs to be exclusive or can nest.
Without **FREEZE_MAY_NEST**, multiple freeze and thaw requests from the
same holder aren't allowed. It is however allowed to hold a single
**FREEZE_HOLDER_USERSPACE** and a single **FREEZE_HOLDER_KERNEL** freeze at
the same time. This is relied upon by some filesystems during online
repair or similar.

bool is_idmapped_mnt(const struct vfsmount \*mnt)
:   check whether a mount is mapped

**Parameters**

`const struct vfsmount *mnt`
:   the mount to check

**Description**

If **mnt** has an non **nop_mnt_idmap** attached to it then **mnt** is mapped.

**Return**

true if mount is mapped, false if not.

void file_start_write(struct [file](api-summary.md#c.file_start_write "file") \*file)
:   get write access to a superblock for regular file io

**Parameters**

`struct file *file`
:   the file we want to write to

**Description**

This is a variant of [`sb_start_write()`](api-summary.md#c.sb_start_write "sb_start_write") which is a noop on non-regualr file.
Should be matched with a call to [`file_end_write()`](api-summary.md#c.file_end_write "file_end_write").

void file_end_write(struct [file](api-summary.md#c.file_end_write "file") \*file)
:   drop write access to a superblock of a regular file

**Parameters**

`struct file *file`
:   the file we wrote to

**Description**

Should be matched with a call to [`file_start_write()`](api-summary.md#c.file_start_write "file_start_write").

void kiocb_start_write(struct kiocb \*iocb)
:   get write access to a superblock for async file io

**Parameters**

`struct kiocb *iocb`
:   the io context we want to submit the write with

**Description**

This is a variant of [`sb_start_write()`](api-summary.md#c.sb_start_write "sb_start_write") for async io submission.
Should be matched with a call to [`kiocb_end_write()`](api-summary.md#c.kiocb_end_write "kiocb_end_write").

void kiocb_end_write(struct kiocb \*iocb)
:   drop write access to a superblock after async file io

**Parameters**

`struct kiocb *iocb`
:   the io context we sumbitted the write with

**Description**

Should be matched with a call to [`kiocb_start_write()`](api-summary.md#c.kiocb_start_write "kiocb_start_write").

void inode_dio_begin(struct [inode](api-summary.md#c.inode_dio_begin "inode") \*inode)
:   signal start of a direct I/O requests

**Parameters**

`struct inode *inode`
:   inode the direct I/O happens on

**Description**

This is called once we've finished processing a direct I/O request,
and is used to wake up callers waiting for direct I/O to be quiesced.

void inode_dio_end(struct [inode](api-summary.md#c.inode_dio_end "inode") \*inode)
:   signal finish of a direct I/O requests

**Parameters**

`struct inode *inode`
:   inode the direct I/O happens on

**Description**

This is called once we've finished processing a direct I/O request,
and is used to wake up callers waiting for direct I/O to be quiesced.

### The Directory Cache

void d_drop(struct [dentry](api-summary.md#c.d_drop "dentry") \*dentry)
:   drop a dentry

**Parameters**

`struct dentry *dentry`
:   dentry to drop

**Description**

[`d_drop()`](api-summary.md#c.d_drop "d_drop") unhashes the entry from the parent dentry hashes, so that it won't
be found through a VFS lookup any more. Note that this is different from
deleting the dentry - d_delete will try to mark the dentry negative if
possible, giving a successful _negative_ lookup, while d_drop will
just make the cache lookup fail.

[`d_drop()`](api-summary.md#c.d_drop "d_drop") is used mainly for stuff that wants to invalidate a dentry for some
reason (NFS timeouts or autofs deletes).

__d_drop requires dentry->d_lock

___d_drop doesn't mark dentry as "unhashed"
(dentry->d_hash.pprev will be LIST_POISON2, not NULL).

struct dentry \*d_find_any_alias(struct [inode](api-summary.md#c.d_find_any_alias "inode") \*inode)
:   find any alias for a given inode

**Parameters**

`struct inode *inode`
:   inode to find an alias for

**Description**

If any aliases exist for the given inode, take and return a
reference for one of them. If no aliases exist, return `NULL`.

struct dentry \*d_find_alias(struct [inode](api-summary.md#c.d_find_alias "inode") \*inode)
:   grab a hashed alias of inode

**Parameters**

`struct inode *inode`
:   inode in question

**Description**

If inode has a hashed alias, or is a directory and has any alias,
acquire the reference to alias and return it. Otherwise return NULL.
Notice that if inode is a directory there can be only one alias and
it can be unhashed only if it has no children, or if it is the root
of a filesystem, or if the directory was renamed and d_revalidate
was the first vfs operation to notice.

If the inode has an IS_ROOT, DCACHE_DISCONNECTED alias, then prefer
any other hashed alias over that one.

void shrink_dcache_sb(struct super_block \*sb)
:   shrink dcache for a superblock

**Parameters**

`struct super_block *sb`
:   superblock

**Description**

Shrink the dcache for the specified super block. This is used to free
the dcache before unmounting a file system.

int path_has_submounts(const struct path \*parent)
:   check for mounts over a dentry in the current namespace.

**Parameters**

`const struct path *parent`
:   path to check.

**Description**

Return true if the parent or its subdirectories contain
a mount point in the current namespace.

void shrink_dcache_parent(struct dentry \*parent)
:   prune dcache

**Parameters**

`struct dentry *parent`
:   parent of entries to prune

**Description**

Prune the dcache to remove unused children of the parent dentry.

void d_invalidate(struct [dentry](api-summary.md#c.d_invalidate "dentry") \*dentry)
:   detach submounts, prune dcache, and drop

**Parameters**

`struct dentry *dentry`
:   dentry to invalidate (aka detach, prune and drop)

struct dentry \*d_alloc(struct dentry \*parent, const struct qstr \*name)
:   allocate a dcache entry

**Parameters**

`struct dentry * parent`
:   parent of entry to allocate

`const struct qstr *name`
:   qstr of the name

**Description**

Allocates a dentry. It returns `NULL` if there is insufficient memory
available. On a success the dentry is returned. The name passed in is
copied and the copy passed in may be reused after this call.

void d_instantiate(struct dentry \*entry, struct [inode](api-summary.md#c.d_instantiate "inode") \*inode)
:   fill in inode information for a dentry

**Parameters**

`struct dentry *entry`
:   dentry to complete

`struct inode * inode`
:   inode to attach to this dentry

**Description**

Fill in inode information in the entry.

This turns negative dentries into productive full members
of society.

NOTE! This assumes that the inode count has been incremented
(or otherwise set) by the caller to indicate that it is now
in use by the dcache.

struct dentry \*d_obtain_alias(struct [inode](api-summary.md#c.d_obtain_alias "inode") \*inode)
:   find or allocate a DISCONNECTED dentry for a given inode

**Parameters**

`struct inode *inode`
:   inode to allocate the dentry for

**Description**

Obtain a dentry for an inode resulting from NFS filehandle conversion or
similar open by handle operations. The returned dentry may be anonymous,
or may have a full name (if the inode was already in the cache).

When called on a directory inode, we must ensure that the inode only ever
has one dentry. If a dentry is found, that is returned instead of
allocating a new one.

On successful return, the reference to the inode has been transferred
to the dentry. In case of an error the reference on the inode is released.
To make it easier to use in export operations a `NULL` or IS_ERR inode may
be passed in and the error will be propagated to the return value,
with a `NULL` **inode** replaced by ERR_PTR(-ESTALE).

struct dentry \*d_obtain_root(struct [inode](api-summary.md#c.d_obtain_root "inode") \*inode)
:   find or allocate a dentry for a given inode

**Parameters**

`struct inode *inode`
:   inode to allocate the dentry for

**Description**

Obtain an IS_ROOT dentry for the root of a filesystem.

We must ensure that directory inodes only ever have one dentry. If a
dentry is found, that is returned instead of allocating a new one.

On successful return, the reference to the inode has been transferred
to the dentry. In case of an error the reference on the inode is
released. A `NULL` or IS_ERR inode may be passed in and will be the
error will be propagate to the return value, with a `NULL` **inode**
replaced by ERR_PTR(-ESTALE).

struct [dentry](api-summary.md#c.d_add_ci "dentry") \*d_add_ci(struct [dentry](api-summary.md#c.d_add_ci "dentry") \*dentry, struct [inode](api-summary.md#c.d_add_ci "inode") \*inode, struct qstr \*name)
:   lookup or allocate new dentry with case-exact name

**Parameters**

`struct dentry *dentry`
:   the negative dentry that was passed to the parent's lookup func

`struct inode *inode`
:   the inode case-insensitive lookup has found

`struct qstr *name`
:   the case-exact name to be associated with the returned dentry

**Description**

This is to avoid filling the dcache with case-insensitive names to the
same inode, only the actual correct case is stored in the dcache for
case-insensitive filesystems.

For a case-insensitive lookup match and if the case-exact dentry
already exists in the dcache, use it and return it.

If no entry exists with the exact case name, allocate new dentry with
the exact case, and return the spliced entry.

bool d_same_name(const struct [dentry](api-summary.md#c.d_same_name "dentry") \*dentry, const struct [dentry](api-summary.md#c.d_same_name "dentry") \*parent, const struct qstr \*name)
:   compare dentry name with case-exact name

**Parameters**

`const struct dentry *dentry`
:   the negative dentry that was passed to the parent's lookup func

`const struct dentry *parent`
:   parent dentry

`const struct qstr *name`
:   the case-exact name to be associated with the returned dentry

**Return**

true if names are same, or false

struct dentry \*d_lookup(const struct dentry \*parent, const struct qstr \*name)
:   search for a dentry

**Parameters**

`const struct dentry *parent`
:   parent dentry

`const struct qstr *name`
:   qstr of name we wish to find

**Return**

dentry, or NULL

**Description**

d_lookup searches the children of the parent dentry for the name in
question. If the dentry is found its reference count is incremented and the
dentry is returned. The caller must use dput to free the entry when it has
finished using it. `NULL` is returned if the dentry does not exist.

struct dentry \*d_hash_and_lookup(struct dentry \*dir, struct qstr \*name)
:   hash the qstr then search for a dentry

**Parameters**

`struct dentry *dir`
:   Directory to search in

`struct qstr *name`
:   qstr of name we wish to find

**Description**

On lookup failure NULL is returned; on bad name - ERR_PTR(-error)

void d_delete(struct [dentry](api-summary.md#c.d_delete "dentry") \*dentry)
:   delete a dentry

**Parameters**

`struct dentry * dentry`
:   The dentry to delete

**Description**

Turn the dentry into a negative dentry if possible, otherwise
remove it from the hash queues so it can be deleted later

void d_rehash(struct dentry \*entry)
:   add an entry back to the hash

**Parameters**

`struct dentry * entry`
:   dentry to add to the hash

**Description**

Adds a dentry to the hash according to its name.

void d_add(struct dentry \*entry, struct [inode](api-summary.md#c.d_add "inode") \*inode)
:   add dentry to hash queues

**Parameters**

`struct dentry *entry`
:   dentry to add

`struct inode *inode`
:   The inode to attach to this dentry

**Description**

This adds the entry to the hash queues and initializes **inode**.
The entry was actually filled in earlier during [`d_alloc()`](api-summary.md#c.d_alloc "d_alloc").

struct dentry \*d_exact_alias(struct dentry \*entry, struct [inode](api-summary.md#c.d_exact_alias "inode") \*inode)
:   find and hash an exact unhashed alias

**Parameters**

`struct dentry *entry`
:   dentry to add

`struct inode *inode`
:   The inode to go with this dentry

**Description**

If an unhashed dentry with the same name/parent and desired
inode already exists, hash and return it. Otherwise, return
NULL.

Parent directory should be locked.

struct [dentry](api-summary.md#c.d_splice_alias "dentry") \*d_splice_alias(struct [inode](api-summary.md#c.d_splice_alias "inode") \*inode, struct [dentry](api-summary.md#c.d_splice_alias "dentry") \*dentry)
:   splice a disconnected dentry into the tree if one exists

**Parameters**

`struct inode *inode`
:   the inode which may have a disconnected dentry

`struct dentry *dentry`
:   a negative dentry which we want to point to the inode.

**Description**

If inode is a directory and has an IS_ROOT alias, then d_move that in
place of the given dentry and return it, else simply d_add the inode
to the dentry and return NULL.

If a non-IS_ROOT directory is found, the filesystem is corrupt, and
we should error out: directories can't have multiple aliases.

This is needed in the lookup routine of any filesystem that is exportable
(via knfsd) so that we can build dcache paths to directories effectively.

If a dentry was found and moved, then it is returned. Otherwise NULL
is returned. This matches the expected return value of ->lookup.

Cluster filesystems may call this function with a negative, hashed dentry.
In that case, we know that the inode will be a regular file, and also this
will only occur during atomic_open. So we need to check for the dentry
being already hashed only in the final case.

bool is_subdir(struct dentry \*new_dentry, struct dentry \*old_dentry)
:   is new dentry a subdirectory of old_dentry

**Parameters**

`struct dentry *new_dentry`
:   new dentry

`struct dentry *old_dentry`
:   old dentry

**Description**

Returns true if new_dentry is a subdirectory of the parent (at any depth).
Returns false otherwise.
Caller must ensure that "new_dentry" is pinned before calling [`is_subdir()`](api-summary.md#c.is_subdir "is_subdir")

struct [dentry](api-summary.md#c.dget_dlock "dentry") \*dget_dlock(struct [dentry](api-summary.md#c.dget_dlock "dentry") \*dentry)
:   get a reference to a dentry

**Parameters**

`struct dentry *dentry`
:   dentry to get a reference to

**Description**

Given a live dentry, increment the reference count and return the dentry.
Caller must hold **dentry->d_lock**. Making sure that dentry is alive is
caller's resonsibility. There are many conditions sufficient to guarantee
that; e.g. anything with non-negative refcount is alive, so's anything
hashed, anything positive, anyone's parent, etc.

struct [dentry](api-summary.md#c.dget "dentry") \*dget(struct [dentry](api-summary.md#c.dget "dentry") \*dentry)
:   get a reference to a dentry

**Parameters**

`struct dentry *dentry`
:   dentry to get a reference to

**Description**

Given a dentry or `NULL` pointer increment the reference count
if appropriate and return the dentry. A dentry will not be
destroyed when it has references. Conversely, a dentry with
no references can disappear for any number of reasons, starting
with memory pressure. In other words, that primitive is
used to clone an existing reference; using it on something with
zero refcount is a bug.

**NOTE**

it will spin if **dentry->d_lock** is held. From the deadlock
avoidance point of view it is equivalent to spin_lock()/increment
refcount/spin_unlock(), so calling it under **dentry->d_lock** is
always a bug; so's calling it under ->d_lock on any of its descendents.

int d_unhashed(const struct [dentry](api-summary.md#c.d_unhashed "dentry") \*dentry)
:   is dentry hashed

**Parameters**

`const struct dentry *dentry`
:   entry to check

**Description**

Returns true if the dentry passed is not currently hashed.

bool d_really_is_negative(const struct [dentry](api-summary.md#c.d_really_is_negative "dentry") \*dentry)
:   Determine if a dentry is really negative (ignoring fallthroughs)

**Parameters**

`const struct dentry *dentry`
:   The dentry in question

**Description**

Returns true if the dentry represents either an absent name or a name that
doesn't map to an inode (ie. ->d_inode is NULL). The dentry could represent
a true miss, a whiteout that isn't represented by a 0,0 chardev or a
fallthrough marker in an opaque directory.

Note! (1) This should be used *only* by a filesystem to examine its own
dentries. It should not be used to look at some other filesystem's
dentries. (2) It should also be used in combination with [`d_inode()`](api-summary.md#c.d_inode "d_inode") to get
the inode. (3) The dentry may have something attached to ->d_lower and the
type field of the flags may be set to something other than miss or whiteout.

bool d_really_is_positive(const struct [dentry](api-summary.md#c.d_really_is_positive "dentry") \*dentry)
:   Determine if a dentry is really positive (ignoring fallthroughs)

**Parameters**

`const struct dentry *dentry`
:   The dentry in question

**Description**

Returns true if the dentry represents a name that maps to an inode
(ie. ->d_inode is not NULL). The dentry might still represent a whiteout if
that is represented on medium as a 0,0 chardev.

Note! (1) This should be used *only* by a filesystem to examine its own
dentries. It should not be used to look at some other filesystem's
dentries. (2) It should also be used in combination with [`d_inode()`](api-summary.md#c.d_inode "d_inode") to get
the inode.

struct inode \*d_inode(const struct [dentry](api-summary.md#c.d_inode "dentry") \*dentry)
:   Get the actual inode of this dentry

**Parameters**

`const struct dentry *dentry`
:   The dentry to query

**Description**

This is the helper normal filesystems should use to get at their own inodes
in their own dentries and ignore the layering superimposed upon them.

struct inode \*d_inode_rcu(const struct [dentry](api-summary.md#c.d_inode_rcu "dentry") \*dentry)
:   Get the actual inode of this dentry with READ_ONCE()

**Parameters**

`const struct dentry *dentry`
:   The dentry to query

**Description**

This is the helper normal filesystems should use to get at their own inodes
in their own dentries and ignore the layering superimposed upon them.

struct inode \*d_backing_inode(const struct dentry \*upper)
:   Get upper or lower inode we should be using

**Parameters**

`const struct dentry *upper`
:   The upper layer

**Description**

This is the helper that should be used to get at the inode that will be used
if this dentry were to be opened as a file. The inode may be on the upper
dentry or it may be on a lower dentry pinned by the upper.

Normal filesystems should not use this to access their own inodes.

struct [dentry](api-summary.md#c.d_real "dentry") \*d_real(struct [dentry](api-summary.md#c.d_real "dentry") \*dentry, const struct [inode](api-summary.md#c.d_real "inode") \*inode)
:   Return the real dentry

**Parameters**

`struct dentry *dentry`
:   the dentry to query

`const struct inode *inode`
:   inode to select the dentry from multiple layers (can be NULL)

**Description**

If dentry is on a union/overlay, then return the underlying, real dentry.
Otherwise return the dentry itself.

See also: [Overview of the Linux Virtual File System](vfs.md)

struct inode \*d_real_inode(const struct [dentry](api-summary.md#c.d_real_inode "dentry") \*dentry)
:   Return the real inode

**Parameters**

`const struct dentry *dentry`
:   The dentry to query

**Description**

If dentry is on a union/overlay, then return the underlying, real inode.
Otherwise return [`d_inode()`](api-summary.md#c.d_inode "d_inode").

### Inode Handling

int inode_init_always(struct super_block \*sb, struct [inode](api-summary.md#c.inode_init_always "inode") \*inode)
:   perform inode structure initialisation

**Parameters**

`struct super_block *sb`
:   superblock inode belongs to

`struct inode *inode`
:   inode to initialise

**Description**

These are initializations that need to be done on every inode
allocation as the fields are not initialised by slab allocation.

void drop_nlink(struct [inode](api-summary.md#c.drop_nlink "inode") \*inode)
:   directly drop an inode's link count

**Parameters**

`struct inode *inode`
:   inode

**Description**

This is a low-level filesystem helper to replace any
direct filesystem manipulation of i_nlink. In cases
where we are attempting to track writes to the
filesystem, a decrement to zero means an imminent
write when the file is truncated and actually unlinked
on the filesystem.

void clear_nlink(struct [inode](api-summary.md#c.clear_nlink "inode") \*inode)
:   directly zero an inode's link count

**Parameters**

`struct inode *inode`
:   inode

**Description**

This is a low-level filesystem helper to replace any
direct filesystem manipulation of i_nlink. See
[`drop_nlink()`](api-summary.md#c.drop_nlink "drop_nlink") for why we care about i_nlink hitting zero.

void set_nlink(struct [inode](api-summary.md#c.set_nlink "inode") \*inode, unsigned int nlink)
:   directly set an inode's link count

**Parameters**

`struct inode *inode`
:   inode

`unsigned int nlink`
:   new nlink (should be non-zero)

**Description**

This is a low-level filesystem helper to replace any
direct filesystem manipulation of i_nlink.

void inc_nlink(struct [inode](api-summary.md#c.inc_nlink "inode") \*inode)
:   directly increment an inode's link count

**Parameters**

`struct inode *inode`
:   inode

**Description**

This is a low-level filesystem helper to replace any
direct filesystem manipulation of i_nlink. Currently,
it is only here for parity with dec_nlink().

void inode_sb_list_add(struct [inode](api-summary.md#c.inode_sb_list_add "inode") \*inode)
:   add inode to the superblock list of inodes

**Parameters**

`struct inode *inode`
:   inode to add

void __insert_inode_hash(struct [inode](api-summary.md#c.__insert_inode_hash "inode") \*inode, unsigned long hashval)
:   hash an inode

**Parameters**

`struct inode *inode`
:   unhashed inode

`unsigned long hashval`
:   unsigned long value used to locate this object in the
    inode_hashtable.

    > Add an inode to the inode hash for this superblock.

void __remove_inode_hash(struct [inode](api-summary.md#c.__remove_inode_hash "inode") \*inode)
:   remove an inode from the hash

**Parameters**

`struct inode *inode`
:   inode to unhash

    Remove an inode from the superblock.

void evict_inodes(struct super_block \*sb)
:   evict all evictable inodes for a superblock

**Parameters**

`struct super_block *sb`
:   superblock to operate on

**Description**

Make sure that no inodes with zero refcount are retained. This is
called by superblock shutdown after having SB_ACTIVE flag removed,
so any inode reaching zero refcount during or after that call will
be immediately evicted.

struct inode \*new_inode(struct super_block \*sb)
:   obtain an inode

**Parameters**

`struct super_block *sb`
:   superblock

    Allocates a new inode for given superblock. The default gfp_mask
    for allocations related to inode->i_mapping is GFP_HIGHUSER_MOVABLE.
    If HIGHMEM pages are unsuitable or it is known that pages allocated
    for the page cache are not reclaimable or migratable,
    mapping_set_gfp_mask() must be called with suitable flags on the
    newly created inode's mapping

void unlock_new_inode(struct [inode](api-summary.md#c.unlock_new_inode "inode") \*inode)
:   clear the I_NEW state and wake up any waiters

**Parameters**

`struct inode *inode`
:   new inode to unlock

**Description**

Called when the inode is fully initialised to clear the new state of the
inode and wake up anyone waiting for the inode to finish initialisation.

void lock_two_nondirectories(struct inode \*inode1, struct inode \*inode2)
:   take two i_mutexes on non-directory objects

**Parameters**

`struct inode *inode1`
:   first inode to lock

`struct inode *inode2`
:   second inode to lock

**Description**

Lock any non-NULL argument. Passed objects must not be directories.
Zero, one or two objects may be locked by this function.

void unlock_two_nondirectories(struct inode \*inode1, struct inode \*inode2)
:   release locks from [`lock_two_nondirectories()`](api-summary.md#c.lock_two_nondirectories "lock_two_nondirectories")

**Parameters**

`struct inode *inode1`
:   first inode to unlock

`struct inode *inode2`
:   second inode to unlock

struct [inode](api-summary.md#c.inode_insert5 "inode") \*inode_insert5(struct [inode](api-summary.md#c.inode_insert5 "inode") \*inode, unsigned long hashval, int (\*test)(struct [inode](api-summary.md#c.inode_insert5 "inode")\*, void\*), int (\*set)(struct [inode](api-summary.md#c.inode_insert5 "inode")\*, void\*), void \*data)
:   obtain an inode from a mounted file system

**Parameters**

`struct inode *inode`
:   pre-allocated inode to use for insert to cache

`unsigned long hashval`
:   hash value (usually inode number) to get

`int (*test)(struct inode *, void *)`
:   callback used for comparisons between inodes

`int (*set)(struct inode *, void *)`
:   callback used to initialize a new struct inode

`void *data`
:   opaque data pointer to pass to **test** and **set**

**Description**

Search for the inode specified by **hashval** and **data** in the inode cache,
and if present it is return it with an increased reference count. This is
a variant of [`iget5_locked()`](api-summary.md#c.iget5_locked "iget5_locked") for callers that don't want to fail on memory
allocation of inode.

If the inode is not in cache, insert the pre-allocated inode to cache and
return it locked, hashed, and with the I_NEW flag set. The file system gets
to fill it in before unlocking it via [`unlock_new_inode()`](api-summary.md#c.unlock_new_inode "unlock_new_inode").

Note both **test** and **set** are called with the inode_hash_lock held, so can't
sleep.

struct inode \*iget5_locked(struct super_block \*sb, unsigned long hashval, int (\*test)(struct inode\*, void\*), int (\*set)(struct inode\*, void\*), void \*data)
:   obtain an inode from a mounted file system

**Parameters**

`struct super_block *sb`
:   super block of file system

`unsigned long hashval`
:   hash value (usually inode number) to get

`int (*test)(struct inode *, void *)`
:   callback used for comparisons between inodes

`int (*set)(struct inode *, void *)`
:   callback used to initialize a new struct inode

`void *data`
:   opaque data pointer to pass to **test** and **set**

**Description**

Search for the inode specified by **hashval** and **data** in the inode cache,
and if present it is return it with an increased reference count. This is
a generalized version of [`iget_locked()`](api-summary.md#c.iget_locked "iget_locked") for file systems where the inode
number is not sufficient for unique identification of an inode.

If the inode is not in cache, allocate a new inode and return it locked,
hashed, and with the I_NEW flag set. The file system gets to fill it in
before unlocking it via [`unlock_new_inode()`](api-summary.md#c.unlock_new_inode "unlock_new_inode").

Note both **test** and **set** are called with the inode_hash_lock held, so can't
sleep.

struct inode \*iget_locked(struct super_block \*sb, unsigned long ino)
:   obtain an inode from a mounted file system

**Parameters**

`struct super_block *sb`
:   super block of file system

`unsigned long ino`
:   inode number to get

**Description**

Search for the inode specified by **ino** in the inode cache and if present
return it with an increased reference count. This is for file systems
where the inode number is sufficient for unique identification of an inode.

If the inode is not in cache, allocate a new inode and return it locked,
hashed, and with the I_NEW flag set. The file system gets to fill it in
before unlocking it via [`unlock_new_inode()`](api-summary.md#c.unlock_new_inode "unlock_new_inode").

ino_t iunique(struct super_block \*sb, ino_t max_reserved)
:   get a unique inode number

**Parameters**

`struct super_block *sb`
:   superblock

`ino_t max_reserved`
:   highest reserved inode number

    Obtain an inode number that is unique on the system for a given
    superblock. This is used by file systems that have no natural
    permanent inode numbering system. An inode number is returned that
    is higher than the reserved limit but unique.

    BUGS:
    With a large number of inodes live on the file system this function
    currently becomes quite slow.

struct inode \*ilookup5_nowait(struct super_block \*sb, unsigned long hashval, int (\*test)(struct inode\*, void\*), void \*data)
:   search for an inode in the inode cache

**Parameters**

`struct super_block *sb`
:   super block of file system to search

`unsigned long hashval`
:   hash value (usually inode number) to search for

`int (*test)(struct inode *, void *)`
:   callback used for comparisons between inodes

`void *data`
:   opaque data pointer to pass to **test**

**Description**

Search for the inode specified by **hashval** and **data** in the inode cache.
If the inode is in the cache, the inode is returned with an incremented
reference count.

Note2: **test** is called with the inode_hash_lock held, so can't sleep.

**Note**

I_NEW is not waited upon so you have to be very careful what you do
with the returned inode. You probably should be using [`ilookup5()`](api-summary.md#c.ilookup5 "ilookup5") instead.

struct inode \*ilookup5(struct super_block \*sb, unsigned long hashval, int (\*test)(struct inode\*, void\*), void \*data)
:   search for an inode in the inode cache

**Parameters**

`struct super_block *sb`
:   super block of file system to search

`unsigned long hashval`
:   hash value (usually inode number) to search for

`int (*test)(struct inode *, void *)`
:   callback used for comparisons between inodes

`void *data`
:   opaque data pointer to pass to **test**

**Description**

Search for the inode specified by **hashval** and **data** in the inode cache,
and if the inode is in the cache, return the inode with an incremented
reference count. Waits on I_NEW before returning the inode.
returned with an incremented reference count.

This is a generalized version of [`ilookup()`](api-summary.md#c.ilookup "ilookup") for file systems where the
inode number is not sufficient for unique identification of an inode.

**Note**

**test** is called with the inode_hash_lock held, so can't sleep.

struct inode \*ilookup(struct super_block \*sb, unsigned long ino)
:   search for an inode in the inode cache

**Parameters**

`struct super_block *sb`
:   super block of file system to search

`unsigned long ino`
:   inode number to search for

**Description**

Search for the inode **ino** in the inode cache, and if the inode is in the
cache, the inode is returned with an incremented reference count.

struct inode \*find_inode_nowait(struct super_block \*sb, unsigned long hashval, int (\*match)(struct inode\*, unsigned long, void\*), void \*data)
:   find an inode in the inode cache

**Parameters**

`struct super_block *sb`
:   super block of file system to search

`unsigned long hashval`
:   hash value (usually inode number) to search for

`int (*match)(struct inode *, unsigned long, void *)`
:   callback used for comparisons between inodes

`void *data`
:   opaque data pointer to pass to **match**

**Description**

Search for the inode specified by **hashval** and **data** in the inode
cache, where the helper function **match** will return 0 if the inode
does not match, 1 if the inode does match, and -1 if the search
should be stopped. The **match** function must be responsible for
taking the i_lock spin_lock and checking i_state for an inode being
freed or being initialized, and incrementing the reference count
before returning 1. It also must not sleep, since it is called with
the inode_hash_lock spinlock held.

This is a even more generalized version of [`ilookup5()`](api-summary.md#c.ilookup5 "ilookup5") when the
function must never block --- find_inode() can block in
__wait_on_freeing_inode() --- or when the caller can not increment
the reference count because the resulting [`iput()`](api-summary.md#c.iput "iput") might cause an
inode eviction. The tradeoff is that the **match** funtion must be
very carefully implemented.

struct inode \*find_inode_rcu(struct super_block \*sb, unsigned long hashval, int (\*test)(struct inode\*, void\*), void \*data)
:   find an inode in the inode cache

**Parameters**

`struct super_block *sb`
:   Super block of file system to search

`unsigned long hashval`
:   Key to hash

`int (*test)(struct inode *, void *)`
:   Function to test match on an inode

`void *data`
:   Data for test function

**Description**

Search for the inode specified by **hashval** and **data** in the inode cache,
where the helper function **test** will return 0 if the inode does not match
and 1 if it does. The **test** function must be responsible for taking the
i_lock spin_lock and checking i_state for an inode being freed or being
initialized.

If successful, this will return the inode for which the **test** function
returned 1 and NULL otherwise.

The **test** function is not permitted to take a ref on any inode presented.
It is also not permitted to sleep.

The caller must hold the RCU read lock.

struct inode \*find_inode_by_ino_rcu(struct super_block \*sb, unsigned long ino)
:   Find an inode in the inode cache

**Parameters**

`struct super_block *sb`
:   Super block of file system to search

`unsigned long ino`
:   The inode number to match

**Description**

Search for the inode specified by **hashval** and **data** in the inode cache,
where the helper function **test** will return 0 if the inode does not match
and 1 if it does. The **test** function must be responsible for taking the
i_lock spin_lock and checking i_state for an inode being freed or being
initialized.

If successful, this will return the inode for which the **test** function
returned 1 and NULL otherwise.

The **test** function is not permitted to take a ref on any inode presented.
It is also not permitted to sleep.

The caller must hold the RCU read lock.

void iput(struct [inode](api-summary.md#c.iput "inode") \*inode)
:   put an inode

**Parameters**

`struct inode *inode`
:   inode to put

    Puts an inode, dropping its usage count. If the inode use count hits
    zero, the inode is then freed and may also be destroyed.

    Consequently, [`iput()`](api-summary.md#c.iput "iput") can sleep.

int bmap(struct [inode](api-summary.md#c.bmap "inode") \*inode, sector_t \*block)
:   find a block number in a file

**Parameters**

`struct inode *inode`
:   inode owning the block number being requested

`sector_t *block`
:   pointer containing the block to find

    Replaces the value in `*block` with the block number on the device holding
    corresponding to the requested block number in the file.
    That is, asked for block 4 of inode 1 the function will replace the
    4 in `*block`, with disk block relative to the disk start that holds that
    block of the file.

    Returns -EINVAL in case of error, 0 otherwise. If mapping falls into a
    hole, returns 0 and `*block` is also set to 0.

int inode_update_timestamps(struct [inode](api-summary.md#c.inode_update_timestamps "inode") \*inode, int flags)
:   update the timestamps on the inode

**Parameters**

`struct inode *inode`
:   inode to be updated

`int flags`
:   S_\* flags that needed to be updated

**Description**

The update_time function is called when an inode's timestamps need to be
updated for a read or write operation. This function handles updating the
actual timestamps. It's up to the caller to ensure that the inode is marked
dirty appropriately.

In the case where any of S_MTIME, S_CTIME, or S_VERSION need to be updated,
attempt to update all three of them. S_ATIME updates can be handled
independently of the rest.

Returns a set of S_\* flags indicating which values changed.

int generic_update_time(struct [inode](api-summary.md#c.generic_update_time "inode") \*inode, int flags)
:   update the timestamps on the inode

**Parameters**

`struct inode *inode`
:   inode to be updated

`int flags`
:   S_\* flags that needed to be updated

**Description**

The update_time function is called when an inode's timestamps need to be
updated for a read or write operation. In the case where any of S_MTIME, S_CTIME,
or S_VERSION need to be updated we attempt to update all three of them. S_ATIME
updates can be handled done independently of the rest.

Returns a S_\* mask indicating which fields were updated.

int file_remove_privs(struct [file](api-summary.md#c.file_remove_privs "file") \*file)
:   remove special file privileges (suid, capabilities)

**Parameters**

`struct file *file`
:   file to remove privileges from

**Description**

When file is modified by a write or truncation ensure that special
file privileges are removed.

**Return**

0 on success, negative errno on failure.

int file_update_time(struct [file](api-summary.md#c.file_update_time "file") \*file)
:   update mtime and ctime time

**Parameters**

`struct file *file`
:   file accessed

**Description**

Update the mtime and ctime members of an inode and mark the inode for
writeback. Note that this function is meant exclusively for usage in
the file write path of filesystems, and filesystems may choose to
explicitly ignore updates via this function with the _NOCMTIME inode
flag, e.g. for network filesystem where these imestamps are handled
by the server. This can return an error for file systems who need to
allocate space in order to update an inode.

**Return**

0 on success, negative errno on failure.

int file_modified(struct [file](api-summary.md#c.file_modified "file") \*file)
:   handle mandated vfs changes when modifying a file

**Parameters**

`struct file *file`
:   file that was modified

**Description**

When file has been modified ensure that special
file privileges are removed and time settings are updated.

**Context**

Caller must hold the file's inode lock.

**Return**

0 on success, negative errno on failure.

int kiocb_modified(struct kiocb \*iocb)
:   handle mandated vfs changes when modifying a file

**Parameters**

`struct kiocb *iocb`
:   iocb that was modified

**Description**

When file has been modified ensure that special
file privileges are removed and time settings are updated.

**Context**

Caller must hold the file's inode lock.

**Return**

0 on success, negative errno on failure.

void inode_init_owner(struct mnt_idmap \*idmap, struct [inode](api-summary.md#c.inode_init_owner "inode") \*inode, const struct [inode](api-summary.md#c.inode_init_owner "inode") \*dir, umode_t mode)
:   Init uid,gid,mode for new inode according to posix standards

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was created from

`struct inode *inode`
:   New inode

`const struct inode *dir`
:   Directory inode

`umode_t mode`
:   mode of the new inode

**Description**

If the inode has been created through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then take
care to map the inode according to **idmap** before checking permissions
and initializing i_uid and i_gid. On non-idmapped mounts or if permission
checking is to be performed on the raw inode simply pass **nop_mnt_idmap**.

bool inode_owner_or_capable(struct mnt_idmap \*idmap, const struct [inode](api-summary.md#c.inode_owner_or_capable "inode") \*inode)
:   check current task permissions to inode

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`const struct inode *inode`
:   inode being checked

**Description**

Return true if current either has CAP_FOWNER in a namespace with the
inode owner uid mapped, or owns the file.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then take
care to map the inode according to **idmap** before checking permissions.
On non-idmapped mounts or if permission checking is to be performed on the
raw inode simply pass **nop_mnt_idmap**.

void inode_dio_wait(struct [inode](api-summary.md#c.inode_dio_wait "inode") \*inode)
:   wait for outstanding DIO requests to finish

**Parameters**

`struct inode *inode`
:   inode to wait for

**Description**

Waits for all pending direct I/O requests to finish so that we can
proceed with a truncate or equivalent operation.

Must be called under a lock that serializes taking new references
to i_dio_count, usually by inode->i_mutex.

struct timespec64 timestamp_truncate(struct timespec64 t, struct [inode](api-summary.md#c.timestamp_truncate "inode") \*inode)
:   Truncate timespec to a granularity

**Parameters**

`struct timespec64 t`
:   Timespec

`struct inode *inode`
:   inode being updated

**Description**

Truncate a timespec to the granularity supported by the fs
containing the inode. Always rounds down. gran must
not be 0 nor greater than a second (NSEC_PER_SEC, or 10^9 ns).

struct timespec64 current_time(struct [inode](api-summary.md#c.current_time "inode") \*inode)
:   Return FS time

**Parameters**

`struct inode *inode`
:   inode.

**Description**

Return the current time truncated to the time granularity supported by
the fs.

Note that inode and inode->sb cannot be NULL.
Otherwise, the function warns and returns time without truncation.

struct timespec64 inode_set_ctime_current(struct [inode](api-summary.md#c.inode_set_ctime_current "inode") \*inode)
:   set the ctime to current_time

**Parameters**

`struct inode *inode`
:   inode

**Description**

Set the inode->i_ctime to the current value for the inode. Returns
the current value that was assigned to i_ctime.

umode_t mode_strip_sgid(struct mnt_idmap \*idmap, const struct inode \*dir, umode_t mode)
:   handle the sgid bit for non-directories

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was created from

`const struct inode *dir`
:   parent directory inode

`umode_t mode`
:   mode of the file to be created in **dir**

**Description**

If the **mode** of the new file has both the S_ISGID and S_IXGRP bit
raised and **dir** has the S_ISGID bit raised ensure that the caller is
either in the group of the parent directory or they have CAP_FSETID
in their user namespace and are privileged over the parent directory.
In all other cases, strip the S_ISGID bit from **mode**.

**Return**

the new mode to use for the file

void make_bad_inode(struct [inode](api-summary.md#c.make_bad_inode "inode") \*inode)
:   mark an inode bad due to an I/O error

**Parameters**

`struct inode *inode`
:   Inode to mark bad

    When an inode cannot be read due to a media or remote network
    failure this function makes the inode "bad" and causes I/O operations
    on it to fail from this point on.

bool is_bad_inode(struct [inode](api-summary.md#c.is_bad_inode "inode") \*inode)
:   is an inode errored

**Parameters**

`struct inode *inode`
:   inode to test

    Returns true if the inode in question has been marked as bad.

void iget_failed(struct [inode](api-summary.md#c.iget_failed "inode") \*inode)
:   Mark an under-construction inode as dead and release it

**Parameters**

`struct inode *inode`
:   The inode to discard

**Description**

Mark an under-construction inode as dead and release it.

### Registration and Superblocks

void deactivate_locked_super(struct super_block \*s)
:   drop an active reference to superblock

**Parameters**

`struct super_block *s`
:   superblock to deactivate

    Drops an active reference to superblock, converting it into a temporary
    one if there is no other active references left. In that case we
    tell fs driver to shut it down and drop the temporary reference we
    had just acquired.

    Caller holds exclusive lock on superblock; that lock is released.

void deactivate_super(struct super_block \*s)
:   drop an active reference to superblock

**Parameters**

`struct super_block *s`
:   superblock to deactivate

    Variant of [`deactivate_locked_super()`](api-summary.md#c.deactivate_locked_super "deactivate_locked_super"), except that superblock is *not*
    locked by caller. If we are going to drop the final active reference,
    lock will be acquired prior to that.

void retire_super(struct super_block \*sb)
:   prevents superblock from being reused

**Parameters**

`struct super_block *sb`
:   superblock to retire

    The function marks superblock to be ignored in superblock test, which
    prevents it from being reused for any new mounts. If the superblock has
    a private bdi, it also unregisters it, but doesn't reduce the refcount
    of the superblock to prevent potential races. The refcount is reduced
    by [`generic_shutdown_super()`](api-summary.md#c.generic_shutdown_super "generic_shutdown_super"). The function can not be called
    concurrently with [`generic_shutdown_super()`](api-summary.md#c.generic_shutdown_super "generic_shutdown_super"). It is safe to call the
    function multiple times, subsequent calls have no effect.

    The marker will affect the re-use only for block-device-based
    superblocks. Other superblocks will still get marked if this function
    is used, but that will not affect their reusability.

void generic_shutdown_super(struct super_block \*sb)
:   common helper for ->kill_sb()

**Parameters**

`struct super_block *sb`
:   superblock to kill

    [`generic_shutdown_super()`](api-summary.md#c.generic_shutdown_super "generic_shutdown_super") does all fs-independent work on superblock
    shutdown. Typical ->kill_sb() should pick all fs-specific objects
    that need destruction out of superblock, call [`generic_shutdown_super()`](api-summary.md#c.generic_shutdown_super "generic_shutdown_super")
    and release aforementioned objects. Note: dentries and inodes _are_
    taken care of and do not need specific handling.

    Upon calling this function, the filesystem may no longer alter or
    rearrange the set of dentries belonging to this super_block, nor may it
    change the attachments of dentries to inodes.

struct super_block \*sget_fc(struct fs_context \*fc, int (\*test)(struct super_block\*, struct fs_context\*), int (\*set)(struct super_block\*, struct fs_context\*))
:   Find or create a superblock

**Parameters**

`struct fs_context *fc`
:   Filesystem context.

`int (*test)(struct super_block *, struct fs_context *)`
:   Comparison callback

`int (*set)(struct super_block *, struct fs_context *)`
:   Setup callback

**Description**

Create a new superblock or find an existing one.

The **test** callback is used to find a matching existing superblock.
Whether or not the requested parameters in **fc** are taken into account
is specific to the **test** callback that is used. They may even be
completely ignored.

If an extant superblock is matched, it will be returned unless:

1. the namespace the filesystem context **fc** and the extant
   superblock's namespace differ
2. the filesystem context **fc** has requested that reusing an extant
   superblock is not allowed

In both cases EBUSY will be returned.

If no match is made, a new superblock will be allocated and basic
initialisation will be performed (s_type, s_fs_info and s_id will be
set and the **set** callback will be invoked), the superblock will be
published and it will be returned in a partially constructed state
with SB_BORN and SB_ACTIVE as yet unset.

**Return**

On success, an extant or newly created superblock is
:   returned. On failure an error pointer is returned.

struct super_block \*sget(struct file_system_type \*type, int (\*test)(struct super_block\*, void\*), int (\*set)(struct super_block\*, void\*), int flags, void \*data)
:   find or create a superblock

**Parameters**

`struct file_system_type *type`
:   filesystem type superblock should belong to

`int (*test)(struct super_block *,void *)`
:   comparison callback

`int (*set)(struct super_block *,void *)`
:   setup callback

`int flags`
:   mount flags

`void *data`
:   argument to each of them

void iterate_supers_type(struct file_system_type \*type, void (\*f)(struct super_block\*, void\*), void \*arg)
:   call function for superblocks of given type

**Parameters**

`struct file_system_type *type`
:   fs type

`void (*f)(struct super_block *, void *)`
:   function to call

`void *arg`
:   argument to pass to it

    Scans the superblock list and calls given function, passing it
    locked superblock and given argument.

int get_anon_bdev(dev_t \*p)
:   Allocate a block device for filesystems which don't have one.

**Parameters**

`dev_t *p`
:   Pointer to a dev_t.

**Description**

Filesystems which don't use real block devices can call this function
to allocate a virtual block device.

**Context**

Any context. Frequently called while holding sb_lock.

**Return**

0 on success, -EMFILE if there are no anonymous bdevs left
or -ENOMEM if memory allocation failed.

struct super_block \*sget_dev(struct fs_context \*fc, dev_t dev)
:   Find or create a superblock by device number

**Parameters**

`struct fs_context *fc`
:   Filesystem context.

`dev_t dev`
:   device number

**Description**

Find or create a superblock using the provided device number that
will be stored in fc->sget_key.

If an extant superblock is matched, then that will be returned with
an elevated reference count that the caller must transfer or discard.

If no match is made, a new superblock will be allocated and basic
initialisation will be performed (s_type, s_fs_info, s_id, s_dev will
be set). The superblock will be published and it will be returned in
a partially constructed state with SB_BORN and SB_ACTIVE as yet
unset.

**Return**

an existing or newly created superblock on success, an error
:   pointer on failure.

int get_tree_bdev(struct fs_context \*fc, int (\*fill_super)(struct super_block\*, struct fs_context\*))
:   Get a superblock based on a single block device

**Parameters**

`struct fs_context *fc`
:   The filesystem context holding the parameters

`int (*fill_super)(struct super_block *, struct fs_context *)`
:   Helper to initialise a new superblock

int vfs_get_tree(struct fs_context \*fc)
:   Get the mountable root

**Parameters**

`struct fs_context *fc`
:   The superblock configuration context.

**Description**

The filesystem is invoked to get or create a superblock which can then later
be used for mounting. The filesystem places a pointer to the root to be
used for mounting in **fc->root**.

int freeze_super(struct super_block \*sb, enum [freeze_holder](api-summary.md#c.freeze_holder "freeze_holder") who)
:   lock the filesystem and force it into a consistent state

**Parameters**

`struct super_block *sb`
:   the super to lock

`enum freeze_holder who`
:   context that wants to freeze

**Description**

Syncs the super to make sure the filesystem is consistent and calls the fs's
freeze_fs. Subsequent calls to this without first thawing the fs may return
-EBUSY.

**who** should be:
\* `FREEZE_HOLDER_USERSPACE` if userspace wants to freeze the fs;
\* `FREEZE_HOLDER_KERNEL` if the kernel wants to freeze the fs.
\* `FREEZE_MAY_NEST` whether nesting freeze and thaw requests is allowed.

The **who** argument distinguishes between the kernel and userspace trying to
freeze the filesystem. Although there cannot be multiple kernel freezes or
multiple userspace freezes in effect at any given time, the kernel and
userspace can both hold a filesystem frozen. The filesystem remains frozen
until there are no kernel or userspace freezes in effect.

A filesystem may hold multiple devices and thus a filesystems may be
frozen through the block layer via multiple block devices. In this
case the request is marked as being allowed to nest by passing
FREEZE_MAY_NEST. The filesystem remains frozen until all block
devices are unfrozen. If multiple freezes are attempted without
FREEZE_MAY_NEST -EBUSY will be returned.

During this function, sb->s_writers.frozen goes through these values:

SB_UNFROZEN: File system is normal, all writes progress as usual.

SB_FREEZE_WRITE: The file system is in the process of being frozen. New
writes should be blocked, though page faults are still allowed. We wait for
all writes to complete and then proceed to the next stage.

SB_FREEZE_PAGEFAULT: Freezing continues. Now also page faults are blocked
but internal fs threads can still modify the filesystem (although they
should not dirty new pages or inodes), writeback can run etc. After waiting
for all running page faults we sync the filesystem which will clean all
dirty pages and inodes (no new dirty pages or inodes can be created when
sync is running).

SB_FREEZE_FS: The file system is frozen. Now all internal sources of fs
modification are blocked (e.g. XFS preallocation truncation on inode
reclaim). This is usually implemented by blocking new transactions for
filesystems that have them and need this additional guard. After all
internal writers are finished we call ->freeze_fs() to finish filesystem
freezing. Then we transition to SB_FREEZE_COMPLETE state. This state is
mostly auxiliary for filesystems to verify they do not modify frozen fs.

sb->s_writers.frozen is protected by sb->s_umount.

**Return**

If the freeze was successful zero is returned. If the freeze
:   failed a negative error code is returned.

int thaw_super(struct super_block \*sb, enum [freeze_holder](api-summary.md#c.freeze_holder "freeze_holder") who)
:   - unlock filesystem

**Parameters**

`struct super_block *sb`
:   the super to thaw

`enum freeze_holder who`
:   context that wants to freeze

**Description**

Unlocks the filesystem and marks it writeable again after [`freeze_super()`](api-summary.md#c.freeze_super "freeze_super")
if there are no remaining freezes on the filesystem.

**who** should be:
\* `FREEZE_HOLDER_USERSPACE` if userspace wants to thaw the fs;
\* `FREEZE_HOLDER_KERNEL` if the kernel wants to thaw the fs.
\* `FREEZE_MAY_NEST` whether nesting freeze and thaw requests is allowed

A filesystem may hold multiple devices and thus a filesystems may
have been frozen through the block layer via multiple block devices.
The filesystem remains frozen until all block devices are unfrozen.

### File Locks

bool locks_owner_has_blockers(struct file_lock_context \*flctx, fl_owner_t owner)
:   Check for blocking lock requests

**Parameters**

`struct file_lock_context *flctx`
:   file lock context

`fl_owner_t owner`
:   lock owner

**Description**

Return values:
:   `true`: **owner** has at least one blocker
    `false`: **owner** has no blockers

int locks_delete_block(struct file_lock \*waiter)
:   stop waiting for a file lock

**Parameters**

`struct file_lock *waiter`
:   the lock which was waiting

    lockd/nfsd need to disconnect the lock while working on it.

int posix_lock_file(struct file \*filp, struct file_lock \*fl, struct file_lock \*conflock)
:   Apply a POSIX-style lock to a file

**Parameters**

`struct file *filp`
:   The file to apply the lock to

`struct file_lock *fl`
:   The lock to be applied

`struct file_lock *conflock`
:   Place to return a copy of the conflicting lock, if found.

**Description**

Add a POSIX style lock to a file.
We merge adjacent & overlapping locks whenever possible.
POSIX locks are sorted by owner task, then by starting address

Note that if called with an FL_EXISTS argument, the caller may determine
whether or not a lock was successfully freed by testing the return
value for -ENOENT.

int __break_lease(struct [inode](api-summary.md#c.__break_lease "inode") \*inode, unsigned int mode, unsigned int type)
:   revoke all outstanding leases on file

**Parameters**

`struct inode *inode`
:   the inode of the file to return

`unsigned int mode`
:   O_RDONLY: break only write leases; O_WRONLY or O_RDWR:
    break all leases

`unsigned int type`
:   FL_LEASE: break leases and delegations; FL_DELEG: break
    only delegations

    > break_lease (inlined for speed) has checked there already is at least
    > some kind of lock (maybe a lease) on this file. Leases are broken on
    > a call to open() or truncate(). This function can sleep unless you
    > specified `O_NONBLOCK` to your open().

void lease_get_mtime(struct [inode](api-summary.md#c.lease_get_mtime "inode") \*inode, struct timespec64 \*time)
:   update modified time of an inode with exclusive lease

**Parameters**

`struct inode *inode`
:   the inode

`struct timespec64 *time`
:   pointer to a timespec which contains the last modified time

**Description**

This is to force NFS clients to flush their caches for files with
exclusive leases. The justification is that if someone has an
exclusive lease, then they could be modifying it.

int generic_setlease(struct file \*filp, int arg, struct file_lock \*\*flp, void \*\*priv)
:   sets a lease on an open file

**Parameters**

`struct file *filp`
:   file pointer

`int arg`
:   type of lease to obtain

`struct file_lock **flp`
:   input - file_lock to use, output - file_lock inserted

`void **priv`
:   private data for lm_setup (may be NULL if lm_setup
    doesn't require it)

    > The (input) flp->fl_lmops->lm_break function is required
    > by break_lease().

int vfs_setlease(struct file \*filp, int arg, struct file_lock \*\*lease, void \*\*priv)
:   sets a lease on an open file

**Parameters**

`struct file *filp`
:   file pointer

`int arg`
:   type of lease to obtain

`struct file_lock **lease`
:   file_lock to use when adding a lease

`void **priv`
:   private info for lm_setup when adding a lease (may be
    NULL if lm_setup doesn't require it)

**Description**

Call this to establish a lease on the file. The "lease" argument is not
used for F_UNLCK requests and may be NULL. For commands that set or alter
an existing lease, the `(*lease)->fl_lmops->lm_break` operation must be
set; if not, this function will return -ENOLCK (and generate a scary-looking
stack trace).

The "priv" pointer is passed directly to the lm_setup function as-is. It
may be NULL if the lm_setup operation doesn't require it.

int locks_lock_inode_wait(struct [inode](api-summary.md#c.locks_lock_inode_wait "inode") \*inode, struct file_lock \*fl)
:   Apply a lock to an inode

**Parameters**

`struct inode *inode`
:   inode of the file to apply to

`struct file_lock *fl`
:   The lock to be applied

**Description**

Apply a POSIX or FLOCK style lock request to an inode.

int vfs_test_lock(struct file \*filp, struct file_lock \*fl)
:   test file byte range lock

**Parameters**

`struct file *filp`
:   The file to test lock for

`struct file_lock *fl`
:   The lock to test; also used to hold result

**Description**

Returns -ERRNO on failure. Indicates presence of conflicting lock by
setting conf->fl_type to something other than F_UNLCK.

int vfs_lock_file(struct file \*filp, unsigned int cmd, struct file_lock \*fl, struct file_lock \*conf)
:   file byte range lock

**Parameters**

`struct file *filp`
:   The file to apply the lock to

`unsigned int cmd`
:   type of locking operation (F_SETLK, F_GETLK, etc.)

`struct file_lock *fl`
:   The lock to be applied

`struct file_lock *conf`
:   Place to return a copy of the conflicting lock, if found.

**Description**

A caller that doesn't care about the conflicting lock may pass NULL
as the final argument.

If the filesystem defines a private ->lock() method, then **conf** will
be left unchanged; so a caller that cares should initialize it to
some acceptable default.

To avoid blocking kernel daemons, such as lockd, that need to acquire POSIX
locks, the ->lock() interface may return asynchronously, before the lock has
been granted or denied by the underlying filesystem, if (and only if)
lm_grant is set. Additionally EXPORT_OP_ASYNC_LOCK in export_operations
flags need to be set.

Callers expecting ->lock() to return asynchronously will only use F_SETLK,
not F_SETLKW; they will set FL_SLEEP if (and only if) the request is for a
blocking lock. When ->lock() does return asynchronously, it must return
FILE_LOCK_DEFERRED, and call ->lm_grant() when the lock request completes.
If the request is for non-blocking lock the file system should return
FILE_LOCK_DEFERRED then try to get the lock and call the callback routine
with the result. If the request timed out the callback routine will return a
nonzero return code and the file system should release the lock. The file
system is also responsible to keep a corresponding posix lock when it
grants a lock so the VFS can find out which locks are locally held and do
the correct lock cleanup when required.
The underlying filesystem must not drop the kernel lock or call
->lm_grant() before returning to the caller with a FILE_LOCK_DEFERRED
return code.

int vfs_cancel_lock(struct file \*filp, struct file_lock \*fl)
:   file byte range unblock lock

**Parameters**

`struct file *filp`
:   The file to apply the unblock to

`struct file_lock *fl`
:   The lock to be unblocked

**Description**

Used by lock managers to cancel blocked requests

bool vfs_inode_has_locks(struct [inode](api-summary.md#c.vfs_inode_has_locks "inode") \*inode)
:   are any file locks held on **inode**?

**Parameters**

`struct inode *inode`
:   inode to check for locks

**Description**

Return true if there are any FL_POSIX or FL_FLOCK locks currently
set on **inode**.

int posix_lock_inode_wait(struct [inode](api-summary.md#c.posix_lock_inode_wait "inode") \*inode, struct file_lock \*fl)
:   Apply a POSIX-style lock to a file

**Parameters**

`struct inode *inode`
:   inode of file to which lock request should be applied

`struct file_lock *fl`
:   The lock to be applied

**Description**

Apply a POSIX style lock request to an inode.

int fcntl_getlease(struct file \*filp)
:   Enquire what lease is currently active

**Parameters**

`struct file *filp`
:   the file

    The value returned by this function will be one of
    (if no lease break is pending):

    `F_RDLCK` to indicate a shared lease is held.

    `F_WRLCK` to indicate an exclusive lease is held.

    `F_UNLCK` to indicate no lease is held.

    (if a lease break is pending):

    `F_RDLCK` to indicate an exclusive lease needs to be
    :   changed to a shared lease (or removed).

    `F_UNLCK` to indicate the lease needs to be removed.

    XXX: sfr & willy disagree over whether F_INPROGRESS
    should be returned to userspace.

int check_conflicting_open(struct file \*filp, const int arg, int flags)
:   see if the given file points to an inode that has an existing open that would conflict with the desired lease.

**Parameters**

`struct file *filp`
:   file to check

`const int arg`
:   type of lease that we're trying to acquire

`int flags`
:   current lock flags

**Description**

Check to see if there's an existing open fd on this file that would
conflict with the lease we're trying to set.

int fcntl_setlease(unsigned int fd, struct file \*filp, int arg)
:   sets a lease on an open file

**Parameters**

`unsigned int fd`
:   open file descriptor

`struct file *filp`
:   file pointer

`int arg`
:   type of lease to obtain

    Call this fcntl to establish a lease on the file.
    Note that you also need to call `F_SETSIG` to
    receive a signal when the lease is broken.

int flock_lock_inode_wait(struct [inode](api-summary.md#c.flock_lock_inode_wait "inode") \*inode, struct file_lock \*fl)
:   Apply a FLOCK-style lock to a file

**Parameters**

`struct inode *inode`
:   inode of the file to apply to

`struct file_lock *fl`
:   The lock to be applied

**Description**

Apply a FLOCK style lock request to an inode.

long sys_flock(unsigned int fd, unsigned int cmd)
:   - flock() system call.

**Parameters**

`unsigned int fd`
:   the file descriptor to lock.

`unsigned int cmd`
:   the type of lock to apply.

    Apply a `FL_FLOCK` style lock to an open file descriptor.
    The **cmd** can be one of:

    - `LOCK_SH` -- a shared lock.
    - `LOCK_EX` -- an exclusive lock.
    - `LOCK_UN` -- remove an existing lock.
    - `LOCK_MAND` -- a 'mandatory' flock. (DEPRECATED)

    `LOCK_MAND` support has been removed from the kernel.

pid_t locks_translate_pid(struct file_lock \*fl, struct pid_namespace \*ns)
:   translate a file_lock's fl_pid number into a namespace

**Parameters**

`struct file_lock *fl`
:   The file_lock who's fl_pid should be translated

`struct pid_namespace *ns`
:   The namespace into which the pid should be translated

**Description**

Used to translate a fl_pid into a namespace virtual pid number

### Other Functions

void mpage_readahead(struct [readahead_control](../core-api/mm-api.md#c.readahead_control "readahead_control") \*rac, get_block_t get_block)
:   start reads against pages

**Parameters**

`struct readahead_control *rac`
:   Describes which pages to read.

`get_block_t get_block`
:   The filesystem's block mapper function.

**Description**

This function walks the pages and the blocks within each page, building and
emitting large BIOs.

If anything unusual happens, such as:

- encountering a page which has buffers
- encountering a page which has a non-hole after a hole
- encountering a page with non-contiguous blocks

then this code just gives up and calls the buffer_head-based read function.
It does handle a page which has holes at the end - that is a common case:
the end-of-file on blocksize < PAGE_SIZE setups.

BH_Boundary explanation:

There is a problem. The mpage read code assembles several pages, gets all
their disk mappings, and then submits them all. That's fine, but obtaining
the disk mappings may require I/O. Reads of indirect blocks, for example.

So an mpage read of the first 16 blocks of an ext2 file will cause I/O to be
submitted in the following order:

> 12 0 1 2 3 4 5 6 7 8 9 10 11 13 14 15 16

because the indirect block has to be read to get the mappings of blocks
13,14,15,16. Obviously, this impacts performance.

So what we do it to allow the filesystem's get_block() function to set
BH_Boundary when it maps block 11. BH_Boundary says: mapping of the block
after this one will require I/O against a block which is probably close to
this one. So you should push what I/O you have currently accumulated.

This all causes the disk requests to be issued in the correct order.

int mpage_writepages(struct [address_space](api-summary.md#c.address_space "address_space") \*mapping, struct writeback_control \*wbc, get_block_t get_block)
:   walk the list of dirty pages of the given address space & writepage() all of them

**Parameters**

`struct address_space *mapping`
:   address space structure to write

`struct writeback_control *wbc`
:   subtract the number of written pages from **\*wbc->nr_to_write**

`get_block_t get_block`
:   the filesystem's block mapper function.

**Description**

This is a library function, which implements the writepages()
address_space_operation.

int generic_permission(struct mnt_idmap \*idmap, struct [inode](api-summary.md#c.generic_permission "inode") \*inode, int mask)
:   check for access rights on a Posix-like filesystem

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`struct inode *inode`
:   inode to check access rights for

`int mask`
:   right to check for (`MAY_READ`, `MAY_WRITE`, `MAY_EXEC`,
    `MAY_NOT_BLOCK` ...)

**Description**

Used to check for read/write/execute permissions on a file.
We use "fsuid" for this, letting us set arbitrary permissions
for filesystem access without changing the "normal" uids which
are used for other things.

generic_permission is rcu-walk aware. It returns -ECHILD in case an rcu-walk
request cannot be satisfied (eg. requires blocking or too much complexity).
It would then be called again in ref-walk mode.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then take
care to map the inode according to **idmap** before checking permissions.
On non-idmapped mounts or if permission checking is to be performed on the
raw inode simply pass **nop_mnt_idmap**.

int inode_permission(struct mnt_idmap \*idmap, struct [inode](api-summary.md#c.inode_permission "inode") \*inode, int mask)
:   Check for access rights to a given inode

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`struct inode *inode`
:   Inode to check permission on

`int mask`
:   Right to check for (`MAY_READ`, `MAY_WRITE`, `MAY_EXEC`)

**Description**

Check for read/write/execute permissions on an inode. We use fs[ug]id for
this, letting us set arbitrary permissions for filesystem access without
changing the "normal" UIDs which are used for other things.

When checking for MAY_APPEND, MAY_WRITE must also be set in **mask**.

void path_get(const struct [path](api-summary.md#c.path_get "path") \*path)
:   get a reference to a path

**Parameters**

`const struct path *path`
:   path to get the reference to

**Description**

Given a path increment the reference count to the dentry and the vfsmount.

void path_put(const struct [path](api-summary.md#c.path_put "path") \*path)
:   put a reference to a path

**Parameters**

`const struct path *path`
:   path to put the reference to

**Description**

Given a path decrement the reference count to the dentry and the vfsmount.

int vfs_path_parent_lookup(struct [filename](api-summary.md#c.vfs_path_parent_lookup "filename") \*filename, unsigned int flags, struct path \*parent, struct qstr \*last, int \*type, const struct path \*root)
:   lookup a parent path relative to a dentry-vfsmount pair

**Parameters**

`struct filename *filename`
:   filename structure

`unsigned int flags`
:   lookup flags

`struct path *parent`
:   pointer to struct path to fill

`struct qstr *last`
:   last component

`int *type`
:   type of the last component

`const struct path *root`
:   pointer to struct path of the base directory

int vfs_path_lookup(struct [dentry](api-summary.md#c.vfs_path_lookup "dentry") \*dentry, struct vfsmount \*mnt, const char \*name, unsigned int flags, struct [path](api-summary.md#c.vfs_path_lookup "path") \*path)
:   lookup a file path relative to a dentry-vfsmount pair

**Parameters**

`struct dentry *dentry`
:   pointer to dentry of the base directory

`struct vfsmount *mnt`
:   pointer to vfs mount of the base directory

`const char *name`
:   pointer to file name

`unsigned int flags`
:   lookup flags

`struct path *path`
:   pointer to struct path to fill

struct dentry \*try_lookup_one_len(const char \*name, struct dentry \*base, int len)
:   filesystem helper to lookup single pathname component

**Parameters**

`const char *name`
:   pathname component to lookup

`struct dentry *base`
:   base directory to lookup from

`int len`
:   maximum length **len** should be interpreted to

**Description**

Look up a dentry by name in the dcache, returning NULL if it does not
currently exist. The function does not try to create a dentry.

Note that this routine is purely a helper for filesystem usage and should
not be called by generic code.

The caller must hold base->i_mutex.

struct dentry \*lookup_one_len(const char \*name, struct dentry \*base, int len)
:   filesystem helper to lookup single pathname component

**Parameters**

`const char *name`
:   pathname component to lookup

`struct dentry *base`
:   base directory to lookup from

`int len`
:   maximum length **len** should be interpreted to

**Description**

Note that this routine is purely a helper for filesystem usage and should
not be called by generic code.

The caller must hold base->i_mutex.

struct dentry \*lookup_one(struct mnt_idmap \*idmap, const char \*name, struct dentry \*base, int len)
:   filesystem helper to lookup single pathname component

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the lookup is performed from

`const char *name`
:   pathname component to lookup

`struct dentry *base`
:   base directory to lookup from

`int len`
:   maximum length **len** should be interpreted to

**Description**

Note that this routine is purely a helper for filesystem usage and should
not be called by generic code.

The caller must hold base->i_mutex.

struct dentry \*lookup_one_unlocked(struct mnt_idmap \*idmap, const char \*name, struct dentry \*base, int len)
:   filesystem helper to lookup single pathname component

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the lookup is performed from

`const char *name`
:   pathname component to lookup

`struct dentry *base`
:   base directory to lookup from

`int len`
:   maximum length **len** should be interpreted to

**Description**

Note that this routine is purely a helper for filesystem usage and should
not be called by generic code.

Unlike lookup_one_len, it should be called without the parent
i_mutex held, and will take the i_mutex itself if necessary.

struct dentry \*lookup_one_positive_unlocked(struct mnt_idmap \*idmap, const char \*name, struct dentry \*base, int len)
:   filesystem helper to lookup single pathname component

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the lookup is performed from

`const char *name`
:   pathname component to lookup

`struct dentry *base`
:   base directory to lookup from

`int len`
:   maximum length **len** should be interpreted to

**Description**

This helper will yield ERR_PTR(-ENOENT) on negatives. The helper returns
known positive or [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR"). This is what most of the users want.

Note that pinned negative with unlocked parent _can_ become positive at any
time, so callers of [`lookup_one_unlocked()`](api-summary.md#c.lookup_one_unlocked "lookup_one_unlocked") need to be very careful; pinned
positives have >d_inode stable, so this one avoids such problems.

Note that this routine is purely a helper for filesystem usage and should
not be called by generic code.

The helper should be called without i_mutex held.

struct dentry \*lookup_one_len_unlocked(const char \*name, struct dentry \*base, int len)
:   filesystem helper to lookup single pathname component

**Parameters**

`const char *name`
:   pathname component to lookup

`struct dentry *base`
:   base directory to lookup from

`int len`
:   maximum length **len** should be interpreted to

**Description**

Note that this routine is purely a helper for filesystem usage and should
not be called by generic code.

Unlike lookup_one_len, it should be called without the parent
i_mutex held, and will take the i_mutex itself if necessary.

int vfs_create(struct mnt_idmap \*idmap, struct inode \*dir, struct [dentry](api-summary.md#c.vfs_create "dentry") \*dentry, umode_t mode, bool want_excl)
:   create new file

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`struct inode *dir`
:   inode of **dentry**

`struct dentry *dentry`
:   pointer to dentry of the base directory

`umode_t mode`
:   mode of the new file

`bool want_excl`
:   whether the file must not yet exist

**Description**

Create a new file.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then take
care to map the inode according to **idmap** before checking permissions.
On non-idmapped mounts or if permission checking is to be performed on the
raw inode simply pass **nop_mnt_idmap**.

struct file \*kernel_tmpfile_open(struct mnt_idmap \*idmap, const struct path \*parentpath, umode_t mode, int open_flag, const struct [cred](api-summary.md#c.kernel_tmpfile_open "cred") \*cred)
:   open a tmpfile for kernel internal use

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`const struct path *parentpath`
:   path of the base directory

`umode_t mode`
:   mode of the new tmpfile

`int open_flag`
:   flags

`const struct cred *cred`
:   credentials for open

**Description**

Create and open a temporary file. The file is not accounted in nr_files,
hence this is only for kernel internal use, and must not be installed into
file tables or such.

int vfs_mknod(struct mnt_idmap \*idmap, struct inode \*dir, struct [dentry](api-summary.md#c.vfs_mknod "dentry") \*dentry, umode_t mode, dev_t dev)
:   create device node or file

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`struct inode *dir`
:   inode of **dentry**

`struct dentry *dentry`
:   pointer to dentry of the base directory

`umode_t mode`
:   mode of the new device node or file

`dev_t dev`
:   device number of device to create

**Description**

Create a device node or file.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then take
care to map the inode according to **idmap** before checking permissions.
On non-idmapped mounts or if permission checking is to be performed on the
raw inode simply pass **nop_mnt_idmap**.

int vfs_mkdir(struct mnt_idmap \*idmap, struct inode \*dir, struct [dentry](api-summary.md#c.vfs_mkdir "dentry") \*dentry, umode_t mode)
:   create directory

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`struct inode *dir`
:   inode of **dentry**

`struct dentry *dentry`
:   pointer to dentry of the base directory

`umode_t mode`
:   mode of the new directory

**Description**

Create a directory.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then take
care to map the inode according to **idmap** before checking permissions.
On non-idmapped mounts or if permission checking is to be performed on the
raw inode simply pass **nop_mnt_idmap**.

int vfs_rmdir(struct mnt_idmap \*idmap, struct inode \*dir, struct [dentry](api-summary.md#c.vfs_rmdir "dentry") \*dentry)
:   remove directory

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`struct inode *dir`
:   inode of **dentry**

`struct dentry *dentry`
:   pointer to dentry of the base directory

**Description**

Remove a directory.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then take
care to map the inode according to **idmap** before checking permissions.
On non-idmapped mounts or if permission checking is to be performed on the
raw inode simply pass **nop_mnt_idmap**.

int vfs_unlink(struct mnt_idmap \*idmap, struct inode \*dir, struct [dentry](api-summary.md#c.vfs_unlink "dentry") \*dentry, struct inode \*\*delegated_inode)
:   unlink a filesystem object

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`struct inode *dir`
:   parent directory

`struct dentry *dentry`
:   victim

`struct inode **delegated_inode`
:   returns victim inode, if the inode is delegated.

**Description**

The caller must hold dir->i_mutex.

If vfs_unlink discovers a delegation, it will return -EWOULDBLOCK and
return a reference to the inode in delegated_inode. The caller
should then break the delegation on that inode and retry. Because
breaking a delegation may take a long time, the caller should drop
dir->i_mutex before doing so.

Alternatively, a caller may pass NULL for delegated_inode. This may
be appropriate for callers that expect the underlying filesystem not
to be NFS exported.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then take
care to map the inode according to **idmap** before checking permissions.
On non-idmapped mounts or if permission checking is to be performed on the
raw inode simply pass **nop_mnt_idmap**.

int vfs_symlink(struct mnt_idmap \*idmap, struct inode \*dir, struct [dentry](api-summary.md#c.vfs_symlink "dentry") \*dentry, const char \*oldname)
:   create symlink

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`struct inode *dir`
:   inode of **dentry**

`struct dentry *dentry`
:   pointer to dentry of the base directory

`const char *oldname`
:   name of the file to link to

**Description**

Create a symlink.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then take
care to map the inode according to **idmap** before checking permissions.
On non-idmapped mounts or if permission checking is to be performed on the
raw inode simply pass **nop_mnt_idmap**.

int vfs_link(struct dentry \*old_dentry, struct mnt_idmap \*idmap, struct inode \*dir, struct dentry \*new_dentry, struct inode \*\*delegated_inode)
:   create a new link

**Parameters**

`struct dentry *old_dentry`
:   object to be linked

`struct mnt_idmap *idmap`
:   idmap of the mount

`struct inode *dir`
:   new parent

`struct dentry *new_dentry`
:   where to create the new link

`struct inode **delegated_inode`
:   returns inode needing a delegation break

**Description**

The caller must hold dir->i_mutex

If vfs_link discovers a delegation on the to-be-linked file in need
of breaking, it will return -EWOULDBLOCK and return a reference to the
inode in delegated_inode. The caller should then break the delegation
and retry. Because breaking a delegation may take a long time, the
caller should drop the i_mutex before doing so.

Alternatively, a caller may pass NULL for delegated_inode. This may
be appropriate for callers that expect the underlying filesystem not
to be NFS exported.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then take
care to map the inode according to **idmap** before checking permissions.
On non-idmapped mounts or if permission checking is to be performed on the
raw inode simply pass **nop_mnt_idmap**.

int vfs_rename(struct [renamedata](api-summary.md#c.renamedata "renamedata") \*rd)
:   rename a filesystem object

**Parameters**

`struct renamedata *rd`
:   pointer to [`struct renamedata`](api-summary.md#c.renamedata "renamedata") info

**Description**

The caller must hold multiple mutexes--see lock_rename()).

If vfs_rename discovers a delegation in need of breaking at either
the source or destination, it will return -EWOULDBLOCK and return a
reference to the inode in delegated_inode. The caller should then
break the delegation and retry. Because breaking a delegation may
take a long time, the caller should drop all locks before doing
so.

Alternatively, a caller may pass NULL for delegated_inode. This may
be appropriate for callers that expect the underlying filesystem not
to be NFS exported.

The worst of all namespace operations - renaming directory. "Perverted"
doesn't even start to describe it. Somebody in UCB had a heck of a trip...
Problems:

> 1. we can get into loop creation.
> 2. race potential - two innocent renames can create a loop together.
>    That's where 4.4BSD screws up. Current fix: serialization on
>    sb->s_vfs_rename_mutex. We might be more accurate, but that's another
>    story.
> 3. we may have to lock up to _four_ objects - parents and victim (if it exists),
>    and source (if it's a non-directory or a subdirectory that moves to
>    different parent).
>    And that - after we got ->i_mutex on parents (until then we don't know
>    whether the target exists). Solution: try to be smart with locking
>    order for inodes. We rely on the fact that tree topology may change
>    only under ->s_vfs_rename_mutex _and_ that parent of the object we
>    move will be locked. Thus we can rank directories by the tree
>    (ancestors first) and rank all non-directories after them.
>    That works since everybody except rename does "lock parent, lookup,
>    lock child" and rename is under ->s_vfs_rename_mutex.
>    HOWEVER, it relies on the assumption that any object with ->lookup()
>    has no more than 1 dentry. If "hybrid" objects will ever appear,
>    we'd better make sure that there's no link(2) for them.
> 4. conversion from fhandle to dentry may come in the wrong moment - when
>    we are removing the target. Solution: we will have to grab ->i_mutex
>    in the fhandle_to_dentry code. [FIXME - current nfsfh.c relies on
>    ->i_mutex on parents, which works but leads to some truly excessive
>    locking].

int vfs_readlink(struct [dentry](api-summary.md#c.vfs_readlink "dentry") \*dentry, char __user \*buffer, int buflen)
:   copy symlink body into userspace buffer

**Parameters**

`struct dentry *dentry`
:   dentry on which to get symbolic link

`char __user *buffer`
:   user memory pointer

`int buflen`
:   size of buffer

**Description**

Does not touch atime. That's up to the caller if necessary

Does not call security hook.

const char \*vfs_get_link(struct [dentry](api-summary.md#c.vfs_get_link "dentry") \*dentry, struct delayed_call \*done)
:   get symlink body

**Parameters**

`struct dentry *dentry`
:   dentry on which to get symbolic link

`struct delayed_call *done`
:   caller needs to free returned data with this

**Description**

Calls security hook and i_op->get_link() on the supplied inode.

It does not touch atime. That's up to the caller if necessary.

Does not work on "special" symlinks like /proc/$$/fd/N

int sync_mapping_buffers(struct [address_space](api-summary.md#c.address_space "address_space") \*mapping)
:   write out & wait upon a mapping's "associated" buffers

**Parameters**

`struct address_space *mapping`
:   the mapping which wants those buffers written

**Description**

Starts I/O against the buffers at mapping->i_private_list, and waits upon
that I/O.

Basically, this is a convenience function for fsync().
**mapping** is a file or directory which needs those buffers to be written for
a successful fsync().

int generic_buffers_fsync_noflush(struct [file](api-summary.md#c.generic_buffers_fsync_noflush "file") \*file, loff_t start, loff_t end, bool datasync)
:   generic buffer fsync implementation for simple filesystems with no inode lock

**Parameters**

`struct file *file`
:   file to synchronize

`loff_t start`
:   start offset in bytes

`loff_t end`
:   end offset in bytes (inclusive)

`bool datasync`
:   only synchronize essential metadata if true

**Description**

This is a generic implementation of the fsync method for simple
filesystems which track all non-inode metadata in the buffers list
hanging off the address_space structure.

int generic_buffers_fsync(struct [file](api-summary.md#c.generic_buffers_fsync "file") \*file, loff_t start, loff_t end, bool datasync)
:   generic buffer fsync implementation for simple filesystems with no inode lock

**Parameters**

`struct file *file`
:   file to synchronize

`loff_t start`
:   start offset in bytes

`loff_t end`
:   end offset in bytes (inclusive)

`bool datasync`
:   only synchronize essential metadata if true

**Description**

This is a generic implementation of the fsync method for simple
filesystems which track all non-inode metadata in the buffers list
hanging off the address_space structure. This also makes sure that
a device cache flush operation is called at the end.

void mark_buffer_dirty(struct buffer_head \*bh)
:   mark a buffer_head as needing writeout

**Parameters**

`struct buffer_head *bh`
:   the buffer_head to mark dirty

**Description**

[`mark_buffer_dirty()`](api-summary.md#c.mark_buffer_dirty "mark_buffer_dirty") will set the dirty bit against the buffer, then set
its backing page dirty, then tag the page as dirty in the page cache
and then attach the address_space's inode to its superblock's dirty
inode list.

[`mark_buffer_dirty()`](api-summary.md#c.mark_buffer_dirty "mark_buffer_dirty") is atomic. It takes bh->b_folio->mapping->i_private_lock,
i_pages lock and mapping->host->i_lock.

struct buffer_head \*bdev_getblk(struct block_device \*bdev, sector_t block, unsigned size, gfp_t gfp)
:   Get a buffer_head in a block device's buffer cache.

**Parameters**

`struct block_device *bdev`
:   The block device.

`sector_t block`
:   The block number.

`unsigned size`
:   The size of buffer_heads for this **bdev**.

`gfp_t gfp`
:   The memory allocation flags to use.

**Return**

The buffer head, or NULL if memory could not be allocated.

struct buffer_head \*__bread_gfp(struct block_device \*bdev, sector_t block, unsigned size, gfp_t gfp)
:   reads a specified block and returns the bh

**Parameters**

`struct block_device *bdev`
:   the block_device to read from

`sector_t block`
:   number of block

`unsigned size`
:   size (in bytes) to read

`gfp_t gfp`
:   page allocation flag

    Reads a specified block, and returns buffer head that contains it.
    The page cache can be allocated from non-movable area
    not to prevent page migration if you set gfp to zero.
    It returns NULL if the block was unreadable.

void block_invalidate_folio(struct [folio](api-summary.md#c.block_invalidate_folio "folio") \*folio, size_t offset, size_t length)
:   Invalidate part or all of a buffer-backed folio.

**Parameters**

`struct folio *folio`
:   The folio which is affected.

`size_t offset`
:   start of the range to invalidate

`size_t length`
:   length of the range to invalidate

**Description**

[`block_invalidate_folio()`](api-summary.md#c.block_invalidate_folio "block_invalidate_folio") is called when all or part of the folio has been
invalidated by a truncate operation.

[`block_invalidate_folio()`](api-summary.md#c.block_invalidate_folio "block_invalidate_folio") does not have to release all buffers, but it must
ensure that no dirty buffer is left outside **offset** and that no I/O
is underway against any of the blocks which are outside the truncation
point. Because the caller is about to free (and possibly reuse) those
blocks on-disk.

void clean_bdev_aliases(struct block_device \*bdev, sector_t block, sector_t len)
:   clean a range of buffers in block device

**Parameters**

`struct block_device *bdev`
:   Block device to clean buffers in

`sector_t block`
:   Start of a range of blocks to clean

`sector_t len`
:   Number of blocks to clean

**Description**

We are taking a range of blocks for data and we don't want writeback of any
buffer-cache aliases starting from return from this function and until the
moment when something will explicitly mark the buffer dirty (hopefully that
will not happen until we will free that block ;-) We don't even need to mark
it not-uptodate - nobody can expect anything from a newly allocated buffer
anyway. We used to use unmap_buffer() for such invalidation, but that was
wrong. We definitely don't want to mark the alias unmapped, for example - it
would confuse anyone who might pick it with bread() afterwards...

Also.. Note that bforget() doesn't lock the buffer. So there can be
writeout I/O going on against recently-freed buffers. We don't wait on that
I/O in bforget() - it's more efficient to wait on the I/O only if we really
need to. That happens here.

int bh_uptodate_or_lock(struct buffer_head \*bh)
:   Test whether the buffer is uptodate

**Parameters**

`struct buffer_head *bh`
:   struct buffer_head

**Description**

Return true if the buffer is up-to-date and false,
with the buffer locked, if not.

int __bh_read(struct buffer_head \*bh, blk_opf_t op_flags, bool wait)
:   Submit read for a locked buffer

**Parameters**

`struct buffer_head *bh`
:   struct buffer_head

`blk_opf_t op_flags`
:   appending REQ_OP_\* flags besides REQ_OP_READ

`bool wait`
:   wait until reading finish

**Description**

Returns zero on success or don't wait, and -EIO on error.

void __bh_read_batch(int nr, struct buffer_head \*bhs[], blk_opf_t op_flags, bool force_lock)
:   Submit read for a batch of unlocked buffers

**Parameters**

`int nr`
:   entry number of the buffer batch

`struct buffer_head *bhs[]`
:   a batch of struct buffer_head

`blk_opf_t op_flags`
:   appending REQ_OP_\* flags besides REQ_OP_READ

`bool force_lock`
:   force to get a lock on the buffer if set, otherwise drops any
    buffer that cannot lock.

**Description**

Returns zero on success or don't wait, and -EIO on error.

void bio_reset(struct [bio](api-summary.md#c.bio_reset "bio") \*bio, struct block_device \*bdev, blk_opf_t opf)
:   reinitialize a bio

**Parameters**

`struct bio *bio`
:   bio to reset

`struct block_device *bdev`
:   block device to use the bio for

`blk_opf_t opf`
:   operation and flags for bio

**Description**

> After calling [`bio_reset()`](api-summary.md#c.bio_reset "bio_reset"), **bio** will be in the same state as a freshly
> allocated bio returned bio [`bio_alloc_bioset()`](api-summary.md#c.bio_alloc_bioset "bio_alloc_bioset") - the only fields that are
> preserved are the ones that are initialized by [`bio_alloc_bioset()`](api-summary.md#c.bio_alloc_bioset "bio_alloc_bioset"). See
> comment in struct bio.

void bio_chain(struct [bio](api-summary.md#c.bio_chain "bio") \*bio, struct [bio](api-summary.md#c.bio_chain "bio") \*parent)
:   chain bio completions

**Parameters**

`struct bio *bio`
:   the target bio

`struct bio *parent`
:   the parent bio of **bio**

**Description**

The caller won't have a bi_end_io called when **bio** completes - instead,
**parent**'s bi_end_io won't be called until both **parent** and **bio** have
completed; the chained bio will also be freed when it completes.

The caller must not set bi_private or bi_end_io in **bio**.

struct bio \*bio_alloc_bioset(struct block_device \*bdev, unsigned short nr_vecs, blk_opf_t opf, gfp_t gfp_mask, struct bio_set \*bs)
:   allocate a bio for I/O

**Parameters**

`struct block_device *bdev`
:   block device to allocate the bio for (can be `NULL`)

`unsigned short nr_vecs`
:   number of bvecs to pre-allocate

`blk_opf_t opf`
:   operation and flags for bio

`gfp_t gfp_mask`
:   the GFP_\* mask given to the slab allocator

`struct bio_set *bs`
:   the bio_set to allocate from.

**Description**

Allocate a bio from the mempools in **bs**.

If `__GFP_DIRECT_RECLAIM` is set then bio_alloc will always be able to
allocate a bio. This is due to the mempool guarantees. To make this work,
callers must never allocate more than 1 bio at a time from the general pool.
Callers that need to allocate more than 1 bio must always submit the
previously allocated bio for IO before attempting to allocate a new one.
Failure to do so can cause deadlocks under memory pressure.

Note that when running under [`submit_bio_noacct()`](../core-api/kernel-api.md#c.submit_bio_noacct "submit_bio_noacct") (i.e. any block driver),
bios are not submitted until after you return - see the code in
[`submit_bio_noacct()`](../core-api/kernel-api.md#c.submit_bio_noacct "submit_bio_noacct") that converts recursion into iteration, to prevent
stack overflows.

This would normally mean allocating multiple bios under [`submit_bio_noacct()`](../core-api/kernel-api.md#c.submit_bio_noacct "submit_bio_noacct")
would be susceptible to deadlocks, but we have
deadlock avoidance code that resubmits any blocked bios from a rescuer
thread.

However, we do not guarantee forward progress for allocations from other
mempools. Doing multiple allocations from the same mempool under
[`submit_bio_noacct()`](../core-api/kernel-api.md#c.submit_bio_noacct "submit_bio_noacct") should be avoided - instead, use bio_set's front_pad
for per bio allocations.

**Return**

Pointer to new bio on success, NULL on failure.

struct bio \*bio_kmalloc(unsigned short nr_vecs, gfp_t gfp_mask)
:   kmalloc a bio

**Parameters**

`unsigned short nr_vecs`
:   number of bio_vecs to allocate

`gfp_t gfp_mask`
:   the GFP_\* mask given to the slab allocator

**Description**

Use kmalloc to allocate a bio (including bvecs). The bio must be initialized
using bio_init() before use. To free a bio returned from this function use
[`kfree()`](../core-api/mm-api.md#c.kfree "kfree") after calling bio_uninit(). A bio returned from this function can
be reused by calling bio_uninit() before calling bio_init() again.

Note that unlike bio_alloc() or [`bio_alloc_bioset()`](api-summary.md#c.bio_alloc_bioset "bio_alloc_bioset") allocations from this
function are not backed by a mempool can fail. Do not use this function
for allocations in the file system I/O path.

**Return**

Pointer to new bio on success, NULL on failure.

void bio_put(struct [bio](api-summary.md#c.bio_put "bio") \*bio)
:   release a reference to a bio

**Parameters**

`struct bio *bio`
:   bio to release reference to

**Description**

> Put a reference to a `struct bio`, either one you have gotten with
> bio_alloc, bio_get or bio_clone_\*. The last put of a bio will free it.

struct bio \*bio_alloc_clone(struct block_device \*bdev, struct bio \*bio_src, gfp_t gfp, struct bio_set \*bs)
:   clone a bio that shares the original bio's biovec

**Parameters**

`struct block_device *bdev`
:   block_device to clone onto

`struct bio *bio_src`
:   bio to clone from

`gfp_t gfp`
:   allocation priority

`struct bio_set *bs`
:   bio_set to allocate from

**Description**

Allocate a new bio that is a clone of **bio_src**. The caller owns the returned
bio, but not the actual data it points to.

The caller must ensure that the return bio is not freed before **bio_src**.

int bio_init_clone(struct block_device \*bdev, struct [bio](api-summary.md#c.bio_init_clone "bio") \*bio, struct [bio](api-summary.md#c.bio_init_clone "bio") \*bio_src, gfp_t gfp)
:   clone a bio that shares the original bio's biovec

**Parameters**

`struct block_device *bdev`
:   block_device to clone onto

`struct bio *bio`
:   bio to clone into

`struct bio *bio_src`
:   bio to clone from

`gfp_t gfp`
:   allocation priority

**Description**

Initialize a new bio in caller provided memory that is a clone of **bio_src**.
The caller owns the returned bio, but not the actual data it points to.

The caller must ensure that **bio_src** is not freed before **bio**.

int bio_add_pc_page(struct request_queue \*q, struct [bio](api-summary.md#c.bio_add_pc_page "bio") \*bio, struct [page](api-summary.md#c.bio_add_pc_page "page") \*page, unsigned int len, unsigned int offset)
:   attempt to add page to passthrough bio

**Parameters**

`struct request_queue *q`
:   the target queue

`struct bio *bio`
:   destination bio

`struct page *page`
:   page to add

`unsigned int len`
:   vec entry length

`unsigned int offset`
:   vec entry offset

**Description**

Attempt to add a page to the bio_vec maplist. This can fail for a
number of reasons, such as the bio being full or target block device
limitations. The target block device must allow bio's up to PAGE_SIZE,
so it is always possible to add a single page to an empty bio.

This should only be used by passthrough bios.

int bio_add_zone_append_page(struct [bio](api-summary.md#c.bio_add_zone_append_page "bio") \*bio, struct [page](api-summary.md#c.bio_add_zone_append_page "page") \*page, unsigned int len, unsigned int offset)
:   attempt to add page to zone-append bio

**Parameters**

`struct bio *bio`
:   destination bio

`struct page *page`
:   page to add

`unsigned int len`
:   vec entry length

`unsigned int offset`
:   vec entry offset

**Description**

Attempt to add a page to the bio_vec maplist of a bio that will be submitted
for a zone-append request. This can fail for a number of reasons, such as the
bio being full or the target block device is not a zoned block device or
other limitations of the target block device. The target block device must
allow bio's up to PAGE_SIZE, so it is always possible to add a single page
to an empty bio.

**Return**

number of bytes added to the bio, or 0 in case of a failure.

void __bio_add_page(struct [bio](api-summary.md#c.__bio_add_page "bio") \*bio, struct [page](api-summary.md#c.__bio_add_page "page") \*page, unsigned int len, unsigned int off)
:   add page(s) to a bio in a new segment

**Parameters**

`struct bio *bio`
:   destination bio

`struct page *page`
:   start page to add

`unsigned int len`
:   length of the data to add, may cross pages

`unsigned int off`
:   offset of the data relative to **page**, may cross pages

**Description**

Add the data at **page** + **off** to **bio** as a new bvec. The caller must ensure
that **bio** has space for another bvec.

int bio_add_page(struct [bio](api-summary.md#c.bio_add_page "bio") \*bio, struct [page](api-summary.md#c.bio_add_page "page") \*page, unsigned int len, unsigned int offset)
:   attempt to add page(s) to bio

**Parameters**

`struct bio *bio`
:   destination bio

`struct page *page`
:   start page to add

`unsigned int len`
:   vec entry length, may cross pages

`unsigned int offset`
:   vec entry offset relative to **page**, may cross pages

    Attempt to add page(s) to the bio_vec maplist. This will only fail
    if either bio->bi_vcnt == bio->bi_max_vecs or it's a cloned bio.

bool bio_add_folio(struct [bio](api-summary.md#c.bio_add_folio "bio") \*bio, struct [folio](api-summary.md#c.bio_add_folio "folio") \*folio, size_t len, size_t off)
:   Attempt to add part of a folio to a bio.

**Parameters**

`struct bio *bio`
:   BIO to add to.

`struct folio *folio`
:   Folio to add.

`size_t len`
:   How many bytes from the folio to add.

`size_t off`
:   First byte in this folio to add.

**Description**

Filesystems that use folios can call this function instead of calling
[`bio_add_page()`](api-summary.md#c.bio_add_page "bio_add_page") for each page in the folio. If **off** is bigger than
PAGE_SIZE, this function can create a bio_vec that starts in a page
after the bv_page. BIOs do not support folios that are 4GiB or larger.

**Return**

Whether the addition was successful.

int bio_iov_iter_get_pages(struct [bio](api-summary.md#c.bio_iov_iter_get_pages "bio") \*bio, struct iov_iter \*iter)
:   add user or kernel pages to a bio

**Parameters**

`struct bio *bio`
:   bio to add pages to

`struct iov_iter *iter`
:   iov iterator describing the region to be added

**Description**

This takes either an iterator pointing to user memory, or one pointing to
kernel pages (BVEC iterator). If we're adding user pages, we pin them and
map them into the kernel. On IO completion, the caller should put those
pages. For bvec based iterators [`bio_iov_iter_get_pages()`](api-summary.md#c.bio_iov_iter_get_pages "bio_iov_iter_get_pages") uses the provided
bvecs rather than copying them. Hence anyone issuing kiocb based IO needs
to ensure the bvecs and pages stay referenced until the submitted I/O is
completed by a call to ->ki_complete() or returns with an error other than
-EIOCBQUEUED. The caller needs to check if the bio is flagged BIO_NO_PAGE_REF
on IO completion. If it isn't, then pages should be released.

The function tries, but does not guarantee, to pin as many pages as
fit into the bio, or are requested in **iter**, whatever is smaller. If
MM encounters an error pinning the requested pages, it stops. Error
is returned only if 0 pages could be pinned.

int submit_bio_wait(struct [bio](api-summary.md#c.submit_bio_wait "bio") \*bio)
:   submit a bio, and wait until it completes

**Parameters**

`struct bio *bio`
:   The `struct bio` which describes the I/O

**Description**

Simple wrapper around [`submit_bio()`](../core-api/kernel-api.md#c.submit_bio "submit_bio"). Returns 0 on success, or the error from
[`bio_endio()`](api-summary.md#c.bio_endio "bio_endio") on failure.

WARNING: Unlike to how [`submit_bio()`](../core-api/kernel-api.md#c.submit_bio "submit_bio") is usually used, this function does not
result in bio reference to be consumed. The caller must drop the reference
on his own.

void bio_copy_data(struct bio \*dst, struct bio \*src)
:   copy contents of data buffers from one bio to another

**Parameters**

`struct bio *dst`
:   destination bio

`struct bio *src`
:   source bio

**Description**

Stops when it reaches the end of either **src** or **dst** - that is, copies
min(src->bi_size, dst->bi_size) bytes (or the equivalent for lists of bios).

void bio_endio(struct [bio](api-summary.md#c.bio_endio "bio") \*bio)
:   end I/O on a bio

**Parameters**

`struct bio *bio`
:   bio

**Description**

> [`bio_endio()`](api-summary.md#c.bio_endio "bio_endio") will end I/O on the whole bio. [`bio_endio()`](api-summary.md#c.bio_endio "bio_endio") is the preferred
> way to end I/O on a bio. No one should call bi_end_io() directly on a
> bio unless they own it and thus know that it has an end_io function.
>
> [`bio_endio()`](api-summary.md#c.bio_endio "bio_endio") can be called several times on a bio that has been chained
> using [`bio_chain()`](api-summary.md#c.bio_chain "bio_chain"). The ->bi_end_io() function will only be called the
> last time.

struct [bio](api-summary.md#c.bio_split "bio") \*bio_split(struct [bio](api-summary.md#c.bio_split "bio") \*bio, int sectors, gfp_t gfp, struct bio_set \*bs)
:   split a bio

**Parameters**

`struct bio *bio`
:   bio to split

`int sectors`
:   number of sectors to split from the front of **bio**

`gfp_t gfp`
:   gfp mask

`struct bio_set *bs`
:   bio set to allocate from

**Description**

Allocates and returns a new bio which represents **sectors** from the start of
**bio**, and updates **bio** to represent the remaining sectors.

Unless this is a discard request the newly allocated bio will point
to **bio**'s bi_io_vec. It is the caller's responsibility to ensure that
neither **bio** nor **bs** are freed before the split bio.

void bio_trim(struct [bio](api-summary.md#c.bio_trim "bio") \*bio, sector_t offset, sector_t size)
:   trim a bio

**Parameters**

`struct bio *bio`
:   bio to trim

`sector_t offset`
:   number of sectors to trim from the front of **bio**

`sector_t size`
:   size we want to trim **bio** to, in sectors

**Description**

This function is typically used for bios that are cloned and submitted
to the underlying device in parts.

int bioset_init(struct bio_set \*bs, unsigned int pool_size, unsigned int front_pad, int flags)
:   Initialize a bio_set

**Parameters**

`struct bio_set *bs`
:   pool to initialize

`unsigned int pool_size`
:   Number of bio and bio_vecs to cache in the mempool

`unsigned int front_pad`
:   Number of bytes to allocate in front of the returned bio

`int flags`
:   Flags to modify behavior, currently `BIOSET_NEED_BVECS`
    and `BIOSET_NEED_RESCUER`

**Description**

> Set up a bio_set to be used with **bio_alloc_bioset**. Allows the caller
> to ask for a number of bytes to be allocated in front of the bio.
> Front pad allocation is useful for embedding the bio inside
> another structure, to avoid allocating extra data to go with the bio.
> Note that the bio must be embedded at the END of that structure always,
> or things will break badly.
> If `BIOSET_NEED_BVECS` is set in **flags**, a separate pool will be allocated
> for allocating iovecs. This pool is not needed e.g. for [`bio_init_clone()`](api-summary.md#c.bio_init_clone "bio_init_clone").
> If `BIOSET_NEED_RESCUER` is set, a workqueue is created which can be used
> to dispatch queued requests when the mempool runs out of space.

int seq_open(struct [file](api-summary.md#c.seq_open "file") \*file, const struct seq_operations \*op)
:   initialize sequential file

**Parameters**

`struct file *file`
:   file we initialize

`const struct seq_operations *op`
:   method table describing the sequence

    [`seq_open()`](api-summary.md#c.seq_open "seq_open") sets **file**, associating it with a sequence described
    by **op**. **op->[`start()`](../networking/ieee802154.md#c.start "start")** sets the iterator up and returns the first
    element of sequence. **op->[`stop()`](../networking/ieee802154.md#c.stop "stop")** shuts it down. **op->next()**
    returns the next element of sequence. **op->show()** prints element
    into the buffer. In case of error ->[`start()`](../networking/ieee802154.md#c.start "start") and ->next() return
    ERR_PTR(error). In the end of sequence they return `NULL`. ->show()
    returns 0 in case of success and negative number in case of error.
    Returning SEQ_SKIP means "discard this element and move on".

**Note**

seq_open() will allocate a struct seq_file and store its
:   pointer in **file->private_data**. This pointer should not be modified.

ssize_t seq_read(struct [file](api-summary.md#c.seq_read "file") \*file, char __user \*buf, size_t size, loff_t \*ppos)
:   ->read() method for sequential files.

**Parameters**

`struct file *file`
:   the file to read from

`char __user *buf`
:   the buffer to read to

`size_t size`
:   the maximum number of bytes to read

`loff_t *ppos`
:   the current position in the file

    Ready-made ->f_op->read()

loff_t seq_lseek(struct [file](api-summary.md#c.seq_lseek "file") \*file, loff_t offset, int whence)
:   ->llseek() method for sequential files.

**Parameters**

`struct file *file`
:   the file in question

`loff_t offset`
:   new position

`int whence`
:   0 for absolute, 1 for relative position

    Ready-made ->f_op->llseek()

int seq_release(struct [inode](api-summary.md#c.seq_release "inode") \*inode, struct [file](api-summary.md#c.seq_release "file") \*file)
:   free the structures associated with sequential file.

**Parameters**

`struct inode *inode`
:   its inode

    Frees the structures associated with sequential file; can be used
    as ->f_op->release() if you don't have private data to destroy.

`struct file *file`
:   file in question

void seq_escape_mem(struct seq_file \*m, const char \*src, size_t len, unsigned int flags, const char \*esc)
:   print data into buffer, escaping some characters

**Parameters**

`struct seq_file *m`
:   target buffer

`const char *src`
:   source buffer

`size_t len`
:   size of source buffer

`unsigned int flags`
:   flags to pass to [`string_escape_mem()`](../core-api/kernel-api.md#c.string_escape_mem "string_escape_mem")

`const char *esc`
:   set of characters that need escaping

**Description**

Puts data into buffer, replacing each occurrence of character from
given class (defined by **flags** and **esc**) with printable escaped sequence.

Use seq_has_overflowed() to check for errors.

char \*mangle_path(char \*s, const char \*p, const char \*esc)
:   mangle and copy path to buffer beginning

**Parameters**

`char *s`
:   buffer start

`const char *p`
:   beginning of path in above buffer

`const char *esc`
:   set of characters that need escaping

    Copy the path from **p** to **s**, replacing each occurrence of character from
    **esc** with usual octal escape.
    Returns pointer past last written character in **s**, or NULL in case of
    failure.

int seq_path(struct seq_file \*m, const struct [path](api-summary.md#c.seq_path "path") \*path, const char \*esc)
:   seq_file interface to print a pathname

**Parameters**

`struct seq_file *m`
:   the seq_file handle

`const struct path *path`
:   the struct path to print

`const char *esc`
:   set of characters to escape in the output

**Description**

return the absolute path of 'path', as represented by the
dentry / mnt pair in the path parameter.

int seq_file_path(struct seq_file \*m, struct [file](api-summary.md#c.seq_file_path "file") \*file, const char \*esc)
:   seq_file interface to print a pathname of a file

**Parameters**

`struct seq_file *m`
:   the seq_file handle

`struct file *file`
:   the struct file to print

`const char *esc`
:   set of characters to escape in the output

**Description**

return the absolute path to the file.

int seq_write(struct seq_file \*seq, const void \*data, size_t len)
:   write arbitrary data to buffer

**Parameters**

`struct seq_file *seq`
:   seq_file identifying the buffer to which data should be written

`const void *data`
:   data address

`size_t len`
:   number of bytes

**Description**

Return 0 on success, non-zero otherwise.

void seq_pad(struct seq_file \*m, char c)
:   write padding spaces to buffer

**Parameters**

`struct seq_file *m`
:   seq_file identifying the buffer to which data should be written

`char c`
:   the byte to append after padding if non-zero

struct hlist_node \*seq_hlist_start(struct hlist_head \*head, loff_t pos)
:   start an iteration of a hlist

**Parameters**

`struct hlist_head *head`
:   the head of the hlist

`loff_t pos`
:   the start position of the sequence

**Description**

Called at seq_file->op->[`start()`](../networking/ieee802154.md#c.start "start").

struct hlist_node \*seq_hlist_start_head(struct hlist_head \*head, loff_t pos)
:   start an iteration of a hlist

**Parameters**

`struct hlist_head *head`
:   the head of the hlist

`loff_t pos`
:   the start position of the sequence

**Description**

Called at seq_file->op->[`start()`](../networking/ieee802154.md#c.start "start"). Call this function if you want to
print a header at the top of the output.

struct hlist_node \*seq_hlist_next(void \*v, struct hlist_head \*head, loff_t \*ppos)
:   move to the next position of the hlist

**Parameters**

`void *v`
:   the current iterator

`struct hlist_head *head`
:   the head of the hlist

`loff_t *ppos`
:   the current position

**Description**

Called at seq_file->op->next().

struct hlist_node \*seq_hlist_start_rcu(struct hlist_head \*head, loff_t pos)
:   start an iteration of a hlist protected by RCU

**Parameters**

`struct hlist_head *head`
:   the head of the hlist

`loff_t pos`
:   the start position of the sequence

**Description**

Called at seq_file->op->[`start()`](../networking/ieee802154.md#c.start "start").

This list-traversal primitive may safely run concurrently with
the _rcu list-mutation primitives such as [`hlist_add_head_rcu()`](../core-api/kernel-api.md#c.hlist_add_head_rcu "hlist_add_head_rcu")
as long as the traversal is guarded by [`rcu_read_lock()`](../core-api/kernel-api.md#c.rcu_read_lock "rcu_read_lock").

struct hlist_node \*seq_hlist_start_head_rcu(struct hlist_head \*head, loff_t pos)
:   start an iteration of a hlist protected by RCU

**Parameters**

`struct hlist_head *head`
:   the head of the hlist

`loff_t pos`
:   the start position of the sequence

**Description**

Called at seq_file->op->[`start()`](../networking/ieee802154.md#c.start "start"). Call this function if you want to
print a header at the top of the output.

This list-traversal primitive may safely run concurrently with
the _rcu list-mutation primitives such as [`hlist_add_head_rcu()`](../core-api/kernel-api.md#c.hlist_add_head_rcu "hlist_add_head_rcu")
as long as the traversal is guarded by [`rcu_read_lock()`](../core-api/kernel-api.md#c.rcu_read_lock "rcu_read_lock").

struct hlist_node \*seq_hlist_next_rcu(void \*v, struct hlist_head \*head, loff_t \*ppos)
:   move to the next position of the hlist protected by RCU

**Parameters**

`void *v`
:   the current iterator

`struct hlist_head *head`
:   the head of the hlist

`loff_t *ppos`
:   the current position

**Description**

Called at seq_file->op->next().

This list-traversal primitive may safely run concurrently with
the _rcu list-mutation primitives such as [`hlist_add_head_rcu()`](../core-api/kernel-api.md#c.hlist_add_head_rcu "hlist_add_head_rcu")
as long as the traversal is guarded by [`rcu_read_lock()`](../core-api/kernel-api.md#c.rcu_read_lock "rcu_read_lock").

struct hlist_node \*seq_hlist_start_percpu(struct hlist_head __percpu \*head, int \*cpu, loff_t pos)
:   start an iteration of a percpu hlist array

**Parameters**

`struct hlist_head __percpu *head`
:   pointer to percpu array of struct hlist_heads

`int *cpu`
:   pointer to cpu "cursor"

`loff_t pos`
:   start position of sequence

**Description**

Called at seq_file->op->[`start()`](../networking/ieee802154.md#c.start "start").

struct hlist_node \*seq_hlist_next_percpu(void \*v, struct hlist_head __percpu \*head, int \*cpu, loff_t \*pos)
:   move to the next position of the percpu hlist array

**Parameters**

`void *v`
:   pointer to current hlist_node

`struct hlist_head __percpu *head`
:   pointer to percpu array of struct hlist_heads

`int *cpu`
:   pointer to cpu "cursor"

`loff_t *pos`
:   start position of sequence

**Description**

Called at seq_file->op->next().

int register_filesystem(struct file_system_type \*fs)
:   register a new filesystem

**Parameters**

`struct file_system_type * fs`
:   the file system structure

    Adds the file system passed to the list of file systems the kernel
    is aware of for mount and other syscalls. Returns 0 on success,
    or a negative errno code on an error.

    The `struct file_system_type` that is passed is linked into the kernel
    structures and must not be freed until the file system has been
    unregistered.

int unregister_filesystem(struct file_system_type \*fs)
:   unregister a file system

**Parameters**

`struct file_system_type * fs`
:   filesystem to unregister

    Remove a file system that was previously successfully registered
    with the kernel. An error is returned if the file system is not found.
    Zero is returned on a success.

    Once this function has returned the `struct file_system_type` structure
    may be freed or reused.

void wbc_attach_and_unlock_inode(struct writeback_control \*wbc, struct [inode](api-summary.md#c.wbc_attach_and_unlock_inode "inode") \*inode)
:   associate wbc with target inode and unlock it

**Parameters**

`struct writeback_control *wbc`
:   writeback_control of interest

`struct inode *inode`
:   target inode

**Description**

**inode** is locked and about to be written back under the control of **wbc**.
Record **inode**'s writeback context into **wbc** and unlock the i_lock. On
writeback completion, [`wbc_detach_inode()`](api-summary.md#c.wbc_detach_inode "wbc_detach_inode") should be called. This is used
to track the cgroup writeback context.

void wbc_detach_inode(struct writeback_control \*wbc)
:   disassociate wbc from inode and perform foreign detection

**Parameters**

`struct writeback_control *wbc`
:   writeback_control of the just finished writeback

**Description**

To be called after a writeback attempt of an inode finishes and undoes
[`wbc_attach_and_unlock_inode()`](api-summary.md#c.wbc_attach_and_unlock_inode "wbc_attach_and_unlock_inode"). Can be called under any context.

As concurrent write sharing of an inode is expected to be very rare and
memcg only tracks page ownership on first-use basis severely confining
the usefulness of such sharing, cgroup writeback tracks ownership
per-inode. While the support for concurrent write sharing of an inode
is deemed unnecessary, an inode being written to by different cgroups at
different points in time is a lot more common, and, more importantly,
charging only by first-use can too readily lead to grossly incorrect
behaviors (single foreign page can lead to gigabytes of writeback to be
incorrectly attributed).

To resolve this issue, cgroup writeback detects the majority dirtier of
an inode and transfers the ownership to it. To avoid unnecessary
oscillation, the detection mechanism keeps track of history and gives
out the switch verdict only if the foreign usage pattern is stable over
a certain amount of time and/or writeback attempts.

On each writeback attempt, **wbc** tries to detect the majority writer
using Boyer-Moore majority vote algorithm. In addition to the byte
count from the majority voting, it also counts the bytes written for the
current wb and the last round's winner wb (max of last round's current
wb, the winner from two rounds ago, and the last round's majority
candidate). Keeping track of the historical winner helps the algorithm
to semi-reliably detect the most active writer even when it's not the
absolute majority.

Once the winner of the round is determined, whether the winner is
foreign or not and how much IO time the round consumed is recorded in
inode->i_wb_frn_history. If the amount of recorded foreign IO time is
over a certain threshold, the switch verdict is given.

void wbc_account_cgroup_owner(struct writeback_control \*wbc, struct [page](api-summary.md#c.wbc_account_cgroup_owner "page") \*page, size_t bytes)
:   account writeback to update inode cgroup ownership

**Parameters**

`struct writeback_control *wbc`
:   writeback_control of the writeback in progress

`struct page *page`
:   page being written out

`size_t bytes`
:   number of bytes being written out

**Description**

**bytes** from **page** are about to written out during the writeback
controlled by **wbc**. Keep the book for foreign inode detection. See
[`wbc_detach_inode()`](api-summary.md#c.wbc_detach_inode "wbc_detach_inode").

void __mark_inode_dirty(struct [inode](api-summary.md#c.__mark_inode_dirty "inode") \*inode, int flags)
:   internal function to mark an inode dirty

**Parameters**

`struct inode *inode`
:   inode to mark

`int flags`
:   what kind of dirty, e.g. I_DIRTY_SYNC. This can be a combination of
    multiple I_DIRTY_\* flags, except that I_DIRTY_TIME can't be combined
    with I_DIRTY_PAGES.

**Description**

Mark an inode as dirty. We notify the filesystem, then update the inode's
dirty flags. Then, if needed we add the inode to the appropriate dirty list.

Most callers should use mark_inode_dirty() or mark_inode_dirty_sync()
instead of calling this directly.

CAREFUL! We only add the inode to the dirty list if it is hashed or if it
refers to a blockdev. Unhashed inodes will never be added to the dirty list
even if they are later hashed, as they will have been marked dirty already.

In short, ensure you hash any inodes _before_ you start marking them dirty.

Note that for blockdevs, inode->dirtied_when represents the dirtying time of
the block-special inode (/dev/hda1) itself. And the ->dirtied_when field of
the kernel-internal blockdev inode represents the dirtying time of the
blockdev's pages. This is why for I_DIRTY_PAGES we always use
page->mapping->host, so the page-dirtying time is recorded in the internal
blockdev inode.

void writeback_inodes_sb_nr(struct super_block \*sb, unsigned long nr, enum wb_reason reason)
:   writeback dirty inodes from given super_block

**Parameters**

`struct super_block *sb`
:   the superblock

`unsigned long nr`
:   the number of pages to write

`enum wb_reason reason`
:   reason why some writeback work initiated

**Description**

Start writeback on some inodes on this super_block. No guarantees are made
on how many (if any) will be written, and this function does not wait
for IO completion of submitted IO.

void writeback_inodes_sb(struct super_block \*sb, enum wb_reason reason)
:   writeback dirty inodes from given super_block

**Parameters**

`struct super_block *sb`
:   the superblock

`enum wb_reason reason`
:   reason why some writeback work was initiated

**Description**

Start writeback on some inodes on this super_block. No guarantees are made
on how many (if any) will be written, and this function does not wait
for IO completion of submitted IO.

void try_to_writeback_inodes_sb(struct super_block \*sb, enum wb_reason reason)
:   try to start writeback if none underway

**Parameters**

`struct super_block *sb`
:   the superblock

`enum wb_reason reason`
:   reason why some writeback work was initiated

**Description**

Invoke __writeback_inodes_sb_nr if no writeback is currently underway.

void sync_inodes_sb(struct super_block \*sb)
:   sync sb inode pages

**Parameters**

`struct super_block *sb`
:   the superblock

**Description**

This function writes and waits on any dirty inode belonging to this
super_block.

int write_inode_now(struct [inode](api-summary.md#c.write_inode_now "inode") \*inode, int sync)
:   write an inode to disk

**Parameters**

`struct inode *inode`
:   inode to write to disk

`int sync`
:   whether the write should be synchronous or not

**Description**

This function commits an inode to disk immediately if it is dirty. This is
primarily needed by knfsd.

The caller must either have a ref on the inode or must have set I_WILL_FREE.

int sync_inode_metadata(struct [inode](api-summary.md#c.sync_inode_metadata "inode") \*inode, int wait)
:   write an inode to disk

**Parameters**

`struct inode *inode`
:   the inode to sync

`int wait`
:   wait for I/O to complete.

**Description**

Write an inode to disk and adjust its dirty state after completion.

**Note**

only writes the actual inode, no associated data or other metadata.

struct file \*anon_inode_getfile(const char \*name, const struct file_operations \*fops, void \*priv, int flags)
:   creates a new file instance by hooking it up to an anonymous inode, and a dentry that describe the "class" of the file

**Parameters**

`const char *name`
:   [in] name of the "class" of the new file

`const struct file_operations *fops`
:   [in] file operations for the new file

`void *priv`
:   [in] private data for the new file (will be file's private_data)

`int flags`
:   [in] flags

**Description**

Creates a new file by hooking it on a single inode. This is useful for files
that do not need to have a full-fledged inode in order to operate correctly.
All the files created with [`anon_inode_getfile()`](api-summary.md#c.anon_inode_getfile "anon_inode_getfile") will share a single inode,
hence saving memory and avoiding code duplication for the file/inode/dentry
setup. Returns the newly created file\* or an error pointer.

struct file \*anon_inode_create_getfile(const char \*name, const struct file_operations \*fops, void \*priv, int flags, const struct inode \*context_inode)
:   Like [`anon_inode_getfile()`](api-summary.md#c.anon_inode_getfile "anon_inode_getfile"), but creates a new !S_PRIVATE anon inode rather than reuse the singleton anon inode and calls the inode_init_security_anon() LSM hook.

**Parameters**

`const char *name`
:   [in] name of the "class" of the new file

`const struct file_operations *fops`
:   [in] file operations for the new file

`void *priv`
:   [in] private data for the new file (will be file's private_data)

`int flags`
:   [in] flags

`const struct inode *context_inode`

> [in] the logical relationship with the new inode (optional)

**Description**

Create a new anonymous inode and file pair. This can be done for two
reasons:

- for the inode to have its own security context, so that LSMs can enforce
  policy on the inode's creation;
- if the caller needs a unique inode, for example in order to customize
  the size returned by fstat()

The LSM may use **context_inode** in inode_init_security_anon(), but a
reference to it is not held.

Returns the newly created file\* or an error pointer.

int anon_inode_getfd(const char \*name, const struct file_operations \*fops, void \*priv, int flags)
:   creates a new file instance by hooking it up to an anonymous inode and a dentry that describe the "class" of the file

**Parameters**

`const char *name`
:   [in] name of the "class" of the new file

`const struct file_operations *fops`
:   [in] file operations for the new file

`void *priv`
:   [in] private data for the new file (will be file's private_data)

`int flags`
:   [in] flags

**Description**

Creates a new file by hooking it on a single inode. This is
useful for files that do not need to have a full-fledged inode in
order to operate correctly. All the files created with
[`anon_inode_getfd()`](api-summary.md#c.anon_inode_getfd "anon_inode_getfd") will use the same singleton inode, reducing
memory use and avoiding code duplication for the file/inode/dentry
setup. Returns a newly created file descriptor or an error code.

int setattr_should_drop_sgid(struct mnt_idmap \*idmap, const struct [inode](api-summary.md#c.setattr_should_drop_sgid "inode") \*inode)
:   determine whether the setgid bit needs to be removed

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount **inode** was found from

`const struct inode *inode`
:   inode to check

**Description**

This function determines whether the setgid bit needs to be removed.
We retain backwards compatibility and require setgid bit to be removed
unconditionally if S_IXGRP is set. Otherwise we have the exact same
requirements as [`setattr_prepare()`](api-summary.md#c.setattr_prepare "setattr_prepare") and [`setattr_copy()`](api-summary.md#c.setattr_copy "setattr_copy").

**Return**

ATTR_KILL_SGID if setgid bit needs to be removed, 0 otherwise.

int setattr_should_drop_suidgid(struct mnt_idmap \*idmap, struct [inode](api-summary.md#c.setattr_should_drop_suidgid "inode") \*inode)
:   determine whether the set{g,u}id bit needs to be dropped

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount **inode** was found from

`struct inode *inode`
:   inode to check

**Description**

This function determines whether the set{g,u}id bits need to be removed.
If the setuid bit needs to be removed ATTR_KILL_SUID is returned. If the
setgid bit needs to be removed ATTR_KILL_SGID is returned. If both
set{g,u}id bits need to be removed the corresponding mask of both flags is
returned.

**Return**

A mask of ATTR_KILL_S{G,U}ID indicating which - if any - setid bits
to remove, 0 otherwise.

int setattr_prepare(struct mnt_idmap \*idmap, struct [dentry](api-summary.md#c.setattr_prepare "dentry") \*dentry, struct iattr \*attr)
:   check if attribute changes to a dentry are allowed

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`struct dentry *dentry`
:   dentry to check

`struct iattr *attr`
:   attributes to change

**Description**

Check if we are allowed to change the attributes contained in **attr**
in the given dentry. This includes the normal unix access permission
checks, as well as checks for rlimits and others. The function also clears
SGID bit from mode if user is not allowed to set it. Also file capabilities
and IMA extended attributes are cleared if ATTR_KILL_PRIV is set.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then
take care to map the inode according to **idmap** before checking
permissions. On non-idmapped mounts or if permission checking is to be
performed on the raw inode simply pass **nop_mnt_idmap**.

Should be called as the first thing in ->setattr implementations,
possibly after taking additional locks.

int inode_newsize_ok(const struct [inode](api-summary.md#c.inode_newsize_ok "inode") \*inode, loff_t offset)
:   may this inode be truncated to a given size

**Parameters**

`const struct inode *inode`
:   the inode to be truncated

`loff_t offset`
:   the new size to assign to the inode

**Description**

inode_newsize_ok must be called with i_mutex held.

inode_newsize_ok will check filesystem limits and ulimits to check that the
new inode size is within limits. inode_newsize_ok will also send SIGXFSZ
when necessary. Caller must not proceed with inode size change if failure is
returned. **inode** must be a file (not directory), with appropriate
permissions to allow truncate (inode_newsize_ok does NOT check these
conditions).

**Return**

0 on success, -ve errno on failure

void setattr_copy(struct mnt_idmap \*idmap, struct [inode](api-summary.md#c.setattr_copy "inode") \*inode, const struct iattr \*attr)
:   copy simple metadata updates into the generic inode

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`struct inode *inode`
:   the inode to be updated

`const struct iattr *attr`
:   the new attributes

**Description**

setattr_copy must be called with i_mutex held.

setattr_copy updates the inode's metadata with that specified
in attr on idmapped mounts. Necessary permission checks to determine
whether or not the S_ISGID property needs to be removed are performed with
the correct idmapped mount permission helpers.
Noticeably missing is inode size update, which is more complex
as it requires pagecache updates.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then
take care to map the inode according to **idmap** before checking
permissions. On non-idmapped mounts or if permission checking is to be
performed on the raw inode simply pass **nop_mnt_idmap**.

The inode is not marked as dirty after this operation. The rationale is
that for "simple" filesystems, the struct inode is the inode storage.
The caller is free to mark the inode dirty afterwards if needed.

int notify_change(struct mnt_idmap \*idmap, struct [dentry](api-summary.md#c.notify_change "dentry") \*dentry, struct iattr \*attr, struct inode \*\*delegated_inode)
:   modify attributes of a filesytem object

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`struct dentry *dentry`
:   object affected

`struct iattr *attr`
:   new attributes

`struct inode **delegated_inode`
:   returns inode, if the inode is delegated

**Description**

The caller must hold the i_mutex on the affected object.

If notify_change discovers a delegation in need of breaking,
it will return -EWOULDBLOCK and return a reference to the inode in
delegated_inode. The caller should then break the delegation and
retry. Because breaking a delegation may take a long time, the
caller should drop the i_mutex before doing so.

Alternatively, a caller may pass NULL for delegated_inode. This may
be appropriate for callers that expect the underlying filesystem not
to be NFS exported. Also, passing NULL is fine for callers holding
the file open for write, as there can be no conflicting delegation in
that case.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then
take care to map the inode according to **idmap** before checking
permissions. On non-idmapped mounts or if permission checking is to be
performed on the raw inode simply pass **nop_mnt_idmap**.

char \*d_path(const struct [path](api-summary.md#c.d_path "path") \*path, char \*buf, int buflen)
:   return the path of a dentry

**Parameters**

`const struct path *path`
:   path to report

`char *buf`
:   buffer to return value in

`int buflen`
:   buffer length

**Description**

Convert a dentry into an ASCII path name. If the entry has been deleted
the string " (deleted)" is appended. Note that this is ambiguous.

Returns a pointer into the buffer or an error code if the path was
too long. Note: Callers should use the returned pointer, not the passed
in buffer, to use the name! The implementation often starts at an offset
into the buffer, and may leave 0 bytes at the start.

"buflen" should be positive.

struct page \*dax_layout_busy_page_range(struct [address_space](api-summary.md#c.address_space "address_space") \*mapping, loff_t start, loff_t end)
:   find first pinned page in **mapping**

**Parameters**

`struct address_space *mapping`
:   address space to scan for a page with ref count > 1

`loff_t start`
:   Starting offset. Page containing 'start' is included.

`loff_t end`
:   End offset. Page containing 'end' is included. If 'end' is LLONG_MAX,
    pages from 'start' till the end of file are included.

**Description**

DAX requires ZONE_DEVICE mapped pages. These pages are never
'onlined' to the page allocator so they are considered idle when
page->count == 1. A filesystem uses this interface to determine if
any page in the mapping is busy, i.e. for DMA, or other
get_user_pages() usages.

It is expected that the filesystem is holding locks to block the
establishment of new mappings in this address_space. I.e. it expects
to be able to run [`unmap_mapping_range()`](../core-api/mm-api.md#c.unmap_mapping_range "unmap_mapping_range") and subsequently not race
mapping_mapped() becoming true.

ssize_t dax_iomap_rw(struct kiocb \*iocb, struct iov_iter \*iter, const struct iomap_ops \*ops)
:   Perform I/O to a DAX file

**Parameters**

`struct kiocb *iocb`
:   The control block for this I/O

`struct iov_iter *iter`
:   The addresses to do I/O from or to

`const struct iomap_ops *ops`
:   iomap ops passed from the file system

**Description**

This function performs read and write operations to directly mapped
persistent memory. The callers needs to take care of read/write exclusion
and evicting any page cache pages in the region under I/O.

[vm_fault_t](../core-api/mm-api.md#c.vm_fault_t "vm_fault_t") dax_iomap_fault(struct vm_fault \*vmf, unsigned int order, pfn_t \*pfnp, int \*iomap_errp, const struct iomap_ops \*ops)
:   handle a page fault on a DAX file

**Parameters**

`struct vm_fault *vmf`
:   The description of the fault

`unsigned int order`
:   Order of the page to fault in

`pfn_t *pfnp`
:   PFN to insert for synchronous faults if fsync is required

`int *iomap_errp`
:   Storage for detailed error code in case of error

`const struct iomap_ops *ops`
:   Iomap ops passed from the file system

**Description**

When a page fault occurs, filesystems may call this helper in
their fault handler for DAX files. [`dax_iomap_fault()`](api-summary.md#c.dax_iomap_fault "dax_iomap_fault") assumes the caller
has done all the necessary locking for page fault to proceed
successfully.

[vm_fault_t](../core-api/mm-api.md#c.vm_fault_t "vm_fault_t") dax_finish_sync_fault(struct vm_fault \*vmf, unsigned int order, pfn_t pfn)
:   finish synchronous page fault

**Parameters**

`struct vm_fault *vmf`
:   The description of the fault

`unsigned int order`
:   Order of entry to be inserted

`pfn_t pfn`
:   PFN to insert

**Description**

This function ensures that the file range touched by the page fault is
stored persistently on the media and handles inserting of appropriate page
table entry.

void simple_rename_timestamp(struct inode \*old_dir, struct dentry \*old_dentry, struct inode \*new_dir, struct dentry \*new_dentry)
:   update the various inode timestamps for rename

**Parameters**

`struct inode *old_dir`
:   old parent directory

`struct dentry *old_dentry`
:   dentry that is being renamed

`struct inode *new_dir`
:   new parent directory

`struct dentry *new_dentry`
:   target for rename

**Description**

POSIX mandates that the old and new parent directories have their ctime and
mtime updated, and that inodes of **old_dentry** and **new_dentry** (if any), have
their ctime updated.

int simple_setattr(struct mnt_idmap \*idmap, struct [dentry](api-summary.md#c.simple_setattr "dentry") \*dentry, struct [iattr](api-summary.md#c.simple_setattr "iattr") \*iattr)
:   setattr for simple filesystem

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the target mount

`struct dentry *dentry`
:   dentry

`struct iattr *iattr`
:   iattr structure

**Description**

Returns 0 on success, -error on failure.

simple_setattr is a simple ->setattr implementation without a proper
implementation of size changes.

It can either be used for in-memory filesystems or special files
on simple regular filesystems. Anything that needs to change on-disk
or wire state on size changes needs its own setattr method.

ssize_t simple_read_from_buffer(void __user \*to, size_t count, loff_t \*ppos, const void \*from, size_t available)
:   copy data from the buffer to user space

**Parameters**

`void __user *to`
:   the user space buffer to read to

`size_t count`
:   the maximum number of bytes to read

`loff_t *ppos`
:   the current position in the buffer

`const void *from`
:   the buffer to read from

`size_t available`
:   the size of the buffer

**Description**

The [`simple_read_from_buffer()`](api-summary.md#c.simple_read_from_buffer "simple_read_from_buffer") function reads up to **count** bytes from the
buffer **from** at offset **ppos** into the user space address starting at **to**.

On success, the number of bytes read is returned and the offset **ppos** is
advanced by this number, or negative value is returned on error.

ssize_t simple_write_to_buffer(void \*to, size_t available, loff_t \*ppos, const void __user \*from, size_t count)
:   copy data from user space to the buffer

**Parameters**

`void *to`
:   the buffer to write to

`size_t available`
:   the size of the buffer

`loff_t *ppos`
:   the current position in the buffer

`const void __user *from`
:   the user space buffer to read from

`size_t count`
:   the maximum number of bytes to read

**Description**

The [`simple_write_to_buffer()`](api-summary.md#c.simple_write_to_buffer "simple_write_to_buffer") function reads up to **count** bytes from the user
space address starting at **from** into the buffer **to** at offset **ppos**.

On success, the number of bytes written is returned and the offset **ppos** is
advanced by this number, or negative value is returned on error.

ssize_t memory_read_from_buffer(void \*to, size_t count, loff_t \*ppos, const void \*from, size_t available)
:   copy data from the buffer

**Parameters**

`void *to`
:   the kernel space buffer to read to

`size_t count`
:   the maximum number of bytes to read

`loff_t *ppos`
:   the current position in the buffer

`const void *from`
:   the buffer to read from

`size_t available`
:   the size of the buffer

**Description**

The [`memory_read_from_buffer()`](api-summary.md#c.memory_read_from_buffer "memory_read_from_buffer") function reads up to **count** bytes from the
buffer **from** at offset **ppos** into the kernel space address starting at **to**.

On success, the number of bytes read is returned and the offset **ppos** is
advanced by this number, or negative value is returned on error.

int generic_encode_ino32_fh(struct [inode](api-summary.md#c.generic_encode_ino32_fh "inode") \*inode, __u32 \*fh, int \*max_len, struct [inode](api-summary.md#c.generic_encode_ino32_fh "inode") \*parent)
:   generic export_operations->encode_fh function

**Parameters**

`struct inode *inode`
:   the object to encode

`__u32 *fh`
:   where to store the file handle fragment

`int *max_len`
:   maximum length to store there (in 4 byte units)

`struct inode *parent`
:   parent directory inode, if wanted

**Description**

This generic encode_fh function assumes that the 32 inode number
is suitable for locating an inode, and that the generation number
can be used to check that it is still valid. It places them in the
filehandle fragment where export_decode_fh expects to find them.

struct dentry \*generic_fh_to_dentry(struct super_block \*sb, struct [fid](api-summary.md#c.generic_fh_to_dentry "fid") \*fid, int fh_len, int fh_type, struct inode \*(\*get_inode)(struct super_block \*sb, u64 ino, u32 gen))
:   generic helper for the fh_to_dentry export operation

**Parameters**

`struct super_block *sb`
:   filesystem to do the file handle conversion on

`struct fid *fid`
:   file handle to convert

`int fh_len`
:   length of the file handle in bytes

`int fh_type`
:   type of file handle

`struct inode *(*get_inode) (struct super_block *sb, u64 ino, u32 gen)`
:   filesystem callback to retrieve inode

**Description**

This function decodes **fid** as long as it has one of the well-known
Linux filehandle types and calls **get_inode** on it to retrieve the
inode for the object specified in the file handle.

struct dentry \*generic_fh_to_parent(struct super_block \*sb, struct [fid](api-summary.md#c.generic_fh_to_parent "fid") \*fid, int fh_len, int fh_type, struct inode \*(\*get_inode)(struct super_block \*sb, u64 ino, u32 gen))
:   generic helper for the fh_to_parent export operation

**Parameters**

`struct super_block *sb`
:   filesystem to do the file handle conversion on

`struct fid *fid`
:   file handle to convert

`int fh_len`
:   length of the file handle in bytes

`int fh_type`
:   type of file handle

`struct inode *(*get_inode) (struct super_block *sb, u64 ino, u32 gen)`
:   filesystem callback to retrieve inode

**Description**

This function decodes **fid** as long as it has one of the well-known
Linux filehandle types and calls **get_inode** on it to retrieve the
inode for the _parent_ object specified in the file handle if it
is specified in the file handle, or NULL otherwise.

int __generic_file_fsync(struct [file](api-summary.md#c.__generic_file_fsync "file") \*file, loff_t start, loff_t end, int datasync)
:   generic fsync implementation for simple filesystems

**Parameters**

`struct file *file`
:   file to synchronize

`loff_t start`
:   start offset in bytes

`loff_t end`
:   end offset in bytes (inclusive)

`int datasync`
:   only synchronize essential metadata if true

**Description**

This is a generic implementation of the fsync method for simple
filesystems which track all non-inode metadata in the buffers list
hanging off the address_space structure.

int generic_file_fsync(struct [file](api-summary.md#c.generic_file_fsync "file") \*file, loff_t start, loff_t end, int datasync)
:   generic fsync implementation for simple filesystems with flush

**Parameters**

`struct file *file`
:   file to synchronize

`loff_t start`
:   start offset in bytes

`loff_t end`
:   end offset in bytes (inclusive)

`int datasync`
:   only synchronize essential metadata if true

int generic_check_addressable(unsigned blocksize_bits, u64 num_blocks)
:   Check addressability of file system

**Parameters**

`unsigned blocksize_bits`
:   log of file system block size

`u64 num_blocks`
:   number of blocks in file system

**Description**

Determine whether a file system with **num_blocks** blocks (and a
block size of 2\*\*\*\*blocksize_bits\*\*) is addressable by the sector_t
and page cache of the system. Return 0 if so and -EFBIG otherwise.

int simple_nosetlease(struct file \*filp, int arg, struct file_lock \*\*flp, void \*\*priv)
:   generic helper for prohibiting leases

**Parameters**

`struct file *filp`
:   file pointer

`int arg`
:   type of lease to obtain

`struct file_lock **flp`
:   new lease supplied for insertion

`void **priv`
:   private data for lm_setup operation

**Description**

Generic helper for filesystems that do not wish to allow leases to be set.
All arguments are ignored and it just returns -EINVAL.

const char \*simple_get_link(struct [dentry](api-summary.md#c.simple_get_link "dentry") \*dentry, struct [inode](api-summary.md#c.simple_get_link "inode") \*inode, struct delayed_call \*done)
:   generic helper to get the target of "fast" symlinks

**Parameters**

`struct dentry *dentry`
:   not used here

`struct inode *inode`
:   the symlink inode

`struct delayed_call *done`
:   not used here

**Description**

Generic helper for filesystems to use for symlink inodes where a pointer to
the symlink target is stored in ->i_link. NOTE: this isn't normally called,
since as an optimization the path lookup code uses any non-NULL ->i_link
directly, without calling ->get_link(). But ->get_link() still must be set,
to mark the inode_operations as being for a symlink.

**Return**

the symlink target

void generic_set_encrypted_ci_d_ops(struct [dentry](api-summary.md#c.generic_set_encrypted_ci_d_ops "dentry") \*dentry)
:   helper for setting d_ops for given dentry

**Parameters**

`struct dentry *dentry`
:   dentry to set ops on

**Description**

Casefolded directories need d_hash and d_compare set, so that the dentries
contained in them are handled case-insensitively. Note that these operations
are needed on the parent directory rather than on the dentries in it, and
while the casefolding flag can be toggled on and off on an empty directory,
dentry_operations can't be changed later. As a result, if the filesystem has
casefolding support enabled at all, we have to give all dentries the
casefolding operations even if their inode doesn't have the casefolding flag
currently (and thus the casefolding ops would be no-ops for now).

Encryption works differently in that the only dentry operation it needs is
d_revalidate, which it only needs on dentries that have the no-key name flag.
The no-key flag can't be set "later", so we don't have to worry about that.

Finally, to maximize compatibility with overlayfs (which isn't compatible
with certain dentry operations) and to avoid taking an unnecessary
performance hit, we use custom dentry_operations for each possible
combination rather than always installing all operations.

bool inode_maybe_inc_iversion(struct [inode](api-summary.md#c.inode_maybe_inc_iversion "inode") \*inode, bool force)
:   increments i_version

**Parameters**

`struct inode *inode`
:   inode with the i_version that should be updated

`bool force`
:   increment the counter even if it's not necessary?

**Description**

Every time the inode is modified, the i_version field must be seen to have
changed by any observer.

If "force" is set or the QUERIED flag is set, then ensure that we increment
the value, and clear the queried flag.

In the common case where neither is set, then we can return "false" without
updating i_version.

If this function returns false, and no other metadata has changed, then we
can avoid logging the metadata.

u64 inode_query_iversion(struct [inode](api-summary.md#c.inode_query_iversion "inode") \*inode)
:   read i_version for later use

**Parameters**

`struct inode *inode`
:   inode from which i_version should be read

**Description**

Read the inode i_version counter. This should be used by callers that wish
to store the returned i_version for later comparison. This will guarantee
that a later query of the i_version will result in a different value if
anything has changed.

In this implementation, we fetch the current value, set the QUERIED flag and
then try to swap it into place with a cmpxchg, if it wasn't already set. If
that fails, we try again with the newly fetched value from the cmpxchg.

struct timespec64 simple_inode_init_ts(struct [inode](api-summary.md#c.simple_inode_init_ts "inode") \*inode)
:   initialize the timestamps for a new inode

**Parameters**

`struct inode *inode`
:   inode to be initialized

**Description**

When a new inode is created, most filesystems set the timestamps to the
current time. Add a helper to do this.

int posix_acl_chmod(struct mnt_idmap \*idmap, struct [dentry](api-summary.md#c.posix_acl_chmod "dentry") \*dentry, umode_t mode)
:   chmod a posix acl

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount **inode** was found from

`struct dentry *dentry`
:   dentry to check permissions on

`umode_t mode`
:   the new mode of **inode**

**Description**

If the dentry has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then
take care to map the inode according to **idmap** before checking
permissions. On non-idmapped mounts or if permission checking is to be
performed on the raw inode simply pass **nop_mnt_idmap**.

int posix_acl_update_mode(struct mnt_idmap \*idmap, struct [inode](api-summary.md#c.posix_acl_update_mode "inode") \*inode, umode_t \*mode_p, struct posix_acl \*\*acl)
:   update mode in set_acl

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount **inode** was found from

`struct inode *inode`
:   target inode

`umode_t *mode_p`
:   mode (pointer) for update

`struct posix_acl **acl`
:   acl pointer

**Description**

Update the file mode when setting an ACL: compute the new file permission
bits based on the ACL. In addition, if the ACL is equivalent to the new
file mode, set **\*acl** to NULL to indicate that no ACL should be set.

As with chmod, clear the setgid bit if the caller is not in the owning group
or capable of CAP_FSETID (see inode_change_ok).

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then
take care to map the inode according to **idmap** before checking
permissions. On non-idmapped mounts or if permission checking is to be
performed on the raw inode simply pass **nop_mnt_idmap**.

Called from set_acl inode operations.

struct posix_acl \*posix_acl_from_xattr(struct user_namespace \*userns, const void \*value, size_t size)
:   convert POSIX ACLs from backing store to VFS format

**Parameters**

`struct user_namespace *userns`
:   the filesystem's idmapping

`const void *value`
:   the uapi representation of POSIX ACLs

`size_t size`
:   the size of **void**

**Description**

Filesystems that store POSIX ACLs in the unaltered uapi format should use
[`posix_acl_from_xattr()`](api-summary.md#c.posix_acl_from_xattr "posix_acl_from_xattr") when reading them from the backing store and
converting them into the struct posix_acl VFS format. The helper is
specifically intended to be called from the acl inode operation.

The [`posix_acl_from_xattr()`](api-summary.md#c.posix_acl_from_xattr "posix_acl_from_xattr") function will map the raw {g,u}id values stored
in ACL_{GROUP,USER} entries into idmapping in **userns**.

Note that [`posix_acl_from_xattr()`](api-summary.md#c.posix_acl_from_xattr "posix_acl_from_xattr") does not take idmapped mounts into account.
If it did it calling it from the get acl inode operation would return POSIX
ACLs mapped according to an idmapped mount which would mean that the value
couldn't be cached for the filesystem. Idmapped mounts are taken into
account on the fly during permission checking or right at the VFS -
userspace boundary before reporting them to the user.

**Return**

Allocated struct posix_acl on success, NULL for a valid header but
:   without actual POSIX ACL entries, or [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") encoded error code.

int vfs_set_acl(struct mnt_idmap \*idmap, struct [dentry](api-summary.md#c.vfs_set_acl "dentry") \*dentry, const char \*acl_name, struct posix_acl \*kacl)
:   set posix acls

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount

`struct dentry *dentry`
:   the dentry based on which to set the posix acls

`const char *acl_name`
:   the name of the posix acl

`struct posix_acl *kacl`
:   the posix acls in the appropriate VFS format

**Description**

This function sets **kacl**. The caller must all posix_acl_release() on **kacl**
afterwards.

**Return**

On success 0, on error negative errno.

struct posix_acl \*vfs_get_acl(struct mnt_idmap \*idmap, struct [dentry](api-summary.md#c.vfs_get_acl "dentry") \*dentry, const char \*acl_name)
:   get posix acls

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount

`struct dentry *dentry`
:   the dentry based on which to retrieve the posix acls

`const char *acl_name`
:   the name of the posix acl

**Description**

This function retrieves **kacl** from the filesystem. The caller must all
posix_acl_release() on **kacl**.

**Return**

On success POSIX ACLs in VFS format, on error negative errno.

int vfs_remove_acl(struct mnt_idmap \*idmap, struct [dentry](api-summary.md#c.vfs_remove_acl "dentry") \*dentry, const char \*acl_name)
:   remove posix acls

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount

`struct dentry *dentry`
:   the dentry based on which to retrieve the posix acls

`const char *acl_name`
:   the name of the posix acl

**Description**

This function removes posix acls.

**Return**

On success 0, on error negative errno.

void generic_fillattr(struct mnt_idmap \*idmap, u32 request_mask, struct [inode](api-summary.md#c.generic_fillattr "inode") \*inode, struct kstat \*stat)
:   Fill in the basic attributes from the inode struct

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount the inode was found from

`u32 request_mask`
:   statx request_mask

`struct inode *inode`
:   Inode to use as the source

`struct kstat *stat`
:   Where to fill in the attributes

**Description**

Fill in the basic attributes in the kstat structure from data that's to be
found on the VFS inode structure. This is the default if no getattr inode
operation is supplied.

If the inode has been found through an idmapped mount the idmap of
the vfsmount must be passed through **idmap**. This function will then
take care to map the inode according to **idmap** before filling in the
uid and gid filds. On non-idmapped mounts or if permission checking is to be
performed on the raw inode simply pass **nop_mnt_idmap**.

void generic_fill_statx_attr(struct [inode](api-summary.md#c.generic_fill_statx_attr "inode") \*inode, struct kstat \*stat)
:   Fill in the statx attributes from the inode flags

**Parameters**

`struct inode *inode`
:   Inode to use as the source

`struct kstat *stat`
:   Where to fill in the attribute flags

**Description**

Fill in the STATX_ATTR_\* flags in the kstat structure for properties of the
inode that are published on i_flags and enforced by the VFS.

int vfs_getattr_nosec(const struct [path](api-summary.md#c.vfs_getattr_nosec "path") \*path, struct kstat \*stat, u32 request_mask, unsigned int query_flags)
:   getattr without security checks

**Parameters**

`const struct path *path`
:   file to get attributes from

`struct kstat *stat`
:   structure to return attributes in

`u32 request_mask`
:   STATX_xxx flags indicating what the caller wants

`unsigned int query_flags`
:   Query mode (AT_STATX_SYNC_TYPE)

**Description**

Get attributes without calling security_inode_getattr.

Currently the only caller other than vfs_getattr is internal to the
filehandle lookup code, which uses only the inode number and returns no
attributes to any user. Any other code probably wants vfs_getattr.

int vfs_fsync_range(struct [file](api-summary.md#c.vfs_fsync_range "file") \*file, loff_t start, loff_t end, int datasync)
:   helper to sync a range of data & metadata to disk

**Parameters**

`struct file *file`
:   file to sync

`loff_t start`
:   offset in bytes of the beginning of data range to sync

`loff_t end`
:   offset in bytes of the end of data range (inclusive)

`int datasync`
:   perform only datasync

**Description**

Write back data in range **start**..\*\*end\*\* and metadata for **file** to disk. If
**datasync** is set only metadata needed to access modified file data is
written.

int vfs_fsync(struct [file](api-summary.md#c.vfs_fsync "file") \*file, int datasync)
:   perform a fsync or fdatasync on a file

**Parameters**

`struct file *file`
:   file to sync

`int datasync`
:   only perform a fdatasync operation

**Description**

Write back data and metadata for **file** to disk. If **datasync** is
set only metadata needed to access modified file data is written.

int __vfs_setxattr_locked(struct mnt_idmap \*idmap, struct [dentry](api-summary.md#c.__vfs_setxattr_locked "dentry") \*dentry, const char \*name, const void \*value, size_t size, int flags, struct inode \*\*delegated_inode)
:   set an extended attribute while holding the inode lock

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount of the target inode

`struct dentry *dentry`
:   object to perform setxattr on

`const char *name`
:   xattr name to set

`const void *value`
:   value to set **name** to

`size_t size`
:   size of **value**

`int flags`
:   flags to pass into filesystem operations

`struct inode **delegated_inode`
:   on return, will contain an inode pointer that
    a delegation was broken on, NULL if none.

ssize_t vfs_listxattr(struct [dentry](api-summary.md#c.vfs_listxattr "dentry") \*dentry, char \*list, size_t size)
:   retrieve 0 separated list of xattr names

**Parameters**

`struct dentry *dentry`
:   the dentry from whose inode the xattr names are retrieved

`char *list`
:   buffer to store xattr names into

`size_t size`
:   size of the buffer

**Description**

This function returns the names of all xattrs associated with the
inode of **dentry**.

Note, for legacy reasons the [`vfs_listxattr()`](api-summary.md#c.vfs_listxattr "vfs_listxattr") function lists POSIX
ACLs as well. Since POSIX ACLs are decoupled from IOP_XATTR the
[`vfs_listxattr()`](api-summary.md#c.vfs_listxattr "vfs_listxattr") function doesn't check for this flag since a
filesystem could implement POSIX ACLs without implementing any other
xattrs.

However, since all codepaths that remove IOP_XATTR also assign of
inode operations that either don't implement or implement a stub
->listxattr() operation.

**Return**

On success, the size of the buffer that was used. On error a
:   negative error code.

int __vfs_removexattr_locked(struct mnt_idmap \*idmap, struct [dentry](api-summary.md#c.__vfs_removexattr_locked "dentry") \*dentry, const char \*name, struct inode \*\*delegated_inode)
:   set an extended attribute while holding the inode lock

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount of the target inode

`struct dentry *dentry`
:   object to perform setxattr on

`const char *name`
:   name of xattr to remove

`struct inode **delegated_inode`
:   on return, will contain an inode pointer that
    a delegation was broken on, NULL if none.

ssize_t generic_listxattr(struct [dentry](api-summary.md#c.generic_listxattr "dentry") \*dentry, char \*buffer, size_t buffer_size)
:   run through a dentry's xattr list() operations

**Parameters**

`struct dentry *dentry`
:   dentry to list the xattrs

`char *buffer`
:   result buffer

`size_t buffer_size`
:   size of **buffer**

**Description**

Combine the results of the list() operation from every xattr_handler in the
xattr_handler stack.

Note that this will not include the entries for POSIX ACLs.

const char \*xattr_full_name(const struct xattr_handler \*handler, const char \*name)
:   Compute full attribute name from suffix

**Parameters**

`const struct xattr_handler *handler`
:   handler of the xattr_handler operation

`const char *name`
:   name passed to the xattr_handler operation

**Description**

The get and set xattr handler operations are called with the remainder of
the attribute name after skipping the handler's prefix: for example, "foo"
is passed to the get operation of a handler with prefix "user." to get
attribute "user.foo". The full name is still "there" in the name though.

**Note**

the list xattr handler operation when called from the vfs is passed a
NULL name; some file systems use this operation internally, with varying
semantics.

int mnt_get_write_access(struct vfsmount \*m)
:   get write access to a mount without freeze protection

**Parameters**

`struct vfsmount *m`
:   the mount on which to take a write

**Description**

This tells the low-level filesystem that a write is about to be performed to
it, and makes sure that writes are allowed (mnt it read-write) before
returning success. This operation does not protect against filesystem being
frozen. When the write operation is finished, [`mnt_put_write_access()`](api-summary.md#c.mnt_put_write_access "mnt_put_write_access") must be
called. This is effectively a refcount.

int mnt_want_write(struct vfsmount \*m)
:   get write access to a mount

**Parameters**

`struct vfsmount *m`
:   the mount on which to take a write

**Description**

This tells the low-level filesystem that a write is about to be performed to
it, and makes sure that writes are allowed (mount is read-write, filesystem
is not frozen) before returning success. When the write operation is
finished, [`mnt_drop_write()`](api-summary.md#c.mnt_drop_write "mnt_drop_write") must be called. This is effectively a refcount.

int mnt_want_write_file(struct [file](api-summary.md#c.mnt_want_write_file "file") \*file)
:   get write access to a file's mount

**Parameters**

`struct file *file`
:   the file who's mount on which to take a write

**Description**

This is like mnt_want_write, but if the file is already open for writing it
skips incrementing mnt_writers (since the open file already has a reference)
and instead only does the freeze protection and the check for emergency r/o
remounts. This must be paired with mnt_drop_write_file.

void mnt_put_write_access(struct vfsmount \*mnt)
:   give up write access to a mount

**Parameters**

`struct vfsmount *mnt`
:   the mount on which to give up write access

**Description**

Tells the low-level filesystem that we are done
performing writes to it. Must be matched with
[`mnt_get_write_access()`](api-summary.md#c.mnt_get_write_access "mnt_get_write_access") call above.

void mnt_drop_write(struct vfsmount \*mnt)
:   give up write access to a mount

**Parameters**

`struct vfsmount *mnt`
:   the mount on which to give up write access

**Description**

Tells the low-level filesystem that we are done performing writes to it and
also allows filesystem to be frozen again. Must be matched with
[`mnt_want_write()`](api-summary.md#c.mnt_want_write "mnt_want_write") call above.

struct vfsmount \*vfs_create_mount(struct fs_context \*fc)
:   Create a mount for a configured superblock

**Parameters**

`struct fs_context *fc`
:   The configuration context with the superblock attached

**Description**

Create a mount to an already configured superblock. If necessary, the
caller should invoke [`vfs_get_tree()`](api-summary.md#c.vfs_get_tree "vfs_get_tree") before calling this.

Note that this does not attach the mount to anything.

bool path_is_mountpoint(const struct [path](api-summary.md#c.path_is_mountpoint "path") \*path)
:   Check if path is a mount in the current namespace.

**Parameters**

`const struct path *path`
:   path to check

    d_mountpoint() can only be used reliably to establish if a dentry is
    not mounted in any namespace and that common case is handled inline.
    d_mountpoint() isn't aware of the possibility there may be multiple
    mounts using a given dentry in a different namespace. This function
    checks if the passed in path is a mountpoint rather than the dentry
    alone.

int may_umount_tree(struct vfsmount \*m)
:   check if a mount tree is busy

**Parameters**

`struct vfsmount *m`
:   root of mount tree

**Description**

This is called to check if a tree of mounts has any
open files, pwds, chroots or sub mounts that are
busy.

int may_umount(struct vfsmount \*mnt)
:   check if a mount point is busy

**Parameters**

`struct vfsmount *mnt`
:   root of mount

**Description**

This is called to check if a mount point has any
open files, pwds, chroots or sub mounts. If the
mount has sub mounts this will return busy
regardless of whether the sub mounts are busy.

Doesn't take quota and stuff into account. IOW, in some cases it will
give false negatives. The main reason why it's here is that we need
a non-destructive way to look for easily umountable filesystems.

struct vfsmount \*clone_private_mount(const struct [path](api-summary.md#c.clone_private_mount "path") \*path)
:   create a private clone of a path

**Parameters**

`const struct path *path`
:   path to clone

**Description**

This creates a new vfsmount, which will be the clone of **path**. The new mount
will not be attached anywhere in the namespace and will be private (i.e.
changes to the originating mount won't be propagated into this).

Release with mntput().

void mnt_set_expiry(struct vfsmount \*mnt, struct list_head \*expiry_list)
:   Put a mount on an expiration list

**Parameters**

`struct vfsmount *mnt`
:   The mount to list.

`struct list_head *expiry_list`
:   The list to add the mount to.

## The proc filesystem

### sysctl interface

int proc_dostring(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read a string sysctl

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   file position

**Description**

Reads/writes a string from/to the user buffer. If the kernel
buffer provided is not large enough to hold the string, the
string is truncated. The copied string is `NULL-terminated`.
If the string is being read by the user process, it is copied
and a newline 'n' is added. It is truncated if the buffer is
not large enough.

Returns 0 on success.

int proc_dobool(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read/write a bool

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   file position

**Description**

Reads/writes one integer value from/to the user buffer,
treated as an ASCII string.

table->data must point to a bool variable and table->maxlen must
be sizeof(bool).

Returns 0 on success.

int proc_dointvec(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read a vector of integers

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   file position

**Description**

Reads/writes up to table->maxlen/sizeof(unsigned int) integer
values from/to the user buffer, treated as an ASCII string.

Returns 0 on success.

int proc_douintvec(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read a vector of unsigned integers

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   file position

**Description**

Reads/writes up to table->maxlen/sizeof(unsigned int) unsigned integer
values from/to the user buffer, treated as an ASCII string.

Returns 0 on success.

int proc_dointvec_minmax(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read a vector of integers with min/max values

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   file position

**Description**

Reads/writes up to table->maxlen/sizeof(unsigned int) integer
values from/to the user buffer, treated as an ASCII string.

This routine will ensure the values are within the range specified by
table->extra1 (min) and table->extra2 (max).

Returns 0 on success or -EINVAL on write when the range check fails.

int proc_douintvec_minmax(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read a vector of unsigned ints with min/max values

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   file position

**Description**

Reads/writes up to table->maxlen/sizeof(unsigned int) unsigned integer
values from/to the user buffer, treated as an ASCII string. Negative
strings are not allowed.

This routine will ensure the values are within the range specified by
table->extra1 (min) and table->extra2 (max). There is a final sanity
check for UINT_MAX to avoid having to support wrap around uses from
userspace.

Returns 0 on success or -ERANGE on write when the range check fails.

int proc_dou8vec_minmax(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read a vector of unsigned chars with min/max values

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   file position

**Description**

Reads/writes up to table->maxlen/sizeof(u8) unsigned chars
values from/to the user buffer, treated as an ASCII string. Negative
strings are not allowed.

This routine will ensure the values are within the range specified by
table->extra1 (min) and table->extra2 (max).

Returns 0 on success or an error on write when the range check fails.

int proc_doulongvec_minmax(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read a vector of long integers with min/max values

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   file position

**Description**

Reads/writes up to table->maxlen/sizeof(unsigned long) unsigned long
values from/to the user buffer, treated as an ASCII string.

This routine will ensure the values are within the range specified by
table->extra1 (min) and table->extra2 (max).

Returns 0 on success.

int proc_doulongvec_ms_jiffies_minmax(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read a vector of millisecond values with min/max values

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   file position

**Description**

Reads/writes up to table->maxlen/sizeof(unsigned long) unsigned long
values from/to the user buffer, treated as an ASCII string. The values
are treated as milliseconds, and converted to jiffies when they are stored.

This routine will ensure the values are within the range specified by
table->extra1 (min) and table->extra2 (max).

Returns 0 on success.

int proc_dointvec_jiffies(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read a vector of integers as seconds

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   file position

**Description**

Reads/writes up to table->maxlen/sizeof(unsigned int) integer
values from/to the user buffer, treated as an ASCII string.
The values read are assumed to be in seconds, and are converted into
jiffies.

Returns 0 on success.

int proc_dointvec_userhz_jiffies(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read a vector of integers as 1/USER_HZ seconds

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   pointer to the file position

**Description**

Reads/writes up to table->maxlen/sizeof(unsigned int) integer
values from/to the user buffer, treated as an ASCII string.
The values read are assumed to be in 1/USER_HZ seconds, and
are converted into jiffies.

Returns 0 on success.

int proc_dointvec_ms_jiffies(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read a vector of integers as 1 milliseconds

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   the current position in the file

**Description**

Reads/writes up to table->maxlen/sizeof(unsigned int) integer
values from/to the user buffer, treated as an ASCII string.
The values read are assumed to be in 1/1000 seconds, and
are converted into jiffies.

Returns 0 on success.

int proc_do_large_bitmap(struct ctl_table \*table, int write, void \*buffer, size_t \*lenp, loff_t \*ppos)
:   read/write from/to a large bitmap

**Parameters**

`struct ctl_table *table`
:   the sysctl table

`int write`
:   `TRUE` if this is a write to the sysctl file

`void *buffer`
:   the user buffer

`size_t *lenp`
:   the size of the user buffer

`loff_t *ppos`
:   file position

**Description**

The bitmap is stored at table->data and the bitmap length (in bits)
in table->maxlen.

We use a range comma separated format (e.g. 1,3-4,10-10) so that
large bitmaps may be represented in a compact manner. Writing into
the file will clear the bitmap then update it with the given input.

Returns 0 on success.

### proc filesystem interface

void proc_flush_pid(struct [pid](api-summary.md#c.proc_flush_pid "pid") \*pid)
:   Remove dcache entries for **pid** from the /proc dcache.

**Parameters**

`struct pid *pid`
:   pid that should be flushed.

**Description**

This function walks a list of inodes (that belong to any proc
filesystem) that are attached to the pid and flushes them from
the dentry cache.

It is safe and reasonable to cache /proc entries for a task until
that task exits. After that they just clog up the dcache with
useless entries, possibly causing useful dcache entries to be
flushed instead. This routine is provided to flush those useless
dcache entries when a process is reaped.

**NOTE**

This routine is just an optimization so it does not guarantee
:   that no dcache entries will exist after a process is reaped
    it just makes it very unlikely that any will persist.

## Events based on file descriptors

void eventfd_signal_mask(struct eventfd_ctx \*ctx, __poll_t mask)
:   Increment the event counter

**Parameters**

`struct eventfd_ctx *ctx`
:   [in] Pointer to the eventfd context.

`__poll_t mask`
:   [in] poll mask

**Description**

This function is supposed to be called by the kernel in paths that do not
allow sleeping. In this function we allow the counter to reach the ULLONG_MAX
value, and we signal this as overflow condition by returning a EPOLLERR
to poll(2).

void eventfd_ctx_put(struct eventfd_ctx \*ctx)
:   Releases a reference to the internal eventfd context.

**Parameters**

`struct eventfd_ctx *ctx`
:   [in] Pointer to eventfd context.

**Description**

The eventfd context reference must have been previously acquired either
with [`eventfd_ctx_fdget()`](api-summary.md#c.eventfd_ctx_fdget "eventfd_ctx_fdget") or [`eventfd_ctx_fileget()`](api-summary.md#c.eventfd_ctx_fileget "eventfd_ctx_fileget").

int eventfd_ctx_remove_wait_queue(struct eventfd_ctx \*ctx, wait_queue_entry_t \*wait, __u64 \*cnt)
:   Read the current counter and removes wait queue.

**Parameters**

`struct eventfd_ctx *ctx`
:   [in] Pointer to eventfd context.

`wait_queue_entry_t *wait`
:   [in] Wait queue to be removed.

`__u64 *cnt`
:   [out] Pointer to the 64-bit counter value.

**Description**

Returns `0` if successful, or the following error codes:

`-EAGAIN`
:   : The operation would have blocked.

This is used to atomically remove a wait queue entry from the eventfd wait
queue head, and read/reset the counter value.

struct file \*eventfd_fget(int fd)
:   Acquire a reference of an eventfd file descriptor.

**Parameters**

`int fd`
:   [in] Eventfd file descriptor.

**Description**

Returns a pointer to the eventfd file structure in case of success, or the
following error pointer:

`-EBADF`
:   : Invalid **fd** file descriptor.

`-EINVAL`
:   : The **fd** file descriptor is not an eventfd file.

struct eventfd_ctx \*eventfd_ctx_fdget(int fd)
:   Acquires a reference to the internal eventfd context.

**Parameters**

`int fd`
:   [in] Eventfd file descriptor.

**Description**

Returns a pointer to the internal eventfd context, otherwise the error
pointers returned by the following functions:

eventfd_fget

struct eventfd_ctx \*eventfd_ctx_fileget(struct [file](api-summary.md#c.eventfd_ctx_fileget "file") \*file)
:   Acquires a reference to the internal eventfd context.

**Parameters**

`struct file *file`
:   [in] Eventfd file pointer.

**Description**

Returns a pointer to the internal eventfd context, otherwise the error
pointer:

`-EINVAL`
:   : The **fd** file descriptor is not an eventfd file.

## eventpoll (epoll) interfaces

int ep_events_available(struct eventpoll \*ep)
:   Checks if ready events might be available.

**Parameters**

`struct eventpoll *ep`
:   Pointer to the eventpoll context.

**Return**

a value different than `zero` if ready events are available,
:   or `zero` otherwise.

int reverse_path_check(void)
:   The tfile_check_list is list of epitem_head, which have links that are proposed to be newly added. We need to make sure that those added links don't add too many paths such that we will spend all our time waking up eventpoll objects.

**Parameters**

`void`
:   no arguments

**Return**

`zero` if the proposed links don't create too many paths,
:   `-1` otherwise.

int ep_poll(struct eventpoll \*ep, struct epoll_event __user \*events, int maxevents, struct timespec64 \*timeout)
:   Retrieves ready events, and delivers them to the caller-supplied event buffer.

**Parameters**

`struct eventpoll *ep`
:   Pointer to the eventpoll context.

`struct epoll_event __user *events`
:   Pointer to the userspace buffer where the ready events should be
    stored.

`int maxevents`
:   Size (in terms of number of events) of the caller event buffer.

`struct timespec64 *timeout`
:   Maximum timeout for the ready events fetch operation, in
    timespec. If the timeout is zero, the function will not block,
    while if the **timeout** ptr is NULL, the function will block
    until at least one event has been retrieved (or an error
    occurred).

**Return**

the number of ready events which have been fetched, or an
:   error code, in case of error.

int ep_loop_check_proc(struct eventpoll \*ep, int depth)
:   verify that adding an epoll file inside another epoll structure does not violate the constraints, in terms of closed loops, or too deep chains (which can result in excessive stack usage).

**Parameters**

`struct eventpoll *ep`
:   the `struct eventpoll` to be currently checked.

`int depth`
:   Current depth of the path being checked.

**Return**

`zero` if adding the epoll **file** inside current epoll
:   structure **ep** does not violate the constraints, or `-1` otherwise.

int ep_loop_check(struct eventpoll \*ep, struct eventpoll \*to)
:   Performs a check to verify that adding an epoll file (**to**) into another epoll file (represented by **ep**) does not create closed loops or too deep chains.

**Parameters**

`struct eventpoll *ep`
:   Pointer to the epoll we are inserting into.

`struct eventpoll *to`
:   Pointer to the epoll to be inserted.

**Return**

`zero` if adding the epoll **to** inside the epoll **from**
does not violate the constraints, or `-1` otherwise.

## The Filesystem for Exporting Kernel Objects

int sysfs_create_file_ns(struct kobject \*kobj, const struct attribute \*attr, const void \*ns)
:   create an attribute file for an object with custom ns

**Parameters**

`struct kobject *kobj`
:   object we're creating for

`const struct attribute *attr`
:   attribute descriptor

`const void *ns`
:   namespace the new file should belong to

int sysfs_add_file_to_group(struct kobject \*kobj, const struct attribute \*attr, const char \*group)
:   add an attribute file to a pre-existing group.

**Parameters**

`struct kobject *kobj`
:   object we're acting for.

`const struct attribute *attr`
:   attribute descriptor.

`const char *group`
:   group name.

int sysfs_chmod_file(struct kobject \*kobj, const struct attribute \*attr, umode_t mode)
:   update the modified mode value on an object attribute.

**Parameters**

`struct kobject *kobj`
:   object we're acting for.

`const struct attribute *attr`
:   attribute descriptor.

`umode_t mode`
:   file permissions.

struct kernfs_node \*sysfs_break_active_protection(struct kobject \*kobj, const struct attribute \*attr)
:   break "active" protection

**Parameters**

`struct kobject *kobj`
:   The kernel object **attr** is associated with.

`const struct attribute *attr`
:   The attribute to break the "active" protection for.

**Description**

With sysfs, just like kernfs, deletion of an attribute is postponed until
all active .show() and .store() callbacks have finished unless this function
is called. Hence this function is useful in methods that implement self
deletion.

void sysfs_unbreak_active_protection(struct kernfs_node \*kn)
:   restore "active" protection

**Parameters**

`struct kernfs_node *kn`
:   Pointer returned by [`sysfs_break_active_protection()`](api-summary.md#c.sysfs_break_active_protection "sysfs_break_active_protection").

**Description**

Undo the effects of [`sysfs_break_active_protection()`](api-summary.md#c.sysfs_break_active_protection "sysfs_break_active_protection"). Since this function
calls kernfs_put() on the kernfs node that corresponds to the 'attr'
argument passed to [`sysfs_break_active_protection()`](api-summary.md#c.sysfs_break_active_protection "sysfs_break_active_protection") that attribute may have
been removed between the [`sysfs_break_active_protection()`](api-summary.md#c.sysfs_break_active_protection "sysfs_break_active_protection") and
[`sysfs_unbreak_active_protection()`](api-summary.md#c.sysfs_unbreak_active_protection "sysfs_unbreak_active_protection") calls, it is not safe to access **kn** after
this function has returned.

void sysfs_remove_file_ns(struct kobject \*kobj, const struct attribute \*attr, const void \*ns)
:   remove an object attribute with a custom ns tag

**Parameters**

`struct kobject *kobj`
:   object we're acting for

`const struct attribute *attr`
:   attribute descriptor

`const void *ns`
:   namespace tag of the file to remove

**Description**

Hash the attribute name and namespace tag and kill the victim.

bool sysfs_remove_file_self(struct kobject \*kobj, const struct attribute \*attr)
:   remove an object attribute from its own method

**Parameters**

`struct kobject *kobj`
:   object we're acting for

`const struct attribute *attr`
:   attribute descriptor

**Description**

See kernfs_remove_self() for details.

void sysfs_remove_file_from_group(struct kobject \*kobj, const struct attribute \*attr, const char \*group)
:   remove an attribute file from a group.

**Parameters**

`struct kobject *kobj`
:   object we're acting for.

`const struct attribute *attr`
:   attribute descriptor.

`const char *group`
:   group name.

int sysfs_create_bin_file(struct kobject \*kobj, const struct bin_attribute \*attr)
:   create binary file for object.

**Parameters**

`struct kobject *kobj`
:   object.

`const struct bin_attribute *attr`
:   attribute descriptor.

void sysfs_remove_bin_file(struct kobject \*kobj, const struct bin_attribute \*attr)
:   remove binary file for object.

**Parameters**

`struct kobject *kobj`
:   object.

`const struct bin_attribute *attr`
:   attribute descriptor.

int sysfs_file_change_owner(struct kobject \*kobj, const char \*name, kuid_t kuid, kgid_t kgid)
:   change owner of a sysfs file.

**Parameters**

`struct kobject *kobj`
:   object.

`const char *name`
:   name of the file to change.

`kuid_t kuid`
:   new owner's kuid

`kgid_t kgid`
:   new owner's kgid

**Description**

This function looks up the sysfs entry **name** under **kobj** and changes the
ownership to **kuid**/**kgid**.

Returns 0 on success or error code on failure.

int sysfs_change_owner(struct kobject \*kobj, kuid_t kuid, kgid_t kgid)
:   change owner of the given object.

**Parameters**

`struct kobject *kobj`
:   object.

`kuid_t kuid`
:   new owner's kuid

`kgid_t kgid`
:   new owner's kgid

**Description**

Change the owner of the default directory, files, groups, and attributes of
**kobj** to **kuid**/**kgid**. Note that sysfs_change_owner mirrors how the sysfs
entries for a kobject are added by driver core. In summary,
[`sysfs_change_owner()`](api-summary.md#c.sysfs_change_owner "sysfs_change_owner") takes care of the default directory entry for **kobj**,
the default attributes associated with the ktype of **kobj** and the default
attributes associated with the ktype of **kobj**.
Additional properties not added by driver core have to be changed by the
driver or subsystem which created them. This is similar to how
driver/subsystem specific entries are removed.

Returns 0 on success or error code on failure.

int sysfs_emit(char \*buf, const char \*fmt, ...)
:   scnprintf equivalent, aware of PAGE_SIZE buffer.

**Parameters**

`char *buf`
:   start of PAGE_SIZE buffer.

`const char *fmt`
:   format

`...`
:   optional arguments to **format**

**Description**

Returns number of characters written to **buf**.

int sysfs_emit_at(char \*buf, int at, const char \*fmt, ...)
:   scnprintf equivalent, aware of PAGE_SIZE buffer.

**Parameters**

`char *buf`
:   start of PAGE_SIZE buffer.

`int at`
:   offset in **buf** to start write in bytes
    **at** must be >= 0 && < PAGE_SIZE

`const char *fmt`
:   format

`...`
:   optional arguments to **fmt**

**Description**

Returns number of characters written starting at &\*\*buf\*\*[**at**].

int sysfs_create_link(struct kobject \*kobj, struct kobject \*target, const char \*name)
:   create symlink between two objects.

**Parameters**

`struct kobject *kobj`
:   object whose directory we're creating the link in.

`struct kobject *target`
:   object we're pointing to.

`const char *name`
:   name of the symlink.

int sysfs_create_link_nowarn(struct kobject \*kobj, struct kobject \*target, const char \*name)
:   create symlink between two objects.

**Parameters**

`struct kobject *kobj`
:   object whose directory we're creating the link in.

`struct kobject *target`
:   object we're pointing to.

`const char *name`
:   name of the symlink.

    This function does the same as [`sysfs_create_link()`](api-summary.md#c.sysfs_create_link "sysfs_create_link"), but it
    doesn't warn if the link already exists.

void sysfs_remove_link(struct kobject \*kobj, const char \*name)
:   remove symlink in object's directory.

**Parameters**

`struct kobject *kobj`
:   object we're acting for.

`const char *name`
:   name of the symlink to remove.

int sysfs_rename_link_ns(struct kobject \*kobj, struct kobject \*targ, const char \*old, const char \*new, const void \*new_ns)
:   rename symlink in object's directory.

**Parameters**

`struct kobject *kobj`
:   object we're acting for.

`struct kobject *targ`
:   object we're pointing to.

`const char *old`
:   previous name of the symlink.

`const char *new`
:   new name of the symlink.

`const void *new_ns`
:   new namespace of the symlink.

    A helper function for the common rename symlink idiom.

## The debugfs filesystem

### debugfs interface

struct dentry \*debugfs_lookup(const char \*name, struct dentry \*parent)
:   look up an existing debugfs file

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to look up.

`struct dentry *parent`
:   a pointer to the parent dentry of the file.

**Description**

This function will return a pointer to a dentry if it succeeds. If the file
doesn't exist or an error occurs, `NULL` will be returned. The returned
dentry must be passed to dput() when it is no longer needed.

If debugfs is not enabled in the kernel, the value -`ENODEV` will be
returned.

struct dentry \*debugfs_create_file(const char \*name, umode_t mode, struct dentry \*parent, void \*data, const struct file_operations \*fops)
:   create a file in the debugfs filesystem

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have.

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is NULL, then the
    file will be created in the root of the debugfs filesystem.

`void *data`
:   a pointer to something that the caller will want to get to later
    on. The inode.i_private pointer will point to this value on
    the open() call.

`const struct file_operations *fops`
:   a pointer to a struct file_operations that should be used for
    this file.

**Description**

This is the basic "create a file" function for debugfs. It allows for a
wide range of flexibility in creating a file, or a directory (if you want
to create a directory, the [`debugfs_create_dir()`](api-summary.md#c.debugfs_create_dir "debugfs_create_dir") function is
recommended to be used instead.)

This function will return a pointer to a dentry if it succeeds. This
pointer must be passed to the [`debugfs_remove()`](api-summary.md#c.debugfs_remove "debugfs_remove") function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.) If an error occurs, ERR_PTR(-ERROR) will be
returned.

If debugfs is not enabled in the kernel, the value -`ENODEV` will be
returned.

**NOTE**

it's expected that most callers should _ignore_ the errors returned
by this function. Other debugfs functions handle the fact that the "dentry"
passed to them could be an error and they don't crash in that case.
Drivers should generally work fine even if debugfs fails to init anyway.

struct dentry \*debugfs_create_file_unsafe(const char \*name, umode_t mode, struct dentry \*parent, void \*data, const struct file_operations \*fops)
:   create a file in the debugfs filesystem

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have.

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is NULL, then the
    file will be created in the root of the debugfs filesystem.

`void *data`
:   a pointer to something that the caller will want to get to later
    on. The inode.i_private pointer will point to this value on
    the open() call.

`const struct file_operations *fops`
:   a pointer to a struct file_operations that should be used for
    this file.

**Description**

[`debugfs_create_file_unsafe()`](api-summary.md#c.debugfs_create_file_unsafe "debugfs_create_file_unsafe") is completely analogous to
[`debugfs_create_file()`](api-summary.md#c.debugfs_create_file "debugfs_create_file"), the only difference being that the fops
handed it will not get protected against file removals by the
debugfs core.

It is your responsibility to protect your struct file_operation
methods against file removals by means of [`debugfs_file_get()`](api-summary.md#c.debugfs_file_get "debugfs_file_get")
and [`debugfs_file_put()`](api-summary.md#c.debugfs_file_put "debugfs_file_put"). ->open() is still protected by
debugfs though.

Any struct file_operations defined by means of
DEFINE_DEBUGFS_ATTRIBUTE() is protected against file removals and
thus, may be used here.

void debugfs_create_file_size(const char \*name, umode_t mode, struct dentry \*parent, void \*data, const struct file_operations \*fops, loff_t file_size)
:   create a file in the debugfs filesystem

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have.

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is NULL, then the
    file will be created in the root of the debugfs filesystem.

`void *data`
:   a pointer to something that the caller will want to get to later
    on. The inode.i_private pointer will point to this value on
    the open() call.

`const struct file_operations *fops`
:   a pointer to a struct file_operations that should be used for
    this file.

`loff_t file_size`
:   initial file size

**Description**

This is the basic "create a file" function for debugfs. It allows for a
wide range of flexibility in creating a file, or a directory (if you want
to create a directory, the [`debugfs_create_dir()`](api-summary.md#c.debugfs_create_dir "debugfs_create_dir") function is
recommended to be used instead.)

struct dentry \*debugfs_create_dir(const char \*name, struct dentry \*parent)
:   create a directory in the debugfs filesystem

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the directory to
    create.

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is NULL, then the
    directory will be created in the root of the debugfs filesystem.

**Description**

This function creates a directory in debugfs with the given name.

This function will return a pointer to a dentry if it succeeds. This
pointer must be passed to the [`debugfs_remove()`](api-summary.md#c.debugfs_remove "debugfs_remove") function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.) If an error occurs, ERR_PTR(-ERROR) will be
returned.

If debugfs is not enabled in the kernel, the value -`ENODEV` will be
returned.

**NOTE**

it's expected that most callers should _ignore_ the errors returned
by this function. Other debugfs functions handle the fact that the "dentry"
passed to them could be an error and they don't crash in that case.
Drivers should generally work fine even if debugfs fails to init anyway.

struct dentry \*debugfs_create_automount(const char \*name, struct dentry \*parent, debugfs_automount_t f, void \*data)
:   create automount point in the debugfs filesystem

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is NULL, then the
    file will be created in the root of the debugfs filesystem.

`debugfs_automount_t f`
:   function to be called when pathname resolution steps on that one.

`void *data`
:   opaque argument to pass to f().

**Description**

**f** should return what ->d_automount() would.

struct dentry \*debugfs_create_symlink(const char \*name, struct dentry \*parent, const char \*target)
:   create a symbolic link in the debugfs filesystem

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the symbolic link to
    create.

`struct dentry *parent`
:   a pointer to the parent dentry for this symbolic link. This
    should be a directory dentry if set. If this parameter is NULL,
    then the symbolic link will be created in the root of the debugfs
    filesystem.

`const char *target`
:   a pointer to a string containing the path to the target of the
    symbolic link.

**Description**

This function creates a symbolic link with the given name in debugfs that
links to the given target path.

This function will return a pointer to a dentry if it succeeds. This
pointer must be passed to the [`debugfs_remove()`](api-summary.md#c.debugfs_remove "debugfs_remove") function when the symbolic
link is to be removed (no automatic cleanup happens if your module is
unloaded, you are responsible here.) If an error occurs, ERR_PTR(-ERROR)
will be returned.

If debugfs is not enabled in the kernel, the value -`ENODEV` will be
returned.

void debugfs_remove(struct [dentry](api-summary.md#c.debugfs_remove "dentry") \*dentry)
:   recursively removes a directory

**Parameters**

`struct dentry *dentry`
:   a pointer to a the dentry of the directory to be removed. If this
    parameter is NULL or an error value, nothing will be done.

**Description**

This function recursively removes a directory tree in debugfs that
was previously created with a call to another debugfs function
(like [`debugfs_create_file()`](api-summary.md#c.debugfs_create_file "debugfs_create_file") or variants thereof.)

This function is required to be called in order for the file to be
removed, no automatic cleanup of files will happen when a module is
removed, you are responsible here.

void debugfs_lookup_and_remove(const char \*name, struct dentry \*parent)
:   lookup a directory or file and recursively remove it

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the item to look up.

`struct dentry *parent`
:   a pointer to the parent dentry of the item.

**Description**

This is the equlivant of doing something like
debugfs_remove(debugfs_lookup(..)) but with the proper reference counting
handled for the directory being looked up.

struct dentry \*debugfs_rename(struct dentry \*old_dir, struct dentry \*old_dentry, struct dentry \*new_dir, const char \*new_name)
:   rename a file/directory in the debugfs filesystem

**Parameters**

`struct dentry *old_dir`
:   a pointer to the parent dentry for the renamed object. This
    should be a directory dentry.

`struct dentry *old_dentry`
:   dentry of an object to be renamed.

`struct dentry *new_dir`
:   a pointer to the parent dentry where the object should be
    moved. This should be a directory dentry.

`const char *new_name`
:   a pointer to a string containing the target name.

**Description**

This function renames a file/directory in debugfs. The target must not
exist for rename to succeed.

This function will return a pointer to old_dentry (which is updated to
reflect renaming) if it succeeds. If an error occurs, ERR_PTR(-ERROR)
will be returned.

If debugfs is not enabled in the kernel, the value -`ENODEV` will be
returned.

bool debugfs_initialized(void)
:   Tells whether debugfs has been registered

**Parameters**

`void`
:   no arguments

int debugfs_file_get(struct [dentry](api-summary.md#c.debugfs_file_get "dentry") \*dentry)
:   mark the beginning of file data access

**Parameters**

`struct dentry *dentry`
:   the dentry object whose data is being accessed.

**Description**

Up to a matching call to [`debugfs_file_put()`](api-summary.md#c.debugfs_file_put "debugfs_file_put"), any successive call
into the file removing functions [`debugfs_remove()`](api-summary.md#c.debugfs_remove "debugfs_remove") and
debugfs_remove_recursive() will block. Since associated private
file data may only get freed after a successful return of any of
the removal functions, you may safely access it after a successful
call to [`debugfs_file_get()`](api-summary.md#c.debugfs_file_get "debugfs_file_get") without worrying about lifetime issues.

If -`EIO` is returned, the file has already been removed and thus,
it is not safe to access any of its data. If, on the other hand,
it is allowed to access the file data, zero is returned.

void debugfs_file_put(struct [dentry](api-summary.md#c.debugfs_file_put "dentry") \*dentry)
:   mark the end of file data access

**Parameters**

`struct dentry *dentry`
:   the dentry object formerly passed to
    [`debugfs_file_get()`](api-summary.md#c.debugfs_file_get "debugfs_file_get").

**Description**

Allow any ongoing concurrent call into [`debugfs_remove()`](api-summary.md#c.debugfs_remove "debugfs_remove") or
debugfs_remove_recursive() blocked by a former call to
[`debugfs_file_get()`](api-summary.md#c.debugfs_file_get "debugfs_file_get") to proceed and return to its caller.

void debugfs_enter_cancellation(struct [file](api-summary.md#c.debugfs_enter_cancellation "file") \*file, struct debugfs_cancellation \*cancellation)
:   enter a debugfs cancellation

**Parameters**

`struct file *file`
:   the file being accessed

`struct debugfs_cancellation *cancellation`
:   the cancellation object, the cancel callback
    inside of it must be initialized

**Description**

When a debugfs file is removed it needs to wait for all active
operations to complete. However, the operation itself may need
to wait for hardware or completion of some asynchronous process
or similar. As such, it may need to be cancelled to avoid long
waits or even deadlocks.

This function can be used inside a debugfs handler that may
need to be cancelled. As soon as this function is called, the
cancellation's 'cancel' callback may be called, at which point
the caller should proceed to call [`debugfs_leave_cancellation()`](api-summary.md#c.debugfs_leave_cancellation "debugfs_leave_cancellation")
and leave the debugfs handler function as soon as possible.
Note that the 'cancel' callback is only ever called in the
context of some kind of [`debugfs_remove()`](api-summary.md#c.debugfs_remove "debugfs_remove").

This function must be paired with [`debugfs_leave_cancellation()`](api-summary.md#c.debugfs_leave_cancellation "debugfs_leave_cancellation").

void debugfs_leave_cancellation(struct [file](api-summary.md#c.debugfs_leave_cancellation "file") \*file, struct debugfs_cancellation \*cancellation)
:   leave cancellation section

**Parameters**

`struct file *file`
:   the file being accessed

`struct debugfs_cancellation *cancellation`
:   the cancellation previously registered with
    [`debugfs_enter_cancellation()`](api-summary.md#c.debugfs_enter_cancellation "debugfs_enter_cancellation")

**Description**

See the documentation of [`debugfs_enter_cancellation()`](api-summary.md#c.debugfs_enter_cancellation "debugfs_enter_cancellation").

void debugfs_create_u8(const char \*name, umode_t mode, struct dentry \*parent, u8 \*value)
:   create a debugfs file that is used to read and write an unsigned 8-bit value

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`u8 *value`
:   a pointer to the variable that the file should read to and write
    from.

**Description**

This function creates a file in debugfs with the given name that
contains the value of the variable **value**. If the **mode** variable is so
set, it can be read from, and written to.

void debugfs_create_u16(const char \*name, umode_t mode, struct dentry \*parent, u16 \*value)
:   create a debugfs file that is used to read and write an unsigned 16-bit value

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`u16 *value`
:   a pointer to the variable that the file should read to and write
    from.

**Description**

This function creates a file in debugfs with the given name that
contains the value of the variable **value**. If the **mode** variable is so
set, it can be read from, and written to.

void debugfs_create_u32(const char \*name, umode_t mode, struct dentry \*parent, u32 \*value)
:   create a debugfs file that is used to read and write an unsigned 32-bit value

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`u32 *value`
:   a pointer to the variable that the file should read to and write
    from.

**Description**

This function creates a file in debugfs with the given name that
contains the value of the variable **value**. If the **mode** variable is so
set, it can be read from, and written to.

void debugfs_create_u64(const char \*name, umode_t mode, struct dentry \*parent, u64 \*value)
:   create a debugfs file that is used to read and write an unsigned 64-bit value

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`u64 *value`
:   a pointer to the variable that the file should read to and write
    from.

**Description**

This function creates a file in debugfs with the given name that
contains the value of the variable **value**. If the **mode** variable is so
set, it can be read from, and written to.

void debugfs_create_ulong(const char \*name, umode_t mode, struct dentry \*parent, unsigned long \*value)
:   create a debugfs file that is used to read and write an unsigned long value.

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`unsigned long *value`
:   a pointer to the variable that the file should read to and write
    from.

**Description**

This function creates a file in debugfs with the given name that
contains the value of the variable **value**. If the **mode** variable is so
set, it can be read from, and written to.

void debugfs_create_x8(const char \*name, umode_t mode, struct dentry \*parent, u8 \*value)
:   create a debugfs file that is used to read and write an unsigned 8-bit value

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`u8 *value`
:   a pointer to the variable that the file should read to and write
    from.

void debugfs_create_x16(const char \*name, umode_t mode, struct dentry \*parent, u16 \*value)
:   create a debugfs file that is used to read and write an unsigned 16-bit value

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`u16 *value`
:   a pointer to the variable that the file should read to and write
    from.

void debugfs_create_x32(const char \*name, umode_t mode, struct dentry \*parent, u32 \*value)
:   create a debugfs file that is used to read and write an unsigned 32-bit value

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`u32 *value`
:   a pointer to the variable that the file should read to and write
    from.

void debugfs_create_x64(const char \*name, umode_t mode, struct dentry \*parent, u64 \*value)
:   create a debugfs file that is used to read and write an unsigned 64-bit value

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`u64 *value`
:   a pointer to the variable that the file should read to and write
    from.

void debugfs_create_size_t(const char \*name, umode_t mode, struct dentry \*parent, size_t \*value)
:   create a debugfs file that is used to read and write an size_t value

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`size_t *value`
:   a pointer to the variable that the file should read to and write
    from.

void debugfs_create_atomic_t(const char \*name, umode_t mode, struct dentry \*parent, atomic_t \*value)
:   create a debugfs file that is used to read and write an atomic_t value

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`atomic_t *value`
:   a pointer to the variable that the file should read to and write
    from.

void debugfs_create_bool(const char \*name, umode_t mode, struct dentry \*parent, bool \*value)
:   create a debugfs file that is used to read and write a boolean value

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`bool *value`
:   a pointer to the variable that the file should read to and write
    from.

**Description**

This function creates a file in debugfs with the given name that
contains the value of the variable **value**. If the **mode** variable is so
set, it can be read from, and written to.

void debugfs_create_str(const char \*name, umode_t mode, struct dentry \*parent, char \*\*value)
:   create a debugfs file that is used to read and write a string value

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`char **value`
:   a pointer to the variable that the file should read to and write
    from.

**Description**

This function creates a file in debugfs with the given name that
contains the value of the variable **value**. If the **mode** variable is so
set, it can be read from, and written to.

struct dentry \*debugfs_create_blob(const char \*name, umode_t mode, struct dentry \*parent, struct debugfs_blob_wrapper \*blob)
:   create a debugfs file that is used to read and write a binary blob

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`struct debugfs_blob_wrapper *blob`
:   a pointer to a struct debugfs_blob_wrapper which contains a pointer
    to the blob data and the size of the data.

**Description**

This function creates a file in debugfs with the given name that exports
**blob->data** as a binary blob. If the **mode** variable is so set it can be
read from and written to.

This function will return a pointer to a dentry if it succeeds. This
pointer must be passed to the [`debugfs_remove()`](api-summary.md#c.debugfs_remove "debugfs_remove") function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.) If an error occurs, ERR_PTR(-ERROR) will be
returned.

If debugfs is not enabled in the kernel, the value ERR_PTR(-ENODEV) will
be returned.

void debugfs_create_u32_array(const char \*name, umode_t mode, struct dentry \*parent, struct debugfs_u32_array \*array)
:   create a debugfs file that is used to read u32 array.

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have.

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`struct debugfs_u32_array *array`
:   wrapper struct containing data pointer and size of the array.

**Description**

This function creates a file in debugfs with the given name that exports
**array** as data. If the **mode** variable is so set it can be read from.
Writing is not supported. Seek within the file is also not supported.
Once array is created its size can not be changed.

void debugfs_print_regs32(struct seq_file \*s, const struct debugfs_reg32 \*regs, int nregs, void __iomem \*base, char \*prefix)
:   use seq_print to describe a set of registers

**Parameters**

`struct seq_file *s`
:   the seq_file structure being used to generate output

`const struct debugfs_reg32 *regs`
:   an array if struct debugfs_reg32 structures

`int nregs`
:   the length of the above array

`void __iomem *base`
:   the base address to be used in reading the registers

`char *prefix`
:   a string to be prefixed to every output line

**Description**

This function outputs a text block describing the current values of
some 32-bit hardware registers. It is meant to be used within debugfs
files based on seq_file that need to show registers, intermixed with other
information. The prefix argument may be used to specify a leading string,
because some peripherals have several blocks of identical registers,
for example configuration of dma channels

void debugfs_create_regset32(const char \*name, umode_t mode, struct dentry \*parent, struct debugfs_regset32 \*regset)
:   create a debugfs file that returns register values

**Parameters**

`const char *name`
:   a pointer to a string containing the name of the file to create.

`umode_t mode`
:   the permission that the file should have

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`struct debugfs_regset32 *regset`
:   a pointer to a struct debugfs_regset32, which contains a pointer
    to an array of register definitions, the array size and the base
    address where the register bank is to be found.

**Description**

This function creates a file in debugfs with the given name that reports
the names and values of a set of 32-bit registers. If the **mode** variable
is so set it can be read from. Writing is not supported.

void debugfs_create_devm_seqfile(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, const char \*name, struct dentry \*parent, int (\*read_fn)(struct seq_file \*s, void \*data))
:   create a debugfs file that is bound to device.

**Parameters**

`struct device *dev`
:   device related to this debugfs file.

`const char *name`
:   name of the debugfs file.

`struct dentry *parent`
:   a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is `NULL`, then the
    file will be created in the root of the debugfs filesystem.

`int (*read_fn)(struct seq_file *s, void *data)`
:   function pointer called to print the seq_file content.

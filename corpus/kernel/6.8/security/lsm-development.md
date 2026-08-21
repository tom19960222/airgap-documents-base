---
collection: kernel
version: "6.8"
title: "Linux Security Module Development"
source_url: https://www.kernel.org/doc/html/v6.8/security/lsm-development.html
fetched_at: 2026-08-21T03:40:18+00:00
---
# Linux Security Module Development

Based on <https://lore.kernel.org/r/20071026073721.618b4778@laptopd505.fenrus.org>,
a new LSM is accepted into the kernel when its intent (a description of
what it tries to protect against and in what cases one would expect to
use it) has been appropriately documented in `Documentation/admin-guide/LSM/`.
This allows an LSM's code to be easily compared to its goals, and so
that end users and distros can make a more informed decision about which
LSMs suit their requirements.

For extensive documentation on the available LSM hook interfaces, please
see `security/security.c` and associated structures:

void security_free_mnt_opts(void \*\*mnt_opts)
:   Free memory associated with mount options

**Parameters**

`void **mnt_opts`
:   LSM processed mount options

**Description**

Free memory associated with **mnt_ops**.

int security_sb_eat_lsm_opts(char \*options, void \*\*mnt_opts)
:   Consume LSM mount options

**Parameters**

`char *options`
:   mount options

`void **mnt_opts`
:   LSM processed mount options

**Description**

Eat (scan **options**) and save them in **mnt_opts**.

**Return**

Returns 0 on success, negative values on failure.

int security_sb_mnt_opts_compat(struct super_block \*sb, void \*mnt_opts)
:   Check if new mount options are allowed

**Parameters**

`struct super_block *sb`
:   filesystem superblock

`void *mnt_opts`
:   new mount options

**Description**

Determine if the new mount options in **mnt_opts** are allowed given the
existing mounted filesystem at **sb**. **sb** superblock being compared.

**Return**

Returns 0 if options are compatible.

int security_sb_remount(struct super_block \*sb, void \*mnt_opts)
:   Verify no incompatible mount changes during remount

**Parameters**

`struct super_block *sb`
:   filesystem superblock

`void *mnt_opts`
:   (re)mount options

**Description**

Extracts security system specific mount options and verifies no changes are
being made to those options.

**Return**

Returns 0 if permission is granted.

int security_sb_set_mnt_opts(struct super_block \*sb, void \*mnt_opts, unsigned long kern_flags, unsigned long \*set_kern_flags)
:   Set the mount options for a filesystem

**Parameters**

`struct super_block *sb`
:   filesystem superblock

`void *mnt_opts`
:   binary mount options

`unsigned long kern_flags`
:   kernel flags (in)

`unsigned long *set_kern_flags`
:   kernel flags (out)

**Description**

Set the security relevant mount options used for a superblock.

**Return**

Returns 0 on success, error on failure.

int security_sb_clone_mnt_opts(const struct super_block \*oldsb, struct super_block \*newsb, unsigned long kern_flags, unsigned long \*set_kern_flags)
:   Duplicate superblock mount options

**Parameters**

`const struct super_block *oldsb`
:   source superblock

`struct super_block *newsb`
:   destination superblock

`unsigned long kern_flags`
:   kernel flags (in)

`unsigned long *set_kern_flags`
:   kernel flags (out)

**Description**

Copy all security options from a given superblock to another.

**Return**

Returns 0 on success, error on failure.

int security_dentry_init_security(struct [dentry](lsm-development.md#c.security_dentry_init_security "dentry") \*dentry, int mode, const struct qstr \*name, const char \*\*xattr_name, void \*\*ctx, u32 \*ctxlen)
:   Perform dentry initialization

**Parameters**

`struct dentry *dentry`
:   the dentry to initialize

`int mode`
:   mode used to determine resource type

`const struct qstr *name`
:   name of the last path component

`const char **xattr_name`
:   name of the security/LSM xattr

`void **ctx`
:   pointer to the resulting LSM context

`u32 *ctxlen`
:   length of **ctx**

**Description**

Compute a context for a dentry as the inode is not yet available since NFSv4
has no label backed by an EA anyway. It is important to note that
**xattr_name** does not need to be free'd by the caller, it is a static string.

**Return**

Returns 0 on success, negative values on failure.

int security_dentry_create_files_as(struct [dentry](lsm-development.md#c.security_dentry_create_files_as "dentry") \*dentry, int mode, struct qstr \*name, const struct cred \*old, struct cred \*new)
:   Perform dentry initialization

**Parameters**

`struct dentry *dentry`
:   the dentry to initialize

`int mode`
:   mode used to determine resource type

`struct qstr *name`
:   name of the last path component

`const struct cred *old`
:   creds to use for LSM context calculations

`struct cred *new`
:   creds to modify

**Description**

Compute a context for a dentry as the inode is not yet available and set
that context in passed in creds so that new files are created using that
context. Context is calculated using the passed in creds and not the creds
of the caller.

**Return**

Returns 0 on success, error on failure.

int security_inode_init_security(struct [inode](lsm-development.md#c.security_inode_init_security "inode") \*inode, struct [inode](lsm-development.md#c.security_inode_init_security "inode") \*dir, const struct [qstr](lsm-development.md#c.security_inode_init_security "qstr") \*qstr, const [initxattrs](lsm-development.md#c.security_inode_init_security "initxattrs") initxattrs, void \*fs_data)
:   Initialize an inode's LSM context

**Parameters**

`struct inode *inode`
:   the inode

`struct inode *dir`
:   parent directory

`const struct qstr *qstr`
:   last component of the pathname

`const initxattrs initxattrs`
:   callback function to write xattrs

`void *fs_data`
:   filesystem specific data

**Description**

Obtain the security attribute name suffix and value to set on a newly
created inode and set up the incore security field for the new inode. This
hook is called by the fs code as part of the inode creation transaction and
provides for atomic labeling of the inode, unlike the post_create/mkdir/...
hooks called by the VFS.

The hook function is expected to populate the xattrs array, by calling
lsm_get_xattr_slot() to retrieve the slots reserved by the security module
with the lbs_xattr_count field of the lsm_blob_sizes structure. For each
slot, the hook function should set ->name to the attribute name suffix
(e.g. selinux), to allocate ->value (will be freed by the caller) and set it
to the attribute value, to set ->value_len to the length of the value. If
the security module does not use security attributes or does not wish to put
a security attribute on this particular inode, then it should return
-EOPNOTSUPP to skip this processing.

**Return**

Returns 0 if the LSM successfully initialized all of the inode
:   security attributes that are required, negative values otherwise.

int security_path_mknod(const struct path \*dir, struct [dentry](lsm-development.md#c.security_path_mknod "dentry") \*dentry, umode_t mode, unsigned int dev)
:   Check if creating a special file is allowed

**Parameters**

`const struct path *dir`
:   parent directory

`struct dentry *dentry`
:   new file

`umode_t mode`
:   new file mode

`unsigned int dev`
:   device number

**Description**

Check permissions when creating a file. Note that this hook is called even
if mknod operation is being done for a regular file.

**Return**

Returns 0 if permission is granted.

int security_path_mkdir(const struct path \*dir, struct [dentry](lsm-development.md#c.security_path_mkdir "dentry") \*dentry, umode_t mode)
:   Check if creating a new directory is allowed

**Parameters**

`const struct path *dir`
:   parent directory

`struct dentry *dentry`
:   new directory

`umode_t mode`
:   new directory mode

**Description**

Check permissions to create a new directory in the existing directory.

**Return**

Returns 0 if permission is granted.

int security_path_unlink(const struct path \*dir, struct [dentry](lsm-development.md#c.security_path_unlink "dentry") \*dentry)
:   Check if removing a hard link is allowed

**Parameters**

`const struct path *dir`
:   parent directory

`struct dentry *dentry`
:   file

**Description**

Check the permission to remove a hard link to a file.

**Return**

Returns 0 if permission is granted.

int security_path_rename(const struct path \*old_dir, struct dentry \*old_dentry, const struct path \*new_dir, struct dentry \*new_dentry, unsigned int flags)
:   Check if renaming a file is allowed

**Parameters**

`const struct path *old_dir`
:   parent directory of the old file

`struct dentry *old_dentry`
:   the old file

`const struct path *new_dir`
:   parent directory of the new file

`struct dentry *new_dentry`
:   the new file

`unsigned int flags`
:   flags

**Description**

Check for permission to rename a file or directory.

**Return**

Returns 0 if permission is granted.

int security_inode_create(struct inode \*dir, struct [dentry](lsm-development.md#c.security_inode_create "dentry") \*dentry, umode_t mode)
:   Check if creating a file is allowed

**Parameters**

`struct inode *dir`
:   the parent directory

`struct dentry *dentry`
:   the file being created

`umode_t mode`
:   requested file mode

**Description**

Check permission to create a regular file.

**Return**

Returns 0 if permission is granted.

int security_inode_mkdir(struct inode \*dir, struct [dentry](lsm-development.md#c.security_inode_mkdir "dentry") \*dentry, umode_t mode)
:   Check if creation a new director is allowed

**Parameters**

`struct inode *dir`
:   parent directory

`struct dentry *dentry`
:   new directory

`umode_t mode`
:   new directory mode

**Description**

Check permissions to create a new directory in the existing directory
associated with inode structure **dir**.

**Return**

Returns 0 if permission is granted.

int security_inode_setattr(struct mnt_idmap \*idmap, struct [dentry](lsm-development.md#c.security_inode_setattr "dentry") \*dentry, struct iattr \*attr)
:   Check if setting file attributes is allowed

**Parameters**

`struct mnt_idmap *idmap`
:   idmap of the mount

`struct dentry *dentry`
:   file

`struct iattr *attr`
:   new attributes

**Description**

Check permission before setting file attributes. Note that the kernel call
to notify_change is performed from several locations, whenever file
attributes change (such as when a file is truncated, chown/chmod operations,
transferring disk quotas, etc).

**Return**

Returns 0 if permission is granted.

int security_inode_listsecurity(struct [inode](lsm-development.md#c.security_inode_listsecurity "inode") \*inode, char \*buffer, size_t buffer_size)
:   List the xattr security label names

**Parameters**

`struct inode *inode`
:   inode

`char *buffer`
:   buffer

`size_t buffer_size`
:   size of buffer

**Description**

Copy the extended attribute names for the security labels associated with
**inode** into **buffer**. The maximum size of **buffer** is specified by
**buffer_size**. **buffer** may be NULL to request the size of the buffer
required.

**Return**

Returns number of bytes used/required on success.

int security_inode_copy_up(struct dentry \*src, struct cred \*\*new)
:   Create new creds for an overlayfs copy-up op

**Parameters**

`struct dentry *src`
:   union dentry of copy-up file

`struct cred **new`
:   newly created creds

**Description**

A file is about to be copied up from lower layer to upper layer of overlay
filesystem. Security module can prepare a set of new creds and modify as
need be and return new creds. Caller will switch to new creds temporarily to
create new file and release newly allocated creds.

**Return**

Returns 0 on success or a negative error code on error.

int security_inode_copy_up_xattr(const char \*name)
:   Filter xattrs in an overlayfs copy-up op

**Parameters**

`const char *name`
:   xattr name

**Description**

Filter the xattrs being copied up when a unioned file is copied up from a
lower layer to the union/overlay layer. The caller is responsible for
reading and writing the xattrs, this hook is merely a filter.

**Return**

Returns 0 to accept the xattr, 1 to discard the xattr, -EOPNOTSUPP
:   if the security module does not know about attribute, or a negative
    error code to abort the copy up.

int security_file_ioctl(struct [file](lsm-development.md#c.security_file_ioctl "file") \*file, unsigned int cmd, unsigned long arg)
:   Check if an ioctl is allowed

**Parameters**

`struct file *file`
:   associated file

`unsigned int cmd`
:   ioctl cmd

`unsigned long arg`
:   ioctl arguments

**Description**

Check permission for an ioctl operation on **file**. Note that **arg** sometimes
represents a user space pointer; in other cases, it may be a simple integer
value. When **arg** represents a user space pointer, it should never be used
by the security module.

**Return**

Returns 0 if permission is granted.

int security_file_ioctl_compat(struct [file](lsm-development.md#c.security_file_ioctl_compat "file") \*file, unsigned int cmd, unsigned long arg)
:   Check if an ioctl is allowed in compat mode

**Parameters**

`struct file *file`
:   associated file

`unsigned int cmd`
:   ioctl cmd

`unsigned long arg`
:   ioctl arguments

**Description**

Compat version of [`security_file_ioctl()`](lsm-development.md#c.security_file_ioctl "security_file_ioctl") that correctly handles 32-bit
processes running on 64-bit kernels.

**Return**

Returns 0 if permission is granted.

void security_cred_getsecid(const struct cred \*c, u32 \*secid)
:   Get the secid from a set of credentials

**Parameters**

`const struct cred *c`
:   credentials

`u32 *secid`
:   secid value

**Description**

Retrieve the security identifier of the cred structure **c**. In case of
failure, **secid** will be set to zero.

int security_kernel_read_file(struct [file](lsm-development.md#c.security_kernel_read_file "file") \*file, enum kernel_read_file_id id, bool contents)
:   Read a file specified by userspace

**Parameters**

`struct file *file`
:   file

`enum kernel_read_file_id id`
:   file identifier

`bool contents`
:   trust if [`security_kernel_post_read_file()`](lsm-development.md#c.security_kernel_post_read_file "security_kernel_post_read_file") will be called

**Description**

Read a file specified by userspace.

**Return**

Returns 0 if permission is granted.

int security_kernel_post_read_file(struct [file](lsm-development.md#c.security_kernel_post_read_file "file") \*file, char \*buf, loff_t size, enum kernel_read_file_id id)
:   Read a file specified by userspace

**Parameters**

`struct file *file`
:   file

`char *buf`
:   file contents

`loff_t size`
:   size of file contents

`enum kernel_read_file_id id`
:   file identifier

**Description**

Read a file specified by userspace. This must be paired with a prior call
to [`security_kernel_read_file()`](lsm-development.md#c.security_kernel_read_file "security_kernel_read_file") call that indicated this hook would also be
called, see [`security_kernel_read_file()`](lsm-development.md#c.security_kernel_read_file "security_kernel_read_file") for more information.

**Return**

Returns 0 if permission is granted.

int security_kernel_load_data(enum kernel_load_data_id id, bool contents)
:   Load data provided by userspace

**Parameters**

`enum kernel_load_data_id id`
:   data identifier

`bool contents`
:   true if [`security_kernel_post_load_data()`](lsm-development.md#c.security_kernel_post_load_data "security_kernel_post_load_data") will be called

**Description**

Load data provided by userspace.

**Return**

Returns 0 if permission is granted.

int security_kernel_post_load_data(char \*buf, loff_t size, enum kernel_load_data_id id, char \*description)
:   Load userspace data from a non-file source

**Parameters**

`char *buf`
:   data

`loff_t size`
:   size of data

`enum kernel_load_data_id id`
:   data identifier

`char *description`
:   text description of data, specific to the id value

**Description**

Load data provided by a non-file source (usually userspace buffer). This
must be paired with a prior [`security_kernel_load_data()`](lsm-development.md#c.security_kernel_load_data "security_kernel_load_data") call that indicated
this hook would also be called, see [`security_kernel_load_data()`](lsm-development.md#c.security_kernel_load_data "security_kernel_load_data") for more
information.

**Return**

Returns 0 if permission is granted.

void security_current_getsecid_subj(u32 \*secid)
:   Get the current task's subjective secid

**Parameters**

`u32 *secid`
:   secid value

**Description**

Retrieve the subjective security identifier of the current task and return
it in **secid**. In case of failure, **secid** will be set to zero.

void security_task_getsecid_obj(struct task_struct \*p, u32 \*secid)
:   Get a task's objective secid

**Parameters**

`struct task_struct *p`
:   target task

`u32 *secid`
:   secid value

**Description**

Retrieve the objective security identifier of the task_struct in **p** and
return it in **secid**. In case of failure, **secid** will be set to zero.

void security_d_instantiate(struct [dentry](lsm-development.md#c.security_d_instantiate "dentry") \*dentry, struct [inode](lsm-development.md#c.security_d_instantiate "inode") \*inode)
:   Populate an inode's LSM state based on a dentry

**Parameters**

`struct dentry *dentry`
:   dentry

`struct inode *inode`
:   inode

**Description**

Fill in **inode** security information for a **dentry** if allowed.

int security_ismaclabel(const char \*name)
:   Check is the named attribute is a MAC label

**Parameters**

`const char *name`
:   full extended attribute name

**Description**

Check if the extended attribute specified by **name** represents a MAC label.

**Return**

Returns 1 if name is a MAC attribute otherwise returns 0.

int security_secid_to_secctx(u32 secid, char \*\*secdata, u32 \*seclen)
:   Convert a secid to a secctx

**Parameters**

`u32 secid`
:   secid

`char **secdata`
:   secctx

`u32 *seclen`
:   secctx length

**Description**

Convert secid to security context. If **secdata** is NULL the length of the
result will be returned in **seclen**, but no **secdata** will be returned. This
does mean that the length could change between calls to check the length and
the next call which actually allocates and returns the **secdata**.

**Return**

Return 0 on success, error on failure.

int security_secctx_to_secid(const char \*secdata, u32 seclen, u32 \*secid)
:   Convert a secctx to a secid

**Parameters**

`const char *secdata`
:   secctx

`u32 seclen`
:   length of secctx

`u32 *secid`
:   secid

**Description**

Convert security context to secid.

**Return**

Returns 0 on success, error on failure.

void security_release_secctx(char \*secdata, u32 seclen)
:   Free a secctx buffer

**Parameters**

`char *secdata`
:   secctx

`u32 seclen`
:   length of secctx

**Description**

Release the security context.

void security_inode_invalidate_secctx(struct [inode](lsm-development.md#c.security_inode_invalidate_secctx "inode") \*inode)
:   Invalidate an inode's security label

**Parameters**

`struct inode *inode`
:   inode

**Description**

Notify the security module that it must revalidate the security context of
an inode.

int security_inode_notifysecctx(struct [inode](lsm-development.md#c.security_inode_notifysecctx "inode") \*inode, void \*ctx, u32 ctxlen)
:   Notify the LSM of an inode's security label

**Parameters**

`struct inode *inode`
:   inode

`void *ctx`
:   secctx

`u32 ctxlen`
:   length of secctx

**Description**

Notify the security module of what the security context of an inode should
be. Initializes the incore security context managed by the security module
for this inode. Example usage: NFS client invokes this hook to initialize
the security context in its incore inode to the value provided by the server
for the file when the server returned the file's attributes to the client.
Must be called with inode->i_mutex locked.

**Return**

Returns 0 on success, error on failure.

int security_inode_setsecctx(struct [dentry](lsm-development.md#c.security_inode_setsecctx "dentry") \*dentry, void \*ctx, u32 ctxlen)
:   Change the security label of an inode

**Parameters**

`struct dentry *dentry`
:   inode

`void *ctx`
:   secctx

`u32 ctxlen`
:   length of secctx

**Description**

Change the security context of an inode. Updates the incore security
context managed by the security module and invokes the fs code as needed
(via __vfs_setxattr_noperm) to update any backing xattrs that represent the
context. Example usage: NFS server invokes this hook to change the security
context in its incore inode and on the backing filesystem to a value
provided by the client on a SETATTR operation. Must be called with
inode->i_mutex locked.

**Return**

Returns 0 on success, error on failure.

int security_inode_getsecctx(struct [inode](lsm-development.md#c.security_inode_getsecctx "inode") \*inode, void \*\*ctx, u32 \*ctxlen)
:   Get the security label of an inode

**Parameters**

`struct inode *inode`
:   inode

`void **ctx`
:   secctx

`u32 *ctxlen`
:   length of secctx

**Description**

On success, returns 0 and fills out **ctx** and **ctxlen** with the security
context for the given **inode**.

**Return**

Returns 0 on success, error on failure.

int security_unix_stream_connect(struct [sock](lsm-development.md#c.security_unix_stream_connect "sock") \*sock, struct [sock](lsm-development.md#c.security_unix_stream_connect "sock") \*other, struct [sock](lsm-development.md#c.security_unix_stream_connect "sock") \*newsk)
:   Check if a AF_UNIX stream is allowed

**Parameters**

`struct sock *sock`
:   originating sock

`struct sock *other`
:   peer sock

`struct sock *newsk`
:   new sock

**Description**

Check permissions before establishing a Unix domain stream connection
between **sock** and **other**.

The **unix_stream_connect** and **unix_may_send** hooks were necessary because
Linux provides an alternative to the conventional file name space for Unix
domain sockets. Whereas binding and connecting to sockets in the file name
space is mediated by the typical file permissions (and caught by the mknod
and permission hooks in inode_security_ops), binding and connecting to
sockets in the abstract name space is completely unmediated. Sufficient
control of Unix domain sockets in the abstract name space isn't possible
using only the socket layer hooks, since we need to know the actual target
socket, which is not looked up until we are inside the af_unix code.

**Return**

Returns 0 if permission is granted.

int security_unix_may_send(struct [socket](../networking/kapi.md#c.socket "socket") \*sock, struct [socket](../networking/kapi.md#c.socket "socket") \*other)
:   Check if AF_UNIX socket can send datagrams

**Parameters**

`struct socket *sock`
:   originating sock

`struct socket *other`
:   peer sock

**Description**

Check permissions before connecting or sending datagrams from **sock** to
**other**.

The **unix_stream_connect** and **unix_may_send** hooks were necessary because
Linux provides an alternative to the conventional file name space for Unix
domain sockets. Whereas binding and connecting to sockets in the file name
space is mediated by the typical file permissions (and caught by the mknod
and permission hooks in inode_security_ops), binding and connecting to
sockets in the abstract name space is completely unmediated. Sufficient
control of Unix domain sockets in the abstract name space isn't possible
using only the socket layer hooks, since we need to know the actual target
socket, which is not looked up until we are inside the af_unix code.

**Return**

Returns 0 if permission is granted.

int security_socket_socketpair(struct [socket](../networking/kapi.md#c.socket "socket") \*socka, struct [socket](../networking/kapi.md#c.socket "socket") \*sockb)
:   Check if creating a socketpair is allowed

**Parameters**

`struct socket *socka`
:   first socket

`struct socket *sockb`
:   second socket

**Description**

Check permissions before creating a fresh pair of sockets.

**Return**

Returns 0 if permission is granted and the connection was
:   established.

int security_sock_rcv_skb(struct [sock](../networking/kapi.md#c.sock "sock") \*sk, struct [sk_buff](../networking/kapi.md#c.sk_buff "sk_buff") \*skb)
:   Check if an incoming network packet is allowed

**Parameters**

`struct sock *sk`
:   destination sock

`struct sk_buff *skb`
:   incoming packet

**Description**

Check permissions on incoming network packets. This hook is distinct from
Netfilter's IP input hooks since it is the first time that the incoming
sk_buff **skb** has been associated with a particular socket, **sk**. Must not
sleep inside this hook because some callers hold spinlocks.

**Return**

Returns 0 if permission is granted.

int security_socket_getpeersec_dgram(struct [socket](../networking/kapi.md#c.socket "socket") \*sock, struct [sk_buff](../networking/kapi.md#c.sk_buff "sk_buff") \*skb, u32 \*secid)
:   Get the remote peer label

**Parameters**

`struct socket *sock`
:   socket

`struct sk_buff *skb`
:   datagram packet

`u32 *secid`
:   remote peer label secid

**Description**

This hook allows the security module to provide peer socket security state
for udp sockets on a per-packet basis to userspace via getsockopt
SO_GETPEERSEC. The application must first have indicated the IP_PASSSEC
option via getsockopt. It can then retrieve the security state returned by
this hook for a packet via the SCM_SECURITY ancillary message type.

**Return**

Returns 0 on success, error on failure.

void security_sk_clone(const struct [sock](../networking/kapi.md#c.sock "sock") \*sk, struct [sock](../networking/kapi.md#c.sock "sock") \*newsk)
:   Clone a sock's LSM state

**Parameters**

`const struct sock *sk`
:   original sock

`struct sock *newsk`
:   target sock

**Description**

Clone/copy security structure.

void security_sk_classify_flow(const struct [sock](../networking/kapi.md#c.sock "sock") \*sk, struct flowi_common \*flic)
:   Set a flow's secid based on socket

**Parameters**

`const struct sock *sk`
:   original socket

`struct flowi_common *flic`
:   target flow

**Description**

Set the target flow's secid to socket's secid.

void security_req_classify_flow(const struct request_sock \*req, struct flowi_common \*flic)
:   Set a flow's secid based on request_sock

**Parameters**

`const struct request_sock *req`
:   request_sock

`struct flowi_common *flic`
:   target flow

**Description**

Sets **flic**'s secid to **req**'s secid.

void security_sock_graft(struct [sock](../networking/kapi.md#c.sock "sock") \*sk, struct [socket](../networking/kapi.md#c.socket "socket") \*parent)
:   Reconcile LSM state when grafting a sock on a socket

**Parameters**

`struct sock *sk`
:   sock being grafted

`struct socket *parent`
:   target parent socket

**Description**

Sets **parent**'s inode secid to **sk**'s secid and update **sk** with any necessary
LSM state from **parent**.

int security_inet_conn_request(const struct [sock](../networking/kapi.md#c.sock "sock") \*sk, struct [sk_buff](../networking/kapi.md#c.sk_buff "sk_buff") \*skb, struct request_sock \*req)
:   Set request_sock state using incoming connect

**Parameters**

`const struct sock *sk`
:   parent listening sock

`struct sk_buff *skb`
:   incoming connection

`struct request_sock *req`
:   new request_sock

**Description**

Initialize the **req** LSM state based on **sk** and the incoming connect in **skb**.

**Return**

Returns 0 if permission is granted.

void security_inet_conn_established(struct [sock](../networking/kapi.md#c.sock "sock") \*sk, struct [sk_buff](../networking/kapi.md#c.sk_buff "sk_buff") \*skb)
:   Update sock's LSM state with connection

**Parameters**

`struct sock *sk`
:   sock

`struct sk_buff *skb`
:   connection packet

**Description**

Update **sock**'s LSM state to represent a new connection from **skb**.

int security_secmark_relabel_packet(u32 secid)
:   Check if setting a secmark is allowed

**Parameters**

`u32 secid`
:   new secmark value

**Description**

Check if the process should be allowed to relabel packets to **secid**.

**Return**

Returns 0 if permission is granted.

void security_secmark_refcount_inc(void)
:   Increment the secmark labeling rule count

**Parameters**

`void`
:   no arguments

**Description**

Tells the LSM to increment the number of secmark labeling rules loaded.

void security_secmark_refcount_dec(void)
:   Decrement the secmark labeling rule count

**Parameters**

`void`
:   no arguments

**Description**

Tells the LSM to decrement the number of secmark labeling rules loaded.

int security_tun_dev_alloc_security(void \*\*security)
:   Allocate a LSM blob for a TUN device

**Parameters**

`void **security`
:   pointer to the LSM blob

**Description**

This hook allows a module to allocate a security structure for a TUN device,
returning the pointer in **security**.

**Return**

Returns a zero on success, negative values on failure.

void security_tun_dev_free_security(void \*security)
:   Free a TUN device LSM blob

**Parameters**

`void *security`
:   LSM blob

**Description**

This hook allows a module to free the security structure for a TUN device.

int security_tun_dev_create(void)
:   Check if creating a TUN device is allowed

**Parameters**

`void`
:   no arguments

**Description**

Check permissions prior to creating a new TUN device.

**Return**

Returns 0 if permission is granted.

int security_tun_dev_attach_queue(void \*security)
:   Check if attaching a TUN queue is allowed

**Parameters**

`void *security`
:   TUN device LSM blob

**Description**

Check permissions prior to attaching to a TUN device queue.

**Return**

Returns 0 if permission is granted.

int security_tun_dev_attach(struct [sock](../networking/kapi.md#c.sock "sock") \*sk, void \*security)
:   Update TUN device LSM state on attach

**Parameters**

`struct sock *sk`
:   associated sock

`void *security`
:   TUN device LSM blob

**Description**

This hook can be used by the module to update any security state associated
with the TUN device's sock structure.

**Return**

Returns 0 if permission is granted.

int security_tun_dev_open(void \*security)
:   Update TUN device LSM state on open

**Parameters**

`void *security`
:   TUN device LSM blob

**Description**

This hook can be used by the module to update any security state associated
with the TUN device's security structure.

**Return**

Returns 0 if permission is granted.

int security_sctp_assoc_request(struct sctp_association \*asoc, struct [sk_buff](../networking/kapi.md#c.sk_buff "sk_buff") \*skb)
:   Update the LSM on a SCTP association req

**Parameters**

`struct sctp_association *asoc`
:   SCTP association

`struct sk_buff *skb`
:   packet requesting the association

**Description**

Passes the **asoc** and **chunk->skb** of the association INIT packet to the LSM.

**Return**

Returns 0 on success, error on failure.

int security_sctp_bind_connect(struct [sock](../networking/kapi.md#c.sock "sock") \*sk, int optname, struct sockaddr \*address, int addrlen)
:   Validate a list of addrs for a SCTP option

**Parameters**

`struct sock *sk`
:   socket

`int optname`
:   SCTP option to validate

`struct sockaddr *address`
:   list of IP addresses to validate

`int addrlen`
:   length of the address list

**Description**

Validiate permissions required for each address associated with sock **sk**.
Depending on **optname**, the addresses will be treated as either a connect or
bind service. The **addrlen** is calculated on each IPv4 and IPv6 address using
sizeof(struct sockaddr_in) or sizeof(struct sockaddr_in6).

**Return**

Returns 0 on success, error on failure.

void security_sctp_sk_clone(struct sctp_association \*asoc, struct [sock](../networking/kapi.md#c.sock "sock") \*sk, struct [sock](../networking/kapi.md#c.sock "sock") \*newsk)
:   Clone a SCTP sock's LSM state

**Parameters**

`struct sctp_association *asoc`
:   SCTP association

`struct sock *sk`
:   original sock

`struct sock *newsk`
:   target sock

**Description**

Called whenever a new socket is created by accept(2) (i.e. a TCP style
socket) or when a socket is 'peeled off' e.g userspace calls
sctp_peeloff(3).

int security_sctp_assoc_established(struct sctp_association \*asoc, struct [sk_buff](../networking/kapi.md#c.sk_buff "sk_buff") \*skb)
:   Update LSM state when assoc established

**Parameters**

`struct sctp_association *asoc`
:   SCTP association

`struct sk_buff *skb`
:   packet establishing the association

**Description**

Passes the **asoc** and **chunk->skb** of the association COOKIE_ACK packet to the
security module.

**Return**

Returns 0 if permission is granted.

int security_ib_pkey_access(void \*sec, u64 subnet_prefix, u16 pkey)
:   Check if access to an IB pkey is allowed

**Parameters**

`void *sec`
:   LSM blob

`u64 subnet_prefix`
:   subnet prefix of the port

`u16 pkey`
:   IB pkey

**Description**

Check permission to access a pkey when modifying a QP.

**Return**

Returns 0 if permission is granted.

int security_ib_endport_manage_subnet(void \*sec, const char \*dev_name, u8 port_num)
:   Check if SMPs traffic is allowed

**Parameters**

`void *sec`
:   LSM blob

`const char *dev_name`
:   IB device name

`u8 port_num`
:   port number

**Description**

Check permissions to send and receive SMPs on a end port.

**Return**

Returns 0 if permission is granted.

int security_ib_alloc_security(void \*\*sec)
:   Allocate an Infiniband LSM blob

**Parameters**

`void **sec`
:   LSM blob

**Description**

Allocate a security structure for Infiniband objects.

**Return**

Returns 0 on success, non-zero on failure.

void security_ib_free_security(void \*sec)
:   Free an Infiniband LSM blob

**Parameters**

`void *sec`
:   LSM blob

**Description**

Deallocate an Infiniband security structure.

int security_xfrm_policy_alloc(struct xfrm_sec_ctx \*\*ctxp, struct xfrm_user_sec_ctx \*sec_ctx, gfp_t gfp)
:   Allocate a xfrm policy LSM blob

**Parameters**

`struct xfrm_sec_ctx **ctxp`
:   xfrm security context being added to the SPD

`struct xfrm_user_sec_ctx *sec_ctx`
:   security label provided by userspace

`gfp_t gfp`
:   gfp flags

**Description**

Allocate a security structure to the xp->security field; the security field
is initialized to NULL when the xfrm_policy is allocated.

**Return**

Return 0 if operation was successful.

void security_xfrm_policy_free(struct xfrm_sec_ctx \*ctx)
:   Free a xfrm security context

**Parameters**

`struct xfrm_sec_ctx *ctx`
:   xfrm security context

**Description**

Free LSM resources associated with **ctx**.

int security_xfrm_state_alloc(struct xfrm_state \*x, struct xfrm_user_sec_ctx \*sec_ctx)
:   Allocate a xfrm state LSM blob

**Parameters**

`struct xfrm_state *x`
:   xfrm state being added to the SAD

`struct xfrm_user_sec_ctx *sec_ctx`
:   security label provided by userspace

**Description**

Allocate a security structure to the **x->security** field; the security field
is initialized to NULL when the xfrm_state is allocated. Set the context to
correspond to **sec_ctx**.

**Return**

Return 0 if operation was successful.

int security_xfrm_state_delete(struct xfrm_state \*x)
:   Check if deleting a xfrm state is allowed

**Parameters**

`struct xfrm_state *x`
:   xfrm state

**Description**

Authorize deletion of x->security.

**Return**

Returns 0 if permission is granted.

int security_locked_down(enum lockdown_reason what)
:   Check if a kernel feature is allowed

**Parameters**

`enum lockdown_reason what`
:   requested kernel feature

**Description**

Determine whether a kernel feature that potentially enables arbitrary code
execution in kernel space should be permitted.

**Return**

Returns 0 if permission is granted.

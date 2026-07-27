---
collection: ceph
version: "19.2.2"
title: "LibCephFS (Python)"
source_url: https://docs.ceph.com/en/squid/cephfs/api/libcephfs-py/
fetched_at: 2026-07-27T16:42:29+00:00
---
# LibCephFS (Python)

The cephfs python module provides access to CephFS service.

## API calls

This module is a thin wrapper around libcephfs.

*class* cephfs.DirEntry(*d_ino*, *d_off*, *d_reclen*, *d_type*, *d_name*, *d_snapid*)

*class* cephfs.LibCephFS
:   libcephfs python wrapper

    abort_conn()
    :   Abort mds connections.

    chdir(*path*)
    :   Change the current working directory.

        Parameters:
        :   **path** -- the path to the working directory to change into.

    chmod(*path*, *mode*)
    :   Change directory mode.

        Parameters:
        :   - **path** -- the path of the directory to create. This must be either an
              absolute path or a relative path off of the current working directory.
            - **mode** -- the permissions the directory should have once created.

        Return type:
        :   `None`

    chown(*path*, *uid*, *gid*, *follow_symlink=True*)
    :   Change directory ownership

        Parameters:
        :   - **path** -- the path of the directory to change.
            - **uid** -- the uid to set
            - **gid** -- the gid to set
            - **follow_symlink** -- perform the operation on the target file if @path
              is a symbolic link (default)

    close(*fd*)
    :   Close the open file.

        Parameters:
        :   **fd** -- the file descriptor referring to the open file.

    closedir(*handle*)
    :   Close the open directory.

        Parameters:
        :   **handle** -- the open directory stream handle

    conf_get(*option*)
    :   Gets the configuration value as a string.

        Parameters:
        :   **option** -- the config option to get

    conf_parse_argv(*argv*)
    :   Parse the command line arguments and load the configuration parameters.

        Parameters:
        :   **argv** -- the argument list

    conf_read_file(*conffile=None*)
    :   Load the ceph configuration from the specified config file.

        Parameters:
        :   **opt** (*conffile str*) -- the path to ceph.conf to override the default settings

    conf_set(*option*, *val*)
    :   Sets a configuration value from a string.

        Parameters:
        :   - **option** -- the configuration option to set
            - **value** -- the value of the configuration option to set

    create(*conf=None*, *conffile=-1*, *auth_id=None*)
    :   Create a mount handle for interacting with Ceph. All libcephfs
        functions operate on a mount info handle.

        Parameters:
        :   - **opt** (*conf dict*) -- settings overriding the default ones and conffile
            - **optional** (*conffile Union**[**int**,**str**]**,*) -- the path to ceph.conf to override the default settings

        Auth_id str opt:
        :   the id used to authenticate the client entity

    debug_get_fd_caps(*fd*)
    :   Get the capabilities currently issued to the client given the fd.

        Parameters:
        :   **fd** -- the file descriptor to get issued

    debug_get_file_caps(*path*)
    :   Get the capabilities currently issued to the client given the path.

        Parameters:
        :   **path** -- the path of the file/directory to get the capabilities of.

    fallocate(*fd*, *offset*, *length*, *mode=0*)
    :   Preallocate or release disk space for the file for the byte range.

        Parameters:
        :   - **fd** -- the file descriptor of the file to fallocate.
            - **mode** -- the flags determines the operation to be performed on the given
              range. default operation (0) is to return -EOPNOTSUPP since
              cephfs does not allocate disk blocks to provide write guarantees.
              if the FALLOC_FL_KEEP_SIZE flag is specified in the mode,
              the file size will not be changed. if the FALLOC_FL_PUNCH_HOLE
              flag is specified in the mode, the operation is deallocate
              space and zero the byte range.
            - **offset** -- the byte range starting.
            - **length** -- the length of the range.

    fchmod(*fd*, *mode*)
    :   Change file mode based on fd.

        Parameters:
        :   - **fd** -- the file descriptor of the file to change file mode
            - **mode** -- the permissions to be set.

    fchown(*fd*, *uid*, *gid*)
    :   Change file ownership

        Parameters:
        :   - **fd** -- the file descriptor of the file to change ownership
            - **uid** -- the uid to set
            - **gid** -- the gid to set

    fgetxattr(*fd*, *name*, *size=255*)
    :   Get an extended attribute given the fd of a file.

        Parameters:
        :   - **fd** -- the open file descriptor referring to the file
            - **name** -- the name of the extended attribute to get
            - **size** -- the size of the pre-allocated buffer

    flistxattr(*fd*, *size=65536*)
    :   List the extended attribute keys set on a file.

        Parameters:
        :   - **fd** -- the open file descriptor referring to the file.
            - **size** -- the size of list buffer to be filled with extended attribute keys.

    flock(*fd*, *operation*, *owner*)
    :   Apply or remove an advisory lock.

        Parameters:
        :   - **fd** -- the open file descriptor to change advisory lock.
            - **operation** -- the advisory lock operation to be performed on the file
            - **owner** -- the user-supplied owner identifier (an arbitrary integer)

    fremovexattr(*fd*, *name*)
    :   Remove an extended attribute of a file.

        Parameters:
        :   - **fd** -- the open file descriptor referring to the file.
            - **name** -- name of the extended attribute to remove.

    fsetattrx(*fd*, *dict_stx*, *mask*)
    :   Set a file’s attributes.

        Parameters:
        :   - **path** -- the path to the file/directory to set the attributes of.
            - **mask** -- a mask of all the CEPH_SETATTR_\* values that have been set in the statx struct.
            - **stx** -- a dict of statx structure that must include attribute values to set on the file.

    fsetxattr(*fd*, *name*, *value*, *flags*)
    :   Set an extended attribute on a file.

        Parameters:
        :   - **fd** -- the open file descriptor referring to the file.
            - **name** -- the name of the extended attribute to set.
            - **value** -- the bytes of the extended attribute value

    fstat(*fd*)
    :   Get an open file’s extended statistics and attributes.

        Parameters:
        :   **fd** -- the file descriptor of the file to get statistics of.

    fsync(*fd*, *syncdataonly*)
    :   Synchronize an open file to persistent media.

        Parameters:
        :   - **fd** -- the file descriptor of the file to sync.
            - **syncdataonly** -- a boolean whether to synchronize metadata and data (0)
              or just data (1).

    ftruncate(*fd*, *size*)
    :   Truncate the file to the given size. If this operation causes the
        file to expand, the empty bytes will be filled in with zeros.

        Parameters:
        :   - **path** -- the path to the file to truncate.
            - **size** -- the new size of the file.

    futime(*fd*, *times=None*)
    :   Set access and modification time for a file pointed by descriptor

        Parameters:
        :   - **fd** -- file descriptor of the open file
            - **times** -- if times is not None, it must be a tuple (atime, mtime)

    futimens(*fd*, *times=None*)
    :   Set access and modification time for a file pointer by descriptor

        Parameters:
        :   - **fd** -- file descriptor of the open file
            - **times** -- if times is not None, it must be a tuple (atime, mtime)

    futimes(*fd*, *times=None*)
    :   Set access and modification time for a file pointer by descriptor

        Parameters:
        :   - **fd** -- file descriptor of the open file
            - **times** -- if times is not None, it must be a tuple (atime, mtime)

    get_addrs()
    :   Get associated client addresses with this RADOS session.

    get_cap_return_timeout()
    :   Get the amount of time that the client has to return caps

        In the event that a client does not return its caps, the MDS may blocklist
        it after this timeout. Applications should check this value and ensure
        that they set the delegation timeout to a value lower than this.

    get_default_pool()
    :   Get the default pool name and id of cephfs. This returns dict{pool_name, pool_id}.

    get_file_replication(*fd*)
    :   Get the file replication information from an open file descriptor.

        Parameters:
        :   **fd** -- the open file descriptor referring to the file to get
            the replication information of.

    get_fscid()
    :   Return the file system id for this fs client.

    get_instance_id()
    :   Get a global id for current instance

    get_layout(*fd*)
    :   Get the file layout from an open file descriptor.

        Parameters:
        :   **fd** -- the open file descriptor referring to the file to get the layout of.

    get_path_replication(*path*)
    :   Get the file replication information given the path.

        Parameters:
        :   **path** -- the path of the file/directory to get the replication information of.

    get_pool_id(*pool_name*)
    :   Get the id of the named pool.

        Parameters:
        :   **pool_name** -- the name of the pool.

    get_pool_replication(*pool_id*)
    :   Get the pool replication factor.

        Parameters:
        :   **pool_id** -- the pool id to look up

    getcwd()
    :   Get the current working directory.

        Return type:
        :   `bytes`

        Returns:
        :   the path to the current working directory

    getxattr(*path*, *name*, *size=255*, *follow_symlink=True*)
    :   Get an extended attribute.

        Parameters:
        :   - **path** -- the path to the file
            - **name** -- the name of the extended attribute to get
            - **size** -- the size of the pre-allocated buffer

    init()
    :   Initialize the filesystem client (but do not mount the filesystem yet)

    lazyio(*fd*, *enable*)
    :   Enable/disable lazyio for the file.

        Parameters:
        :   - **fd** -- the file descriptor of the file for which to enable lazio.
            - **enable** -- a boolean to enable lazyio or disable lazyio.

    lazyio_propagate(*fd*, *offset*, *count*)
    :   Flushes the write buffer for the file thereby propogating the buffered write to the file.

        Parameters:
        :   - **fd** -- the file descriptor of the file to sync.
            - **offset** -- the byte range starting.
            - **count** -- the number of bytes starting from offset.

    lazyio_synchronize(*fd*, *offset*, *count*)
    :   Flushes the write buffer for the file and invalidate the read cache. This allows a
        subsequent read operation to read and cache data directly from the file and hence
        everyone’s propagated writes would be visible.

        Parameters:
        :   - **fd** -- the file descriptor of the file to sync.
            - **offset** -- the byte range starting.
            - **count** -- the number of bytes starting from offset.

    lchmod(*path*, *mode*)
    :   Change file mode. If the path is a symbolic link, it won’t be dereferenced.

        Parameters:
        :   - **path** -- the path of the file. This must be either an absolute path or
              a relative path off of the current working directory.
            - **mode** -- the permissions to be set .

        Return type:
        :   `None`

    lchown(*path*, *uid*, *gid*)
    :   Change ownership of a symbolic link

        Parameters:
        :   - **path** -- the path of the symbolic link to change.
            - **uid** -- the uid to set
            - **gid** -- the gid to set

    lgetxattr(*path*, *name*, *size=255*)
    :   Get an extended attribute without following symbolic links. This
        function is identical to ceph_getxattr, but if the path refers to
        a symbolic link, we get the extended attributes of the symlink
        rather than the attributes of the file it points to.

        Parameters:
        :   - **path** -- the path to the file
            - **name** -- the name of the extended attribute to get
            - **size** -- the size of the pre-allocated buffer

    link(*existing*, *newname*)
    :   Create a link.

        Parameters:
        :   - **existing** -- the path to the existing file/directory to link to.
            - **newname** -- the path to the new file/directory to link from.

    listxattr(*path*, *size=65536*, *follow_symlink=True*)
    :   List the extended attribute keys set on a file.

        Parameters:
        :   - **path** -- path of the file.
            - **size** -- the size of list buffer to be filled with extended attribute keys.

    llistxattr(*path*, *size=65536*)
    :   List the extended attribute keys set on a file but do not follow symbolic link.

        Parameters:
        :   - **path** -- path of the file.
            - **size** -- the size of list buffer to be filled with extended attribute keys.

    lremovexattr(*path*, *name*)
    :   Remove an extended attribute of a file but do not follow symbolic link.

        Parameters:
        :   - **path** -- path of the file.
            - **name** -- name of the extended attribute to remove.

    lseek(*fd*, *offset*, *whence*)
    :   Set the file’s current position.

        Parameters:
        :   - **fd** -- the file descriptor of the open file to read from.
            - **offset** -- the offset in the file to read from. If this value is negative, the
              function reads from the current offset of the file descriptor.
            - **whence** -- the flag to indicate what type of seeking to performs:SEEK_SET, SEEK_CUR, SEEK_END

    lsetxattr(*path*, *name*, *value*, *flags*)
    :   Set an extended attribute on a file but do not follow symbolic link.

        Parameters:
        :   - **path** -- the path to the file.
            - **name** -- the name of the extended attribute to set.
            - **value** -- the bytes of the extended attribute value

    lstat(*path*)
    :   Get a file’s extended statistics and attributes. If the file is a
        symbolic link, return the information of the link itself rather than
        the information of the file it points to.

        Parameters:
        :   **path** -- the file or directory to get the statistics of.

    lutimes(*path*, *times=None*)
    :   Set access and modification time for a file. If the file is a symbolic
        link do not follow to the target.

        Parameters:
        :   - **path** -- file path for which timestamps have to be changed
            - **times** -- if times is not None, it must be a tuple (atime, mtime)

    mds_command(*mds_spec*, *args*, *input_data*)
    :   Returns:
        :   3-tuple of output status int, output status string, output data

    mds_command2(*result*, *mds_spec*, *args*, *input_data=None*, *one_shot=False*)
    :   Param:
        :   result: a completion object with a complete method accepting an integer rc, bytes output, and bytes error output

        Param:
        :   mds_spec: the identity of one or more MDS to send the command to (e.g. “\*” or “fsname:0”)

        Param:
        :   args: the JSON-encoded MDS command

        Param:
        :   input_data: optional input data to the command

        Param:
        :   one_shot: optional boolean indicating if the command should only be tried/sent once

        Returns:
        :   0 if command is/will be sent or an exception is raised

    mkdir(*path*, *mode*)
    :   Create a directory.

        Parameters:
        :   - **path** -- the path of the directory to create. This must be either an
              absolute path or a relative path off of the current working directory.
            - **mode** -- the permissions the directory should have once created.

    mkdirs(*path*, *mode*)
    :   Create multiple directories at once.

        Parameters:
        :   - **path** -- the full path of directories and sub-directories that should
              be created.
            - **mode** -- the permissions the directory should have once created

    mknod(*path*, *mode*, *rdev=0*)
    :   Make a block or character special file.

        Parameters:
        :   - **path** -- the path to the special file.
            - **mode** -- the permissions to use and the type of special file. The type can be
              one of stat.S_IFREG, stat.S_IFCHR, stat.S_IFBLK, stat.S_IFIFO. Both
              should be combined using bitwise OR.
            - **rdev** -- If the file type is stat.S_IFCHR or stat.S_IFBLK then this parameter
              specifies the major and minor numbers of the newly created device
              special file. Otherwise, it is ignored.

    mksnap(*path*, *name*, *mode*, *metadata={}*)
    :   Create a snapshot.

        Parameters:
        :   - **path** -- path of the directory to snapshot.
            - **name** -- snapshot name
            - **mode** -- permission of the snapshot
            - **metadata** -- metadata key/value to store with the snapshot

        Raises:
        :   class:
            :   TypeError

        Raises:
        :   class:
            :   Error

        Return type:
        :   `int`

        Returns:
        :   0 on success

    mount(*mount_root=None*, *filesystem_name=None*)
    :   Perform a mount using the path for the root of the mount.

    open(*path*, *flags*, *mode=0*)
    :   Create and/or open a file.

        Parameters:
        :   - **path** -- the path of the file to open. If the flags parameter includes O_CREAT,
              the file will first be created before opening.
            - **flags** -- set of option masks that control how the file is created/opened.
            - **mode** -- the permissions to place on the file if the file does not exist and O_CREAT
              is specified in the flags.

    opendir(*path*)
    :   Open the given directory.

        Parameters:
        :   **path** -- the path name of the directory to open. Must be either an absolute path
            or a path relative to the current working directory.

        Return type:
        :   `DirResult`

        Returns:
        :   the open directory stream handle

    opensnapdiff(*root_path*, *rel_path*, *snap1name*, *snap2name*)
    :   Open the given directory.

        Parameters:
        :   **path** -- the path name of the directory to open. Must be either an absolute path
            or a path relative to the current working directory.

        Return type:
        :   `SnapDiffHandle`

        Returns:
        :   the open directory stream handle

    preadv(*fd*, *buffers*, *offset*)
    :   Write data to a file.

        Parameters:
        :   - **fd** -- the file descriptor of the open file to read from
            - **buffers** -- the list of byte object to read from the file
            - **offset** -- the offset of the file read from. If this value is negative, the
              function reads from the current offset of the file descriptor.

    pwritev(*fd*, *buffers*, *offset*)
    :   Write data to a file.

        Parameters:
        :   - **fd** -- the file descriptor of the open file to write to
            - **buffers** -- the list of byte object to write to the file
            - **offset** -- the offset of the file write into. If this value is negative, the
              function writes to the current offset of the file descriptor.

    read(*fd*, *offset*, *l*)
    :   Read data from the file.

        Parameters:
        :   - **fd** -- the file descriptor of the open file to read from.
            - **offset** -- the offset in the file to read from. If this value is negative, the
              function reads from the current offset of the file descriptor.
            - **l** -- the flag to indicate what type of seeking to perform

    readdir(*handle*)
    :   Get the next entry in an open directory.

        Parameters:
        :   **handle** -- the open directory stream handle

        Return type:
        :   `Optional`[[`DirEntry`](index.md#cephfs.DirEntry "cephfs.DirEntry")]

        Returns:
        :   the next directory entry or None if at the end of the
            directory (or the directory is empty. This pointer
            should not be freed by the caller, and is only safe to
            access between return and the next call to readdir or
            closedir.

    readlink(*path*, *size*)
    :   Read a symbolic link.

        Parameters:
        :   - **path** -- the path to the symlink to read
            - **size** -- the length of the buffer

        Return type:
        :   `bytes`

        Returns:
        :   buffer to hold the path of the file that the symlink points to.

    removexattr(*path*, *name*, *follow_symlink=True*)
    :   Remove an extended attribute of a file.

        Parameters:
        :   - **path** -- path of the file.
            - **name** -- name of the extended attribute to remove.

    rename(*src*, *dst*)
    :   Rename a file or directory.

        Parameters:
        :   - **src** -- the path to the existing file or directory.
            - **dst** -- the new name of the file or directory.

    rewinddir(*handle*)
    :   Rewind the directory stream to the beginning of the directory.

        Parameters:
        :   **handle** -- the open directory stream handle

    rmdir(*path*)
    :   Remove a directory.

        Parameters:
        :   **path** -- the path of the directory to remove.

    rmsnap(*path*, *name*)
    :   Remove a snapshot.

        Parameters:
        :   - **path** -- path of the directory for removing snapshot
            - **name** -- snapshot name

        Raises:
        :   class:
            :   Error

        Return type:
        :   `int`

        Returns:
        :   0 on success

    seekdir(*handle*, *offset*)
    :   Move the directory stream to a position specified by the given offset.

        Parameters:
        :   - **handle** -- the open directory stream handle
            - **offset** -- the position to move the directory stream to. This offset should be
              a value returned by telldir. Note that this value does not refer to
              the nth entry in a directory, and can not be manipulated with plus
              or minus.

    set_mount_timeout(*timeout*)
    :   Set mount timeout

        Parameters:
        :   **timeout** -- mount timeout

    set_session_timeout(*timeout*)
    :   Set ceph client session timeout. Must be called before mount.

        Parameters:
        :   **timeout** -- the timeout to set

    set_uuid(*uuid*)
    :   Set ceph client uuid. Must be called before mount.

        Parameters:
        :   **uuid** -- the uuid to set

    setattrx(*path*, *dict_stx*, *mask*, *flags*)
    :   Set a file’s attributes.

        Parameters:
        :   - **path** -- the path to the file/directory to set the attributes of.
            - **mask** -- a mask of all the CEPH_SETATTR_\* values that have been set in the statx struct.
            - **stx** -- a dict of statx structure that must include attribute values to set on the file.
            - **flags** -- mask of AT_\* flags (only AT_ATTR_NOFOLLOW is respected for now)

    setxattr(*path*, *name*, *value*, *flags*, *follow_symlink=True*)
    :   > Set an extended attribute on a file.

        Parameters:
        :   - **path** -- the path to the file.
            - **name** -- the name of the extended attribute to set.
            - **value** -- the bytes of the extended attribute value

    shutdown()
    :   Unmount and destroy the ceph mount handle.

    snap_info(*path*)
    :   Fetch sapshot info

        Parameters:
        :   **path** -- snapshot path

        Raises:
        :   class:
            :   Error

        Return type:
        :   `Dict`[`str`, `Any`]

        Returns:
        :   snapshot metadata

    stat(*path*, *follow_symlink=True*)
    :   Get a file’s extended statistics and attributes.

        Parameters:
        :   **path** -- the file or directory to get the statistics of.

    statfs(*path*)
    :   Perform a statfs on the ceph file system. This call fills in file system wide statistics
        into the passed in buffer.

        Parameters:
        :   **path** -- any path within the mounted filesystem

    statx(*path*, *mask*, *flag*)
    :   Get a file’s extended statistics and attributes.

        Parameters:
        :   - **path** -- the file or directory to get the statistics of.
            - **mask** -- want bitfield of CEPH_STATX_\* flags showing designed attributes.
            - **flag** -- bitfield that can be used to set AT_\* modifier flags (AT_STATX_SYNC_AS_STAT, AT_STATX_FORCE_SYNC, AT_STATX_DONT_SYNC and AT_SYMLINK_NOFOLLOW)

    symlink(*existing*, *newname*)
    :   Creates a symbolic link.

        Parameters:
        :   - **existing** -- the path to the existing file/directory to link to.
            - **newname** -- the path to the new file/directory to link from.

    sync_fs()
    :   Synchronize all filesystem data to persistent media

    telldir(*handle*)
    :   Get the current position of a directory stream.

        Parameters:
        :   **handle** -- the open directory stream handle

        Return value:
        :   The position of the directory stream. Note that the offsets
            returned by ceph_telldir do not have a particular order (cannot
            be compared with inequality).

    truncate(*path*, *size*)
    :   Truncate the file to the given size. If this operation causes the
        file to expand, the empty bytes will be filled in with zeros.

        Parameters:
        :   - **path** -- the path to the file to truncate.
            - **size** -- the new size of the file.

    unlink(*path*)
    :   Removes a file, link, or symbolic link. If the file/link has multiple links to it, the
        file will not disappear from the namespace until all references to it are removed.

        Parameters:
        :   **path** -- the path of the file or link to unlink.

    unmount()
    :   Unmount a mount handle.

    utime(*path*, *times=None*)
    :   Set access and modification time for path

        Parameters:
        :   - **path** -- file path for which timestamps have to be changed
            - **times** -- if times is not None, it must be a tuple (atime, mtime)

    utimes(*path*, *times=None*, *follow_symlink=True*)
    :   Set access and modification time for path

        Parameters:
        :   - **path** -- file path for which timestamps have to be changed
            - **times** -- if times is not None, it must be a tuple (atime, mtime)
            - **follow_symlink** -- perform the operation on the target file if @path
              is a symbolic link (default)

    version()
    :   Get the version number of the `libcephfs` C library.

        Returns:
        :   a tuple of `(major, minor, extra)` components of the
            libcephfs version

    write(*fd*, *buf*, *offset*)
    :   Write data to a file.

        Parameters:
        :   - **fd** -- the file descriptor of the open file to write to
            - **buf** -- the bytes to write to the file
            - **offset** -- the offset of the file write into. If this value is negative, the
              function writes to the current offset of the file descriptor.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).

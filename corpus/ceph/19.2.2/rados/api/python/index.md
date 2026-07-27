---
collection: ceph
version: "19.2.2"
title: "Librados (Python)"
source_url: https://docs.ceph.com/en/squid/rados/api/python/
fetched_at: 2026-07-27T16:39:51+00:00
---
# Librados (Python)

The `rados` module is a thin Python wrapper for `librados`.

## Installation

To install Python libraries for Ceph, see [Getting librados for Python](../librados-intro.md#getting-librados-for-python).

## Getting Started

You can create your own Ceph client using Python. The following tutorial will
show you how to import the Ceph Python module, connect to a Ceph cluster, and
perform object operations as a `client.admin` user.

> **Note:**
>
> To use the Ceph Python bindings, you must have access to a
> running Ceph cluster. To set one up quickly, see [Getting Started](../../../start.md).

First, create a Python source file for your Ceph client.

```
vim client.py
```

### Import the Module

To use the `rados` module, import it into your source file.

```python
1     import rados
```

### Configure a Cluster Handle

Before connecting to the Ceph Storage Cluster, create a cluster handle. By
default, the cluster handle assumes a cluster named `ceph` (i.e., the default
for deployment tools, and our Getting Started guides too), and a
`client.admin` user name. You may change these defaults to suit your needs.

To connect to the Ceph Storage Cluster, your application needs to know where to
find the Ceph Monitor. Provide this information to your application by
specifying the path to your Ceph configuration file, which contains the location
of the initial Ceph monitors.

```python
1     import rados, sys
2
3     #Create Handle Examples.
4     cluster = rados.Rados(conffile='ceph.conf')
5     cluster = rados.Rados(conffile=sys.argv[1])
6     cluster = rados.Rados(conffile = 'ceph.conf', conf = dict (keyring = '/path/to/keyring'))
```

Ensure that the `conffile` argument provides the path and file name of your
Ceph configuration file. You may use the `sys` module to avoid hard-coding the
Ceph configuration path and file name.

Your Python client also requires a client keyring. For this example, we use the
`client.admin` key by default. If you would like to specify the keyring when
creating the cluster handle, you may use the `conf` argument. Alternatively,
you may specify the keyring path in your Ceph configuration file. For example,
you may add something like the following line to your Ceph configuration file:

```
keyring = /path/to/ceph.client.admin.keyring
```

For additional details on modifying your configuration via Python, see [Configuration](index.md#configuration).

### Connect to the Cluster

Once you have a cluster handle configured, you may connect to the cluster.
With a connection to the cluster, you may execute methods that return
information about the cluster.

```python
 1     import rados, sys
 2
 3     cluster = rados.Rados(conffile='ceph.conf')
 4     print("\nlibrados version: {}".format(str(cluster.version())))
 5     print("Will attempt to connect to: {}".format(str(cluster.conf_get('mon host'))))
 6
 7     cluster.connect()
 8     print("\nCluster ID: {}".format(cluster.get_fsid()))
 9
10     print("\n\nCluster Statistics")
11     print("==================")
12     cluster_stats = cluster.get_cluster_stats()
13
14     for key, value in cluster_stats.items():
15             print(key, value)
```

By default, Ceph authentication is `on`. Your application will need to know
the location of the keyring. The `python-ceph` module doesn’t have the default
location, so you need to specify the keyring path. The easiest way to specify
the keyring is to add it to the Ceph configuration file. The following Ceph
configuration file example uses the `client.admin` keyring.

```ini
1     [global]
2     # ... elided configuration
3     keyring = /path/to/keyring/ceph.client.admin.keyring
```

### Manage Pools

When connected to the cluster, the `Rados` API allows you to manage pools. You
can list pools, check for the existence of a pool, create a pool and delete a
pool.

```python
 1     print("\n\nPool Operations")
 2     print("===============")
 3
 4     print("\nAvailable Pools")
 5     print("----------------")
 6     pools = cluster.list_pools()
 7
 8     for pool in pools:
 9             print(pool)
10
11     print("\nCreate 'test' Pool")
12     print("------------------")
13     cluster.create_pool('test')
14
15     print("\nPool named 'test' exists: {}".format(str(cluster.pool_exists('test'))))
16     print("\nVerify 'test' Pool Exists")
17     print("-------------------------")
18     pools = cluster.list_pools()
19
20     for pool in pools:
21             print(pool)
22
23     print("\nDelete 'test' Pool")
24     print("------------------")
25     cluster.delete_pool('test')
26     print("\nPool named 'test' exists: {}".format(str(cluster.pool_exists('test'))))
```

### Input/Output Context

Reading from and writing to the Ceph Storage Cluster requires an input/output
context (ioctx). You can create an ioctx with the `open_ioctx()` or
`open_ioctx2()` method of the `Rados` class. The `ioctx_name` parameter
is the name of the pool and `pool_id` is the ID of the pool you wish to use.

```python
1     ioctx = cluster.open_ioctx('data')
```

or

```python
1     ioctx = cluster.open_ioctx2(pool_id)
```

Once you have an I/O context, you can read/write objects, extended attributes,
and perform a number of other operations. After you complete operations, ensure
that you close the connection. For example:

```python
1     print("\nClosing the connection.")
2     ioctx.close()
```

### Writing, Reading and Removing Objects

Once you create an I/O context, you can write objects to the cluster. If you
write to an object that doesn’t exist, Ceph creates it. If you write to an
object that exists, Ceph overwrites it (except when you specify a range, and
then it only overwrites the range). You may read objects (and object ranges)
from the cluster. You may also remove objects from the cluster. For example:

```python
1print("\nWriting object 'hw' with contents 'Hello World!' to pool 'data'.")
2ioctx.write_full("hw", "Hello World!")
3
4print("\n\nContents of object 'hw'\n------------------------\n")
5print(ioctx.read("hw"))
6
7print("\nRemoving object 'hw'")
8ioctx.remove_object("hw")
```

### Writing and Reading XATTRS

Once you create an object, you can write extended attributes (XATTRs) to
the object and read XATTRs from the object. For example:

```python
1print("\n\nWriting XATTR 'lang' with value 'en_US' to object 'hw'")
2ioctx.set_xattr("hw", "lang", "en_US")
3
4print("\n\nGetting XATTR 'lang' from object 'hw'\n")
5print(ioctx.get_xattr("hw", "lang"))
```

### Listing Objects

If you want to examine the list of objects in a pool, you may
retrieve the list of objects and iterate over them with the object iterator.
For example:

```python
 1object_iterator = ioctx.list_objects()
 2
 3while True :
 4
 5        try :
 6                rados_object = object_iterator.__next__()
 7                print("Object contents = {}".format(rados_object.read()))
 8
 9        except StopIteration :
10                break
11
12# Or alternatively
13[print("Object contents = {}".format(obj.read())) for obj in ioctx.list_objects()]
```

The `Object` class provides a file-like interface to an object, allowing
you to read and write content and extended attributes. Object operations using
the I/O context provide additional functionality and asynchronous capabilities.

## Cluster Handle API

The `Rados` class provides an interface into the Ceph Storage Daemon.

### Configuration

The `Rados` class provides methods for getting and setting configuration
values, reading the Ceph configuration file, and parsing arguments. You
do not need to be connected to the Ceph Storage Cluster to invoke the following
methods. See [Storage Cluster Configuration](../../configuration.md) for details on settings.

Rados.conf_get(*option*)
:   Rados.conf_get(self, str option: str) -> Optional[str]

    Get the value of a configuration option

    Parameters:
    :   **option** (`str`) -- which option to read

    Return type:
    :   `Optional`[`str`]

    Returns:
    :   value of the option or None

    Raises:
    :   `TypeError`

Rados.conf_set(*option*, *val*)
:   Rados.conf_set(self, str option: str, str val: str)

    Set the value of a configuration option

    Parameters:
    :   - **option** (`str`) -- which option to set
        - **option** -- value of the option

    Raises:
    :   `TypeError`, `ObjectNotFound`

Rados.conf_read_file(*path=None*)
:   Rados.conf_read_file(self, str path: Optional[str] = None)

    Configure the cluster handle using a Ceph config file.

    Parameters:
    :   **path** (`Optional`[`str`]) -- path to the config file

Rados.conf_parse_argv(*args*)
:   Rados.conf_parse_argv(self, args: Sequence[str])

    Parse known arguments from args, and remove; returned
    args contain only those unknown to ceph

Rados.version()
:   Rados.version(self) -> Version

    Get the version number of the `librados` C library.

    Return type:
    :   `Version`

    Returns:
    :   a tuple of `(major, minor, extra)` components of the
        librados version

### Connection Management

Once you configure your cluster handle, you may connect to the cluster, check
the cluster `fsid`, retrieve cluster statistics, and disconnect (shutdown)
from the cluster. You may also assert that the cluster handle is in a particular
state (e.g., “configuring”, “connecting”, etc.).

Rados.connect(*timeout=0*)
:   Rados.connect(self, int timeout: int = 0)

    Connect to the cluster. Use shutdown() to release resources.

    Parameters:
    :   **timeout** (`int`) -- Any supplied timeout value is currently ignored.

Rados.shutdown()
:   Rados.shutdown(self)

    Disconnects from the cluster. Call this explicitly when a
    Rados.connect()ed object is no longer used.

Rados.get_fsid()
:   Rados.get_fsid(self) -> str

    Get the fsid of the cluster as a hexadecimal string.

    Raises:
    :   `Error`

    Return type:
    :   `str`

    Returns:
    :   cluster fsid

Rados.get_cluster_stats()
:   Rados.get_cluster_stats(self) -> Dict[str, int]

    Read usage info about the cluster

    This tells you total space, space used, space available, and number
    of objects. These are not updated immediately when data is written,
    they are eventually consistent.
    :rtype: `Dict`[`str`, `int`]
    :returns: contains the following keys:

    > - `kb` (int) - total space
    > - `kb_used` (int) - space used
    > - `kb_avail` (int) - free space available
    > - `num_objects` (int) - number of objects

*class* rados.Rados
:   require_state(*\*args*)
    :   Checks if the Rados object is in a special state

        Parameters:
        :   **args** -- Any number of states to check as separate arguments

        Raises:
        :   `RadosStateError`

### Pool Operations

To use pool operation methods, you must connect to the Ceph Storage Cluster
first. You may list the available pools, create a pool, check to see if a pool
exists, and delete a pool.

Rados.list_pools()
:   Rados.list_pools(self) -> List[str]

    Gets a list of pool names.

    Return type:
    :   `List`[`str`]

    Returns:
    :   list of pool names.

Rados.create_pool(*pool_name*, *crush_rule=None*, *auid=None*)
:   Rados.create_pool(self, str pool_name: str, int crush_rule: Optional[int] = None, int auid: Optional[int] = None)

    Create a pool:
    - with default settings: if crush_rule=None and auid=None
    - with a specific CRUSH rule: crush_rule given
    - with a specific auid: auid given
    - with a specific CRUSH rule and auid: crush_rule and auid given

    Parameters:
    :   - **pool_name** (`str`) -- name of the pool to create
        - **crush_rule** (`Optional`[`int`]) -- rule to use for placement in the new pool
        - **auid** (`Optional`[`int`]) -- id of the owner of the new pool

    Raises:
    :   `TypeError`, `Error`

Rados.pool_exists(*pool_name*)
:   Rados.pool_exists(self, str pool_name: str) -> bool

    Checks if a given pool exists.

    Parameters:
    :   **pool_name** (`str`) -- name of the pool to check

    Raises:
    :   `TypeError`, `Error`

    Return type:
    :   `bool`

    Returns:
    :   whether the pool exists, false otherwise.

Rados.delete_pool(*pool_name*)
:   Rados.delete_pool(self, str pool_name: str)

    Delete a pool and all data inside it.

    The pool is removed from the cluster immediately,
    but the actual data is deleted in the background.

    Parameters:
    :   **pool_name** (`str`) -- name of the pool to delete

    Raises:
    :   `TypeError`, `Error`

### CLI Commands

The Ceph CLI command is internally using the following librados Python binding methods.

In order to send a command, choose the correct method and choose the correct target.

Rados.mon_command(*cmd*, *inbuf*, *timeout=0*, *target=None*)
:   Send a command to the mon.

    mon_command[_target](cmd, inbuf, outbuf, outbuflen, outs, outslen)

    Parameters:
    :   - **cmd** (`str`) -- JSON formatted string.
        - **inbuf** (`bytes`) -- optional string.
        - **timeout** (`int`) -- This parameter is ignored.
        - **target** (`Union`[`int`, `str`, `None`]) -- name or rank of a specific mon. Optional

    Return type:
    :   `Tuple`[`int`, `bytes`, `str`]

    Returns:
    :   (int ret, string outbuf, string outs)

    Example:

    ```
    >>> import json
    >>> c = Rados(conffile='/etc/ceph/ceph.conf')
    >>> c.connect()
    >>> cmd = json.dumps({"prefix": "osd safe-to-destroy", "ids": ["2"], "format": "json"})
    >>> c.mon_command(cmd, b'')
    ```

Rados.osd_command(*osdid*, *cmd*, *inbuf*, *timeout=0*)
:   osd_command(osdid, cmd, inbuf, outbuf, outbuflen, outs, outslen)

    Return type:
    :   `Tuple`[`int`, `bytes`, `str`]

    Returns:
    :   (int ret, string outbuf, string outs)

Rados.mgr_command(*cmd*, *inbuf*, *timeout=0*, *target=None*)
:   Return type:
    :   `Tuple`[`int`, `str`, `bytes`]

    Returns:
    :   (int ret, string outbuf, string outs)

Rados.pg_command(*pgid*, *cmd*, *inbuf*, *timeout=0*)
:   pg_command(pgid, cmd, inbuf, outbuf, outbuflen, outs, outslen)

    Return type:
    :   `Tuple`[`int`, `bytes`, `str`]

    Returns:
    :   (int ret, string outbuf, string outs)

## Input/Output Context API

To write data to and read data from the Ceph Object Store, you must create
an Input/Output context (ioctx). The Rados class provides open_ioctx()
and open_ioctx2() methods. The remaining `ioctx` operations involve
invoking methods of the Ioctx and other classes.

Rados.open_ioctx(*ioctx_name*)
:   Rados.open_ioctx(self, str ioctx_name: str) -> Ioctx

    Create an io context

    The io context allows you to perform operations within a particular
    pool.

    Parameters:
    :   **ioctx_name** (`str`) -- name of the pool

    Raises:
    :   `TypeError`, `Error`

    Return type:
    :   `Ioctx`

    Returns:
    :   Rados Ioctx object

Ioctx.require_ioctx_open()
:   Ioctx.require_ioctx_open(self)

    Checks if the rados.Ioctx object state is ‘open’

    Raises:
    :   IoctxStateError

Ioctx.get_stats()
:   Ioctx.get_stats(self) -> Dict[str, int]

    Get pool usage statistics

    Return type:
    :   `Dict`[`str`, `int`]

    Returns:
    :   dict contains the following keys:

        - `num_bytes` (int) - size of pool in bytes
        - `num_kb` (int) - size of pool in kbytes
        - `num_objects` (int) - number of objects in the pool
        - `num_object_clones` (int) - number of object clones
        - `num_object_copies` (int) - number of object copies
        - `num_objects_missing_on_primary` (int) - number of objects
          :   missing on primary
        - `num_objects_unfound` (int) - number of unfound objects
        - `num_objects_degraded` (int) - number of degraded objects
        - `num_rd` (int) - bytes read
        - `num_rd_kb` (int) - kbytes read
        - `num_wr` (int) - bytes written
        - `num_wr_kb` (int) - kbytes written

Ioctx.get_last_version()
:   Ioctx.get_last_version(self) -> int

    Return the version of the last object read or written to.

    This exposes the internal version number of the last object read or
    written via this io context

    Return type:
    :   `int`

    Returns:
    :   version of the last object used

Ioctx.close()
:   Ioctx.close(self)

    Close a rados.Ioctx object.

    This just tells librados that you no longer need to use the io context.
    It may not be freed immediately if there are pending asynchronous
    requests on it, but you should not use an io context again after
    calling this function on it.

### Object Operations

The Ceph Storage Cluster stores data as objects. You can read and write objects
synchronously or asynchronously. You can read and write from offsets. An object
has a name (or key) and data.

Ioctx.aio_write(*object_name*, *to_write*, *offset=0*, *oncomplete=None*, *onsafe=None*)
:   Ioctx.aio_write(self, str object_name: str, bytes to_write: bytes, int offset: int = 0, oncomplete: Optional[Callable[[Completion], None]] = None, onsafe: Optional[Callable[[Completion], None]] = None) -> Completion

    Write data to an object asynchronously

    Queues the write and returns.

    Parameters:
    :   - **object_name** (`str`) -- name of the object
        - **to_write** (`bytes`) -- data to write
        - **offset** (`int`) -- byte offset in the object to begin writing at
        - **oncomplete** (`Optional`[`Callable`[[`Completion`], `None`]]) -- what to do when the write is safe and complete in memory
          on all replicas
        - **onsafe** (`Optional`[`Callable`[[`Completion`], `None`]]) -- what to do when the write is safe and complete on storage
          on all replicas

    Raises:
    :   `Error`

    Return type:
    :   `Completion`

    Returns:
    :   completion object

Ioctx.aio_write_full(*object_name*, *to_write*, *oncomplete=None*, *onsafe=None*)
:   Ioctx.aio_write_full(self, str object_name: str, bytes to_write: bytes, oncomplete: Optional[Callable] = None, onsafe: Optional[Callable] = None) -> Completion

    Asynchronously write an entire object

    The object is filled with the provided data. If the object exists,
    it is atomically truncated and then written.
    Queues the write and returns.

    Parameters:
    :   - **object_name** (`str`) -- name of the object
        - **to_write** (`bytes`) -- data to write
        - **oncomplete** (`Optional`[`Callable`]) -- what to do when the write is safe and complete in memory
          on all replicas
        - **onsafe** (`Optional`[`Callable`]) -- what to do when the write is safe and complete on storage
          on all replicas

    Raises:
    :   `Error`

    Return type:
    :   `Completion`

    Returns:
    :   completion object

Ioctx.aio_append(*object_name*, *to_append*, *oncomplete=None*, *onsafe=None*)
:   Ioctx.aio_append(self, str object_name: str, bytes to_append: bytes, oncomplete: Optional[Callable] = None, onsafe: Optional[Callable] = None) -> Completion

    Asynchronously append data to an object

    Queues the write and returns.

    Parameters:
    :   - **object_name** (`str`) -- name of the object
        - **to_append** (`bytes`) -- data to append
        - **offset** -- byte offset in the object to begin writing at
        - **oncomplete** (`Optional`[`Callable`]) -- what to do when the write is safe and complete in memory
          on all replicas
        - **onsafe** (`Optional`[`Callable`]) -- what to do when the write is safe and complete on storage
          on all replicas

    Raises:
    :   `Error`

    Return type:
    :   `Completion`

    Returns:
    :   completion object

Ioctx.write(*key*, *data*, *offset=0*)
:   Ioctx.write(self, str key: str, bytes data: bytes, int offset: int = 0)

    Write data to an object synchronously

    Parameters:
    :   - **key** (`str`) -- name of the object
        - **data** (`bytes`) -- data to write
        - **offset** (`int`) -- byte offset in the object to begin writing at

    Raises:
    :   `TypeError`

    Raises:
    :   `LogicError`

    Returns:
    :   int - 0 on success

Ioctx.write_full(*key*, *data*)
:   Ioctx.write_full(self, str key: str, bytes data: bytes)

    Write an entire object synchronously.

    The object is filled with the provided data. If the object exists,
    it is atomically truncated and then written.

    Parameters:
    :   - **key** (`str`) -- name of the object
        - **data** (`bytes`) -- data to write

    Raises:
    :   `TypeError`

    Raises:
    :   `Error`

    Returns:
    :   int - 0 on success

Ioctx.aio_flush()
:   Ioctx.aio_flush(self)

    Block until all pending writes in an io context are safe

    Raises:
    :   `Error`

Ioctx.set_locator_key(*loc_key*)
:   Ioctx.set_locator_key(self, str loc_key: str)

    Set the key for mapping objects to pgs within an io context.

    The key is used instead of the object name to determine which
    placement groups an object is put in. This affects all subsequent
    operations of the io context - until a different locator key is
    set, all objects in this io context will be placed in the same pg.

    Parameters:
    :   **loc_key** (`str`) -- the key to use as the object locator, or NULL to discard
        any previously set key

    Raises:
    :   `TypeError`

Ioctx.aio_read(*object_name*, *length*, *offset*, *oncomplete=None*)
:   Ioctx.aio_read(self, str object_name: str, int length: int, int offset: int, oncomplete: Optional[Callable] = None) -> Completion

    Asynchronously read data from an object

    oncomplete will be called with the returned read value as
    well as the completion:

    oncomplete(completion, data_read)

    Parameters:
    :   - **object_name** (`str`) -- name of the object to read from
        - **length** (`int`) -- the number of bytes to read
        - **offset** (`int`) -- byte offset in the object to begin reading from
        - **oncomplete** (`Optional`[`Callable`]) -- what to do when the read is complete

    Raises:
    :   `Error`

    Return type:
    :   `Completion`

    Returns:
    :   completion object

Ioctx.read(*key*, *length=8192*, *offset=0*)
:   Ioctx.read(self, str key: str, int length: int = 8192, int offset: int = 0) -> bytes

    Read data from an object synchronously

    Parameters:
    :   - **key** (`str`) -- name of the object
        - **length** (`int`) -- the number of bytes to read (default=8192)
        - **offset** (`int`) -- byte offset in the object to begin reading at

    Raises:
    :   `TypeError`

    Raises:
    :   `Error`

    Return type:
    :   `bytes`

    Returns:
    :   data read from object

Ioctx.stat(*key*)
:   Ioctx.stat(self, str key: str) -> Tuple[int, time.struct_time]

    Get object stats (size/mtime)

    Parameters:
    :   **key** (`str`) -- the name of the object to get stats from

    Raises:
    :   `TypeError`

    Raises:
    :   `Error`

    Return type:
    :   `Tuple`[`int`, `struct_time`]

    Returns:
    :   (size,timestamp)

Ioctx.trunc(*key*, *size*)
:   Ioctx.trunc(self, str key: str, int size: int) -> int

    Resize an object

    If this enlarges the object, the new area is logically filled with
    zeroes. If this shrinks the object, the excess data is removed.

    Parameters:
    :   - **key** (`str`) -- the name of the object to resize
        - **size** (`int`) -- the new size of the object in bytes

    Raises:
    :   `TypeError`

    Raises:
    :   `Error`

    Return type:
    :   `int`

    Returns:
    :   0 on success, otherwise raises error

Ioctx.remove_object(*key*)
:   Ioctx.remove_object(self, str key: str) -> bool

    Delete an object

    This does not delete any snapshots of the object.

    Parameters:
    :   **key** (`str`) -- the name of the object to delete

    Raises:
    :   `TypeError`

    Raises:
    :   `Error`

    Return type:
    :   `bool`

    Returns:
    :   True on success

### Object Extended Attributes

You may set extended attributes (XATTRs) on an object. You can retrieve a list
of objects or XATTRs and iterate over them.

Ioctx.set_xattr(*key*, *xattr_name*, *xattr_value*)
:   Ioctx.set_xattr(self, str key: str, str xattr_name: str, bytes xattr_value: bytes) -> bool

    Set an extended attribute on an object.

    Parameters:
    :   - **key** (`str`) -- the name of the object to set xattr to
        - **xattr_name** (`str`) -- which extended attribute to set
        - **xattr_value** (`bytes`) -- the value of the extended attribute

    Raises:
    :   `TypeError`

    Raises:
    :   `Error`

    Return type:
    :   `bool`

    Returns:
    :   True on success, otherwise raise an error

Ioctx.get_xattrs(*oid*)
:   Ioctx.get_xattrs(self, str oid: str) -> XattrIterator

    Start iterating over xattrs on an object.

    Parameters:
    :   **oid** (`str`) -- the name of the object to get xattrs from

    Raises:
    :   `TypeError`

    Raises:
    :   `Error`

    Return type:
    :   `XattrIterator`

    Returns:
    :   XattrIterator

XattrIterator.__next__()
:   XattrIterator.__next__(self)

    Get the next xattr on the object

    Raises:
    :   StopIteration

    Returns:
    :   pair - of name and value of the next Xattr

Ioctx.get_xattr(*key*, *xattr_name*)
:   Ioctx.get_xattr(self, str key: str, str xattr_name: str) -> bytes

    Get the value of an extended attribute on an object.

    Parameters:
    :   - **key** (`str`) -- the name of the object to get xattr from
        - **xattr_name** (`str`) -- which extended attribute to read

    Raises:
    :   `TypeError`

    Raises:
    :   `Error`

    Return type:
    :   `bytes`

    Returns:
    :   value of the xattr

Ioctx.rm_xattr(*key*, *xattr_name*)
:   Ioctx.rm_xattr(self, str key: str, str xattr_name: str) -> bool

    Removes an extended attribute on from an object.

    Parameters:
    :   - **key** (`str`) -- the name of the object to remove xattr from
        - **xattr_name** (`str`) -- which extended attribute to remove

    Raises:
    :   `TypeError`

    Raises:
    :   `Error`

    Return type:
    :   `bool`

    Returns:
    :   True on success, otherwise raise an error

## Object Interface

From an I/O context, you can retrieve a list of objects from a pool and iterate
over them. The object interface provide makes each object look like a file, and
you may perform synchronous operations on the objects. For asynchronous
operations, you should use the I/O context methods.

Ioctx.list_objects()
:   Ioctx.list_objects(self) -> ObjectIterator

    Get ObjectIterator on rados.Ioctx object.

    Return type:
    :   `ObjectIterator`

    Returns:
    :   ObjectIterator

ObjectIterator.__next__()
:   ObjectIterator.__next__(self)

    Get the next object name and locator in the pool

    Raises:
    :   StopIteration

    Returns:
    :   next rados.Ioctx Object

Object.read(*length=1024 \* 1024*)

Object.write(*string_to_write*)

Object.get_xattrs()

Object.get_xattr(*xattr_name*)

Object.set_xattr(*xattr_name*, *xattr_value*)

Object.rm_xattr(*xattr_name*)

Object.stat()

Object.remove()

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).

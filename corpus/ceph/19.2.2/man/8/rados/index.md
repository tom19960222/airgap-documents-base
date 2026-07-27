---
collection: ceph
version: "19.2.2"
title: "rados -- rados object storage utility"
source_url: https://docs.ceph.com/en/squid/man/8/rados/
fetched_at: 2026-07-27T16:42:04+00:00
---
# rados -- rados object storage utility

## Synopsis

**rados** [ *options* ] [ *command* ]

## Description

**rados** is a utility for interacting with a Ceph object storage
cluster (RADOS), part of the Ceph distributed storage system.

## Global Options

--object-locator object_locator
:   Set object_locator for operation.

-p pool, --pool pool
:   Interact with the given pool. Required by most commands.

--target-pool pool
:   Select target pool by name.

--pgid
:   As an alternative to `--pool`, `--pgid` also allow users to specify the
    PG id to which the command will be directed. With this option, certain
    commands like `ls` allow users to limit the scope of the command to the given PG.

-N namespace, --namespace namespace
:   Specify the rados namespace to use for the object.

--all
:   Use with ls to list objects in all namespaces.
    Put in CEPH_ARGS environment variable to make this the default.

--default
:   Use with ls to list objects in default namespace.
    Takes precedence over --all in case --all is in environment.

-s snap, --snap snap
:   Read from the given pool snapshot. Valid for all pool-specific read operations.

--create
:   Create the pool or directory that was specified.

-i infile
:   will specify an input file to be passed along as a payload with the
    command to the monitor cluster. This is only used for specific
    monitor commands.

-m monaddress[:port]
:   Connect to specified monitor (instead of looking through ceph.conf).

-b block_size
:   Set the block size for put/get/append ops and for write benchmarking.

--striper
:   Uses the striping API of rados rather than the default one.
    Available for stat, stat2, get, put, append, truncate, rm, ls
    and all xattr related operation.

-O object_size, --object-size object_size
:   Set the object size for put/get ops and for write benchmarking.

--max-objects
:   Set the max number of objects for write benchmarking.

--lock-cookie locker-cookie
:   Will set the lock cookie for acquiring advisory lock (lock get command).
    If the cookie is not empty, this option must be passed to lock break command
    to find the correct lock when releasing lock.

--target-locator
:   Use with cp to specify the locator of the new object.

--target-nspace
:   Use with cp to specify the namespace of the new object.

## Bench options

-t N, --concurrent-ios=N
:   Set number of concurrent I/O operations.

--show-time
:   Prefix output with date/time.

--no-verify
:   Do not verify contents of read objects.

--write-object
:   Write contents to the objects.

--write-omap
:   Write contents to the omap.

--write-xattr
:   Write contents to the extended attributes.

## Load gen options

--num-objects
:   Total number of objects.

--min-object-size
:   Min object size.

--max-object-size
:   Max object size.

--min-op-len
:   Min io size of operations.

--max-op-len
:   Max io size of operations.

--max-ops
:   Max number of operations.

--max-backlog
:   Max backlog size.

--read-percent
:   Percent of operations that are read.

--target-throughput
:   Target throughput (in bytes).

--run-length
:   Total time (in seconds).

--offset-align
:   At what boundary to align random op offsets.

## Cache pools options

--with-clones
:   Include clones when doing flush or evict.

## OMAP options

--omap-key-file file
:   Read the omap key from a file.

## Generic options

-c FILE, --conf FILE
:   Read configuration from the given configuration file.

--id ID
:   Set ID portion of my name.

-n TYPE.ID, --name TYPE.ID
:   Set cephx user name.

--cluster NAME
:   Set cluster name (default: ceph).

--setuser USER
:   Set uid to user or uid (and gid to user’s gid).

--setgroup GROUP
:   Set gid to group or gid.

--version
:   Show version and quit.

## Global commands

**lspools**
:   List object pools

**df**
:   Show utilization statistics, including disk usage (bytes) and object
    counts, over the entire system and broken down by pool.

**list-inconsistent-pg** *pool*
:   List inconsistent PGs in given pool.

**list-inconsistent-obj** *pgid*
:   List inconsistent objects in given PG.

**list-inconsistent-snapset** *pgid*
:   List inconsistent snapsets in given PG.

## Pool specific commands

**get** *name* *outfile*
:   Read object name from the cluster and write it to outfile.

**put** *name* *infile* [--offset offset]
:   Write object name with start offset (default:0) to the cluster with contents from infile.
    **Warning:** The put command creates a single RADOS object, sized just as
    large as your input file. Unless your objects are of reasonable and consistent sizes, that
    is probably not what you want -- consider using RGW/S3, CephFS, or RBD instead.

**append** *name* *infile*
:   Append object name to the cluster with contents from infile.

**rm** [--force-full] *name* …
:   Remove object(s) with name(s). With `--force-full` will remove when cluster is marked full.

**listwatchers** *name*
:   List the watchers of object name.

**ls** *outfile*
:   List objects in the given pool and write to outfile. Instead of `--pool` if `--pgid` will be specified, `ls` will only list the objects in the given PG.

**lssnap**
:   List snapshots for given pool.

**mksnap** *foo*
:   Create pool snapshot named *foo*.

**rmsnap** *foo*
:   Remove pool snapshot named *foo*.

**bench** *seconds* *mode* [ -b *objsize* ] [ -t *threads* ]
:   Benchmark for *seconds*. The mode can be *write*, *seq*, or
    *rand*. *seq* and *rand* are read benchmarks, either
    sequential or random. Before running one of the reading benchmarks,
    run a write benchmark with the *--no-cleanup* option. The default
    object size is 4 MB, and the default number of simulated threads
    (parallel writes) is 16. The *--run-name <label>* option is useful
    for benchmarking a workload test from multiple clients. The *<label>*
    is an arbitrary object name. It is “benchmark_last_metadata” by
    default, and is used as the underlying object name for “read” and
    “write” ops.
    Note: -b *objsize* option is valid only in *write* mode.
    Note: *write* and *seq* must be run on the same host otherwise the
    objects created by *write* will have names that will fail *seq*.

**cleanup** [ --run-name *run_name* ] [ --prefix *prefix* ]
:   Clean up a previous benchmark operation.
    Note: the default run-name is “benchmark_last_metadata”

**listxattr** *name*
:   List all extended attributes of an object.

**getxattr** *name* *attr*
:   Dump the extended attribute value of *attr* of an object.

**setxattr** *name* *attr* *value*
:   Set the value of *attr* in the extended attributes of an object.

**rmxattr** *name* *attr*
:   Remove *attr* from the extended attributes of an object.

**stat** *name*
:   Get stat (ie. mtime, size) of given object

**stat2** *name*
:   Get stat (similar to stat, but with high precision time) of given object

**listomapkeys** *name*
:   List all the keys stored in the object map of object name.

**listomapvals** *name*
:   List all key/value pairs stored in the object map of object name.
    The values are dumped in hexadecimal.

**getomapval** [ --omap-key-file *file* ] *name* *key* [ *out-file* ]
:   Dump the hexadecimal value of key in the object map of object name.
    If the optional *out-file* argument is not provided, the value will be
    written to standard output.

**setomapval** [ --omap-key-file *file* ] *name* *key* [ *value* ]
:   Set the value of key in the object map of object name. If the optional
    *value* argument is not provided, the value will be read from standard
    input.

**rmomapkey** [ --omap-key-file *file* ] *name* *key*
:   Remove key from the object map of object name.

**getomapheader** *name*
:   Dump the hexadecimal value of the object map header of object name.

**setomapheader** *name* *value*
:   Set the value of the object map header of object name.

**export** *filename*
:   Serialize pool contents to a file or standard output.n”

**import** [--dry-run] [--no-overwrite] < filename | - >
:   Load pool contents from a file or standard input

## Examples

To view cluster utilization:

```
rados df
```

To get a list object in pool foo sent to stdout:

```
rados -p foo ls -
```

To get a list of objects in PG 0.6:

```
rados --pgid 0.6 ls
```

To write an object:

```
rados -p foo put myobject blah.txt
```

To create a snapshot:

```
rados -p foo mksnap mysnap
```

To delete the object:

```
rados -p foo rm myobject
```

To read a previously snapshotted version of an object:

```
rados -p foo -s mysnap get myobject blah.txt.old
```

To list inconsistent objects in PG 0.6:

```
rados list-inconsistent-obj 0.6 --format=json-pretty
```

## Availability

**rados** is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to
the Ceph documentation at <https://docs.ceph.com> for more information.

## See also

[ceph](../ceph/index.md)(8)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).

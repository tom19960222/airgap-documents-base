---
collection: ceph
version: "19.2.2"
title: "crushdiff -- ceph crush map test tool"
source_url: https://docs.ceph.com/en/squid/man/8/crushdiff/
fetched_at: 2026-07-27T16:42:02+00:00
---
# crushdiff -- ceph crush map test tool

## Synopsis

**crushdiff** [ --osdmap *osdmap* ] [ --pg-dump *pg-dump* ]
[ --compiled ] [ --verbose ] *command* *crushmap*

## Description

**crushdiff** is a utility that lets you test the effect of a crushmap
change: number of pgs, objects, bytes moved. This is a wrapper around
[osdmaptool](../osdmaptool/index.md)(8), relying on its **--test-map-pgs-dump**
option to get the list of changed pgs. Additionally it uses pg stats
to calculate the numbers of objects and bytes moved.

By default, **crushdiff** will use the cluster current osdmap and pg
stats, which requires access to the cluster. Though one can use the
**--osdmap** and **--pg-dump** options to test against previously
obtained data.

## Options

--compiled
:   The input/output crushmap is compiled. If the options is not
    specified the expected/returned crushmap is in txt (decompiled)
    format.

--pg-dump <pg-dump>
:   JSON output of **ceph pg dump**. If not specified **crushdiff**
    will try to get data running the command itself.

--osdmap <osdmap>
:   The cluster osdmap, obtained with **ceph osd getmap** command. If
    not specified **crushdiff** will try to get data running the
    command itself.

--verbose
:   Produce diagnostic output.

## Commands

**compare** *crushmap*
:   Compare the crushmap from *crushmap* file with the crushmap from
    the cluster osdmap. The output will show the expected number of pgs,
    objects, bytes moved when the new crushmap is installed.

**export** *crushmap*
:   Export crushmap to *crushmap* file from the cluster osdmap.

**import** *crushmap*
:   Import crushmap from *crushmap* file to the cluster osdmap.

## Example

Get the current crushmap:

```
crushdiff export cm.txt
```

Edit the map:

```
$EDITOR cm.txt
```

Check the result:

```
crushdiff compare cm.txt

79/416 (18.99%) pgs affected
281/1392 (20.19%) objects affected
80/1248 (6.41%) pg shards to move
281/4176 (6.73%) pg object shards to move
730.52Mi/10.55Gi (6.76%) bytes to move
```

When running with **--verbose** option the output will also contain
detailed information about the affected pgs, like below:

```
4.3     [0, 2, 1] -> [1, 4, 2]
4.b     [0, 1, 3] -> [2, 1, 3]
4.c     [4, 0, 1] -> [4, 1, 2]
```

i.e. a pg number, and its old and the new osd active sets.

If the result is satisfactory install the updated map:

```
crushdiff import cm.txt
```

## Availability

**crushdiff** is part of Ceph, a massively scalable, open-source, distributed storage system. Please
refer to the Ceph documentation at <https://docs.ceph.com> for more
information.

## See also

[ceph](../ceph/index.md)(8),
[crushtool](../crushtool/index.md)(8),
[osdmaptool](../osdmaptool/index.md)(8),

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).

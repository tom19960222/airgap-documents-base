---
collection: ceph
version: "19.2.2"
title: "ceph-volume-systemd -- systemd ceph-volume helper tool"
source_url: https://docs.ceph.com/en/squid/man/8/ceph-volume-systemd/
fetched_at: 2026-07-27T16:41:57+00:00
---
# ceph-volume-systemd -- systemd ceph-volume helper tool

## Synopsis

**ceph-volume-systemd** *systemd instance name*

## Description

**ceph-volume-systemd** is a systemd helper tool that receives input
from (dynamically created) systemd units so that activation of OSDs can
proceed.

It translates the input into a system call to ceph-volume for activation
purposes only.

## Examples

Its input is the `systemd instance name` (represented by `%i` in a systemd
unit), and it should be in the following format:

```
<ceph-volume subcommand>-<extra metadata>
```

In the case of `lvm` a call could look like:

```
/usr/bin/ceph-volume-systemd lvm-0-8715BEB4-15C5-49DE-BA6F-401086EC7B41
```

Which in turn will call `ceph-volume` in the following way:

```
ceph-volume lvm trigger  0-8715BEB4-15C5-49DE-BA6F-401086EC7B41
```

Any other subcommand will need to have implemented a `trigger` command that
can consume the extra metadata in this format.

## Availability

**ceph-volume-systemd** is part of Ceph, a massively scalable,
open-source, distributed storage system. Please refer to the documentation at
<http://docs.ceph.com/> for more information.

## See also

[ceph-osd](../ceph-osd/index.md)(8),

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).

---
collection: ceph
version: "20.2.4"
title: "ceph-volume-systemd -- systemd ceph-volume helper tool"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/man/8/ceph-volume-systemd.rst
fetched_at: 2026-08-18T01:32:45Z
---
:orphan:

# ceph-volume-systemd -- systemd ceph-volume helper tool

.. program:: ceph-volume-systemd

# Synopsis

| **ceph-volume-systemd** *systemd instance name*

# Description
ceph-volume-systemd is a systemd helper tool that receives input
from (dynamically created) systemd units so that activation of OSDs can
proceed.

It translates the input into a system call to ceph-volume for activation
purposes only.

# Examples
Its input is the ``systemd instance name`` (represented by ``%i`` in a systemd
unit), and it should be in the following format:

```
<ceph-volume subcommand>-<extra metadata>
```

In the case of ``lvm`` a call could look like:

```
/usr/bin/ceph-volume-systemd lvm-0-8715BEB4-15C5-49DE-BA6F-401086EC7B41
```

Which in turn will call ``ceph-volume`` in the following way:

```
ceph-volume lvm trigger  0-8715BEB4-15C5-49DE-BA6F-401086EC7B41
```

Any other subcommand will need to have implemented a ``trigger`` command that
can consume the extra metadata in this format.

# Availability

ceph-volume-systemd is part of Ceph, a massively scalable,
open-source, distributed storage system. Please refer to the documentation at
http://docs.ceph.com/ for more information.

# See also

[ceph-osd](ceph-osd.md)\(8),

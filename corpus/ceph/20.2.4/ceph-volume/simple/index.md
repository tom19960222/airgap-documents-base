---
collection: ceph
version: "20.2.4"
title: "``simple``"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/ceph-volume/simple/index.rst
fetched_at: 2026-08-18T01:32:45Z
---
.. _ceph-volume-simple:

# ``simple``
Implements the functionality needed to manage OSDs from the `simple` subcommand:
`ceph-volume simple`

**Command Line Subcommands**

* ceph-volume-simple-scan

* ceph-volume-simple-activate

* ceph-volume-simple-systemd

By *taking over* management, it disables all `ceph-disk` systemd units used
to trigger devices at startup, relying on basic (customizable) JSON
configuration and systemd for starting up OSDs.

This process involves two steps:

1. Scan the running OSD or the data device
1. Activate the scanned OSD

The scanning will infer everything that `ceph-volume` needs to start the OSD,
so that when activation is needed, the OSD can start normally without getting
interference from `ceph-disk`.

As part of the activation process the systemd units for `ceph-disk` in charge
of reacting to `udev` events, are linked to `/dev/null` so that they are
fully inactive.

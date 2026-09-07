---
collection: ceph
version: "20.2.4"
title: "``activate``"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/ceph-volume/lvm/activate.rst
fetched_at: 2026-08-18T01:32:45Z
---
.. _ceph-volume-lvm-activate:

# ``activate``

After ceph-volume-lvm-prepare has completed its run, the volume can be
activated.

Activating the volume involves enabling a `systemd` unit that persists the
`OSD ID` and its `UUID` (which is also called the `fsid` in the Ceph CLI
tools). After this information has been persisted, the cluster can determine
which OSD is enabled and must be mounted.

> **Note:** The execution of this call is fully idempotent. This means that the
> call can be executed multiple times without changing the result of its first
> successful execution.

For information about OSDs deployed by cephadm, refer to
cephadm-osd-activate.

## New OSDs
To activate newly prepared OSDs both the OSD id and OSD uuid
need to be supplied. For example:

```
ceph-volume lvm activate --bluestore 0 0263644D-0BF1-4D6D-BC34-28BD98AE3BC8
```

> **Note:** The UUID is stored in the `fsid` file in the OSD path, which is
> generated when ceph-volume-lvm-prepare is used.

## Activating all OSDs

> **Note:** For OSDs deployed by cephadm, please refer to cephadm-osd-activate
> instead.

It is possible to activate all existing OSDs at once by using the `--all`
flag. For example:

```
ceph-volume lvm activate --all
```

This call will inspect all the OSDs created by ceph-volume that are inactive
and will activate them one by one. If any of the OSDs are already running, it
will report them in the command output and skip them, making it safe to rerun
(idempotent).

### requiring uuids
The OSD uuid is being required as an extra step to ensure that the
right OSD is being activated. It is entirely possible that a previous OSD with
the same id exists and would end up activating the incorrect one.

### dmcrypt
If the OSD was prepared with dmcrypt by ceph-volume, there is no need to
specify `--dmcrypt` on the command line again (that flag is not available for
the `activate` subcommand). An encrypted OSD will be automatically detected.

## Discovery
With OSDs previously created by `ceph-volume`, a *discovery* process is
performed using LVM tags to enable the systemd units.

The systemd unit will capture the OSD id and OSD uuid and
persist it. Internally, the activation will enable it like:

```
systemctl enable ceph-volume@lvm-$id-$uuid
```

For example:

```
systemctl enable ceph-volume@lvm-0-8715BEB4-15C5-49DE-BA6F-401086EC7B41
```

Would start the discovery process for the OSD with an id of `0` and a UUID of
`8715BEB4-15C5-49DE-BA6F-401086EC7B41`.

> **Note:** for more details on the systemd workflow see ceph-volume-lvm-systemd

The systemd unit will look for the matching OSD device, and by looking at its
LVM tags will proceed to:

1. Mount the device in the corresponding location (by convention this is
`/var/lib/ceph/osd/<cluster name>-<osd id>/`)

1. Ensure that all required devices are ready for that OSD.

1. Start the `ceph-osd@0` systemd unit

> **Note:** The system infers the objectstore type by
> inspecting the LVM tags applied to the OSD devices

## Existing OSDs
For existing OSDs that have been deployed with `ceph-disk`, they need to be
scanned and activated using the simple sub-command.
If a different tool was used then the only way to port them over to the new
mechanism is to prepare them again (losing data). See
ceph-volume-lvm-existing-osds for details on how to proceed.

## Summary
To recap the `activate` process for bluestore:

1. Require both OSD id and OSD uuid
1. Enable the system unit with matching id and uuid
1. Create the `tmpfs` mount at the OSD directory in
   `/var/lib/ceph/osd/$cluster-$id/`
1. Recreate all the files needed with `ceph-bluestore-tool prime-osd-dir` by
   pointing it to the OSD `block` device.
1. The systemd unit will ensure all devices are ready and linked
1. The matching `ceph-osd` systemd unit will get started

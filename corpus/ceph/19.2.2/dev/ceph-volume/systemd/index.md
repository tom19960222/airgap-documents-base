---
collection: ceph
version: "19.2.2"
title: "systemd"
source_url: https://docs.ceph.com/en/squid/dev/ceph-volume/systemd/
fetched_at: 2026-07-27T16:43:16+00:00
---
# systemd

The workflow to *“activate”* an OSD is by relying on systemd unit files and its
ability to persist information as a suffix to the instance name.

`ceph-volume` exposes the following convention for unit files:

```
ceph-volume@<sub command>-<extra metadata>
```

For example, this is how enabling an OSD could look like for the
[lvm](../../../ceph-volume/lvm/index.md#ceph-volume-lvm) sub command:

```
systemctl enable ceph-volume@lvm-0-8715BEB4-15C5-49DE-BA6F-401086EC7B41
```

These 3 pieces of persisted information are needed by the sub-command so that
it understands what OSD it needs to activate.

Since `lvm` is not the only subcommand that will be supported, this
is how it will allow other device types to be defined.

At some point for example, for plain disks, it could be:

```
systemctl enable ceph-volume@disk-0-8715BEB4-15C5-49DE-BA6F-401086EC7B41
```

At startup, the systemd unit will execute a helper script that will parse the
suffix and will end up calling `ceph-volume` back. Using the previous
example for lvm, that call will look like:

```
ceph-volume lvm activate 0 8715BEB4-15C5-49DE-BA6F-401086EC7B41
```

> **Warning:**
>
> These workflows are not meant to be public, but are documented so that
> it is clear what the tool is doing behind the scenes. Do not alter
> any of these values.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).

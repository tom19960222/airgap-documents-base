---
collection: ceph
version: "19.2.2"
title: "systemd"
source_url: https://docs.ceph.com/en/squid/ceph-volume/systemd/
fetched_at: 2026-07-27T16:41:38+00:00
---
# systemd

As part of the activation process (either with [activate](../lvm/activate/index.md#ceph-volume-lvm-activate)
or [activate](../simple/activate/index.md#ceph-volume-simple-activate)), systemd units will get enabled that
will use the OSD id and uuid as part of their name. These units will be run
when the system boots, and will proceed to activate their corresponding
volumes via their sub-command implementation.

The API for activation is a bit loose, it only requires two parts: the
subcommand to use and any extra meta information separated by a dash. This
convention makes the units look like:

```
ceph-volume@{command}-{extra metadata}
```

The *extra metadata* can be anything needed that the subcommand implementing
the processing might need. In the case of [lvm](../lvm/index.md#ceph-volume-lvm) and
[simple](../simple/index.md#ceph-volume-simple), both look to consume the [OSD id](../../glossary/index.md#term-OSD-ID) and [OSD uuid](../../glossary/index.md#term-OSD-UUID),
but this is not a hard requirement, it is just how the sub-commands are
implemented.

Both the command and extra metadata gets persisted by systemd as part of the
*“instance name”* of the unit. For example an OSD with an ID of 0, for the
`lvm` sub-command would look like:

```
systemctl enable ceph-volume@lvm-0-0A3E1ED2-DA8A-4F0E-AA95-61DEC71768D6
```

The enabled unit is a [systemd oneshot](../../glossary/index.md#term-systemd-oneshot) service, meant to start at boot
after the local file system is ready to be used.

## Failure and Retries

It is common to have failures when a system is coming up online. The devices
are sometimes not fully available and this unpredictable behavior may cause an
OSD to not be ready to be used.

There are two configurable environment variables used to set the retry
behavior:

- `CEPH_VOLUME_SYSTEMD_TRIES`: Defaults to 30
- `CEPH_VOLUME_SYSTEMD_INTERVAL`: Defaults to 5

The *“tries”* is a number that sets the maximum number of times the unit will
attempt to activate an OSD before giving up.

The *“interval”* is a value in seconds that determines the waiting time before
initiating another try at activating the OSD.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).

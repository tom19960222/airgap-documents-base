---
collection: ceph
version: "19.2.2"
title: "Windows basic configuration"
source_url: https://docs.ceph.com/en/squid/install/windows-basic-config/
fetched_at: 2026-07-27T16:43:26+00:00
---
# Windows basic configuration

This page describes the minimum Ceph configuration required for using the
client components on Windows.

## ceph.conf

The default location for the `ceph.conf` file on Windows is
`%ProgramData%\ceph\ceph.conf`, which usually expands to
`C:\ProgramData\ceph\ceph.conf`.

Below you may find a sample. Please fill in the monitor addresses
accordingly.

```ini
[global]
    log to stderr = true
    ; Uncomment the following in order to use the Windows Event Log
    ; log to syslog = true

    run dir = C:/ProgramData/ceph/out
    crash dir = C:/ProgramData/ceph/out

    ; Use the following to change the cephfs client log level
    ; debug client = 2
[client]
    keyring = C:/ProgramData/ceph/keyring
    ; log file = C:/ProgramData/ceph/out/$name.$pid.log
    admin socket = C:/ProgramData/ceph/out/$name.$pid.asok

    ; client_permissions = true
    ; client_mount_uid = 1000
    ; client_mount_gid = 1000
[global]
    mon host = <ceph_monitor_addresses>
```

Don’t forget to also copy your keyring file to the specified location and make
sure that the configured directories exist (e.g. `C:\ProgramData\ceph\out`).

Please use slashes `/` instead of backslashes `\` as path separators
within `ceph.conf`.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).

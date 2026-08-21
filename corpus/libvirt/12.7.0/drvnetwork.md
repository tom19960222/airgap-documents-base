---
collection: libvirt
version: "12.7.0"
title: "Network driver"
source_url: https://libvirt.org/drvnetwork.html
fetched_at: 2026-08-21T04:09:36+00:00
---
# Network driver

Contents

- [Platform-specific notes](drvnetwork.md#platform-specific-notes)

  - [FreeBSD](drvnetwork.md#freebsd)

# [Platform-specific notes](drvnetwork.md#id1)

## [FreeBSD](drvnetwork.md#id2)

FreeBSD netowork driver uses the pf firewall. Libvirt managed pf rules
are created within anchors. Anchors need to be configured manually by
the user. Sample /etc/pf.conf might look like:

```
scrub all

nat-anchor "libvirt\*"
anchor "libvirt\*"

pass all
```

Users are not expected to manually modify rules in the "libvirt\\*"
subanchors because the changes will be lost on restart.

---
collection: libvirt
version: "12.7.0"
title: "macOS support"
source_url: https://libvirt.org/macos.html
fetched_at: 2026-08-21T04:09:18+00:00
---
# macOS support

Contents

- [Installation](macos.md#installation)
- [Running libvirtd locally](macos.md#running-libvirtd-locally)

Libvirt works both as client (for most drivers) and server (for the
[QEMU driver](drvqemu.md)) on macOS.

Since 8.1.0, the "hvf" domain type can be used to run
hardware-accelerated VMs on macOS via
[Hypervisor.framework](https://developer.apple.com/documentation/hypervisor).
QEMU version 2.12 or newer is needed for this to work.

# [Installation](macos.md#id1)

libvirt client (virsh), server (libvirtd) and development headers can be
installed from [Homebrew](https://brew.sh):

```
brew install libvirt
```

# [Running libvirtd locally](macos.md#id2)

The server can be started manually:

```
$ libvirtd
```

or on system boot:

```
$ brew services start libvirt
```

Once started, you can use virsh as you would on Linux.

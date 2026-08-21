---
collection: libvirt
version: "12.7.0"
title: "Internal drivers"
source_url: https://libvirt.org/drivers.html
fetched_at: 2026-08-21T04:09:17+00:00
---
# Internal drivers

- [Hypervisor drivers](drivers.md#hypervisor-drivers)
- [Storage drivers](storage.md)
- [Node device driver](drvnodedev.md)
- [Secret driver](drvsecret.md)
- [Network driver](drvnetwork.md)

The libvirt public API delegates its implementation to one or more internal
drivers, depending on the [connection URI](uri.md) passed when initializing
the library. There is always a hypervisor driver active, and if the libvirt
daemon is available there will usually be a network and storage driver active.

# Hypervisor drivers

The hypervisor drivers currently supported by libvirt are:

- [LXC](drvlxc.md) - Linux Containers
- [OpenVZ](drvopenvz.md)
- [QEMU/KVM/HVF](drvqemu.md)
- [Test](drvtest.md) - Used for testing
- [VirtualBox](drvvbox.md)
- [VMware ESX](drvesx.md)
- [VMware Workstation/Player](drvvmware.md)
- [Xen](drvxen.md)
- [Microsoft Hyper-V](drvhyperv.md)
- [Virtuozzo](drvvirtuozzo.md)
- [Bhyve](drvbhyve.md) - The BSD Hypervisor
- [Cloud Hypervisor](drvch.md)

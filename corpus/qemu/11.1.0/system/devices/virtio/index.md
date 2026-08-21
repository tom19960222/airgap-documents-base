---
collection: qemu
version: "11.1.0"
title: "VirtIO Devices"
source_url: https://www.qemu.org/docs/master/system/devices/virtio/index.html
fetched_at: 2026-08-21T03:23:10+00:00
---
# VirtIO Devices

VirtIO devices are paravirtualized devices designed to be efficient to
emulate and virtualize. Unless you are specifically trying to exercise
a driver for some particular hardware they are the recommended device
models to use for virtual machines.

The [VirtIO specification](https://docs.oasis-open.org/virtio/virtio/v1.3/virtio-v1.3.html) is an open standard managed by OASIS. It
describes how a *driver* in a guest operating system interacts with
the *device* model provided by QEMU. Multiple Operating Systems
support drivers for VirtIO with Linux perhaps having the widest range
of device types supported.

The device implementation can either be provided wholly by QEMU, or in
concert with the kernel (known as *vhost*). The device implementation
can also be off-loaded to an external process via [vhost user](vhost-user.md#vhost-user).

- [VirtIO GPU](virtio-gpu.md)
- [VirtIO Persistent Memory](virtio-pmem.md)
- [VirtIO Sound](virtio-snd.md)
- [vhost-user back ends](vhost-user.md)
- [vhost-user daemons in contrib](vhost-user-contrib.md)

---
collection: qemu
version: "11.1.0"
title: "vhost-user back ends"
source_url: https://www.qemu.org/docs/master/system/devices/virtio/vhost-user.html
fetched_at: 2026-08-21T03:23:50+00:00
---
# vhost-user back ends

vhost-user back ends are way to service the request of VirtIO devices
outside of QEMU itself. To do this there are a number of things
required.

## vhost-user device

These are simple stub devices that ensure the VirtIO device is visible
to the guest. The code is mostly boilerplate although each device has
a `chardev` option which specifies the ID of the `--chardev`
device that connects via a socket to the vhost-user *daemon*.

Each device will have an virtio-mmio and virtio-pci variant. See your
platform details for what sort of virtio bus to use.

vhost-user devices

| Device | Type | Notes |
| --- | --- | --- |
| vhost-user-blk | Block storage | [QEMU Storage Daemon](../../../tools/qemu-storage-daemon.md#storage-daemon) |
| vhost-user-fs | File based storage driver | [virtiofsd](https://gitlab.com/virtio-fs/virtiofsd) |
| vhost-user-gpio | Proxy gpio pins to host | [vhost-device-gpio](https://github.com/rust-vmm/vhost-device/tree/main/vhost-device-gpio) |
| vhost-user-gpu | GPU driver | [vhost-device-gpu](https://github.com/rust-vmm/vhost-device/tree/main/vhost-device-gpu) or [vhost-user-gpu - gpu device](vhost-user-contrib.md#vhost-user-gpu) |
| vhost-user-i2c | Proxy i2c devices to host | [vhost-device-i2c](https://github.com/rust-vmm/vhost-device/tree/main/vhost-device-i2c) |
| vhost-user-input | Generic input driver | [vhost-device-input](https://github.com/rust-vmm/vhost-device/tree/main/vhost-device-input) or [vhost-user-input - Input emulation](vhost-user-contrib.md#vhost-user-input) |
| vhost-user-rng | Entropy driver | [vhost-device-rng](https://github.com/rust-vmm/vhost-device/tree/main/vhost-device-rng) |
| vhost-user-scmi | System Control and Management Interface | [vhost-device-scmi](https://github.com/rust-vmm/vhost-device/tree/main/vhost-device-scmi) |
| vhost-user-snd | Audio device | [vhost-device-sound](https://github.com/rust-vmm/vhost-device/tree/main/vhost-device-sound) |
| vhost-user-scsi | SCSI based storage | [vhost-user-scsi - SCSI controller](vhost-user-contrib.md#vhost-user-scsi) |
| vhost-user-vsock | Socket based communication | [vhost-device-vsock](https://github.com/rust-vmm/vhost-device/tree/main/vhost-device-vsock) |
| vhost-user-spi | Proxy spi devices to host | [vhost-device-spi](https://github.com/rust-vmm/vhost-device/tree/main/vhost-device-spi) |
| vhost-user-rtc | Real time clock | [vhost-device-rtc](https://github.com/rust-vmm/vhost-device/tree/main/vhost-device-rtc) |

The referenced *daemons* are not exhaustive, any conforming backend
implementing the device and using the vhost-user protocol should work.

### vhost-user-test-device

The vhost-user-test-device is a generic development device intended
for expert use while developing new backends. The user needs to
specify all the required parameters including:

> - Device `virtio-id`
> - The `num_vqs` it needs and their `vq_size`
> - The `config_size` if needed

> **Note:**
>
> While this is a useful device for development it is not recommended
> for production use.

## vhost-user daemon

This is a separate process that is connected to by QEMU via a socket
following the [Vhost-user Protocol](../../../interop/vhost-user.md#vhost-user-proto). There are a number of daemons
that can be built when enabled by the project although any daemon that
meets the specification for a given device can be used.

## Shared memory object

In order for the daemon to access the VirtIO queues to process the
requests it needs access to the guest’s address space. This is
achieved via the `memory-backend-file`, `memory-backend-memfd`, or
`memory-backend-shm` objects.
A reference to a file-descriptor which can access this object
will be passed via the socket as part of the protocol negotiation.

Currently the shared memory object needs to match the size of the main
system memory as defined by the `-m` argument.

## Example

First start your daemon.

```
$ virtio-foo --socket-path=/var/run/foo.sock $OTHER_ARGS
```

Then you start your QEMU instance specifying the device, chardev and
memory objects.

```
$ qemu-system-x86_64 \
    -m 4096 \
    -chardev socket,id=ba1,path=/var/run/foo.sock \
    -device vhost-user-foo,chardev=ba1,$OTHER_ARGS \
    -object memory-backend-memfd,id=mem,size=4G,share=on \
    -numa node,memdev=mem \
      ...
```

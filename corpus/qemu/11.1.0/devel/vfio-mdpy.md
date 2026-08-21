---
collection: qemu
version: "11.1.0"
title: "Testing VFIO display with mdev mdpy"
source_url: https://www.qemu.org/docs/master/devel/vfio-mdpy.html
fetched_at: 2026-08-21T03:26:16+00:00
---
# [Testing VFIO display with mdev mdpy](vfio-mdpy.md#id1)

Table of Contents

- [Testing VFIO display with mdev mdpy](vfio-mdpy.md#testing-vfio-display-with-mdev-mdpy)

  - [The kernel modules](vfio-mdpy.md#the-kernel-modules)
  - [Creating an mdev instance](vfio-mdpy.md#creating-an-mdev-instance)
  - [Starting QEMU](vfio-mdpy.md#starting-qemu)

    - [Boot-time attachment](vfio-mdpy.md#boot-time-attachment)
    - [Hotplug via HMP](vfio-mdpy.md#hotplug-via-hmp)

The kernel provides a sample mediated device driver, `mdpy`
(`samples/vfio-mdev/mdpy.c`), that exposes a fake framebuffer through the VFIO
display region interface. It can be used to test VFIO display support, including
hotplug, without any real GPU hardware.

## [The kernel modules](vfio-mdpy.md#id2)

The `mdpy` driver depends on the `mdev` subsystem. Enable, build and load
the modules.

The minimal set is:

```
CONFIG_SAMPLE_VFIO_MDEV_MDPY=m
CONFIG_SAMPLE_VFIO_MDEV_MDPY_FB=m   # guest framebuffer driver
```

CONFIG_VFIO_MDEV is selected automatically.

Verify that the driver registered successfully:

```bash
ls /sys/devices/virtual/mdpy/mdpy/mdev_supported_types/
```

## [Creating an mdev instance](vfio-mdpy.md#id3)

Available types correspond to different resolutions (e.g. `mdpy-vga`
for 640x480, `mdpy-xga` for 1024x768, `mdpy-hd` for 1920x1080).

Each mdev instance is identified by a UUID:

```bash
uuid=$(uuidgen)
echo "$uuid" > /sys/devices/virtual/mdpy/mdpy/mdev_supported_types/mdpy-xga/create
```

To remove the instance later:

```bash
echo 1 > /sys/bus/mdev/devices/$uuid/remove
```

Make sure your user has the necessary permissions to access the vfio group.
(ex: chmod 666 /dev/vfio/16)

## [Starting QEMU](vfio-mdpy.md#id4)

### [Boot-time attachment](vfio-mdpy.md#id5)

```bash
qemu-system-x86_64 -machine q35 -m 1G \
    -device vfio-pci,sysfsdev=/sys/bus/mdev/devices/$uuid,display=on \
    -display gtk,gl=on
```

### [Hotplug via HMP](vfio-mdpy.md#id6)

Start QEMU with a PCIe root port (required for PCIe hotplug) and a
monitor:

```bash
qemu-system-x86_64 -machine q35 -m 1G \
    -device pcie-root-port,id=rp0,slot=1 \
    -display gtk,gl=on \
    -monitor stdio
```

Then at the `(qemu)` prompt:

```
device_add vfio-pci,sysfsdev=/sys/bus/mdev/devices/<uuid>,display=on,bus=rp0,id=mdpy0
```

To hot-unplug:

```
device_del mdpy0
```

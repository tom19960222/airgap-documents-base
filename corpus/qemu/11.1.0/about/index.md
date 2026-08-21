---
collection: qemu
version: "11.1.0"
title: "About QEMU"
source_url: https://www.qemu.org/docs/master/about/index.html
fetched_at: 2026-08-21T03:21:10+00:00
---
# About QEMU

QEMU is a generic and open source machine emulator and virtualizer.

QEMU can be used in several different ways. The most common is for
[System Emulation](../system/index.md#system-emulation), where it provides a virtual model of an
entire machine (CPU, memory and emulated devices) to run a guest OS.
In this mode the CPU may be fully emulated, or it may work with a
hypervisor such as KVM, Xen or Hypervisor.Framework to allow the
guest to run directly on the host CPU.

The second supported way to use QEMU is [User Mode Emulation](../user/index.md#user-mode-emulation),
where QEMU can launch processes compiled for one CPU on another CPU.
In this mode the CPU is always emulated.

QEMU also provides a number of standalone [command line
utilities](../tools/index.md#tools), such as the `qemu-img` disk image utility that
allows you to create, convert and modify disk images.

- [Supported build platforms](build-platforms.md)
  - [Supported host architectures](build-platforms.md#supported-host-architectures)
  - [Linux OS, macOS, FreeBSD, NetBSD, OpenBSD](build-platforms.md#linux-os-macos-freebsd-netbsd-openbsd)
  - [Windows](build-platforms.md#windows)
- [Emulation](emulation.md)
  - [Semihosting](emulation.md#semihosting)
  - [TCG Plugins](emulation.md#tcg-plugins)
  - [Other emulation features](emulation.md#other-emulation-features)
- [Deprecated features](deprecated.md)
  - [System emulator command line arguments](deprecated.md#system-emulator-command-line-arguments)
  - [QEMU Machine Protocol (QMP) commands](deprecated.md#qemu-machine-protocol-qmp-commands)
  - [Human Machine Protocol (HMP) commands](deprecated.md#human-machine-protocol-hmp-commands)
  - [Host Architectures](deprecated.md#host-architectures)
  - [System emulator CPUs](deprecated.md#system-emulator-cpus)
  - [System emulator machines](deprecated.md#system-emulator-machines)
  - [Backend options](deprecated.md#backend-options)
  - [Device options](deprecated.md#device-options)
  - [linux-user mode CPUs](deprecated.md#linux-user-mode-cpus)
  - [Backwards compatibility](deprecated.md#backwards-compatibility)
- [Removed features](removed-features.md)
  - [System emulator command line arguments](removed-features.md#system-emulator-command-line-arguments)
  - [User-mode emulator command line arguments](removed-features.md#user-mode-emulator-command-line-arguments)
  - [QEMU Machine Protocol (QMP) commands](removed-features.md#qemu-machine-protocol-qmp-commands)
  - [QEMU Machine Protocol (QMP) events](removed-features.md#qemu-machine-protocol-qmp-events)
  - [Human Monitor Protocol (HMP) commands](removed-features.md#human-monitor-protocol-hmp-commands)
  - [Host Architectures](removed-features.md#host-architectures)
  - [Guest Emulator ISAs](removed-features.md#guest-emulator-isas)
  - [System emulator CPUS](removed-features.md#system-emulator-cpus)
  - [System accelerators](removed-features.md#system-accelerators)
  - [System emulator machines](removed-features.md#system-emulator-machines)
  - [linux-user mode CPUs](removed-features.md#linux-user-mode-cpus)
  - [TCG introspection features](removed-features.md#tcg-introspection-features)
  - [Firmware, ACPI, Device Tree](removed-features.md#firmware-acpi-device-tree)
  - [System emulator devices](removed-features.md#system-emulator-devices)
  - [System emulator binaries](removed-features.md#system-emulator-binaries)
  - [Related binaries](removed-features.md#related-binaries)
  - [Block devices](removed-features.md#block-devices)
  - [VFIO devices](removed-features.md#vfio-devices)
  - [Tools](removed-features.md#tools)
  - [QEMU guest agent](removed-features.md#qemu-guest-agent)
  - [Device options](removed-features.md#device-options)
- [License](license.md)

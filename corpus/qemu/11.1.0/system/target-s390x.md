---
collection: qemu
version: "11.1.0"
title: "s390x System emulator"
source_url: https://www.qemu.org/docs/master/system/target-s390x.html
fetched_at: 2026-08-21T03:23:35+00:00
---
# s390x System emulator

QEMU can emulate z/Architecture (in particular, 64 bit) s390x systems
via the `qemu-system-s390x` binary. Only one machine type,
`s390-ccw-virtio`, is supported (with versioning for compatibility
handling).

When using KVM as accelerator, QEMU can emulate CPUs up to the generation
of the host. When using the default cpu model with TCG as accelerator,
QEMU will emulate a subset of z13 cpu features that should be enough to run
distributions built for the z13.

## Device support

QEMU will not emulate most of the traditional devices found under LPAR or
z/VM; virtio devices (especially using virtio-ccw) make up the bulk of
the available devices. Passthrough of host devices via vfio-pci, vfio-ccw,
or vfio-ap is also available.

- [Adjunct Processor (AP) Device](s390x/vfio-ap.md)
  - [Introduction](s390x/vfio-ap.md#introduction)
  - [AP Architectural Overview](s390x/vfio-ap.md#ap-architectural-overview)
  - [Start Interpretive Execution (SIE) Instruction](s390x/vfio-ap.md#start-interpretive-execution-sie-instruction)
    - [Example 1: Valid configuration](s390x/vfio-ap.md#example-1-valid-configuration)
    - [Example 2: Valid configuration](s390x/vfio-ap.md#example-2-valid-configuration)
    - [Example 3: Invalid configuration](s390x/vfio-ap.md#example-3-invalid-configuration)
  - [AP Matrix Configuration on Linux Host](s390x/vfio-ap.md#ap-matrix-configuration-on-linux-host)
    - [Binding AP devices to device drivers](s390x/vfio-ap.md#binding-ap-devices-to-device-drivers)
    - [Configuring an AP matrix for a linux guest](s390x/vfio-ap.md#configuring-an-ap-matrix-for-a-linux-guest)
    - [Starting a Linux Guest Configured with an AP Matrix](s390x/vfio-ap.md#starting-a-linux-guest-configured-with-an-ap-matrix)
    - [Hot plug a vfio-ap device into a running guest](s390x/vfio-ap.md#hot-plug-a-vfio-ap-device-into-a-running-guest)
    - [Hot unplug a vfio-ap device from a running guest](s390x/vfio-ap.md#hot-unplug-a-vfio-ap-device-from-a-running-guest)
  - [Example: Configure AP Matrices for Three Linux Guests](s390x/vfio-ap.md#example-configure-ap-matrices-for-three-linux-guests)
  - [Limitations](s390x/vfio-ap.md#limitations)
- [The virtual channel subsystem](s390x/css.md)
  - [Examples](s390x/css.md#examples)
- [3270 devices](s390x/3270.md)
  - [Example configuration](s390x/3270.md#example-configuration)
  - [Restrictions](s390x/3270.md#restrictions)
- [Subchannel passthrough via vfio-ccw](s390x/vfio-ccw.md)
  - [Example configuration](s390x/vfio-ccw.md#example-configuration)
    - [Step 1: configure the host device](s390x/vfio-ccw.md#step-1-configure-the-host-device)
    - [Step 2: configure QEMU](s390x/vfio-ccw.md#step-2-configure-qemu)
- [PCI devices on s390x](s390x/pcidevices.md)

## Architectural features

- [Boot devices on s390x](s390x/bootdevices.md)
  - [Booting with bootindex parameter](s390x/bootdevices.md#booting-with-bootindex-parameter)
  - [Booting without bootindex parameter](s390x/bootdevices.md#booting-without-bootindex-parameter)
  - [Selecting kernels with the `loadparm` property](s390x/bootdevices.md#selecting-kernels-with-the-loadparm-property)
  - [Booting from a network device](s390x/bootdevices.md#booting-from-a-network-device)
- [Protected Virtualization on s390x](s390x/protvirt.md)
  - [Prerequisites](s390x/protvirt.md#prerequisites)
  - [Running a Protected Virtual Machine](s390x/protvirt.md#running-a-protected-virtual-machine)
  - [Boot Process](s390x/protvirt.md#boot-process)
- [CPU topology on s390x](s390x/cpu-topology.md)
  - [Prerequisites](s390x/cpu-topology.md#prerequisites)
  - [Enabling CPU topology](s390x/cpu-topology.md#enabling-cpu-topology)
  - [Default topology usage](s390x/cpu-topology.md#default-topology-usage)
    - [Hot plug](s390x/cpu-topology.md#hot-plug)
    - [Examples](s390x/cpu-topology.md#examples)
  - [Polarization, entitlement and dedication](s390x/cpu-topology.md#polarization-entitlement-and-dedication)
    - [Polarization](s390x/cpu-topology.md#polarization)
    - [Entitlement](s390x/cpu-topology.md#entitlement)
  - [Defining the topology on the command line](s390x/cpu-topology.md#defining-the-topology-on-the-command-line)

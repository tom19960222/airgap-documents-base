---
collection: qemu
version: "11.1.0"
title: "Glossary"
source_url: https://www.qemu.org/docs/master/glossary.html
fetched_at: 2026-08-21T03:21:16+00:00
---
# Glossary

This section of the manual presents brief definitions of acronyms and terms used
by QEMU developers.

## Accelerator

A specific API used to accelerate execution of guest instructions. It can be
hardware-based, through a virtualization API provided by the host OS (kvm, hvf,
whpx, mshv, …), or software-based (tcg). See this description of [supported
accelerators](system/introduction.md#accelerators).

## Board

Another name for [Machine](glossary.md#machine).

## Block

Block drivers are the available [disk formats and front-ends](system/images.md#block-drivers) available, and block devices [(see Block device section on
options page)](system/invocation.md#sec-005finvocation) are using them to implement disks for a
virtual machine.

## CFI

Control Flow Integrity is a hardening technique used to prevent exploits
targeting QEMU by detecting unexpected branches during execution. QEMU [actively
supports](devel/control-flow-integrity.md#cfi) being compiled with CFI enabled.

## Device

In QEMU, a device is a piece of hardware visible to the guest. Examples include
UARTs, PCI controllers, PCI cards, VGA controllers, and many more.

QEMU is able to emulate a CPU, and all the hardware interacting with it,
including [many devices](system/device-emulation.md#device-emulation). When QEMU runs a virtual machine
using a hardware-based accelerator, it is responsible for emulating, using
software, all devices.

## EDK2

EDK2, as known as [TianoCore](https://www.tianocore.org/), is an open source
implementation of UEFI standard. QEMU virtual machines that boot a UEFI firmware
usually use EDK2.

## gdbstub

QEMU implements a [gdb server](system/gdb.md#gdb-usage), allowing gdb to attach to it and
debug a running virtual machine, or a program in user-mode. This allows
debugging the guest code that is running inside QEMU.

## glib2

[GLib2](https://docs.gtk.org/glib/) is one of the most important libraries we
are using through the codebase. It provides many data structures, macros, string
and thread utilities and portable functions across different OS. It’s required
to build QEMU.

## Guest agent

The [QEMU Guest Agent](interop/qemu-ga.md#qemu-ga) is a daemon intended to be run within virtual
machines. It provides various services to help QEMU to interact with it.

## Guest

Guest is the architecture of the virtual machine, which is emulated.
See also [Host](glossary.md#host).

Sometimes this is called the [Target](glossary.md#target) architecture, but that term
can be ambiguous.

## Host

Host is the architecture on which QEMU is running on, which is native.
See also [Guest](glossary.md#guest).

## Hypervisor

The formal definition of an hypervisor is a program or API than can be used to
manage a virtual machine. QEMU is a virtualizer, that interacts with various
hypervisors.

In the context of QEMU, an hypervisor is an API, provided by the Host OS,
allowing to execute virtual machines. Linux provides a choice of KVM, Xen
or MSHV; MacOS provides HVF; Windows provides WHPX; NetBSD provides NVMM.

## Machine

QEMU’s system emulation models many different types of hardware. A machine model
(sometimes called a board model) is the model of a complete virtual system with
RAM, one or more CPUs, and various devices. It can be selected with the option
`-machine` of qemu-system. Our machine models can be found on this [page](system/targets.md#system-targets-ref).

## Migration

QEMU can save and restore the execution of a virtual machine between different
host systems. This is provided by the [Migration framework](devel/migration/main.md#migration).

## NBD

The [QEMU Network Block Device server](tools/qemu-nbd.md#qemu-nbd) is a tool that can be used to
mount and access QEMU images, providing functionality similar to a loop device.

## Mailing List

This is [where](https://wiki.qemu.org/Contribute/MailingLists) all the
development happens! Changes are posted as series, that all developers can
review and share feedback for.

For reporting issues, our [GitLab](https://gitlab.com/qemu-project/qemu/-/issues) tracker is the best place.

## MMU / softmmu

The Memory Management Unit is responsible for translating virtual addresses to
physical addresses and managing memory protection. QEMU system mode is named
“softmmu” precisely because it implements this in software, including a TLB
(Translation lookaside buffer), for the guest virtual machine.

QEMU user-mode does not implement a full software MMU, but “simply” translates
virtual addresses by adding a specific offset, and relying on host MMU/OS
instead.

## Monitor / QMP / HMP

The [QEMU Monitor](system/monitor.md#qemu-monitor) is a text interface which can be used to interact
with a running virtual machine.

QMP stands for QEMU Monitor Protocol and is a json based interface.
HMP stands for Human Monitor Protocol and is a set of text commands available
for users who prefer natural language to json.

## MTTCG

Multiple CPU support was first implemented using a round-robin algorithm
running on a single thread. Later on, [Multi-threaded TCG](devel/multi-thread-tcg.md#mttcg) was developed
to benefit from multiple cores to speed up execution.

## Plugins

[TCG Plugins](devel/tcg-plugins.md#tcg-plugins) is an API used to instrument guest code, in system
and user mode. The end goal is to have a similar set of functionality compared
to [DynamoRIO](https://dynamorio.org/) or [valgrind](https://valgrind.org/).

One key advantage of QEMU plugins is that they can be used to perform
architecture agnostic instrumentation.

## Patchew

[Patchew](https://patchew.org/QEMU/) is a website that tracks patches on the
Mailing List.

## PR

Once a series is reviewed and accepted by a subsystem maintainer, it will be
included in a PR (Pull Request) that the project maintainer will merge into QEMU
main branch, after running tests.

The QEMU project doesn’t currently expect most developers to directly submit
pull requests.

## QCOW2

QEMU Copy On Write is a disk format developed by QEMU. It provides transparent
compression, automatic extension, and many other advantages over a raw image.

qcow2 is the recommended format to use.

## QEMU

[QEMU (Quick Emulator)](https://www.qemu.org/) is a generic and open source
machine emulator and virtualizer.

## QOM

[QEMU Object Model](devel/qom.md#qom) is an object oriented API used to define
various devices and hardware in the QEMU codebase.

## Record/replay

[Record/replay](system/replay.md#replay) is a feature of QEMU allowing to have a
deterministic and reproducible execution of a virtual machine.

## Rust

[A new programming language](https://www.rust-lang.org/), memory safe by
default. There is a work in progress to integrate it in QEMU codebase for
various subsystems.

## System mode

QEMU System mode provides a virtual model of an entire machine (CPU, memory and
emulated devices) to run a guest OS. In this mode the CPU may be fully emulated,
or it may work with a hypervisor such as KVM, Xen or Hypervisor.Framework to
allow the guest to run directly on the host CPU.

QEMU System mode is called [softmmu](glossary.md#softmmu) as well.

## Target

The term “target” can be ambiguous. In most places in QEMU it is used as a
synonym for [Guest](glossary.md#guest). For example the code for emulating Arm CPUs is in
`target/arm/`. However in the [TCG subsystem](devel/index-tcg.md#tcg) “target” refers to the
architecture which QEMU is running on, i.e. the [Host](glossary.md#host).

## TCG

TCG is the QEMU [Tiny Code Generator](devel/index-tcg.md#tcg). It is the JIT (just-in-time)
compiler we use to emulate a guest CPU in software.

It is one of the accelerators supported by QEMU, and supports a lot of
guest/host architectures.

## User mode

QEMU User mode can launch processes compiled for one CPU on another CPU. In this
mode the CPU is always emulated. In this mode, QEMU translate system calls from
guest to host kernel. It is available for Linux and BSD.

## VirtIO

VirtIO is an open standard used to define and implement virtual devices with a
minimal overhead, defining a set of data structures and hypercalls (similar to
system calls, but targeting an hypervisor, which happens to be QEMU in our
case). It’s designed to be more efficient than emulating a real device, by
minimizing the amount of interactions between a guest VM and its hypervisor.

## vhost-user

[Vhost-user](system/devices/virtio/vhost-user.md#vhost-user) is an interface used to implement VirtIO devices
outside of QEMU itself.

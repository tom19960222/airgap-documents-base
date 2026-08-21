---
collection: qemu
version: "11.1.0"
title: "Codebase"
source_url: https://www.qemu.org/docs/master/devel/codebase.html
fetched_at: 2026-08-21T03:23:08+00:00
---
# Codebase

This section presents the various parts of QEMU and how the codebase is
organized.

Beyond giving succinct descriptions, the goal is to offer links to various
parts of the documentation/codebase.

Those two videos are an excellent introduction to QEMU codebase:

- [QEMU Dev Starter guide - General overview](https://www.youtube.com/watch?v=OCBLTMKLGAk)
- [QEMU Dev Starter guide - System mode](https://www.youtube.com/watch?v=jrZ56K3Sl_k)

## Subsystems

An exhaustive list of subsystems and associated files can be found in the
[MAINTAINERS](https://gitlab.com/qemu-project/qemu/-/blob/master/MAINTAINERS)
file.

Some of the main QEMU subsystems are:

- [Accelerators](../system/introduction.md#accelerators)
- Block devices and [disk images](../system/images.md#disk-images) support
- [CI](testing/ci.md#ci) and [Tests](testing/main.md#testing)
- [Devices](../system/device-emulation.md#device-emulation) & Board models
- [Documentation](../index.md#documentation-root)
- [GDB support](../system/gdb.md#gdb-usage)
- [Migration](migration/main.md#migration)
- [Monitor](../system/monitor.md#qemu-monitor)
- [QOM (QEMU Object Model)](qom.md#qom)
- [System mode](../system/index.md#system-emulation)
- [TCG (Tiny Code Generator)](index-tcg.md#tcg)
- [User mode](../user/main.md#user-mode) ([Linux](../user/main.md#linux-user-mode) & [BSD](../user/main.md#bsd-user-mode))
- User Interfaces

More documentation on QEMU subsystems can be found on [Internal Subsystem Information](index-internals.md#internal-subsystem)
page.

## The Grand tour

We present briefly here what every folder in the top directory of the codebase
contains. Hop on!

The folder name links here will take you to that folder in our gitlab
repository. Other links will take you to more detailed documentation for that
subsystem, where we have it. Unfortunately not every subsystem has documentation
yet, so sometimes the source code is all you have.

- [accel](https://gitlab.com/qemu-project/qemu/-/tree/master/accel):
  Infrastructure and architecture agnostic code related to the various
  [accelerators](../system/introduction.md#accelerators) supported by QEMU
  (TCG, KVM, hvf, whpx, xen, nvmm, mshv).
  Contains interfaces for operations that will be implemented per
  [target](https://gitlab.com/qemu-project/qemu/-/tree/master/target).
- [audio](https://gitlab.com/qemu-project/qemu/-/tree/master/audio):
  Audio (host) support.
- [authz](https://gitlab.com/qemu-project/qemu/-/tree/master/authz):
  [QEMU Authorization framework](../system/authz.md#client-authorization).
- [backends](https://gitlab.com/qemu-project/qemu/-/tree/master/backends):
  Various backends that are used to access resources on the host (e.g. for
  random number generation, memory backing or cryptographic functions).
- [block](https://gitlab.com/qemu-project/qemu/-/tree/master/block):
  Block devices and [image formats](../system/images.md#disk-images) implementation.
- [bsd-user](https://gitlab.com/qemu-project/qemu/-/tree/master/bsd-user):
  [BSD User mode](../user/main.md#bsd-user-mode).
- build: Where the code built goes by default. You can tell the QEMU build
  system to put the built code anywhere else you like.
- [chardev](https://gitlab.com/qemu-project/qemu/-/tree/master/chardev):
  Various backends used by char devices.
- [common-user](https://gitlab.com/qemu-project/qemu/-/tree/master/common-user):
  User-mode assembly code for dealing with signals occurring during syscalls.
- [configs](https://gitlab.com/qemu-project/qemu/-/tree/master/configs):
  Makefiles defining configurations to build QEMU.
- [contrib](https://gitlab.com/qemu-project/qemu/-/tree/master/contrib):
  Community contributed devices/plugins/tools.
- [crypto](https://gitlab.com/qemu-project/qemu/-/tree/master/crypto):
  Cryptographic algorithms used in QEMU.
- [disas](https://gitlab.com/qemu-project/qemu/-/tree/master/disas):
  Disassembly functions used by QEMU target code.
- [docs](https://gitlab.com/qemu-project/qemu/-/tree/master/docs):
  QEMU Documentation.
- [dump](https://gitlab.com/qemu-project/qemu/-/tree/master/dump):
  Code to dump memory of a running VM.
- [ebpf](https://gitlab.com/qemu-project/qemu/-/tree/master/ebpf):
  eBPF program support in QEMU. [virtio-net RSS](ebpf_rss.md#ebpf-rss) uses it.
- [fpu](https://gitlab.com/qemu-project/qemu/-/tree/master/fpu):
  Floating-point software emulation.
- [fsdev](https://gitlab.com/qemu-project/qemu/-/tree/master/fsdev):
  [VirtFS](https://www.linux-kvm.org/page/VirtFS) support.
- [gdbstub](https://gitlab.com/qemu-project/qemu/-/tree/master/gdbstub):
  [GDB](../system/gdb.md#gdb-usage) support.
- [host](https://gitlab.com/qemu-project/qemu/-/tree/master/host):
  Various architecture specific header files (crypto, atomic, memory
  operations).
- [linux-headers](https://gitlab.com/qemu-project/qemu/-/tree/master/linux-headers):
  A subset of headers imported from Linux kernel and used for implementing
  KVM support and user-mode.
- [linux-user](https://gitlab.com/qemu-project/qemu/-/tree/master/linux-user):
  [User mode](../user/main.md#user-mode) implementation. Contains one folder per target
  architecture.
- [.gitlab-ci.d](https://gitlab.com/qemu-project/qemu/-/tree/master/.gitlab-ci.d):
  [CI](testing/ci.md#ci) yaml and scripts.
- [include](https://gitlab.com/qemu-project/qemu/-/tree/master/include):
  All headers associated to different subsystems in QEMU. The hierarchy used
  mirrors source code organization and naming.
- [hw](https://gitlab.com/qemu-project/qemu/-/tree/master/hw):
  [Devices](../system/device-emulation.md#device-emulation) and boards emulation. Devices are categorized by
  type/protocol/architecture and located in associated subfolder.
- [io](https://gitlab.com/qemu-project/qemu/-/tree/master/io):
  QEMU [I/O channels](https://lists.gnu.org/archive/html/qemu-devel/2015-11/msg04208.html).
- [libdecnumber](https://gitlab.com/qemu-project/qemu/-/tree/master/libdecnumber):
  Import of gcc library, used to implement decimal number arithmetic.
- [migration](https://gitlab.com/qemu-project/qemu/-/tree/master/migration):
  [Migration framework](migration/main.md#migration).
- [monitor](https://gitlab.com/qemu-project/qemu/-/tree/master/monitor):
  [Monitor](../system/monitor.md#qemu-monitor) implementation (HMP & QMP).
- [nbd](https://gitlab.com/qemu-project/qemu/-/tree/master/nbd):
  QEMU NBD (Network Block Device) server.
- [net](https://gitlab.com/qemu-project/qemu/-/tree/master/net):
  Network (host) support.
- [pc-bios](https://gitlab.com/qemu-project/qemu/-/tree/master/pc-bios):
  Contains pre-built firmware binaries and boot images, ready to use in
  QEMU without compilation.
- [plugins](https://gitlab.com/qemu-project/qemu/-/tree/master/plugins):
  [TCG plugins](../about/emulation.md#tcg-plugins) core implementation. Plugins can be found in
  [tests](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/tcg/plugins)
  and [contrib](https://gitlab.com/qemu-project/qemu/-/tree/master/contrib/plugins)
  folders.
- [po](https://gitlab.com/qemu-project/qemu/-/tree/master/po):
  Translation files.
- [python](https://gitlab.com/qemu-project/qemu/-/tree/master/python):
  Python part of our build/test system.
- [qapi](https://gitlab.com/qemu-project/qemu/-/tree/master/qapi):
  [QAPI](qapi-code-gen.md#qapi) implementation.
- [qobject](https://gitlab.com/qemu-project/qemu/-/tree/master/qobject):
  QEMU Object implementation.
- [qga](https://gitlab.com/qemu-project/qemu/-/tree/master/qga):
  QEMU [Guest agent](../interop/qemu-ga.md#qemu-ga) implementation.
- [qom](https://gitlab.com/qemu-project/qemu/-/tree/master/qom):
  QEMU [Object model](qom.md#qom) implementation, with monitor associated commands.
- [replay](https://gitlab.com/qemu-project/qemu/-/tree/master/replay):
  QEMU [Record/replay](../system/replay.md#replay) implementation.
- [roms](https://gitlab.com/qemu-project/qemu/-/tree/master/roms):
  Contains source code for various firmware and ROMs, which can be compiled if
  custom or updated versions are needed.
- [rust](https://gitlab.com/qemu-project/qemu/-/tree/master/rust):
  Rust integration in QEMU. It contains the new interfaces defined and
  associated devices using it.
- [scripts](https://gitlab.com/qemu-project/qemu/-/tree/master/scripts):
  Collection of scripts used in build and test systems, and various
  tools for QEMU codebase and execution traces.
- [scsi](https://gitlab.com/qemu-project/qemu/-/tree/master/scsi):
  Code related to SCSI support, used by SCSI devices.
- [semihosting](https://gitlab.com/qemu-project/qemu/-/tree/master/semihosting):
  QEMU [Semihosting](../about/emulation.md#semihosting) implementation.
- [stats](https://gitlab.com/qemu-project/qemu/-/tree/master/stats):
  [Monitor](../system/monitor.md#qemu-monitor) stats commands implementation.
- [storage-daemon](https://gitlab.com/qemu-project/qemu/-/tree/master/storage-daemon):
  QEMU [Storage daemon](../tools/qemu-storage-daemon.md#storage-daemon) implementation.
- [stubs](https://gitlab.com/qemu-project/qemu/-/tree/master/stubs):
  Various stubs (empty functions) used to compile QEMU with specific
  configurations.
- [subprojects](https://gitlab.com/qemu-project/qemu/-/tree/master/subprojects):
  QEMU submodules used by QEMU build system.
- [system](https://gitlab.com/qemu-project/qemu/-/tree/master/system):
  QEMU [system mode](../system/index.md#system-emulation) implementation (cpu, mmu, boot support).
- [target](https://gitlab.com/qemu-project/qemu/-/tree/master/target):
  Contains code for all target architectures supported (one subfolder
  per arch). For every architecture, you can find accelerator specific
  implementations.
- [tcg](https://gitlab.com/qemu-project/qemu/-/tree/master/tcg):
  [TCG](index-tcg.md#tcg) related code.
  Contains one subfolder per host supported architecture.
- [tests](https://gitlab.com/qemu-project/qemu/-/tree/master/tests):
  QEMU [test](testing/main.md#testing) suite

  - [data](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/data):
    Data for various tests.
  - [decode](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/decode):
    Testsuite for [decodetree](decodetree.md#decodetree) implementation.
  - [docker](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/docker):
    Code and scripts to create [containers](testing/main.md#container-ref) used in [CI](testing/ci.md#ci).
  - [fp](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/fp):
    QEMU testsuite for soft float implementation.
  - [functional](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/functional):
    [Functional tests](testing/functional.md#checkfunctional-ref) (full VM boot).
  - [lcitool](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/lcitool):
    Generate dockerfiles for CI containers.
  - [migration](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/migration):
    Test scripts and data for [Migration framework](migration/main.md#migration).
  - [multiboot](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/multiboot):
    Test multiboot functionality for x86_64/i386.
  - [qapi-schema](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/qapi-schema):
    Test scripts and data for [QAPI](testing/main.md#qapi-tests).
  - [qemu-iotests](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/qemu-iotests):
    [Disk image and block tests](testing/main.md#qemu-iotests).
  - [qtest](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/qtest):
    [Device emulation testing](testing/qtest.md#qtest).
  - [tcg](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/tcg):
    [TCG related tests](testing/main.md#checktcg-ref). Contains code per architecture
    (subfolder) and multiarch tests as well.
  - [tsan](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/tsan):
    [Suppressions](testing/main.md#tsan-suppressions) for thread sanitizer.
  - [uefi-test-tools](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/uefi-test-tools):
    Test tool for UEFI support.
  - [unit](https://gitlab.com/qemu-project/qemu/-/tree/master/tests/unit):
    QEMU [Unit tests](testing/main.md#unit-tests).
- [trace](https://gitlab.com/qemu-project/qemu/-/tree/master/trace):
  [Tracing framework](tracing.md#tracing). Used to print information associated to various
  events during execution.
- [ui](https://gitlab.com/qemu-project/qemu/-/tree/master/ui):
  QEMU User interfaces.
- [util](https://gitlab.com/qemu-project/qemu/-/tree/master/util):
  Utility code used by other parts of QEMU.

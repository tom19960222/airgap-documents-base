---
collection: qemu
version: "11.1.0"
title: "LoongArch System emulator"
source_url: https://www.qemu.org/docs/master/system/target-loongarch.html
fetched_at: 2026-08-21T03:23:27+00:00
---
# LoongArch System emulator

QEMU can emulate loongArch 64 bit systems via the
`qemu-system-loongarch64` binary. Only one machine type `virt` is
supported.

When using KVM as accelerator, QEMU can emulate la464 cpu model. And when
using the default cpu model with TCG as accelerator, QEMU will emulate a
subset of la464 cpu features that should be enough to run distributions
built for the la464.

## Board-specific documentation

- [loongson3 virt generic platform (`virt`)](loongarch/virt.md)
  - [Supported devices](loongarch/virt.md#supported-devices)
  - [CPU and machine Type](loongarch/virt.md#cpu-and-machine-type)
  - [Boot options](loongarch/virt.md#boot-options)

---
collection: qemu
version: "11.1.0"
title: "OpenRISC 1000 CPU architecture support"
source_url: https://www.qemu.org/docs/master/system/or1k/emulation.html
fetched_at: 2026-08-21T03:24:30+00:00
---
# OpenRISC 1000 CPU architecture support

QEMU’s TCG emulation includes support for the OpenRISC or1200 implementation of
the OpenRISC 1000 cpu architecture.

The or1200 cpu also has support for the following instruction subsets:

- ORBIS32 (OpenRISC Basic Instruction Set)
- ORFPX32 (OpenRISC Floating-Point eXtension)

In addition to the instruction subsets the QEMU TCG emulation also has support
for most Class II (optional) instructions.

For information on all OpenRISC instructions please refer to the latest
architecture manual available on the OpenRISC website in the
[OpenRISC Architecture](https://openrisc.io/architecture) section.

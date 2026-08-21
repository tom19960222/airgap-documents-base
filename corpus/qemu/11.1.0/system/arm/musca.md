---
collection: qemu
version: "11.1.0"
title: "Arm Musca boards ( musca-a , musca-b1 )"
source_url: https://www.qemu.org/docs/master/system/arm/musca.html
fetched_at: 2026-08-21T03:23:56+00:00
---
# Arm Musca boards (`musca-a`, `musca-b1`)

The Arm Musca development boards are a reference implementation
of a system using the SSE-200 Subsystem for Embedded. They are
dual Cortex-M33 systems.

QEMU provides models of the A and B1 variants of this board.

Unimplemented devices:

- SPI
- I2C
- I2S
- PWM
- QSPI
- Timer
- SCC
- GPIO
- eFlash
- MHU
- PVT
- SDIO
- CryptoCell

Note that (like the real hardware) the Musca-A machine is
asymmetric: CPU 0 does not have the FPU or DSP extensions,
but CPU 1 does. Also like the real hardware, the memory maps
for the A and B1 variants differ significantly, so guest
software must be built for the right variant.

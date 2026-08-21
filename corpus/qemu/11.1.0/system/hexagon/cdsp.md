---
collection: qemu
version: "11.1.0"
title: "Compute DSP"
source_url: https://www.qemu.org/docs/master/system/hexagon/cdsp.html
fetched_at: 2026-08-21T03:25:11+00:00
---
# Compute DSP

A Hexagon CDSP is designed as a computation offload device for an SoC. The
`V66G_1024` machine contains:

- L2VIC interrupt controller
- QTimer timer device

This machine will support any Hexagon CPU, but will default to `v66`.

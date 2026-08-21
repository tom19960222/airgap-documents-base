---
collection: qemu
version: "11.1.0"
title: "Siemens SX1 ( sx1 , sx1-v1 )"
source_url: https://www.qemu.org/docs/master/system/arm/sx1.html
fetched_at: 2026-08-21T03:24:17+00:00
---
# Siemens SX1 (`sx1`, `sx1-v1`)

The Siemens SX1 models v1 and v2 (default) basic emulation. The
emulation includes the following elements:

- Texas Instruments OMAP310 System-on-chip (ARM925T core)
- ROM and RAM memories (ROM firmware image can be loaded with
  -pflash) V1 1 Flash of 16MB and 1 Flash of 8MB V2 1 Flash of 32MB
- On-chip LCD controller
- On-chip Real Time Clock
- Secure Digital card connected to OMAP MMC/SD host
- Three on-chip UARTs

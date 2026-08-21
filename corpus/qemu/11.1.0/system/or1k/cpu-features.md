---
collection: qemu
version: "11.1.0"
title: "CPU Features"
source_url: https://www.qemu.org/docs/master/system/or1k/cpu-features.html
fetched_at: 2026-08-21T03:24:31+00:00
---
# CPU Features

The QEMU emulation of the OpenRISC architecture provides following built in
features.

- Shadow GPRs
- MMU TLB with 128 entries, 1 way
- Power Management (PM)
- Programmable Interrupt Controller (PIC)
- Tick Timer

These features are on by default and the presence can be confirmed by checking
the contents of the Unit Presence Register (`UPR`) and CPU Configuration
Register (`CPUCFGR`).

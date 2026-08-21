---
collection: qemu
version: "11.1.0"
title: "Migration"
source_url: https://www.qemu.org/docs/master/devel/migration/index.html
fetched_at: 2026-08-21T03:26:07+00:00
---
# Migration

This is the main entry for QEMU migration documentations. It explains how
QEMU live migration works.

- [Migration framework](main.md)
  - [Transports](main.md#transports)
  - [Common infrastructure](main.md#common-infrastructure)
  - [Saving the state of one device](main.md#saving-the-state-of-one-device)
  - [Stream structure](main.md#stream-structure)
- [Migration features](features.md)
  - [Postcopy](postcopy.md)
  - [Dirty limit](dirty-limit.md)
  - [VFIO device migration](vfio.md)
  - [Virtio device migration](virtio.md)
  - [Mapped-ram](mapped-ram.md)
  - [CheckPoint and Restart (CPR)](CPR.md)
  - [QPL Compression](qpl-compression.md)
  - [User Space Accelerator Development Kit (UADK) Compression](uadk-compression.md)
  - [QATzip Compression](qatzip-compression.md)
  - [XBZRLE (Xor Based Zero Run Length Encoding)](xbzrle.md)
- [Backwards compatibility](compatibility.md)
  - [How backwards compatibility works](compatibility.md#how-backwards-compatibility-works)
  - [A device with different features on both sides](compatibility.md#a-device-with-different-features-on-both-sides)
  - [How to mitigate when we have a backward compatibility error](compatibility.md#how-to-mitigate-when-we-have-a-backward-compatibility-error)
- [Best practices](best-practices.md)
  - [Debugging](best-practices.md#debugging)
  - [Firmware](best-practices.md#firmware)

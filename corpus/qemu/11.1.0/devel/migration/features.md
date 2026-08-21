---
collection: qemu
version: "11.1.0"
title: "Migration features"
source_url: https://www.qemu.org/docs/master/devel/migration/features.html
fetched_at: 2026-08-21T03:26:21+00:00
---
# Migration features

Migration has plenty of features to support different use cases.

- [Postcopy](postcopy.md)
  - [Enabling postcopy](postcopy.md#enabling-postcopy)
  - [Postcopy internals](postcopy.md#postcopy-internals)
  - [Postcopy features](postcopy.md#postcopy-features)
- [Dirty limit](dirty-limit.md)
- [VFIO device migration](vfio.md)
  - [System memory dirty pages tracking](vfio.md#system-memory-dirty-pages-tracking)
  - [System memory dirty pages tracking when vIOMMU is enabled](vfio.md#system-memory-dirty-pages-tracking-when-viommu-is-enabled)
  - [Live migration save path](vfio.md#live-migration-save-path)
  - [Live migration resume path](vfio.md#live-migration-resume-path)
- [Virtio device migration](virtio.md)
  - [Save state procedure](virtio.md#save-state-procedure)
  - [Load state procedure](virtio.md#load-state-procedure)
  - [Implications of this setup](virtio.md#implications-of-this-setup)
- [Mapped-ram](mapped-ram.md)
  - [Usage](mapped-ram.md#usage)
  - [Use-cases](mapped-ram.md#use-cases)
  - [RAM section format](mapped-ram.md#ram-section-format)
  - [Restrictions](mapped-ram.md#restrictions)
- [CheckPoint and Restart (CPR)](CPR.md)
  - [cpr-reboot mode](CPR.md#cpr-reboot-mode)
  - [cpr-transfer mode](CPR.md#cpr-transfer-mode)
  - [cpr-exec mode](CPR.md#cpr-exec-mode)
- [QPL Compression](qpl-compression.md)
  - [QPL Compression Framework](qpl-compression.md#qpl-compression-framework)
  - [Shared Virtual Memory(SVM) Introduction](qpl-compression.md#shared-virtual-memory-svm-introduction)
  - [How To Use QPL Compression In Migration](qpl-compression.md#how-to-use-qpl-compression-in-migration)
  - [The Difference Between QPL And ZLIB](qpl-compression.md#the-difference-between-qpl-and-zlib)
  - [The Best Practices](qpl-compression.md#the-best-practices)
- [User Space Accelerator Development Kit (UADK) Compression](uadk-compression.md)
  - [UADK Framework](uadk-compression.md#uadk-framework)
- [QATzip Compression](qatzip-compression.md)
  - [QATzip Compression Framework](qatzip-compression.md#qatzip-compression-framework)
  - [How To Use QATzip Compression](qatzip-compression.md#how-to-use-qatzip-compression)
  - [QAT Memory Requirements](qatzip-compression.md#qat-memory-requirements)
  - [How To Choose Between QATzip and QPL](qatzip-compression.md#how-to-choose-between-qatzip-and-qpl)
- [XBZRLE (Xor Based Zero Run Length Encoding)](xbzrle.md)
  - [Format](xbzrle.md#format)
  - [Cache update strategy](xbzrle.md#cache-update-strategy)
  - [Usage](xbzrle.md#usage)

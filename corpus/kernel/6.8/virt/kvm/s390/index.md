---
collection: kernel
version: "6.8"
title: "KVM for s390 systems"
source_url: https://www.kernel.org/doc/html/v6.8/virt/kvm/s390/index.html
fetched_at: 2026-08-21T03:52:45+00:00
---
# KVM for s390 systems

- [The s390 DIAGNOSE call on KVM](s390-diag.md)
  - [General remarks](s390-diag.md#general-remarks)
  - [DIAGNOSE function code 'X'500' - KVM virtio functions](s390-diag.md#diagnose-function-code-x-500-kvm-virtio-functions)
  - [DIAGNOSE function code 'X'501 - KVM breakpoint](s390-diag.md#diagnose-function-code-x-501-kvm-breakpoint)
  - [DIAGNOSE function code 'X'9C - Voluntary Time Slice Yield](s390-diag.md#diagnose-function-code-x-9c-voluntary-time-slice-yield)
- [s390 (IBM Z) Ultravisor and Protected VMs](s390-pv.md)
  - [Summary](s390-pv.md#summary)
  - [Interrupt injection](s390-pv.md#interrupt-injection)
  - [Mask notification interceptions](s390-pv.md#mask-notification-interceptions)
  - [Instruction emulation](s390-pv.md#instruction-emulation)
  - [Instruction emulation interceptions](s390-pv.md#instruction-emulation-interceptions)
  - [Links](s390-pv.md#links)
- [s390 (IBM Z) Boot/IPL of Protected VMs](s390-pv-boot.md)
  - [Summary](s390-pv-boot.md#summary)
  - [Diag308](s390-pv-boot.md#diag308)
  - [Keys](s390-pv-boot.md#keys)
- [s390 (IBM Z) Protected Virtualization dumps](s390-pv-dump.md)
  - [Summary](s390-pv-dump.md#summary)
  - [Dump process](s390-pv-dump.md#dump-process)

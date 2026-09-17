---
collection: kernel
version: "6.17"
title: "ARM"
source_url: https://www.kernel.org/doc/html/v6.17/virt/kvm/arm/index.html
fetched_at: 2026-09-16T16:43:37+00:00
---
# ARM

- [ARM firmware pseudo-registers interface](fw-pseudo-registers.md)
  - [Bitmap Feature Firmware Registers](fw-pseudo-registers.md#bitmap-feature-firmware-registers)
- [Internal ABI between the kernel and HYP](hyp-abi.md)
- [KVM/arm64-specific hypercalls exposed to guests](hypercalls.md)
  - [`ARM_SMCCC_VENDOR_HYP_KVM_FEATURES_FUNC_ID`](hypercalls.md#arm-smccc-vendor-hyp-kvm-features-func-id)
  - [`ARM_SMCCC_VENDOR_HYP_KVM_PTP_FUNC_ID`](hypercalls.md#arm-smccc-vendor-hyp-kvm-ptp-func-id)
  - [`ARM_SMCCC_KVM_FUNC_HYP_MEMINFO`](hypercalls.md#arm-smccc-kvm-func-hyp-meminfo)
  - [`ARM_SMCCC_KVM_FUNC_MEM_SHARE`](hypercalls.md#arm-smccc-kvm-func-mem-share)
  - [`ARM_SMCCC_KVM_FUNC_MEM_UNSHARE`](hypercalls.md#arm-smccc-kvm-func-mem-unshare)
  - [`ARM_SMCCC_KVM_FUNC_MMIO_GUARD`](hypercalls.md#arm-smccc-kvm-func-mmio-guard)
  - [`ARM_SMCCC_VENDOR_HYP_KVM_DISCOVER_IMPL_VER_FUNC_ID`](hypercalls.md#arm-smccc-vendor-hyp-kvm-discover-impl-ver-func-id)
  - [`ARM_SMCCC_VENDOR_HYP_KVM_DISCOVER_IMPL_CPUS_FUNC_ID`](hypercalls.md#arm-smccc-vendor-hyp-kvm-discover-impl-cpus-func-id)
- [Paravirtualized time support for arm64](pvtime.md)
  - [Stolen Time](pvtime.md#stolen-time)
- [PTP_KVM support for arm/arm64](ptp_kvm.md)
  - [`ARM_SMCCC_VENDOR_HYP_KVM_PTP_FUNC_ID`](ptp_kvm.md#arm-smccc-vendor-hyp-kvm-ptp-func-id)
- [vCPU feature selection on arm64](vcpu-features.md)
  - [KVM_ARM_VCPU_INIT](vcpu-features.md#kvm-arm-vcpu-init)
  - [The ID Registers](vcpu-features.md#the-id-registers)

---
collection: kernel
version: "6.8"
title: "Devices"
source_url: https://www.kernel.org/doc/html/v6.8/virt/kvm/devices/index.html
fetched_at: 2026-08-21T03:52:44+00:00
---
# Devices

- [ARM Virtual Interrupt Translation Service (ITS)](arm-vgic-its.md)
  - [Groups](arm-vgic-its.md#groups)
- [ARM Virtual Generic Interrupt Controller v2 (VGIC)](arm-vgic.md)
- [ARM Virtual Generic Interrupt Controller v3 and later (VGICv3)](arm-vgic-v3.md)
- [MPIC interrupt controller](mpic.md)
- [FLIC (floating interrupt controller)](s390_flic.md)
- [Generic vcpu interface](vcpu.md)
  - [1. GROUP: KVM_ARM_VCPU_PMU_V3_CTRL](vcpu.md#group-kvm-arm-vcpu-pmu-v3-ctrl)
  - [2. GROUP: KVM_ARM_VCPU_TIMER_CTRL](vcpu.md#group-kvm-arm-vcpu-timer-ctrl)
  - [3. GROUP: KVM_ARM_VCPU_PVTIME_CTRL](vcpu.md#group-kvm-arm-vcpu-pvtime-ctrl)
  - [4. GROUP: KVM_VCPU_TSC_CTRL](vcpu.md#group-kvm-vcpu-tsc-ctrl)
- [VFIO virtual device](vfio.md)
- [Generic vm interface](vm.md)
  - [1. GROUP: KVM_S390_VM_MEM_CTRL](vm.md#group-kvm-s390-vm-mem-ctrl)
  - [2. GROUP: KVM_S390_VM_CPU_MODEL](vm.md#group-kvm-s390-vm-cpu-model)
  - [2.2. ATTRIBUTE: KVM_S390_VM_CPU_PROCESSOR (r/w)](vm.md#attribute-kvm-s390-vm-cpu-processor-r-w)
  - [3. GROUP: KVM_S390_VM_TOD](vm.md#group-kvm-s390-vm-tod)
  - [4. GROUP: KVM_S390_VM_CRYPTO](vm.md#group-kvm-s390-vm-crypto)
  - [5. GROUP: KVM_S390_VM_MIGRATION](vm.md#group-kvm-s390-vm-migration)
  - [6. GROUP: KVM_ARM_VM_SMCCC_CTRL](vm.md#group-kvm-arm-vm-smccc-ctrl)
- [XICS interrupt controller](xics.md)
- [POWER9 eXternal Interrupt Virtualization Engine (XIVE Gen1)](xive.md)

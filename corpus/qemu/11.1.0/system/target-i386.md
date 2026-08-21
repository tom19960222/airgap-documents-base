---
collection: qemu
version: "11.1.0"
title: "x86 System emulator"
source_url: https://www.qemu.org/docs/master/system/target-i386.html
fetched_at: 2026-08-21T03:23:38+00:00
---
# x86 System emulator

## Board-specific documentation

- [i440fx PC (`pc-i440fx`, `pc`)](i386/pc.md)
- [‘microvm’ virtual platform (`microvm`)](i386/microvm.md)
- [‘nitro-enclave’ virtual machine (`nitro-enclave`)](i386/nitro-enclave.md)

## Architectural features

- [Recommendations for KVM CPU model configuration on x86 hosts](i386/cpu.md)
- [Syntax for configuring CPU models](i386/cpu.md#syntax-for-configuring-cpu-models)
- [Hyper-V Enlightenments](i386/hyperv.md)
- [Xen HVM guest support](i386/xen.md)
- [Xen PVH machine (`xenpvh`)](i386/xenpvh.md)
- [Paravirtualized KVM features](i386/kvm-pv.md)
- [Software Guard eXtensions (SGX)](i386/sgx.md)
- [AMD Secure Encrypted Virtualization (SEV)](i386/amd-memory-encryption.md)
- [Intel Trusted Domain eXtension (TDX)](i386/tdx.md)

## OS requirements

On x86_64 hosts, the default set of CPU features enabled by the KVM
accelerator require the host to be running Linux v4.5 or newer.

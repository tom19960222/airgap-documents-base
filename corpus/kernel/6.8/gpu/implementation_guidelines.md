---
collection: kernel
version: "6.8"
title: "Misc DRM driver uAPI- and feature implementation guidelines"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/implementation_guidelines.html
fetched_at: 2026-08-21T03:48:14+00:00
---
# Misc DRM driver uAPI- and feature implementation guidelines

- [Asynchronous VM_BIND](drm-vm-bind-async.md)
  - [Nomenclature:](drm-vm-bind-async.md#nomenclature)
  - [Synchronous / Asynchronous VM_BIND operation](drm-vm-bind-async.md#synchronous-asynchronous-vm-bind-operation)
    - [Synchronous VM_BIND](drm-vm-bind-async.md#synchronous-vm-bind)
    - [Asynchronous VM_BIND](drm-vm-bind-async.md#id1)
  - [Multi-operation VM_BIND IOCTL error handling and interrupts](drm-vm-bind-async.md#multi-operation-vm-bind-ioctl-error-handling-and-interrupts)
  - [Example: The Xe VM_BIND uAPI](drm-vm-bind-async.md#example-the-xe-vm-bind-uapi)
- [VM_BIND locking](drm-vm-bind-locking.md)
  - [The DRM GPUVM set of helpers](drm-vm-bind-locking.md#the-drm-gpuvm-set-of-helpers)
  - [Nomenclature](drm-vm-bind-locking.md#nomenclature)
  - [Locks and locking order](drm-vm-bind-locking.md#locks-and-locking-order)
  - [Protection and lifetime of gpu_vm_bos and gpu_vmas](drm-vm-bind-locking.md#protection-and-lifetime-of-gpu-vm-bos-and-gpu-vmas)
  - [Revalidation and eviction of local objects](drm-vm-bind-locking.md#revalidation-and-eviction-of-local-objects)
    - [Revalidation](drm-vm-bind-locking.md#revalidation)
    - [Eviction](drm-vm-bind-locking.md#eviction)
  - [Locking with external buffer objects](drm-vm-bind-locking.md#locking-with-external-buffer-objects)
  - [Accessing the gpu_vm's lists without the dma_resv lock held](drm-vm-bind-locking.md#accessing-the-gpu-vm-s-lists-without-the-dma-resv-lock-held)
  - [userptr gpu_vmas](drm-vm-bind-locking.md#userptr-gpu-vmas)
    - [Efficient userptr gpu_vma exec_function iteration](drm-vm-bind-locking.md#efficient-userptr-gpu-vma-exec-function-iteration)
  - [Locking at bind and unbind time](drm-vm-bind-locking.md#locking-at-bind-and-unbind-time)
  - [Locking for recoverable page-fault page-table updates](drm-vm-bind-locking.md#locking-for-recoverable-page-fault-page-table-updates)

---
collection: kernel
version: "6.8"
title: "GPU RFC Section"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/rfc/index.html
fetched_at: 2026-08-21T03:48:16+00:00
---
# GPU RFC Section

For complex work, especially new uapi, it is often good to nail the high level
design issues before getting lost in the code details. This section is meant to
host such documentation:

- Each RFC should be a section in this file, explaining the goal and main design
  considerations. Especially for uapi make sure you Cc: all relevant project
  mailing lists and involved people outside of dri-devel.
- For uapi structures add a file to this directory with and then pull the
  kerneldoc in like with real uapi headers.
- Once the code has landed move all the documentation to the right places in
  the main core, helper or driver sections.

- [I915 DG1/LMEM RFC Section](i915_gem_lmem.md)
  - [Upstream plan](i915_gem_lmem.md#upstream-plan)

- [I915 GuC Submission/DRM Scheduler Section](i915_scheduler.md)
  - [Upstream plan](i915_scheduler.md#upstream-plan)
  - [TODOs for GuC submission upstream](i915_scheduler.md#todos-for-guc-submission-upstream)
  - [New uAPI for basic GuC submission](i915_scheduler.md#new-uapi-for-basic-guc-submission)
    - [Spec references:](i915_scheduler.md#spec-references)
  - [New parallel submission uAPI](i915_scheduler.md#new-parallel-submission-uapi)
    - [Export engines logical mapping](i915_scheduler.md#export-engines-logical-mapping)
    - [A 'set_parallel' extension to configure contexts for parallel submission](i915_scheduler.md#a-set-parallel-extension-to-configure-contexts-for-parallel-submission)
    - [Extend execbuf2 IOCTL to support submitting N BBs in a single IOCTL](i915_scheduler.md#extend-execbuf2-ioctl-to-support-submitting-n-bbs-in-a-single-ioctl)

- [I915 Small BAR RFC Section](i915_small_bar.md)
  - [I915_GEM_CREATE_EXT_FLAG_NEEDS_CPU_ACCESS flag](i915_small_bar.md#i915-gem-create-ext-flag-needs-cpu-access-flag)
  - [probed_cpu_visible_size attribute](i915_small_bar.md#probed-cpu-visible-size-attribute)
  - [Error Capture restrictions](i915_small_bar.md#error-capture-restrictions)

- [I915 VM_BIND feature design and use cases](i915_vm_bind.md)
  - [VM_BIND feature](i915_vm_bind.md#vm-bind-feature)
    - [TLB flush consideration](i915_vm_bind.md#tlb-flush-consideration)
    - [Execbuf ioctl in VM_BIND mode](i915_vm_bind.md#execbuf-ioctl-in-vm-bind-mode)
    - [VM_PRIVATE objects](i915_vm_bind.md#vm-private-objects)
    - [VM_BIND locking hierarchy](i915_vm_bind.md#vm-bind-locking-hierarchy)
    - [VM_BIND LRU handling](i915_vm_bind.md#vm-bind-lru-handling)
    - [VM_BIND dma_resv usage](i915_vm_bind.md#vm-bind-dma-resv-usage)
    - [Mesa use case](i915_vm_bind.md#mesa-use-case)
  - [Other VM_BIND use cases](i915_vm_bind.md#other-vm-bind-use-cases)
    - [Long running Compute contexts](i915_vm_bind.md#long-running-compute-contexts)
      - [User/Memory Fence](i915_vm_bind.md#user-memory-fence)
      - [Low Latency Submission](i915_vm_bind.md#low-latency-submission)
    - [Debugger](i915_vm_bind.md#debugger)
    - [GPU page faults](i915_vm_bind.md#gpu-page-faults)
    - [Page level hints settings](i915_vm_bind.md#page-level-hints-settings)
    - [Page level Cache/CLOS settings](i915_vm_bind.md#page-level-cache-clos-settings)
    - [Evictable page table allocations](i915_vm_bind.md#evictable-page-table-allocations)
    - [Shared Virtual Memory (SVM) support](i915_vm_bind.md#shared-virtual-memory-svm-support)
  - [VM_BIND UAPI](i915_vm_bind.md#vm-bind-uapi)

- [Xe – Merge Acceptance Plan](xe.md)
  - [Xe – Overview](xe.md#xe-overview)
  - [Xe – Platforms](xe.md#xe-platforms)
  - [Xe – Pre-Merge Goals - Work-in-Progress](xe.md#xe-pre-merge-goals-work-in-progress)
    - [Display integration with i915](xe.md#display-integration-with-i915)
  - [Xe – uAPI high level overview](xe.md#xe-uapi-high-level-overview)
  - [Xe – Pre-Merge Goals - Completed](xe.md#xe-pre-merge-goals-completed)
    - [Drm_exec](xe.md#drm-exec)
    - [Userptr integration and vm_bind](xe.md#userptr-integration-and-vm-bind)
    - [ASYNC VM_BIND](xe.md#async-vm-bind)
    - [Drm_scheduler](xe.md#drm-scheduler)
    - [Long running compute: minimal data structure/scaffolding](xe.md#long-running-compute-minimal-data-structure-scaffolding)
    - [Dev_coredump](xe.md#dev-coredump)
    - [DRM_VM_BIND](xe.md#drm-vm-bind)
    - [GPU VA](xe.md#gpu-va)

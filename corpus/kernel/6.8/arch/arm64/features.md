---
collection: kernel
version: "6.8"
title: "Feature status on arm64 architecture"
source_url: https://www.kernel.org/doc/html/v6.8/arch/arm64/features.html
fetched_at: 2026-08-21T03:36:15+00:00
---
# Feature status on arm64 architecture

| Subsystem | Feature | Kconfig | Status | Description |
| --- | --- | --- | --- | --- |
| core | cBPF-JIT | HAVE_CBPF_JIT | TODO | arch supports cBPF JIT optimizations |
| core | eBPF-JIT | HAVE_EBPF_JIT | ok | arch supports eBPF JIT optimizations |
| core | generic-idle-thread | GENERIC_SMP_IDLE_THREAD | ok | arch makes use of the generic SMP idle thread facility |
| core | jump-labels | HAVE_ARCH_JUMP_LABEL | ok | arch supports live patched, high efficiency branches |
| core | thread-info-in-task | THREAD_INFO_IN_TASK | ok | arch makes use of the core kernel facility to embed thread_info in task_struct |
| core | tracehook | HAVE_ARCH_TRACEHOOK | ok | arch supports tracehook (ptrace) register handling APIs |
| debug | debug-vm-pgtable | ARCH_HAS_DEBUG_VM_PGTABLE | ok | arch supports pgtable tests for semantics compliance |
| debug | gcov-profile-all | ARCH_HAS_GCOV_PROFILE_ALL | ok | arch supports whole-kernel GCOV code coverage profiling |
| debug | KASAN | HAVE_ARCH_KASAN | ok | arch supports the KASAN runtime memory checker |
| debug | kcov | ARCH_HAS_KCOV | ok | arch supports kcov for coverage-guided fuzzing |
| debug | kgdb | HAVE_ARCH_KGDB | ok | arch supports the kGDB kernel debugger |
| debug | kmemleak | HAVE_DEBUG_KMEMLEAK | ok | arch supports the kernel memory leak detector |
| debug | kprobes | HAVE_KPROBES | ok | arch supports live patched kernel probe |
| debug | kprobes-on-ftrace | HAVE_KPROBES_ON_FTRACE | TODO | arch supports combined kprobes and ftrace live patching |
| debug | kretprobes | HAVE_KRETPROBES | ok | arch supports kernel function-return probes |
| debug | optprobes | HAVE_OPTPROBES | TODO | arch supports live patched optprobes |
| debug | stackprotector | HAVE_STACKPROTECTOR | ok | arch supports compiler driven stack overflow protection |
| debug | uprobes | ARCH_SUPPORTS_UPROBES | ok | arch supports live patched user probes |
| debug | user-ret-profiler | HAVE_USER_RETURN_NOTIFIER | TODO | arch supports user-space return from system call profiler |
| io | dma-contiguous | HAVE_DMA_CONTIGUOUS | ok | arch supports the DMA CMA (continuous memory allocator) |
| locking | cmpxchg-local | HAVE_CMPXCHG_LOCAL | ok | arch supports the this_cpu_cmpxchg() API |
| locking | lockdep | LOCKDEP_SUPPORT | ok | arch supports the runtime locking correctness debug facility |
| locking | queued-rwlocks | ARCH_USE_QUEUED_RWLOCKS | ok | arch supports queued rwlocks |
| locking | queued-spinlocks | ARCH_USE_QUEUED_SPINLOCKS | ok | arch supports queued spinlocks |
| perf | kprobes-event | HAVE_REGS_AND_STACK_ACCESS_API | ok | arch supports kprobes with perf events |
| perf | perf-regs | HAVE_PERF_REGS | ok | arch supports perf events register access |
| perf | perf-stackdump | HAVE_PERF_USER_STACK_DUMP | ok | arch supports perf events stack dumps |
| sched | membarrier-sync-core | ARCH_HAS_MEMBARRIER_SYNC_CORE | ok | arch supports core serializing membarrier |
| sched | numa-balancing | ARCH_SUPPORTS_NUMA_BALANCING | ok | arch supports NUMA balancing |
| seccomp | seccomp-filter | HAVE_ARCH_SECCOMP_FILTER | ok | arch supports seccomp filters |
| time | arch-tick-broadcast | ARCH_HAS_TICK_BROADCAST | ok | arch provides tick_broadcast() |
| time | clockevents | !LEGACY_TIMER_TICK | ok | arch support generic clock events |
| time | irq-time-acct | HAVE_IRQ_TIME_ACCOUNTING | ok | arch supports precise IRQ time accounting |
| time | user-context-tracking | HAVE_CONTEXT_TRACKING_USER | ok | arch supports user context tracking for NO_HZ_FULL |
| time | virt-cpuacct | HAVE_VIRT_CPU_ACCOUNTING | ok | arch supports precise virtual CPU time accounting |
| vm | batch-unmap-tlb-flush | ARCH_WANT_BATCHED_UNMAP_TLB_FLUSH | ok | arch supports deferral of TLB flush until multiple pages are unmapped |
| vm | ELF-ASLR | ARCH_WANT_DEFAULT_TOPDOWN_MMAP_LAYOUT | ok | arch randomizes the stack, heap and binary images of ELF binaries |
| vm | huge-vmap | HAVE_ARCH_HUGE_VMAP | ok | arch supports the arch_vmap_pud_supported() and arch_vmap_pmd_supported() VM APIs |
| vm | ioremap_prot | HAVE_IOREMAP_PROT | ok | arch has ioremap_prot() |
| vm | PG_uncached | ARCH_USES_PG_UNCACHED | TODO | arch supports the PG_uncached page flag |
| vm | pte_special | ARCH_HAS_PTE_SPECIAL | ok | arch supports the pte_special()/pte_mkspecial() VM APIs |
| vm | THP | HAVE_ARCH_TRANSPARENT_HUGEPAGE | ok | arch supports transparent hugepages |

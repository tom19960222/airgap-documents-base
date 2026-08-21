---
collection: qemu
version: "11.1.0"
title: "TCG Emulation"
source_url: https://www.qemu.org/docs/master/devel/index-tcg.html
fetched_at: 2026-08-21T03:23:07+00:00
---
# TCG Emulation

Details about QEMU’s Tiny Code Generator and the infrastructure
associated with emulation. You do not need to worry about this if you
are only implementing things for HW accelerated hypervisors.

- [Translator Internals](tcg.md)
  - [CPU state optimisations](tcg.md#cpu-state-optimisations)
  - [Direct block chaining](tcg.md#direct-block-chaining)
  - [Self-modifying code and translated code invalidation](tcg.md#self-modifying-code-and-translated-code-invalidation)
  - [Exception support](tcg.md#exception-support)
  - [MMU emulation](tcg.md#mmu-emulation)
  - [Profiling JITted code](tcg.md#profiling-jitted-code)
- [TCG Intermediate Representation](tcg-ops.md)
  - [Introduction](tcg-ops.md#introduction)
  - [Definitions](tcg-ops.md#definitions)
  - [Basic Blocks](tcg-ops.md#basic-blocks)
  - [Operations](tcg-ops.md#operations)
  - [Variables](tcg-ops.md#variables)
  - [Types](tcg-ops.md#types)
  - [Helpers](tcg-ops.md#helpers)
  - [Code Optimizations](tcg-ops.md#code-optimizations)
  - [Instruction Reference](tcg-ops.md#instruction-reference)
  - [Backend](tcg-ops.md#backend)
  - [Recommended coding rules for best performance](tcg-ops.md#recommended-coding-rules-for-best-performance)
- [Decodetree Specification](decodetree.md)
  - [Fields](decodetree.md#fields)
  - [Argument Sets](decodetree.md#argument-sets)
  - [Formats](decodetree.md#formats)
  - [Patterns](decodetree.md#patterns)
  - [Pattern Groups](decodetree.md#pattern-groups)
- [Multi-threaded TCG](multi-thread-tcg.md)
  - [vCPU Scheduling](multi-thread-tcg.md#vcpu-scheduling)
  - [Shared Data Structures](multi-thread-tcg.md#shared-data-structures)
  - [Memory Consistency](multi-thread-tcg.md#memory-consistency)
- [TCG Instruction Counting](tcg-icount.md)
  - [Core Concepts](tcg-icount.md#core-concepts)
- [QEMU TCG Plugins](tcg-plugins.md)
  - [Writing plugins](tcg-plugins.md#writing-plugins)
  - [Internals](tcg-plugins.md#internals)
- [Plugin API](tcg-plugins.md#plugin-api)
- [Execution Record/Replay](replay.md)
  - [Core concepts](replay.md#core-concepts)
  - [Virtual devices](replay.md#virtual-devices)
  - [Replay log format](replay.md#replay-log-format)

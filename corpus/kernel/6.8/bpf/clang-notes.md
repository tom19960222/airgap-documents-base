---
collection: kernel
version: "6.8"
title: "1 Clang implementation notes"
source_url: https://www.kernel.org/doc/html/v6.8/bpf/clang-notes.html
fetched_at: 2026-08-21T03:54:03+00:00
---
Contents

- [1 Clang implementation notes](clang-notes.md#clang-implementation-notes)

  - [1.1 Versions](clang-notes.md#versions)
  - [1.2 Arithmetic instructions](clang-notes.md#arithmetic-instructions)
  - [1.3 Jump instructions](clang-notes.md#jump-instructions)
  - [1.4 Atomic operations](clang-notes.md#atomic-operations)

# [1 Clang implementation notes](clang-notes.md#id1)

This document provides more details specific to the Clang/LLVM implementation of the eBPF instruction set.

## [1.1 Versions](clang-notes.md#id2)

Clang defined "CPU" versions, where a CPU version of 3 corresponds to the current eBPF ISA.

Clang can select the eBPF ISA version using `-mcpu=v3` for example to select version 3.

## [1.2 Arithmetic instructions](clang-notes.md#id3)

For CPU versions prior to 3, Clang v7.0 and later can enable `BPF_ALU` support with
`-Xclang -target-feature -Xclang +alu32`. In CPU version 3, support is automatically included.

## [1.3 Jump instructions](clang-notes.md#id4)

If `-O0` is used, Clang will generate the `BPF_CALL | BPF_X | BPF_JMP` (0x8d)
instruction, which is not supported by the Linux kernel verifier.

## [1.4 Atomic operations](clang-notes.md#id5)

Clang can generate atomic instructions by default when `-mcpu=v3` is
enabled. If a lower version for `-mcpu` is set, the only atomic instruction
Clang can generate is `BPF_ADD` *without* `BPF_FETCH`. If you need to enable
the atomics features, while keeping a lower `-mcpu` version, you can use
`-Xclang -target-feature -Xclang +alu32`.

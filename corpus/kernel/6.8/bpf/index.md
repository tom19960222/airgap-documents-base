---
collection: kernel
version: "6.8"
title: "BPF Documentation"
source_url: https://www.kernel.org/doc/html/v6.8/bpf/index.html
fetched_at: 2026-08-21T03:33:09+00:00
---
# BPF Documentation

This directory contains documentation for the BPF (Berkeley Packet
Filter) facility, with a focus on the extended BPF version (eBPF).

This kernel side documentation is still work in progress.
The Cilium project also maintains a [BPF and XDP Reference Guide](https://docs.cilium.io/en/latest/bpf/)
that goes into great technical depth about the BPF Architecture.

- [eBPF verifier](verifier.md)
- [libbpf](libbpf/index.md)
- [BPF Standardization](standardization/index.md)
- [BPF Type Format (BTF)](btf.md)
- [Frequently asked questions (FAQ)](faq.md)
- [Syscall API](syscall_api.md)
- [Helper functions](helpers.md)
- [BPF Kernel Functions (kfuncs)](kfuncs.md)
- [BPF cpumask kfuncs](cpumasks.md)
- [BPF filesystem kfuncs](fs_kfuncs.md)
- [Program Types](programs.md)
- [BPF maps](maps.md)
- [Running BPF programs from userspace](bpf_prog_run.md)
- [Classic BPF vs eBPF](classic_vs_extended.md)
- [BPF Iterators](bpf_iterators.md)
- [BPF licensing](bpf_licensing.md)
- [Testing and debugging BPF](test_debug.md)
- [1 Clang implementation notes](clang-notes.md)
- [1 Linux implementation notes](linux-notes.md)
- [Other](other.md)
- [Redirect](redirect.md)

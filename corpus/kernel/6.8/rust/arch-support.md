---
collection: kernel
version: "6.8"
title: "Arch Support"
source_url: https://www.kernel.org/doc/html/v6.8/rust/arch-support.html
fetched_at: 2026-08-21T03:34:24+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/rust/arch-support.md)

# Arch Support

Currently, the Rust compiler (`rustc`) uses LLVM for code generation,
which limits the supported architectures that can be targeted. In addition,
support for building the kernel with LLVM/Clang varies (please see
[Building Linux with Clang/LLVM](../kbuild/llvm.md)). This support is needed for `bindgen`
which uses `libclang`.

Below is a general summary of architectures that currently work. Level of
support corresponds to `S` values in the `MAINTAINERS` file.

| Architecture | Level of support | Constraints |
| --- | --- | --- |
| `loongarch` | Maintained |  |
| `um` | Maintained | `x86_64` only. |
| `x86` | Maintained | `x86_64` only. |

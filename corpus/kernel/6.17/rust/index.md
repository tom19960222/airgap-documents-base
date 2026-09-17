---
collection: kernel
version: "6.17"
title: "Rust"
source_url: https://www.kernel.org/doc/html/v6.17/rust/index.html
fetched_at: 2026-09-16T16:17:46+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/rust/index.md)

# Rust

Documentation related to Rust within the kernel. To start using Rust
in the kernel, please read the [Quick Start](quick-start.md) guide.

## The Rust experiment

The Rust support was merged in v6.1 into mainline in order to help in
determining whether Rust as a language was suitable for the kernel, i.e. worth
the tradeoffs.

Currently, the Rust support is primarily intended for kernel developers and
maintainers interested in the Rust support, so that they can start working on
abstractions and drivers, as well as helping the development of infrastructure
and tools.

If you are an end user, please note that there are currently no in-tree
drivers/modules suitable or intended for production use, and that the Rust
support is still in development/experimental, especially for certain kernel
configurations.

## Code documentation

Given a kernel configuration, the kernel may generate Rust code documentation,
i.e. HTML rendered by the `rustdoc` tool.

This kernel documentation was not built with Rust code documentation.

A pregenerated version is provided at:

> <https://rust.docs.kernel.org>

Please see the [Code documentation](general-information.md#rust-code-documentation) section for
more details.

- [Quick Start](quick-start.md)
- [General Information](general-information.md)
- [Coding Guidelines](coding-guidelines.md)
- [Arch Support](arch-support.md)
- [Testing](testing.md)

You can also find learning materials for Rust in its section in
[Index of Further Kernel Documentation](../process/kernel-docs.md).

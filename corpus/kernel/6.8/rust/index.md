---
collection: kernel
version: "6.8"
title: "Rust"
source_url: https://www.kernel.org/doc/html/v6.8/rust/index.html
fetched_at: 2026-08-21T03:28:45+00:00
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

This documentation does not include rustdoc generated information.

- [Quick Start](quick-start.md)
- [General Information](general-information.md)
- [Coding Guidelines](coding-guidelines.md)
- [Arch Support](arch-support.md)

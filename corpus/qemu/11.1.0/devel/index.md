---
collection: qemu
version: "11.1.0"
title: "Developer Information"
source_url: https://www.qemu.org/docs/master/devel/index.html
fetched_at: 2026-08-21T03:21:15+00:00
---
# Developer Information

This section of the manual documents various parts of the internals of
QEMU. You only need to read it if you are interested in reading or
modifying QEMU’s source code.

QEMU is a large and mature project with a number of complex subsystems
that can be overwhelming to understand. The development documentation
is not comprehensive but hopefully presents enough to get you started.
If there are areas that are unclear please reach out either via the
IRC channel or mailing list and hopefully we can improve the
documentation for future developers.

All developers will want to familiarise themselves with
[QEMU Community Processes](index-process.md#development-process) and how the community interacts. Please pay
particular attention to the [QEMU Coding Style](style.md#coding-style) and
[Submitting a Patch](submitting-a-patch.md#submitting-a-patch) sections to avoid common pitfalls.

If you wish to implement a new hardware model you will want to read
through the [The QEMU Object Model (QOM)](qom.md#qom) documentation to understand how QEMU’s object
model works.

Those wishing to enhance or add new CPU emulation capabilities will
want to read our [TCG Emulation](index-tcg.md#tcg) documentation, especially the overview of
the [Translator Internals](tcg.md#tcg-internals).

- [QEMU Community Processes](index-process.md)
- [QEMU Build System](index-build.md)
- [Testing QEMU](testing/index.md)
- [Internal QEMU APIs](index-api.md)
- [Internal Subsystem Information](index-internals.md)
- [TCG Emulation](index-tcg.md)
- [Codebase](codebase.md)

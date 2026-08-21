---
collection: kernel
version: "6.8"
title: "Working with the kernel development community"
source_url: https://www.kernel.org/doc/html/v6.8/process/index.html
fetched_at: 2026-08-21T03:28:37+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/process/index.md)
- [Chinese (Traditional)](../translations/zh_TW/process/index.md)
- [Italian](../translations/it_IT/process/index.md)
- [Spanish](../translations/sp_SP/process/index.md)

# Working with the kernel development community

So you want to be a Linux kernel developer? Welcome! While there is a lot
to be learned about the kernel in a technical sense, it is also important
to learn about how our community works. Reading these documents will make
it much easier for you to get your changes merged with a minimum of
trouble.

## An introduction to how kernel development works

Read these documents first: an understanding of the material here will ease
your entry into the kernel community.

- [HOWTO do Linux kernel development](howto.md)
- [A guide to the Kernel Development Process](development-process.md)
- [Submitting patches: the essential guide to getting your code into the kernel](submitting-patches.md)
- [Linux Kernel patch submission checklist](submit-checklist.md)

## Tools and technical guides for kernel developers

This is a collection of material that kernel developers should be familiar
with.

- [Minimal requirements to compile the Kernel](changes.md)
- [Programming Language](programming-language.md)
- [Linux kernel coding style](coding-style.md)
- [Kernel Maintainer PGP guide](maintainer-pgp-guide.md)
- [Email clients info for Linux](email-clients.md)
- [Applying Patches To The Linux Kernel](applying-patches.md)
- [Backporting and conflict resolution](backporting.md)
- [Adding a New System Call](adding-syscalls.md)
- [Why the "volatile" type class should not be used](volatile-considered-harmful.md)
- [(How to avoid) Botching up ioctls](botching-up-ioctls.md)

## Policy guides and developer statements

These are the rules that we try to live by in the kernel community (and
beyond).

- [Linux kernel licensing rules](license-rules.md)
- [Contributor Covenant Code of Conduct](code-of-conduct.md)
- [Linux Kernel Contributor Covenant Code of Conduct Interpretation](code-of-conduct-interpretation.md)
- [Linux Kernel Contribution Maturity Model](contribution-maturity-model.md)
- [Linux Kernel Enforcement Statement](kernel-enforcement-statement.md)
- [Kernel Driver Statement](kernel-driver-statement.md)
- [The Linux Kernel Driver Interface](stable-api-nonsense.md)
- [Everything you ever wanted to know about Linux -stable releases](stable-kernel-rules.md)
- [Linux kernel management style](management-style.md)
- [Researcher Guidelines](researcher-guidelines.md)

## Dealing with bugs

Bugs are a fact of life; it is important that we handle them properly.
The documents below describe our policies around the handling of a couple
of special classes of bugs: regressions and security problems.

- [Handling regressions](handling-regressions.md)
- [Security bugs](security-bugs.md)
- [CVEs](cve.md)
- [Embargoed hardware issues](embargoed-hardware-issues.md)

## Maintainer information

How to find the people who will accept your patches.

- [Subsystem and maintainer tree specific development process notes](maintainer-handbooks.md)
- [List of maintainers](maintainers.md)

## Other material

Here are some other guides to the community that are of interest to most
developers:

- [Index of Further Kernel Documentation](kernel-docs.md)
- [Deprecated Interfaces, Language Features, Attributes, and Conventions](deprecated.md)

These are some overall technical guides that have been put here for now for
lack of a better place.

- [Linux magic numbers](magic-number.md)
- [clang-format](clang-format.md)
- [arch/riscv maintenance guidelines for developers](../arch/riscv/patch-acceptance.md)
- [Unaligned Memory Accesses](../core-api/unaligned-memory-access.md)

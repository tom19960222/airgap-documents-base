---
collection: kernel
version: "6.8"
title: "Subsystem and maintainer tree specific development process notes"
source_url: https://www.kernel.org/doc/html/v6.8/process/maintainer-handbooks.html
fetched_at: 2026-08-21T03:29:19+00:00
---
English

- [Italian](../translations/it_IT/process/maintainer-handbooks.md)

# Subsystem and maintainer tree specific development process notes

The purpose of this document is to provide subsystem specific information
which is supplementary to the general development process handbook
[Documentation/process](development-process.md#development-process-main).

Contents:

- [1. Networking subsystem (netdev)](maintainer-netdev.md)
  - [1.1. tl;dr](maintainer-netdev.md#tl-dr)
  - [1.2. netdev](maintainer-netdev.md#netdev)
  - [1.3. Development cycle](maintainer-netdev.md#development-cycle)
  - [1.4. git trees and patch flow](maintainer-netdev.md#git-trees-and-patch-flow)
  - [1.5. netdev patch review](maintainer-netdev.md#netdev-patch-review)
  - [1.6. Preparing changes](maintainer-netdev.md#preparing-changes)
  - [1.7. Testing](maintainer-netdev.md#testing)
  - [1.8. Reviewer guidance](maintainer-netdev.md#reviewer-guidance)
  - [1.9. Testimonials / feedback](maintainer-netdev.md#testimonials-feedback)
- [2. SoC Subsystem](maintainer-soc.md)
  - [2.1. Overview](maintainer-soc.md#overview)
  - [2.2. Information for (new) Submaintainers](maintainer-soc.md#information-for-new-submaintainers)
- [3. SoC Platforms with DTS Compliance Requirements](maintainer-soc-clean-dts.md)
  - [3.1. Overview](maintainer-soc-clean-dts.md#overview)
  - [3.2. Strict DTS DT Schema and dtc Compliance](maintainer-soc-clean-dts.md#strict-dts-dt-schema-and-dtc-compliance)
- [4. The tip tree handbook](maintainer-tip.md)
  - [4.1. What is the tip tree?](maintainer-tip.md#what-is-the-tip-tree)
  - [4.2. Patch submission notes](maintainer-tip.md#patch-submission-notes)
  - [4.3. Coding style notes](maintainer-tip.md#coding-style-notes)
  - [4.4. Commit notifications](maintainer-tip.md#commit-notifications)
- [5. KVM x86](maintainer-kvm-x86.md)
  - [5.1. Foreword](maintainer-kvm-x86.md#foreword)
  - [5.2. TL;DR](maintainer-kvm-x86.md#tl-dr)
  - [5.3. Trees](maintainer-kvm-x86.md#trees)
  - [5.4. Development](maintainer-kvm-x86.md#development)
  - [5.5. Testing](maintainer-kvm-x86.md#testing)
  - [5.6. Posting](maintainer-kvm-x86.md#posting)
  - [5.7. Notifications](maintainer-kvm-x86.md#notifications)
  - [5.8. Vulnerabilities](maintainer-kvm-x86.md#vulnerabilities)

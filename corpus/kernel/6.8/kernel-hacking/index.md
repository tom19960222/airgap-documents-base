---
collection: kernel
version: "6.8"
title: "Kernel Hacking Guides"
source_url: https://www.kernel.org/doc/html/v6.8/kernel-hacking/index.html
fetched_at: 2026-08-21T03:28:43+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/kernel-hacking/index.md)
- [Italian](../translations/it_IT/kernel-hacking/index.md)

# Kernel Hacking Guides

- [Unreliable Guide To Hacking The Linux Kernel](hacking.md)
  - [Introduction](hacking.md#introduction)
  - [The Players](hacking.md#the-players)
  - [Some Basic Rules](hacking.md#some-basic-rules)
  - [ioctls: Not writing a new system call](hacking.md#ioctls-not-writing-a-new-system-call)
  - [Recipes for Deadlock](hacking.md#recipes-for-deadlock)
  - [Common Routines](hacking.md#common-routines)
  - [Wait Queues `include/linux/wait.h`](hacking.md#wait-queues-include-linux-wait-h)
  - [Atomic Operations](hacking.md#atomic-operations)
  - [Symbols](hacking.md#symbols)
  - [Routines and Conventions](hacking.md#routines-and-conventions)
  - [Putting Your Stuff in the Kernel](hacking.md#putting-your-stuff-in-the-kernel)
  - [Kernel Cantrips](hacking.md#kernel-cantrips)
  - [Thanks](hacking.md#thanks)
- [Unreliable Guide To Locking](locking.md)
  - [Introduction](locking.md#introduction)
  - [The Problem With Concurrency](locking.md#the-problem-with-concurrency)
  - [Locking in the Linux Kernel](locking.md#locking-in-the-linux-kernel)
  - [Hard IRQ Context](locking.md#hard-irq-context)
  - [Cheat Sheet For Locking](locking.md#cheat-sheet-for-locking)
  - [The trylock Functions](locking.md#the-trylock-functions)
  - [Common Examples](locking.md#common-examples)
  - [Common Problems](locking.md#common-problems)
  - [Locking Speed](locking.md#locking-speed)
  - [What Functions Are Safe To Call From Interrupts?](locking.md#what-functions-are-safe-to-call-from-interrupts)
  - [Mutex API reference](locking.md#mutex-api-reference)
  - [Futex API reference](locking.md#futex-api-reference)
  - [Further reading](locking.md#further-reading)
  - [Thanks](locking.md#thanks)
  - [Glossary](locking.md#glossary)
- [False Sharing](false-sharing.md)
  - [What is False Sharing](false-sharing.md#what-is-false-sharing)
  - [False Sharing Pitfalls](false-sharing.md#false-sharing-pitfalls)
  - [How to detect and analyze False Sharing](false-sharing.md#how-to-detect-and-analyze-false-sharing)
  - [Possible Mitigations](false-sharing.md#possible-mitigations)
  - [Miscellaneous](false-sharing.md#miscellaneous)

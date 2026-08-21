---
collection: kernel
version: "6.8"
title: "eBPF 用户空间API"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/userspace-api/ebpf/index.html
fetched_at: 2026-08-21T03:56:35+00:00
---
Chinese (Simplified)

- [English](../../../../userspace-api/ebpf/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [eBPF Userspace API](../../../../userspace-api/ebpf/index.md)

翻译
:   李睿 Rui Li <[me@lirui.org](mailto:me%40lirui.org)>

# eBPF 用户空间API

eBPF是一种在Linux内核中提供沙箱化运行环境的机制，它可以在不改变内核源码或加载
内核模块的情况下扩展运行时和编写工具。eBPF程序能够被附加到各种内核子系统中，包
括网络，跟踪和Linux安全模块(LSM)等。

关于eBPF的内部内核文档，请查看 [BPF Documentation](../../../../bpf/index.md) 。

- [eBPF Syscall](syscall.md)

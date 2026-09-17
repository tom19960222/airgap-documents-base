---
collection: kernel
version: "6.17"
title: "eBPF Syscall"
source_url: https://www.kernel.org/doc/html/v6.17/translations/zh_CN/userspace-api/ebpf/syscall.html
fetched_at: 2026-09-16T16:49:54+00:00
---
Chinese (Simplified)

- [English](../../../../userspace-api/ebpf/syscall.md)

> **Note:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请发建议或者补丁给
> 该文件的译者，或者请求中文文档维护者和审阅者的帮助。

Original:
:   [eBPF Syscall](../../../../userspace-api/ebpf/syscall.md)

翻译:
:   李睿 Rui Li <[me@lirui.org](mailto:me%40lirui.org)>

# eBPF Syscall

作者:
:   - Alexei Starovoitov <[ast@kernel.org](mailto:ast%40kernel.org)>
    - Joe Stringer <[joe@wand.net.nz](mailto:joe%40wand.net.nz)>
    - Michael Kerrisk <[mtk.manpages@gmail.com](mailto:mtk.manpages%40gmail.com)>

bpf syscall的主要信息可以在 [man-pages](https://www.kernel.org/doc/man-pages/) 中的 [bpf(2)](https://man7.org/linux/man-pages/man2/bpf.2.html) 找到。

## bpf() 子命令参考

子命令在以下内核代码中：

include/uapi/linux/bpf.h

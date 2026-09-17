---
collection: kernel
version: "6.17"
title: "内核骇客指南"
source_url: https://www.kernel.org/doc/html/v6.17/translations/zh_CN/kernel-hacking/index.html
fetched_at: 2026-09-16T16:21:51+00:00
---
Chinese (Simplified)

- [English](../../../kernel-hacking/index.md)
- [Italian](../../it_IT/kernel-hacking/index.md)

> **Note:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请发建议或者补丁给
> 该文件的译者，或者请求中文文档维护者和审阅者的帮助。

Original:
:   [Kernel Hacking Guides](../../../kernel-hacking/index.md)

译者:
:   吴想成 Wu XiangCheng <[bobwxc@email.cn](mailto:bobwxc%40email.cn)>

# 内核骇客指南

- [内核骇客指北](hacking.md)
  - [引言](hacking.md#id2)
  - [玩家](hacking.md#id3)
  - [一些基本规则](hacking.md#id5)
  - [输入输出控制（ioctls）：避免编写新的系统调用](hacking.md#ioctls)
  - [死锁的“配方”](hacking.md#id6)
  - [常用函数/程序](hacking.md#id7)
  - [等待队列 `include/linux/wait.h`](hacking.md#include-linux-wait-h)
  - [原子操作](hacking.md#id11)
  - [符号](hacking.md#id12)
  - [程序与惯例](hacking.md#id13)
  - [把你的东西放进内核里](hacking.md#id17)
  - [Kernel 仙女棒](hacking.md#kernel)
  - [致谢](hacking.md#id18)

TODO

- locking

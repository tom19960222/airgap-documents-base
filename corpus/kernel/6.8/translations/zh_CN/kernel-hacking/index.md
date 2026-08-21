---
collection: kernel
version: "6.8"
title: "内核骇客指南"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/kernel-hacking/index.html
fetched_at: 2026-08-21T03:33:48+00:00
---
Chinese (Simplified)

- [English](../../../kernel-hacking/index.md)
- [Italian](../../it_IT/kernel-hacking/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Kernel Hacking Guides](../../../kernel-hacking/index.md)

译者
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

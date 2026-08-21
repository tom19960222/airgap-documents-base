---
collection: kernel
version: "6.8"
title: "与Linux 内核社区一起工作"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/process/index.html
fetched_at: 2026-08-21T03:29:47+00:00
---
Chinese (Simplified)

- [English](../../../process/index.md)
- [Chinese (Traditional)](../../zh_TW/process/index.md)
- [Italian](../../it_IT/process/index.md)
- [Spanish](../../sp_SP/process/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Working with the kernel development community](../../../process/index.md)

翻译
:   Alex Shi <[alex.shi@linux.alibaba.com](mailto:alex.shi%40linux.alibaba.com)>

# 与Linux 内核社区一起工作

你想成为Linux内核开发人员吗？欢迎之至！在学习许多关于内核的技术知识的同时，
了解我们社区的工作方式也很重要。阅读这些文档可以让您以更轻松的、麻烦更少的
方式将更改合并到内核。

以下是每位开发人员都应阅读的基本指南：

- [Linux内核许可规则](license-rules.md)
- [如何参与Linux内核开发](howto.md)
- [贡献者契约行为准则](code-of-conduct.md)
- [Linux内核贡献者契约行为准则解释](code-of-conduct-interpretation.md)
- [内核开发过程指南](development-process.md)
- [提交补丁：如何让你的改动进入内核](submitting-patches.md)
- [程序设计语言](programming-language.md)
- [Linux 内核代码风格](coding-style.md)
- [内核维护者 PGP 指南](maintainer-pgp-guide.md)
- [Linux邮件客户端配置信息](email-clients.md)
- [Linux 内核执行声明](kernel-enforcement-statement.md)
- [内核驱动声明](kernel-driver-statement.md)

TODOLIST:

- handling-regressions
- maintainer-handbooks

安全方面, 请阅读:

- [被限制的硬件问题](embargoed-hardware-issues.md)

TODOLIST:

- security-bugs

其它大多数开发人员感兴趣的社区指南：

- [Linux 内核驱动接口](stable-api-nonsense.md)
- [Linux内核管理风格](management-style.md)
- [所有你想知道的事情 - 关于linux稳定版发布](stable-kernel-rules.md)
- [Linux内核补丁提交检查单](submit-checklist.md)

TODOLIST:

- changes
- kernel-docs
- deprecated
- maintainers
- researcher-guidelines
- contribution-maturity-model

这些是一些总体性技术指南，由于不大好分类而放在这里：

- [Linux 魔术数](magic-number.md)
- [为什么不应该使用“volatile”类型](volatile-considered-harmful.md)
- [arch/riscv 开发者维护指南](../arch/riscv/patch-acceptance.md)
- [非对齐内存访问](../core-api/unaligned-memory-access.md)

TODOLIST:

- applying-patches
- backporting
- adding-syscalls
- botching-up-ioctls
- clang-format

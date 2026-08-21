---
collection: kernel
version: "6.8"
title: "内核开发过程指南"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/process/development-process.html
fetched_at: 2026-08-21T03:29:13+00:00
---
Chinese (Simplified)

- [English](../../../process/development-process.md)
- [Chinese (Traditional)](../../zh_TW/process/development-process.md)
- [Italian](../../it_IT/process/development-process.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Documentation/process/development-process.rst](../../../process/development-process.md#development-process-main)

Translator
:   Alex Shi <[alex.shi@linux.alibaba.com](mailto:alex.shi%40linux.alibaba.com)>

# 内核开发过程指南

本文档的目的是帮助开发人员（及其经理）以最小的挫折感与开发社区合作。它试图记录这个社区如何以一种不熟悉Linux内核开发（或者实际上是自由软件开发）的人可以访问的方式工作。虽然这里有一些技术资料，但这是一个面向过程的讨论，不需要深入了解内核编程就可以理解。

内容

- [1. 引言](1.Intro.md)
  - [1.1. 内容提要](1.Intro.md#id2)
  - [1.2. 这个文档是关于什么的](1.Intro.md#id3)
  - [1.3. 致谢](1.Intro.md#id4)
  - [1.4. 代码进入主线的重要性](1.Intro.md#id5)
  - [1.5. 许可](1.Intro.md#id6)
- [2. 开发流程如何进行](2.Process.md)
  - [2.1. 总览](2.Process.md#id2)
  - [2.2. 补丁的生命周期](2.Process.md#id3)
  - [2.3. 补丁如何进入内核](2.Process.md#id4)
  - [2.4. Next 树](2.Process.md#next)
  - [2.5. Staging 树](2.Process.md#staging)
  - [2.6. 工具](2.Process.md#id5)
  - [2.7. 邮件列表](2.Process.md#id6)
  - [2.8. 开始内核开发](2.Process.md#id7)
- [3. 早期规划](3.Early-stage.md)
  - [3.1. 搞清问题](3.Early-stage.md#id2)
  - [3.2. 早期讨论](3.Early-stage.md#id3)
  - [3.3. 找谁交流？](3.Early-stage.md#id4)
  - [3.4. 何时邮寄？](3.Early-stage.md#id5)
  - [3.5. 获得官方认可](3.Early-stage.md#id6)
- [4. 使代码正确](4.Coding.md)
  - [4.1. 陷阱](4.Coding.md#id2)
  - [4.2. 代码检查工具](4.Coding.md#id8)
  - [4.3. 文档](4.Coding.md#id9)
  - [4.4. 内部API更改](4.Coding.md#api)
- [5. 发布补丁](5.Posting.md)
  - [5.1. 何时寄送](5.Posting.md#id2)
  - [5.2. 创建补丁之前](5.Posting.md#id3)
  - [5.3. 补丁准备](5.Posting.md#id4)
  - [5.4. 补丁格式和更改日志](5.Posting.md#id5)
  - [5.5. 寄送补丁](5.Posting.md#id6)
- [6. 跟进](6.Followthrough.md)
  - [6.1. 与审阅者合作](6.Followthrough.md#id2)
  - [6.2. 接下来会发生什么](6.Followthrough.md#id3)
  - [6.3. 其他可能发生的事情](6.Followthrough.md#id4)
- [7. 高级主题](7.AdvancedTopics.md)
  - [7.1. 使用Git管理补丁](7.AdvancedTopics.md#git)
  - [7.2. 审阅补丁](7.AdvancedTopics.md#id2)
- [8. 更多信息](8.Conclusion.md)
- [9. 结论](8.Conclusion.md#id2)

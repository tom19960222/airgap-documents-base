---
collection: kernel
version: "6.17"
title: "中文翻译"
source_url: https://www.kernel.org/doc/html/v6.17/translations/zh_CN/index.html
fetched_at: 2026-09-16T16:17:52+00:00
---
Chinese (Simplified)

- [English](../../index.md)
- [Chinese (Traditional)](../zh_TW/index.md)
- [Italian](../it_IT/index.md)
- [Japanese](../ja_JP/index.md)
- [Korean](../ko_KR/index.md)
- [Spanish](../sp_SP/index.md)

# 中文翻译

> **Note:**
>
> **翻译计划:**
> 内核中文文档欢迎任何翻译投稿，特别是关于内核用户和管理员指南部分。

这是中文内核文档树的顶级目录。内核文档，就像内核本身一样，在很大程度上是一
项正在进行的工作；当我们努力将许多分散的文件整合成一个连贯的整体时尤其如此。
另外，随时欢迎您对内核文档进行改进；如果您想提供帮助，请加入vger.kernel.org
上的linux-doc邮件列表，并按照Documentation/translations/zh_CN/how-to.rst的
指引提交补丁。提交补丁之前请确保执行”make htmldocs”后无与翻译有关的异常输出。

## 如何翻译内核文档

翻译文档本身是一件很简单的事情，但是提交补丁需要注意一些细节，为了保证内核中文文档的高质量可持续发展，提供了一份翻译指南。

- [Linux 内核中文文档翻译规范](how-to.md)

## 与Linux 内核社区一起工作

与内核开发社区进行协作并将工作推向上游的基本指南。

- [内核开发过程指南](process/development-process.md)
- [提交补丁：如何让你的改动进入内核](process/submitting-patches.md)
- [行为准则](process/code-of-conduct.md)
- [内核维护者手册](maintainer/index.md)
- [完整开发流程文档](process/index.md)

## 内部API文档

开发人员使用的内核内部交互接口手册。

- [核心API文档](core-api/index.md)
- [Linux驱动实现者的API指南](driver-api/index.md)
- [内核子系统文档](subsystem-apis.md)
- [内核中的锁](locking/index.md)

## 开发工具和流程

为所有内核开发人员提供有用信息的各种其他手册。

- [Linux内核许可规则](process/license-rules.md)
- [如何编写内核文档](doc-guide/index.md)
- [内核开发工具](dev-tools/index.md)
- [内核测试指南](dev-tools/testing-overview.md)
- [内核骇客指南](kernel-hacking/index.md)
- [Rust](rust/index.md)

TODOList:

- trace/index
- fault-injection/index
- livepatch/index

## 面向用户的文档

下列手册针对
希望内核在给定系统上以最佳方式工作的\*用户\*，
和查找内核用户空间API信息的程序开发人员。

- [Linux 内核用户和管理员指南](admin-guide/index.md)
- [报告问题](admin-guide/reporting-issues.md)
- [Linux 内核用户空间API指南](userspace-api/index.md)
- [内核构建系统](kbuild/index.md)

TODOList:

- 用户空间工具 <tools/index>

也可参考独立于内核文档的 [Linux 手册页](https://www.kernel.org/doc/man-pages/) 。

## 固件相关文档

下列文档描述了内核需要的平台固件相关信息。

- [Open Firmware 和 Devicetree](devicetree/index.md)
  - [内核Devicetree的使用](devicetree/index.md#devicetree)
  - [Devicetree Overlays](devicetree/index.md#devicetree-overlays)
  - [Devicetree Bindings](devicetree/index.md#devicetree-bindings)

TODOList:

- firmware-guide/index

## 体系结构文档

- [处理器体系结构](arch/index.md)
  - [MIPS特性文档](arch/mips/index.md)
  - [ARM64 架构](arch/arm64/index.md)
  - [RISC-V 体系结构](arch/riscv/index.md)
  - [OpenRISC 体系架构](arch/openrisc/index.md)
  - [PA-RISC体系架构](arch/parisc/index.md)
  - [LoongArch体系结构](arch/loongarch/index.md)

## 其他文档

有几份未分类的文档似乎不适合放在文档的其他部分，或者可能需要进行一些调整和/或
转换为reStructureText格式，也有可能太旧。

- [未分类文档](staging/index.md)
  - [推测执行](staging/speculation.md)
  - [Linux中的XZ数据压缩](staging/xz.md)

## 术语表

- [术语表](glossary.md)

## 索引和表格

- [Index](../../genindex.md)

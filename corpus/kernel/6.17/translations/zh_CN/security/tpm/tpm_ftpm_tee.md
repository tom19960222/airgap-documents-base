---
collection: kernel
version: "6.17"
title: "固件TPM驱动"
source_url: https://www.kernel.org/doc/html/v6.17/translations/zh_CN/security/tpm/tpm_ftpm_tee.html
fetched_at: 2026-09-16T16:56:23+00:00
---
Chinese (Simplified)

- [English](../../../../security/tpm/tpm_ftpm_tee.md)

> **Note:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请发建议或者补丁给
> 该文件的译者，或者请求中文文档维护者和审阅者的帮助。

Original:
:   [Firmware TPM Driver](../../../../security/tpm/tpm_ftpm_tee.md)

翻译:
:   赵硕 Shuo Zhao <[zhaoshuo@cqsoftware.com.cn](mailto:zhaoshuo%40cqsoftware.com.cn)>

# 固件TPM驱动

本文档描述了固件可信平台模块（fTPM）设备驱动。

## 介绍

该驱动程序是用于ARM的TrustZone环境中实现的固件的适配器。该驱动
程序允许程序以与硬件TPM相同的方式与TPM进行交互。

## 设计

该驱动程序充当一个薄层，传递命令到固件实现的TPM并接收其响应。驱动
程序本身并不包含太多逻辑，更像是固件与内核/用户空间之间的一个管道。

固件本身基于以下论文：
<https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/ftpm1.pdf>

当驱动程序被加载时，它会向用户空间暴露 `/dev/tpmX` 字符设备，允许
用户空间通过该设备与固件TPM进行通信。

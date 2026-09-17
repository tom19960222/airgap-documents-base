---
collection: kernel
version: "6.17"
title: "可信平台模块文档"
source_url: https://www.kernel.org/doc/html/v6.17/translations/zh_CN/security/tpm/index.html
fetched_at: 2026-09-16T16:54:11+00:00
---
Chinese (Simplified)

- [English](../../../../security/tpm/index.md)

> **Note:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请发建议或者补丁给
> 该文件的译者，或者请求中文文档维护者和审阅者的帮助。

Original:
:   [Trusted Platform Module documentation](../../../../security/tpm/index.md)

翻译:
:   赵硕 Shuo Zhao <[zhaoshuo@cqsoftware.com.cn](mailto:zhaoshuo%40cqsoftware.com.cn)>

# 可信平台模块文档

- [TPM事件日志](tpm_event_log.md)
  - [介绍](tpm_event_log.md#id1)
  - [UEFI事件日志](tpm_event_log.md#uefi)
  - [参考文献](tpm_event_log.md#id2)
- [TPM安全](tpm-security.md)
  - [介绍](tpm-security.md#id1)
  - [总线上的窥探和篡改攻击](tpm-security.md#id2)
  - [测量（PCR）完整性](tpm-security.md#pcr)
  - [秘密保护](tpm-security.md#id3)
  - [与TPM建立初始信任](tpm-security.md#id4)
  - [信任堆叠](tpm-security.md#id5)
  - [会话属性](tpm-security.md#id6)
  - [保护类型](tpm-security.md#id7)
- [空主密钥认证在用户空间的实现](tpm-security.md#id8)
- [TPM FIFO接口驱动](tpm_tis.md)
- [参考文献](tpm_tis.md#id1)
- [Linux容器的虚拟TPM代理驱动](tpm_vtpm_proxy.md)
  - [介绍](tpm_vtpm_proxy.md#id1)
  - [设计](tpm_vtpm_proxy.md#id2)
  - [UAPI](tpm_vtpm_proxy.md#uapi)
- [Xen的虚拟TPM接口](xen-tpmfront.md)
  - [介绍](xen-tpmfront.md#id1)
  - [设计概述](xen-tpmfront.md#id2)
  - [与Xen的集成](xen-tpmfront.md#xen)
- [固件TPM驱动](tpm_ftpm_tee.md)
  - [介绍](tpm_ftpm_tee.md#id1)
  - [设计](tpm_ftpm_tee.md#id2)

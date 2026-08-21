---
collection: kernel
version: "6.8"
title: "ACRN CPUID位域"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/virt/acrn/cpuid.html
fetched_at: 2026-08-21T04:00:42+00:00
---
Chinese (Simplified)

- [English](../../../../virt/acrn/cpuid.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [ACRN CPUID bits](../../../../virt/acrn/cpuid.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

校译
:   时奎亮 Alex Shi <[alexs@kernel.org](mailto:alexs%40kernel.org)>

# ACRN CPUID位域

在ACRN超级管理器上运行的客户虚拟机可以使用CPUID检查其一些功能。

ACRN的cpuid函数是:

函数: 0x40000000

返回:

```
eax = 0x40000010
ebx = 0x4e524341
ecx = 0x4e524341
edx = 0x4e524341
```

注意，ebx，ecx和edx中的这个值对应于字符串“ACRNACRNACRN”。eax中的值对应于这个叶子
中存在的最大cpuid函数，如果将来有更多的函数加入，将被更新。

函数: define ACRN_CPUID_FEATURES (0x40000001)

返回:

```
ebx, ecx, edx
eax = an OR'ed group of (1 << flag)
```

其中 `flag` 的定义如下:

| 标志 | 值 | 描述 |
| --- | --- | --- |
| ACRN_FEATURE_PRIVILEGED_VM | 0 | 客户虚拟机是一个有特权的虚拟机 |

函数: 0x40000010

返回:

```
ebx, ecx, edx
eax = (Virtual) TSC frequency in kHz.
```

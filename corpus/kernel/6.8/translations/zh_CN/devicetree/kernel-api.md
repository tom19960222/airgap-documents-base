---
collection: kernel
version: "6.8"
title: "内核中的设备树API"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/devicetree/kernel-api.html
fetched_at: 2026-08-21T03:58:24+00:00
---
Chinese (Simplified)

- [English](../../../devicetree/kernel-api.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [DeviceTree Kernel API](../../../devicetree/kernel-api.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

校译

# 内核中的设备树API

## 核心函数

该API在以下内核代码中:

drivers/of/base.c

include/linux/of.h

drivers/of/property.c

include/linux/of_graph.h

drivers/of/address.c

drivers/of/irq.c

drivers/of/fdt.c

## 驱动模型函数

该API在以下内核代码中:

include/linux/of_device.h

drivers/of/device.c

include/linux/of_platform.h

drivers/of/platform.c

## 覆盖和动态DT函数

该API在以下内核代码中:

drivers/of/resolver.c

drivers/of/dynamic.c

drivers/of/overlay.c

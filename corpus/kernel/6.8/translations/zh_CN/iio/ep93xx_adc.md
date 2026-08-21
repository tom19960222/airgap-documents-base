---
collection: kernel
version: "6.8"
title: "思睿逻辑 EP93xx 模拟数字转换器驱动"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/iio/ep93xx_adc.html
fetched_at: 2026-08-21T04:00:32+00:00
---
Chinese (Simplified)

- [English](../../../iio/ep93xx_adc.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Cirrus Logic EP93xx ADC driver](../../../iio/ep93xx_adc.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

# 思睿逻辑 EP93xx 模拟数字转换器驱动

## 1. 概述

该驱动同时适用于具有5通道模拟数字转换器的低端 (EP9301, Ep9302) 设备和10通道
触摸屏/模拟数字转换器的高端设备(EP9307, EP9312, EP9315)。

## 2. 通道编号

EP9301和EP9302数据表定义了通道0..4的编号方案。虽然EP9307, EP9312和EP9315多
了3个通道（一共8个），但是编号并没有定义。所以说最后三个通道是随机编号的。

如果ep93xx_adc是IIO设备0，您将在以下位置找到条目
/sys/bus/iio/devices/iio:device0/:

> | sysfs 入口 | ball/pin 名称 |
> | --- | --- |
> | in_voltage0_raw | YM |
> | in_voltage1_raw | SXP |
> | in_voltage2_raw | SXM |
> | in_voltage3_raw | SYP |
> | in_voltage4_raw | SYM |
> | in_voltage5_raw | XP |
> | in_voltage6_raw | XM |
> | in_voltage7_raw | YP |

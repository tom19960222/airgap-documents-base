---
collection: kernel
version: "6.8"
title: "通用型输入/输出（GPIO）"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/driver-api/gpio/index.html
fetched_at: 2026-08-21T03:46:24+00:00
---
Chinese (Simplified)

- [English](../../../../driver-api/gpio/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [General Purpose Input/Output (GPIO)](../../../../driver-api/gpio/index.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

校译

# 通用型输入/输出（GPIO）

目录

- [传统GPIO接口](legacy.md)
- [什么是GPIO？](legacy.md#id1)
- [GPIO 公约](legacy.md#id2)
  - [标识 GPIO](legacy.md#id3)
  - [使用 GPIO](legacy.md#id4)
  - [访问自旋锁安全的 GPIO](legacy.md#id5)
  - [访问可能休眠的 GPIO](legacy.md#id6)
  - [声明和释放 GPIO](legacy.md#id7)
  - [GPIO 映射到 IRQ](legacy.md#gpio-irq)
  - [模拟开漏信号](legacy.md#id8)
  - [GPIO控制器和引脚控制子系统](legacy.md#id9)
- [这些公约忽略了什么？](legacy.md#id10)
- [GPIO 实现者的框架（可选）](legacy.md#id11)
  - [控制器驱动: gpio_chip](legacy.md#gpio-chip)
  - [平台支持](legacy.md#id12)
  - [板级支持](legacy.md#id13)
- [用户空间的 Sysfs 接口（可选）](legacy.md#sysfs)
  - [Sysfs 中的路径](legacy.md#id14)
- [API参考](legacy.md#api)

Todolist:

- intro
- using-gpio
- driver
- consumer
- board
- drivers-on-gpio
- bt8xxgpio

## 核心

该API在以下内核代码中:

include/linux/gpio/driver.h

drivers/gpio/gpiolib.c

## ACPI支持

该API在以下内核代码中:

drivers/gpio/gpiolib-acpi.c

## 设备树支持

该API在以下内核代码中:

drivers/gpio/gpiolib-of.c

## 设备管理支持

该API在以下内核代码中:

drivers/gpio/gpiolib-devres.c

## sysfs帮助（函数）

该API在以下内核代码中:

drivers/gpio/gpiolib-sysfs.c

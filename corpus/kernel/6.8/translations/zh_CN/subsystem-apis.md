---
collection: kernel
version: "6.8"
title: "内核子系统文档"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/subsystem-apis.html
fetched_at: 2026-08-21T03:33:13+00:00
---
Chinese (Simplified)

- [English](../../subsystem-apis.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Kernel subsystem documentation](../../subsystem-apis.md)

翻译
:   唐艺舟 Tang Yizhou <[tangyeechou@gmail.com](mailto:tangyeechou%40gmail.com)>

# 内核子系统文档

这些书籍从内核开发者的角度，详细介绍了特定内核子系统
的如何工作。这里的大部分信息直接取自内核源代码，并
根据需要添加了补充材料（或者至少是我们设法添加的 - 可
能 *不是* 所有的材料都有需要）。

## 核心子系统

- [核心API文档](core-api/index.md)
- [Linux驱动实现者的API指南](driver-api/index.md)
- [Linux内存管理文档](mm/index.md)
- [电源管理](power/index.md)
- [Linux调度器](scheduler/index.md)
- [锁](locking/index.md)

TODOList:

- timers/index

## 人机接口

- [Linux 声音子系统文档](sound/index.md)

TODOList:

- input/index
- hid/index
- gpu/index
- fb/index

## 网络接口

- [infiniband](infiniband/index.md)

TODOList:

- networking/index
- netlabel/index
- isdn/index
- mhi/index

## 存储接口

- [Linux Kernel中的文件系统](filesystems/index.md)

TODOList:

- block/index
- cdrom/index
- scsi/index
- target/index

**Fixme**: 这里还需要更多的分类组织工作。

- [计数](accounting/index.md)
- [Linux CPUFreq - Linux(TM)内核中的CPU频率和电压升降代码](cpu-freq/index.md)
- [工业 I/O](iio/index.md)
- [Linux虚拟化支持](virt/index.md)
- [Linux PCI总线子系统](PCI/index.md)
- [Linux PECI 子系统](peci/index.md)

TODOList:

- fpga/index
- i2c/index
- leds/index
- pcmcia/index
- spi/index
- w1/index
- watchdog/index
- hwmon/index
- accel/index
- security/index
- crypto/index
- bpf/index
- usb/index
- misc-devices/index
- wmi/index

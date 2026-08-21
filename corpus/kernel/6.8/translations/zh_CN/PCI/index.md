---
collection: kernel
version: "6.8"
title: "Linux PCI总线子系统"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/PCI/index.html
fetched_at: 2026-08-21T03:54:11+00:00
---
Chinese (Simplified)

- [English](../../../PCI/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [PCI Bus Subsystem](../../../PCI/index.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

校译

# Linux PCI总线子系统

- [1. 如何写Linux PCI驱动](pci.md)
  - [1.1. PCI驱动的结构体](pci.md#pci)
  - [1.2. 调用pci_register_driver()](pci.md#pci-register-driver)
  - [1.3. 如何手动搜索PCI设备](pci.md#id2)
  - [1.4. 设备初始化步骤](pci.md#id3)
  - [1.5. PCI设备关闭](pci.md#id7)
  - [1.6. 如何访问PCI配置空间](pci.md#id14)
  - [1.7. 其它有趣的函数](pci.md#id15)
  - [1.8. 杂项提示](pci.md#id16)
  - [1.9. 供应商和设备标识](pci.md#id17)
  - [1.10. 过时的函数](pci.md#id18)
  - [1.11. MMIO空间和“写通知”](pci.md#mmio)
- [2. PCI Express端口总线驱动指南](pciebus-howto.md)
  - [2.1. 关于本指南](pciebus-howto.md#id1)
  - [2.2. 什么是PCI Express端口总线驱动程序](pciebus-howto.md#id2)
  - [2.3. 为什么要使用PCI Express端口总线驱动程序？](pciebus-howto.md#id3)
  - [2.4. 配置PCI Express端口总线驱动程序与服务驱动程序](pciebus-howto.md#id4)
  - [2.5. 可能的资源冲突](pciebus-howto.md#id8)
- [3. PCI Express I/O 虚拟化指南](pci-iov-howto.md)
  - [3.1. 概述](pci-iov-howto.md#id1)
  - [3.2. 使用指南](pci-iov-howto.md#id2)
  - [3.3. 开发者指南](pci-iov-howto.md#id5)
- [4. MSI驱动指南](msi-howto.md)
  - [4.1. 关于本指南](msi-howto.md#id1)
  - [4.2. 什么是MSI?](msi-howto.md#id2)
  - [4.3. 为什么用MSI?](msi-howto.md#id3)
  - [4.4. 如何使用MSI](msi-howto.md#id4)
  - [4.5. MSI特性](msi-howto.md#id9)
  - [4.6. MSI(-X) APIs设备驱动程序列表](msi-howto.md#msi-x-apis)
- [5. 通过sysfs访问PCI设备资源](sysfs-pci.md)
  - [5.1. 通过sysfs访问原有资源](sysfs-pci.md#sysfs)
  - [5.2. 支持新平台上的PCI访问](sysfs-pci.md#pci)
- [6. PCI主桥的ACPI注意事项](acpi-info.md)

Todolist:

- pci-error-recovery
- pcieaer-howto
- endpoint/index
- boot-interrupts

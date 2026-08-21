---
collection: kernel
version: "6.8"
title: "Linux驱动实现者的API指南"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/driver-api/index.html
fetched_at: 2026-08-21T03:31:30+00:00
---
Chinese (Simplified)

- [English](../../../driver-api/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [Driver implementer's API guide](../../../driver-api/index.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

校译

# Linux驱动实现者的API指南

内核提供了各种各样的接口来支持设备驱动的开发。这份文档只是对其中一些接口进行了
一定程度的整理——希望随着时间的推移，它能变得更好！可用的小节可以在下面看到。

目录列表

- [通用型输入/输出（GPIO）](gpio/index.md)
  - [传统GPIO接口](gpio/legacy.md)
  - [什么是GPIO？](gpio/legacy.md#id1)
  - [GPIO 公约](gpio/legacy.md#id2)
  - [这些公约忽略了什么？](gpio/legacy.md#id10)
  - [GPIO 实现者的框架（可选）](gpio/legacy.md#id11)
  - [用户空间的 Sysfs 接口（可选）](gpio/legacy.md#sysfs)
  - [API参考](gpio/legacy.md#api)
  - [核心](gpio/index.md#id1)
  - [ACPI支持](gpio/index.md#acpi)
  - [设备树支持](gpio/index.md#id2)
  - [设备管理支持](gpio/index.md#id3)
  - [sysfs帮助（函数）](gpio/index.md#sysfs)
- [对内存映射地址的I/O写入排序](io_ordering.md)

Todolist:

- driver-model/index
- basics
- infrastructure
- ioctl
- early-userspace/index
- pm/index
- clk
- device-io
- dma-buf
- device_link
- component
- message-based
- infiniband
- aperture
- frame-buffer
- regulator
- reset
- iio/index
- input
- usb/index
- firewire
- pci/index
- cxl/index
- spi
- i2c
- ipmb
- ipmi
- i3c/index
- interconnect
- devfreq
- hsi
- edac
- scsi
- libata
- target
- mailbox
- mtdnand
- miscellaneous
- mei/index
- mtd/index
- mmc/index
- nvdimm/index
- w1
- rapidio/index
- s390-drivers
- vme
- 80211/index
- uio-howto
- firmware/index
- pin-control
- md/index
- media/index
- misc_devices
- nfc/index
- dmaengine/index
- slimbus
- soundwire/index
- thermal/index
- fpga/index
- acpi/index
- auxiliary_bus
- backlight/lp855x-driver.rst
- connector
- console
- dcdbas
- eisa
- isa
- isapnp
- io-mapping
- generic-counter
- memory-devices/index
- men-chameleon-bus
- ntb
- nvmem
- parport-lowlevel
- pps
- ptp
- phy/index
- pwm
- pldmfw/index
- rfkill
- serial/index
- sm501
- surface_aggregator/index
- switchtec
- sync_file
- tty/index
- vfio-mediated-device
- vfio
- vfio-pci-device-specific-driver-acceptance
- xilinx/index
- xillybus
- zorro
- hte/index

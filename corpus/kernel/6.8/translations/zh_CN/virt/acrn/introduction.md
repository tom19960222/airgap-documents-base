---
collection: kernel
version: "6.8"
title: "ACRN超级管理器介绍"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/virt/acrn/introduction.html
fetched_at: 2026-08-21T04:00:40+00:00
---
Chinese (Simplified)

- [English](../../../../virt/acrn/introduction.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [ACRN Hypervisor Introduction](../../../../virt/acrn/introduction.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

校译
:   时奎亮 Alex Shi <[alexs@kernel.org](mailto:alexs%40kernel.org)>

# ACRN超级管理器介绍

ACRN超级管理器是一个第一类超级管理器，直接在裸机硬件上运行。它有一个特权管理虚拟机，称为服
务虚拟机，用于管理用户虚拟机和进行I/O仿真。

ACRN用户空间是一个运行在服务虚拟机中的应用程序，它根据命令行配置为用户虚拟机仿真设备。
ACRN管理程序服务模块（HSM）是服务虚拟机中的一个内核模块，为ACRN用户空间提供管理程序服
务。

下图展示了该架构。

```
              服务端VM                      用户端VM
    +----------------------------+  |  +------------------+
    |        +--------------+    |  |  |                  |
    |        |ACRN用户空间  |    |  |  |                  |
    |        +--------------+    |  |  |                  |
    |-----------------ioctl------|  |  |                  |   ...
    |内核空间       +----------+ |  |  |                  |
    |               |   HSM    | |  |  | 驱动             |
    |               +----------+ |  |  |                  |
    +--------------------|-------+  |  +------------------+
+---------------------hypercall----------------------------------------+
|                         ACRN超级管理器                               |
+----------------------------------------------------------------------+
|                          硬件                                        |
+----------------------------------------------------------------------+
```

ACRN用户空间为用户虚拟机分配内存，配置和初始化用户虚拟机使用的设备，加载虚拟引导程序，
初始化虚拟CPU状态，处理来自用户虚拟机的I/O请求访问。它使用ioctls来与HSM通信。HSM通过
与ACRN超级管理器的hypercalls进行交互来实现管理服务。HSM向用户空间输出一个char设备接口
（/dev/acrn_hsm）。

ACRN超级管理器是开源的，任何人都可以贡献。源码库在
<https://github.com/projectacrn/acrn-hypervisor>。

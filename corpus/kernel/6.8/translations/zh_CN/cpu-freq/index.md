---
collection: kernel
version: "6.8"
title: "Linux CPUFreq - Linux(TM)内核中的CPU频率和电压升降代码"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/cpu-freq/index.html
fetched_at: 2026-08-21T03:51:04+00:00
---
Chinese (Simplified)

- [English](../../../cpu-freq/index.md)
- [Chinese (Traditional)](../../zh_TW/cpu-freq/index.md)

> **Warning:**
>
> 此文件的目的是为让中文读者更容易阅读和理解，而不是作为一个分支。 因此，
> 如果您对此文件有任何意见或更新，请先尝试更新原始英文文件。

> **Note:**
>
> 如果您发现本文档与原始文件有任何不同或者有翻译问题，请联系该文件的译者，
> 或者请求时奎亮的帮助：<[alexs@kernel.org](mailto:alexs%40kernel.org)>。

Original
:   [CPUFreq - CPU frequency and voltage scaling code in the Linux(TM) kernel](../../../cpu-freq/index.md)

翻译
:   司延腾 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

# Linux CPUFreq - Linux(TM)内核中的CPU频率和电压升降代码

Author: Dominik Brodowski <[linux@brodo.de](mailto:linux%40brodo.de)>

> 时钟升降允许你在运行中改变CPU的时钟速度。这是一个很好的节省电池电量的方法，因为时
> 钟速度越低，CPU消耗的电量越少。

- [CPUFreq核心和CPUFreq通知器的通用说明](core.md)
- [如何实现一个新的CPUFreq处理器驱动程序？](cpu-drivers.md)
- [sysfs CPUFreq Stats的一般说明](cpufreq-stats.md)

## 邮件列表

这里有一个 CPU 频率变化的 CVS 提交和通用列表，您可以在这里报告bug、问题或提交补丁。要发
布消息，请发送电子邮件到 [linux-pm@vger.kernel.org](mailto:linux-pm%40vger.kernel.org)。

## 链接

FTP档案:
\* <ftp://ftp.linux.org.uk/pub/linux/cpufreq/>

如何访问CVS仓库:
\* <http://cvs.arm.linux.org.uk/>

CPUFreq邮件列表:
\* <http://vger.kernel.org/vger-lists.html#linux-pm>

SA-1100的时钟和电压标度:
\* <http://www.lartmaker.nl/projects/scaling>

---
collection: kernel
version: "6.8"
title: "处理器体系结构"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/arch/index.html
fetched_at: 2026-08-21T03:35:53+00:00
---
Chinese (Simplified)

- [English](../../../arch/index.md)
- [Chinese (Traditional)](../../zh_TW/arch/index.md)

# 处理器体系结构

以下文档提供了具体架构实现的编程细节。

- [MIPS特性文档](mips/index.md)
  - [1. BMIPS设备树引导](mips/booting.md)
  - [2. 君正 JZ47xx SoC定时器/计数器硬件单元](mips/ingenic-tcu.md)
  - [3. Feature status on mips architecture](mips/features.md)
- [ARM64 架构](arm64/index.md)
  - [AArch64 Linux 中扩展的活动监控单元](arm64/amu.md)
  - [ARM64中的 HugeTLBpage](arm64/hugetlbpage.md)
  - [Perf 事件属性](arm64/perf.md)
  - [ARM64 ELF hwcaps](arm64/elf_hwcaps.md)
- [RISC-V 体系结构](riscv/index.md)
  - [RISC-V内核启动要求和限制](riscv/boot.md)
  - [RISC-V Linux启动镜像文件头](riscv/boot-image-header.md)
  - [RISC-V Linux上的虚拟内存布局](riscv/vm-layout.md)
  - [arch/riscv 开发者维护指南](riscv/patch-acceptance.md)
- [OpenRISC 体系架构](openrisc/index.md)
  - [OpenRISC Linux](openrisc/openrisc_port.md)
  - [待办事项](openrisc/todo.md)
- [PA-RISC体系架构](parisc/index.md)
  - [调试PA-RISC](parisc/debugging.md)
  - [Linux/PA-RISC的寄存器用法](parisc/registers.md)
- [LoongArch体系结构](loongarch/index.md)
  - [1. LoongArch介绍](loongarch/introduction.md)
  - [2. 启动 Linux/LoongArch](loongarch/booting.md)
  - [3. LoongArch的IRQ芯片模型（层级关系）](loongarch/irq-chip-model.md)
  - [4. Feature status on loongarch architecture](loongarch/features.md)

TODOList:

- arm/index
- m68k/index
- nios2/index
- powerpc/index
- s390/index
- sh/index
- sparc/index
- x86/index
- xtensa/index

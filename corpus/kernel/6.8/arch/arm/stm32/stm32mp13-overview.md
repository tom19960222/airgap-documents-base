---
collection: kernel
version: "6.8"
title: "STM32MP13 Overview"
source_url: https://www.kernel.org/doc/html/v6.8/arch/arm/stm32/stm32mp13-overview.html
fetched_at: 2026-08-21T03:37:57+00:00
---
# STM32MP13 Overview

## Introduction

The STM32MP131/STM32MP133/STM32MP135 are Cortex-A MPU aimed at various applications.
They feature:

- One Cortex-A7 application core
- Standard memories interface support
- Standard connectivity, widely inherited from the STM32 MCU family
- Comprehensive security support

More details:

- Cortex-A7 core running up to @900MHz
- FMC controller to connect SDRAM, NOR and NAND memories
- QSPI
- SD/MMC/SDIO support
- 2\*Ethernet controller
- CAN
- ADC/DAC
- USB EHCI/OHCI controllers
- USB OTG
- I2C, SPI, CAN busses support
- Several general purpose timers
- Serial Audio interface
- LCD controller
- DCMIPP
- SPDIFRX
- DFSDM

Authors

- Alexandre Torgue <[alexandre.torgue@foss.st.com](mailto:alexandre.torgue%40foss.st.com)>

---
collection: kernel
version: "6.8"
title: "STM32MP151 Overview"
source_url: https://www.kernel.org/doc/html/v6.8/arch/arm/stm32/stm32mp151-overview.html
fetched_at: 2026-08-21T03:37:57+00:00
---
# STM32MP151 Overview

## Introduction

The STM32MP151 is a Cortex-A MPU aimed at various applications.
It features:

- Single Cortex-A7 application core
- Standard memories interface support
- Standard connectivity, widely inherited from the STM32 MCU family
- Comprehensive security support

More details:

- Cortex-A7 core running up to @800MHz
- FMC controller to connect SDRAM, NOR and NAND memories
- QSPI
- SD/MMC/SDIO support
- Ethernet controller
- ADC/DAC
- USB EHCI/OHCI controllers
- USB OTG
- I2C, SPI busses support
- Several general purpose timers
- Serial Audio interface
- LCD-TFT controller
- DCMIPP
- SPDIFRX
- DFSDM

Authors

- Roan van Dijk <[roan@protonic.nl](mailto:roan%40protonic.nl)>

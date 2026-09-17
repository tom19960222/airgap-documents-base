---
collection: kernel
version: "6.17"
title: "Kernel driver i2c-pca-isa"
source_url: https://www.kernel.org/doc/html/v6.17/i2c/busses/i2c-pca-isa.html
fetched_at: 2026-09-16T16:53:36+00:00
---
# Kernel driver i2c-pca-isa

Supported adapters:

This driver supports ISA boards using the Philips PCA 9564
Parallel bus to I2C bus controller

Author: Ian Campbell <[icampbell@arcom.com](mailto:icampbell%40arcom.com)>, Arcom Control Systems

## Module Parameters

- base int
  :   I/O base address
- irq int
  :   IRQ interrupt
- clock int
  :   Clock rate as described in table 1 of PCA9564 datasheet

## Description

This driver supports ISA boards using the Philips PCA 9564
Parallel bus to I2C bus controller

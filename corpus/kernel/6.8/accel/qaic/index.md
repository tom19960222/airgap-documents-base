---
collection: kernel
version: "6.8"
title: "accel/qaic Qualcomm Cloud AI driver"
source_url: https://www.kernel.org/doc/html/v6.8/accel/qaic/index.html
fetched_at: 2026-08-21T03:53:50+00:00
---
# accel/qaic Qualcomm Cloud AI driver

The accel/qaic driver supports the Qualcomm Cloud AI machine learning
accelerator cards.

- [QAIC driver](qaic.md)
  - [Interrupts](qaic.md#interrupts)
    - [IRQ Storm Mitigation](qaic.md#irq-storm-mitigation)
    - [Single MSI Mode](qaic.md#single-msi-mode)
  - [Neural Network Control (NNC) Protocol](qaic.md#neural-network-control-nnc-protocol)
  - [uAPI](qaic.md#uapi)
  - [Userspace Client Isolation](qaic.md#userspace-client-isolation)
  - [Module parameters](qaic.md#module-parameters)
- [Qualcomm Cloud AI 100 (AIC100)](aic100.md)
  - [Overview](aic100.md#overview)
  - [Hardware Description](aic100.md#hardware-description)
    - [MHI](aic100.md#mhi)
    - [QSM](aic100.md#qsm)
    - [NSP](aic100.md#nsp)
    - [DMA Bridge](aic100.md#dma-bridge)
    - [DDR](aic100.md#ddr)
  - [High-level Use Flow](aic100.md#high-level-use-flow)
  - [Boot Flow](aic100.md#boot-flow)
  - [Userspace components](aic100.md#userspace-components)
    - [Compiler](aic100.md#compiler)
    - [Usermode Driver (UMD)](aic100.md#usermode-driver-umd)
    - [Sahara loader](aic100.md#sahara-loader)
  - [MHI Channels](aic100.md#mhi-channels)
  - [DMA Bridge](aic100.md#id1)
    - [Overview](aic100.md#id2)
    - [Request FIFO](aic100.md#request-fifo)
    - [Response FIFO](aic100.md#response-fifo)
  - [Neural Network Control (NNC) Protocol](aic100.md#neural-network-control-nnc-protocol)
    - [Transaction descriptions](aic100.md#transaction-descriptions)
  - [Subsystem Restart (SSR)](aic100.md#subsystem-restart-ssr)
  - [Reliability, Accessibility, Serviceability (RAS)](aic100.md#reliability-accessibility-serviceability-ras)
  - [Telemetry](aic100.md#telemetry)

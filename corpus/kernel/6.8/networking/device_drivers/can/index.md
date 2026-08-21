---
collection: kernel
version: "6.8"
title: "Controller Area Network (CAN) Device Drivers"
source_url: https://www.kernel.org/doc/html/v6.8/networking/device_drivers/can/index.html
fetched_at: 2026-08-21T03:48:49+00:00
---
# Controller Area Network (CAN) Device Drivers

Device drivers for CAN devices.

Contents:

- [can327: ELM327 driver for Linux SocketCAN](can327.md)
  - [Authors](can327.md#authors)
  - [Motivation](can327.md#motivation)
  - [Introduction](can327.md#introduction)
  - [Data sheet](can327.md#data-sheet)
  - [How to attach the line discipline](can327.md#how-to-attach-the-line-discipline)
  - [How to check the controller version](can327.md#how-to-check-the-controller-version)
  - [Communication example](can327.md#communication-example)
  - [Known limitations of the controller](can327.md#known-limitations-of-the-controller)
  - [Known limitations of the driver](can327.md#known-limitations-of-the-driver)
  - [Rationale behind the chosen configuration](can327.md#rationale-behind-the-chosen-configuration)
  - [A note on CAN bus termination](can327.md#a-note-on-can-bus-termination)
- [CTU CAN FD Driver](ctu/ctucanfd-driver.md)
  - [About CTU CAN FD IP Core](ctu/ctucanfd-driver.md#about-ctu-can-fd-ip-core)
  - [About SocketCAN](ctu/ctucanfd-driver.md#about-socketcan)
  - [Integrating the core to Xilinx Zynq](ctu/ctucanfd-driver.md#integrating-the-core-to-xilinx-zynq)
  - [CTU CAN FD Driver design](ctu/ctucanfd-driver.md#ctu-can-fd-driver-design)
  - [CTU CAN FD Driver Sources Reference](ctu/ctucanfd-driver.md#ctu-can-fd-driver-sources-reference)
  - [CTU CAN FD IP Core and Driver Development Acknowledgment](ctu/ctucanfd-driver.md#ctu-can-fd-ip-core-and-driver-development-acknowledgment)
  - [Notes](ctu/ctucanfd-driver.md#notes)
- [Flexcan CAN Controller driver](freescale/flexcan.md)
  - [On/off RTR frames reception](freescale/flexcan.md#on-off-rtr-frames-reception)

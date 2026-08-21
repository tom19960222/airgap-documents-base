---
collection: kernel
version: "6.8"
title: "Kernel driver i2c-amd756"
source_url: https://www.kernel.org/doc/html/v6.8/i2c/busses/i2c-amd756.html
fetched_at: 2026-08-21T03:43:29+00:00
---
# Kernel driver i2c-amd756

Supported adapters:
:   - AMD 756
    - AMD 766
    - AMD 768
    - AMD 8111

      Datasheets: Publicly available on AMD website
    - nVidia nForce

      Datasheet: Unavailable

Authors:
:   - Frodo Looijaard <[frodol@dds.nl](mailto:frodol%40dds.nl)>,
    - Philip Edelbrock <[phil@netroedge.com](mailto:phil%40netroedge.com)>

## Description

This driver supports the AMD 756, 766, 768 and 8111 Peripheral Bus
Controllers, and the nVidia nForce.

Note that for the 8111, there are two SMBus adapters. The SMBus 1.0 adapter
is supported by this driver, and the SMBus 2.0 adapter is supported by the
i2c-amd8111 driver.

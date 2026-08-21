---
collection: kernel
version: "6.8"
title: "Kernel driver i2c-amd-mp2"
source_url: https://www.kernel.org/doc/html/v6.8/i2c/busses/i2c-amd-mp2.html
fetched_at: 2026-08-21T04:00:30+00:00
---
# Kernel driver i2c-amd-mp2

Supported adapters:
:   - AMD MP2 PCIe interface

Datasheet: not publicly available.

Authors:
:   - Shyam Sundar S K <[Shyam-sundar.S-k@amd.com](mailto:Shyam-sundar.S-k%40amd.com)>
    - Nehal Shah <[nehal-bakulchandra.shah@amd.com](mailto:nehal-bakulchandra.shah%40amd.com)>
    - Elie Morisse <[syniurge@gmail.com](mailto:syniurge%40gmail.com)>

## Description

The MP2 is an ARM processor programmed as an I2C controller and communicating
with the x86 host through PCI.

If you see something like this:

```
03:00.7 MP2 I2C controller: Advanced Micro Devices, Inc. [AMD] Device 15e6
```

in your `lspci -v`, then this driver is for your device.

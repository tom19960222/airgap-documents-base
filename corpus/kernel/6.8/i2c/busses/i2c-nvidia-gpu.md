---
collection: kernel
version: "6.8"
title: "Kernel driver i2c-nvidia-gpu"
source_url: https://www.kernel.org/doc/html/v6.8/i2c/busses/i2c-nvidia-gpu.html
fetched_at: 2026-08-21T03:43:26+00:00
---
# Kernel driver i2c-nvidia-gpu

Datasheet: not publicly available.

Authors:
:   Ajay Gupta <[ajayg@nvidia.com](mailto:ajayg%40nvidia.com)>

## Description

i2c-nvidia-gpu is a driver for I2C controller included in NVIDIA Turing
and later GPUs and it is used to communicate with Type-C controller on GPUs.

If your `lspci -v` listing shows something like the following:

```
01:00.3 Serial bus controller [0c80]: NVIDIA Corporation Device 1ad9 (rev a1)
```

then this driver should support the I2C controller of your GPU.

---
collection: kernel
version: "6.17"
title: "nova NVIDIA GPU drivers"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/nova/index.html
fetched_at: 2026-09-16T16:39:38+00:00
---
# nova NVIDIA GPU drivers

The nova driver project consists out of two separate drivers nova-core and
nova-drm and intends to supersede the nouveau driver for NVIDIA GPUs based on
the GPU System Processor (GSP).

The following documents apply to both nova-core and nova-drm.

- [Guidelines](guidelines.md)

## nova-core

The nova-core driver is the core driver for NVIDIA GPUs based on GSP. nova-core,
as the 1st level driver, provides an abstraction around the GPUs hard- and
firmware interfaces providing a common base for 2nd level drivers, such as the
vGPU manager VFIO driver and the nova-drm driver.

- [Guidelines](core/guidelines.md)
- [Task List](core/todo.md)
- [VBIOS](core/vbios.md)
- [Device Initialization (devinit)](core/devinit.md)
- [FWSEC (Firmware Security)](core/fwsec.md)
- [Falcon (FAst Logic Controller)](core/falcon.md)

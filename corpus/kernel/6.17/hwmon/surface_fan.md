---
collection: kernel
version: "6.17"
title: "Kernel driver surface_fan"
source_url: https://www.kernel.org/doc/html/v6.17/hwmon/surface_fan.html
fetched_at: 2026-09-16T16:34:02+00:00
---
# Kernel driver surface_fan

Supported Devices:

> - Microsoft Surface Pro 9

Author: Ivor Wanders <[ivor@iwanders.net](mailto:ivor%40iwanders.net)>

## Description

This provides monitoring of the fan found in some Microsoft Surface Pro devices,
like the Surface Pro 9. The fan is always controlled by the onboard controller.

## Sysfs interface

| Name | Perm | Description |
| --- | --- | --- |
| `fan1_input` | RO | Current fan speed in RPM. |

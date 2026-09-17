---
collection: kernel
version: "6.17"
title: "octeontx2 devlink support"
source_url: https://www.kernel.org/doc/html/v6.17/crypto/device_drivers/octeontx2.html
fetched_at: 2026-09-16T16:45:59+00:00
---
# octeontx2 devlink support

This document describes the devlink features implemented by the `octeontx2 CPT`
device drivers.

## Parameters

The `octeontx2` driver implements the following driver-specific parameters.

Driver-specific parameters implemented

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Type | Mode | Description |
| `t106_mode` | u8 | runtime | Used to configure CN10KA B0/CN10KB CPT to work as CN10KA A0/A1. |

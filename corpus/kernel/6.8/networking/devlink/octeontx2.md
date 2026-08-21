---
collection: kernel
version: "6.8"
title: "octeontx2 devlink support"
source_url: https://www.kernel.org/doc/html/v6.8/networking/devlink/octeontx2.html
fetched_at: 2026-08-21T04:00:16+00:00
---
# octeontx2 devlink support

This document describes the devlink features implemented by the `octeontx2 AF, PF and VF`
device drivers.

## Parameters

The `octeontx2 PF and VF` drivers implement the following driver-specific parameters.

Driver-specific parameters implemented

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Type | Mode | Description |
| `mcam_count` | u16 | runtime | Select number of match CAM entries to be allocated for an interface. The same is used for ntuple filters of the interface. Supported by PF and VF drivers. |

The `octeontx2 AF` driver implements the following driver-specific parameters.

Driver-specific parameters implemented

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Type | Mode | Description |
| `dwrr_mtu` | u32 | runtime | Use to set the quantum which hardware uses for scheduling among transmit queues. Hardware uses weighted DWRR algorithm to schedule among all transmit queues. |

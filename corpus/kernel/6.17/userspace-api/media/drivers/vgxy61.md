---
collection: kernel
version: "6.17"
title: "12. ST VGXY61 camera sensor driver"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/media/drivers/vgxy61.html
fetched_at: 2026-09-16T16:34:53+00:00
---
# 12. ST VGXY61 camera sensor driver

The ST VGXY61 driver implements the following controls:

## 12.1. `V4L2_CID_HDR_SENSOR_MODE`

> Change the sensor HDR mode. A HDR picture is obtained by merging two
> captures of the same scene using two different exposure periods.

|  |  |
| --- | --- |
| HDR linearize | The merger outputs a long exposure capture as long as it is not saturated. |
| HDR subtraction | This involves subtracting the short exposure frame from the long exposure frame. |
| No HDR | This mode is used for standard dynamic range (SDR) exposures. |

---
collection: kernel
version: "6.8"
title: "10. ST VGXY61 camera sensor driver"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/drivers/st-vgxy61.html
fetched_at: 2026-08-21T03:44:57+00:00
---
# 10. ST VGXY61 camera sensor driver

The ST VGXY61 driver implements the following controls:

## 10.1. `V4L2_CID_HDR_SENSOR_MODE`

> Change the sensor HDR mode. A HDR picture is obtained by merging two
> captures of the same scene using two different exposure periods.

|  |  |
| --- | --- |
| HDR linearize | The merger outputs a long exposure capture as long as it is not saturated. |
| HDR subtraction | This involves subtracting the short exposure frame from the long exposure frame. |
| No HDR | This mode is used for standard dynamic range (SDR) exposures. |

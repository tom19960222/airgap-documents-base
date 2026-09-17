---
collection: kernel
version: "6.17"
title: "2.13.6. V4L2_META_FMT_RPI_FE_CFG"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/media/v4l/metafmt-pisp-fe.html
fetched_at: 2026-09-16T16:55:44+00:00
---
# 2.13.6. V4L2_META_FMT_RPI_FE_CFG

## 2.13.6.1. Raspberry Pi PiSP Front End configuration format

The Raspberry Pi PiSP Front End image signal processor is configured by
userspace by providing a buffer of configuration parameters to the
rp1-cfe-fe-config output video device node using the
[`v4l2_meta_format`](dev-meta.md#c.v4l2_meta_format "v4l2_meta_format") interface.

The [Raspberry Pi PiSP technical specification](https://datasheets.raspberrypi.com/camera/raspberry-pi-image-signal-processor-specification.pdf)
provide detailed description of the Front End configuration and programming
model.

# 2.13.7. V4L2_META_FMT_RPI_FE_STATS

## 2.13.7.1. Raspberry Pi PiSP Front End statistics format

The Raspberry Pi PiSP Front End image signal processor provides statistics data
by writing to a buffer provided via the rp1-cfe-fe-stats capture video device
node using the
[`v4l2_meta_format`](dev-meta.md#c.v4l2_meta_format "v4l2_meta_format") interface.

The [Raspberry Pi PiSP technical specification](https://datasheets.raspberrypi.com/camera/raspberry-pi-image-signal-processor-specification.pdf)
provide detailed description of the Front End configuration and programming
model.

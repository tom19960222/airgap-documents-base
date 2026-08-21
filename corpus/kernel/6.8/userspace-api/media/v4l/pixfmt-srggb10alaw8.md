---
collection: kernel
version: "6.8"
title: "2.6.1.4. V4L2_PIX_FMT_SBGGR10ALAW8 ('aBA8'), V4L2_PIX_FMT_SGBRG10ALAW8 ('aGA8'), V4L2_PIX_FMT_SGRBG10ALAW8 ('agA8'), V4L2_PIX_FMT_SRGGB10ALAW8 ('aRA8'),"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-srggb10alaw8.html
fetched_at: 2026-08-21T03:57:01+00:00
---
# 2.6.1.4. V4L2_PIX_FMT_SBGGR10ALAW8 ('aBA8'), V4L2_PIX_FMT_SGBRG10ALAW8 ('aGA8'), V4L2_PIX_FMT_SGRBG10ALAW8 ('agA8'), V4L2_PIX_FMT_SRGGB10ALAW8 ('aRA8'),

V4L2_PIX_FMT_SGBRG10ALAW8
V4L2_PIX_FMT_SGRBG10ALAW8
V4L2_PIX_FMT_SRGGB10ALAW8
10-bit Bayer formats compressed to 8 bits

## 2.6.1.4.1. Description

These four pixel formats are raw sRGB / Bayer formats with 10 bits per
color compressed to 8 bits each, using the A-LAW algorithm. Each color
component consumes 8 bits of memory. In other respects this format is
similar to [V4L2_PIX_FMT_SRGGB8 ('RGGB'), V4L2_PIX_FMT_SGRBG8 ('GRBG'), V4L2_PIX_FMT_SGBRG8 ('GBRG'), V4L2_PIX_FMT_SBGGR8 ('BA81'),](pixfmt-srggb8.md#v4l2-pix-fmt-srggb8).

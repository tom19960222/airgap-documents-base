---
collection: kernel
version: "6.8"
title: "2.6.1.5. V4L2_PIX_FMT_SBGGR10DPCM8 ('bBA8'), V4L2_PIX_FMT_SGBRG10DPCM8 ('bGA8'), V4L2_PIX_FMT_SGRBG10DPCM8 ('BD10'), V4L2_PIX_FMT_SRGGB10DPCM8 ('bRA8'),"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-srggb10dpcm8.html
fetched_at: 2026-08-21T03:57:01+00:00
---
# 2.6.1.5. V4L2_PIX_FMT_SBGGR10DPCM8 ('bBA8'), V4L2_PIX_FMT_SGBRG10DPCM8 ('bGA8'), V4L2_PIX_FMT_SGRBG10DPCM8 ('BD10'), V4L2_PIX_FMT_SRGGB10DPCM8 ('bRA8'),

*man V4L2_PIX_FMT_SBGGR10DPCM8(2)*

V4L2_PIX_FMT_SGBRG10DPCM8
V4L2_PIX_FMT_SGRBG10DPCM8
V4L2_PIX_FMT_SRGGB10DPCM8
10-bit Bayer formats compressed to 8 bits

## 2.6.1.5.1. Description

These four pixel formats are raw sRGB / Bayer formats with 10 bits per
colour compressed to 8 bits each, using DPCM compression. DPCM,
differential pulse-code modulation, is lossy. Each colour component
consumes 8 bits of memory. In other respects this format is similar to
[V4L2_PIX_FMT_SRGGB10 ('RG10'), V4L2_PIX_FMT_SGRBG10 ('BA10'), V4L2_PIX_FMT_SGBRG10 ('GB10'), V4L2_PIX_FMT_SBGGR10 ('BG10'),](pixfmt-srggb10.md#v4l2-pix-fmt-srggb10).

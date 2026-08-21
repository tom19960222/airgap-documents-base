---
collection: kernel
version: "6.8"
title: "2.7.1.6. V4L2_PIX_FMT_UV8 ('UV8')"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-uv8.html
fetched_at: 2026-08-21T03:57:08+00:00
---
# 2.7.1.6. V4L2_PIX_FMT_UV8 ('UV8')

UV plane interleaved

## 2.7.1.6.1. Description

In this format there is no Y plane, Only CbCr plane. ie (UV interleaved)

**Byte Order.**
Each cell is one byte.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| start + 0: | Cb00 | Cr00 | Cb01 | Cr01 |
| start + 4: | Cb10 | Cr10 | Cb11 | Cr11 |
| start + 8: | Cb20 | Cr20 | Cb21 | Cr21 |
| start + 12: | Cb30 | Cr30 | Cb31 | Cr31 |

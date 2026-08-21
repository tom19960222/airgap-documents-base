---
collection: kernel
version: "6.8"
title: "2.7.1.7. V4L2_PIX_FMT_M420 ('M420')"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-m420.html
fetched_at: 2026-08-21T03:57:09+00:00
---
# 2.7.1.7. V4L2_PIX_FMT_M420 ('M420')

Format with ½ horizontal and vertical chroma resolution, also known as
YUV 4:2:0. Hybrid plane line-interleaved layout.

## 2.7.1.7.1. Description

M420 is a YUV format with ½ horizontal and vertical chroma subsampling
(YUV 4:2:0). Pixels are organized as interleaved luma and chroma planes.
Two lines of luma data are followed by one line of chroma data.

The luma plane has one byte per pixel. The chroma plane contains
interleaved CbCr pixels subsampled by ½ in the horizontal and vertical
directions. Each CbCr pair belongs to four pixels. For example,
Cb0/Cr0 belongs to Y'00, Y'01,
Y'10, Y'11.

All line lengths are identical: if the Y lines include pad bytes so do
the CbCr lines.

**Byte Order.**
Each cell is one byte.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| start + 0: | Y'00 | Y'01 | Y'02 | Y'03 |
| start + 4: | Y'10 | Y'11 | Y'12 | Y'13 |
| start + 8: | Cb00 | Cr00 | Cb01 | Cr01 |
| start + 16: | Y'20 | Y'21 | Y'22 | Y'23 |
| start + 20: | Y'30 | Y'31 | Y'32 | Y'33 |
| start + 24: | Cb10 | Cr10 | Cb11 | Cr11 |

**Color Sample Location:**
Chroma samples are [interstitially sited](yuv-formats.md#yuv-chroma-centered)
horizontally and vertically.

---
collection: kernel
version: "6.8"
title: "2.6.1.7. V4L2_PIX_FMT_SRGGB12 ('RG12'), V4L2_PIX_FMT_SGRBG12 ('BA12'), V4L2_PIX_FMT_SGBRG12 ('GB12'), V4L2_PIX_FMT_SBGGR12 ('BG12'),"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-srggb12.html
fetched_at: 2026-08-21T03:57:02+00:00
---
# 2.6.1.7. V4L2_PIX_FMT_SRGGB12 ('RG12'), V4L2_PIX_FMT_SGRBG12 ('BA12'), V4L2_PIX_FMT_SGBRG12 ('GB12'), V4L2_PIX_FMT_SBGGR12 ('BG12'),

V4L2_PIX_FMT_SGRBG12
V4L2_PIX_FMT_SGBRG12
V4L2_PIX_FMT_SBGGR12
12-bit Bayer formats expanded to 16 bits

## 2.6.1.7.1. Description

These four pixel formats are raw sRGB / Bayer formats with 12 bits per
colour. Each colour component is stored in a 16-bit word, with 4 unused
high bits filled with zeros. Each n-pixel row contains n/2 green samples
and n/2 blue or red samples, with alternating red and blue rows. Bytes
are stored in memory in little endian order. They are conventionally
described as GRGR... BGBG..., RGRG... GBGB..., etc. Below is an example
of a small V4L2_PIX_FMT_SBGGR12 image:

**Byte Order.**
Each cell is one byte, the 4 most significant bits in the high bytes are
0.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| start + 0: | B00low | B00high | G01low | G01high | B02low | B02high | G03low | G03high |
| start + 8: | G10low | G10high | R11low | R11high | G12low | G12high | R13low | R13high |
| start + 16: | B20low | B20high | G21low | G21high | B22low | B22high | G23low | G23high |
| start + 24: | G30low | G30high | R31low | R31high | G32low | G32high | R33low | R33high |

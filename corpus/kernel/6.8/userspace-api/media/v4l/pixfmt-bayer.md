---
collection: kernel
version: "6.8"
title: "2.6. Raw Bayer Formats"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-bayer.html
fetched_at: 2026-08-21T03:56:59+00:00
---
# 2.6. Raw Bayer Formats

## 2.6.1. Description

The raw Bayer formats are used by image sensors before much if any processing is
performed on the image. The formats contain green, red and blue components, with
alternating lines of red and green, and blue and green pixels in different
orders. See also [the Wikipedia article on Bayer filter](https://en.wikipedia.org/wiki/Bayer_filter).

- [2.6.1.1. V4L2_PIX_FMT_SRGGB8 ('RGGB'), V4L2_PIX_FMT_SGRBG8 ('GRBG'), V4L2_PIX_FMT_SGBRG8 ('GBRG'), V4L2_PIX_FMT_SBGGR8 ('BA81'),](pixfmt-srggb8.md)
- [2.6.1.2. V4L2_PIX_FMT_SRGGB10 ('RG10'), V4L2_PIX_FMT_SGRBG10 ('BA10'), V4L2_PIX_FMT_SGBRG10 ('GB10'), V4L2_PIX_FMT_SBGGR10 ('BG10'),](pixfmt-srggb10.md)
- [2.6.1.3. V4L2_PIX_FMT_SRGGB10P ('pRAA'), V4L2_PIX_FMT_SGRBG10P ('pgAA'), V4L2_PIX_FMT_SGBRG10P ('pGAA'), V4L2_PIX_FMT_SBGGR10P ('pBAA'),](pixfmt-srggb10p.md)
- [2.6.1.4. V4L2_PIX_FMT_SBGGR10ALAW8 ('aBA8'), V4L2_PIX_FMT_SGBRG10ALAW8 ('aGA8'), V4L2_PIX_FMT_SGRBG10ALAW8 ('agA8'), V4L2_PIX_FMT_SRGGB10ALAW8 ('aRA8'),](pixfmt-srggb10alaw8.md)
- [2.6.1.5. V4L2_PIX_FMT_SBGGR10DPCM8 ('bBA8'), V4L2_PIX_FMT_SGBRG10DPCM8 ('bGA8'), V4L2_PIX_FMT_SGRBG10DPCM8 ('BD10'), V4L2_PIX_FMT_SRGGB10DPCM8 ('bRA8'),](pixfmt-srggb10dpcm8.md)
- [2.6.1.6. V4L2_PIX_FMT_IPU3_SBGGR10 ('ip3b'), V4L2_PIX_FMT_IPU3_SGBRG10 ('ip3g'), V4L2_PIX_FMT_IPU3_SGRBG10 ('ip3G'), V4L2_PIX_FMT_IPU3_SRGGB10 ('ip3r')](pixfmt-srggb10-ipu3.md)
- [2.6.1.7. V4L2_PIX_FMT_SRGGB12 ('RG12'), V4L2_PIX_FMT_SGRBG12 ('BA12'), V4L2_PIX_FMT_SGBRG12 ('GB12'), V4L2_PIX_FMT_SBGGR12 ('BG12'),](pixfmt-srggb12.md)
- [2.6.1.8. V4L2_PIX_FMT_SRGGB12P ('pRCC'), V4L2_PIX_FMT_SGRBG12P ('pgCC'), V4L2_PIX_FMT_SGBRG12P ('pGCC'), V4L2_PIX_FMT_SBGGR12P ('pBCC'),](pixfmt-srggb12p.md)
- [2.6.1.9. V4L2_PIX_FMT_SRGGB14 ('RG14'), V4L2_PIX_FMT_SGRBG14 ('GR14'), V4L2_PIX_FMT_SGBRG14 ('GB14'), V4L2_PIX_FMT_SBGGR14 ('BG14'),](pixfmt-srggb14.md)
- [2.6.1.10. V4L2_PIX_FMT_SRGGB14P ('pREE'), V4L2_PIX_FMT_SGRBG14P ('pgEE'), V4L2_PIX_FMT_SGBRG14P ('pGEE'), V4L2_PIX_FMT_SBGGR14P ('pBEE'),](pixfmt-srggb14p.md)
- [2.6.1.11. V4L2_PIX_FMT_SRGGB16 ('RG16'), V4L2_PIX_FMT_SGRBG16 ('GR16'), V4L2_PIX_FMT_SGBRG16 ('GB16'), V4L2_PIX_FMT_SBGGR16 ('BYR2'),](pixfmt-srggb16.md)

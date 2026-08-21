---
collection: kernel
version: "6.8"
title: "2. Image Formats"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt.html
fetched_at: 2026-08-21T03:56:56+00:00
---
# 2. Image Formats

The V4L2 API was primarily designed for devices exchanging image data
with applications. The struct [`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format") and
struct [`v4l2_pix_format_mplane`](pixfmt-v4l2-mplane.md#c.v4l2_pix_format_mplane "v4l2_pix_format_mplane") structures define the
format and layout of an image in memory. The former is used with the
single-planar API, while the latter is used with the multi-planar
version (see [Single- and multi-planar APIs](planar-apis.md#planar-apis)). Image formats are negotiated with
the [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl. (The explanations here
focus on video capturing and output, for overlay frame buffer formats
see also [VIDIOC_G_FBUF](vidioc-g-fbuf.md#vidioc-g-fbuf).)

- [2.1. Single-planar format structure](pixfmt-v4l2.md)
- [2.2. Multi-planar format structures](pixfmt-v4l2-mplane.md)
- [2.3. Standard Image Formats](pixfmt-intro.md)
- [2.4. Indexed Format](pixfmt-indexed.md)
- [2.5. RGB Formats](pixfmt-rgb.md)
- [2.6. Raw Bayer Formats](pixfmt-bayer.md)
- [2.7. YUV Formats](yuv-formats.md)
- [2.8. HSV Formats](hsv-formats.md)
- [2.9. Depth Formats](depth-formats.md)
- [2.10. Compressed Formats](pixfmt-compressed.md)
- [2.11. SDR Formats](sdr-formats.md)
- [2.12. Touch Formats](tch-formats.md)
- [2.13. Metadata Formats](meta-formats.md)
- [2.14. Reserved Format Identifiers](pixfmt-reserved.md)
- [2.15. Colorspaces](colorspaces.md)
- [2.16. Defining Colorspaces in V4L2](colorspaces-defs.md)
- [2.17. Detailed Colorspace Descriptions](colorspaces-details.md)
- [2.18. Detailed Transfer Function Descriptions](colorspaces-details.md#detailed-transfer-function-descriptions)

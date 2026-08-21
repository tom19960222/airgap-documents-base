---
collection: kernel
version: "6.8"
title: "2.2. Multi-planar format structures"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-v4l2-mplane.html
fetched_at: 2026-08-21T03:41:19+00:00
---
# 2.2. Multi-planar format structures

The struct [`v4l2_plane_pix_format`](pixfmt-v4l2-mplane.md#c.v4l2_plane_pix_format "v4l2_plane_pix_format") structures define size
and layout for each of the planes in a multi-planar format. The
struct [`v4l2_pix_format_mplane`](pixfmt-v4l2-mplane.md#c.v4l2_pix_format_mplane "v4l2_pix_format_mplane") structure contains
information common to all planes (such as image width and height) and an
array of struct [`v4l2_plane_pix_format`](pixfmt-v4l2-mplane.md#c.v4l2_plane_pix_format "v4l2_plane_pix_format") structures,
describing all planes of that format.

type v4l2_plane_pix_format

struct v4l2_plane_pix_format

|  |  |  |
| --- | --- | --- |
| __u32 | `sizeimage` | Maximum size in bytes required for image data in this plane, set by the driver. When the image consists of variable length compressed data this is the number of bytes required by the codec to support the worst-case compression scenario.  The driver will set the value for uncompressed images.  Clients are allowed to set the sizeimage field for variable length compressed data flagged with `V4L2_FMT_FLAG_COMPRESSED` at [ioctl VIDIOC_ENUM_FMT](vidioc-enum-fmt.md#vidioc-enum-fmt), but the driver may ignore it and set the value itself, or it may modify the provided value based on alignment requirements or minimum/maximum size requirements. If the client wants to leave this to the driver, then it should set sizeimage to 0. |
| __u32 | `bytesperline` | Distance in bytes between the leftmost pixels in two adjacent lines. See struct [`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format"). |
| __u16 | `reserved[6]` | Reserved for future extensions. Should be zeroed by drivers and applications. |

type v4l2_pix_format_mplane

struct v4l2_pix_format_mplane

|  |  |  |
| --- | --- | --- |
| __u32 | `width` | Image width in pixels. See struct [`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format"). |
| __u32 | `height` | Image height in pixels. See struct [`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format"). |
| __u32 | `pixelformat` | The pixel format. Both single- and multi-planar four character codes can be used. |
| __u32 | `field` | Field order, from enum [`v4l2_field`](field-order.md#c.v4l2_field "v4l2_field"). See struct [`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format"). |
| __u32 | `colorspace` | Colorspace encoding, from enum [`v4l2_colorspace`](colorspaces-defs.md#c.v4l2_colorspace "v4l2_colorspace"). See struct [`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format"). |
| struct [`v4l2_plane_pix_format`](pixfmt-v4l2-mplane.md#c.v4l2_plane_pix_format "v4l2_plane_pix_format") | `plane_fmt[VIDEO_MAX_PLANES]` | An array of structures describing format of each plane this pixel format consists of. The number of valid entries in this array has to be put in the `num_planes` field. |
| __u8 | `num_planes` | Number of planes (i.e. separate memory buffers) for this format and the number of valid entries in the `plane_fmt` array. |
| __u8 | `flags` | Flags set by the application or driver, see [Format Flags](pixfmt-v4l2.md#format-flags). |
| union { | (anonymous) | |
| __u8 | `ycbcr_enc` | Y'CbCr encoding, from enum [`v4l2_ycbcr_encoding`](colorspaces-defs.md#c.v4l2_ycbcr_encoding "v4l2_ycbcr_encoding"). See struct [`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format"). |
| __u8 | `hsv_enc` | HSV encoding, from enum [`v4l2_hsv_encoding`](colorspaces-defs.md#c.v4l2_hsv_encoding "v4l2_hsv_encoding"). See struct [`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format"). |
| } |  | |
| __u8 | `quantization` | Quantization range, from enum [`v4l2_quantization`](colorspaces-defs.md#c.v4l2_quantization "v4l2_quantization"). See struct [`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format"). |
| __u8 | `xfer_func` | Transfer function, from enum [`v4l2_xfer_func`](colorspaces-defs.md#c.v4l2_xfer_func "v4l2_xfer_func"). See struct [`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format"). |
| __u8 | `reserved[7]` | Reserved for future extensions. Should be zeroed by drivers and applications. |

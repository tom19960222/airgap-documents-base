---
collection: kernel
version: "6.8"
title: "4.14. Metadata Interface"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/dev-meta.html
fetched_at: 2026-08-21T03:41:18+00:00
---
# 4.14. Metadata Interface

Metadata refers to any non-image data that supplements video frames with
additional information. This may include statistics computed over the image,
frame capture parameters supplied by the image source or device specific
parameters for specifying how the device processes images. This interface is
intended for transfer of metadata between the userspace and the hardware and
control of that operation.

The metadata interface is implemented on video device nodes. The device can be
dedicated to metadata or can support both video and metadata as specified in its
reported capabilities.

## 4.14.1. Querying Capabilities

Device nodes supporting the metadata capture interface set the
`V4L2_CAP_META_CAPTURE` flag in the `device_caps` field of the
`v4l2_capability` structure returned by the `VIDIOC_QUERYCAP()`
ioctl. That flag means the device can capture metadata to memory. Similarly,
device nodes supporting metadata output interface set the
`V4L2_CAP_META_OUTPUT` flag in the `device_caps` field of
`v4l2_capability` structure. That flag means the device can read
metadata from memory.

At least one of the read/write or streaming I/O methods must be supported.

## 4.14.2. Data Format Negotiation

The metadata device uses the [Data Formats](format.md#format) ioctls to select the capture format.
The metadata buffer content format is bound to that selected format. In addition
to the basic [Data Formats](format.md#format) ioctls, the `VIDIOC_ENUM_FMT()` ioctl must be
supported as well.

To use the [Data Formats](format.md#format) ioctls applications set the `type` field of the
`v4l2_format` structure to `V4L2_BUF_TYPE_META_CAPTURE` or to
`V4L2_BUF_TYPE_META_OUTPUT` and use the [`v4l2_meta_format`](dev-meta.md#c.v4l2_meta_format "v4l2_meta_format") `meta`
member of the `fmt` union as needed per the desired operation. Both drivers
and applications must set the remainder of the `v4l2_format` structure
to 0.

type v4l2_meta_format

struct v4l2_meta_format

|  |  |  |
| --- | --- | --- |
| __u32 | `dataformat` | The data format, set by the application. This is a little endian [four character code](vidioc-enum-fmt.md#v4l2-fourcc). V4L2 defines metadata formats in [Metadata Formats](meta-formats.md#meta-formats). |
| __u32 | `buffersize` | Maximum buffer size in bytes required for data. The value is set by the driver. |

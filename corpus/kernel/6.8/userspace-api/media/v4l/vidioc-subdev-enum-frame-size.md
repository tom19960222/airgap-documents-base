---
collection: kernel
version: "6.8"
title: "7.56. ioctl VIDIOC_SUBDEV_ENUM_FRAME_SIZE"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-subdev-enum-frame-size.html
fetched_at: 2026-08-21T03:40:55+00:00
---
# 7.56. ioctl VIDIOC_SUBDEV_ENUM_FRAME_SIZE

## 7.56.1. Name

VIDIOC_SUBDEV_ENUM_FRAME_SIZE - Enumerate media bus frame sizes

## 7.56.2. Synopsis

VIDIOC_SUBDEV_ENUM_FRAME_SIZE

`int ioctl(int fd, VIDIOC_SUBDEV_ENUM_FRAME_SIZE, struct v4l2_subdev_frame_size_enum * argp)`

## 7.56.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_subdev_frame_size_enum`](vidioc-subdev-enum-frame-size.md#c.V4L.v4l2_subdev_frame_size_enum "v4l2_subdev_frame_size_enum").

## 7.56.4. Description

This ioctl allows applications to access the enumeration of frame sizes
supported by a sub-device on the specified pad
for the specified media bus format.
Supported formats can be retrieved with the
[ioctl VIDIOC_SUBDEV_ENUM_MBUS_CODE](vidioc-subdev-enum-mbus-code.md#vidioc-subdev-enum-mbus-code)
ioctl.

The enumerations are defined by the driver, and indexed using the `index` field
of the struct [`v4l2_subdev_frame_size_enum`](vidioc-subdev-enum-frame-size.md#c.V4L.v4l2_subdev_frame_size_enum "v4l2_subdev_frame_size_enum").
Each pair of `pad` and `code` correspond to a separate enumeration.
Each enumeration starts with the `index` of 0, and
the lowest invalid index marks the end of the enumeration.

Therefore, to enumerate frame sizes allowed on the specified pad
and using the specified mbus format, initialize the
`pad`, `which`, and `code` fields to desired values,
and set `index` to 0.
Then call the [ioctl VIDIOC_SUBDEV_ENUM_FRAME_SIZE](vidioc-subdev-enum-frame-size.md#vidioc-subdev-enum-frame-size) ioctl with a pointer to the
structure.

A successful call will return with minimum and maximum frame sizes filled in.
Repeat with increasing `index` until `EINVAL` is received.
`EINVAL` means that either no more entries are available in the enumeration,
or that an input parameter was invalid.

Sub-devices that only support discrete frame sizes (such as most
sensors) will return one or more frame sizes with identical minimum and
maximum values.

Not all possible sizes in given [minimum, maximum] ranges need to be
supported. For instance, a scaler that uses a fixed-point scaling ratio
might not be able to produce every frame size between the minimum and
maximum values. Applications must use the
[VIDIOC_SUBDEV_S_FMT](vidioc-subdev-g-fmt.md#vidioc-subdev-g-fmt) ioctl to try the
sub-device for an exact supported frame size.

Available frame sizes may depend on the current 'try' formats at other
pads of the sub-device, as well as on the current active links and the
current values of V4L2 controls. See
[ioctl VIDIOC_SUBDEV_G_FMT, VIDIOC_SUBDEV_S_FMT](vidioc-subdev-g-fmt.md#vidioc-subdev-g-fmt) for more
information about try formats.

type v4l2_subdev_frame_size_enum

struct v4l2_subdev_frame_size_enum

|  |  |  |
| --- | --- | --- |
| __u32 | `index` | Index of the frame size in the enumeration belonging to the given pad and format. Filled in by the application. |
| __u32 | `pad` | Pad number as reported by the media controller API. Filled in by the application. |
| __u32 | `code` | The media bus format code, as defined in [Media Bus Formats](subdev-formats.md#v4l2-mbus-format). Filled in by the application. |
| __u32 | `min_width` | Minimum frame width, in pixels. Filled in by the driver. |
| __u32 | `max_width` | Maximum frame width, in pixels. Filled in by the driver. |
| __u32 | `min_height` | Minimum frame height, in pixels. Filled in by the driver. |
| __u32 | `max_height` | Maximum frame height, in pixels. Filled in by the driver. |
| __u32 | `which` | Frame sizes to be enumerated, from enum [v4l2_subdev_format_whence](vidioc-subdev-g-fmt.md#v4l2-subdev-format-whence). |
| __u32 | `stream` | Stream identifier. |
| __u32 | `reserved`[7] | Reserved for future extensions. Applications and drivers must set the array to zero. |

## 7.56.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The struct [`v4l2_subdev_frame_size_enum`](vidioc-subdev-enum-frame-size.md#c.V4L.v4l2_subdev_frame_size_enum "v4l2_subdev_frame_size_enum") `pad` references a
    non-existing pad, the `which` field has an unsupported value, the `code`
    is invalid for the given pad, or the `index` field is out of bounds.

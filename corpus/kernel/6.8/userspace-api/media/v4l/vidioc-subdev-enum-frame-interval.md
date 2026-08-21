---
collection: kernel
version: "6.8"
title: "7.55. ioctl VIDIOC_SUBDEV_ENUM_FRAME_INTERVAL"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-subdev-enum-frame-interval.html
fetched_at: 2026-08-21T03:40:55+00:00
---
# 7.55. ioctl VIDIOC_SUBDEV_ENUM_FRAME_INTERVAL

## 7.55.1. Name

VIDIOC_SUBDEV_ENUM_FRAME_INTERVAL - Enumerate frame intervals

## 7.55.2. Synopsis

VIDIOC_SUBDEV_ENUM_FRAME_INTERVAL

`int ioctl(int fd, VIDIOC_SUBDEV_ENUM_FRAME_INTERVAL, struct v4l2_subdev_frame_interval_enum * argp)`

## 7.55.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_subdev_frame_interval_enum`](vidioc-subdev-enum-frame-interval.md#c.V4L.v4l2_subdev_frame_interval_enum "v4l2_subdev_frame_interval_enum").

## 7.55.4. Description

This ioctl lets applications enumerate available frame intervals on a
given sub-device pad. Frame intervals only makes sense for sub-devices
that can control the frame period on their own. This includes, for
instance, image sensors and TV tuners.

For the common use case of image sensors, the frame intervals available
on the sub-device output pad depend on the frame format and size on the
same pad. Applications must thus specify the desired format and size
when enumerating frame intervals.

To enumerate frame intervals applications initialize the `index`,
`pad`, `which`, `code`, `width` and `height` fields of struct
[`v4l2_subdev_frame_interval_enum`](vidioc-subdev-enum-frame-interval.md#c.V4L.v4l2_subdev_frame_interval_enum "v4l2_subdev_frame_interval_enum")
and call the [ioctl VIDIOC_SUBDEV_ENUM_FRAME_INTERVAL](vidioc-subdev-enum-frame-interval.md#vidioc-subdev-enum-frame-interval) ioctl with a pointer
to this structure. Drivers fill the rest of the structure or return an
EINVAL error code if one of the input fields is invalid. All frame
intervals are enumerable by beginning at index zero and incrementing by
one until `EINVAL` is returned.

Available frame intervals may depend on the current 'try' formats at
other pads of the sub-device, as well as on the current active links.
See [ioctl VIDIOC_SUBDEV_G_FMT, VIDIOC_SUBDEV_S_FMT](vidioc-subdev-g-fmt.md#vidioc-subdev-g-fmt) for more
information about the try formats.

Sub-devices that support the frame interval enumeration ioctl should
implemented it on a single pad only. Its behaviour when supported on
multiple pads of the same sub-device is not defined.

type v4l2_subdev_frame_interval_enum

struct v4l2_subdev_frame_interval_enum

|  |  |  |
| --- | --- | --- |
| __u32 | `index` | Number of the format in the enumeration, set by the application. |
| __u32 | `pad` | Pad number as reported by the media controller API. |
| __u32 | `code` | The media bus format code, as defined in [Media Bus Formats](subdev-formats.md#v4l2-mbus-format). |
| __u32 | `width` | Frame width, in pixels. |
| __u32 | `height` | Frame height, in pixels. |
| struct [`v4l2_fract`](vidioc-enumstd.md#c.V4L.v4l2_fract "v4l2_fract") | `interval` | Period, in seconds, between consecutive video frames. |
| __u32 | `which` | Frame intervals to be enumerated, from enum [v4l2_subdev_format_whence](vidioc-subdev-g-fmt.md#v4l2-subdev-format-whence). |
| __u32 | `stream` | Stream identifier. |
| __u32 | `reserved`[7] | Reserved for future extensions. Applications and drivers must set the array to zero. |

## 7.55.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The struct [`v4l2_subdev_frame_interval_enum`](vidioc-subdev-enum-frame-interval.md#c.V4L.v4l2_subdev_frame_interval_enum "v4l2_subdev_frame_interval_enum") `pad` references a
    non-existing pad, the `which` field has an unsupported value, one of the
    `code`, `width` or `height` fields are invalid for the given pad, or
    the `index` field is out of bounds.

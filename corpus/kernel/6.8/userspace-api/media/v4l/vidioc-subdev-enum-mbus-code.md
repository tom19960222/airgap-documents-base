---
collection: kernel
version: "6.8"
title: "7.57. ioctl VIDIOC_SUBDEV_ENUM_MBUS_CODE"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-subdev-enum-mbus-code.html
fetched_at: 2026-08-21T03:40:56+00:00
---
# 7.57. ioctl VIDIOC_SUBDEV_ENUM_MBUS_CODE

## 7.57.1. Name

VIDIOC_SUBDEV_ENUM_MBUS_CODE - Enumerate media bus formats

## 7.57.2. Synopsis

VIDIOC_SUBDEV_ENUM_MBUS_CODE

`int ioctl(int fd, VIDIOC_SUBDEV_ENUM_MBUS_CODE, struct v4l2_subdev_mbus_code_enum * argp)`

## 7.57.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_subdev_mbus_code_enum`](vidioc-subdev-enum-mbus-code.md#c.V4L.v4l2_subdev_mbus_code_enum "v4l2_subdev_mbus_code_enum").

## 7.57.4. Description

This call is used by the application to access the enumeration
of media bus formats for the selected pad.

The enumerations are defined by the driver, and indexed using the `index` field
of struct [`v4l2_subdev_mbus_code_enum`](vidioc-subdev-enum-mbus-code.md#c.V4L.v4l2_subdev_mbus_code_enum "v4l2_subdev_mbus_code_enum").
Each enumeration starts with the `index` of 0, and
the lowest invalid index marks the end of enumeration.

Therefore, to enumerate media bus formats available at a given sub-device pad,
initialize the `pad`, and `which` fields to desired values,
and set `index` to 0.
Then call the [ioctl VIDIOC_SUBDEV_ENUM_MBUS_CODE](vidioc-subdev-enum-mbus-code.md#vidioc-subdev-enum-mbus-code) ioctl
with a pointer to this structure.

A successful call will return with the `code` field filled in
with a mbus code value.
Repeat with increasing `index` until `EINVAL` is received.
`EINVAL` means that either `pad` is invalid,
or that there are no more codes available at this pad.

The driver must not return the same value of `code` for different indices
at the same pad.

Available media bus formats may depend on the current 'try' formats at
other pads of the sub-device, as well as on the current active links.
See [ioctl VIDIOC_SUBDEV_G_FMT, VIDIOC_SUBDEV_S_FMT](vidioc-subdev-g-fmt.md#vidioc-subdev-g-fmt) for more
information about the try formats.

type v4l2_subdev_mbus_code_enum

struct v4l2_subdev_mbus_code_enum

|  |  |  |
| --- | --- | --- |
| __u32 | `pad` | Pad number as reported by the media controller API. Filled in by the application. |
| __u32 | `index` | Index of the mbus code in the enumeration belonging to the given pad. Filled in by the application. |
| __u32 | `code` | The media bus format code, as defined in [Media Bus Formats](subdev-formats.md#v4l2-mbus-format). Filled in by the driver. |
| __u32 | `which` | Media bus format codes to be enumerated, from enum [v4l2_subdev_format_whence](vidioc-subdev-g-fmt.md#v4l2-subdev-format-whence). |
| __u32 | `flags` | See [Subdev Media Bus Code Enumerate Flags](vidioc-subdev-enum-mbus-code.md#v4l2-subdev-mbus-code-flags) |
| __u32 | `stream` | Stream identifier. |
| __u32 | `reserved`[6] | Reserved for future extensions. Applications and drivers must set the array to zero. |

Subdev Media Bus Code Enumerate Flags

|  |  |  |
| --- | --- | --- |
| V4L2_SUBDEV_MBUS_CODE_CSC_COLORSPACE | 0x00000001 | The driver allows the application to try to change the default colorspace encoding. The application can ask to configure the colorspace of the subdevice when calling the [VIDIOC_SUBDEV_S_FMT](vidioc-subdev-g-fmt.md#vidioc-subdev-g-fmt) ioctl with [V4L2_MBUS_FRAMEFMT_SET_CSC](subdev-formats.md#mbus-framefmt-set-csc) set. See [Media Bus Formats](subdev-formats.md#v4l2-mbus-format) on how to do this. |
| V4L2_SUBDEV_MBUS_CODE_CSC_XFER_FUNC | 0x00000002 | The driver allows the application to try to change the default transform function. The application can ask to configure the transform function of the subdevice when calling the [VIDIOC_SUBDEV_S_FMT](vidioc-subdev-g-fmt.md#vidioc-subdev-g-fmt) ioctl with [V4L2_MBUS_FRAMEFMT_SET_CSC](subdev-formats.md#mbus-framefmt-set-csc) set. See [Media Bus Formats](subdev-formats.md#v4l2-mbus-format) on how to do this. |
| V4L2_SUBDEV_MBUS_CODE_CSC_YCBCR_ENC | 0x00000004 | The driver allows the application to try to change the default Y'CbCr encoding. The application can ask to configure the Y'CbCr encoding of the subdevice when calling the [VIDIOC_SUBDEV_S_FMT](vidioc-subdev-g-fmt.md#vidioc-subdev-g-fmt) ioctl with [V4L2_MBUS_FRAMEFMT_SET_CSC](subdev-formats.md#mbus-framefmt-set-csc) set. See [Media Bus Formats](subdev-formats.md#v4l2-mbus-format) on how to do this. |
| V4L2_SUBDEV_MBUS_CODE_CSC_HSV_ENC | 0x00000004 | The driver allows the application to try to change the default HSV encoding. The application can ask to configure the HSV encoding of the subdevice when calling the [VIDIOC_SUBDEV_S_FMT](vidioc-subdev-g-fmt.md#vidioc-subdev-g-fmt) ioctl with [V4L2_MBUS_FRAMEFMT_SET_CSC](subdev-formats.md#mbus-framefmt-set-csc) set. See [Media Bus Formats](subdev-formats.md#v4l2-mbus-format) on how to do this. |
| V4L2_SUBDEV_MBUS_CODE_CSC_QUANTIZATION | 0x00000008 | The driver allows the application to try to change the default quantization. The application can ask to configure the quantization of the subdevice when calling the [VIDIOC_SUBDEV_S_FMT](vidioc-subdev-g-fmt.md#vidioc-subdev-g-fmt) ioctl with [V4L2_MBUS_FRAMEFMT_SET_CSC](subdev-formats.md#mbus-framefmt-set-csc) set. See [Media Bus Formats](subdev-formats.md#v4l2-mbus-format) on how to do this. |

## 7.57.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The struct [`v4l2_subdev_mbus_code_enum`](vidioc-subdev-enum-mbus-code.md#c.V4L.v4l2_subdev_mbus_code_enum "v4l2_subdev_mbus_code_enum") `pad` references a
    non-existing pad, the `which` field has an unsupported value, or the
    `index` field is out of bounds.

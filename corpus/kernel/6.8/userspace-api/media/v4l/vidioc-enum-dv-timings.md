---
collection: kernel
version: "6.8"
title: "7.13. ioctl VIDIOC_ENUM_DV_TIMINGS, VIDIOC_SUBDEV_ENUM_DV_TIMINGS"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-enum-dv-timings.html
fetched_at: 2026-08-21T03:40:38+00:00
---
# 7.13. ioctl VIDIOC_ENUM_DV_TIMINGS, VIDIOC_SUBDEV_ENUM_DV_TIMINGS

## 7.13.1. Name

VIDIOC_ENUM_DV_TIMINGS - VIDIOC_SUBDEV_ENUM_DV_TIMINGS - Enumerate supported Digital Video timings

## 7.13.2. Synopsis

VIDIOC_ENUM_DV_TIMINGS

`int ioctl(int fd, VIDIOC_ENUM_DV_TIMINGS, struct v4l2_enum_dv_timings *argp)`

VIDIOC_SUBDEV_ENUM_DV_TIMINGS

`int ioctl(int fd, VIDIOC_SUBDEV_ENUM_DV_TIMINGS, struct v4l2_enum_dv_timings *argp)`

## 7.13.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_enum_dv_timings`](vidioc-enum-dv-timings.md#c.V4L.v4l2_enum_dv_timings "v4l2_enum_dv_timings").

## 7.13.4. Description

While some DV receivers or transmitters support a wide range of timings,
others support only a limited number of timings. With this ioctl
applications can enumerate a list of known supported timings. Call
[ioctl VIDIOC_DV_TIMINGS_CAP, VIDIOC_SUBDEV_DV_TIMINGS_CAP](vidioc-dv-timings-cap.md#vidioc-dv-timings-cap) to check if it
also supports other standards or even custom timings that are not in
this list.

To query the available timings, applications initialize the `index`
field, set the `pad` field to 0, zero the reserved array of struct
[`v4l2_enum_dv_timings`](vidioc-enum-dv-timings.md#c.V4L.v4l2_enum_dv_timings "v4l2_enum_dv_timings") and call the
`VIDIOC_ENUM_DV_TIMINGS` ioctl on a video node with a pointer to this
structure. Drivers fill the rest of the structure or return an `EINVAL`
error code when the index is out of bounds. To enumerate all supported
DV timings, applications shall begin at index zero, incrementing by one
until the driver returns `EINVAL`.

> **Note:**
>
> Drivers may enumerate a different set of DV timings after
> switching the video input or output.

When implemented by the driver DV timings of subdevices can be queried
by calling the `VIDIOC_SUBDEV_ENUM_DV_TIMINGS` ioctl directly on a
subdevice node. The DV timings are specific to inputs (for DV receivers)
or outputs (for DV transmitters), applications must specify the desired
pad number in the struct
[`v4l2_enum_dv_timings`](vidioc-enum-dv-timings.md#c.V4L.v4l2_enum_dv_timings "v4l2_enum_dv_timings") `pad` field.
Attempts to enumerate timings on a pad that doesn't support them will
return an `EINVAL` error code.

type v4l2_enum_dv_timings

struct v4l2_enum_dv_timings

|  |  |  |
| --- | --- | --- |
| __u32 | `index` | Number of the DV timings, set by the application. |
| __u32 | `pad` | Pad number as reported by the media controller API. This field is only used when operating on a subdevice node. When operating on a video node applications must set this field to zero. |
| __u32 | `reserved`[2] | Reserved for future extensions. Drivers and applications must set the array to zero. |
| struct [`v4l2_dv_timings`](vidioc-g-dv-timings.md#c.V4L.v4l2_dv_timings "v4l2_dv_timings") | `timings` | The timings. |

## 7.13.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The struct [`v4l2_enum_dv_timings`](vidioc-enum-dv-timings.md#c.V4L.v4l2_enum_dv_timings "v4l2_enum_dv_timings")
    `index` is out of bounds or the `pad` number is invalid.

ENODATA
:   Digital video presets are not supported for this input or output.

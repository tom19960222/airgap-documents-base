---
collection: kernel
version: "6.8"
title: "7.9. ioctl VIDIOC_DV_TIMINGS_CAP, VIDIOC_SUBDEV_DV_TIMINGS_CAP"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-dv-timings-cap.html
fetched_at: 2026-08-21T03:40:29+00:00
---
# 7.9. ioctl VIDIOC_DV_TIMINGS_CAP, VIDIOC_SUBDEV_DV_TIMINGS_CAP

## 7.9.1. Name

VIDIOC_DV_TIMINGS_CAP - VIDIOC_SUBDEV_DV_TIMINGS_CAP - The capabilities of the Digital Video receiver/transmitter

## 7.9.2. Synopsis

VIDIOC_DV_TIMINGS_CAP

`int ioctl(int fd, VIDIOC_DV_TIMINGS_CAP, struct v4l2_dv_timings_cap *argp)`

VIDIOC_SUBDEV_DV_TIMINGS_CAP

`int ioctl(int fd, VIDIOC_SUBDEV_DV_TIMINGS_CAP, struct v4l2_dv_timings_cap *argp)`

## 7.9.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_dv_timings_cap`](vidioc-dv-timings-cap.md#c.V4L.v4l2_dv_timings_cap "v4l2_dv_timings_cap").

## 7.9.4. Description

To query the capabilities of the DV receiver/transmitter applications
initialize the `pad` field to 0, zero the reserved array of struct
[`v4l2_dv_timings_cap`](vidioc-dv-timings-cap.md#c.V4L.v4l2_dv_timings_cap "v4l2_dv_timings_cap") and call the
`VIDIOC_DV_TIMINGS_CAP` ioctl on a video node and the driver will fill
in the structure.

> **Note:**
>
> Drivers may return different values after
> switching the video input or output.

When implemented by the driver DV capabilities of subdevices can be
queried by calling the `VIDIOC_SUBDEV_DV_TIMINGS_CAP` ioctl directly
on a subdevice node. The capabilities are specific to inputs (for DV
receivers) or outputs (for DV transmitters), applications must specify
the desired pad number in the struct
[`v4l2_dv_timings_cap`](vidioc-dv-timings-cap.md#c.V4L.v4l2_dv_timings_cap "v4l2_dv_timings_cap") `pad` field and
zero the `reserved` array. Attempts to query capabilities on a pad
that doesn't support them will return an `EINVAL` error code.

type v4l2_bt_timings_cap

struct v4l2_bt_timings_cap

|  |  |  |
| --- | --- | --- |
| __u32 | `min_width` | Minimum width of the active video in pixels. |
| __u32 | `max_width` | Maximum width of the active video in pixels. |
| __u32 | `min_height` | Minimum height of the active video in lines. |
| __u32 | `max_height` | Maximum height of the active video in lines. |
| __u64 | `min_pixelclock` | Minimum pixelclock frequency in Hz. |
| __u64 | `max_pixelclock` | Maximum pixelclock frequency in Hz. |
| __u32 | `standards` | The video standard(s) supported by the hardware. See [DV BT Timing standards](vidioc-g-dv-timings.md#dv-bt-standards) for a list of standards. |
| __u32 | `capabilities` | Several flags giving more information about the capabilities. See [DV BT Timing capabilities](vidioc-dv-timings-cap.md#dv-bt-cap-capabilities) for a description of the flags. |
| __u32 | `reserved`[16] | Reserved for future extensions. Drivers must set the array to zero. |

type v4l2_dv_timings_cap

struct v4l2_dv_timings_cap

|  |  |  |
| --- | --- | --- |
| __u32 | `type` | Type of DV timings as listed in [DV Timing types](vidioc-g-dv-timings.md#dv-timing-types). |
| __u32 | `pad` | Pad number as reported by the media controller API. This field is only used when operating on a subdevice node. When operating on a video node applications must set this field to zero. |
| __u32 | `reserved`[2] | Reserved for future extensions.  Drivers and applications must set the array to zero. |
| union { | (anonymous) | |
| struct [`v4l2_bt_timings_cap`](vidioc-dv-timings-cap.md#c.V4L.v4l2_bt_timings_cap "v4l2_bt_timings_cap") | `bt` | BT.656/1120 timings capabilities of the hardware. |
| __u32 | `raw_data`[32] | |
| } |  | |

DV BT Timing capabilities

|  |  |
| --- | --- |
| Flag | Description |
|  |  |
| `V4L2_DV_BT_CAP_INTERLACED` | Interlaced formats are supported. |
| `V4L2_DV_BT_CAP_PROGRESSIVE` | Progressive formats are supported. |
| `V4L2_DV_BT_CAP_REDUCED_BLANKING` | CVT/GTF specific: the timings can make use of reduced blanking (CVT) or the 'Secondary GTF' curve (GTF). |
| `V4L2_DV_BT_CAP_CUSTOM` | Can support non-standard timings, i.e. timings not belonging to the standards set in the `standards` field. |

## 7.9.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

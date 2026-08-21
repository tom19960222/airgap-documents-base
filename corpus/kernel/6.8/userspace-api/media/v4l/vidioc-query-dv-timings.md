---
collection: kernel
version: "6.8"
title: "7.50. ioctl VIDIOC_QUERY_DV_TIMINGS"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-query-dv-timings.html
fetched_at: 2026-08-21T03:41:04+00:00
---
# 7.50. ioctl VIDIOC_QUERY_DV_TIMINGS

## 7.50.1. Name

VIDIOC_QUERY_DV_TIMINGS - VIDIOC_SUBDEV_QUERY_DV_TIMINGS - Sense the DV preset received by the current input

## 7.50.2. Synopsis

VIDIOC_QUERY_DV_TIMINGS

`int ioctl(int fd, VIDIOC_QUERY_DV_TIMINGS, struct v4l2_dv_timings *argp)`

VIDIOC_SUBDEV_QUERY_DV_TIMINGS

`int ioctl(int fd, VIDIOC_SUBDEV_QUERY_DV_TIMINGS, struct v4l2_dv_timings *argp)`

## 7.50.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_dv_timings`](vidioc-g-dv-timings.md#c.V4L.v4l2_dv_timings "v4l2_dv_timings").

## 7.50.4. Description

The hardware may be able to detect the current DV timings automatically,
similar to sensing the video standard. To do so, applications call
[ioctl VIDIOC_QUERY_DV_TIMINGS](vidioc-query-dv-timings.md#vidioc-query-dv-timings) with a pointer to a struct
[`v4l2_dv_timings`](vidioc-g-dv-timings.md#c.V4L.v4l2_dv_timings "v4l2_dv_timings"). Once the hardware detects
the timings, it will fill in the timings structure.

> **Note:**
>
> Drivers shall *not* switch timings automatically if new
> timings are detected. Instead, drivers should send the
> `V4L2_EVENT_SOURCE_CHANGE` event (if they support this) and expect
> that userspace will take action by calling [ioctl VIDIOC_QUERY_DV_TIMINGS](vidioc-query-dv-timings.md#vidioc-query-dv-timings).
> The reason is that new timings usually mean different buffer sizes as
> well, and you cannot change buffer sizes on the fly. In general,
> applications that receive the Source Change event will have to call
> [ioctl VIDIOC_QUERY_DV_TIMINGS](vidioc-query-dv-timings.md#vidioc-query-dv-timings), and if the detected timings are valid they
> will have to stop streaming, set the new timings, allocate new buffers
> and start streaming again.

If the timings could not be detected because there was no signal, then
ENOLINK is returned. If a signal was detected, but it was unstable and
the receiver could not lock to the signal, then `ENOLCK` is returned. If
the receiver could lock to the signal, but the format is unsupported
(e.g. because the pixelclock is out of range of the hardware
capabilities), then the driver fills in whatever timings it could find
and returns `ERANGE`. In that case the application can call
[ioctl VIDIOC_DV_TIMINGS_CAP, VIDIOC_SUBDEV_DV_TIMINGS_CAP](vidioc-dv-timings-cap.md#vidioc-dv-timings-cap) to compare the
found timings with the hardware's capabilities in order to give more
precise feedback to the user.

## 7.50.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

ENODATA
:   Digital video timings are not supported for this input or output.

ENOLINK
:   No timings could be detected because no signal was found.

ENOLCK
:   The signal was unstable and the hardware could not lock on to it.

ERANGE
:   Timings were found, but they are out of range of the hardware
    capabilities.

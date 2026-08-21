---
collection: kernel
version: "6.8"
title: "7.51. ioctl VIDIOC_QUERYSTD, VIDIOC_SUBDEV_QUERYSTD"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-querystd.html
fetched_at: 2026-08-21T03:41:05+00:00
---
# 7.51. ioctl VIDIOC_QUERYSTD, VIDIOC_SUBDEV_QUERYSTD

## 7.51.1. Name

VIDIOC_QUERYSTD - VIDIOC_SUBDEV_QUERYSTD - Sense the video standard received by the current input

## 7.51.2. Synopsis

VIDIOC_QUERYSTD

`int ioctl(int fd, VIDIOC_QUERYSTD, v4l2_std_id *argp)`

VIDIOC_SUBDEV_QUERYSTD

`int ioctl(int fd, VIDIOC_SUBDEV_QUERYSTD, v4l2_std_id *argp)`

## 7.51.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to `v4l2_std_id`.

## 7.51.4. Description

The hardware may be able to detect the current video standard
automatically. To do so, applications call [ioctl VIDIOC_QUERYSTD, VIDIOC_SUBDEV_QUERYSTD](vidioc-querystd.md#vidioc-querystd) with a
pointer to a [v4l2_std_id](vidioc-enumstd.md#v4l2-std-id) type. The driver
stores here a set of candidates, this can be a single flag or a set of
supported standards if for example the hardware can only distinguish
between 50 and 60 Hz systems. If no signal was detected, then the driver
will return V4L2_STD_UNKNOWN. When detection is not possible or fails,
the set must contain all standards supported by the current video input
or output.

> **Note:**
>
> Drivers shall *not* switch the video standard
> automatically if a new video standard is detected. Instead, drivers
> should send the `V4L2_EVENT_SOURCE_CHANGE` event (if they support
> this) and expect that userspace will take action by calling
> [ioctl VIDIOC_QUERYSTD, VIDIOC_SUBDEV_QUERYSTD](vidioc-querystd.md#vidioc-querystd). The reason is that a new video standard can mean
> different buffer sizes as well, and you cannot change buffer sizes on
> the fly. In general, applications that receive the Source Change event
> will have to call [ioctl VIDIOC_QUERYSTD, VIDIOC_SUBDEV_QUERYSTD](vidioc-querystd.md#vidioc-querystd), and if the detected video
> standard is valid they will have to stop streaming, set the new
> standard, allocate new buffers and start streaming again.

## 7.51.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

ENODATA
:   Standard video timings are not supported for this input or output.

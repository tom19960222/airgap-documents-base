---
collection: kernel
version: "6.8"
title: "1.29. Streaming Parameters"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/streaming-par.html
fetched_at: 2026-08-21T03:56:56+00:00
---
# 1.29. Streaming Parameters

Streaming parameters are intended to optimize the video capture process
as well as I/O. Presently applications can request a high quality
capture mode with the [VIDIOC_S_PARM](vidioc-g-parm.md#vidioc-g-parm) ioctl.

The current video standard determines a nominal number of frames per
second. If less than this number of frames is to be captured or output,
applications can request frame skipping or duplicating on the driver
side. This is especially useful when using the
[`read()`](func-read.md#c.V4L.read "read") or [`write()`](func-write.md#c.V4L.write "write"), which are
not augmented by timestamps or sequence counters, and to avoid
unnecessary data copying.

Finally these ioctls can be used to determine the number of buffers used
internally by a driver in read/write mode. For implications see the
section discussing the [`read()`](func-read.md#c.V4L.read "read") function.

To get and set the streaming parameters applications call the
[VIDIOC_G_PARM](vidioc-g-parm.md#vidioc-g-parm) and
[VIDIOC_S_PARM](vidioc-g-parm.md#vidioc-g-parm) ioctl, respectively. They take
a pointer to a struct [`v4l2_streamparm`](vidioc-g-parm.md#c.V4L.v4l2_streamparm "v4l2_streamparm"), which
contains a union holding separate parameters for input and output
devices.

These ioctls are optional, drivers need not implement them. If so, they
return the `EINVAL` error code.

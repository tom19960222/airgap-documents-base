---
collection: kernel
version: "6.8"
title: "1.3. Application Priority"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/app-pri.html
fetched_at: 2026-08-21T03:56:39+00:00
---
# 1.3. Application Priority

When multiple applications share a device it may be desirable to assign
them different priorities. Contrary to the traditional "rm -rf /" school
of thought, a video recording application could for example block other
applications from changing video controls or switching the current TV
channel. Another objective is to permit low priority applications
working in background, which can be preempted by user controlled
applications and automatically regain control of the device at a later
time.

Since these features cannot be implemented entirely in user space V4L2
defines the [VIDIOC_G_PRIORITY](vidioc-g-priority.md#vidioc-g-priority) and
[VIDIOC_S_PRIORITY](vidioc-g-priority.md#vidioc-g-priority) ioctls to request and
query the access priority associate with a file descriptor. Opening a
device assigns a medium priority, compatible with earlier versions of
V4L2 and drivers not supporting these ioctls. Applications requiring a
different priority will usually call [VIDIOC_S_PRIORITY](vidioc-g-priority.md#vidioc-g-priority) after verifying the device with the
[ioctl VIDIOC_QUERYCAP](vidioc-querycap.md#vidioc-querycap) ioctl.

Ioctls changing driver properties, such as
[VIDIOC_S_INPUT](vidioc-g-input.md#vidioc-g-input), return an `EBUSY` error code
after another application obtained higher priority.

---
collection: kernel
version: "6.8"
title: "1.2. Querying Capabilities"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/querycap.html
fetched_at: 2026-08-21T03:56:39+00:00
---
# 1.2. Querying Capabilities

Because V4L2 covers a wide variety of devices not all aspects of the API
are equally applicable to all types of devices. Furthermore devices of
the same type have different capabilities and this specification permits
the omission of a few complicated and less important parts of the API.

The [ioctl VIDIOC_QUERYCAP](vidioc-querycap.md#vidioc-querycap) ioctl is available to
check if the kernel device is compatible with this specification, and to
query the [functions](devices.md#devices) and [I/O methods](io.md#io)
supported by the device.

Starting with kernel version 3.1, [ioctl VIDIOC_QUERYCAP](vidioc-querycap.md#vidioc-querycap)
will return the V4L2 API version used by the driver, with generally
matches the Kernel version. There's no need of using
[ioctl VIDIOC_QUERYCAP](vidioc-querycap.md#vidioc-querycap) to check if a specific ioctl
is supported, the V4L2 core now returns `ENOTTY` if a driver doesn't
provide support for an ioctl.

Other features can be queried by calling the respective ioctl, for
example [ioctl VIDIOC_ENUMINPUT](vidioc-enuminput.md#vidioc-enuminput) to learn about the
number, types and names of video connectors on the device. Although
abstraction is a major objective of this API, the
[ioctl VIDIOC_QUERYCAP](vidioc-querycap.md#vidioc-querycap) ioctl also allows driver
specific applications to reliably identify the driver.

All V4L2 drivers must support [ioctl VIDIOC_QUERYCAP](vidioc-querycap.md#vidioc-querycap).
Applications should always call this ioctl after opening the device.

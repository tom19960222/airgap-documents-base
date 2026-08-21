---
collection: kernel
version: "6.8"
title: "1.25. Data Formats"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/format.html
fetched_at: 2026-08-21T03:56:50+00:00
---
# 1.25. Data Formats

## 1.25.1. Data Format Negotiation

Different devices exchange different kinds of data with applications,
for example video images, raw or sliced VBI data, RDS datagrams. Even
within one kind many different formats are possible, in particular there is an
abundance of image formats. Although drivers must provide a default and
the selection persists across closing and reopening a device,
applications should always negotiate a data format before engaging in
data exchange. Negotiation means the application asks for a particular
format and the driver selects and reports the best the hardware can do
to satisfy the request. Of course applications can also just query the
current selection.

A single mechanism exists to negotiate all data formats using the
aggregate struct [`v4l2_format`](vidioc-g-fmt.md#c.V4L.v4l2_format "v4l2_format") and the
[VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt) and
[VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctls. Additionally the
[VIDIOC_TRY_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl can be used to examine
what the hardware *could* do, without actually selecting a new data
format. The data formats supported by the V4L2 API are covered in the
respective device section in [Interfaces](devices.md#devices). For a closer look at
image formats see [Image Formats](pixfmt.md#pixfmt).

The [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl is a major turning-point in the
initialization sequence. Prior to this point multiple panel applications
can access the same device concurrently to select the current input,
change controls or modify other properties. The first [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt)
assigns a logical stream (video data, VBI data etc.) exclusively to one
file descriptor.

Exclusive means no other application, more precisely no other file
descriptor, can grab this stream or change device properties
inconsistent with the negotiated parameters. A video standard change for
example, when the new standard uses a different number of scan lines,
can invalidate the selected image format. Therefore only the file
descriptor owning the stream can make invalidating changes. Accordingly
multiple file descriptors which grabbed different logical streams
prevent each other from interfering with their settings. When for
example video overlay is about to start or already in progress,
simultaneous video capturing may be restricted to the same cropping and
image size.

When applications omit the [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl its locking side
effects are implied by the next step, the selection of an I/O method
with the [ioctl VIDIOC_REQBUFS](vidioc-reqbufs.md#vidioc-reqbufs) ioctl or implicit
with the first [`read()`](func-read.md#c.V4L.read "read") or
[`write()`](func-write.md#c.V4L.write "write") call.

Generally only one logical stream can be assigned to a file descriptor,
the exception being drivers permitting simultaneous video capturing and
overlay using the same file descriptor for compatibility with V4L and
earlier versions of V4L2. Switching the logical stream or returning into
"panel mode" is possible by closing and reopening the device. Drivers
*may* support a switch using [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt).

All drivers exchanging data with applications must support the
[VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt) and [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl. Implementation of the
[VIDIOC_TRY_FMT](vidioc-g-fmt.md#vidioc-g-fmt) is highly recommended but optional.

## 1.25.2. Image Format Enumeration

Apart of the generic format negotiation functions a special ioctl to
enumerate all image formats supported by video capture, overlay or
output devices is available. [1](format.md#f1)

The [ioctl VIDIOC_ENUM_FMT](vidioc-enum-fmt.md#vidioc-enum-fmt) ioctl must be supported
by all drivers exchanging image data with applications.

> **Important:**
>
> Drivers are not supposed to convert image formats in kernel space.
> They must enumerate only formats directly supported by the hardware.
> If necessary driver writers should publish an example conversion
> routine or library for integration into applications.

[1](format.md#id1)
:   Enumerating formats an application has no a-priori knowledge of
    (otherwise it could explicitly ask for them and need not enumerate)
    seems useless, but there are applications serving as proxy between
    drivers and the actual video applications for which this is useful.

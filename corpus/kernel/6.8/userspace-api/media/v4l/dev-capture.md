---
collection: kernel
version: "6.8"
title: "4.1. Video Capture Interface"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/dev-capture.html
fetched_at: 2026-08-21T03:57:30+00:00
---
# 4.1. Video Capture Interface

Video capture devices sample an analog video signal and store the
digitized images in memory. Today nearly all devices can capture at full
25 or 30 frames/second. With this interface applications can control the
capture process and move images from the driver into user space.

Conventionally V4L2 video capture devices are accessed through character
device special files named `/dev/video` and `/dev/video0` to
`/dev/video63` with major number 81 and minor numbers 0 to 63.
`/dev/video` is typically a symbolic link to the preferred video
device.

> **Note:**
>
> The same device file names are used for video output devices.

## 4.1.1. Querying Capabilities

Devices supporting the video capture interface set the
`V4L2_CAP_VIDEO_CAPTURE` or `V4L2_CAP_VIDEO_CAPTURE_MPLANE` flag in
the `capabilities` field of struct
[`v4l2_capability`](vidioc-querycap.md#c.V4L.v4l2_capability "v4l2_capability") returned by the
[ioctl VIDIOC_QUERYCAP](vidioc-querycap.md#vidioc-querycap) ioctl. As secondary device
functions they may also support the [video overlay](dev-overlay.md#overlay)
(`V4L2_CAP_VIDEO_OVERLAY`) and the [raw VBI capture](dev-raw-vbi.md#raw-vbi)
(`V4L2_CAP_VBI_CAPTURE`) interface. At least one of the read/write or
streaming I/O methods must be supported. Tuners and audio inputs are
optional.

## 4.1.2. Supplemental Functions

Video capture devices shall support [audio input](audio.md#audio),
[Tuners and Modulators](tuner.md#tuner), [controls](control.md#control),
[cropping and scaling](crop.md#crop) and
[streaming parameter](streaming-par.md#streaming-par) ioctls as needed. The
[video input](video.md#video) ioctls must be supported by all video
capture devices.

## 4.1.3. Image Format Negotiation

The result of a capture operation is determined by cropping and image
format parameters. The former select an area of the video picture to
capture, the latter how images are stored in memory, i. e. in RGB or YUV
format, the number of bits per pixel or width and height. Together they
also define how images are scaled in the process.

As usual these parameters are *not* reset at [`open()`](func-open.md#c.V4L.open "open")
time to permit Unix tool chains, programming a device and then reading
from it as if it was a plain file. Well written V4L2 applications ensure
they really get what they want, including cropping and scaling.

Cropping initialization at minimum requires to reset the parameters to
defaults. An example is given in [Image Cropping, Insertion and Scaling -- the CROP API](crop.md#crop).

To query the current image format applications set the `type` field of
a struct [`v4l2_format`](vidioc-g-fmt.md#c.V4L.v4l2_format "v4l2_format") to
`V4L2_BUF_TYPE_VIDEO_CAPTURE` or
`V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE` and call the
[VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl with a pointer to this
structure. Drivers fill the struct
[`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format") `pix` or the struct
[`v4l2_pix_format_mplane`](pixfmt-v4l2-mplane.md#c.v4l2_pix_format_mplane "v4l2_pix_format_mplane") `pix_mp`
member of the `fmt` union.

To request different parameters applications set the `type` field of a
struct [`v4l2_format`](vidioc-g-fmt.md#c.V4L.v4l2_format "v4l2_format") as above and initialize all
fields of the struct [`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format")
`vbi` member of the `fmt` union, or better just modify the results
of [VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt), and call the [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt)
ioctl with a pointer to this structure. Drivers may adjust the
parameters and finally return the actual parameters as [VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt)
does.

Like [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) the [VIDIOC_TRY_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl
can be used to learn about hardware limitations without disabling I/O or
possibly time consuming hardware preparations.

The contents of struct [`v4l2_pix_format`](pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format") and
struct [`v4l2_pix_format_mplane`](pixfmt-v4l2-mplane.md#c.v4l2_pix_format_mplane "v4l2_pix_format_mplane") are
discussed in [Image Formats](pixfmt.md#pixfmt). See also the specification of the
[VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt), [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) and [VIDIOC_TRY_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctls for
details. Video capture devices must implement both the [VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt)
and [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl, even if [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ignores all
requests and always returns default parameters as [VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt) does.
[VIDIOC_TRY_FMT](vidioc-g-fmt.md#vidioc-g-fmt) is optional.

## 4.1.4. Reading Images

A video capture device may support the [read() function](func-read.md#func-read)
and/or streaming ([memory mapping](func-mmap.md#func-mmap) or
[user pointer](userp.md#userp)) I/O. See [Input/Output](io.md#io) for details.

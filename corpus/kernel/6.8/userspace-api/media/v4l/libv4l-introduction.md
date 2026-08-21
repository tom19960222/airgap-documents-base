---
collection: kernel
version: "6.8"
title: "5.1. Introduction"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/libv4l-introduction.html
fetched_at: 2026-08-21T03:40:32+00:00
---
# 5.1. Introduction

libv4l is a collection of libraries which adds a thin abstraction layer
on top of video4linux2 devices. The purpose of this (thin) layer is to
make it easy for application writers to support a wide variety of
devices without having to write separate code for different devices in
the same class.

An example of using libv4l is provided by
[v4l2grab](v4l2grab-example.md#v4l2grab-example).

libv4l consists of 3 different libraries:

## 5.1.1. libv4lconvert

libv4lconvert is a library that converts several different pixelformats
found in V4L2 drivers into a few common RGB and YUY formats.

It currently accepts the following V4L2 driver formats:
[V4L2_PIX_FMT_BGR24](pixfmt-rgb.md#v4l2-pix-fmt-bgr24),
[V4L2_PIX_FMT_NV12_16L16](pixfmt-yuv-planar.md#v4l2-pix-fmt-nv12-16l16),
[V4L2_PIX_FMT_JPEG](pixfmt-compressed.md#v4l2-pix-fmt-jpeg),
[V4L2_PIX_FMT_MJPEG](pixfmt-reserved.md#v4l2-pix-fmt-mjpeg),
[V4L2_PIX_FMT_MR97310A](pixfmt-reserved.md#v4l2-pix-fmt-mr97310a),
[V4L2_PIX_FMT_OV511](pixfmt-reserved.md#v4l2-pix-fmt-ov511),
[V4L2_PIX_FMT_OV518](pixfmt-reserved.md#v4l2-pix-fmt-ov518),
[V4L2_PIX_FMT_PAC207](pixfmt-reserved.md#v4l2-pix-fmt-pac207),
[V4L2_PIX_FMT_PJPG](pixfmt-reserved.md#v4l2-pix-fmt-pjpg),
[V4L2_PIX_FMT_RGB24](pixfmt-rgb.md#v4l2-pix-fmt-rgb24),
[V4L2_PIX_FMT_SBGGR8](pixfmt-srggb8.md#v4l2-pix-fmt-sbggr8),
[V4L2_PIX_FMT_SGBRG8](pixfmt-srggb8.md#v4l2-pix-fmt-sgbrg8),
[V4L2_PIX_FMT_SGRBG8](pixfmt-srggb8.md#v4l2-pix-fmt-sgrbg8),
[V4L2_PIX_FMT_SN9C10X](pixfmt-reserved.md#v4l2-pix-fmt-sn9c10x),
[V4L2_PIX_FMT_SN9C20X_I420](pixfmt-reserved.md#v4l2-pix-fmt-sn9c20x-i420),
[V4L2_PIX_FMT_SPCA501](pixfmt-reserved.md#v4l2-pix-fmt-spca501),
[V4L2_PIX_FMT_SPCA505](pixfmt-reserved.md#v4l2-pix-fmt-spca505),
[V4L2_PIX_FMT_SPCA508](pixfmt-reserved.md#v4l2-pix-fmt-spca508),
[V4L2_PIX_FMT_SPCA561](pixfmt-reserved.md#v4l2-pix-fmt-spca561),
[V4L2_PIX_FMT_SQ905C](pixfmt-reserved.md#v4l2-pix-fmt-sq905c),
[V4L2_PIX_FMT_SRGGB8](pixfmt-srggb8.md#v4l2-pix-fmt-srggb8),
[V4L2_PIX_FMT_UYVY](pixfmt-packed-yuv.md#v4l2-pix-fmt-uyvy),
[V4L2_PIX_FMT_YUV420](pixfmt-yuv-planar.md#v4l2-pix-fmt-yuv420),
[V4L2_PIX_FMT_YUYV](pixfmt-packed-yuv.md#v4l2-pix-fmt-yuyv),
[V4L2_PIX_FMT_YVU420](pixfmt-yuv-planar.md#v4l2-pix-fmt-yvu420), and
[V4L2_PIX_FMT_YVYU](pixfmt-packed-yuv.md#v4l2-pix-fmt-yvyu).

Later on libv4lconvert was expanded to also be able to do various video
processing functions to improve webcam video quality. The video
processing is split in to 2 parts: libv4lconvert/control and
libv4lconvert/processing.

The control part is used to offer video controls which can be used to
control the video processing functions made available by
libv4lconvert/processing. These controls are stored application wide
(until reboot) by using a persistent shared memory object.

libv4lconvert/processing offers the actual video processing
functionality.

## 5.1.2. libv4l1

This library offers functions that can be used to quickly make v4l1
applications work with v4l2 devices. These functions work exactly like
the normal open/close/etc, except that libv4l1 does full emulation of
the v4l1 api on top of v4l2 drivers, in case of v4l1 drivers it will
just pass calls through.

Since those functions are emulations of the old V4L1 API, it shouldn't
be used for new applications.

## 5.1.3. libv4l2

This library should be used for all modern V4L2 applications.

It provides handles to call V4L2 open/ioctl/close/poll methods. Instead
of just providing the raw output of the device, it enhances the calls in
the sense that it will use libv4lconvert to provide more video formats
and to enhance the image quality.

In most cases, libv4l2 just passes the calls directly through to the
v4l2 driver, intercepting the calls to
[VIDIOC_TRY_FMT](vidioc-g-fmt.md#vidioc-g-fmt),
[VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt),
[VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt),
[VIDIOC_ENUM_FRAMESIZES](vidioc-enum-framesizes.md#vidioc-enum-framesizes) and
[VIDIOC_ENUM_FRAMEINTERVALS](vidioc-enum-frameintervals.md#vidioc-enum-frameintervals) in
order to emulate the formats
[V4L2_PIX_FMT_BGR24](pixfmt-rgb.md#v4l2-pix-fmt-bgr24),
[V4L2_PIX_FMT_RGB24](pixfmt-rgb.md#v4l2-pix-fmt-rgb24),
[V4L2_PIX_FMT_YUV420](pixfmt-yuv-planar.md#v4l2-pix-fmt-yuv420), and
[V4L2_PIX_FMT_YVU420](pixfmt-yuv-planar.md#v4l2-pix-fmt-yvu420), if they aren't
available in the driver. [VIDIOC_ENUM_FMT](vidioc-enum-fmt.md#vidioc-enum-fmt)
keeps enumerating the hardware supported formats, plus the emulated
formats offered by libv4l at the end.

### 5.1.3.1. Libv4l device control functions

The common file operation methods are provided by libv4l.

Those functions operate just like the gcc function `dup()` and
V4L2 functions
[`open()`](func-open.md#c.V4L.open "open"), [`close()`](func-close.md#c.V4L.close "close"),
`ioctl()`, [`read()`](func-read.md#c.V4L.read "read"),
[`mmap()`](func-mmap.md#c.V4L.mmap "mmap") and [`munmap()`](func-munmap.md#c.V4L.munmap "munmap"):

int v4l2_open(const char \*file, int oflag, ...)
:   operates like the [`open()`](func-open.md#c.V4L.open "open") function.

int v4l2_close(int fd)
:   operates like the [`close()`](func-close.md#c.V4L.close "close") function.

int v4l2_dup(int fd)
:   operates like the libc `dup()` function, duplicating a file handler.

int v4l2_ioctl(int fd, unsigned long int request, ...)
:   operates like the `ioctl()` function.

int v4l2_read(int fd, void \*buffer, size_t n)
:   operates like the [`read()`](func-read.md#c.V4L.read "read") function.

void \*v4l2_mmap(void \*start, size_t length, int prot, int flags, int fd, int64_t offset);
:   operates like the [`mmap()`](func-mmap.md#c.V4L.mmap "mmap") function.

int v4l2_munmap(void \*_start, size_t length);
:   operates like the [`munmap()`](func-munmap.md#c.V4L.munmap "munmap") function.

Those functions provide additional control:

int v4l2_fd_open(int fd, int v4l2_flags)
:   opens an already opened fd for further use through v4l2lib and possibly
    modify libv4l2's default behavior through the `v4l2_flags` argument.
    Currently, `v4l2_flags` can be `V4L2_DISABLE_CONVERSION`, to disable
    format conversion.

int v4l2_set_control(int fd, int cid, int value)
:   This function takes a value of 0 - 65535, and then scales that range to the
    actual range of the given v4l control id, and then if the cid exists and is
    not locked sets the cid to the scaled value.

int v4l2_get_control(int fd, int cid)
:   This function returns a value of 0 - 65535, scaled to from the actual range
    of the given v4l control id. when the cid does not exist, could not be
    accessed for some reason, or some error occurred 0 is returned.

## 5.1.4. v4l1compat.so wrapper library

This library intercepts calls to
[`open()`](func-open.md#c.V4L.open "open"), [`close()`](func-close.md#c.V4L.close "close"),
`ioctl()`, [`mmap()`](func-mmap.md#c.V4L.mmap "mmap") and
[`munmap()`](func-munmap.md#c.V4L.munmap "munmap")
operations and redirects them to the libv4l counterparts, by using
`LD_PRELOAD=/usr/lib/v4l1compat.so`. It also emulates V4L1 calls via V4L2
API.

It allows usage of binary legacy applications that still don't use
libv4l.

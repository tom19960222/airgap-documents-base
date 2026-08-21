---
collection: kernel
version: "6.8"
title: "7.41. ioctl VIDIOC_G_STD, VIDIOC_S_STD, VIDIOC_SUBDEV_G_STD, VIDIOC_SUBDEV_S_STD"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-g-std.html
fetched_at: 2026-08-21T03:41:02+00:00
---
# 7.41. ioctl VIDIOC_G_STD, VIDIOC_S_STD, VIDIOC_SUBDEV_G_STD, VIDIOC_SUBDEV_S_STD

## 7.41.1. Name

VIDIOC_G_STD - VIDIOC_S_STD - VIDIOC_SUBDEV_G_STD - VIDIOC_SUBDEV_S_STD - Query or select the video standard of the current input

## 7.41.2. Synopsis

VIDIOC_G_STD

`int ioctl(int fd, VIDIOC_G_STD, v4l2_std_id *argp)`

VIDIOC_S_STD

`int ioctl(int fd, VIDIOC_S_STD, const v4l2_std_id *argp)`

VIDIOC_SUBDEV_G_STD

`int ioctl(int fd, VIDIOC_SUBDEV_G_STD, v4l2_std_id *argp)`

VIDIOC_SUBDEV_S_STD

`int ioctl(int fd, VIDIOC_SUBDEV_S_STD, const v4l2_std_id *argp)`

## 7.41.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to `v4l2_std_id`.

## 7.41.4. Description

To query and select the current video standard applications use the
[VIDIOC_G_STD](vidioc-g-std.md#vidioc-g-std) and [VIDIOC_S_STD](vidioc-g-std.md#vidioc-g-std) ioctls which take a pointer to a
[v4l2_std_id](vidioc-enumstd.md#v4l2-std-id) type as argument. [VIDIOC_G_STD](vidioc-g-std.md#vidioc-g-std)
can return a single flag or a set of flags as in struct
[`v4l2_standard`](vidioc-enumstd.md#c.V4L.v4l2_standard "v4l2_standard") field `id`. The flags must be
unambiguous such that they appear in only one enumerated
struct [`v4l2_standard`](vidioc-enumstd.md#c.V4L.v4l2_standard "v4l2_standard") structure.

[VIDIOC_S_STD](vidioc-g-std.md#vidioc-g-std) accepts one or more flags, being a write-only ioctl it
does not return the actual new standard as [VIDIOC_G_STD](vidioc-g-std.md#vidioc-g-std) does. When
no flags are given or the current input does not support the requested
standard the driver returns an `EINVAL` error code. When the standard set
is ambiguous drivers may return `EINVAL` or choose any of the requested
standards. If the current input or output does not support standard
video timings (e.g. if [ioctl VIDIOC_ENUMINPUT](vidioc-enuminput.md#vidioc-enuminput)
does not set the `V4L2_IN_CAP_STD` flag), then `ENODATA` error code is
returned.

Calling `VIDIOC_SUBDEV_S_STD` on a subdev device node that has been registered
in read-only mode is not allowed. An error is returned and the errno variable is
set to `-EPERM`.

## 7.41.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The [VIDIOC_S_STD](vidioc-g-std.md#vidioc-g-std) parameter was unsuitable.

ENODATA
:   Standard video timings are not supported for this input or output.

EPERM
:   `VIDIOC_SUBDEV_S_STD` has been called on a read-only subdevice.

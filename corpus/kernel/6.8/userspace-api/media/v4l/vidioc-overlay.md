---
collection: kernel
version: "6.8"
title: "7.44. ioctl VIDIOC_OVERLAY"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-overlay.html
fetched_at: 2026-08-21T03:41:03+00:00
---
# 7.44. ioctl VIDIOC_OVERLAY

## 7.44.1. Name

VIDIOC_OVERLAY - Start or stop video overlay

## 7.44.2. Synopsis

VIDIOC_OVERLAY

`int ioctl(int fd, VIDIOC_OVERLAY, const int *argp)`

## 7.44.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to an integer.

## 7.44.4. Description

This ioctl is part of the [video overlay](dev-overlay.md#overlay) I/O method.
Applications call [ioctl VIDIOC_OVERLAY](vidioc-overlay.md#vidioc-overlay) to start or stop the overlay. It
takes a pointer to an integer which must be set to zero by the
application to stop overlay, to one to start.

Drivers do not support [ioctl VIDIOC_STREAMON, VIDIOC_STREAMOFF](vidioc-streamon.md#vidioc-streamon) or
[VIDIOC_STREAMOFF](vidioc-streamon.md#vidioc-streamon) with
`V4L2_BUF_TYPE_VIDEO_OVERLAY`.

## 7.44.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The overlay parameters have not been set up. See [Video Overlay Interface](dev-overlay.md#overlay)
    for the necessary steps.

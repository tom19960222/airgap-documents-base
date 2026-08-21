---
collection: kernel
version: "6.8"
title: "7.45. ioctl VIDIOC_PREPARE_BUF"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-prepare-buf.html
fetched_at: 2026-08-21T03:41:04+00:00
---
# 7.45. ioctl VIDIOC_PREPARE_BUF

## 7.45.1. Name

VIDIOC_PREPARE_BUF - Prepare a buffer for I/O

## 7.45.2. Synopsis

VIDIOC_PREPARE_BUF

`int ioctl(int fd, VIDIOC_PREPARE_BUF, struct v4l2_buffer *argp)`

## 7.45.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_buffer`](buffer.md#c.V4L.v4l2_buffer "v4l2_buffer").

## 7.45.4. Description

Applications can optionally call the [ioctl VIDIOC_PREPARE_BUF](vidioc-prepare-buf.md#vidioc-prepare-buf) ioctl to
pass ownership of the buffer to the driver before actually enqueuing it,
using the [VIDIOC_QBUF](vidioc-qbuf.md#vidioc-qbuf) ioctl, and to prepare it for future I/O. Such
preparations may include cache invalidation or cleaning. Performing them
in advance saves time during the actual I/O.

The struct [`v4l2_buffer`](buffer.md#c.V4L.v4l2_buffer "v4l2_buffer") structure is specified in
[Buffers](buffer.md#buffer).

## 7.45.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EBUSY
:   File I/O is in progress.

EINVAL
:   The buffer `type` is not supported, or the `index` is out of
    bounds, or no buffers have been allocated yet, or the `userptr` or
    `length` are invalid.

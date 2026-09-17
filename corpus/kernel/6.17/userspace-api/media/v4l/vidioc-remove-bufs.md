---
collection: kernel
version: "6.17"
title: "7.53. ioctl VIDIOC_REMOVE_BUFS"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/media/v4l/vidioc-remove-bufs.html
fetched_at: 2026-09-16T16:30:12+00:00
---
# 7.53. ioctl VIDIOC_REMOVE_BUFS

## 7.53.1. Name

VIDIOC_REMOVE_BUFS - Removes buffers from a queue

## 7.53.2. Synopsis

VIDIOC_REMOVE_BUFS

`int ioctl(int fd, VIDIOC_REMOVE_BUFS, struct v4l2_remove_buffers *argp)`

## 7.53.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_remove_buffers`](vidioc-remove-bufs.md#c.V4L.v4l2_remove_buffers "v4l2_remove_buffers").

## 7.53.4. Description

Applications can optionally call the [ioctl VIDIOC_REMOVE_BUFS](vidioc-remove-bufs.md#vidioc-remove-bufs) ioctl to
remove buffers from a queue.
[ioctl VIDIOC_CREATE_BUFS](vidioc-create-bufs.md#vidioc-create-bufs) ioctl support is mandatory to enable [ioctl VIDIOC_REMOVE_BUFS](vidioc-remove-bufs.md#vidioc-remove-bufs).
This ioctl is available if the `V4L2_BUF_CAP_SUPPORTS_REMOVE_BUFS` capability
is set on the queue when [`VIDIOC_REQBUFS()`](vidioc-reqbufs.md#c.V4L.VIDIOC_REQBUFS "VIDIOC_REQBUFS") or [`VIDIOC_CREATE_BUFS()`](vidioc-create-bufs.md#c.V4L.VIDIOC_CREATE_BUFS "VIDIOC_CREATE_BUFS")
are invoked.

type v4l2_remove_buffers

struct v4l2_remove_buffers

|  |  |  |
| --- | --- | --- |
| __u32 | `index` | The starting buffer index to remove. This field is ignored if count == 0. |
| __u32 | `count` | The number of buffers to be removed with indices ‘index’ until ‘index + count - 1’. All buffers in this range must be valid and in DEQUEUED state. [ioctl VIDIOC_REMOVE_BUFS](vidioc-remove-bufs.md#vidioc-remove-bufs) will always check the validity of ``` type`, if it is invalid it returns ``EINVAL ``` error code. If count is set to 0 [ioctl VIDIOC_REMOVE_BUFS](vidioc-remove-bufs.md#vidioc-remove-bufs) will do nothing and return 0. |
| __u32 | `type` | Type of the stream or buffers, this is the same as the struct [`v4l2_format`](vidioc-g-fmt.md#c.V4L.v4l2_format "v4l2_format") `type` field. See [`v4l2_buf_type`](buffer.md#c.V4L.v4l2_buf_type "v4l2_buf_type") for valid values. |
| __u32 | `reserved`[13] | A place holder for future extensions. Drivers and applications must set the array to zero. |

## 7.53.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter. If an error occurs, no
buffers will be freed and one of the error codes below will be returned:

EBUSY
:   File I/O is in progress.
    One or more of the buffers in the range `index` to `index + count - 1` are not
    in DEQUEUED state.

EINVAL
:   One or more of the buffers in the range `index` to `index + count - 1` do not
    exist in the queue.
    The buffer type (`type` field) is not valid.

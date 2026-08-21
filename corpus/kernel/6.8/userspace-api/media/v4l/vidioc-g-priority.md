---
collection: kernel
version: "6.8"
title: "7.38. ioctl VIDIOC_G_PRIORITY, VIDIOC_S_PRIORITY"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-g-priority.html
fetched_at: 2026-08-21T03:40:49+00:00
---
# 7.38. ioctl VIDIOC_G_PRIORITY, VIDIOC_S_PRIORITY

## 7.38.1. Name

VIDIOC_G_PRIORITY - VIDIOC_S_PRIORITY - Query or request the access priority associated with a file descriptor

## 7.38.2. Synopsis

VIDIOC_G_PRIORITY

`int ioctl(int fd, VIDIOC_G_PRIORITY, enum v4l2_priority *argp)`

VIDIOC_S_PRIORITY

`int ioctl(int fd, VIDIOC_S_PRIORITY, const enum v4l2_priority *argp)`

## 7.38.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to an enum [`v4l2_priority`](vidioc-g-priority.md#c.V4L.v4l2_priority "v4l2_priority") type.

## 7.38.4. Description

To query the current access priority applications call the
[VIDIOC_G_PRIORITY](vidioc-g-priority.md#vidioc-g-priority) ioctl with a pointer to an [`enum v4l2_priority`](vidioc-g-priority.md#c.V4L.v4l2_priority "V4L.v4l2_priority")
variable where the driver stores the current priority.

To request an access priority applications store the desired priority in
an [`enum v4l2_priority`](vidioc-g-priority.md#c.V4L.v4l2_priority "V4L.v4l2_priority") variable and call [VIDIOC_S_PRIORITY](vidioc-g-priority.md#vidioc-g-priority) ioctl
with a pointer to this variable.

type v4l2_priority

enum v4l2_priority

|  |  |  |
| --- | --- | --- |
| `V4L2_PRIORITY_UNSET` | 0 |  |
| `V4L2_PRIORITY_BACKGROUND` | 1 | Lowest priority, usually applications running in background, for example monitoring VBI transmissions. A proxy application running in user space will be necessary if multiple applications want to read from a device at this priority. |
| `V4L2_PRIORITY_INTERACTIVE` | 2 |  |
| `V4L2_PRIORITY_DEFAULT` | 2 | Medium priority, usually applications started and interactively controlled by the user. For example TV viewers, Teletext browsers, or just "panel" applications to change the channel or video controls. This is the default priority unless an application requests another. |
| `V4L2_PRIORITY_RECORD` | 3 | Highest priority. Only one file descriptor can have this priority, it blocks any other fd from changing device properties. Usually applications which must not be interrupted, like video recording. |

## 7.38.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The requested priority value is invalid.

EBUSY
:   Another application already requested higher priority.

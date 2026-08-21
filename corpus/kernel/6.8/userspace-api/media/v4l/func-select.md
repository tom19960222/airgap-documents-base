---
collection: kernel
version: "6.8"
title: "7.71. V4L2 select()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/func-select.html
fetched_at: 2026-08-21T03:40:27+00:00
---
# 7.71. V4L2 select()

## 7.71.1. Name

v4l2-select - Synchronous I/O multiplexing

## 7.71.2. Synopsis

```c
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
```

int select(int nfds, fd_set \*readfds, fd_set \*writefds, fd_set \*exceptfds, struct timeval \*timeout)

## 7.71.3. Arguments

`nfds`
:   The highest-numbered file descriptor in any of the three sets, plus 1.

`readfds`
:   File descriptions to be watched if a [`read()`](func-read.md#c.V4L.read "V4L.read") call won't block.

`writefds`
:   File descriptions to be watched if a [`write()`](func-write.md#c.V4L.write "V4L.write") won't block.

`exceptfds`
:   File descriptions to be watched for V4L2 events.

`timeout`
:   Maximum time to wait.

## 7.71.4. Description

With the [`select()`](func-select.md#c.V4L.select "select") function applications can suspend
execution until the driver has captured data or is ready to accept data
for output.

When streaming I/O has been negotiated this function waits until a
buffer has been filled or displayed and can be dequeued with the
[VIDIOC_DQBUF](vidioc-qbuf.md#vidioc-qbuf) ioctl. When buffers are already in
the outgoing queue of the driver the function returns immediately.

On success [`select()`](func-select.md#c.V4L.select "select") returns the total number of bits set in
`fd_set`. When the function timed out it returns
a value of zero. On failure it returns -1 and the `errno` variable is
set appropriately. When the application did not call
[ioctl VIDIOC_QBUF, VIDIOC_DQBUF](vidioc-qbuf.md#vidioc-qbuf) or
[ioctl VIDIOC_STREAMON, VIDIOC_STREAMOFF](vidioc-streamon.md#vidioc-streamon) yet the [`select()`](func-select.md#c.V4L.select "select")
function succeeds, setting the bit of the file descriptor in `readfds`
or `writefds`, but subsequent [VIDIOC_DQBUF](vidioc-qbuf.md#vidioc-qbuf)
calls will fail. [1](func-select.md#f1)

When use of the [`read()`](func-read.md#c.V4L.read "read") function has been negotiated and the
driver does not capture yet, the [`select()`](func-select.md#c.V4L.select "select") function starts
capturing. When that fails, [`select()`](func-select.md#c.V4L.select "select") returns successful and
a subsequent [`read()`](func-read.md#c.V4L.read "read") call, which also attempts to start
capturing, will return an appropriate error code. When the driver
captures continuously (as opposed to, for example, still images) and
data is already available the [`select()`](func-select.md#c.V4L.select "select") function returns
immediately.

When use of the [`write()`](func-write.md#c.V4L.write "write") function has been negotiated the
[`select()`](func-select.md#c.V4L.select "select") function just waits until the driver is ready for a
non-blocking [`write()`](func-write.md#c.V4L.write "write") call.

All drivers implementing the [`read()`](func-read.md#c.V4L.read "read") or [`write()`](func-write.md#c.V4L.write "write")
function or streaming I/O must also support the [`select()`](func-select.md#c.V4L.select "select")
function.

For more details see the [`select()`](func-select.md#c.V4L.select "select") manual page.

## 7.71.5. Return Value

On success, [`select()`](func-select.md#c.V4L.select "select") returns the number of descriptors
contained in the three returned descriptor sets, which will be zero if
the timeout expired. On error -1 is returned, and the `errno` variable
is set appropriately; the sets and `timeout` are undefined. Possible
error codes are:

EBADF
:   One or more of the file descriptor sets specified a file descriptor
    that is not open.

EBUSY
:   The driver does not support multiple read or write streams and the
    device is already in use.

EFAULT
:   The `readfds`, `writefds`, `exceptfds` or `timeout` pointer
    references an inaccessible memory area.

EINTR
:   The call was interrupted by a signal.

EINVAL
:   The `nfds` argument is less than zero or greater than
    `FD_SETSIZE`.

[1](func-select.md#id1)
:   The Linux kernel implements [`select()`](func-select.md#c.V4L.select "select") like the
    [`poll()`](func-poll.md#c.V4L.poll "poll") function, but [`select()`](func-select.md#c.V4L.select "select") cannot
    return a `POLLERR`.

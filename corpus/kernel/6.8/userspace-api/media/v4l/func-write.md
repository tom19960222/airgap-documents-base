---
collection: kernel
version: "6.8"
title: "7.72. V4L2 write()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/func-write.html
fetched_at: 2026-08-21T03:41:07+00:00
---
# 7.72. V4L2 write()

## 7.72.1. Name

v4l2-write - Write to a V4L2 device

## 7.72.2. Synopsis

```c
#include <unistd.h>
```

ssize_t write(int fd, void \*buf, size_t count)

## 7.72.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`buf`
:   Buffer with data to be written

`count`
:   Number of bytes at the buffer

## 7.72.4. Description

[`write()`](func-write.md#c.V4L.write "write") writes up to `count` bytes to the device
referenced by the file descriptor `fd` from the buffer starting at
`buf`. When the hardware outputs are not active yet, this function
enables them. When `count` is zero, [`write()`](func-write.md#c.V4L.write "write") returns 0
without any other effect.

When the application does not provide more data in time, the previous
video frame, raw VBI image, sliced VPS or WSS data is displayed again.
Sliced Teletext or Closed Caption data is not repeated, the driver
inserts a blank line instead.

## 7.72.5. Return Value

On success, the number of bytes written are returned. Zero indicates
nothing was written. On error, -1 is returned, and the `errno`
variable is set appropriately. In this case the next write will start at
the beginning of a new frame. Possible error codes are:

EAGAIN
:   Non-blocking I/O has been selected using the
    [O_NONBLOCK](func-open.md#func-open) flag and no buffer space was
    available to write the data immediately.

EBADF
:   `fd` is not a valid file descriptor or is not open for writing.

EBUSY
:   The driver does not support multiple write streams and the device is
    already in use.

EFAULT
:   `buf` references an inaccessible memory area.

EINTR
:   The call was interrupted by a signal before any data was written.

EIO
:   I/O error. This indicates some hardware problem.

EINVAL
:   The [`write()`](func-write.md#c.V4L.write "write") function is not supported by this driver,
    not on this device, or generally not on this type of device.

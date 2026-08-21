---
collection: kernel
version: "6.8"
title: "7.69. V4L2 poll()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/func-poll.html
fetched_at: 2026-08-21T03:40:26+00:00
---
# 7.69. V4L2 poll()

## 7.69.1. Name

v4l2-poll - Wait for some event on a file descriptor

## 7.69.2. Synopsis

```c
#include <sys/poll.h>
```

int poll(struct pollfd \*ufds, unsigned int nfds, int timeout)

## 7.69.3. Arguments

## 7.69.4. Description

With the [`poll()`](func-poll.md#c.V4L.poll "poll") function applications can suspend execution
until the driver has captured data or is ready to accept data for
output.

When streaming I/O has been negotiated this function waits until a
buffer has been filled by the capture device and can be dequeued with
the [VIDIOC_DQBUF](vidioc-qbuf.md#vidioc-qbuf) ioctl. For output devices this
function waits until the device is ready to accept a new buffer to be
queued up with the [VIDIOC_QBUF](vidioc-qbuf.md#vidioc-qbuf) ioctl for
display. When buffers are already in the outgoing queue of the driver
(capture) or the incoming queue isn't full (display) the function
returns immediately.

On success [`poll()`](func-poll.md#c.V4L.poll "poll") returns the number of file descriptors
that have been selected (that is, file descriptors for which the
`revents` field of the respective `struct pollfd` structure
is non-zero). Capture devices set the `POLLIN` and `POLLRDNORM`
flags in the `revents` field, output devices the `POLLOUT` and
`POLLWRNORM` flags. When the function timed out it returns a value of
zero, on failure it returns -1 and the `errno` variable is set
appropriately. When the application did not call
[VIDIOC_STREAMON](vidioc-streamon.md#vidioc-streamon) the [`poll()`](func-poll.md#c.V4L.poll "poll")
function succeeds, but sets the `POLLERR` flag in the `revents`
field. When the application has called
[VIDIOC_STREAMON](vidioc-streamon.md#vidioc-streamon) for a capture device but
hasn't yet called [VIDIOC_QBUF](vidioc-qbuf.md#vidioc-qbuf), the
[`poll()`](func-poll.md#c.V4L.poll "poll") function succeeds and sets the `POLLERR` flag in
the `revents` field. For output devices this same situation will cause
[`poll()`](func-poll.md#c.V4L.poll "poll") to succeed as well, but it sets the `POLLOUT` and
`POLLWRNORM` flags in the `revents` field.

If an event occurred (see [ioctl VIDIOC_DQEVENT](vidioc-dqevent.md#vidioc-dqevent))
then `POLLPRI` will be set in the `revents` field and
[`poll()`](func-poll.md#c.V4L.poll "poll") will return.

When use of the [`read()`](func-read.md#c.V4L.read "read") function has been negotiated and the
driver does not capture yet, the [`poll()`](func-poll.md#c.V4L.poll "poll") function starts
capturing. When that fails it returns a `POLLERR` as above. Otherwise
it waits until data has been captured and can be read. When the driver
captures continuously (as opposed to, for example, still images) the
function may return immediately.

When use of the [`write()`](func-write.md#c.V4L.write "write") function has been negotiated and the
driver does not stream yet, the [`poll()`](func-poll.md#c.V4L.poll "poll") function starts
streaming. When that fails it returns a `POLLERR` as above. Otherwise
it waits until the driver is ready for a non-blocking
[`write()`](func-write.md#c.V4L.write "write") call.

If the caller is only interested in events (just `POLLPRI` is set in
the `events` field), then [`poll()`](func-poll.md#c.V4L.poll "poll") will *not* start
streaming if the driver does not stream yet. This makes it possible to
just poll for events and not for buffers.

All drivers implementing the [`read()`](func-read.md#c.V4L.read "read") or [`write()`](func-write.md#c.V4L.write "write")
function or streaming I/O must also support the [`poll()`](func-poll.md#c.V4L.poll "poll")
function.

For more details see the [`poll()`](func-poll.md#c.V4L.poll "poll") manual page.

## 7.69.5. Return Value

On success, [`poll()`](func-poll.md#c.V4L.poll "poll") returns the number structures which have
non-zero `revents` fields, or zero if the call timed out. On error -1
is returned, and the `errno` variable is set appropriately:

EBADF
:   One or more of the `ufds` members specify an invalid file
    descriptor.

EBUSY
:   The driver does not support multiple read or write streams and the
    device is already in use.

EFAULT
:   `ufds` references an inaccessible memory area.

EINTR
:   The call was interrupted by a signal.

EINVAL
:   The `nfds` value exceeds the `RLIMIT_NOFILE` value. Use
    `getrlimit()` to obtain this value.

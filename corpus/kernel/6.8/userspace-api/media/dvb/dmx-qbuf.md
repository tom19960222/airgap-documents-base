---
collection: kernel
version: "6.8"
title: "3.2.19. ioctl DMX_QBUF, DMX_DQBUF"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-qbuf.html
fetched_at: 2026-08-21T03:39:11+00:00
---
# 3.2.19. ioctl DMX_QBUF, DMX_DQBUF

## 3.2.19.1. Name

DMX_QBUF - DMX_DQBUF - Exchange a buffer with the driver

> **Warning:**
>
> this API is still experimental

## 3.2.19.2. Synopsis

DMX_QBUF

`int ioctl(int fd, DMX_QBUF, struct dmx_buffer *argp)`

DMX_DQBUF

`int ioctl(int fd, DMX_DQBUF, struct dmx_buffer *argp)`

## 3.2.19.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

`argp`
:   Pointer to struct [`dmx_buffer`](dmx_types.md#c.dmx_buffer "dmx_buffer").

## 3.2.19.4. Description

Applications call the `DMX_QBUF` ioctl to enqueue an empty
(capturing) or filled (output) buffer in the driver's incoming queue.
The semantics depend on the selected I/O method.

To enqueue a buffer applications set the `index` field. Valid index
numbers range from zero to the number of buffers allocated with
[ioctl DMX_REQBUFS](dmx-reqbufs.md#dmx-reqbufs) (struct [`dmx_requestbuffers`](dmx_types.md#c.dmx_requestbuffers "dmx_requestbuffers") `count`) minus
one. The contents of the struct [`dmx_buffer`](dmx_types.md#c.dmx_buffer "dmx_buffer") returned
by a [ioctl DMX_QUERYBUF](dmx-querybuf.md#dmx-querybuf) ioctl will do as well.

When `DMX_QBUF` is called with a pointer to this structure, it locks the
memory pages of the buffer in physical memory, so they cannot be swapped
out to disk. Buffers remain locked until dequeued, until the
device is closed.

Applications call the `DMX_DQBUF` ioctl to dequeue a filled
(capturing) buffer from the driver's outgoing queue.
They just set the `index` field with the buffer ID to be queued.
When `DMX_DQBUF` is called with a pointer to struct [`dmx_buffer`](dmx_types.md#c.dmx_buffer "dmx_buffer"),
the driver fills the remaining fields or returns an error code.

By default `DMX_DQBUF` blocks when no buffer is in the outgoing
queue. When the `O_NONBLOCK` flag was given to the
[`open()`](dmx-fopen.md#c.DTV.dmx.open "open") function, `DMX_DQBUF` returns
immediately with an `EAGAIN` error code when no buffer is available.

The struct [`dmx_buffer`](dmx_types.md#c.dmx_buffer "dmx_buffer") structure is specified in
[Buffers](../v4l/buffer.md#buffer).

## 3.2.19.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EAGAIN
:   Non-blocking I/O has been selected using `O_NONBLOCK` and no
    buffer was in the outgoing queue.

EINVAL
:   The `index` is out of bounds, or no buffers have been allocated yet.

EIO
:   `DMX_DQBUF` failed due to an internal error. Can also indicate
    temporary problems like signal loss or CRC errors.

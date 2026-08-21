---
collection: kernel
version: "6.8"
title: "3.2.17. ioctl DMX_QUERYBUF"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-querybuf.html
fetched_at: 2026-08-21T03:39:14+00:00
---
# 3.2.17. ioctl DMX_QUERYBUF

## 3.2.17.1. Name

DMX_QUERYBUF - Query the status of a buffer

> **Warning:**
>
> this API is still experimental

## 3.2.17.2. Synopsis

DMX_QUERYBUF

`int ioctl(int fd, DMX_QUERYBUF, struct dvb_buffer *argp)`

## 3.2.17.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

`argp`
:   Pointer to struct [`dvb_buffer`](../../../driver-api/media/dtv-common.md#c.dvb_buffer "dvb_buffer").

## 3.2.17.4. Description

This ioctl is part of the mmap streaming I/O method. It can
be used to query the status of a buffer at any time after buffers have
been allocated with the [ioctl DMX_REQBUFS](dmx-reqbufs.md#dmx-reqbufs) ioctl.

Applications set the `index` field. Valid index numbers range from zero
to the number of buffers allocated with [ioctl DMX_REQBUFS](dmx-reqbufs.md#dmx-reqbufs)
(struct `dvb_requestbuffers` `count`) minus one.

After calling [ioctl DMX_QUERYBUF](dmx-querybuf.md#dmx-querybuf) with a pointer to this structure,
drivers return an error code or fill the rest of the structure.

On success, the `offset` will contain the offset of the buffer from the
start of the device memory, the `length` field its size, and the
`bytesused` the number of bytes occupied by data in the buffer (payload).

## 3.2.17.5. Return Value

On success 0 is returned, the `offset` will contain the offset of the
buffer from the start of the device memory, the `length` field its size,
and the `bytesused` the number of bytes occupied by data in the buffer
(payload).

On error it returns -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The `index` is out of bounds.

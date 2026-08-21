---
collection: kernel
version: "6.8"
title: "3.2.16. ioctl DMX_REQBUFS"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-reqbufs.html
fetched_at: 2026-08-21T03:39:15+00:00
---
# 3.2.16. ioctl DMX_REQBUFS

## 3.2.16.1. Name

DMX_REQBUFS - Initiate Memory Mapping and/or DMA buffer I/O

> **Warning:**
>
> this API is still experimental

## 3.2.16.2. Synopsis

DMX_REQBUFS

`int ioctl(int fd, DMX_REQBUFS, struct dmx_requestbuffers *argp)`

## 3.2.16.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

`argp`
:   Pointer to struct [`dmx_requestbuffers`](dmx_types.md#c.dmx_requestbuffers "dmx_requestbuffers").

## 3.2.16.4. Description

This ioctl is used to initiate a memory mapped or DMABUF based demux I/O.

Memory mapped buffers are located in device memory and must be allocated
with this ioctl before they can be mapped into the application's address
space. User buffers are allocated by applications themselves, and this
ioctl is merely used to switch the driver into user pointer I/O mode and
to setup some internal structures. Similarly, DMABUF buffers are
allocated by applications through a device driver, and this ioctl only
configures the driver into DMABUF I/O mode without performing any direct
allocation.

To allocate device buffers applications initialize all fields of the
struct [`dmx_requestbuffers`](dmx_types.md#c.dmx_requestbuffers "dmx_requestbuffers") structure. They set the `count` field
to the desired number of buffers, and `size` to the size of each
buffer.

When the ioctl is called with a pointer to this structure, the driver will
attempt to allocate the requested number of buffers and it stores the actual
number allocated in the `count` field. The `count` can be smaller than the number requested, even zero, when the driver runs out of free memory. A larger
number is also possible when the driver requires more buffers to
function correctly. The actual allocated buffer size can is returned
at `size`, and can be smaller than what's requested.

When this I/O method is not supported, the ioctl returns an `EOPNOTSUPP`
error code.

Applications can call [ioctl DMX_REQBUFS](dmx-reqbufs.md#dmx-reqbufs) again to change the number of
buffers, however this cannot succeed when any buffers are still mapped.
A `count` value of zero frees all buffers, after aborting or finishing
any DMA in progress.

## 3.2.16.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EOPNOTSUPP
:   The the requested I/O method is not supported.

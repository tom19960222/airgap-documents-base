---
collection: kernel
version: "6.8"
title: "3.2.18. ioctl DMX_EXPBUF"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-expbuf.html
fetched_at: 2026-08-21T03:39:12+00:00
---
# 3.2.18. ioctl DMX_EXPBUF

## 3.2.18.1. Name

DMX_EXPBUF - Export a buffer as a DMABUF file descriptor.

> **Warning:**
>
> this API is still experimental

## 3.2.18.2. Synopsis

DMX_EXPBUF

`int ioctl(int fd, DMX_EXPBUF, struct dmx_exportbuffer *argp)`

## 3.2.18.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

`argp`
:   Pointer to struct [`dmx_exportbuffer`](dmx_types.md#c.dmx_exportbuffer "dmx_exportbuffer").

## 3.2.18.4. Description

This ioctl is an extension to the memory mapping I/O method.
It can be used to export a buffer as a DMABUF file at any time after
buffers have been allocated with the [ioctl DMX_REQBUFS](dmx-reqbufs.md#dmx-reqbufs) ioctl.

To export a buffer, applications fill struct [`dmx_exportbuffer`](dmx_types.md#c.dmx_exportbuffer "dmx_exportbuffer").
Applications must set the `index` field. Valid index numbers
range from zero to the number of buffers allocated with [ioctl DMX_REQBUFS](dmx-reqbufs.md#dmx-reqbufs)
(struct [`dmx_requestbuffers`](dmx_types.md#c.dmx_requestbuffers "dmx_requestbuffers") `count`) minus one.
Additional flags may be posted in the `flags` field. Refer to a manual
for [`open()`](dmx-fopen.md#c.DTV.dmx.open "DTV.dmx.open") for details. Currently only O_CLOEXEC, O_RDONLY, O_WRONLY,
and O_RDWR are supported.
All other fields must be set to zero. In the
case of multi-planar API, every plane is exported separately using
multiple [ioctl DMX_EXPBUF](dmx-expbuf.md#dmx-expbuf) calls.

After calling [ioctl DMX_EXPBUF](dmx-expbuf.md#dmx-expbuf) the `fd` field will be set by a
driver, on success. This is a DMABUF file descriptor. The application may
pass it to other DMABUF-aware devices. It is recommended to close a DMABUF
file when it is no longer used to allow the associated memory to be reclaimed.

## 3.2.18.5. Examples

```c
int buffer_export(int v4lfd, enum dmx_buf_type bt, int index, int *dmafd)
{
    struct dmx_exportbuffer expbuf;

    memset(&expbuf, 0, sizeof(expbuf));
    expbuf.type = bt;
    expbuf.index = index;
    if (ioctl(v4lfd, DMX_EXPBUF, &expbuf) == -1) {
        perror("DMX_EXPBUF");
        return -1;
    }

    *dmafd = expbuf.fd;

    return 0;
}
```

## 3.2.18.6. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   A queue is not in MMAP mode or DMABUF exporting is not supported or
    `flags` or `index` fields are invalid.

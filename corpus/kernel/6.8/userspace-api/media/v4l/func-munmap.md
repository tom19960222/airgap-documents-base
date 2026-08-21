---
collection: kernel
version: "6.8"
title: "7.67. V4L2 munmap()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/func-munmap.html
fetched_at: 2026-08-21T03:40:25+00:00
---
# 7.67. V4L2 munmap()

## 7.67.1. Name

v4l2-munmap - Unmap device memory

## 7.67.2. Synopsis

```c
#include <unistd.h>
#include <sys/mman.h>
```

int munmap(void \*start, size_t length)

## 7.67.3. Arguments

`start`
:   Address of the mapped buffer as returned by the
    [`mmap()`](func-mmap.md#c.V4L.mmap "mmap") function.

`length`
:   Length of the mapped buffer. This must be the same value as given to
    [`mmap()`](func-mmap.md#c.V4L.mmap "mmap") and returned by the driver in the struct
    [`v4l2_buffer`](buffer.md#c.V4L.v4l2_buffer "v4l2_buffer") `length` field for the
    single-planar API and in the struct
    [`v4l2_plane`](buffer.md#c.V4L.v4l2_plane "v4l2_plane") `length` field for the
    multi-planar API.

## 7.67.4. Description

Unmaps a previously with the [`mmap()`](func-mmap.md#c.V4L.mmap "mmap") function mapped
buffer and frees it, if possible.

## 7.67.5. Return Value

On success [`munmap()`](func-munmap.md#c.V4L.munmap "munmap") returns 0, on failure -1 and the
`errno` variable is set appropriately:

EINVAL
:   The `start` or `length` is incorrect, or no buffers have been
    mapped yet.

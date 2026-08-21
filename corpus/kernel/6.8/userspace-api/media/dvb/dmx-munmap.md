---
collection: kernel
version: "6.8"
title: "3.2.6. DVB munmap()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-munmap.html
fetched_at: 2026-08-21T03:39:19+00:00
---
# 3.2.6. DVB munmap()

## 3.2.6.1. Name

dmx-munmap - Unmap device memory

> **Warning:**
>
> This API is still experimental.

## 3.2.6.2. Synopsis

```c
#include <unistd.h>
#include <sys/mman.h>
```

int munmap(void \*start, size_t length)

## 3.2.6.3. Arguments

`start`
:   Address of the mapped buffer as returned by the
    [`mmap()`](dmx-mmap.md#c.DTV.dmx.mmap "mmap") function.

`length`
:   Length of the mapped buffer. This must be the same value as given to
    [`mmap()`](dmx-mmap.md#c.DTV.dmx.mmap "mmap").

## 3.2.6.4. Description

Unmaps a previously with the [`mmap()`](dmx-mmap.md#c.DTV.dmx.mmap "mmap") function mapped
buffer and frees it, if possible.

## 3.2.6.5. Return Value

On success [`munmap()`](dmx-munmap.md#c.DTV.dmx.munmap "munmap") returns 0, on failure -1 and the
`errno` variable is set appropriately:

EINVAL
:   The `start` or `length` is incorrect, or no buffers have been
    mapped yet.

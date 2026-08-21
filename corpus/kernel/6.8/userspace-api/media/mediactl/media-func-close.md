---
collection: kernel
version: "6.8"
title: "5.2. media close()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/mediactl/media-func-close.html
fetched_at: 2026-08-21T03:39:54+00:00
---
# 5.2. media close()

## 5.2.1. Name

media-close - Close a media device

## 5.2.2. Synopsis

```c
#include <unistd.h>
```

int close(int fd)

## 5.2.3. Arguments

`fd`
:   File descriptor returned by [`open()`](media-func-open.md#c.MC.open "open").

## 5.2.4. Description

Closes the media device. Resources associated with the file descriptor
are freed. The device configuration remain unchanged.

## 5.2.5. Return Value

[`close()`](media-func-close.md#c.MC.close "close") returns 0 on success. On error, -1 is returned, and
`errno` is set appropriately. Possible error codes are:

EBADF
:   `fd` is not a valid open file descriptor.

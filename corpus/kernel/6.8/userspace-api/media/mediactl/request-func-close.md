---
collection: kernel
version: "6.8"
title: "5.10. request close()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/mediactl/request-func-close.html
fetched_at: 2026-08-21T03:40:01+00:00
---
# 5.10. request close()

## 5.10.1. Name

request-close - Close a request file descriptor

## 5.10.2. Synopsis

```c
#include <unistd.h>
```

int close(int fd)

## 5.10.3. Arguments

`fd`
:   File descriptor returned by [ioctl MEDIA_IOC_REQUEST_ALLOC](media-ioc-request-alloc.md#media-ioc-request-alloc).

## 5.10.4. Description

Closes the request file descriptor. Resources associated with the request
are freed once all file descriptors associated with the request are closed
and the driver has completed the request.
See [here](request-api.md#media-request-life-time) for more information.

## 5.10.5. Return Value

[`close()`](request-func-close.md#c.MC.request.close "close") returns 0 on success. On error, -1 is
returned, and `errno` is set appropriately. Possible error codes are:

EBADF
:   `fd` is not a valid open file descriptor.

---
collection: kernel
version: "6.8"
title: "2.2. cec close()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/cec/cec-func-close.html
fetched_at: 2026-08-21T03:38:50+00:00
---
# 2.2. cec close()

## 2.2.1. Name

cec-close - Close a cec device

## 2.2.2. Synopsis

```c
#include <unistd.h>
```

int close(int fd)

## 2.2.3. Arguments

`fd`
:   File descriptor returned by [`open()`](cec-func-open.md#c.CEC.open "open").

## 2.2.4. Description

Closes the cec device. Resources associated with the file descriptor are
freed. The device configuration remain unchanged.

## 2.2.5. Return Value

[`close()`](cec-func-close.md#c.CEC.close "close") returns 0 on success. On error, -1 is returned, and
`errno` is set appropriately. Possible error codes are:

`EBADF`
:   `fd` is not a valid open file descriptor.

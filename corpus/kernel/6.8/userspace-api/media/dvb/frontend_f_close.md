---
collection: kernel
version: "6.8"
title: "2.4.2. Digital TV frontend close()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/frontend_f_close.html
fetched_at: 2026-08-21T03:39:21+00:00
---
# 2.4.2. Digital TV frontend close()

## 2.4.2.1. Name

fe-close - Close a frontend device

## 2.4.2.2. Synopsis

```c
#include <unistd.h>
```

int close(int fd)

## 2.4.2.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

## 2.4.2.4. Description

This system call closes a previously opened front-end device. After
closing a front-end device, its corresponding hardware might be powered
down automatically.

## 2.4.2.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

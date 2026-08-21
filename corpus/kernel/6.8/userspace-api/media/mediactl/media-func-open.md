---
collection: kernel
version: "6.8"
title: "5.1. media open()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/mediactl/media-func-open.html
fetched_at: 2026-08-21T03:40:00+00:00
---
# 5.1. media open()

## 5.1.1. Name

media-open - Open a media device

## 5.1.2. Synopsis

```c
#include <fcntl.h>
```

int open(const char \*device_name, int flags)

## 5.1.3. Arguments

`device_name`
:   Device to be opened.

`flags`
:   Open flags. Access mode must be either `O_RDONLY` or `O_RDWR`.
    Other flags have no effect.

## 5.1.4. Description

To open a media device applications call [`open()`](media-func-open.md#c.MC.open "open") with the
desired device name. The function has no side effects; the device
configuration remain unchanged.

When the device is opened in read-only mode, attempts to modify its
configuration will result in an error, and `errno` will be set to
EBADF.

## 5.1.5. Return Value

[`open()`](media-func-open.md#c.MC.open "open") returns the new file descriptor on success. On error,
-1 is returned, and `errno` is set appropriately. Possible error codes
are:

EACCES
:   The requested access to the file is not allowed.

EMFILE
:   The process already has the maximum number of files open.

ENFILE
:   The system limit on the total number of open files has been reached.

ENOMEM
:   Insufficient kernel memory was available.

ENXIO
:   No device corresponding to this device special file exists.

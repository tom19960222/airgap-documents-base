---
collection: kernel
version: "6.8"
title: "2.4.1. Digital TV frontend open()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/frontend_f_open.html
fetched_at: 2026-08-21T03:39:33+00:00
---
# 2.4.1. Digital TV frontend open()

## 2.4.1.1. Name

fe-open - Open a frontend device

## 2.4.1.2. Synopsis

```c
#include <fcntl.h>
```

int open(const char \*device_name, int flags)

## 2.4.1.3. Arguments

`device_name`
:   Device to be opened.

`flags`
:   Open flags. Access can either be `O_RDWR` or `O_RDONLY`.

    Multiple opens are allowed with `O_RDONLY`. In this mode, only
    query and read ioctls are allowed.

    Only one open is allowed in `O_RDWR`. In this mode, all ioctls are
    allowed.

    When the `O_NONBLOCK` flag is given, the system calls may return
    `EAGAIN` error code when no data is available or when the device
    driver is temporarily busy.

    Other flags have no effect.

## 2.4.1.4. Description

This system call opens a named frontend device
(`/dev/dvb/adapter?/frontend?`) for subsequent use. Usually the first
thing to do after a successful open is to find out the frontend type
with [ioctl FE_GET_INFO](fe-get-info.md#fe-get-info).

The device can be opened in read-only mode, which only allows monitoring
of device status and statistics, or read/write mode, which allows any
kind of use (e.g. performing tuning operations.)

In a system with multiple front-ends, it is usually the case that
multiple devices cannot be open in read/write mode simultaneously. As
long as a front-end device is opened in read/write mode, other [`open()`](frontend_f_open.md#c.DTV.fe.open "DTV.fe.open")
calls in read/write mode will either fail or block, depending on whether
non-blocking or blocking mode was specified. A front-end device opened
in blocking mode can later be put into non-blocking mode (and vice
versa) using the F_SETFL command of the fcntl system call. This is a
standard system call, documented in the Linux manual page for fcntl.
When an [`open()`](frontend_f_open.md#c.DTV.fe.open "DTV.fe.open") call has succeeded, the device will be ready for use in
the specified mode. This implies that the corresponding hardware is
powered up, and that other front-ends may have been powered down to make
that possible.

## 2.4.1.5. Return Value

On success [`open()`](frontend_f_open.md#c.DTV.fe.open "open") returns the new file descriptor.
On error, -1 is returned, and the `errno` variable is set appropriately.

Possible error codes are:

On success 0 is returned, and [`ca_slot_info`](ca_data_types.md#c.ca_slot_info "ca_slot_info") is filled.

On error -1 is returned, and the `errno` variable is set
appropriately.

|  |  |
| --- | --- |
| `EPERM` | The caller has no permission to access the device. |
| `EBUSY` | The the device driver is already in use. |
| `EMFILE` | The process already has the maximum number of files open. |
| `ENFILE` | The limit on the total number of files open on the system has been reached. |

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

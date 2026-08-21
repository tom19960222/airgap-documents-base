---
collection: kernel
version: "6.8"
title: "2.4.4. ioctl FE_READ_STATUS"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-read-status.html
fetched_at: 2026-08-21T03:39:30+00:00
---
# 2.4.4. ioctl FE_READ_STATUS

## 2.4.4.1. Name

FE_READ_STATUS - Returns status information about the front-end. This call only requires - read-only access to the device

## 2.4.4.2. Synopsis

FE_READ_STATUS

`int ioctl(int fd, FE_READ_STATUS, unsigned int *status)`

## 2.4.4.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`status`
:   pointer to a bitmask integer filled with the values defined by enum
    [`fe_status`](frontend-header.md#c.fe_status "fe_status").

## 2.4.4.4. Description

All Digital TV frontend devices support the `FE_READ_STATUS` ioctl. It is
used to check about the locking status of the frontend after being
tuned. The ioctl takes a pointer to an integer where the status will be
written.

> **Note:**
>
> The size of status is actually sizeof([`enum fe_status`](frontend-header.md#c.fe_status "fe_status")), with
> varies according with the architecture. This needs to be fixed in the
> future.

## 2.4.4.5. int fe_status

The fe_status parameter is used to indicate the current state and/or
state changes of the frontend hardware. It is produced using the enum
[`fe_status`](frontend-header.md#c.fe_status "fe_status") values on a bitmask

## 2.4.4.6. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

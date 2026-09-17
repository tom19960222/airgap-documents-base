---
collection: kernel
version: "6.17"
title: "2.4.6. ioctl FE_DISEQC_RESET_OVERLOAD"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/media/dvb/fe-diseqc-reset-overload.html
fetched_at: 2026-09-16T16:28:07+00:00
---
# 2.4.6. ioctl FE_DISEQC_RESET_OVERLOAD

## 2.4.6.1. Name

FE_DISEQC_RESET_OVERLOAD - Restores the power to the antenna subsystem, if it was powered off due - to power overload.

## 2.4.6.2. Synopsis

FE_DISEQC_RESET_OVERLOAD

`int ioctl(int fd, FE_DISEQC_RESET_OVERLOAD, NULL)`

## 2.4.6.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

## 2.4.6.4. Description

If the bus has been automatically powered off due to power overload,
this ioctl call restores the power to the bus. The call requires
read/write access to the device. This call has no effect if the device
is manually powered off. Not all Digital TV adapters support this ioctl.

## 2.4.6.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

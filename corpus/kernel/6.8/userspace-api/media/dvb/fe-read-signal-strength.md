---
collection: kernel
version: "6.8"
title: "6.1.2.3. FE_READ_SIGNAL_STRENGTH"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-read-signal-strength.html
fetched_at: 2026-08-21T03:39:28+00:00
---
# 6.1.2.3. FE_READ_SIGNAL_STRENGTH

## 6.1.2.3.1. Name

FE_READ_SIGNAL_STRENGTH

> **Attention:**
>
> This ioctl is deprecated.

## 6.1.2.3.2. Synopsis

FE_READ_SIGNAL_STRENGTH

`int ioctl(int fd, FE_READ_SIGNAL_STRENGTH, uint16_t *strength)`

## 6.1.2.3.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`strength`
:   The signal strength value is stored into \*strength.

## 6.1.2.3.4. Description

This ioctl call returns the signal strength value for the signal
currently received by the front-end. For this command, read-only access
to the device is sufficient.

## 6.1.2.3.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

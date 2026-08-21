---
collection: kernel
version: "6.8"
title: "6.1.2.4. FE_READ_UNCORRECTED_BLOCKS"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-read-uncorrected-blocks.html
fetched_at: 2026-08-21T03:39:30+00:00
---
# 6.1.2.4. FE_READ_UNCORRECTED_BLOCKS

## 6.1.2.4.1. Name

FE_READ_UNCORRECTED_BLOCKS

> **Attention:**
>
> This ioctl is deprecated.

## 6.1.2.4.2. Synopsis

FE_READ_UNCORRECTED_BLOCKS

`int ioctl(int fd, FE_READ_UNCORRECTED_BLOCKS, uint32_t *ublocks)`

## 6.1.2.4.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`ublocks`
:   The total number of uncorrected blocks seen by the driver so far.

## 6.1.2.4.4. Description

This ioctl call returns the number of uncorrected blocks detected by the
device driver during its lifetime. For meaningful measurements, the
increment in block count during a specific time interval should be
calculated. For this command, read-only access to the device is
sufficient.

## 6.1.2.4.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

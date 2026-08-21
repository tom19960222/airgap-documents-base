---
collection: kernel
version: "6.8"
title: "6.5.6. ioctl LIRC_GET_REC_RESOLUTION"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-get-rec-resolution.html
fetched_at: 2026-08-21T03:40:08+00:00
---
# 6.5.6. ioctl LIRC_GET_REC_RESOLUTION

## 6.5.6.1. Name

LIRC_GET_REC_RESOLUTION - Obtain the value of receive resolution, in microseconds.

## 6.5.6.2. Synopsis

LIRC_GET_REC_RESOLUTION

`int ioctl(int fd, LIRC_GET_REC_RESOLUTION, __u32 *microseconds)`

## 6.5.6.3. Arguments

`fd`
:   File descriptor returned by open().

`microseconds`
:   Resolution, in microseconds.

## 6.5.6.4. Description

Some receivers have maximum resolution which is defined by internal
sample rate or data format limitations. E.g. it's common that
signals can only be reported in 50 microsecond steps.

This ioctl returns the integer value with such resolution, with can be
used by userspace applications like lircd to automatically adjust the
tolerance value.

## 6.5.6.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

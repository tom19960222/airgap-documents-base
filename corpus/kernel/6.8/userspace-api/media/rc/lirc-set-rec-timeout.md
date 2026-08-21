---
collection: kernel
version: "6.8"
title: "6.5.9. ioctl LIRC_GET_REC_TIMEOUT and LIRC_SET_REC_TIMEOUT"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-set-rec-timeout.html
fetched_at: 2026-08-21T03:40:09+00:00
---
# 6.5.9. ioctl LIRC_GET_REC_TIMEOUT and LIRC_SET_REC_TIMEOUT

## 6.5.9.1. Name

LIRC_GET_REC_TIMEOUT/LIRC_SET_REC_TIMEOUT - Get/set the integer value for IR inactivity timeout.

## 6.5.9.2. Synopsis

LIRC_GET_REC_TIMEOUT

`int ioctl(int fd, LIRC_GET_REC_TIMEOUT, __u32 *timeout)`

LIRC_SET_REC_TIMEOUT

`int ioctl(int fd, LIRC_SET_REC_TIMEOUT, __u32 *timeout)`

## 6.5.9.3. Arguments

`fd`
:   File descriptor returned by open().

`timeout`
:   Timeout, in microseconds.

## 6.5.9.4. Description

Get and set the integer value for IR inactivity timeout.

If supported by the hardware, setting it to 0 disables all hardware timeouts
and data should be reported as soon as possible. If the exact value
cannot be set, then the next possible value _greater_ than the
given value should be set.

> **Note:**
>
> The range of supported timeout is given by [ioctls LIRC_GET_MIN_TIMEOUT and LIRC_GET_MAX_TIMEOUT](lirc-get-timeout.md#lirc-get-min-timeout).

## 6.5.9.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

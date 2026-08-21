---
collection: kernel
version: "6.8"
title: "6.5.8. ioctls LIRC_GET_MIN_TIMEOUT and LIRC_GET_MAX_TIMEOUT"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-get-timeout.html
fetched_at: 2026-08-21T03:40:07+00:00
---
# 6.5.8. ioctls LIRC_GET_MIN_TIMEOUT and LIRC_GET_MAX_TIMEOUT

## 6.5.8.1. Name

LIRC_GET_MIN_TIMEOUT / LIRC_GET_MAX_TIMEOUT - Obtain the possible timeout
range for IR receive.

## 6.5.8.2. Synopsis

LIRC_GET_MIN_TIMEOUT

`int ioctl(int fd, LIRC_GET_MIN_TIMEOUT, __u32 *timeout)`

LIRC_GET_MAX_TIMEOUT

`int ioctl(int fd, LIRC_GET_MAX_TIMEOUT, __u32 *timeout)`

## 6.5.8.3. Arguments

`fd`
:   File descriptor returned by open().

`timeout`
:   Timeout, in microseconds.

## 6.5.8.4. Description

Some devices have internal timers that can be used to detect when
there's no IR activity for a long time. This can help lircd in
detecting that a IR signal is finished and can speed up the decoding
process. Returns an integer value with the minimum/maximum timeout
that can be set.

> **Note:**
>
> Some devices have a fixed timeout, in that case
> both ioctls will return the same value even though the timeout
> cannot be changed via [ioctl LIRC_GET_REC_TIMEOUT and LIRC_SET_REC_TIMEOUT](lirc-set-rec-timeout.md#lirc-set-rec-timeout).

## 6.5.8.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

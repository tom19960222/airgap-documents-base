---
collection: kernel
version: "6.17"
title: "GPIO_GET_LINEINFO_UNWATCH_IOCTL"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/gpio/gpio-get-lineinfo-unwatch-ioctl.html
fetched_at: 2026-09-16T16:28:41+00:00
---
# GPIO_GET_LINEINFO_UNWATCH_IOCTL

## Name

GPIO_GET_LINEINFO_UNWATCH_IOCTL - Disable watching a line for changes to its
requested state and configuration information.

## Synopsis

GPIO_GET_LINEINFO_UNWATCH_IOCTL

`int ioctl(int chip_fd, GPIO_GET_LINEINFO_UNWATCH_IOCTL, u32 *offset)`

## Arguments

`chip_fd`
:   The file descriptor of the GPIO character device returned by open().

`offset`
:   The offset of the line to no longer watch.

## Description

Remove the line from the list of lines being watched on this `chip_fd`.

This is the reverse of [GPIO_V2_GET_LINEINFO_WATCH_IOCTL](gpio-v2-get-lineinfo-watch-ioctl.md) (v2) and
[GPIO_GET_LINEINFO_WATCH_IOCTL](gpio-get-lineinfo-watch-ioctl.md) (v1).

Unwatching a line that is not watched is an error (**EBUSY**).

First added in 5.7.

## Return Value

On success 0.

On error -1 and the `errno` variable is set appropriately.
Common error codes are described in [GPIO Error Codes](error-codes.md).

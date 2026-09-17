---
collection: kernel
version: "6.17"
title: "GPIO_GET_LINEINFO_IOCTL"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/gpio/gpio-get-lineinfo-ioctl.html
fetched_at: 2026-09-16T16:28:41+00:00
---
# GPIO_GET_LINEINFO_IOCTL

> **Warning:**
>
> This ioctl is part of [GPIO Character Device Userspace API (v1)](chardev_v1.md) and is obsoleted by
> [GPIO_V2_GET_LINEINFO_IOCTL](gpio-v2-get-lineinfo-ioctl.md).

## Name

GPIO_GET_LINEINFO_IOCTL - Get the publicly available information for a line.

## Synopsis

GPIO_GET_LINEINFO_IOCTL

`int ioctl(int chip_fd, GPIO_GET_LINEINFO_IOCTL, struct gpioline_info *info)`

## Arguments

`chip_fd`
:   The file descriptor of the GPIO character device returned by open().

`info`
:   The [`line_info`](chardev_v1.md#c.gpioline_info "gpioline_info") to be populated, with the
    `offset` field set to indicate the line to be collected.

## Description

Get the publicly available information for a line.

This information is available independent of whether the line is in use.

> **Note:**
>
> The line info does not include the line value.
>
> The line must be requested using [GPIO_GET_LINEHANDLE_IOCTL](gpio-get-linehandle-ioctl.md) or
> [GPIO_GET_LINEEVENT_IOCTL](gpio-get-lineevent-ioctl.md) to access its value.

## Return Value

On success 0 and `info` is populated with the chip info.

On error -1 and the `errno` variable is set appropriately.
Common error codes are described in [GPIO Error Codes](error-codes.md).

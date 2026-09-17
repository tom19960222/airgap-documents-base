---
collection: kernel
version: "6.17"
title: "GPIO_V2_GET_LINEINFO_IOCTL"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/gpio/gpio-v2-get-lineinfo-ioctl.html
fetched_at: 2026-09-16T16:28:44+00:00
---
# GPIO_V2_GET_LINEINFO_IOCTL

## Name

GPIO_V2_GET_LINEINFO_IOCTL - Get the publicly available information for a line.

## Synopsis

GPIO_V2_GET_LINEINFO_IOCTL

`int ioctl(int chip_fd, GPIO_V2_GET_LINEINFO_IOCTL, struct gpio_v2_line_info *info)`

## Arguments

`chip_fd`
:   The file descriptor of the GPIO character device returned by open().

`info`
:   The [`line_info`](chardev.md#c.gpio_v2_line_info "gpio_v2_line_info") to be populated, with the
    `offset` field set to indicate the line to be collected.

## Description

Get the publicly available information for a line.

This information is available independent of whether the line is in use.

> **Note:**
>
> The line info does not include the line value.
>
> The line must be requested using [GPIO_V2_GET_LINE_IOCTL](gpio-v2-get-line-ioctl.md) to access its
> value.

## Return Value

On success 0 and `info` is populated with the chip info.

On error -1 and the `errno` variable is set appropriately.
Common error codes are described in [GPIO Error Codes](error-codes.md).

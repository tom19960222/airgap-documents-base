---
collection: kernel
version: "6.17"
title: "GPIO_GET_CHIPINFO_IOCTL"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/gpio/gpio-get-chipinfo-ioctl.html
fetched_at: 2026-09-16T16:28:39+00:00
---
# GPIO_GET_CHIPINFO_IOCTL

## Name

GPIO_GET_CHIPINFO_IOCTL - Get the publicly available information for a chip.

## Synopsis

GPIO_GET_CHIPINFO_IOCTL

`int ioctl(int chip_fd, GPIO_GET_CHIPINFO_IOCTL, struct gpiochip_info *info)`

## Arguments

`chip_fd`
:   The file descriptor of the GPIO character device returned by open().

`info`
:   The [`chip_info`](chardev.md#c.gpiochip_info "gpiochip_info") to be populated.

## Description

Gets the publicly available information for a particular GPIO chip.

## Return Value

On success 0 and `info` is populated with the chip info.

On error -1 and the `errno` variable is set appropriately.
Common error codes are described in [GPIO Error Codes](error-codes.md).

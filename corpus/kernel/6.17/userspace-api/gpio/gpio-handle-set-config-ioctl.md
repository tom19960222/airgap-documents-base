---
collection: kernel
version: "6.17"
title: "GPIOHANDLE_SET_CONFIG_IOCTL"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/gpio/gpio-handle-set-config-ioctl.html
fetched_at: 2026-09-16T16:28:49+00:00
---
# GPIOHANDLE_SET_CONFIG_IOCTL

> **Warning:**
>
> This ioctl is part of [GPIO Character Device Userspace API (v1)](chardev_v1.md) and is obsoleted by
> [GPIO_V2_LINE_SET_CONFIG_IOCTL](gpio-v2-line-set-config-ioctl.md).

## Name

GPIOHANDLE_SET_CONFIG_IOCTL - Update the configuration of previously requested lines.

## Synopsis

GPIOHANDLE_SET_CONFIG_IOCTL

`int ioctl(int handle_fd, GPIOHANDLE_SET_CONFIG_IOCTL, struct gpiohandle_config *config)`

## Arguments

`handle_fd`
:   The file descriptor of the GPIO character device, as returned in the
    [`request.fd`](chardev_v1.md#c.gpiohandle_request "gpiohandle_request") by [GPIO_GET_LINEHANDLE_IOCTL](gpio-get-linehandle-ioctl.md).

`config`
:   The new [`configuration`](chardev_v1.md#c.gpiohandle_config "gpiohandle_config") to apply to the
    requested lines.

## Description

Update the configuration of previously requested lines, without releasing the
line or introducing potential glitches.

The configuration applies to all requested lines.

The same [Configuration Rules](gpio-get-linehandle-ioctl.md#gpio-get-linehandle-config-rules) and
[Configuration Support](gpio-get-linehandle-ioctl.md#gpio-get-linehandle-config-support) that apply when requesting the
lines also apply when updating the line configuration, with the additional
restriction that a direction flag must be set. Requesting an invalid
configuration, including without a direction flag set, is an error
(**EINVAL**).

The motivating use case for this command is changing direction of
bi-directional lines between input and output, but it may be used more
generally to move lines seamlessly from one configuration state to another.

To only change the value of output lines, use
[GPIO_HANDLE_SET_LINE_VALUES_IOCTL](gpio-handle-set-line-values-ioctl.md).

First added in 5.5.

## Return Value

On success 0.

On error -1 and the `errno` variable is set appropriately.
Common error codes are described in [GPIO Error Codes](error-codes.md).

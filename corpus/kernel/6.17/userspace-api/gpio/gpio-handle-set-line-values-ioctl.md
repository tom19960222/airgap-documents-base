---
collection: kernel
version: "6.17"
title: "GPIO_HANDLE_SET_LINE_VALUES_IOCTL"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/gpio/gpio-handle-set-line-values-ioctl.html
fetched_at: 2026-09-16T16:28:43+00:00
---
# GPIO_HANDLE_SET_LINE_VALUES_IOCTL

> **Warning:**
>
> This ioctl is part of [GPIO Character Device Userspace API (v1)](chardev_v1.md) and is obsoleted by
> [GPIO_V2_LINE_SET_VALUES_IOCTL](gpio-v2-line-set-values-ioctl.md).

## Name

GPIO_HANDLE_SET_LINE_VALUES_IOCTL - Set the values of all requested output lines.

## Synopsis

GPIO_HANDLE_SET_LINE_VALUES_IOCTL

`int ioctl(int handle_fd, GPIO_HANDLE_SET_LINE_VALUES_IOCTL, struct gpiohandle_data *values)`

## Arguments

`handle_fd`
:   The file descriptor of the GPIO character device, as returned in the
    [`request.fd`](chardev_v1.md#c.gpiohandle_request "gpiohandle_request") by [GPIO_GET_LINEHANDLE_IOCTL](gpio-get-linehandle-ioctl.md).

`values`
:   The [`line_values`](chardev_v1.md#c.gpiohandle_data "gpiohandle_data") to set.

## Description

Set the values of all requested output lines.

The values set are logical, indicating if the line is to be active or inactive.
The `GPIOHANDLE_REQUEST_ACTIVE_LOW` flag controls the mapping between logical
values (active/inactive) and physical values (high/low).
If `GPIOHANDLE_REQUEST_ACTIVE_LOW` is not set then active is high and
inactive is low. If `GPIOHANDLE_REQUEST_ACTIVE_LOW` is set then active is low
and inactive is high.

Only the values of output lines may be set.
Attempting to set the value of input lines is an error (**EPERM**).

## Return Value

On success 0.

On error -1 and the `errno` variable is set appropriately.
Common error codes are described in [GPIO Error Codes](error-codes.md).

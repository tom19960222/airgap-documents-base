---
collection: kernel
version: "6.17"
title: "GPIO_GET_LINEEVENT_IOCTL"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/gpio/gpio-get-lineevent-ioctl.html
fetched_at: 2026-09-16T16:28:39+00:00
---
# GPIO_GET_LINEEVENT_IOCTL

> **Warning:**
>
> This ioctl is part of [GPIO Character Device Userspace API (v1)](chardev_v1.md) and is obsoleted by
> [GPIO_V2_GET_LINE_IOCTL](gpio-v2-get-line-ioctl.md).

## Name

GPIO_GET_LINEEVENT_IOCTL - Request a line with edge detection from the kernel.

## Synopsis

GPIO_GET_LINEEVENT_IOCTL

`int ioctl(int chip_fd, GPIO_GET_LINEEVENT_IOCTL, struct gpioevent_request *request)`

## Arguments

`chip_fd`
:   The file descriptor of the GPIO character device returned by open().

`request`
:   The [`event_request`](chardev_v1.md#c.gpioevent_request "gpioevent_request") specifying the line
    to request and its configuration.

## Description

Request a line with edge detection from the kernel.

On success, the requesting process is granted exclusive access to the line
value and may receive events when edges are detected on the line, as
described in [GPIO_LINEEVENT_DATA_READ](gpio-lineevent-data-read.md).

The state of a line is guaranteed to remain as requested until the returned
file descriptor is closed. Once the file descriptor is closed, the state of
the line becomes uncontrolled from the userspace perspective, and may revert
to its default state.

Requesting a line already in use is an error (**EBUSY**).

Requesting edge detection on a line that does not support interrupts is an
error (**ENXIO**).

As with the [line handle](gpio-get-linehandle-ioctl.md#gpio-get-linehandle-config-support), the
bias configuration is best effort.

Closing the `chip_fd` has no effect on existing line events.

### Configuration Rules

The following configuration rules apply:

The line event is requested as an input, so no flags specific to output lines,
`GPIOHANDLE_REQUEST_OUTPUT`, `GPIOHANDLE_REQUEST_OPEN_DRAIN`, or
`GPIOHANDLE_REQUEST_OPEN_SOURCE`, may be set.

Only one bias flag, `GPIOHANDLE_REQUEST_BIAS_xxx`, may be set.
If no bias flags are set then the bias configuration is not changed.

The edge flags, `GPIOEVENT_REQUEST_RISING_EDGE` and
`GPIOEVENT_REQUEST_FALLING_EDGE`, may be combined to detect both rising
and falling edges.

Requesting an invalid configuration is an error (**EINVAL**).

## Return Value

On success 0 and the [`request.fd`](chardev_v1.md#c.gpioevent_request "gpioevent_request") contains the file
descriptor for the request.

On error -1 and the `errno` variable is set appropriately.
Common error codes are described in [GPIO Error Codes](error-codes.md).

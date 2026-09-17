---
collection: kernel
version: "6.17"
title: "GPIO_V2_GET_LINEINFO_WATCH_IOCTL"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/gpio/gpio-v2-get-lineinfo-watch-ioctl.html
fetched_at: 2026-09-16T16:28:44+00:00
---
# GPIO_V2_GET_LINEINFO_WATCH_IOCTL

## Name

GPIO_V2_GET_LINEINFO_WATCH_IOCTL - Enable watching a line for changes to its
request state and configuration information.

## Synopsis

GPIO_V2_GET_LINEINFO_WATCH_IOCTL

`int ioctl(int chip_fd, GPIO_V2_GET_LINEINFO_WATCH_IOCTL, struct gpio_v2_line_info *info)`

## Arguments

`chip_fd`
:   The file descriptor of the GPIO character device returned by open().

`info`
:   The [`line_info`](chardev.md#c.gpio_v2_line_info "gpio_v2_line_info") `struct to` be populated, with
    the `offset` set to indicate the line to watch

## Description

Enable watching a line for changes to its request state and configuration
information. Changes to line info include a line being requested, released
or reconfigured.

> **Note:**
>
> Watching line info is not generally required, and would typically only be
> used by a system monitoring component.
>
> The line info does NOT include the line value.
> The line must be requested using [GPIO_V2_GET_LINE_IOCTL](gpio-v2-get-line-ioctl.md) to access
> its value, and the line request can monitor a line for events using
> [GPIO_V2_LINE_EVENT_READ](gpio-v2-line-event-read.md).

By default all lines are unwatched when the GPIO chip is opened.

Multiple lines may be watched simultaneously by adding a watch for each.

Once a watch is set, any changes to line info will generate events which can be
read from the `chip_fd` as described in
[GPIO_V2_LINEINFO_CHANGED_READ](gpio-v2-lineinfo-changed-read.md).

Adding a watch to a line that is already watched is an error (**EBUSY**).

Watches are specific to the `chip_fd` and are independent of watches
on the same GPIO chip opened with a separate call to open().

## Return Value

On success 0 and `info` is populated with the current line info.

On error -1 and the `errno` variable is set appropriately.
Common error codes are described in [GPIO Error Codes](error-codes.md).

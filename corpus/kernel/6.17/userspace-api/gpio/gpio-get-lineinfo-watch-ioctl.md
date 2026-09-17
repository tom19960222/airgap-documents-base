---
collection: kernel
version: "6.17"
title: "GPIO_GET_LINEINFO_WATCH_IOCTL"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/gpio/gpio-get-lineinfo-watch-ioctl.html
fetched_at: 2026-09-16T16:28:42+00:00
---
# GPIO_GET_LINEINFO_WATCH_IOCTL

> **Warning:**
>
> This ioctl is part of [GPIO Character Device Userspace API (v1)](chardev_v1.md) and is obsoleted by
> [GPIO_V2_GET_LINEINFO_WATCH_IOCTL](gpio-v2-get-lineinfo-watch-ioctl.md).

## Name

GPIO_GET_LINEINFO_WATCH_IOCTL - Enable watching a line for changes to its
request state and configuration information.

## Synopsis

GPIO_GET_LINEINFO_WATCH_IOCTL

`int ioctl(int chip_fd, GPIO_GET_LINEINFO_WATCH_IOCTL, struct gpioline_info *info)`

## Arguments

`chip_fd`
:   The file descriptor of the GPIO character device returned by open().

`info`
:   The [`line_info`](chardev_v1.md#c.gpioline_info "gpioline_info") `struct to` be populated, with
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
>
> The line must be requested using [GPIO_GET_LINEHANDLE_IOCTL](gpio-get-linehandle-ioctl.md) or
> [GPIO_GET_LINEEVENT_IOCTL](gpio-get-lineevent-ioctl.md) to access its value, and the line event can
> monitor a line for events using [GPIO_LINEEVENT_DATA_READ](gpio-lineevent-data-read.md).

By default all lines are unwatched when the GPIO chip is opened.

Multiple lines may be watched simultaneously by adding a watch for each.

Once a watch is set, any changes to line info will generate events which can be
read from the `chip_fd` as described in
[GPIO_LINEINFO_CHANGED_READ](gpio-lineinfo-changed-read.md).

Adding a watch to a line that is already watched is an error (**EBUSY**).

Watches are specific to the `chip_fd` and are independent of watches
on the same GPIO chip opened with a separate call to open().

First added in 5.7.

## Return Value

On success 0 and `info` is populated with the current line info.

On error -1 and the `errno` variable is set appropriately.
Common error codes are described in [GPIO Error Codes](error-codes.md).

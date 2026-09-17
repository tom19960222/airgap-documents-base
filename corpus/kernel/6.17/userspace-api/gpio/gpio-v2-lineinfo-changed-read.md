---
collection: kernel
version: "6.17"
title: "GPIO_V2_LINEINFO_CHANGED_READ"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/gpio/gpio-v2-lineinfo-changed-read.html
fetched_at: 2026-09-16T16:50:57+00:00
---
# GPIO_V2_LINEINFO_CHANGED_READ

## Name

GPIO_V2_LINEINFO_CHANGED_READ - Read line info changed events for watched
lines from the chip.

## Synopsis

`int read(int chip_fd, void *buf, size_t count)`

## Arguments

`chip_fd`
:   The file descriptor of the GPIO character device returned by open().

`buf`
:   The buffer to contain the [`events`](chardev.md#c.gpio_v2_line_info_changed "gpio_v2_line_info_changed").

`count`
:   The number of bytes available in `buf`, which must be at least the size
    of a [`gpio_v2_line_info_changed`](chardev.md#c.gpio_v2_line_info_changed "gpio_v2_line_info_changed") event.

## Description

Read line info changed events for watched lines from the chip.

> **Note:**
>
> Monitoring line info changes is not generally required, and would typically
> only be performed by a system monitoring component.
>
> These events relate to changes in a line’s request state or configuration,
> not its value. Use [GPIO_V2_LINE_EVENT_READ](gpio-v2-line-event-read.md) to receive events when a
> line changes value.

A line must be watched using [GPIO_V2_GET_LINEINFO_WATCH_IOCTL](gpio-v2-get-lineinfo-watch-ioctl.md) to generate
info changed events. Subsequently, a request, release, or reconfiguration
of the line will generate an info changed event.

The kernel timestamps events when they occur and stores them in a buffer
from where they can be read by userspace at its convenience using read().

The size of the kernel event buffer is fixed at 32 events per `chip_fd`.

The buffer may overflow if bursts of events occur quicker than they are read
by userspace. If an overflow occurs then the most recent event is discarded.
Overflow cannot be detected from userspace.

Events read from the buffer are always in the same order that they were
detected by the kernel, including when multiple lines are being monitored by
the one `chip_fd`.

To minimize the number of calls required to copy events from the kernel to
userspace, read() supports copying multiple events. The number of events
copied is the lower of the number available in the kernel buffer and the
number that will fit in the userspace buffer (`buf`).

A read() will block if no event is available and the `chip_fd` has not
been set **O_NONBLOCK**.

The presence of an event can be tested for by checking that the `chip_fd` is
readable using poll() or an equivalent.

## Return Value

On success the number of bytes read, which will be a multiple of the size
of a [`gpio_v2_line_info_changed`](chardev.md#c.gpio_v2_line_info_changed "gpio_v2_line_info_changed") event.

On error -1 and the `errno` variable is set appropriately.
Common error codes are described in [GPIO Error Codes](error-codes.md).

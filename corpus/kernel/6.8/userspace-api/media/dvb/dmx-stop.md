---
collection: kernel
version: "6.8"
title: "3.2.8. DMX_STOP"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-stop.html
fetched_at: 2026-08-21T03:39:18+00:00
---
# 3.2.8. DMX_STOP

## 3.2.8.1. Name

DMX_STOP

## 3.2.8.2. Synopsis

DMX_STOP

`int ioctl(int fd, DMX_STOP)`

## 3.2.8.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

## 3.2.8.4. Description

This ioctl call is used to stop the actual filtering operation defined
via the ioctl calls [DMX_SET_FILTER](dmx-set-filter.md#dmx-set-filter) or [DMX_SET_PES_FILTER](dmx-set-pes-filter.md#dmx-set-pes-filter) and
started via the [DMX_START](dmx-start.md#dmx-start) command.

## 3.2.8.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

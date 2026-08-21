---
collection: kernel
version: "6.8"
title: "3.2.7. DMX_START"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-start.html
fetched_at: 2026-08-21T03:39:17+00:00
---
# 3.2.7. DMX_START

## 3.2.7.1. Name

DMX_START

## 3.2.7.2. Synopsis

DMX_START

`int ioctl(int fd, DMX_START)`

## 3.2.7.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

## 3.2.7.4. Description

This ioctl call is used to start the actual filtering operation defined
via the ioctl calls [DMX_SET_FILTER](dmx-set-filter.md#dmx-set-filter) or [DMX_SET_PES_FILTER](dmx-set-pes-filter.md#dmx-set-pes-filter).

## 3.2.7.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

|  |  |
| --- | --- |
| `EINVAL` | Invalid argument, i.e. no filtering parameters provided via the [DMX_SET_FILTER](dmx-set-filter.md#dmx-set-filter) or [DMX_SET_PES_FILTER](dmx-set-pes-filter.md#dmx-set-pes-filter) ioctls. |
| `EBUSY` | This error code indicates that there are conflicting requests. There are active filters filtering data from another input source. Make sure that these filters are stopped before starting this filter. |

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

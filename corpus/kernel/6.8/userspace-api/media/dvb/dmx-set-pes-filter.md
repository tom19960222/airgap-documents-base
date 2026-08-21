---
collection: kernel
version: "6.8"
title: "3.2.10. DMX_SET_PES_FILTER"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-set-pes-filter.html
fetched_at: 2026-08-21T03:39:17+00:00
---
# 3.2.10. DMX_SET_PES_FILTER

## 3.2.10.1. Name

DMX_SET_PES_FILTER

## 3.2.10.2. Synopsis

DMX_SET_PES_FILTER

`int ioctl(int fd, DMX_SET_PES_FILTER, struct dmx_pes_filter_params *params)`

## 3.2.10.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

`params`
:   Pointer to structure containing filter parameters.

## 3.2.10.4. Description

This ioctl call sets up a PES filter according to the parameters
provided. By a PES filter is meant a filter that is based just on the
packet identifier (PID), i.e. no PES header or payload filtering
capability is supported.

## 3.2.10.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

|  |  |
| --- | --- |
| `EBUSY` | This error code indicates that there are conflicting requests. There are active filters filtering data from another input source. Make sure that these filters are stopped before starting this filter. |

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

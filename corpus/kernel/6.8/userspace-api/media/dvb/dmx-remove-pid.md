---
collection: kernel
version: "6.8"
title: "3.2.15. DMX_REMOVE_PID"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-remove-pid.html
fetched_at: 2026-08-21T03:39:14+00:00
---
# 3.2.15. DMX_REMOVE_PID

## 3.2.15.1. Name

DMX_REMOVE_PID

## 3.2.15.2. Synopsis

DMX_REMOVE_PID

`int ioctl(fd, DMX_REMOVE_PID, __u16 *pid)`

## 3.2.15.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

`pid`
:   PID of the PES filter to be removed.

## 3.2.15.4. Description

This ioctl call allows to remove a PID when multiple PIDs are set on a
transport stream filter, e. g. a filter previously set up with output
equal to [`DMX_OUT_TSDEMUX_TAP`](dmx_types.md#c.dmx_output "dmx_output"), created via either
[DMX_SET_PES_FILTER](dmx-set-pes-filter.md#dmx-set-pes-filter) or [DMX_ADD_PID](dmx-add-pid.md#dmx-add-pid).

## 3.2.15.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

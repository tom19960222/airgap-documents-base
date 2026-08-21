---
collection: kernel
version: "6.8"
title: "3.2.14. DMX_ADD_PID"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-add-pid.html
fetched_at: 2026-08-21T03:39:11+00:00
---
# 3.2.14. DMX_ADD_PID

## 3.2.14.1. Name

DMX_ADD_PID

## 3.2.14.2. Synopsis

DMX_ADD_PID

`int ioctl(fd, DMX_ADD_PID, __u16 *pid)`

## 3.2.14.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

`pid`
:   PID number to be filtered.

## 3.2.14.4. Description

This ioctl call allows to add multiple PIDs to a transport stream filter
previously set up with [DMX_SET_PES_FILTER](dmx-set-pes-filter.md#dmx-set-pes-filter) and output equal to
[`DMX_OUT_TSDEMUX_TAP`](dmx_types.md#c.dmx_output "dmx_output").

## 3.2.14.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

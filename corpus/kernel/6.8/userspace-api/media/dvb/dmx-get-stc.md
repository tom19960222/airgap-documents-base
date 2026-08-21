---
collection: kernel
version: "6.8"
title: "3.2.12. DMX_GET_STC"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-get-stc.html
fetched_at: 2026-08-21T03:39:13+00:00
---
# 3.2.12. DMX_GET_STC

## 3.2.12.1. Name

DMX_GET_STC

## 3.2.12.2. Synopsis

DMX_GET_STC

`int ioctl(int fd, DMX_GET_STC, struct dmx_stc *stc)`

## 3.2.12.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

`stc`
:   Pointer to [`dmx_stc`](dmx_types.md#c.dmx_stc "dmx_stc") where the stc data is to be stored.

## 3.2.12.4. Description

This ioctl call returns the current value of the system time counter
(which is driven by a PES filter of type [`DMX_PES_PCR`](dmx_types.md#c.dmx_ts_pes "dmx_ts_pes")).
Some hardware supports more than one STC, so you must specify which one by
setting the [`num`](dmx_types.md#c.dmx_stc "dmx_stc") field of stc before the ioctl (range 0...n).
The result is returned in form of a ratio with a 64 bit numerator
and a 32 bit denominator, so the real 90kHz STC value is
`stc->stc / stc->base`.

## 3.2.12.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

|  |  |
| --- | --- |
| `EINVAL` | Invalid stc number. |

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

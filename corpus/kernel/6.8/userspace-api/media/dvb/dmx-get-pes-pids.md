---
collection: kernel
version: "6.8"
title: "3.2.13. DMX_GET_PES_PIDS"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-get-pes-pids.html
fetched_at: 2026-08-21T03:39:12+00:00
---
# 3.2.13. DMX_GET_PES_PIDS

## 3.2.13.1. Name

DMX_GET_PES_PIDS

## 3.2.13.2. Synopsis

DMX_GET_PES_PIDS

`int ioctl(fd, DMX_GET_PES_PIDS, __u16 pids[5])`

## 3.2.13.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

`pids`
:   Array used to store 5 Program IDs.

## 3.2.13.4. Description

This ioctl allows to query a DVB device to return the first PID used
by audio, video, textext, subtitle and PCR programs on a given service.
They're stored as:

| PID element | position | content |
| --- | --- | --- |
| pids[DMX_PES_AUDIO] | 0 | first audio PID |
| pids[DMX_PES_VIDEO] | 1 | first video PID |
| pids[DMX_PES_TELETEXT] | 2 | first teletext PID |
| pids[DMX_PES_SUBTITLE] | 3 | first subtitle PID |
| pids[DMX_PES_PCR] | 4 | first Program Clock Reference PID |

> **Note:**
>
> A value equal to 0xffff means that the PID was not filled by the
> Kernel.

## 3.2.13.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

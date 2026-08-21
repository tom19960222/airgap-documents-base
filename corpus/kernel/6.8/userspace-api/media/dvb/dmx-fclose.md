---
collection: kernel
version: "6.8"
title: "3.2.2. Digital TV demux close()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-fclose.html
fetched_at: 2026-08-21T03:39:10+00:00
---
# 3.2.2. Digital TV demux close()

## 3.2.2.1. Name

Digital TV demux [`close()`](dmx-fclose.md#c.DTV.dmx.close "DTV.dmx.close")

## 3.2.2.2. Synopsis

int close(int fd)

## 3.2.2.3. Arguments

`fd`
:   File descriptor returned by a previous call to
    [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

## 3.2.2.4. Description

This system call deactivates and deallocates a filter that was
previously allocated via the [`open()`](dmx-fopen.md#c.DTV.dmx.open "open") call.

## 3.2.2.5. Return Value

On success 0 is returned.

On error, -1 is returned and the `errno` variable is set
appropriately.

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

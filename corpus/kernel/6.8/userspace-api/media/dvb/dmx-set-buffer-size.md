---
collection: kernel
version: "6.8"
title: "3.2.11. DMX_SET_BUFFER_SIZE"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-set-buffer-size.html
fetched_at: 2026-08-21T03:39:15+00:00
---
# 3.2.11. DMX_SET_BUFFER_SIZE

## 3.2.11.1. Name

DMX_SET_BUFFER_SIZE

## 3.2.11.2. Synopsis

DMX_SET_BUFFER_SIZE

`int ioctl(int fd, DMX_SET_BUFFER_SIZE, unsigned long size)`

## 3.2.11.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

`size`
:   Unsigned long size

## 3.2.11.4. Description

This ioctl call is used to set the size of the circular buffer used for
filtered data. The default size is two maximum sized sections, i.e. if
this function is not called a buffer size of `2 * 4096` bytes will be
used.

## 3.2.11.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

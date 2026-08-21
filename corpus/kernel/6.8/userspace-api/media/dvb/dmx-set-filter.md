---
collection: kernel
version: "6.8"
title: "3.2.9. DMX_SET_FILTER"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dmx-set-filter.html
fetched_at: 2026-08-21T03:39:16+00:00
---
# 3.2.9. DMX_SET_FILTER

## 3.2.9.1. Name

DMX_SET_FILTER

## 3.2.9.2. Synopsis

DMX_SET_FILTER

`int ioctl(int fd, DMX_SET_FILTER, struct dmx_sct_filter_params *params)`

## 3.2.9.3. Arguments

`fd`
:   File descriptor returned by [`open()`](dmx-fopen.md#c.DTV.dmx.open "open").

`params`

> Pointer to structure containing filter parameters.

## 3.2.9.4. Description

This ioctl call sets up a filter according to the filter and mask
parameters provided. A timeout may be defined stating number of seconds
to wait for a section to be loaded. A value of 0 means that no timeout
should be applied. Finally there is a flag field where it is possible to
state whether a section should be CRC-checked, whether the filter should
be a "one-shot" filter, i.e. if the filtering operation should be
stopped after the first section is received, and whether the filtering
operation should be started immediately (without waiting for a
[DMX_START](dmx-start.md#dmx-start) ioctl call). If a filter was previously set-up, this
filter will be canceled, and the receive buffer will be flushed.

## 3.2.9.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

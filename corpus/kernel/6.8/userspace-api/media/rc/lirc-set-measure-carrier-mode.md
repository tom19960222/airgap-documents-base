---
collection: kernel
version: "6.8"
title: "6.5.14. ioctl LIRC_SET_MEASURE_CARRIER_MODE"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-set-measure-carrier-mode.html
fetched_at: 2026-08-21T03:40:10+00:00
---
# 6.5.14. ioctl LIRC_SET_MEASURE_CARRIER_MODE

## 6.5.14.1. Name

LIRC_SET_MEASURE_CARRIER_MODE - enable or disable measure mode

## 6.5.14.2. Synopsis

LIRC_SET_MEASURE_CARRIER_MODE

`int ioctl(int fd, LIRC_SET_MEASURE_CARRIER_MODE, __u32 *enable)`

## 6.5.14.3. Arguments

`fd`
:   File descriptor returned by open().

`enable`
:   enable = 1 means enable measure mode, enable = 0 means disable measure
    mode.

## 6.5.14.4. Description

Enable or disable measure mode. If enabled, from the next key
press on, the driver will send `LIRC_MODE2_FREQUENCY` packets. By
default this should be turned off.

## 6.5.14.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

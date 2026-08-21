---
collection: kernel
version: "6.8"
title: "6.5.10. ioctl LIRC_SET_REC_CARRIER"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-set-rec-carrier.html
fetched_at: 2026-08-21T03:40:11+00:00
---
# 6.5.10. ioctl LIRC_SET_REC_CARRIER

## 6.5.10.1. Name

LIRC_SET_REC_CARRIER - Set carrier used to modulate IR receive.

## 6.5.10.2. Synopsis

LIRC_SET_REC_CARRIER

`int ioctl(int fd, LIRC_SET_REC_CARRIER, __u32 *frequency)`

## 6.5.10.3. Arguments

`fd`
:   File descriptor returned by open().

`frequency`
:   Frequency of the carrier that modulates PWM data, in Hz.

## 6.5.10.4. Description

Set receive carrier used to modulate IR PWM pulses and spaces.

> **Note:**
>
> If called together with [ioctl LIRC_SET_REC_CARRIER_RANGE](lirc-set-rec-carrier-range.md#lirc-set-rec-carrier-range), this ioctl
> sets the upper bound frequency that will be recognized by the device.

## 6.5.10.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

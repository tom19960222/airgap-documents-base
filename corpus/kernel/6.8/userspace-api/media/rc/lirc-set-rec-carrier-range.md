---
collection: kernel
version: "6.8"
title: "6.5.11. ioctl LIRC_SET_REC_CARRIER_RANGE"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-set-rec-carrier-range.html
fetched_at: 2026-08-21T03:40:11+00:00
---
# 6.5.11. ioctl LIRC_SET_REC_CARRIER_RANGE

## 6.5.11.1. Name

LIRC_SET_REC_CARRIER_RANGE - Set lower bound of the carrier used to modulate
IR receive.

## 6.5.11.2. Synopsis

LIRC_SET_REC_CARRIER_RANGE

`int ioctl(int fd, LIRC_SET_REC_CARRIER_RANGE, __u32 *frequency)`

## 6.5.11.3. Arguments

`fd`
:   File descriptor returned by open().

`frequency`
:   Frequency of the carrier that modulates PWM data, in Hz.

## 6.5.11.4. Description

This ioctl sets the upper range of carrier frequency that will be recognized
by the IR receiver.

> **Note:**
>
> To set a range use [LIRC_SET_REC_CARRIER_RANGE](lirc-set-rec-carrier-range.md#lirc-set-rec-carrier-range) with the lower bound first and later call
> [LIRC_SET_REC_CARRIER](lirc-set-rec-carrier.md#lirc-set-rec-carrier) with the upper bound.

## 6.5.11.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

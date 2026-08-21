---
collection: kernel
version: "6.8"
title: "6.5.12. ioctl LIRC_SET_SEND_CARRIER"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-set-send-carrier.html
fetched_at: 2026-08-21T03:40:12+00:00
---
# 6.5.12. ioctl LIRC_SET_SEND_CARRIER

## 6.5.12.1. Name

LIRC_SET_SEND_CARRIER - Set send carrier used to modulate IR TX.

## 6.5.12.2. Synopsis

LIRC_SET_SEND_CARRIER

`int ioctl(int fd, LIRC_SET_SEND_CARRIER, __u32 *frequency)`

## 6.5.12.3. Arguments

`fd`
:   File descriptor returned by open().

`frequency`
:   Frequency of the carrier to be modulated, in Hz.

## 6.5.12.4. Description

Set send carrier used to modulate IR PWM pulses and spaces.

## 6.5.12.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

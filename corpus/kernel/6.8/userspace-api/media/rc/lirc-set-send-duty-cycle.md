---
collection: kernel
version: "6.8"
title: "6.5.7. ioctl LIRC_SET_SEND_DUTY_CYCLE"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-set-send-duty-cycle.html
fetched_at: 2026-08-21T03:40:12+00:00
---
# 6.5.7. ioctl LIRC_SET_SEND_DUTY_CYCLE

## 6.5.7.1. Name

LIRC_SET_SEND_DUTY_CYCLE - Set the duty cycle of the carrier signal for
IR transmit.

## 6.5.7.2. Synopsis

LIRC_SET_SEND_DUTY_CYCLE

`int ioctl(int fd, LIRC_SET_SEND_DUTY_CYCLE, __u32 *duty_cycle)`

## 6.5.7.3. Arguments

`fd`
:   File descriptor returned by open().

`duty_cycle`
:   Duty cicle, describing the pulse width in percent (from 1 to 99) of
    the total cycle. Values 0 and 100 are reserved.

## 6.5.7.4. Description

Get/set the duty cycle of the carrier signal for IR transmit.

Currently, no special meaning is defined for 0 or 100, but this
could be used to switch off carrier generation in the future, so
these values should be reserved.

## 6.5.7.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

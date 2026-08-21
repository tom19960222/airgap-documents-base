---
collection: kernel
version: "6.8"
title: "6.5.3. ioctl LIRC_GET_FEATURES"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-get-features.html
fetched_at: 2026-08-21T03:40:06+00:00
---
# 6.5.3. ioctl LIRC_GET_FEATURES

## 6.5.3.1. Name

LIRC_GET_FEATURES - Get the underlying hardware device's features

## 6.5.3.2. Synopsis

LIRC_GET_FEATURES

`int ioctl(int fd, LIRC_GET_FEATURES, __u32 *features)`

## 6.5.3.3. Arguments

`fd`
:   File descriptor returned by open().

`features`
:   Bitmask with the LIRC features.

## 6.5.3.4. Description

Get the underlying hardware device's features. If a driver does not
announce support of certain features, calling of the corresponding ioctls
is undefined.

## 6.5.3.5. LIRC features

`LIRC_CAN_REC_RAW`

> Unused. Kept just to avoid breaking uAPI.

`LIRC_CAN_REC_PULSE`

> Unused. Kept just to avoid breaking uAPI.
> [LIRC_MODE_PULSE](lirc-dev-intro.md#lirc-mode-pulse) can only be used for transmitting.

`LIRC_CAN_REC_MODE2`

> This is raw IR driver for receiving. This means that
> [LIRC_MODE_MODE2](lirc-dev-intro.md#lirc-mode-mode2) is used. This also implies
> that [LIRC_MODE_SCANCODE](lirc-dev-intro.md#lirc-mode-scancode) is also supported,
> as long as the kernel is recent enough. Use the
> [ioctls LIRC_GET_REC_MODE and LIRC_SET_REC_MODE](lirc-get-rec-mode.md#lirc-set-rec-mode) to switch modes.

`LIRC_CAN_REC_LIRCCODE`

> Unused. Kept just to avoid breaking uAPI.

`LIRC_CAN_REC_SCANCODE`

> This is a scancode driver for receiving. This means that
> [LIRC_MODE_SCANCODE](lirc-dev-intro.md#lirc-mode-scancode) is used.

`LIRC_CAN_SET_SEND_CARRIER`

> The driver supports changing the modulation frequency via
> [ioctl LIRC_SET_SEND_CARRIER](lirc-set-send-carrier.md#lirc-set-send-carrier).

`LIRC_CAN_SET_SEND_DUTY_CYCLE`

> The driver supports changing the duty cycle using
> [ioctl LIRC_SET_SEND_DUTY_CYCLE](lirc-set-send-duty-cycle.md#lirc-set-send-duty-cycle).

`LIRC_CAN_SET_TRANSMITTER_MASK`

> The driver supports changing the active transmitter(s) using
> [ioctl LIRC_SET_TRANSMITTER_MASK](lirc-set-transmitter-mask.md#lirc-set-transmitter-mask).

`LIRC_CAN_SET_REC_CARRIER`

> The driver supports setting the receive carrier frequency using
> [ioctl LIRC_SET_REC_CARRIER](lirc-set-rec-carrier.md#lirc-set-rec-carrier).

`LIRC_CAN_SET_REC_CARRIER_RANGE`

> The driver supports
> [ioctl LIRC_SET_REC_CARRIER_RANGE](lirc-set-rec-carrier-range.md#lirc-set-rec-carrier-range).

`LIRC_CAN_GET_REC_RESOLUTION`

> The driver supports
> [ioctl LIRC_GET_REC_RESOLUTION](lirc-get-rec-resolution.md#lirc-get-rec-resolution).

`LIRC_CAN_SET_REC_TIMEOUT`

> The driver supports
> [ioctl LIRC_SET_REC_TIMEOUT](lirc-set-rec-timeout.md#lirc-set-rec-timeout).

`LIRC_CAN_MEASURE_CARRIER`

> The driver supports measuring of the modulation frequency using
> [ioctl LIRC_SET_MEASURE_CARRIER_MODE](lirc-set-measure-carrier-mode.md#lirc-set-measure-carrier-mode).

`LIRC_CAN_USE_WIDEBAND_RECEIVER`

> The driver supports learning mode using
> [ioctl LIRC_SET_WIDEBAND_RECEIVER](lirc-set-wideband-receiver.md#lirc-set-wideband-receiver).

`LIRC_CAN_SEND_RAW`

> Unused. Kept just to avoid breaking uAPI.

`LIRC_CAN_SEND_PULSE`

> The driver supports sending (also called as IR blasting or IR TX) using
> [LIRC_MODE_PULSE](lirc-dev-intro.md#lirc-mode-pulse). This implies that
> [LIRC_MODE_SCANCODE](lirc-dev-intro.md#lirc-mode-scancode) is also supported for
> transmit, as long as the kernel is recent enough. Use the
> [ioctls LIRC_GET_SEND_MODE and LIRC_SET_SEND_MODE](lirc-get-send-mode.md#lirc-set-send-mode) to switch modes.

`LIRC_CAN_SEND_MODE2`

> Unused. Kept just to avoid breaking uAPI.
> [LIRC_MODE_MODE2](lirc-dev-intro.md#lirc-mode-mode2) can only be used for receiving.

`LIRC_CAN_SEND_LIRCCODE`

> Unused. Kept just to avoid breaking uAPI.

## 6.5.3.6. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

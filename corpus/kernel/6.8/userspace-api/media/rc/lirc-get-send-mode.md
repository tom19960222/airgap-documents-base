---
collection: kernel
version: "6.8"
title: "6.5.4. ioctls LIRC_GET_SEND_MODE and LIRC_SET_SEND_MODE"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-get-send-mode.html
fetched_at: 2026-08-21T03:40:09+00:00
---
# 6.5.4. ioctls LIRC_GET_SEND_MODE and LIRC_SET_SEND_MODE

## 6.5.4.1. Name

LIRC_GET_SEND_MODE/LIRC_SET_SEND_MODE - Get/set current transmit mode.

## 6.5.4.2. Synopsis

LIRC_GET_SEND_MODE

`int ioctl(int fd, LIRC_GET_SEND_MODE, __u32 *mode)`

LIRC_SET_SEND_MODE

`int ioctl(int fd, LIRC_SET_SEND_MODE, __u32 *mode)`

## 6.5.4.3. Arguments

`fd`
:   File descriptor returned by open().

`mode`
:   The mode used for transmitting.

## 6.5.4.4. Description

Get/set current transmit mode.

Only [LIRC_MODE_PULSE](lirc-dev-intro.md#lirc-mode-pulse) and
[LIRC_MODE_SCANCODE](lirc-dev-intro.md#lirc-mode-scancode) are supported by for IR send,
depending on the driver. Use [ioctl LIRC_GET_FEATURES](lirc-get-features.md#lirc-get-features) to find out which
modes the driver supports.

## 6.5.4.5. Return Value

|  |  |
| --- | --- |
| `ENODEV` | Device not available. |
| `ENOTTY` | Device does not support transmitting. |
| `EINVAL` | Invalid mode or invalid mode for this device. |

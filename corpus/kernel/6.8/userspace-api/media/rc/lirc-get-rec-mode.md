---
collection: kernel
version: "6.8"
title: "6.5.5. ioctls LIRC_GET_REC_MODE and LIRC_SET_REC_MODE"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-get-rec-mode.html
fetched_at: 2026-08-21T03:40:08+00:00
---
# 6.5.5. ioctls LIRC_GET_REC_MODE and LIRC_SET_REC_MODE

## 6.5.5.1. Name

LIRC_GET_REC_MODE/LIRC_SET_REC_MODE - Get/set current receive mode.

## 6.5.5.2. Synopsis

LIRC_GET_REC_MODE

`int ioctl(int fd, LIRC_GET_REC_MODE, __u32 *mode)`

LIRC_SET_REC_MODE

`int ioctl(int fd, LIRC_SET_REC_MODE, __u32 *mode)`

## 6.5.5.3. Arguments

`fd`
:   File descriptor returned by open().

`mode`
:   Mode used for receive.

## 6.5.5.4. Description

Get and set the current receive mode. Only
[LIRC_MODE_MODE2](lirc-dev-intro.md#lirc-mode-mode2) and
[LIRC_MODE_SCANCODE](lirc-dev-intro.md#lirc-mode-scancode) are supported.
Use [ioctl LIRC_GET_FEATURES](lirc-get-features.md#lirc-get-features) to find out which modes the driver supports.

## 6.5.5.5. Return Value

|  |  |
| --- | --- |
| `ENODEV` | Device not available. |
| `ENOTTY` | Device does not support receiving. |
| `EINVAL` | Invalid mode or invalid mode for this device. |

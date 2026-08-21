---
collection: kernel
version: "6.8"
title: "6.5.15. ioctl LIRC_SET_WIDEBAND_RECEIVER"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-set-wideband-receiver.html
fetched_at: 2026-08-21T03:40:13+00:00
---
# 6.5.15. ioctl LIRC_SET_WIDEBAND_RECEIVER

## 6.5.15.1. Name

LIRC_SET_WIDEBAND_RECEIVER - enable wide band receiver.

## 6.5.15.2. Synopsis

LIRC_SET_WIDEBAND_RECEIVER

`int ioctl(int fd, LIRC_SET_WIDEBAND_RECEIVER, __u32 *enable)`

## 6.5.15.3. Arguments

`fd`
:   File descriptor returned by open().

`enable`
:   enable = 1 means enable wideband receiver, enable = 0 means disable
    wideband receiver.

## 6.5.15.4. Description

Some receivers are equipped with special wide band receiver which is
intended to be used to learn output of existing remote. This ioctl
allows enabling or disabling it.

This might be useful of receivers that have otherwise narrow band receiver
that prevents them to be used with some remotes. Wide band receiver might
also be more precise. On the other hand its disadvantage it usually
reduced range of reception.

> **Note:**
>
> Wide band receiver might be implicitly enabled if you enable
> carrier reports. In that case it will be disabled as soon as you disable
> carrier reports. Trying to disable wide band receiver while carrier
> reports are active will do nothing.

## 6.5.15.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

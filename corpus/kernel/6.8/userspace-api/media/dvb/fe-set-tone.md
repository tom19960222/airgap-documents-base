---
collection: kernel
version: "6.8"
title: "2.4.10. ioctl FE_SET_TONE"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-set-tone.html
fetched_at: 2026-08-21T03:39:32+00:00
---
# 2.4.10. ioctl FE_SET_TONE

## 2.4.10.1. Name

FE_SET_TONE - Sets/resets the generation of the continuous 22kHz tone.

## 2.4.10.2. Synopsis

FE_SET_TONE

`int ioctl(int fd, FE_SET_TONE, enum fe_sec_tone_mode tone)`

## 2.4.10.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`tone`
:   an integer enumered value described at [`fe_sec_tone_mode`](frontend-header.md#c.fe_sec_tone_mode "fe_sec_tone_mode")

## 2.4.10.4. Description

This ioctl is used to set the generation of the continuous 22kHz tone.
This call requires read/write permissions.

Usually, satellite antenna subsystems require that the digital TV device
to send a 22kHz tone in order to select between high/low band on some
dual-band LNBf. It is also used to send signals to DiSEqC equipment, but
this is done using the DiSEqC ioctls.

> **Attention:**
>
> If more than one device is connected to the same antenna,
> setting a tone may interfere on other devices, as they may lose the
> capability of selecting the band. So, it is recommended that applications
> would change to SEC_TONE_OFF when the device is not used.

## 2.4.10.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

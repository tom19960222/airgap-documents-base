---
collection: kernel
version: "6.8"
title: "6.1.2.2. FE_READ_SNR"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-read-snr.html
fetched_at: 2026-08-21T03:39:29+00:00
---
# 6.1.2.2. FE_READ_SNR

## 6.1.2.2.1. Name

FE_READ_SNR

> **Attention:**
>
> This ioctl is deprecated.

## 6.1.2.2.2. Synopsis

FE_READ_SNR

`int ioctl(int fd, FE_READ_SNR, int16_t *snr)`

## 6.1.2.2.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`snr`
:   The signal-to-noise ratio is stored into \*snr.

## 6.1.2.2.4. Description

This ioctl call returns the signal-to-noise ratio for the signal
currently received by the front-end. For this command, read-only access
to the device is sufficient.

## 6.1.2.2.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

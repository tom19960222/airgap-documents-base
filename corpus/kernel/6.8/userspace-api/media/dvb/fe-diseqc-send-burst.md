---
collection: kernel
version: "6.8"
title: "2.4.9. ioctl FE_DISEQC_SEND_BURST"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-diseqc-send-burst.html
fetched_at: 2026-08-21T03:39:23+00:00
---
# 2.4.9. ioctl FE_DISEQC_SEND_BURST

## 2.4.9.1. Name

FE_DISEQC_SEND_BURST - Sends a 22KHz tone burst for 2x1 mini DiSEqC satellite selection.

## 2.4.9.2. Synopsis

FE_DISEQC_SEND_BURST

`int ioctl(int fd, FE_DISEQC_SEND_BURST, enum fe_sec_mini_cmd tone)`

## 2.4.9.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`tone`
:   An integer enumered value described at [`fe_sec_mini_cmd`](frontend-header.md#c.fe_sec_mini_cmd "fe_sec_mini_cmd").

## 2.4.9.4. Description

This ioctl is used to set the generation of a 22kHz tone burst for mini
DiSEqC satellite selection for 2x1 switches. This call requires
read/write permissions.

It provides support for what's specified at
[Digital Satellite Equipment Control (DiSEqC) - Simple "ToneBurst" Detection Circuit specification.](http://www.eutelsat.com/files/contributed/satellites/pdf/Diseqc/associated%20docs/simple_tone_burst_detec.pdf)

## 2.4.9.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

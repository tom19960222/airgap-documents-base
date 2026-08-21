---
collection: kernel
version: "6.8"
title: "2.4.12. ioctl FE_ENABLE_HIGH_LNB_VOLTAGE"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-enable-high-lnb-voltage.html
fetched_at: 2026-08-21T03:39:25+00:00
---
# 2.4.12. ioctl FE_ENABLE_HIGH_LNB_VOLTAGE

## 2.4.12.1. Name

FE_ENABLE_HIGH_LNB_VOLTAGE - Select output DC level between normal LNBf voltages or higher LNBf - voltages.

## 2.4.12.2. Synopsis

FE_ENABLE_HIGH_LNB_VOLTAGE

`int ioctl(int fd, FE_ENABLE_HIGH_LNB_VOLTAGE, unsigned int high)`

## 2.4.12.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`high`
:   Valid flags:

    - 0 - normal 13V and 18V.
    - >0 - enables slightly higher voltages instead of 13/18V, in order
      to compensate for long antenna cables.

## 2.4.12.4. Description

Select output DC level between normal LNBf voltages or higher LNBf
voltages between 0 (normal) or a value grater than 0 for higher
voltages.

## 2.4.12.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

---
collection: kernel
version: "6.8"
title: "2.4.13. ioctl FE_SET_FRONTEND_TUNE_MODE"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-set-frontend-tune-mode.html
fetched_at: 2026-08-21T03:39:31+00:00
---
# 2.4.13. ioctl FE_SET_FRONTEND_TUNE_MODE

## 2.4.13.1. Name

FE_SET_FRONTEND_TUNE_MODE - Allow setting tuner mode flags to the frontend.

## 2.4.13.2. Synopsis

FE_SET_FRONTEND_TUNE_MODE

`int ioctl(int fd, FE_SET_FRONTEND_TUNE_MODE, unsigned int flags)`

## 2.4.13.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`flags`
:   Valid flags:

    - 0 - normal tune mode
    - `FE_TUNE_MODE_ONESHOT` - When set, this flag will disable any
      zigzagging or other "normal" tuning behaviour. Additionally,
      there will be no automatic monitoring of the lock status, and
      hence no frontend events will be generated. If a frontend device
      is closed, this flag will be automatically turned off when the
      device is reopened read-write.

## 2.4.13.4. Description

Allow setting tuner mode flags to the frontend, between 0 (normal) or
`FE_TUNE_MODE_ONESHOT` mode

## 2.4.13.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

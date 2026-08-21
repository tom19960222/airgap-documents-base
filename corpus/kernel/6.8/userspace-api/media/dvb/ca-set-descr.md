---
collection: kernel
version: "6.8"
title: "4.2.9. CA_SET_DESCR"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/ca-set-descr.html
fetched_at: 2026-08-21T03:39:08+00:00
---
# 4.2.9. CA_SET_DESCR

## 4.2.9.1. Name

CA_SET_DESCR

## 4.2.9.2. Synopsis

CA_SET_DESCR

`int ioctl(fd, CA_SET_DESCR, struct ca_descr *desc)`

## 4.2.9.3. Arguments

`fd`
:   File descriptor returned by a previous call to [`open()`](ca-fopen.md#c.DTV.ca.open "open").

`msg`
:   Pointer to struct [`ca_descr`](ca_data_types.md#c.ca_descr "ca_descr").

## 4.2.9.4. Description

CA_SET_DESCR is used for feeding descrambler CA slots with descrambling
keys (referred as control words).

## 4.2.9.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

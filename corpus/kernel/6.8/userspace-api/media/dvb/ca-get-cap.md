---
collection: kernel
version: "6.8"
title: "4.2.4. CA_GET_CAP"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/ca-get-cap.html
fetched_at: 2026-08-21T03:39:05+00:00
---
# 4.2.4. CA_GET_CAP

## 4.2.4.1. Name

CA_GET_CAP

## 4.2.4.2. Synopsis

CA_GET_CAP

`int ioctl(fd, CA_GET_CAP, struct ca_caps *caps)`

## 4.2.4.3. Arguments

`fd`
:   File descriptor returned by a previous call to [`open()`](ca-fopen.md#c.DTV.ca.open "open").

`caps`
:   Pointer to struct [`ca_caps`](ca_data_types.md#c.ca_caps "ca_caps").

## 4.2.4.4. Description

Queries the Kernel for information about the available CA and descrambler
slots, and their types.

## 4.2.4.5. Return Value

On success 0 is returned and [`ca_caps`](ca_data_types.md#c.ca_caps "ca_caps") is filled.

On error, -1 is returned and the `errno` variable is set
appropriately.

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

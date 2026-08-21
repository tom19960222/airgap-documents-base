---
collection: kernel
version: "6.8"
title: "4.2.6. CA_GET_DESCR_INFO"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/ca-get-descr-info.html
fetched_at: 2026-08-21T03:39:06+00:00
---
# 4.2.6. CA_GET_DESCR_INFO

## 4.2.6.1. Name

CA_GET_DESCR_INFO

## 4.2.6.2. Synopsis

CA_GET_DESCR_INFO

`int ioctl(fd, CA_GET_DESCR_INFO, struct ca_descr_info *desc)`

## 4.2.6.3. Arguments

`fd`
:   File descriptor returned by a previous call to [`open()`](ca-fopen.md#c.DTV.ca.open "open").

`desc`
:   Pointer to struct [`ca_descr_info`](ca_data_types.md#c.ca_descr_info "ca_descr_info").

## 4.2.6.4. Description

Returns information about all descrambler slots.

## 4.2.6.5. Return Value

On success 0 is returned, and [`ca_descr_info`](ca_data_types.md#c.ca_descr_info "ca_descr_info") is filled.

On error -1 is returned, and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

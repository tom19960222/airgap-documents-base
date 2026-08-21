---
collection: kernel
version: "6.8"
title: "4.2.5. CA_GET_SLOT_INFO"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/ca-get-slot-info.html
fetched_at: 2026-08-21T03:39:07+00:00
---
# 4.2.5. CA_GET_SLOT_INFO

## 4.2.5.1. Name

CA_GET_SLOT_INFO

## 4.2.5.2. Synopsis

CA_GET_SLOT_INFO

`int ioctl(fd, CA_GET_SLOT_INFO, struct ca_slot_info *info)`

## 4.2.5.3. Arguments

`fd`
:   File descriptor returned by a previous call to [`open()`](ca-fopen.md#c.DTV.ca.open "open").

`info`
:   Pointer to struct [`ca_slot_info`](ca_data_types.md#c.ca_slot_info "ca_slot_info").

## 4.2.5.4. Description

Returns information about a CA slot identified by
[`ca_slot_info`](ca_data_types.md#c.ca_slot_info "ca_slot_info").slot_num.

## 4.2.5.5. Return Value

On success 0 is returned, and [`ca_slot_info`](ca_data_types.md#c.ca_slot_info "ca_slot_info") is filled.

On error -1 is returned, and the `errno` variable is set
appropriately.

|  |  |
| --- | --- |
| `ENODEV` | the slot is not available. |

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

---
collection: kernel
version: "6.17"
title: "4.2.7. CA_GET_MSG"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/media/dvb/ca-get-msg.html
fetched_at: 2026-09-16T16:27:51+00:00
---
# 4.2.7. CA_GET_MSG

## 4.2.7.1. Name

CA_GET_MSG

## 4.2.7.2. Synopsis

CA_GET_MSG

`int ioctl(fd, CA_GET_MSG, struct ca_msg *msg)`

## 4.2.7.3. Arguments

`fd`
:   File descriptor returned by a previous call to [`open()`](ca-fopen.md#c.DTV.ca.open "open").

`msg`
:   Pointer to struct [`ca_msg`](ca_data_types.md#c.ca_msg "ca_msg").

## 4.2.7.4. Description

Receives a message via a CI CA module.

> **Note:**
>
> Please notice that, on most drivers, this is done by reading from
> the /dev/adapter?/ca? device node.

## 4.2.7.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

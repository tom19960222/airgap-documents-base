---
collection: kernel
version: "6.8"
title: "4.2.8. CA_SEND_MSG"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/ca-send-msg.html
fetched_at: 2026-08-21T03:39:08+00:00
---
# 4.2.8. CA_SEND_MSG

## 4.2.8.1. Name

CA_SEND_MSG

## 4.2.8.2. Synopsis

CA_SEND_MSG

`int ioctl(fd, CA_SEND_MSG, struct ca_msg *msg)`

## 4.2.8.3. Arguments

`fd`
:   File descriptor returned by a previous call to [`open()`](ca-fopen.md#c.DTV.ca.open "open").

`msg`
:   Pointer to struct [`ca_msg`](ca_data_types.md#c.ca_msg "ca_msg").

## 4.2.8.4. Description

Sends a message via a CI CA module.

> **Note:**
>
> Please notice that, on most drivers, this is done by writing
> to the /dev/adapter?/ca? device node.

## 4.2.8.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

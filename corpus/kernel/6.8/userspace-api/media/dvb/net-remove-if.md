---
collection: kernel
version: "6.8"
title: "5.1.3. ioctl NET_REMOVE_IF"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/net-remove-if.html
fetched_at: 2026-08-21T03:39:35+00:00
---
# 5.1.3. ioctl NET_REMOVE_IF

## 5.1.3.1. Name

NET_REMOVE_IF - Removes a network interface.

## 5.1.3.2. Synopsis

NET_REMOVE_IF

`int ioctl(int fd, NET_REMOVE_IF, int ifnum)`

## 5.1.3.3. Arguments

`fd`
:   File descriptor returned by `open()`.

`net_if`
:   number of the interface to be removed

## 5.1.3.4. Description

The NET_REMOVE_IF ioctl deletes an interface previously created via
[NET_ADD_IF](net.md#net).

## 5.1.3.5. Return Value

On success 0 is returned, and [`ca_slot_info`](ca_data_types.md#c.ca_slot_info "ca_slot_info") is filled.

On error -1 is returned, and the `errno` variable is set
appropriately.

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

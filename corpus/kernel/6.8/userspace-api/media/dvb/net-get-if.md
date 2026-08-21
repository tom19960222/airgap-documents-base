---
collection: kernel
version: "6.8"
title: "5.1.4. ioctl NET_GET_IF"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/net-get-if.html
fetched_at: 2026-08-21T03:39:34+00:00
---
# 5.1.4. ioctl NET_GET_IF

## 5.1.4.1. Name

NET_GET_IF - Read the configuration data of an interface created via - [NET_ADD_IF](net.md#net).

## 5.1.4.2. Synopsis

NET_GET_IF

`int ioctl(int fd, NET_GET_IF, struct dvb_net_if *net_if)`

## 5.1.4.3. Arguments

`fd`
:   File descriptor returned by `open()`.

`net_if`
:   pointer to struct [`dvb_net_if`](net-types.md#c.dvb_net_if "dvb_net_if")

## 5.1.4.4. Description

The NET_GET_IF ioctl uses the interface number given by the struct
[`dvb_net_if`](net-types.md#c.dvb_net_if "dvb_net_if")::ifnum field and fills the content of
struct [`dvb_net_if`](net-types.md#c.dvb_net_if "dvb_net_if") with the packet ID and
encapsulation type used on such interface. If the interface was not
created yet with [NET_ADD_IF](net.md#net), it will return -1 and fill
the `errno` with `EINVAL` error code.

## 5.1.4.5. Return Value

On success 0 is returned, and [`ca_slot_info`](ca_data_types.md#c.ca_slot_info "ca_slot_info") is filled.

On error -1 is returned, and the `errno` variable is set
appropriately.

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

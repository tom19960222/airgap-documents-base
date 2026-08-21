---
collection: kernel
version: "6.8"
title: "5.1.2. ioctl NET_ADD_IF"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/net-add-if.html
fetched_at: 2026-08-21T03:39:33+00:00
---
# 5.1.2. ioctl NET_ADD_IF

## 5.1.2.1. Name

NET_ADD_IF - Creates a new network interface for a given Packet ID.

## 5.1.2.2. Synopsis

NET_ADD_IF

`int ioctl(int fd, NET_ADD_IF, struct dvb_net_if *net_if)`

## 5.1.2.3. Arguments

`fd`
:   File descriptor returned by `open()`.

`net_if`
:   pointer to struct [`dvb_net_if`](net-types.md#c.dvb_net_if "dvb_net_if")

## 5.1.2.4. Description

The NET_ADD_IF ioctl system call selects the Packet ID (PID) that
contains a TCP/IP traffic, the type of encapsulation to be used (MPE or
ULE) and the interface number for the new interface to be created. When
the system call successfully returns, a new virtual network interface is
created.

The struct [`dvb_net_if`](net-types.md#c.dvb_net_if "dvb_net_if")::ifnum field will be
filled with the number of the created interface.

## 5.1.2.5. Return Value

On success 0 is returned, and [`ca_slot_info`](ca_data_types.md#c.ca_slot_info "ca_slot_info") is filled.

On error -1 is returned, and the `errno` variable is set
appropriately.

The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

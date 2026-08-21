---
collection: kernel
version: "6.8"
title: "Linux kernel networking driver for Marvell's Octeon PCI Endpoint NIC"
source_url: https://www.kernel.org/doc/html/v6.8/networking/device_drivers/ethernet/marvell/octeon_ep.html
fetched_at: 2026-08-21T03:59:50+00:00
---
# Linux kernel networking driver for Marvell's Octeon PCI Endpoint NIC

Network driver for Marvell's Octeon PCI EndPoint NIC.
Copyright (c) 2020 Marvell International Ltd.

## Contents

- [Overview](octeon_ep.md#overview)
- [Supported Devices](octeon_ep.md#supported-devices)
- [Interface Control](octeon_ep.md#interface-control)

## Overview

This driver implements networking functionality of Marvell's Octeon PCI
EndPoint NIC.

## Supported Devices

Currently, this driver support following devices:
:   - Network controller: Cavium, Inc. Device b100
    - Network controller: Cavium, Inc. Device b200
    - Network controller: Cavium, Inc. Device b400
    - Network controller: Cavium, Inc. Device b900
    - Network controller: Cavium, Inc. Device ba00
    - Network controller: Cavium, Inc. Device bc00
    - Network controller: Cavium, Inc. Device bd00

## Interface Control

Network Interface control like changing mtu, link speed, link down/up are
done by writing command to mailbox command queue, a mailbox interface
implemented through a reserved region in BAR4.
This driver writes the commands into the mailbox and the firmware on the
Octeon device processes them. The firmware also sends unsolicited notifications
to driver for events suchs as link change, through notification queue
implemented as part of mailbox interface.

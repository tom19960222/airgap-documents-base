---
collection: kernel
version: "6.8"
title: "ISA Plug & Play support"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/isapnp.html
fetched_at: 2026-08-21T03:35:31+00:00
---
# ISA Plug & Play support

## Interface /proc/isapnp

The interface was removed in kernel 2.5.53. See pnp.rst for more details.

## Interface /proc/bus/isapnp

This directory allows access to ISA PnP cards and logical devices.
The regular files contain the contents of ISA PnP registers for
a logical device.

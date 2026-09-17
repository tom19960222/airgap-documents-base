---
collection: kernel
version: "6.17"
title: "FAILOVER"
source_url: https://www.kernel.org/doc/html/v6.17/networking/failover.html
fetched_at: 2026-09-16T16:32:56+00:00
---
# FAILOVER

## Overview

The failover module provides a generic interface for paravirtual drivers
to register a netdev and a set of ops with a failover instance. The ops
are used as event handlers that get called to handle netdev register/
unregister/link change/name change events on slave pci ethernet devices
with the same mac address as the failover netdev.

This enables paravirtual drivers to use a VF as an accelerated low latency
datapath. It also allows live migration of VMs with direct attached VFs by
failing over to the paravirtual datapath when the VF is unplugged.

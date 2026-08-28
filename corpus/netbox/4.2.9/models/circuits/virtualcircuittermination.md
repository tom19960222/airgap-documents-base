---
collection: netbox
version: "4.2.9"
title: "Virtual Circuit Terminations"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/circuits/virtualcircuittermination.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Virtual Circuit Terminations

!!! info "This feature was introduced in NetBox v4.2."

This model represents the connection of a virtual [interface](../dcim/interface.md) to a [virtual circuit](./virtualcircuit.md).

## Fields

### Virtual Circuit

The [virtual circuit](./virtualcircuit.md) to which the interface is connected.

### Interface

The [interface](../dcim/interface.md) connected to the virtual circuit.

### Role

The functional role of the termination. This depends on the virtual circuit's topology, which is typically either peer-to-peer or hub-and-spoke (multipoint). Valid choices include:

* Peer
* Hub
* Spoke

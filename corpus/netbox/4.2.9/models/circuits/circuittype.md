---
collection: netbox
version: "4.2.9"
title: "Circuit Types"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/circuits/circuittype.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Circuit Types

[Circuits](./circuit.md) are classified by functional type. These types are completely customizable, and are typically used to convey the type of service being delivered over a circuit. For example, you might define circuit types for:

* Internet transit
* Out-of-band connectivity
* Peering
* Private backhaul

## Fields

### Name

A unique human-friendly name.

### Slug

A unique URL-friendly identifier. (This value can be used for filtering.)

---
collection: netbox
version: "4.2.9"
title: "ASN Ranges"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/ipam/asnrange.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# ASN Ranges

Ranges can be defined to group [AS numbers](./asn.md) numerically and to facilitate their automatic provisioning. Each range must be assigned to a [RIR](./rir.md).

## Fields

### Name

A unique human-friendly name for the range.

### Slug

A unique URL-friendly identifier. (This value can be used for filtering.)

### RIR

The [Regional Internet Registry](./rir.md) or similar authority responsible for the allocation of AS numbers within this range.

### Start & End

The starting and ending numeric boundaries of the range (inclusive).

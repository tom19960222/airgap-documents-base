---
collection: netbox
version: "4.2.9"
title: "Manufacturers"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/dcim/manufacturer.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Manufacturers

A manufacturer represents the "make" of a device; e.g. Cisco or Dell. Each [device type](./devicetype.md) must be assigned to a manufacturer. ([Inventory items](./inventoryitem.md) and [platforms](./platform.md) may also be associated with manufacturers.)

## Fields

### Name

A unique human-friendly name.

### Slug

A unique URL-friendly identifier. (This value can be used for filtering.)

---
collection: netbox
version: "4.2.9"
title: "Wireless LAN Groups"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/wireless/wirelesslangroup.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Wireless LAN Groups

Wireless LAN groups can be used to organize and classify [wireless LANs](./wirelesslan.md). These groups are hierarchical: groups can be nested within parent groups. However, each wireless LAN may be assigned only to one group.

## Fields

### Parent

The parent wireless LAN group (if any).

### Name

A unique human-friendly name.

### Slug

A unique URL-friendly identifier. (This value can be used for filtering.)

---
collection: netbox
version: "4.2.9"
title: "Prefix/VLAN Roles"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/ipam/role.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Prefix/VLAN Roles

A role indicates the function of a prefix or VLAN. For example, you might define Data, Voice, and Security roles. Generally, a prefix will be assigned the same functional role as the VLAN to which it is assigned (if any).

## Fields

### Name

A unique human-friendly name.

### Slug

A unique URL-friendly identifier. (This value can be used for filtering.)

### Weight

A numeric weight employed to influence the ordering of roles. Roles with a lower weight will be listed before those with higher weights.

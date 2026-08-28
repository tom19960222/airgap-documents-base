---
collection: netbox
version: "4.2.9"
title: "Tenants"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/tenancy/tenant.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Tenants

A tenant represents a discrete grouping of resources used for administrative purposes. Typically, tenants are used to represent individual customers or internal departments within an organization. 

## Fields

### Name

A human-friendly name, unique to the assigned group.

### Slug

A URL-friendly identifier, unique to the assigned group. (This value can be used for filtering.)

### Group

The [tenant group](./tenantgroup.md) to which this tenant belongs (if any).

---
collection: netbox
version: "4.2.9"
title: "Tenant Groups"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/tenancy/tenantgroup.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Tenant Groups

[Tenants](./tenant.md) can be organized by custom groups. For instance, you might create one group called "Customers" and one called "Departments." The assignment of a tenant to a group is optional.

Tenant groups may be nested recursively to achieve a multi-level hierarchy. For example, you might have a group called "Customers" containing subgroups of individual tenants grouped by product or account team.

## Fields

### Parent

The parent tenant group (if any).

### Name

A unique human-friendly name.

### Slug

A unique URL-friendly identifier. (This value can be used for filtering.)

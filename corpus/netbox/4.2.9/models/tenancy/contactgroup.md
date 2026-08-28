---
collection: netbox
version: "4.2.9"
title: "Contact Groups"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/tenancy/contactgroup.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Contact Groups

[Contacts](./contact.md) can be organized into arbitrary groups. These groups can be recursively nested for convenience. Each contact within a group must have a unique name, but other attributes can be repeated.

## Fields

### Parent

The parent contact group (if any).

### Name

A unique human-friendly name.

### Slug

A unique URL-friendly identifier. (This value can be used for filtering.)

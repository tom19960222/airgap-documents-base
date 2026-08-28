---
collection: netbox
version: "4.2.9"
title: "Device Roles"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/dcim/devicerole.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Device Roles

Devices can be organized by functional roles, which are fully customizable by the user. For example, you might create roles for core switches, distribution switches, and access switches within your network.

## Fields

### Name

A unique human-friendly name.

### Slug

A unique URL-friendly identifier. (This value can be used for filtering.)

### Color

The color used when displaying the role in the NetBox UI.

### VM Role

If selected, this role may be assigned to [virtual machines](../virtualization/virtualmachine.md)

### Configuration Template

The default [configuration template](../extras/configtemplate.md) for devices assigned to this role.

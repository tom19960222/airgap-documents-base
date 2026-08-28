---
collection: netbox
version: "4.2.9"
title: "Power Panel"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/dcim/powerpanel.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Power Panel

A power panel represents the origin point in NetBox for electrical power being disseminated by one or more [power feeds](./powerfeed.md). In a data center environment, one power panel often serves a group of racks, with an individual power feed extending to each rack, though this is not always the case. It is common to have two sets of panels and feeds arranged in parallel to provide redundant power to each rack.

!!! note
    NetBox does not model the mechanism by which power is delivered to a power panel. Power panels define the root level of the power distribution hierarchy in NetBox.

## Fields

### Site

The [site](./site.md) in which the power panel resides.

### Location

A specific [location](./location.md) within the assigned site where the power panel is installed.

### Name

The power panel's name. Must be unique to the assigned site.

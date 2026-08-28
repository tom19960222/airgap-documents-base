---
collection: netbox
version: "4.2.9"
title: "Regions"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/dcim/region.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Regions

[Sites](./site.md) can be arranged geographically using regions. A region might represent a continent, country, city, campus, or other area depending on your use case. Regions can be nested recursively to construct a hierarchy. For example, you might define several country regions, and within each of those several state or city regions to which sites are assigned.

## Fields

### Parent

The parent region, if any.

### Name

The region's name. Must be unique to the parent region, if one is assigned.

### Slug

A unique URL-friendly identifier. (This value can be used for filtering.)

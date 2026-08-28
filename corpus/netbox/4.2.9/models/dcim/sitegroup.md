---
collection: netbox
version: "4.2.9"
title: "Site Groups"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/dcim/sitegroup.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Site Groups

Like [regions](./region.md), site groups can be used to organize [sites](./site.md). Whereas regions are intended to provide geographic organization, site groups can be used to classify sites by role or function. Also like regions, site groups can be nested to form a hierarchy. Sites which belong to a child group are also considered to be members of all its parent groups.

## Fields

### Parent

The parent site group, if any.

### Name

The site group's name. Must be unique to the parent group, if one is assigned.

### Slug

A unique URL-friendly identifier. (This value can be used for filtering.)

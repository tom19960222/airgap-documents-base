---
collection: netbox
version: "4.2.9"
title: "Tags"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/extras/tag.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Tags

Tags are user-defined labels which can be applied to a variety of objects within NetBox. They can be used to establish dimensions of organization beyond the relationships built into NetBox. For example, you might create a tag to identify a particular ownership or condition across several types of objects.

## Fields

### Name

A unique human-friendly label for the tag.

### Slug

A unique URL-friendly identifier. (This value will be used for filtering.) This is automatically generated from the tag's name, but can be altered as needed.

### Color

The color to use when displaying the tag in the NetBox UI.

### Object Types

The assignment of a tag may be limited to a prescribed set of objects. For example, it may be desirable to limit the application of a specific tag to only devices and virtual machines.

If no object types are specified, the tag will be assignable to any type of object.

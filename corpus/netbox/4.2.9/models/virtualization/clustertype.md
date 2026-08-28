---
collection: netbox
version: "4.2.9"
title: "Cluster Types"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/virtualization/clustertype.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Cluster Types

A cluster type represents a technology or mechanism by which a [cluster](./cluster.md) is formed. For example, you might create a cluster type named "VMware vSphere" for a locally hosted cluster or "DigitalOcean NYC3" for one hosted by a cloud provider.

## Fields

### Name

A unique human-friendly name.

### Slug

A unique URL-friendly identifier. (This value can be used for filtering.)

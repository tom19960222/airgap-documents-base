---
collection: netbox
version: "4.2.9"
title: "Route Targets"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/ipam/routetarget.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Route Targets

A route target is a particular type of [extended BGP community](https://tools.ietf.org/html/rfc4360#section-4) used to control the redistribution of routes among VRF tables in a network. Route targets can be assigned to individual VRFs in NetBox as import or export targets (or both) to model this exchange in an L3VPN. Each route target must be given a unique name, which should be in a format prescribed by [RFC 4364](https://tools.ietf.org/html/rfc4364#section-4.2), similar to a VR route distinguisher.

## Fields

### Name

The route target identifier formatted in accordance with [RFC 4360](https://tools.ietf.org/html/rfc4360).

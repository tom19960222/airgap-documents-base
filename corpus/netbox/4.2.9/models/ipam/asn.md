---
collection: netbox
version: "4.2.9"
title: "ASNs"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/ipam/asn.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# ASNs

An Autonomous System Number (ASN) is a numeric identifier used in the Border Gateway Protocol (BGP) to identify which [autonomous system](https://en.wikipedia.org/wiki/Autonomous_system_%28Internet%29) a particular prefix is originating from or transiting through. NetBox supports both 16- and 32-bit ASNs.

ASNs must be globally unique within NetBox, and may be allocated from within a [defined range](./asnrange.md). Each ASN may be assigned to multiple [sites](../dcim/site.md).

## Fields

### AS Number

The 16- or 32-bit AS number.

### RIR

The [Regional Internet Registry](./rir.md) or similar authority responsible for the allocation of this particular ASN.

### Sites

The [site(s)](../dcim/site.md) to which this ASN is assigned.

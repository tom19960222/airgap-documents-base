---
collection: netbox
version: "4.2.9"
title: "IPSec Policy"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/vpn/ipsecpolicy.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# IPSec Policy

An [IPSec](https://en.wikipedia.org/wiki/IPsec) policy defines a set of [proposals](./ikeproposal.md) to be used in the formation of IPSec tunnels. A perfect forward secrecy (PFS) group may optionally also be defined. These policies are referenced by [IPSec profiles](./ipsecprofile.md).

## Fields

### Name

The unique user-assigned name for the policy.

### Proposals

One or more [IPSec proposals](./ipsecproposal.md) supported for use by this policy.

### PFS Group

The [perfect forward secrecy (PFS)](https://en.wikipedia.org/wiki/Forward_secrecy) group supported by this policy (optional).

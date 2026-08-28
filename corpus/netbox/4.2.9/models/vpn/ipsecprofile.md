---
collection: netbox
version: "4.2.9"
title: "IPSec Profile"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/vpn/ipsecprofile.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# IPSec Profile

An [IPSec](https://en.wikipedia.org/wiki/IPsec) profile defines an [IKE policy](./ikepolicy.md), [IPSec policy](./ipsecpolicy.md), and IPSec mode used for establishing an IPSec tunnel.

## Fields

### Name

The unique user-assigned name for the profile.

### Mode

The IPSec mode employed by the profile: Encapsulating Security Payload (ESP) or Authentication Header (AH).

### IKE Policy

The [IKE policy](./ikepolicy.md) associated with the profile.

### IPSec Policy

The [IPSec policy](./ipsecpolicy.md) associated with the profile.

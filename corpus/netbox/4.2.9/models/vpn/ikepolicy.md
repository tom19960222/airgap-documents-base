---
collection: netbox
version: "4.2.9"
title: "IKE Policies"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/vpn/ikepolicy.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# IKE Policies

An [Internet Key Exchange (IKE)](https://en.wikipedia.org/wiki/Internet_Key_Exchange) policy defines an IKE version, mode, and set of [proposals](./ikeproposal.md) to be used in IKE negotiation. These policies are referenced by [IPSec profiles](./ipsecprofile.md).

## Fields

### Name

The unique user-assigned name for the policy.

### Version

The IKE version employed (v1 or v2).

### Mode

The mode employed (main or aggressive) when IKEv1 is in use. This setting is not supported for IKEv2.

### Proposals

One or more [IKE proposals](./ikeproposal.md) supported for use by this policy.

### Pre-shared Key

A pre-shared secret key associated with this policy (optional).

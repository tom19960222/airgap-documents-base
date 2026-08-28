---
collection: netbox
version: "4.2.9"
title: "Provider Networks"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/circuits/providernetwork.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Provider Networks

This model can be used to represent the boundary of a provider network, the details of which are unknown or unimportant to the NetBox user. For example, it might represent a provider's regional MPLS network to which multiple circuits provide connectivity.

## Fields

### Provider

The [provider](./provider.md) responsible for the operation of this network.

### Name

A human-friendly name, unique to the provider.

### Service ID

An arbitrary identifier used as an alternate reference for the type of connectivity or service being delivered.

---
collection: netbox
version: "4.2.9"
title: "L2VPN"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/vpn/l2vpn.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# L2VPN

A L2VPN object is NetBox is a representation of a layer 2 bridge technology such as VXLAN, VPLS, or EPL. Each L2VPN can be identified by name as well as by an optional unique identifier (VNI would be an example). Once created, L2VPNs can be terminated to [interfaces](../dcim/interface.md) and [VLANs](../ipam/vlan.md).

## Fields

### Name

A unique human-friendly name.

### Slug

A unique URL-friendly identifier. (This value can be used for filtering.)

### Type

The technology employed in forming and operating the L2VPN. Choices include:

* VPLS
* VPWS
* EPL
* EVPL
* EP-LAN
* EVP-LAN
* EP-TREE
* EVP-TREE
* VXLAN
* VXLAN-EVPN
* MPLS-EVPN
* PBB-EVPN
* EVPN-VPWS

!!! note
    Designating the type as VPWS, EPL, EP-LAN, EP-TREE will limit the L2VPN instance to two terminations.

### Identifier

An optional numeric identifier. This can be used to track a pseudowire ID, for example.

### Import & Export Targets

The [route targets](../ipam/routetarget.md) associated with this L2VPN to control the import and export of forwarding information.

---
collection: netbox
version: "4.2.9"
title: "L2VPN Termination"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/vpn/l2vpntermination.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# L2VPN Termination

A L2VPN termination is the attachment of an [L2VPN](./l2vpn.md) to an [interface](../dcim/interface.md) or [VLAN](../ipam/vlan.md). Note that the L2VPNs of the following types may have only two terminations assigned to them:

* VPWS
* EPL
* EP-LAN
* EP-TREE

## Fields

### L2VPN

The [L2VPN](./l2vpn.md) instance.

### VLAN or Interface

The [VLAN](../ipam/vlan.md), [device interface](../dcim/interface.md), or [virtual machine interface](../virtualization/virtualmachine.md) attached to the L2VPN.

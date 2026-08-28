---
collection: netbox
version: "4.2.9"
title: "L2VPN & Overlay"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/features/l2vpn-overlay.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# L2VPN & Overlay

L2VPN and overlay networks, such as VXLAN and EVPN, can be defined in NetBox and tied to interfaces and VLANs. This allows for easy tracking of overlay assets and their relationships with underlay resources.

Each L2VPN instance has a type and optional unique identifier. Like VRFs, L2VPNs can also have import and export route targets assigned to them. Terminations can then be created to assign VLANs and/or device and virtual machine interfaces to the overlay.

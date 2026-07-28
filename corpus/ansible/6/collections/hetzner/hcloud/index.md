---
collection: ansible
version: "6"
title: "Hetzner.Hcloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/index.html
fetched_at: 2026-07-27T16:41:58+00:00
---
# Hetzner.Hcloud

Collection version 1.9.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

A Collection for managing Hetzner Cloud resources

**Author:**

- Hetzner Cloud (github.com/hetznercloud)

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)

## [Plugin Index](index.md#id2)

These are the plugins in the hetzner.hcloud collection:

### Modules

- [hcloud_certificate module](hcloud_certificate_module.md#ansible-collections-hetzner-hcloud-hcloud-certificate-module) – Create and manage certificates on the Hetzner Cloud.
- [hcloud_certificate_info module](hcloud_certificate_info_module.md#ansible-collections-hetzner-hcloud-hcloud-certificate-info-module) – Gather infos about your Hetzner Cloud certificates.
- [hcloud_datacenter_info module](hcloud_datacenter_info_module.md#ansible-collections-hetzner-hcloud-hcloud-datacenter-info-module) – Gather info about the Hetzner Cloud datacenters.
- [hcloud_firewall module](hcloud_firewall_module.md#ansible-collections-hetzner-hcloud-hcloud-firewall-module) – Create and manage firewalls on the Hetzner Cloud.
- [hcloud_floating_ip module](hcloud_floating_ip_module.md#ansible-collections-hetzner-hcloud-hcloud-floating-ip-module) – Create and manage cloud Floating IPs on the Hetzner Cloud.
- [hcloud_floating_ip_info module](hcloud_floating_ip_info_module.md#ansible-collections-hetzner-hcloud-hcloud-floating-ip-info-module) – Gather infos about the Hetzner Cloud Floating IPs.
- [hcloud_image_info module](hcloud_image_info_module.md#ansible-collections-hetzner-hcloud-hcloud-image-info-module) – Gather infos about your Hetzner Cloud images.
- [hcloud_load_balancer module](hcloud_load_balancer_module.md#ansible-collections-hetzner-hcloud-hcloud-load-balancer-module) – Create and manage cloud Load Balancers on the Hetzner Cloud.
- [hcloud_load_balancer_info module](hcloud_load_balancer_info_module.md#ansible-collections-hetzner-hcloud-hcloud-load-balancer-info-module) – Gather infos about your Hetzner Cloud Load Balancers.
- [hcloud_load_balancer_network module](hcloud_load_balancer_network_module.md#ansible-collections-hetzner-hcloud-hcloud-load-balancer-network-module) – Manage the relationship between Hetzner Cloud Networks and Load Balancers
- [hcloud_load_balancer_service module](hcloud_load_balancer_service_module.md#ansible-collections-hetzner-hcloud-hcloud-load-balancer-service-module) – Create and manage the services of cloud Load Balancers on the Hetzner Cloud.
- [hcloud_load_balancer_target module](hcloud_load_balancer_target_module.md#ansible-collections-hetzner-hcloud-hcloud-load-balancer-target-module) – Manage Hetzner Cloud Load Balancer targets
- [hcloud_load_balancer_type_info module](hcloud_load_balancer_type_info_module.md#ansible-collections-hetzner-hcloud-hcloud-load-balancer-type-info-module) – Gather infos about the Hetzner Cloud Load Balancer types.
- [hcloud_location_info module](hcloud_location_info_module.md#ansible-collections-hetzner-hcloud-hcloud-location-info-module) – Gather infos about your Hetzner Cloud locations.
- [hcloud_network module](hcloud_network_module.md#ansible-collections-hetzner-hcloud-hcloud-network-module) – Create and manage cloud Networks on the Hetzner Cloud.
- [hcloud_network_info module](hcloud_network_info_module.md#ansible-collections-hetzner-hcloud-hcloud-network-info-module) – Gather info about your Hetzner Cloud networks.
- [hcloud_placement_group module](hcloud_placement_group_module.md#ansible-collections-hetzner-hcloud-hcloud-placement-group-module) – Create and manage placement groups on the Hetzner Cloud.
- [hcloud_primary_ip module](hcloud_primary_ip_module.md#ansible-collections-hetzner-hcloud-hcloud-primary-ip-module) – Create and manage cloud Primary IPs on the Hetzner Cloud.
- [hcloud_rdns module](hcloud_rdns_module.md#ansible-collections-hetzner-hcloud-hcloud-rdns-module) – Create and manage reverse DNS entries on the Hetzner Cloud.
- [hcloud_route module](hcloud_route_module.md#ansible-collections-hetzner-hcloud-hcloud-route-module) – Create and delete cloud routes on the Hetzner Cloud.
- [hcloud_server module](hcloud_server_module.md#ansible-collections-hetzner-hcloud-hcloud-server-module) – Create and manage cloud servers on the Hetzner Cloud.
- [hcloud_server_info module](hcloud_server_info_module.md#ansible-collections-hetzner-hcloud-hcloud-server-info-module) – Gather infos about your Hetzner Cloud servers.
- [hcloud_server_network module](hcloud_server_network_module.md#ansible-collections-hetzner-hcloud-hcloud-server-network-module) – Manage the relationship between Hetzner Cloud Networks and servers
- [hcloud_server_type_info module](hcloud_server_type_info_module.md#ansible-collections-hetzner-hcloud-hcloud-server-type-info-module) – Gather infos about the Hetzner Cloud server types.
- [hcloud_ssh_key module](hcloud_ssh_key_module.md#ansible-collections-hetzner-hcloud-hcloud-ssh-key-module) – Create and manage ssh keys on the Hetzner Cloud.
- [hcloud_ssh_key_info module](hcloud_ssh_key_info_module.md#ansible-collections-hetzner-hcloud-hcloud-ssh-key-info-module) – Gather infos about your Hetzner Cloud ssh_keys.
- [hcloud_subnetwork module](hcloud_subnetwork_module.md#ansible-collections-hetzner-hcloud-hcloud-subnetwork-module) – Manage cloud subnetworks on the Hetzner Cloud.
- [hcloud_volume module](hcloud_volume_module.md#ansible-collections-hetzner-hcloud-hcloud-volume-module) – Create and manage block Volume on the Hetzner Cloud.
- [hcloud_volume_info module](hcloud_volume_info_module.md#ansible-collections-hetzner-hcloud-hcloud-volume-info-module) – Gather infos about your Hetzner Cloud Volumes.

### Inventory Plugins

- [hcloud inventory](hcloud_inventory.md#ansible-collections-hetzner-hcloud-hcloud-inventory) – Ansible dynamic inventory plugin for the Hetzner Cloud.

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

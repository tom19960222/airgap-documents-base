---
collection: ansible
version: "8"
title: "Ngine_Io.Cloudstack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/index.html
fetched_at: 2026-07-28T01:02:52+00:00
---
# Ngine_Io.Cloudstack

Collection version 2.3.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Collection for Apache CloudStack based clouds

**Authors:**

- René Moser <[mail@renemoser.net](mailto:mail%40renemoser.net)>
- David Passante (@dpassante)
- Netservers Ltd. <[support@netservers.co.uk](mailto:support%40netservers.co.uk)>
- Patryk D. Cichy <[patryk.d.cichy@gmail.com](mailto:patryk.d.cichy%40gmail.com)>
- Darren Worrall <[darren@iweb.co.uk](mailto:darren%40iweb.co.uk)>
- Marc-Aurèle Brothier (@marcaurele)
- Jefferson Girão <[jefferson@girao.net](mailto:jefferson%40girao.net)>
- Gregor Riepl (@onitake)
- Rafael del Valle (@rvalle)

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)

## [Plugin Index](index.md#id2)

These are the plugins in the ngine_io.cloudstack collection:

### Modules

- [cs_account module](cs_account_module.md#ansible-collections-ngine-io-cloudstack-cs-account-module) – Manages accounts on Apache CloudStack based clouds.
- [cs_affinitygroup module](cs_affinitygroup_module.md#ansible-collections-ngine-io-cloudstack-cs-affinitygroup-module) – Manages affinity groups on Apache CloudStack based clouds.
- [cs_cluster module](cs_cluster_module.md#ansible-collections-ngine-io-cloudstack-cs-cluster-module) – Manages host clusters on Apache CloudStack based clouds.
- [cs_configuration module](cs_configuration_module.md#ansible-collections-ngine-io-cloudstack-cs-configuration-module) – Manages configuration on Apache CloudStack based clouds.
- [cs_disk_offering module](cs_disk_offering_module.md#ansible-collections-ngine-io-cloudstack-cs-disk-offering-module) – Manages disk offerings on Apache CloudStack based clouds.
- [cs_domain module](cs_domain_module.md#ansible-collections-ngine-io-cloudstack-cs-domain-module) – Manages domains on Apache CloudStack based clouds.
- [cs_facts module](cs_facts_module.md#ansible-collections-ngine-io-cloudstack-cs-facts-module) – Gather facts on instances of Apache CloudStack based clouds.
- [cs_firewall module](cs_firewall_module.md#ansible-collections-ngine-io-cloudstack-cs-firewall-module) – Manages firewall rules on Apache CloudStack based clouds.
- [cs_host module](cs_host_module.md#ansible-collections-ngine-io-cloudstack-cs-host-module) – Manages hosts on Apache CloudStack based clouds.
- [cs_image_store module](cs_image_store_module.md#ansible-collections-ngine-io-cloudstack-cs-image-store-module) – Manages CloudStack Image Stores.
- [cs_instance module](cs_instance_module.md#ansible-collections-ngine-io-cloudstack-cs-instance-module) – Manages instances and virtual machines on Apache CloudStack based clouds.
- [cs_instance_info module](cs_instance_info_module.md#ansible-collections-ngine-io-cloudstack-cs-instance-info-module) – Gathering information from the API of instances from Apache CloudStack based clouds.
- [cs_instance_nic module](cs_instance_nic_module.md#ansible-collections-ngine-io-cloudstack-cs-instance-nic-module) – Manages NICs of an instance on Apache CloudStack based clouds.
- [cs_instance_nic_secondaryip module](cs_instance_nic_secondaryip_module.md#ansible-collections-ngine-io-cloudstack-cs-instance-nic-secondaryip-module) – Manages secondary IPs of an instance on Apache CloudStack based clouds.
- [cs_instance_password_reset module](cs_instance_password_reset_module.md#ansible-collections-ngine-io-cloudstack-cs-instance-password-reset-module) – Allows resetting VM the default passwords on Apache CloudStack based clouds.
- [cs_instancegroup module](cs_instancegroup_module.md#ansible-collections-ngine-io-cloudstack-cs-instancegroup-module) – Manages instance groups on Apache CloudStack based clouds.
- [cs_ip_address module](cs_ip_address_module.md#ansible-collections-ngine-io-cloudstack-cs-ip-address-module) – Manages public IP address associations on Apache CloudStack based clouds.
- [cs_iso module](cs_iso_module.md#ansible-collections-ngine-io-cloudstack-cs-iso-module) – Manages ISO images on Apache CloudStack based clouds.
- [cs_loadbalancer_rule module](cs_loadbalancer_rule_module.md#ansible-collections-ngine-io-cloudstack-cs-loadbalancer-rule-module) – Manages load balancer rules on Apache CloudStack based clouds.
- [cs_loadbalancer_rule_member module](cs_loadbalancer_rule_member_module.md#ansible-collections-ngine-io-cloudstack-cs-loadbalancer-rule-member-module) – Manages load balancer rule members on Apache CloudStack based clouds.
- [cs_network module](cs_network_module.md#ansible-collections-ngine-io-cloudstack-cs-network-module) – Manages networks on Apache CloudStack based clouds.
- [cs_network_acl module](cs_network_acl_module.md#ansible-collections-ngine-io-cloudstack-cs-network-acl-module) – Manages network access control lists (ACL) on Apache CloudStack based clouds.
- [cs_network_acl_rule module](cs_network_acl_rule_module.md#ansible-collections-ngine-io-cloudstack-cs-network-acl-rule-module) – Manages network access control list (ACL) rules on Apache CloudStack based clouds.
- [cs_network_offering module](cs_network_offering_module.md#ansible-collections-ngine-io-cloudstack-cs-network-offering-module) – Manages network offerings on Apache CloudStack based clouds.
- [cs_physical_network module](cs_physical_network_module.md#ansible-collections-ngine-io-cloudstack-cs-physical-network-module) – Manages physical networks on Apache CloudStack based clouds.
- [cs_pod module](cs_pod_module.md#ansible-collections-ngine-io-cloudstack-cs-pod-module) – Manages pods on Apache CloudStack based clouds.
- [cs_portforward module](cs_portforward_module.md#ansible-collections-ngine-io-cloudstack-cs-portforward-module) – Manages port forwarding rules on Apache CloudStack based clouds.
- [cs_project module](cs_project_module.md#ansible-collections-ngine-io-cloudstack-cs-project-module) – Manages projects on Apache CloudStack based clouds.
- [cs_region module](cs_region_module.md#ansible-collections-ngine-io-cloudstack-cs-region-module) – Manages regions on Apache CloudStack based clouds.
- [cs_resourcelimit module](cs_resourcelimit_module.md#ansible-collections-ngine-io-cloudstack-cs-resourcelimit-module) – Manages resource limits on Apache CloudStack based clouds.
- [cs_role module](cs_role_module.md#ansible-collections-ngine-io-cloudstack-cs-role-module) – Manages user roles on Apache CloudStack based clouds.
- [cs_role_permission module](cs_role_permission_module.md#ansible-collections-ngine-io-cloudstack-cs-role-permission-module) – Manages role permissions on Apache CloudStack based clouds.
- [cs_router module](cs_router_module.md#ansible-collections-ngine-io-cloudstack-cs-router-module) – Manages routers on Apache CloudStack based clouds.
- [cs_securitygroup module](cs_securitygroup_module.md#ansible-collections-ngine-io-cloudstack-cs-securitygroup-module) – Manages security groups on Apache CloudStack based clouds.
- [cs_securitygroup_rule module](cs_securitygroup_rule_module.md#ansible-collections-ngine-io-cloudstack-cs-securitygroup-rule-module) – Manages security group rules on Apache CloudStack based clouds.
- [cs_service_offering module](cs_service_offering_module.md#ansible-collections-ngine-io-cloudstack-cs-service-offering-module) – Manages service offerings on Apache CloudStack based clouds.
- [cs_snapshot_policy module](cs_snapshot_policy_module.md#ansible-collections-ngine-io-cloudstack-cs-snapshot-policy-module) – Manages volume snapshot policies on Apache CloudStack based clouds.
- [cs_sshkeypair module](cs_sshkeypair_module.md#ansible-collections-ngine-io-cloudstack-cs-sshkeypair-module) – Manages SSH keys on Apache CloudStack based clouds.
- [cs_staticnat module](cs_staticnat_module.md#ansible-collections-ngine-io-cloudstack-cs-staticnat-module) – Manages static NATs on Apache CloudStack based clouds.
- [cs_storage_pool module](cs_storage_pool_module.md#ansible-collections-ngine-io-cloudstack-cs-storage-pool-module) – Manages Primary Storage Pools on Apache CloudStack based clouds.
- [cs_template module](cs_template_module.md#ansible-collections-ngine-io-cloudstack-cs-template-module) – Manages templates on Apache CloudStack based clouds.
- [cs_traffic_type module](cs_traffic_type_module.md#ansible-collections-ngine-io-cloudstack-cs-traffic-type-module) – Manages traffic types on CloudStack Physical Networks
- [cs_user module](cs_user_module.md#ansible-collections-ngine-io-cloudstack-cs-user-module) – Manages users on Apache CloudStack based clouds.
- [cs_vlan_ip_range module](cs_vlan_ip_range_module.md#ansible-collections-ngine-io-cloudstack-cs-vlan-ip-range-module) – Manages VLAN IP ranges on Apache CloudStack based clouds.
- [cs_vmsnapshot module](cs_vmsnapshot_module.md#ansible-collections-ngine-io-cloudstack-cs-vmsnapshot-module) – Manages VM snapshots on Apache CloudStack based clouds.
- [cs_volume module](cs_volume_module.md#ansible-collections-ngine-io-cloudstack-cs-volume-module) – Manages volumes on Apache CloudStack based clouds.
- [cs_vpc module](cs_vpc_module.md#ansible-collections-ngine-io-cloudstack-cs-vpc-module) – Manages VPCs on Apache CloudStack based clouds.
- [cs_vpc_offering module](cs_vpc_offering_module.md#ansible-collections-ngine-io-cloudstack-cs-vpc-offering-module) – Manages vpc offerings on Apache CloudStack based clouds.
- [cs_vpn_connection module](cs_vpn_connection_module.md#ansible-collections-ngine-io-cloudstack-cs-vpn-connection-module) – Manages site-to-site VPN connections on Apache CloudStack based clouds.
- [cs_vpn_customer_gateway module](cs_vpn_customer_gateway_module.md#ansible-collections-ngine-io-cloudstack-cs-vpn-customer-gateway-module) – Manages site-to-site VPN customer gateway configurations on Apache CloudStack based clouds.
- [cs_vpn_gateway module](cs_vpn_gateway_module.md#ansible-collections-ngine-io-cloudstack-cs-vpn-gateway-module) – Manages site-to-site VPN gateways on Apache CloudStack based clouds.
- [cs_zone module](cs_zone_module.md#ansible-collections-ngine-io-cloudstack-cs-zone-module) – Manages zones on Apache CloudStack based clouds.
- [cs_zone_info module](cs_zone_info_module.md#ansible-collections-ngine-io-cloudstack-cs-zone-info-module) – Gathering information about zones from Apache CloudStack based clouds.

### Inventory Plugins

- [instance inventory](instance_inventory.md#ansible-collections-ngine-io-cloudstack-instance-inventory) – Apache CloudStack instance inventory source

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

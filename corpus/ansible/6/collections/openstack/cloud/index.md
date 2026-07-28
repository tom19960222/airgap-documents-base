---
collection: ansible
version: "6"
title: "Openstack.Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/index.html
fetched_at: 2026-07-27T16:42:07+00:00
---
# Openstack.Cloud

Collection version 1.10.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Openstack Ansible modules

**Author:**

- Openstack

**Supported ansible-core versions:**

- 2.8 or newer

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

## [Plugin Index](index.md#id2)

These are the plugins in the openstack.cloud collection:

### Modules

- [address_scope module](address_scope_module.md#ansible-collections-openstack-cloud-address-scope-module) – Create or delete address scopes from OpenStack
- [auth module](auth_module.md#ansible-collections-openstack-cloud-auth-module) – Retrieve an auth token
- [baremetal_inspect module](baremetal_inspect_module.md#ansible-collections-openstack-cloud-baremetal-inspect-module) – Explicitly triggers baremetal node introspection in ironic.
- [baremetal_node module](baremetal_node_module.md#ansible-collections-openstack-cloud-baremetal-node-module) – Create/Delete Bare Metal Resources from OpenStack
- [baremetal_node_action module](baremetal_node_action_module.md#ansible-collections-openstack-cloud-baremetal-node-action-module) – Activate/Deactivate Bare Metal Resources from OpenStack
- [baremetal_node_info module](baremetal_node_info_module.md#ansible-collections-openstack-cloud-baremetal-node-info-module) – Retrieve information about Bare Metal nodes from OpenStack
- [baremetal_port module](baremetal_port_module.md#ansible-collections-openstack-cloud-baremetal-port-module) – Create/Delete Bare Metal port Resources from OpenStack
- [baremetal_port_info module](baremetal_port_info_module.md#ansible-collections-openstack-cloud-baremetal-port-info-module) – Retrieve information about Bare Metal ports from OpenStack
- [catalog_service module](catalog_service_module.md#ansible-collections-openstack-cloud-catalog-service-module) – Manage OpenStack Identity services
- [coe_cluster module](coe_cluster_module.md#ansible-collections-openstack-cloud-coe-cluster-module) – Add/Remove COE cluster from OpenStack Cloud
- [coe_cluster_template module](coe_cluster_template_module.md#ansible-collections-openstack-cloud-coe-cluster-template-module) – Add/Remove COE cluster template from OpenStack Cloud
- [compute_flavor module](compute_flavor_module.md#ansible-collections-openstack-cloud-compute-flavor-module) – Manage OpenStack compute flavors
- [compute_flavor_info module](compute_flavor_info_module.md#ansible-collections-openstack-cloud-compute-flavor-info-module) – Retrieve information about one or more flavors
- [compute_service_info module](compute_service_info_module.md#ansible-collections-openstack-cloud-compute-service-info-module) – Retrieve information about one or more OpenStack compute services
- [config module](config_module.md#ansible-collections-openstack-cloud-config-module) – Get OpenStack Client config
- [dns_zone module](dns_zone_module.md#ansible-collections-openstack-cloud-dns-zone-module) – Manage OpenStack DNS zones
- [dns_zone_info module](dns_zone_info_module.md#ansible-collections-openstack-cloud-dns-zone-info-module) – Getting information about dns zones
- [endpoint module](endpoint_module.md#ansible-collections-openstack-cloud-endpoint-module) – Manage OpenStack Identity service endpoints
- [federation_idp module](federation_idp_module.md#ansible-collections-openstack-cloud-federation-idp-module) – manage a federation Identity Provider
- [federation_idp_info module](federation_idp_info_module.md#ansible-collections-openstack-cloud-federation-idp-info-module) – Get the information about the available federation identity providers
- [federation_mapping module](federation_mapping_module.md#ansible-collections-openstack-cloud-federation-mapping-module) – Manage a federation mapping
- [federation_mapping_info module](federation_mapping_info_module.md#ansible-collections-openstack-cloud-federation-mapping-info-module) – Get the information about the available federation mappings
- [floating_ip module](floating_ip_module.md#ansible-collections-openstack-cloud-floating-ip-module) – Add/Remove floating IP from an instance
- [floating_ip_info module](floating_ip_info_module.md#ansible-collections-openstack-cloud-floating-ip-info-module) – Get information about floating ips
- [group_assignment module](group_assignment_module.md#ansible-collections-openstack-cloud-group-assignment-module) – Associate OpenStack Identity users and groups
- [host_aggregate module](host_aggregate_module.md#ansible-collections-openstack-cloud-host-aggregate-module) – Manage OpenStack host aggregates
- [identity_domain module](identity_domain_module.md#ansible-collections-openstack-cloud-identity-domain-module) – Manage OpenStack Identity Domains
- [identity_domain_info module](identity_domain_info_module.md#ansible-collections-openstack-cloud-identity-domain-info-module) – Retrieve information about one or more OpenStack domains
- [identity_group module](identity_group_module.md#ansible-collections-openstack-cloud-identity-group-module) – Manage OpenStack Identity Groups
- [identity_group_info module](identity_group_info_module.md#ansible-collections-openstack-cloud-identity-group-info-module) – Retrieve info about one or more OpenStack groups
- [identity_role module](identity_role_module.md#ansible-collections-openstack-cloud-identity-role-module) – Manage OpenStack Identity Roles
- [identity_role_info module](identity_role_info_module.md#ansible-collections-openstack-cloud-identity-role-info-module) – Retrieve information about roles
- [identity_user module](identity_user_module.md#ansible-collections-openstack-cloud-identity-user-module) – Manage OpenStack Identity Users
- [identity_user_info module](identity_user_info_module.md#ansible-collections-openstack-cloud-identity-user-info-module) – Retrieve information about one or more OpenStack users
- [image module](image_module.md#ansible-collections-openstack-cloud-image-module) – Add/Delete images from OpenStack Cloud
- [image_info module](image_info_module.md#ansible-collections-openstack-cloud-image-info-module) – Retrieve information about an image within OpenStack.
- [keypair module](keypair_module.md#ansible-collections-openstack-cloud-keypair-module) – Add/Delete a keypair from OpenStack
- [keypair_info module](keypair_info_module.md#ansible-collections-openstack-cloud-keypair-info-module) – Get information about keypairs from OpenStack
- [keystone_federation_protocol module](keystone_federation_protocol_module.md#ansible-collections-openstack-cloud-keystone-federation-protocol-module) – manage a federation Protocol
- [keystone_federation_protocol_info module](keystone_federation_protocol_info_module.md#ansible-collections-openstack-cloud-keystone-federation-protocol-info-module) – get information about federation Protocols
- [lb_health_monitor module](lb_health_monitor_module.md#ansible-collections-openstack-cloud-lb-health-monitor-module) – Add/Delete a health m nonitor to a pool in the load balancing service from OpenStack Cloud
- [lb_listener module](lb_listener_module.md#ansible-collections-openstack-cloud-lb-listener-module) – Add/Delete a listener for a load balancer from OpenStack Cloud
- [lb_member module](lb_member_module.md#ansible-collections-openstack-cloud-lb-member-module) – Add/Delete a member for a pool in load balancer from OpenStack Cloud
- [lb_pool module](lb_pool_module.md#ansible-collections-openstack-cloud-lb-pool-module) – Add/Delete a pool in the load balancing service from OpenStack Cloud
- [loadbalancer module](loadbalancer_module.md#ansible-collections-openstack-cloud-loadbalancer-module) – Add/Delete load balancer from OpenStack Cloud
- [network module](network_module.md#ansible-collections-openstack-cloud-network-module) – Creates/removes networks from OpenStack
- [networks_info module](networks_info_module.md#ansible-collections-openstack-cloud-networks-info-module) – Retrieve information about one or more OpenStack networks.
- [neutron_rbac_policies_info module](neutron_rbac_policies_info_module.md#ansible-collections-openstack-cloud-neutron-rbac-policies-info-module) – Fetch Neutron policies.
- [neutron_rbac_policy module](neutron_rbac_policy_module.md#ansible-collections-openstack-cloud-neutron-rbac-policy-module) – Create or delete a Neutron policy to apply a RBAC rule against an object.
- [object module](object_module.md#ansible-collections-openstack-cloud-object-module) – Create or Delete objects and containers from OpenStack
- [object_container module](object_container_module.md#ansible-collections-openstack-cloud-object-container-module) – Manage Swift container.
- [port module](port_module.md#ansible-collections-openstack-cloud-port-module) – Add/Update/Delete ports from an OpenStack cloud.
- [port_info module](port_info_module.md#ansible-collections-openstack-cloud-port-info-module) – Retrieve information about ports within OpenStack.
- [project module](project_module.md#ansible-collections-openstack-cloud-project-module) – Manage OpenStack Projects
- [project_access module](project_access_module.md#ansible-collections-openstack-cloud-project-access-module) – Manage OpenStack compute flavors access
- [project_info module](project_info_module.md#ansible-collections-openstack-cloud-project-info-module) – Retrieve information about one or more OpenStack projects
- [quota module](quota_module.md#ansible-collections-openstack-cloud-quota-module) – Manage OpenStack Quotas
- [recordset module](recordset_module.md#ansible-collections-openstack-cloud-recordset-module) – Manage OpenStack DNS recordsets
- [role_assignment module](role_assignment_module.md#ansible-collections-openstack-cloud-role-assignment-module) – Associate OpenStack Identity users and roles
- [router module](router_module.md#ansible-collections-openstack-cloud-router-module) – Create or delete routers from OpenStack
- [routers_info module](routers_info_module.md#ansible-collections-openstack-cloud-routers-info-module) – Retrieve information about one or more OpenStack routers.
- [security_group module](security_group_module.md#ansible-collections-openstack-cloud-security-group-module) – Add/Delete security groups from an OpenStack cloud.
- [security_group_info module](security_group_info_module.md#ansible-collections-openstack-cloud-security-group-info-module) – Lists security groups
- [security_group_rule module](security_group_rule_module.md#ansible-collections-openstack-cloud-security-group-rule-module) – Add/Delete rule from an existing security group
- [security_group_rule_info module](security_group_rule_info_module.md#ansible-collections-openstack-cloud-security-group-rule-info-module) – Querying security group rules
- [server module](server_module.md#ansible-collections-openstack-cloud-server-module) – Create/Delete Compute Instances from OpenStack
- [server_action module](server_action_module.md#ansible-collections-openstack-cloud-server-action-module) – Perform actions on Compute Instances from OpenStack
- [server_group module](server_group_module.md#ansible-collections-openstack-cloud-server-group-module) – Manage OpenStack server groups
- [server_info module](server_info_module.md#ansible-collections-openstack-cloud-server-info-module) – Retrieve information about one or more compute instances
- [server_metadata module](server_metadata_module.md#ansible-collections-openstack-cloud-server-metadata-module) – Add/Update/Delete Metadata in Compute Instances from OpenStack
- [server_volume module](server_volume_module.md#ansible-collections-openstack-cloud-server-volume-module) – Attach/Detach Volumes from OpenStack VM’s
- [stack module](stack_module.md#ansible-collections-openstack-cloud-stack-module) – Add/Remove Heat Stack
- [stack_info module](stack_info_module.md#ansible-collections-openstack-cloud-stack-info-module) – Retrive information about Heat stacks
- [subnet module](subnet_module.md#ansible-collections-openstack-cloud-subnet-module) – Add/Remove subnet to an OpenStack network
- [subnet_pool module](subnet_pool_module.md#ansible-collections-openstack-cloud-subnet-pool-module) – Create or delete subnet pools from OpenStack
- [subnets_info module](subnets_info_module.md#ansible-collections-openstack-cloud-subnets-info-module) – Retrieve information about one or more OpenStack subnets.
- [volume module](volume_module.md#ansible-collections-openstack-cloud-volume-module) – Create/Delete Cinder Volumes
- [volume_backup module](volume_backup_module.md#ansible-collections-openstack-cloud-volume-backup-module) – Add/Delete Volume backup
- [volume_backup_info module](volume_backup_info_module.md#ansible-collections-openstack-cloud-volume-backup-info-module) – Get Backups
- [volume_info module](volume_info_module.md#ansible-collections-openstack-cloud-volume-info-module) – Retrive information about volumes
- [volume_snapshot module](volume_snapshot_module.md#ansible-collections-openstack-cloud-volume-snapshot-module) – Create/Delete Cinder Volume Snapshots
- [volume_snapshot_info module](volume_snapshot_info_module.md#ansible-collections-openstack-cloud-volume-snapshot-info-module) – Get volume snapshots

### Inventory Plugins

- [openstack inventory](openstack_inventory.md#ansible-collections-openstack-cloud-openstack-inventory) – OpenStack inventory source

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

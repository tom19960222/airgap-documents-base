---
collection: ansible
version: "8"
title: "Openstack.Cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/index.html
fetched_at: 2026-07-28T01:02:54+00:00
---
# Openstack.Cloud

Collection version 2.2.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Openstack Ansible modules

**Author:**

- Openstack

**Supported ansible-core versions:**

- 2.8 or newer

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

## [Plugin Index](index.md#id2)

These are the plugins in the openstack.cloud collection:

### Modules

- [address_scope module](address_scope_module.md#ansible-collections-openstack-cloud-address-scope-module) – Create or delete address scopes from OpenStack
- [auth module](auth_module.md#ansible-collections-openstack-cloud-auth-module) – Retrieve auth token from OpenStack cloud
- [baremetal_deploy_template module](baremetal_deploy_template_module.md#ansible-collections-openstack-cloud-baremetal-deploy-template-module) – Create/Delete Bare Metal deploy template Resources from OpenStack
- [baremetal_inspect module](baremetal_inspect_module.md#ansible-collections-openstack-cloud-baremetal-inspect-module) – Explicitly triggers baremetal node introspection in ironic.
- [baremetal_node module](baremetal_node_module.md#ansible-collections-openstack-cloud-baremetal-node-module) – Create/Delete Bare Metal Resources from OpenStack
- [baremetal_node_action module](baremetal_node_action_module.md#ansible-collections-openstack-cloud-baremetal-node-action-module) – Activate/Deactivate Bare Metal nodes from OpenStack
- [baremetal_node_info module](baremetal_node_info_module.md#ansible-collections-openstack-cloud-baremetal-node-info-module) – Retrieve information about Bare Metal nodes from OpenStack
- [baremetal_port module](baremetal_port_module.md#ansible-collections-openstack-cloud-baremetal-port-module) – Create/Delete Bare Metal port Resources from OpenStack
- [baremetal_port_info module](baremetal_port_info_module.md#ansible-collections-openstack-cloud-baremetal-port-info-module) – Retrieve information about Bare Metal ports from OpenStack
- [catalog_service module](catalog_service_module.md#ansible-collections-openstack-cloud-catalog-service-module) – Manage OpenStack services
- [catalog_service_info module](catalog_service_info_module.md#ansible-collections-openstack-cloud-catalog-service-info-module) – Retrieve information about services from OpenStack
- [coe_cluster module](coe_cluster_module.md#ansible-collections-openstack-cloud-coe-cluster-module) – Manage COE cluster in OpenStack Cloud
- [coe_cluster_template module](coe_cluster_template_module.md#ansible-collections-openstack-cloud-coe-cluster-template-module) – Manage COE cluster template in OpenStack Cloud
- [compute_flavor module](compute_flavor_module.md#ansible-collections-openstack-cloud-compute-flavor-module) – Manage OpenStack compute flavors
- [compute_flavor_access module](compute_flavor_access_module.md#ansible-collections-openstack-cloud-compute-flavor-access-module) – Manage access to OpenStack compute flavors
- [compute_flavor_info module](compute_flavor_info_module.md#ansible-collections-openstack-cloud-compute-flavor-info-module) – Fetch compute flavors from OpenStack cloud
- [compute_service_info module](compute_service_info_module.md#ansible-collections-openstack-cloud-compute-service-info-module) – Fetch OpenStack Compute (Nova) services
- [config module](config_module.md#ansible-collections-openstack-cloud-config-module) – Get OpenStack Client config
- [dns_zone module](dns_zone_module.md#ansible-collections-openstack-cloud-dns-zone-module) – Manage a OpenStack DNS zone.
- [dns_zone_info module](dns_zone_info_module.md#ansible-collections-openstack-cloud-dns-zone-info-module) – Getting information about dns zones
- [endpoint module](endpoint_module.md#ansible-collections-openstack-cloud-endpoint-module) – Manage OpenStack Identity service endpoints
- [federation_idp module](federation_idp_module.md#ansible-collections-openstack-cloud-federation-idp-module) – Manage an identity provider in a OpenStack cloud
- [federation_idp_info module](federation_idp_info_module.md#ansible-collections-openstack-cloud-federation-idp-info-module) – Fetch OpenStack federation identity providers
- [federation_mapping module](federation_mapping_module.md#ansible-collections-openstack-cloud-federation-mapping-module) – Manage a federation mapping
- [federation_mapping_info module](federation_mapping_info_module.md#ansible-collections-openstack-cloud-federation-mapping-info-module) – Fetch Keystone federation mappings
- [floating_ip module](floating_ip_module.md#ansible-collections-openstack-cloud-floating-ip-module) – Manage floating IP addresses for OpenStack servers
- [floating_ip_info module](floating_ip_info_module.md#ansible-collections-openstack-cloud-floating-ip-info-module) – Get information about floating ips
- [group_assignment module](group_assignment_module.md#ansible-collections-openstack-cloud-group-assignment-module) – Assign OpenStack identity users to groups
- [host_aggregate module](host_aggregate_module.md#ansible-collections-openstack-cloud-host-aggregate-module) – Manage OpenStack host aggregates
- [identity_domain module](identity_domain_module.md#ansible-collections-openstack-cloud-identity-domain-module) – Manage OpenStack identity (Keystone) domains
- [identity_domain_info module](identity_domain_info_module.md#ansible-collections-openstack-cloud-identity-domain-info-module) – Fetch identity (Keystone) domains from OpenStack cloud
- [identity_group module](identity_group_module.md#ansible-collections-openstack-cloud-identity-group-module) – Manage a OpenStack identity (Keystone) group
- [identity_group_info module](identity_group_info_module.md#ansible-collections-openstack-cloud-identity-group-info-module) – Fetch OpenStack identity (Keystone) groups
- [identity_role module](identity_role_module.md#ansible-collections-openstack-cloud-identity-role-module) – Manage a OpenStack identity (Keystone) role
- [identity_role_info module](identity_role_info_module.md#ansible-collections-openstack-cloud-identity-role-info-module) – Fetch OpenStack identity (Keystone) roles
- [identity_user module](identity_user_module.md#ansible-collections-openstack-cloud-identity-user-module) – Manage a OpenStack identity (Keystone) user
- [identity_user_info module](identity_user_info_module.md#ansible-collections-openstack-cloud-identity-user-info-module) – Fetch OpenStack identity (Keystone) users
- [image module](image_module.md#ansible-collections-openstack-cloud-image-module) – Manage images of OpenStack image (Glance) service.
- [image_info module](image_info_module.md#ansible-collections-openstack-cloud-image-info-module) – Fetch images from OpenStack image (Glance) service.
- [keypair module](keypair_module.md#ansible-collections-openstack-cloud-keypair-module) – Add/Delete a keypair from OpenStack
- [keypair_info module](keypair_info_module.md#ansible-collections-openstack-cloud-keypair-info-module) – Get information about keypairs from OpenStack
- [keystone_federation_protocol module](keystone_federation_protocol_module.md#ansible-collections-openstack-cloud-keystone-federation-protocol-module) – Manage a Keystone federation protocol
- [keystone_federation_protocol_info module](keystone_federation_protocol_info_module.md#ansible-collections-openstack-cloud-keystone-federation-protocol-info-module) – Fetch Keystone federation protocols
- [lb_health_monitor module](lb_health_monitor_module.md#ansible-collections-openstack-cloud-lb-health-monitor-module) – Manage health monitor in a OpenStack load-balancer pool
- [lb_listener module](lb_listener_module.md#ansible-collections-openstack-cloud-lb-listener-module) – Manage load-balancer listener in a OpenStack cloud
- [lb_member module](lb_member_module.md#ansible-collections-openstack-cloud-lb-member-module) – Manage members in a OpenStack load-balancer pool
- [lb_pool module](lb_pool_module.md#ansible-collections-openstack-cloud-lb-pool-module) – Manage load-balancer pool in a OpenStack cloud.
- [loadbalancer module](loadbalancer_module.md#ansible-collections-openstack-cloud-loadbalancer-module) – Manage Octavia load-balancer in an OpenStack cloud
- [network module](network_module.md#ansible-collections-openstack-cloud-network-module) – Creates/removes networks from OpenStack
- [networks_info module](networks_info_module.md#ansible-collections-openstack-cloud-networks-info-module) – Retrieve information about one or more OpenStack networks.
- [neutron_rbac_policies_info module](neutron_rbac_policies_info_module.md#ansible-collections-openstack-cloud-neutron-rbac-policies-info-module) – Fetch Neutron RBAC policies.
- [neutron_rbac_policy module](neutron_rbac_policy_module.md#ansible-collections-openstack-cloud-neutron-rbac-policy-module) – Create or delete a Neutron RBAC policy.
- [object module](object_module.md#ansible-collections-openstack-cloud-object-module) – Create or delete Swift objects in OpenStack clouds
- [object_container module](object_container_module.md#ansible-collections-openstack-cloud-object-container-module) – Manage a Swift container.
- [port module](port_module.md#ansible-collections-openstack-cloud-port-module) – Add/Update/Delete ports from an OpenStack cloud.
- [port_info module](port_info_module.md#ansible-collections-openstack-cloud-port-info-module) – Retrieve information about ports within OpenStack.
- [project module](project_module.md#ansible-collections-openstack-cloud-project-module) – Manage OpenStack Identity (Keystone) projects
- [project_info module](project_info_module.md#ansible-collections-openstack-cloud-project-info-module) – Retrieve information about one or more OpenStack projects
- [quota module](quota_module.md#ansible-collections-openstack-cloud-quota-module) – Manage OpenStack Quotas
- [recordset module](recordset_module.md#ansible-collections-openstack-cloud-recordset-module) – Manage OpenStack DNS recordsets
- [resource module](resource_module.md#ansible-collections-openstack-cloud-resource-module) – Manage a OpenStack cloud resource
- [resources module](resources_module.md#ansible-collections-openstack-cloud-resources-module) – List OpenStack cloud resources
- [role_assignment module](role_assignment_module.md#ansible-collections-openstack-cloud-role-assignment-module) – Assign OpenStack identity groups and users to roles
- [router module](router_module.md#ansible-collections-openstack-cloud-router-module) – Create or delete routers from OpenStack
- [routers_info module](routers_info_module.md#ansible-collections-openstack-cloud-routers-info-module) – Retrieve information about one or more OpenStack routers.
- [security_group module](security_group_module.md#ansible-collections-openstack-cloud-security-group-module) – Manage Neutron security groups of an OpenStack cloud.
- [security_group_info module](security_group_info_module.md#ansible-collections-openstack-cloud-security-group-info-module) – Lists security groups
- [security_group_rule module](security_group_rule_module.md#ansible-collections-openstack-cloud-security-group-rule-module) – Manage security group rules in OpenStack network (Neutron)
- [security_group_rule_info module](security_group_rule_info_module.md#ansible-collections-openstack-cloud-security-group-rule-info-module) – Fetch OpenStack network (Neutron) security group rules
- [server module](server_module.md#ansible-collections-openstack-cloud-server-module) – Create/Delete Compute Instances from OpenStack
- [server_action module](server_action_module.md#ansible-collections-openstack-cloud-server-action-module) – Perform actions on OpenStack compute (Nova) instances
- [server_group module](server_group_module.md#ansible-collections-openstack-cloud-server-group-module) – Manage OpenStack server groups
- [server_info module](server_info_module.md#ansible-collections-openstack-cloud-server-info-module) – Retrieve information about one or more compute instances
- [server_metadata module](server_metadata_module.md#ansible-collections-openstack-cloud-server-metadata-module) – Add/Update/Delete Metadata in Compute Instances from OpenStack
- [server_volume module](server_volume_module.md#ansible-collections-openstack-cloud-server-volume-module) – Attach/Detach Volumes from OpenStack VM’s
- [stack module](stack_module.md#ansible-collections-openstack-cloud-stack-module) – Add/Remove Heat Stack
- [stack_info module](stack_info_module.md#ansible-collections-openstack-cloud-stack-info-module) – Retrieve information about Heat stacks
- [subnet module](subnet_module.md#ansible-collections-openstack-cloud-subnet-module) – Add/Remove subnet to an OpenStack network
- [subnet_pool module](subnet_pool_module.md#ansible-collections-openstack-cloud-subnet-pool-module) – Create, update or delete a subnet pool from OpenStack
- [subnets_info module](subnets_info_module.md#ansible-collections-openstack-cloud-subnets-info-module) – Retrieve information about one or more OpenStack subnets.
- [volume module](volume_module.md#ansible-collections-openstack-cloud-volume-module) – Create/Delete Cinder Volumes
- [volume_backup module](volume_backup_module.md#ansible-collections-openstack-cloud-volume-backup-module) – Add/Delete Volume backup
- [volume_backup_info module](volume_backup_info_module.md#ansible-collections-openstack-cloud-volume-backup-info-module) – Get Backups
- [volume_info module](volume_info_module.md#ansible-collections-openstack-cloud-volume-info-module) – Retrieve information about volumes
- [volume_snapshot module](volume_snapshot_module.md#ansible-collections-openstack-cloud-volume-snapshot-module) – Create/Delete Cinder Volume Snapshots
- [volume_snapshot_info module](volume_snapshot_info_module.md#ansible-collections-openstack-cloud-volume-snapshot-info-module) – Get volume snapshots
- [volume_type module](volume_type_module.md#ansible-collections-openstack-cloud-volume-type-module) – Manage OpenStack volume type
- [volume_type_access module](volume_type_access_module.md#ansible-collections-openstack-cloud-volume-type-access-module) – Manage access to OpenStack block-storage volume type
- [volume_type_encryption module](volume_type_encryption_module.md#ansible-collections-openstack-cloud-volume-type-encryption-module) – Manage OpenStack volume type encryption
- [volume_type_info module](volume_type_info_module.md#ansible-collections-openstack-cloud-volume-type-info-module) – Get OpenStack volume type details

### Inventory Plugins

- [openstack inventory](openstack_inventory.md#ansible-collections-openstack-cloud-openstack-inventory) – OpenStack inventory source

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

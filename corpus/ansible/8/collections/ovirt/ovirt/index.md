---
collection: ansible
version: "8"
title: "Ovirt.Ovirt"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/index.html
fetched_at: 2026-07-28T01:02:55+00:00
---
# Ovirt.Ovirt

Collection version 3.2.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

The oVirt Ansible Collection.

**Author:**

- Martin Necas <[mnecas@redhat.com](mailto:mnecas%40redhat.com)>

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)

## [Plugin Index](index.md#id2)

These are the plugins in the ovirt.ovirt collection:

### Modules

- [ovirt_affinity_group module](ovirt_affinity_group_module.md#ansible-collections-ovirt-ovirt-ovirt-affinity-group-module) – Module to manage affinity groups in oVirt/RHV
- [ovirt_affinity_label module](ovirt_affinity_label_module.md#ansible-collections-ovirt-ovirt-ovirt-affinity-label-module) – Module to manage affinity labels in oVirt/RHV
- [ovirt_affinity_label_info module](ovirt_affinity_label_info_module.md#ansible-collections-ovirt-ovirt-ovirt-affinity-label-info-module) – Retrieve information about one or more oVirt/RHV affinity labels
- [ovirt_api_info module](ovirt_api_info_module.md#ansible-collections-ovirt-ovirt-ovirt-api-info-module) – Retrieve information about the oVirt/RHV API
- [ovirt_auth module](ovirt_auth_module.md#ansible-collections-ovirt-ovirt-ovirt-auth-module) – Module to manage authentication to oVirt/RHV
- [ovirt_cluster module](ovirt_cluster_module.md#ansible-collections-ovirt-ovirt-ovirt-cluster-module) – Module to manage clusters in oVirt/RHV
- [ovirt_cluster_info module](ovirt_cluster_info_module.md#ansible-collections-ovirt-ovirt-ovirt-cluster-info-module) – Retrieve information about one or more oVirt/RHV clusters
- [ovirt_datacenter module](ovirt_datacenter_module.md#ansible-collections-ovirt-ovirt-ovirt-datacenter-module) – Module to manage data centers in oVirt/RHV
- [ovirt_datacenter_info module](ovirt_datacenter_info_module.md#ansible-collections-ovirt-ovirt-ovirt-datacenter-info-module) – Retrieve information about one or more oVirt/RHV datacenters
- [ovirt_disk module](ovirt_disk_module.md#ansible-collections-ovirt-ovirt-ovirt-disk-module) – Module to manage Virtual Machine and floating disks in oVirt/RHV
- [ovirt_disk_info module](ovirt_disk_info_module.md#ansible-collections-ovirt-ovirt-ovirt-disk-info-module) – Retrieve information about one or more oVirt/RHV disks
- [ovirt_disk_profile module](ovirt_disk_profile_module.md#ansible-collections-ovirt-ovirt-ovirt-disk-profile-module) – Module to manage storage domain disk profiles in ovirt
- [ovirt_event module](ovirt_event_module.md#ansible-collections-ovirt-ovirt-ovirt-event-module) – Create or delete an event in oVirt/RHV
- [ovirt_event_info module](ovirt_event_info_module.md#ansible-collections-ovirt-ovirt-ovirt-event-info-module) – This module can be used to retrieve information about one or more oVirt/RHV events
- [ovirt_external_provider module](ovirt_external_provider_module.md#ansible-collections-ovirt-ovirt-ovirt-external-provider-module) – Module to manage external providers in oVirt/RHV
- [ovirt_external_provider_info module](ovirt_external_provider_info_module.md#ansible-collections-ovirt-ovirt-ovirt-external-provider-info-module) – Retrieve information about one or more oVirt/RHV external providers
- [ovirt_group module](ovirt_group_module.md#ansible-collections-ovirt-ovirt-ovirt-group-module) – Module to manage groups in oVirt/RHV
- [ovirt_group_info module](ovirt_group_info_module.md#ansible-collections-ovirt-ovirt-ovirt-group-info-module) – Retrieve information about one or more oVirt/RHV groups
- [ovirt_host module](ovirt_host_module.md#ansible-collections-ovirt-ovirt-ovirt-host-module) – Module to manage hosts in oVirt/RHV
- [ovirt_host_info module](ovirt_host_info_module.md#ansible-collections-ovirt-ovirt-ovirt-host-info-module) – Retrieve information about one or more oVirt/RHV hosts
- [ovirt_host_network module](ovirt_host_network_module.md#ansible-collections-ovirt-ovirt-ovirt-host-network-module) – Module to manage host networks in oVirt/RHV
- [ovirt_host_pm module](ovirt_host_pm_module.md#ansible-collections-ovirt-ovirt-ovirt-host-pm-module) – Module to manage power management of hosts in oVirt/RHV
- [ovirt_host_storage_info module](ovirt_host_storage_info_module.md#ansible-collections-ovirt-ovirt-ovirt-host-storage-info-module) – Retrieve information about one or more oVirt/RHV HostStorages (applicable only for block storage)
- [ovirt_instance_type module](ovirt_instance_type_module.md#ansible-collections-ovirt-ovirt-ovirt-instance-type-module) – Module to manage Instance Types in oVirt/RHV
- [ovirt_job module](ovirt_job_module.md#ansible-collections-ovirt-ovirt-ovirt-job-module) – Module to manage jobs in oVirt/RHV
- [ovirt_mac_pool module](ovirt_mac_pool_module.md#ansible-collections-ovirt-ovirt-ovirt-mac-pool-module) – Module to manage MAC pools in oVirt/RHV
- [ovirt_network module](ovirt_network_module.md#ansible-collections-ovirt-ovirt-ovirt-network-module) – Module to manage logical networks in oVirt/RHV
- [ovirt_network_info module](ovirt_network_info_module.md#ansible-collections-ovirt-ovirt-ovirt-network-info-module) – Retrieve information about one or more oVirt/RHV networks
- [ovirt_nic module](ovirt_nic_module.md#ansible-collections-ovirt-ovirt-ovirt-nic-module) – Module to manage network interfaces of Virtual Machines in oVirt/RHV
- [ovirt_nic_info module](ovirt_nic_info_module.md#ansible-collections-ovirt-ovirt-ovirt-nic-info-module) – Retrieve information about one or more oVirt/RHV virtual machine network interfaces
- [ovirt_permission module](ovirt_permission_module.md#ansible-collections-ovirt-ovirt-ovirt-permission-module) – Module to manage permissions of users/groups in oVirt/RHV
- [ovirt_permission_info module](ovirt_permission_info_module.md#ansible-collections-ovirt-ovirt-ovirt-permission-info-module) – Retrieve information about one or more oVirt/RHV permissions
- [ovirt_qos module](ovirt_qos_module.md#ansible-collections-ovirt-ovirt-ovirt-qos-module) – Module to manage QoS entries in ovirt
- [ovirt_quota module](ovirt_quota_module.md#ansible-collections-ovirt-ovirt-ovirt-quota-module) – Module to manage datacenter quotas in oVirt/RHV
- [ovirt_quota_info module](ovirt_quota_info_module.md#ansible-collections-ovirt-ovirt-ovirt-quota-info-module) – Retrieve information about one or more oVirt/RHV quotas
- [ovirt_role module](ovirt_role_module.md#ansible-collections-ovirt-ovirt-ovirt-role-module) – Module to manage roles in oVirt/RHV
- [ovirt_scheduling_policy_info module](ovirt_scheduling_policy_info_module.md#ansible-collections-ovirt-ovirt-ovirt-scheduling-policy-info-module) – Retrieve information about one or more oVirt scheduling policies
- [ovirt_snapshot module](ovirt_snapshot_module.md#ansible-collections-ovirt-ovirt-ovirt-snapshot-module) – Module to manage Virtual Machine Snapshots in oVirt/RHV
- [ovirt_snapshot_info module](ovirt_snapshot_info_module.md#ansible-collections-ovirt-ovirt-ovirt-snapshot-info-module) – Retrieve information about one or more oVirt/RHV virtual machine snapshots
- [ovirt_storage_connection module](ovirt_storage_connection_module.md#ansible-collections-ovirt-ovirt-ovirt-storage-connection-module) – Module to manage storage connections in oVirt
- [ovirt_storage_domain module](ovirt_storage_domain_module.md#ansible-collections-ovirt-ovirt-ovirt-storage-domain-module) – Module to manage storage domains in oVirt/RHV
- [ovirt_storage_domain_info module](ovirt_storage_domain_info_module.md#ansible-collections-ovirt-ovirt-ovirt-storage-domain-info-module) – Retrieve information about one or more oVirt/RHV storage domains
- [ovirt_storage_template_info module](ovirt_storage_template_info_module.md#ansible-collections-ovirt-ovirt-ovirt-storage-template-info-module) – Retrieve information about one or more oVirt/RHV templates relate to a storage domain.
- [ovirt_storage_vm_info module](ovirt_storage_vm_info_module.md#ansible-collections-ovirt-ovirt-ovirt-storage-vm-info-module) – Retrieve information about one or more oVirt/RHV virtual machines relate to a storage domain.
- [ovirt_system_option_info module](ovirt_system_option_info_module.md#ansible-collections-ovirt-ovirt-ovirt-system-option-info-module) – Retrieve information about one oVirt/RHV system options.
- [ovirt_tag module](ovirt_tag_module.md#ansible-collections-ovirt-ovirt-ovirt-tag-module) – Module to manage tags in oVirt/RHV
- [ovirt_tag_info module](ovirt_tag_info_module.md#ansible-collections-ovirt-ovirt-ovirt-tag-info-module) – Retrieve information about one or more oVirt/RHV tags
- [ovirt_template module](ovirt_template_module.md#ansible-collections-ovirt-ovirt-ovirt-template-module) – Module to manage virtual machine templates in oVirt/RHV
- [ovirt_template_info module](ovirt_template_info_module.md#ansible-collections-ovirt-ovirt-ovirt-template-info-module) – Retrieve information about one or more oVirt/RHV templates
- [ovirt_user module](ovirt_user_module.md#ansible-collections-ovirt-ovirt-ovirt-user-module) – Module to manage users in oVirt/RHV
- [ovirt_user_info module](ovirt_user_info_module.md#ansible-collections-ovirt-ovirt-ovirt-user-info-module) – Retrieve information about one or more oVirt/RHV users
- [ovirt_vm module](ovirt_vm_module.md#ansible-collections-ovirt-ovirt-ovirt-vm-module) – Module to manage Virtual Machines in oVirt/RHV
- [ovirt_vm_info module](ovirt_vm_info_module.md#ansible-collections-ovirt-ovirt-ovirt-vm-info-module) – Retrieve information about one or more oVirt/RHV virtual machines
- [ovirt_vm_os_info module](ovirt_vm_os_info_module.md#ansible-collections-ovirt-ovirt-ovirt-vm-os-info-module) – Retrieve information on all supported oVirt/RHV operating systems
- [ovirt_vmpool module](ovirt_vmpool_module.md#ansible-collections-ovirt-ovirt-ovirt-vmpool-module) – Module to manage VM pools in oVirt/RHV
- [ovirt_vmpool_info module](ovirt_vmpool_info_module.md#ansible-collections-ovirt-ovirt-ovirt-vmpool-info-module) – Retrieve information about one or more oVirt/RHV vmpools
- [ovirt_vnic_profile module](ovirt_vnic_profile_module.md#ansible-collections-ovirt-ovirt-ovirt-vnic-profile-module) – Module to manage vNIC profile of network in oVirt/RHV
- [ovirt_vnic_profile_info module](ovirt_vnic_profile_info_module.md#ansible-collections-ovirt-ovirt-ovirt-vnic-profile-info-module) – Retrieve information about one or more oVirt/RHV vnic profiles

### Callback Plugins

- [stdout callback](stdout_callback.md#ansible-collections-ovirt-ovirt-stdout-callback) – Output the log of ansible

### Filter Plugins

- [convert_to_bytes filter](convert_to_bytes_filter.md#ansible-collections-ovirt-ovirt-convert-to-bytes-filter) – Convert units to bytes
- [filtervalue filter](filtervalue_filter.md#ansible-collections-ovirt-ovirt-filtervalue-filter) – Filter to findall occurance of some value in dict
- [get_network_xml_to_dict filter](get_network_xml_to_dict_filter.md#ansible-collections-ovirt-ovirt-get-network-xml-to-dict-filter) – Get network bridge and uuid to dict
- [get_ovf_disk_size filter](get_ovf_disk_size_filter.md#ansible-collections-ovirt-ovirt-get-ovf-disk-size-filter) – Get OVF disk size
- [json_query filter](json_query_filter.md#ansible-collections-ovirt-ovirt-json-query-filter) – Copy of community.general.json_query
- [ovirtdiff filter](ovirtdiff_filter.md#ansible-collections-ovirt-ovirt-ovirtdiff-filter) – Show what will be changed in next run of the VM
- [ovirtvmip filter](ovirtvmip_filter.md#ansible-collections-ovirt-ovirt-ovirtvmip-filter) – Return first IP
- [ovirtvmips filter](ovirtvmips_filter.md#ansible-collections-ovirt-ovirt-ovirtvmips-filter) – VM all IPs
- [ovirtvmipsv4 filter](ovirtvmipsv4_filter.md#ansible-collections-ovirt-ovirt-ovirtvmipsv4-filter) – VM IPv4
- [ovirtvmipsv6 filter](ovirtvmipsv6_filter.md#ansible-collections-ovirt-ovirt-ovirtvmipsv6-filter) – VM IPv4
- [ovirtvmipv4 filter](ovirtvmipv4_filter.md#ansible-collections-ovirt-ovirt-ovirtvmipv4-filter) – VM IPv4
- [ovirtvmipv6 filter](ovirtvmipv6_filter.md#ansible-collections-ovirt-ovirt-ovirtvmipv6-filter) – VM IPv4
- [removesensitivevmdata filter](removesensitivevmdata_filter.md#ansible-collections-ovirt-ovirt-removesensitivevmdata-filter) – removesensitivevmdata internal filter

### Inventory Plugins

- [ovirt inventory](ovirt_inventory.md#ansible-collections-ovirt-ovirt-ovirt-inventory) – oVirt inventory source

### Test Plugins

- [proxied test](proxied_test.md#ansible-collections-ovirt-ovirt-proxied-test) –

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_info module – Collect information from HPE Nimble Storage array"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_info_module.html
fetched_at: 2026-07-28T02:34:21+00:00
---
# hpe.nimble.hpe_nimble_info module – Collect information from HPE Nimble Storage array

> **Note:**
>
> This module is part of the [hpe.nimble collection](https://galaxy.ansible.com/ui/repo/published/hpe/nimble/) (version 1.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hpe.nimble`.
> You need further requirements to be able to use this module,
> see [Requirements](hpe_nimble_info_module.md#ansible-collections-hpe-nimble-hpe-nimble-info-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_info`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_info_module.md#synopsis)
- [Requirements](hpe_nimble_info_module.md#requirements)
- [Parameters](hpe_nimble_info_module.md#parameters)
- [Notes](hpe_nimble_info_module.md#notes)
- [Examples](hpe_nimble_info_module.md#examples)
- [Return Values](hpe_nimble_info_module.md#return-values)

## [Synopsis](hpe_nimble_info_module.md#id1)

- Collect information from a HPE Nimble Storage array. By default, the module will collect basic information including array, groups config, protection templates, protection schedules, snapshots, snapshot collections, volume collections and volume counts. Additional information can be collected based on the configured set of arguments.

## [Requirements](hpe_nimble_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **gather_subset**  list / elements=any | When supplied, this argument will define the information to be collected. Possible values for this include “all” “minimum” “config” “access_control_records”, “alarms”, “application_servers”, “application_categories”, “arrays”, “chap_users”, “controllers”, “disks”, “fibre_channel_interfaces”, “fibre_channel_configs”, “fibre_channel_initiator_aliases”, “fibre_channel_ports”, “folders”, “groups”, “initiator_groups”, “initiators”, “master_key”, “network_configs”, “performance_policies”, “pools”, “protection_schedules”, “protection_templates”, “protocol_endpoints”, “replication_partners”, “shelves”, “snapshots”, “snapshot_collections”, “software_versions”, “user_groups”, “user_policies”, “users”, “volumes”, “volume_collections”.  Each subset except “all”, “minimum” and “config” supports four types of subset options. Subset “all” supports limit and detail as subset options. Subset “config” and “minimum” does not support any subset options.  See the example section for usage of the following subset options.  fields - A string representing which attributes to display for a given subset.  limit - An integer value which represents how many latest items to show for a given subset.  detail - A bool flag when set to true fetches everything for a given subset. Default is “True”.  query - A key-value pair to query.  **Default:** `["minimum"]` |
| **host**  string / required | HPE Nimble Storage IP address. |
| **password**  string / required | HPE Nimble Storage password. |
| **username**  string / required | HPE Nimble Storage user name. |

## [Notes](hpe_nimble_info_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](hpe_nimble_info_module.md#id5)

```yaml+jinja
- name: Collect default set of information
  hpe.nimble.hpe_nimble_info:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    gather_subset:
      - minimum:
  register: array_info

- name: Show default information
  ansible.builtin.debug:
    msg: "{{ array_info['nimble_info']['default'] }}"

- name: Collect config
  hpe.nimble.hpe_nimble_info:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    gather_subset:
      - config:
  register: array_info

- name: Show config information
  ansible.builtin.debug:
    msg: "{{ array_info['nimble_info']['config'] }}"

- name: Collect all
  hpe.nimble.hpe_nimble_info:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    gather_subset:
      - all:
          limit: 1
  register: array_info

- name: Show all information
  ansible.builtin.debug:
    msg: "{{ array_info['nimble_info'] }}"

- name: Collect volume, snapshot and volume collection. Below query will show just one
        snapshot detail with attributes 'name and id' for a volume called 'vol1'
  hpe.nimble.hpe_nimble_info:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    gather_subset:
      - volumes:
          fields: "name,id"
          limit: 2
      - volume_collections:
          limit: 1
          detail: false
      - snapshots:
          fields: "name,id"
          query:
            vol_name: "vol1"
          limit: 1
          detail: True
  register: array_info

- name: Show information
  ansible.builtin.debug:
    msg: "{{ array_info['nimble_info'] }}"
```

## [Return Values](hpe_nimble_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **nimble_info**  complex | Returns the information collected from the HPE Nimble Storage array  **Returned:** always  **Sample:** `{"config": {"arrays": [{"all_flash": false, "extended_model": "vmware-4G-5T-160F", "full_name": "ansibler1-va", "role": "leader", "serial": "ansibler1-va"}], "groups": [{"alarms_enabled": true, "auto_switchover_enabled": true, "auto_switchover_messages": [], "autosupport_enabled": true, "default_iscsi_target_scope": "group", "dns_servers": [{"ip_addr": "10.235.0.185"}, {"ip_addr": "10.1.255.254"}], "domain_name": "vlab.nimblestorage.com", "encryption_config": {"cipher": "aes_256_xts", "encryption_active": true, "encryption_key_manager": "local", "master_key_set": true, "mode": "available", "scope": "group"}, "failover_mode": "Manual", "fc_enabled": false, "iscsi_enabled": true, "isns_enabled": true, "leader_array_name": "ansibler1-va", "member_list": ["ansibler1-va"], "name": "group-ansibler1-va", "ntp_server": "time.nimblestorage.com", "send_alert_to_support": true, "smtp_auth_enabled": false, "smtp_auth_username": "", "smtp_port": 25, "smtp_server": "", "snmp_community": "public", "snmp_trap_enabled": false, "snmp_trap_host": "", "snmp_trap_port": 162, "syslogd_enabled": false, "syslogd_server": "", "vvol_enabled": true}], "network_configs": [{"active_since": 1592210265, "array_list": [{"ctrlr_a_support_ip": "10.18.1.1", "ctrlr_b_support_ip": "10.18.2.2", "member_gid": 1, "name": "ansibler1-va", "nic_list": [{"data_ip": "172.16.41.139", "name": "eth3", "subnet_label": "data1", "tagged": false}, {"data_ip": "172.16.234.76", "name": "eth4", "subnet_label": "data2", "tagged": false}, {"data_ip": "", "name": "eth2", "subnet_label": "mgmt-data", "tagged": false}, {"data_ip": "", "name": "eth1", "subnet_label": "mgmt-data", "tagged": false}]}], "creation_time": 1586411318, "group_leader_array": "ansibler1-va", "id": "177321e77f009f2013000000000000000000000001", "iscsi_automatic_connection_method": true, "iscsi_connection_rebalancing": true, "last_active": 1592210256, "last_modified": 1586411356, "mgmt_ip": "10.18.171.96", "name": "active", "role": "active", "route_list": [{"gateway": "10.18.160.1", "tgt_netmask": "0.0.0.0", "tgt_network": "0.0.0.0"}], "secondary_mgmt_ip": "", "subnet_list": [{"allow_group": true, "allow_iscsi": true, "discovery_ip": "172.16.41.140", "failover": true, "failover_enable_time": 0, "label": "data1", "mtu": 1500, "netmask": "255.255.224.0", "network": "172.16.32.0", "netzone_type": "single", "type": "data", "vlan_id": 0}, {"allow_group": true, "allow_iscsi": true, "discovery_ip": "172.16.234.101", "failover": true, "failover_enable_time": 0, "label": "data2", "mtu": 1500, "netmask": "255.255.224.0", "network": "172.16.224.0", "netzone_type": "single", "type": "data", "vlan_id": 0}, {"allow_group": false, "allow_iscsi": false, "discovery_ip": "", "failover": true, "failover_enable_time": 0, "label": "mgmt-data", "mtu": 1500, "netmask": "255.255.224.0", "network": "10.18.160.0", "netzone_type": "none", "type": "mgmt", "vlan_id": 0}]}, {"active_since": 0, "array_list": [{"ctrlr_a_support_ip": "10.18.1.1", "ctrlr_b_support_ip": "10.18.2.2", "member_gid": 1, "name": "ansibler1-va", "nic_list": [{"data_ip": "", "name": "eth2", "subnet_label": "mgmt-data", "tagged": false}, {"data_ip": "", "name": "eth1", "subnet_label": "mgmt-data", "tagged": false}, {"data_ip": "172.16.41.139", "name": "eth3", "subnet_label": "data1", "tagged": false}, {"data_ip": "172.16.234.76", "name": "eth4", "subnet_label": "data2", "tagged": false}]}], "creation_time": 1586411356, "group_leader_array": "ansibler1-va", "id": "177321e77f009f2013000000000000000000000002", "iscsi_automatic_connection_method": true, "iscsi_connection_rebalancing": true, "last_active": 1592210265, "last_modified": 1586411318, "mgmt_ip": "10.18.171.96", "name": "backup", "role": "backup", "route_list": [{"gateway": "10.18.160.1", "tgt_netmask": "0.0.0.0", "tgt_network": "0.0.0.0"}], "secondary_mgmt_ip": "", "subnet_list": [{"allow_group": false, "allow_iscsi": false, "discovery_ip": "", "failover": true, "failover_enable_time": 0, "label": "mgmt-data", "mtu": 1500, "netmask": "255.255.224.0", "network": "10.18.160.0", "netzone_type": "none", "type": "mgmt", "vlan_id": 0}, {"allow_group": true, "allow_iscsi": true, "discovery_ip": "172.16.41.140", "failover": true, "failover_enable_time": 0, "label": "data1", "mtu": 1500, "netmask": "255.255.224.0", "network": "172.16.32.0", "netzone_type": "single", "type": "data", "vlan_id": 0}, {"allow_group": true, "allow_iscsi": true, "discovery_ip": "172.16.234.101", "failover": true, "failover_enable_time": 0, "label": "data2", "mtu": 1500, "netmask": "255.255.224.0", "network": "172.16.224.0", "netzone_type": "single", "type": "data", "vlan_id": 0}]}], "pools": [{"array_count": 1, "dedupe_all_volumes": false, "dedupe_capable": false, "is_default": true, "name": "default", "vol_list": [{"id": "0675a5e21cc205c609000000000000000000000001", "name": "vol1", "vol_id": "0675a5e21cc205c609000000000000000000000001", "vol_name": "vol1"}, {"id": "067321e77f009f2013000000000000000000000271", "name": "volumetc-vol1-0-24-07-2020-71470d6d-cd6e-11ea-9165-00505696c568", "vol_id": "067321e77f009f2013000000000000000000000271", "vol_name": "volumetc-vol1-0-24-07-2020-71470d6d-cd6e-11ea-9165-00505696c568"}, {"id": "067321e77f009f201300000000000000000000024d", "name": "ansible-vol1", "vol_id": "067321e77f009f201300000000000000000000024d", "vol_name": "ansible-vol1"}]}]}, "default": {"arrays": [{"all_flash": false, "extended_model": "vmware-4G-5T-160F", "full_name": "ansibler1-va"}], "disks": 16, "folders": 0, "groups": [{"auto_switchover_messages": [], "default_iscsi_target_scope": "group", "encryption_config": {"cipher": "aes_256_xts", "encryption_active": true, "encryption_key_manager": "local", "master_key_set": true, "mode": "available", "scope": "group"}, "fc_enabled": false, "iscsi_enabled": true, "leader_array_name": "ansibler1-va", "name": "group-ansibler1-va", "num_snaps": 49}], "initiator_groups": 1, "protection_schedules": 6, "protection_templates": 3, "protocol_endpoints": 0, "snapshot_collections": 49, "snapshots": 49, "software_versions": "5.2.2.0-730069-opt", "users": 2, "volume_collections": 1, "volumes": 3}, "snapshots": [{"access_control_records": null, "agent_type": "none", "app_uuid": "", "creation_time": 1586429663, "description": "Replicated by protection policy volcoll2 schedule Schedule-new", "expiry_after": 1, "expiry_time": 0, "id": "0475a5e21cc205c609000000000000000200000004", "is_manually_managed": true, "is_replica": true, "is_unmanaged": false, "last_modified": 1586429956, "metadata": null, "name": "adfsasfasfasf", "new_data_compressed_bytes": 0, "new_data_uncompressed_bytes": 0, "new_data_valid": true, "offline_reason": "user", "online": false, "origin_name": "", "pool_name": "default", "replication_status": null, "schedule_id": "0c7321e77f009f2013000000000000000000000008", "schedule_name": "Schedule-new", "serial_number": "022e0240e677ef2f6c9ce9006cc7be73", "size": 1073741824, "snap_collection_id": "0575a5e21cc205c609000000000000000000000004", "snap_collection_name": "adfsasfasfasf", "target_name": "iqn.2007-11.com.nimblestorage:group-ansibler1-va-g7321e77f009f2013", "vol_id": "0675a5e21cc205c609000000000000000000000001", "vol_name": "vol1", "vpd_ieee0": "022e0240e677ef2f", "vpd_ieee1": "6c9ce9006cc7be73", "vpd_t10": "Nimble  022e0240e677ef2f6c9ce9006cc7be73", "writable": false}], "volume_collections": [{"volcoll2": {"id": "077321e77f009f2013000000000000000000000005", "name": "volcoll2"}}], "volumes": [{"10.18.180.239-ansible-vol1": {"id": "067321e77f009f2013000000000000000000000230", "name": "10.18.180.239-ansible-vol1"}}, {"changed-volname": {"id": "067321e77f009f201300000000000000000000022f", "name": "changed-volname"}}]}` |

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)

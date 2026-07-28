---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_info module – NetApp information gatherer"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_info_module.html
fetched_at: 2026-07-28T02:42:21+00:00
---
# netapp.ontap.na_ontap_info module – NetApp information gatherer

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/ui/repo/published/netapp/ontap/) (version 22.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_info_module.md#ansible-collections-netapp-ontap-na-ontap-info-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_info`.

New in netapp.ontap 2.9.0

- [Synopsis](na_ontap_info_module.md#synopsis)
- [Requirements](na_ontap_info_module.md#requirements)
- [Parameters](na_ontap_info_module.md#parameters)
- [Notes](na_ontap_info_module.md#notes)
- [Examples](na_ontap_info_module.md#examples)
- [Return Values](na_ontap_info_module.md#return-values)

## [Synopsis](na_ontap_info_module.md#id1)

- This module allows you to gather various information about ONTAP configuration

## [Requirements](na_ontap_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later
- netapp_lib

## [Parameters](na_ontap_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **continue_on_error**  list / elements=string | By default, this module fails on the first error.  This option allows to provide a list of errors that are not failing the module.  Errors in the list are reported in the output, under the related info element, as an “error” entry.  Possible values are always, never, missing_vserver_api_error, rpc_error, other_error.  missing_vserver_api_error - most likely the API is available at cluster level but not vserver level.  rpc_error - some queries are failing because the node cannot reach another node in the cluster.  key_error - a query is failing because the returned data does not contain an expected key.  for key errors, make sure to report this in Discord. It may be a change in a new ONTAP version.  other_error - anything not in the above list.  always will continue on any error, never will fail on any error, they cannot be used with any other keyword.  **Default:** `["never"]` |
| **desired_attributes**  dictionary  *added in netapp.ontap 20.6.0* | Advanced feature requiring to understand ZAPI internals.  Allows to request a specific attribute that is not returned by default, or to limit the returned attributes.  A dictionary for the zapi desired-attributes element.  An XML tag *<tag>value</tag>* is a dictionary with tag as the key.  Value can be another dictionary, a list of dictionaries, a string, or nothing.  eg *<tag/>* is represented as *tag:*  Only a single subset can be called at a time if this option is set.  It is the caller responsibity to make sure key attributes are present in the right position.  The module will error out if any key attribute is missing. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the information collected to a given subset. Possible values for this argument include  active_directory_account_info  aggregate_info  aggr_efficiency_info  autosupport_check_info  cifs_options_info  cifs_server_info  cifs_share_info  cifs_vserver_security_info  cluster_identity_info  cluster_image_info  cluster_log_forwarding_info  cluster_node_info  cluster_peer_info  cluster_switch_info  clock_info  disk_info  env_sensors_info  event_notification_destination_info  event_notification_info  export_policy_info  export_rule_info  fcp_adapter_info  fcp_alias_info  fcp_service_info  igroup_info  iscsi_service_info  job_schedule_cron_info  kerberos_realm_info  ldap_client  ldap_config  license_info  lun_info  lun_map_info  metrocluster_check_info  metrocluster_info  metrocluster_node_info  net_dev_discovery_info  net_dns_info  net_failover_group_info  net_firewall_info  net_ifgrp_info  net_interface_info  net_interface_service_policy_info  net_ipspaces_info  net_port_info  net_port_broadcast_domain_info  net_routes_info  net_vlan_info  nfs_info  ntfs_dacl_info  ntfs_sd_info  ntp_server_info  nvme_info  nvme_interface_info  nvme_namespace_info  nvme_subsystem_info  ontap_system_version  ontap_version  ontapi_version  qos_adaptive_policy_info  qos_policy_info  qtree_info  quota_policy_info  quota_report_info  role_info  security_key_manager_key_info  security_login_account_info  security_login_role_config_info  security_login_role_info  service_processor_info  service_processor_network_info  shelf_info  sis_info  sis_policy_info  snapmirror_info  snapmirror_destination_info  snapmirror_policy_info  snapshot_info  snapshot_policy_info  storage_failover_info  storage_bridge_info  subsys_health_info  sysconfig_info  sys_cluster_alerts  volume_info  volume_space_info  vscan_info  vscan_status_info  vscan_scanner_pool_info  vscan_connection_status_all_info  vscan_connection_extended_stats_info  vserver_info  vserver_login_banner_info  vserver_motd_info  vserver_nfs_info  vserver_peer_info  Can specify a list of values to include a larger subset.  Values can also be used with an initial `!` to specify that a specific subset should not be collected.  nvme is supported with ONTAP 9.4 onwards.  use “help” to get a list of supported information for your system.  with lun_info, serial_hex and naa_id are computed when serial_number is present.  **Default:** `["all"]` |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **max_records**  integer  *added in netapp.ontap 20.2.0* | Maximum number of records returned in a single ZAPI call. Valid range is [1..2^32-1]. This parameter controls internal behavior of this module.  **Default:** `1024` |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **query**  dictionary  *added in netapp.ontap 20.7.0* | Advanced feature requiring to understand ZAPI internals.  Allows to specify which objects to return.  A dictionary for the zapi query element.  An XML tag *<tag>value</tag>* is a dictionary with tag as the key.  Value can be another dictionary, a list of dictionaries, a string, or nothing.  eg *<tag/>* is represented as *tag:*  Only a single subset can be called at a time if this option is set. |
| **state**  string | deprecated as of 21.1.0.  this option was ignored and continues to be ignored. |
| **summary**  boolean  *added in netapp.ontap 20.4.0* | Boolean flag to control return all attributes of the module info or only the names.  If true, only names are returned.  **Choices:**   - `false` ← (default) - `true` |
| **use_native_zapi_tags**  boolean  *added in netapp.ontap 20.6.0* | By default, *-* in the returned dictionary keys are translated to *_*.  If set to true, the translation is disabled.  **Choices:**   - `false` ← (default) - `true` |
| **use_rest**  string | This module only support ZAPI and will can not be swtich to REST  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will always use ZAPI.  **Default:** `"never"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **volume_move_target_aggr_info**  dictionary  *added in netapp.ontap 20.5.0* | Required options for volume_move_target_aggr_info |
| **volume_name**  string / required  *added in netapp.ontap 20.5.0* | Volume name to get target aggr info for |
| **vserver**  string / required  *added in netapp.ontap 20.5.0* | vserver the Volume lives on |
| **vserver**  string  *added in netapp.ontap 19.11.0* | If present, ‘vserver tunneling’ will limit the output to the vserver scope.  Note that not all subsets are supported on a vserver, and ‘all’ will trigger an error. |

## [Notes](na_ontap_info_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_info_module.md#id5)

```yaml+jinja
- name: Get NetApp info as Cluster Admin (Password Authentication)
  netapp.ontap.na_ontap_info:
    hostname: "na-vsim"
    username: "admin"
    password: "admins_password"
  register: ontap_info
- debug:
    msg: "{{ ontap_info.ontap_info }}"

- name: Get NetApp version as Vserver admin
  netapp.ontap.na_ontap_info:
    hostname: "na-vsim"
    username: "vsadmin"
    vserver: trident_svm
    password: "vsadmins_password"

- name: run ontap info module using vserver tunneling and ignoring errors
  netapp.ontap.na_ontap_info:
    hostname: "na-vsim"
    username: "admin"
    password: "admins_password"
    vserver: trident_svm
    summary: true
    continue_on_error:
      - missing_vserver_api_error
      - rpc_error

- name: Limit Info Gathering to Aggregate Information as Cluster Admin
  netapp.ontap.na_ontap_info:
    hostname: "na-vsim"
    username: "admin"
    password: "admins_password"
    gather_subset: "aggregate_info"
  register: ontap_info

- name: Limit Info Gathering to Volume and Lun Information as Cluster Admin
  netapp.ontap.na_ontap_info:
    hostname: "na-vsim"
    username: "admin"
    password: "admins_password"
    gather_subset:
      - volume_info
      - lun_info
  register: ontap_info

- name: Gather all info except for volume and lun information as Cluster Admin
  netapp.ontap.na_ontap_info:
    hostname: "na-vsim"
    username: "admin"
    password: "admins_password"
    gather_subset:
      - "!volume_info"
      - "!lun_info"
  register: ontap_info

- name: Gather Volume move information for a specific volume
  netapp.ontap.na_ontap_info:
    hostname: "na-vsim"
    username: "admin"
    password: "admins_password"
    gather_subset: volume_move_target_aggr_info
    volume_move_target_aggr_info:
      volume_name: carchitest
      vserver: ansible

- name: run ontap info module for aggregate module, requesting specific fields
  netapp.ontap.na_ontap_info:
    # <<: *login
    gather_subset: aggregate_info
    desired_attributes:
      aggr-attributes:
      aggr-inode-attributes:
        files-private-used:
      aggr-raid-attributes:
        aggregate-type:
    use_native_zapi_tags: true
    register: ontap
- debug: var=ontap

- name: run ontap info to get offline volumes with dp in the name
  netapp.ontap.na_ontap_info:
    # <<: *cert_login
    gather_subset: volume_info
    query:
      volume-attributes:
        volume-id-attributes:
          name: '*dp*'
        volume-state-attributes:
          state: offline
    desired_attributes:
      volume-attributes:
        volume-id-attributes:
          name:
        volume-state-attributes:
          state:
  register: ontap
- debug: var=ontap
```

## [Return Values](na_ontap_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ontap_info**  dictionary | Returns various information about NetApp cluster configuration  **Returned:** always  **Sample:** `"{ \"ontap_info\": { \"active_directory_account_info\": {...}, \"aggregate_info\": {...}, \"autosupport_check_info\": {...}, \"cluster_identity_info\": {...}, \"cluster_image_info\": {...}, \"cluster_node_info\": {...}, \"igroup_info\": {...}, \"iscsi_service_info\": {...}, \"license_info\": {...}, \"lun_info\": {...}, \"metrocluster_check_info\": {...}, \"metrocluster_info\": {...}, \"metrocluster_node_info\": {...}, \"net_dns_info\": {...}, \"net_ifgrp_info\": {...}, \"net_interface_info\": {...}, \"net_interface_service_policy_info\": {...}, \"net_port_info\": {...}, \"ontap_system_version\": {...}, \"ontap_version\": {...}, \"ontapi_version\": {...}, \"qos_policy_info\": {...}, \"qos_adaptive_policy_info\": {...}, \"qtree_info\": {...}, \"quota_policy_info\": {..}, \"quota_report_info\": {...}, \"security_key_manager_key_info\": {...}, \"security_login_account_info\": {...}, \"snapmirror_info\": {...} \"snapmirror_destination_info\": {...} \"storage_bridge_info\": {...} \"storage_failover_info\": {...}, \"volume_info\": {...}, \"vserver_login_banner_info\": {...}, \"vserver_motd_info\": {...}, \"vserver_info\": {...}, \"vserver_nfs_info\": {...}, \"vscan_status_info\": {...}, \"vscan_scanner_pool_info\": {...}, \"vscan_connection_status_all_info\": {...}, \"vscan_connection_extended_stats_info\": {...} }"` |

### Authors

- Piotr Olczak (@dprts)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)

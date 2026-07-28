---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_rest_info module – NetApp ONTAP information gatherer using REST APIs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_rest_info_module.html
fetched_at: 2026-07-28T00:13:03+00:00
---
# netapp.ontap.na_ontap_rest_info module – NetApp ONTAP information gatherer using REST APIs

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/netapp/ontap) (version 21.24.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_rest_info_module.md#ansible-collections-netapp-ontap-na-ontap-rest-info-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_rest_info`.

New in netapp.ontap 20.5.0

- [Synopsis](na_ontap_rest_info_module.md#synopsis)
- [Requirements](na_ontap_rest_info_module.md#requirements)
- [Parameters](na_ontap_rest_info_module.md#parameters)
- [Notes](na_ontap_rest_info_module.md#notes)
- [Examples](na_ontap_rest_info_module.md#examples)

## [Synopsis](na_ontap_rest_info_module.md#id1)

- This module allows you to gather various information about ONTAP configuration using REST APIs

## [Requirements](na_ontap_rest_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_rest_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **fields**  list / elements=string  added in netapp.ontap 20.6.0 | Request specific fields from subset.  Recommended - ‘<list of fields>’ to return specified fields, only one subset will be allowed.  Discouraged - ‘\*’ to return all the fields, one or more subsets are allowed. This option can be used for discovery, but is discouraged in production.  Stongly discouraged - ‘\*\*’ to return all the fields, one or more subsets are allowed. This option can put an extra load on the system and should not be used in production.  Limited - ‘’ to return default fields, generally the properties that uniquely identify the record (keys). Other data is not returned by default and need to be explicitly called for using the field name or \*.  If the option is not present, return default fields for that API (see ‘’ above). |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the information collected to a given subset.  Either the REST API or the ZAPI info name can be given. Possible values for this argument include  application/applications or application_info  application/consistency-groups  application/templates or application_template_info  cloud/targets or cloud_targets_info  cluster  cluster/chassis or cluster_chassis_info  cluster/counter/tables  cluster/fireware/history  cluster/jobs or cluster_jobs_info  cluster/licensing/capacity-pools  cluster/licensing/license-managers  cluster/licensing/licenses or license_info  cluster/mediators  cluster/metrics or cluster_metrics_info  cluster/metrocluster or metrocluster_info  cluster/metrocluster/diagnostics or cluster_metrocluster_diagnostics or metrocluster_check_info  cluster/metrocluster/dr-groups  cluster/metrocluster/interconnects  cluster/metrocluster/nodes or metrocluster-node-get-iter  cluster/metrocluster/operations  cluster/metrocluster/svms  cluster/nodes or cluster_node_info or sysconfig_info  cluster/ntp/keys  cluster/ntp/servers or ntp_server_info  cluster/peers or cluster_peer_info  cluster/schedules or cluster_schedules or job_schedule_cron_info  cluster/sensors  cluster/software or ontap_system_version or cluster_image_info  cluster/software/download or cluster_software_download  cluster/software/history or cluster_software_history  cluster/software/packages or cluster_software_packages  cluster/web  name-services/cache/group-membership/settings  name-services/cache/host/settings  name-services/cache/netgroup/settings  name-services/cache/setting  name-services/cache/unix-group/settings  name-services/dns or svm_dns_config_info or net_dns_info  name-services/ldap or svm_ldap_config_info or ldap_client or ldap_config  name-services/ldap-schemas  name-services/local-hosts  name-services/name-mappings or svm_name_mapping_config_info  name-services/nis or svm_nis_config_info  name-services/unix-groups  name-services/unix-users  network/ethernet/broadcast-domains or broadcast_domains_info or net_port_broadcast_domain_info  network/ethernet/ports or network_ports_info or net_port_info  network/ethernet/switch/ports  network/ethernet/switches or cluster_switch_info  network/fc/fabrics  network/fc/interfaces  network/fc/logins or san_fc_logins_info  network/fc/ports  network/fc/wwpn-aliases or san_fc_wppn-aliases or fcp_alias_info  network/http-proxy  network/ip/bgp/peer-groups  network/ip/interfaces or ip_interfaces_info or net_interface_info  network/ip/routes or ip_routes_info or net_routes_info  network/ip/service-policies or ip_service_policies or net_interface_service_policy_info  network/ip/subnets  network/ipspaces or network_ipspaces_info or net_ipspaces_info  private/support/alerts or sys_cluster_alerts  private/cli/vserver/security/file-directory or file_directory_security  protocols/audit  protocols/cifs/connections  protocols/cifs/domains  protocols/cifs/home-directory/search-paths or cifs_home_directory_info  protocols/cifs/local-groups  protocols/cifs/local-users  protocols/cifs/netbios  protocols/cifs/services or cifs_services_info or cifs_options_info  protocols/cifs/session/files  protocols/cifs/sessions  protocols/cifs/shadow-copies  protocols/cifs/shadowcopy-sets  protocols/cifs/shares or cifs_share_info  protocols/cifs/users-and-groups/privileges  protocols/cifs/unix-symlink-mapping  protocols/fpolicy  protocols/locks  protocols/ndmp  protocols/ndmp/nodes  protocols/ndmp/sessions  protocols/ndmp/svms  protocols/nfs/connected-clients  protocols/nfs/connected-client-maps  protocols/nfs/export-policies or export_policy_info  protocols/nfs/export-policies/rules **Requires the owning_resource to be set**  protocols/nfs/kerberos/interfaces  protocols/nfs/kerberos/realms or kerberos_realm_info  protocols/nfs/services or vserver_nfs_info or nfs_info  protocols/nvme/interfaces or nvme_interface_info  protocols/nvme/services or nvme_info  protocols/nvme/subsystems or nvme_subsystem_info  protocols/nvme/subsystem-controllers  protocols/nvme/subsystem-maps  protocols/s3/buckets  protocols/s3/services  protocols/san/fcp/services or san_fcp_services or fcp_service_info  protocols/san/igroups or nitiator_groups_info or igroup_info  protocols/san/iscsi/credentials or san_iscsi_credentials  protocols/san/iscsi/services or san_iscsi_services or iscsi_service_info  protocols/san/iscsi/sessions  protocols/san/lun-maps or san_lun_maps or lun_map_info  protocols/san/portsets  protocols/san/vvol-bindings  protocols/vscan or vscan_status_info or vscan_info  protocols/vscan/on-access-policies **Requires the owning_resource to be set**  protocols/vscan/on-demand-policies **Requires the owning_resource to be set**  protocols/vscan/scanner-pools **Requires the owning_resource to be set**  protocols/vscan/server-status or vscan_connection_status_all_info  security  security/accounts or security_login_info or security_login_account_info  security/anti-ransomware/suspects  security/audit  security/audit/destinations or cluster_log_forwarding_info  security/audit/messages  security/authentication/cluster/ad-proxy  security/authentication/cluster/ldap  security/authentication/cluster/nis  security/authentication/cluster/saml-sp  security/authentication/publickeys  security/azure-key-vaults  security/certificates  security/gcp-kms  security/ipsec  security/ipsec/ca-certificates  security/ipsec/policies  security/ipsec/security-associations  security/key-manager-configs  security/key-managers  security/key-stores  security/login/messages  security/multi-admin-verify  security/multi-admin-verify/approval-groups  security/multi-admin-verify/requests  security/multi-admin-verify/rules  security/roles or security_login_rest_role_info  security/ssh  security/ssh/svms  snapmirror/policies or snapmirror_policy_info  snapmirror/relationships or snapmirror_info  storage/aggregates or aggregate_info  storage/bridges or storage_bridge_info  storage/cluster  storage/disks or disk_info  storage/file/clone/split-loads  storage/file/clone/split-status  storage/file/clone/tokens  storage/file/moves  storage/flexcache/flexcaches or storage_flexcaches_info  storage/flexcache/origins or storage_flexcaches_origin_info  storage/luns or storage_luns_info or lun_info (if serial_number is present, serial_hex and naa_id are computed)  storage/namespaces or storage_NVMe_namespaces or nvme_namespace_info  storage/pools  storage/ports or storage_ports_info  storage/qos/policies or storage_qos_policies or qos_policy_info or qos_adaptive_policy_info  storage/qos/workloads  storage/qtrees or storage_qtrees_config or qtree_info  storage/quota/reports or storage_quota_reports or quota_report_info  storage/quota/rules or storage_quota_policy_rules  storage/shelves or storage_shelves_config or shelf_info  storage/snaplock/audit-logs  storage/snaplock/compliance-clocks  storage/snaplock/event-retention/operations  storage/snaplock/event-retention/policies  storage/snaplock/file-fingerprints  storage/snaplock/litigations  storage/snapshot-policies or storage_snapshot_policies or snapshot_policy_info  storage/switches  storage/tape-devices  storage/volumes or volume_info  storage/volumes/snapshots **Requires the owning_resource to be set**  storage/volume-efficiency-policies or sis_policy_info  support/autosupport or autosupport_config_info  support/autosupport/check or autosupport_check_info  support/autosupport/messages or autosupport_messages_history  support/auto-update  support/auto-update/configurations  support/auto-update/updates  support/configuration-backup  support/configuration-backup/backups  support/coredump/coredumps  support/ems or support_ems_config  support/ems/destinations or event_notification_info or event_notification_destination_info  support/ems/events or support_ems_events  support/ems/filters or support_ems_filters  support/ems/messages  support/snmp  support/snmp/traphosts  support/snmp/users  svm/migrations  svm/peers or svm_peers_info or vserver_peer_info  svm/peer-permissions or svm_peer-permissions_info  svm/svms or vserver_info  **The following do not have direct Rest API equivalent**  aggr_efficiency_info  cifs_vserver_security_info  clock_info  cluster_identity_info  net_vlan_info  sis_info  snapmirror_destination_info  system_node_info  volume_space_info  Can specify a list of values to include a larger subset.  REST APIs are supported with ONTAP 9.6 onwards.  Default: `["demo"]` |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **ignore_api_errors**  list / elements=string  added in netapp.ontap 21.23.0 | List of substrings.  If a substring is contained in an error message when fetching a subset, the module does not fail and the error is reported in the subset. |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **max_records**  integer | Maximum number of records returned in a single call.  Default: `1024` |
| **ontapi**  integer | The ontap api version to use |
| **owning_resource**  dictionary  added in netapp.ontap 21.19.0 | Some resources cannot be accessed directly. You need to select them based on the owner or parent. For instance, volume for a snaphot.  The following subsets require an owning resource, and the following suboptions when uuid is not present.  <storage/volumes/snapshots> **volume_name** is the volume name, **svm_name** is the owning vserver name for the volume.  <protocols/nfs/export-policies/rules> **policy_name** is the name of the policy, **svm_name** is the owning vserver name for the policy, **rule_index** is the rule index.  <protocols/vscan/on-access-policies> **svm_name** is the owning vserver name for the vscan  <protocols/vscan/on-demand-policies> **svm_name** is the owning vserver name for the vscan  <protocols/vscan/scanner-pools> **svm_name** is the owning vserver name for the vscan |
| **parameters**  dictionary  added in netapp.ontap 20.7.0 | Allows for any rest option to be passed in |
| **password**  aliases: pass  string | Password for the specified user. |
| **state**  string | deprecated as of 21.1.0.  this option was ignored and continues to be ignored. |
| **use_python_keys**  boolean  added in netapp.ontap 21.9.0 | If true, */* in the returned dictionary keys are translated to *_*.  It makes it possible to use a . notation when processing the output.  For instance *ontap_info[“svm/svms”]* can be accessed as *ontap_info.svm_svms*.  Choices:   - `false` ← (default) - `true` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](na_ontap_rest_info_module.md#id4)

> **Note:**
>
> - *security_login_role_config_info* there is no REST equivalent.
> - *security_login_role_info* there is no REST equivalent.
> - *security_key_manager_key_info* there is no REST equivalent.
> - *vserver_motd_info* there is no REST equivalent.
> - *vserver_login_banner_info* there is no REST equivalent.
> - *vscan_connection_extended_stats_info* there is no REST equivalent.
> - *env_sensors_info* there is no REST equivalent.
> - *fcp_adapter_info* there is no REST equivalent.
> - *net_dev_discovery_info* there is no REST equivalent.
> - *net_failover_group_info* there is no REST equivalent.
> - *net_firewall_info* there is no REST equivalent.
> - *ntfs_dacl_info* there is no REST equivalent.
> - *ntfs_sd_info* there is no REST equivalent.
> - *role_info* there is not REST equivalent.
> - *subsys_health_info* there is not REST equivalent.
> - *volume_move_target_aggr_info* there is not REST equivalent.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_rest_info_module.md#id5)

```yaml+jinja
- name: run ONTAP gather facts for vserver info
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      validate_certs: false
      use_rest: Always
      gather_subset:
        - svm/svms

- name: run ONTAP gather facts for aggregate info and volume info
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      validate_certs: false
      use_rest: Always
      gather_subset:
        - storage/aggregates
        - storage/volumes

- name: run ONTAP gather facts for all subsets
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      validate_certs: false
      use_rest: Always
      gather_subset:
        - all

- name: run ONTAP gather facts for aggregate info and volume info with fields section
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      fields:
        - '*'
      validate_certs: false
      use_rest: Always
      gather_subset:
        - storage/aggregates
        - storage/volumes

- name: run ONTAP gather facts for aggregate info with specified fields
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      fields:
        - 'uuid'
        - 'name'
        - 'node'
      validate_certs: false
      use_rest: Always
      gather_subset:
        - storage/aggregates
      parameters:
        recommend:
          true

- name: Get Snapshot info (owning_resource example)
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      fields:
        - '*'
      validate_certs: false
      use_rest: Always
      gather_subset:
        - storage/volumes/snapshots
      owning_resource:
        volume_name: volume_name
        svm_name: svm_name

- name: run ONTAP gather facts for volume info with query on name and state
  netapp.ontap.na_ontap_rest_info:
      hostname: "1.2.3.4"
      username: "testuser"
      password: "test-password"
      https: true
      validate_certs: false
      gather_subset:
        - storage/volumes
      parameters:
        name: ansible*
        state: online

- name: run ONTAP gather fact to get DACLs
  netapp.ontap.na_ontap_rest_info:
    hostname: "1.2.3.4"
    username: "testuser"
    password: "test-password"
    https: true
    validate_certs: false
    gather_subset:
      - file_directory_security
    parameters:
      vserver: svm1
      path: /vol1/qtree1
    use_python_keys: true

# assuming module_defaults is used to set hostname, username, ...
- name: run demo subset using custom vsadmin role
  netapp.ontap.na_ontap_rest_info:
    gather_subset:
      - demo
    force_ontap_version: 9.8
    ignore_api_errors:
      - 'not authorized for that command'

# reports: {"cluster/nodes": {"error": {"code": "6", "message": "not authorized for that command"}}
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)

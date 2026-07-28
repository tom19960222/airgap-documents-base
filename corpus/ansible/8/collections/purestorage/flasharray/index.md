---
collection: ansible
version: "8"
title: "Purestorage.Flasharray"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/index.html
fetched_at: 2026-07-28T01:02:56+00:00
---
# Purestorage.Flasharray

Collection version 1.24.0

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Collection of modules to manage Pure Storage FlashArrays (including Cloud Block Store)

**Author:**

- Pure Storage Ansible Team <[pure-ansible-team@purestorage.com](mailto:pure-ansible-team%40purestorage.com)>

**Supported ansible-core versions:**

- 2.14.0 or newer

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)

## [Communication](index.md#id2)

- Mailing list: [Ansible Project List](https://groups.google.com/g/ansible-project).
  ([Subscribe](mailto:ansible-project+subscribe%40googlegroups.com?subject=subscribe))

## [Plugin Index](index.md#id3)

These are the plugins in the purestorage.flasharray collection:

### Modules

- [purefa_ad module](purefa_ad_module.md#ansible-collections-purestorage-flasharray-purefa-ad-module) – Manage FlashArray Active Directory Account
- [purefa_admin module](purefa_admin_module.md#ansible-collections-purestorage-flasharray-purefa-admin-module) – Configure Pure Storage FlashArray Global Admin settings
- [purefa_alert module](purefa_alert_module.md#ansible-collections-purestorage-flasharray-purefa-alert-module) – Configure Pure Storage FlashArray alert email settings
- [purefa_apiclient module](purefa_apiclient_module.md#ansible-collections-purestorage-flasharray-purefa-apiclient-module) – Manage FlashArray API Clients
- [purefa_arrayname module](purefa_arrayname_module.md#ansible-collections-purestorage-flasharray-purefa-arrayname-module) – Configure Pure Storage FlashArray array name
- [purefa_banner module](purefa_banner_module.md#ansible-collections-purestorage-flasharray-purefa-banner-module) – Configure Pure Storage FlashArray GUI and SSH MOTD message
- [purefa_certs module](purefa_certs_module.md#ansible-collections-purestorage-flasharray-purefa-certs-module) – Manage FlashArray SSL Certificates
- [purefa_connect module](purefa_connect_module.md#ansible-collections-purestorage-flasharray-purefa-connect-module) – Manage replication connections between two FlashArrays
- [purefa_console module](purefa_console_module.md#ansible-collections-purestorage-flasharray-purefa-console-module) – Enable or Disable Pure Storage FlashArray Console Lock
- [purefa_default_protection module](purefa_default_protection_module.md#ansible-collections-purestorage-flasharray-purefa-default-protection-module) – Manage SafeMode default protection for a Pure Storage FlashArray
- [purefa_directory module](purefa_directory_module.md#ansible-collections-purestorage-flasharray-purefa-directory-module) – Manage FlashArray File System Directories
- [purefa_dirsnap module](purefa_dirsnap_module.md#ansible-collections-purestorage-flasharray-purefa-dirsnap-module) – Manage FlashArray File System Directory Snapshots
- [purefa_dns module](purefa_dns_module.md#ansible-collections-purestorage-flasharray-purefa-dns-module) – Configure FlashArray DNS settings
- [purefa_ds module](purefa_ds_module.md#ansible-collections-purestorage-flasharray-purefa-ds-module) – Configure FlashArray Directory Service
- [purefa_dsrole module](purefa_dsrole_module.md#ansible-collections-purestorage-flasharray-purefa-dsrole-module) – Configure FlashArray Directory Service Roles
- [purefa_endpoint module](purefa_endpoint_module.md#ansible-collections-purestorage-flasharray-purefa-endpoint-module) – Manage VMware protocol-endpoints on Pure Storage FlashArrays
- [purefa_eradication module](purefa_eradication_module.md#ansible-collections-purestorage-flasharray-purefa-eradication-module) – Configure Pure Storage FlashArray Eradication Timer
- [purefa_eula module](purefa_eula_module.md#ansible-collections-purestorage-flasharray-purefa-eula-module) – Sign Pure Storage FlashArray EULA
- [purefa_export module](purefa_export_module.md#ansible-collections-purestorage-flasharray-purefa-export-module) – Manage FlashArray File System Exports
- [purefa_file module](purefa_file_module.md#ansible-collections-purestorage-flasharray-purefa-file-module) – Manage FlashArray File Copies
- [purefa_fs module](purefa_fs_module.md#ansible-collections-purestorage-flasharray-purefa-fs-module) – Manage FlashArray File Systems
- [purefa_hardware module](purefa_hardware_module.md#ansible-collections-purestorage-flasharray-purefa-hardware-module) – Manage FlashArray Hardware Identification
- [purefa_hg module](purefa_hg_module.md#ansible-collections-purestorage-flasharray-purefa-hg-module) – Manage hostgroups on Pure Storage FlashArrays
- [purefa_host module](purefa_host_module.md#ansible-collections-purestorage-flasharray-purefa-host-module) – Manage hosts on Pure Storage FlashArrays
- [purefa_info module](purefa_info_module.md#ansible-collections-purestorage-flasharray-purefa-info-module) – Collect information from Pure Storage FlashArray
- [purefa_inventory module](purefa_inventory_module.md#ansible-collections-purestorage-flasharray-purefa-inventory-module) – Collect information from Pure Storage FlashArray
- [purefa_kmip module](purefa_kmip_module.md#ansible-collections-purestorage-flasharray-purefa-kmip-module) – Manage FlashArray KMIP server objects
- [purefa_logging module](purefa_logging_module.md#ansible-collections-purestorage-flasharray-purefa-logging-module) – Manage Pure Storage FlashArray Audit and Session logs
- [purefa_maintenance module](purefa_maintenance_module.md#ansible-collections-purestorage-flasharray-purefa-maintenance-module) – Configure Pure Storage FlashArray Maintence Windows
- [purefa_messages module](purefa_messages_module.md#ansible-collections-purestorage-flasharray-purefa-messages-module) – List FlashArray Alert Messages
- [purefa_network module](purefa_network_module.md#ansible-collections-purestorage-flasharray-purefa-network-module) – Manage network interfaces in a Pure Storage FlashArray
- [purefa_ntp module](purefa_ntp_module.md#ansible-collections-purestorage-flasharray-purefa-ntp-module) – Configure Pure Storage FlashArray NTP settings
- [purefa_offload module](purefa_offload_module.md#ansible-collections-purestorage-flasharray-purefa-offload-module) – Create, modify and delete NFS, S3 or Azure offload targets
- [purefa_pg module](purefa_pg_module.md#ansible-collections-purestorage-flasharray-purefa-pg-module) – Manage protection groups on Pure Storage FlashArrays
- [purefa_pgsched module](purefa_pgsched_module.md#ansible-collections-purestorage-flasharray-purefa-pgsched-module) – Manage protection groups replication schedules on Pure Storage FlashArrays
- [purefa_pgsnap module](purefa_pgsnap_module.md#ansible-collections-purestorage-flasharray-purefa-pgsnap-module) – Manage protection group snapshots on Pure Storage FlashArrays
- [purefa_phonehome module](purefa_phonehome_module.md#ansible-collections-purestorage-flasharray-purefa-phonehome-module) – Enable or Disable Pure Storage FlashArray Phonehome
- [purefa_pod module](purefa_pod_module.md#ansible-collections-purestorage-flasharray-purefa-pod-module) – Manage AC pods in Pure Storage FlashArrays
- [purefa_pod_replica module](purefa_pod_replica_module.md#ansible-collections-purestorage-flasharray-purefa-pod-replica-module) – Manage ActiveDR pod replica links between Pure Storage FlashArrays
- [purefa_policy module](purefa_policy_module.md#ansible-collections-purestorage-flasharray-purefa-policy-module) – Manage FlashArray File System Policies
- [purefa_proxy module](purefa_proxy_module.md#ansible-collections-purestorage-flasharray-purefa-proxy-module) – Configure FlashArray phonehome HTTPs proxy settings
- [purefa_ra module](purefa_ra_module.md#ansible-collections-purestorage-flasharray-purefa-ra-module) – Enable or Disable Pure Storage FlashArray Remote Assist
- [purefa_saml module](purefa_saml_module.md#ansible-collections-purestorage-flasharray-purefa-saml-module) – Manage FlashArray SAML2 service and identity providers
- [purefa_smis module](purefa_smis_module.md#ansible-collections-purestorage-flasharray-purefa-smis-module) – Enable or disable FlashArray SMI-S features
- [purefa_smtp module](purefa_smtp_module.md#ansible-collections-purestorage-flasharray-purefa-smtp-module) – Configure FlashArray SMTP settings
- [purefa_snap module](purefa_snap_module.md#ansible-collections-purestorage-flasharray-purefa-snap-module) – Manage volume snapshots on Pure Storage FlashArrays
- [purefa_snmp module](purefa_snmp_module.md#ansible-collections-purestorage-flasharray-purefa-snmp-module) – Configure FlashArray SNMP Managers
- [purefa_snmp_agent module](purefa_snmp_agent_module.md#ansible-collections-purestorage-flasharray-purefa-snmp-agent-module) – Configure the FlashArray SNMP Agent
- [purefa_sso module](purefa_sso_module.md#ansible-collections-purestorage-flasharray-purefa-sso-module) – Configure Pure Storage FlashArray Single Sign-On
- [purefa_subnet module](purefa_subnet_module.md#ansible-collections-purestorage-flasharray-purefa-subnet-module) – Manage network subnets in a Pure Storage FlashArray
- [purefa_syslog module](purefa_syslog_module.md#ansible-collections-purestorage-flasharray-purefa-syslog-module) – Configure Pure Storage FlashArray syslog settings
- [purefa_syslog_settings module](purefa_syslog_settings_module.md#ansible-collections-purestorage-flasharray-purefa-syslog-settings-module) – Manage FlashArray syslog servers settings
- [purefa_timeout module](purefa_timeout_module.md#ansible-collections-purestorage-flasharray-purefa-timeout-module) – Configure Pure Storage FlashArray GUI idle timeout
- [purefa_token module](purefa_token_module.md#ansible-collections-purestorage-flasharray-purefa-token-module) – Create or delete an API token for an existing admin user
- [purefa_user module](purefa_user_module.md#ansible-collections-purestorage-flasharray-purefa-user-module) – Create, modify or delete FlashArray local user account
- [purefa_vg module](purefa_vg_module.md#ansible-collections-purestorage-flasharray-purefa-vg-module) – Manage volume groups on Pure Storage FlashArrays
- [purefa_vlan module](purefa_vlan_module.md#ansible-collections-purestorage-flasharray-purefa-vlan-module) – Manage network VLAN interfaces in a Pure Storage FlashArray
- [purefa_vnc module](purefa_vnc_module.md#ansible-collections-purestorage-flasharray-purefa-vnc-module) – Enable or Disable VNC port for installed apps
- [purefa_volume module](purefa_volume_module.md#ansible-collections-purestorage-flasharray-purefa-volume-module) – Manage volumes on Pure Storage FlashArrays
- [purefa_volume_tags module](purefa_volume_tags_module.md#ansible-collections-purestorage-flasharray-purefa-volume-tags-module) – Manage volume tags on Pure Storage FlashArrays

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

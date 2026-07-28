---
collection: ansible
version: "6"
title: "Purestorage.Flashblade"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/index.html
fetched_at: 2026-07-27T16:42:08+00:00
---
# Purestorage.Flashblade

Collection version 1.10.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Collection of modules to manage Pure Storage FlashBlades

**Author:**

- Pure Storage Ansible Team <[pure-ansible-team@purestorage.com](mailto:pure-ansible-team%40purestorage.com)>

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)

## [Plugin Index](index.md#id2)

These are the plugins in the purestorage.flashblade collection:

### Modules

- [purefb_ad module](purefb_ad_module.md#ansible-collections-purestorage-flashblade-purefb-ad-module) – Manage FlashBlade Active Directory Account
- [purefb_admin module](purefb_admin_module.md#ansible-collections-purestorage-flashblade-purefb-admin-module) – Configure Pure Storage FlashBlade Global Admin settings
- [purefb_alert module](purefb_alert_module.md#ansible-collections-purestorage-flashblade-purefb-alert-module) – Configure Pure Storage FlashBlade alert email settings
- [purefb_apiclient module](purefb_apiclient_module.md#ansible-collections-purestorage-flashblade-purefb-apiclient-module) – Manage FlashBlade API Clients
- [purefb_banner module](purefb_banner_module.md#ansible-collections-purestorage-flashblade-purefb-banner-module) – Configure Pure Storage FlashBlade GUI and SSH MOTD message
- [purefb_bladename module](purefb_bladename_module.md#ansible-collections-purestorage-flashblade-purefb-bladename-module) – Configure Pure Storage FlashBlade name
- [purefb_bucket module](purefb_bucket_module.md#ansible-collections-purestorage-flashblade-purefb-bucket-module) – Manage Object Store Buckets on a Pure Storage FlashBlade.
- [purefb_bucket_replica module](purefb_bucket_replica_module.md#ansible-collections-purestorage-flashblade-purefb-bucket-replica-module) – Manage bucket replica links between Pure Storage FlashBlades
- [purefb_certgrp module](purefb_certgrp_module.md#ansible-collections-purestorage-flashblade-purefb-certgrp-module) – Manage FlashBlade Certifcate Groups
- [purefb_certs module](purefb_certs_module.md#ansible-collections-purestorage-flashblade-purefb-certs-module) – Manage FlashBlade SSL Certificates
- [purefb_connect module](purefb_connect_module.md#ansible-collections-purestorage-flashblade-purefb-connect-module) – Manage replication connections between two FlashBlades
- [purefb_dns module](purefb_dns_module.md#ansible-collections-purestorage-flashblade-purefb-dns-module) – Configure Pure Storage FlashBlade DNS settings
- [purefb_ds module](purefb_ds_module.md#ansible-collections-purestorage-flashblade-purefb-ds-module) – Configure FlashBlade Directory Service
- [purefb_dsrole module](purefb_dsrole_module.md#ansible-collections-purestorage-flashblade-purefb-dsrole-module) – Configure FlashBlade Management Directory Service Roles
- [purefb_eula module](purefb_eula_module.md#ansible-collections-purestorage-flashblade-purefb-eula-module) – Sign Pure Storage FlashBlade EULA
- [purefb_fs module](purefb_fs_module.md#ansible-collections-purestorage-flashblade-purefb-fs-module) – Manage filesystemon Pure Storage FlashBlade`
- [purefb_fs_replica module](purefb_fs_replica_module.md#ansible-collections-purestorage-flashblade-purefb-fs-replica-module) – Manage filesystem replica links between Pure Storage FlashBlades
- [purefb_groupquota module](purefb_groupquota_module.md#ansible-collections-purestorage-flashblade-purefb-groupquota-module) – Manage filesystem group quotas
- [purefb_info module](purefb_info_module.md#ansible-collections-purestorage-flashblade-purefb-info-module) – Collect information from Pure Storage FlashBlade
- [purefb_inventory module](purefb_inventory_module.md#ansible-collections-purestorage-flashblade-purefb-inventory-module) – Collect information from Pure Storage FlashBlade
- [purefb_keytabs module](purefb_keytabs_module.md#ansible-collections-purestorage-flashblade-purefb-keytabs-module) – Manage FlashBlade Kerberos Keytabs
- [purefb_lag module](purefb_lag_module.md#ansible-collections-purestorage-flashblade-purefb-lag-module) – Manage FlashBlade Link Aggregation Groups
- [purefb_lifecycle module](purefb_lifecycle_module.md#ansible-collections-purestorage-flashblade-purefb-lifecycle-module) – Manage FlashBlade object lifecycles
- [purefb_messages module](purefb_messages_module.md#ansible-collections-purestorage-flashblade-purefb-messages-module) – List FlashBlade Alert Messages
- [purefb_network module](purefb_network_module.md#ansible-collections-purestorage-flashblade-purefb-network-module) – Manage network interfaces in a Pure Storage FlashBlade
- [purefb_ntp module](purefb_ntp_module.md#ansible-collections-purestorage-flashblade-purefb-ntp-module) – Configure Pure Storage FlashBlade NTP settings
- [purefb_phonehome module](purefb_phonehome_module.md#ansible-collections-purestorage-flashblade-purefb-phonehome-module) – Enable or Disable Pure Storage FlashBlade Phone Home
- [purefb_policy module](purefb_policy_module.md#ansible-collections-purestorage-flashblade-purefb-policy-module) – Manage FlashBlade policies
- [purefb_proxy module](purefb_proxy_module.md#ansible-collections-purestorage-flashblade-purefb-proxy-module) – Configure FlashBlade phonehome HTTPs proxy settings
- [purefb_ra module](purefb_ra_module.md#ansible-collections-purestorage-flashblade-purefb-ra-module) – Enable or Disable Pure Storage FlashBlade Remote Assist
- [purefb_remote_cred module](purefb_remote_cred_module.md#ansible-collections-purestorage-flashblade-purefb-remote-cred-module) – Create, modify and delete FlashBlade object store remote credentials
- [purefb_s3acc module](purefb_s3acc_module.md#ansible-collections-purestorage-flashblade-purefb-s3acc-module) – Create or delete FlashBlade Object Store accounts
- [purefb_s3user module](purefb_s3user_module.md#ansible-collections-purestorage-flashblade-purefb-s3user-module) – Create or delete FlashBlade Object Store account users
- [purefb_smtp module](purefb_smtp_module.md#ansible-collections-purestorage-flashblade-purefb-smtp-module) – Configure SMTP for Pure Storage FlashBlade
- [purefb_snap module](purefb_snap_module.md#ansible-collections-purestorage-flashblade-purefb-snap-module) – Manage filesystem snapshots on Pure Storage FlashBlades
- [purefb_snmp_agent module](purefb_snmp_agent_module.md#ansible-collections-purestorage-flashblade-purefb-snmp-agent-module) – Configure the FlashBlade SNMP Agent
- [purefb_snmp_mgr module](purefb_snmp_mgr_module.md#ansible-collections-purestorage-flashblade-purefb-snmp-mgr-module) – Configure FlashBlade SNMP Managers
- [purefb_subnet module](purefb_subnet_module.md#ansible-collections-purestorage-flashblade-purefb-subnet-module) – Manage network subnets in a Pure Storage FlashBlade
- [purefb_syslog module](purefb_syslog_module.md#ansible-collections-purestorage-flashblade-purefb-syslog-module) – Configure Pure Storage FlashBlade syslog settings
- [purefb_target module](purefb_target_module.md#ansible-collections-purestorage-flashblade-purefb-target-module) – Manage remote S3-capable targets for a FlashBlade
- [purefb_timeout module](purefb_timeout_module.md#ansible-collections-purestorage-flashblade-purefb-timeout-module) – Configure Pure Storage FlashBlade GUI idle timeout
- [purefb_tz module](purefb_tz_module.md#ansible-collections-purestorage-flashblade-purefb-tz-module) – Configure Pure Storage FlashBlade timezone
- [purefb_user module](purefb_user_module.md#ansible-collections-purestorage-flashblade-purefb-user-module) – Modify FlashBlade user accounts
- [purefb_userpolicy module](purefb_userpolicy_module.md#ansible-collections-purestorage-flashblade-purefb-userpolicy-module) – Manage FlashBlade Object Store User Access Policies
- [purefb_userquota module](purefb_userquota_module.md#ansible-collections-purestorage-flashblade-purefb-userquota-module) – Manage filesystem user quotas
- [purefb_virtualhost module](purefb_virtualhost_module.md#ansible-collections-purestorage-flashblade-purefb-virtualhost-module) – Manage FlashBlade Object Store Virtual Hosts

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

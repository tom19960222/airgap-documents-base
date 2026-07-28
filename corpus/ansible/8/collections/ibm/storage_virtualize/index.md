---
collection: ansible
version: "8"
title: "Ibm.Storage_Virtualize"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/index.html
fetched_at: 2026-07-28T01:02:39+00:00
---
# Ibm.Storage_Virtualize

Collection version 2.1.0

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Collections for IBM Storage Virtualize

**Authors:**

- Shilpi Jain (github.com/Shilpi-J)
- Sumit Gupta (github.com/sumitguptaibm)

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)

## [Communication](index.md#id2)

- Matrix room `#users:ansible.im`: [General usage and support questions](https://matrix.to/#/#users:ansible.im).
- IRC channel `#ansible` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible).
- Mailing list: [Ansible Project List](https://groups.google.com/g/ansible-project).
  ([Subscribe](mailto:ansible-project+subscribe%40googlegroups.com?subject=subscribe))

## [Plugin Index](index.md#id3)

These are the plugins in the ibm.storage_virtualize collection:

### Modules

- [ibm_sv_manage_awss3_cloudaccount module](ibm_sv_manage_awss3_cloudaccount_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-awss3-cloudaccount-module) – This module configures and manages Amazon Simple Storage Service (Amazon S3) cloud account on IBM Storage Virtualize family systems
- [ibm_sv_manage_cloud_backups module](ibm_sv_manage_cloud_backups_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-cloud-backups-module) – This module configures and manages cloud backups on IBM Storage Virtualize family systems
- [ibm_sv_manage_fc_partnership module](ibm_sv_manage_fc_partnership_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-fc-partnership-module) – This module configures and manages Fibre Channel (FC) partnership on IBM Storage Virtualize family systems
- [ibm_sv_manage_fcportsetmember module](ibm_sv_manage_fcportsetmember_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-fcportsetmember-module) – This module manages addition or removal of ports to or from the Fibre Channel(FC) portsets on IBM Storage Virtualize family systems.
- [ibm_sv_manage_ip_partnership module](ibm_sv_manage_ip_partnership_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-ip-partnership-module) – This module manages IP partnerships on IBM Storage Virtualize family systems
- [ibm_sv_manage_provisioning_policy module](ibm_sv_manage_provisioning_policy_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-provisioning-policy-module) – This module configures and manages provisioning policies on IBM Storage Virtualize family systems
- [ibm_sv_manage_replication_policy module](ibm_sv_manage_replication_policy_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-replication-policy-module) – This module configures and manages replication policies on IBM Storage Virtualize family systems
- [ibm_sv_manage_security module](ibm_sv_manage_security_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-security-module) – This module manages security options on IBM Storage Virtualize family storage systems
- [ibm_sv_manage_snapshot module](ibm_sv_manage_snapshot_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-snapshot-module) – This module manages snapshots (PiT image of a volume) on IBM Storage Virtualize family systems
- [ibm_sv_manage_snapshotpolicy module](ibm_sv_manage_snapshotpolicy_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-snapshotpolicy-module) – This module manages snapshot policy configuration on IBM Storage Virtualize family systems
- [ibm_sv_manage_ssl_certificate module](ibm_sv_manage_ssl_certificate_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-ssl-certificate-module) – This module exports existing system-signed certificate on to IBM Storage Virtualize family systems
- [ibm_sv_manage_storage_partition module](ibm_sv_manage_storage_partition_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-storage-partition-module) – This module manages storage partition on IBM Storage Virtualize family systems
- [ibm_sv_manage_syslog_server module](ibm_sv_manage_syslog_server_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-syslog-server-module) – This module manages syslog server on IBM Storage Virtualize family systems
- [ibm_sv_manage_truststore_for_replication module](ibm_sv_manage_truststore_for_replication_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-manage-truststore-for-replication-module) – This module manages certificate trust stores for replication on IBM Storage Virtualize family systems
- [ibm_sv_restore_cloud_backup module](ibm_sv_restore_cloud_backup_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-restore-cloud-backup-module) – This module restores the cloud backup on IBM Storage Virtualize family systems
- [ibm_sv_switch_replication_direction module](ibm_sv_switch_replication_direction_module.md#ansible-collections-ibm-storage-virtualize-ibm-sv-switch-replication-direction-module) – This module switches the replication direction on IBM Storage Virtualize family systems
- [ibm_svc_auth module](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) – This module generates an authentication token for a user on IBM Storage Virtualize family system
- [ibm_svc_complete_initial_setup module](ibm_svc_complete_initial_setup_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-complete-initial-setup-module) – This module completes the initial setup configuration for LMC systems
- [ibm_svc_host module](ibm_svc_host_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-host-module) – This module manages hosts on IBM Storage Virtualize family systems
- [ibm_svc_hostcluster module](ibm_svc_hostcluster_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-hostcluster-module) – This module manages host cluster on IBM Storage Virtualize family systems
- [ibm_svc_info module](ibm_svc_info_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-info-module) – This module gathers various information from the IBM Storage Virtualize family systems
- [ibm_svc_initial_setup module](ibm_svc_initial_setup_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-initial-setup-module) – This module allows users to manage the initial setup configuration on IBM Storage Virtualize family systems
- [ibm_svc_manage_callhome module](ibm_svc_manage_callhome_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-callhome-module) – This module manages Call Home feature configuration on IBM Storage Virtualize family systems
- [ibm_svc_manage_consistgrp_flashcopy module](ibm_svc_manage_consistgrp_flashcopy_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-consistgrp-flashcopy-module) – This module manages FlashCopy consistency groups on IBM Storage Virtualize family systems
- [ibm_svc_manage_cv module](ibm_svc_manage_cv_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-cv-module) – This module manages the change volume for a given volume on IBM Storage Virtualize family systems
- [ibm_svc_manage_flashcopy module](ibm_svc_manage_flashcopy_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-flashcopy-module) – This module manages FlashCopy mappings on IBM Storage Virtualize family systems
- [ibm_svc_manage_ip module](ibm_svc_manage_ip_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-ip-module) – This module manages IP provisioning on IBM Storage Virtualize family systems
- [ibm_svc_manage_migration module](ibm_svc_manage_migration_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-migration-module) – This module manages volume migration between clusters on IBM Storage Virtualize family systems
- [ibm_svc_manage_mirrored_volume module](ibm_svc_manage_mirrored_volume_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-mirrored-volume-module) – This module manages mirrored volumes on IBM Storage Virtualize family systems
- [ibm_svc_manage_ownershipgroup module](ibm_svc_manage_ownershipgroup_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-ownershipgroup-module) – This module manages ownership group on IBM Storage Virtualize family systems
- [ibm_svc_manage_portset module](ibm_svc_manage_portset_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-portset-module) – This module manages portset configuration on IBM Storage Virtualize family systems
- [ibm_svc_manage_replication module](ibm_svc_manage_replication_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-replication-module) – This module manages remote copies (or rcrelationship) on IBM Storage Virtualize family systems
- [ibm_svc_manage_replicationgroup module](ibm_svc_manage_replicationgroup_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-replicationgroup-module) – This module manages remote copy consistency group on IBM Storage Virtualize family systems
- [ibm_svc_manage_safeguarded_policy module](ibm_svc_manage_safeguarded_policy_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-safeguarded-policy-module) – This module manages safeguarded policy configuration on IBM Storage Virtualize family systems
- [ibm_svc_manage_sra module](ibm_svc_manage_sra_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-sra-module) – This module manages remote support assistance configuration on IBM Storage Virtualize family systems
- [ibm_svc_manage_user module](ibm_svc_manage_user_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-user-module) – This module manages user on IBM Storage Virtualize family systems
- [ibm_svc_manage_usergroup module](ibm_svc_manage_usergroup_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-usergroup-module) – This module manages user group on IBM Storage Virtualize family systems
- [ibm_svc_manage_volume module](ibm_svc_manage_volume_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-volume-module) – This module manages standard volumes on IBM Storage Virtualize family systems
- [ibm_svc_manage_volumegroup module](ibm_svc_manage_volumegroup_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-manage-volumegroup-module) – This module manages volume groups on IBM Storage Virtualize family systems
- [ibm_svc_mdisk module](ibm_svc_mdisk_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-mdisk-module) – This module manages MDisks on IBM Storage Virtualize family systems
- [ibm_svc_mdiskgrp module](ibm_svc_mdiskgrp_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-mdiskgrp-module) – This module manages pools on IBM Storage Virtualize family systems
- [ibm_svc_start_stop_flashcopy module](ibm_svc_start_stop_flashcopy_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-start-stop-flashcopy-module) – This module starts or stops FlashCopy mapping and consistency groups on IBM Storage Virtualize family systems
- [ibm_svc_start_stop_replication module](ibm_svc_start_stop_replication_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-start-stop-replication-module) – This module starts or stops remote copies on IBM Storage Virtualize family systems
- [ibm_svc_vol_map module](ibm_svc_vol_map_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-vol-map-module) – This module manages volume mapping on IBM Storage Virtualize family systems
- [ibm_svcinfo_command module](ibm_svcinfo_command_module.md#ansible-collections-ibm-storage-virtualize-ibm-svcinfo-command-module) – This module implements SSH Client which helps to run svcinfo CLI command on IBM Storage Virtualize family systems
- [ibm_svctask_command module](ibm_svctask_command_module.md#ansible-collections-ibm-storage-virtualize-ibm-svctask-command-module) – This module implements SSH Client which helps to run svctask CLI command(s) on IBM Storage Virtualize family systems

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

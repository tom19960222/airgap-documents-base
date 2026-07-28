---
collection: ansible
version: "8"
title: "Netapp_Eseries.Santricity"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/index.html
fetched_at: 2026-07-28T01:02:50+00:00
---
# Netapp_Eseries.Santricity

Collection version 1.4.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Latest content available for NetApp E-Series Ansible automation.

**Authors:**

- Joe McCormick (@iamjoemccormick)
- Nathan Swartz (@ndswartz)

**Supported ansible-core versions:**

- 2.13 or newer

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)

## [Plugin Index](index.md#id2)

These are the plugins in the netapp_eseries.santricity collection:

### Modules

- [na_santricity_alerts module](na_santricity_alerts_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-alerts-module) – NetApp E-Series manage email notification settings
- [na_santricity_alerts_syslog module](na_santricity_alerts_syslog_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-alerts-syslog-module) – NetApp E-Series manage syslog servers receiving storage system alerts.
- [na_santricity_asup module](na_santricity_asup_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-asup-module) – NetApp E-Series manage auto-support settings
- [na_santricity_auditlog module](na_santricity_auditlog_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-auditlog-module) – NetApp E-Series manage audit-log configuration
- [na_santricity_auth module](na_santricity_auth_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-auth-module) – NetApp E-Series set or update the password for a storage array device or SANtricity Web Services Proxy.
- [na_santricity_client_certificate module](na_santricity_client_certificate_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-client-certificate-module) – NetApp E-Series manage remote server certificates.
- [na_santricity_discover module](na_santricity_discover_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-discover-module) – NetApp E-Series discover E-Series storage systems
- [na_santricity_drive_firmware module](na_santricity_drive_firmware_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-drive-firmware-module) – NetApp E-Series manage drive firmware
- [na_santricity_facts module](na_santricity_facts_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-facts-module) – NetApp E-Series retrieve facts about NetApp E-Series storage arrays
- [na_santricity_firmware module](na_santricity_firmware_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-firmware-module) – NetApp E-Series manage firmware.
- [na_santricity_global module](na_santricity_global_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-global-module) – NetApp E-Series manage global settings configuration
- [na_santricity_host module](na_santricity_host_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-host-module) – NetApp E-Series manage eseries hosts
- [na_santricity_hostgroup module](na_santricity_hostgroup_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-hostgroup-module) – NetApp E-Series manage array host groups
- [na_santricity_ib_iser_interface module](na_santricity_ib_iser_interface_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-ib-iser-interface-module) – NetApp E-Series manage InfiniBand iSER interface configuration
- [na_santricity_iscsi_interface module](na_santricity_iscsi_interface_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-iscsi-interface-module) –
- [na_santricity_iscsi_target module](na_santricity_iscsi_target_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-iscsi-target-module) – NetApp E-Series manage iSCSI target configuration
- [na_santricity_ldap module](na_santricity_ldap_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-ldap-module) – NetApp E-Series manage LDAP integration to use for authentication
- [na_santricity_lun_mapping module](na_santricity_lun_mapping_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-lun-mapping-module) – NetApp E-Series manage lun mappings
- [na_santricity_mgmt_interface module](na_santricity_mgmt_interface_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-mgmt-interface-module) – NetApp E-Series manage management interface configuration
- [na_santricity_nvme_interface module](na_santricity_nvme_interface_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-nvme-interface-module) – NetApp E-Series manage NVMe interface configuration
- [na_santricity_proxy_drive_firmware_upload module](na_santricity_proxy_drive_firmware_upload_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-proxy-drive-firmware-upload-module) – NetApp E-Series manage proxy drive firmware files
- [na_santricity_proxy_firmware_upload module](na_santricity_proxy_firmware_upload_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-proxy-firmware-upload-module) – NetApp E-Series manage proxy firmware uploads.
- [na_santricity_proxy_systems module](na_santricity_proxy_systems_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-proxy-systems-module) – NetApp E-Series manage SANtricity web services proxy storage arrays
- [na_santricity_server_certificate module](na_santricity_server_certificate_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-server-certificate-module) – NetApp E-Series manage the storage system’s server SSL certificates.
- [na_santricity_snapshot module](na_santricity_snapshot_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-snapshot-module) – NetApp E-Series storage system’s snapshots.
- [na_santricity_storagepool module](na_santricity_storagepool_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-storagepool-module) – NetApp E-Series manage volume groups and disk pools
- [na_santricity_syslog module](na_santricity_syslog_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-syslog-module) – NetApp E-Series manage syslog settings
- [na_santricity_volume module](na_santricity_volume_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-volume-module) – NetApp E-Series manage storage volumes (standard and thin)
- [netapp_e_alerts module](netapp_e_alerts_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-alerts-module) – NetApp E-Series manage email notification settings
- [netapp_e_amg module](netapp_e_amg_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-amg-module) – NetApp E-Series create, remove, and update asynchronous mirror groups
- [netapp_e_amg_role module](netapp_e_amg_role_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-amg-role-module) – NetApp E-Series update the role of a storage array within an Asynchronous Mirror Group (AMG).
- [netapp_e_amg_sync module](netapp_e_amg_sync_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-amg-sync-module) – NetApp E-Series conduct synchronization actions on asynchronous mirror groups.
- [netapp_e_asup module](netapp_e_asup_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-asup-module) – NetApp E-Series manage auto-support settings
- [netapp_e_auditlog module](netapp_e_auditlog_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-auditlog-module) – NetApp E-Series manage audit-log configuration
- [netapp_e_auth module](netapp_e_auth_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-auth-module) – NetApp E-Series set or update the password for a storage array.
- [netapp_e_drive_firmware module](netapp_e_drive_firmware_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-drive-firmware-module) – NetApp E-Series manage drive firmware
- [netapp_e_facts module](netapp_e_facts_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-facts-module) – NetApp E-Series retrieve facts about NetApp E-Series storage arrays
- [netapp_e_firmware module](netapp_e_firmware_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-firmware-module) – NetApp E-Series manage firmware.
- [netapp_e_flashcache module](netapp_e_flashcache_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-flashcache-module) – NetApp E-Series manage SSD caches
- [netapp_e_global module](netapp_e_global_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-global-module) – NetApp E-Series manage global settings configuration
- [netapp_e_host module](netapp_e_host_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-host-module) – NetApp E-Series manage eseries hosts
- [netapp_e_hostgroup module](netapp_e_hostgroup_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-hostgroup-module) – NetApp E-Series manage array host groups
- [netapp_e_iscsi_interface module](netapp_e_iscsi_interface_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-iscsi-interface-module) – NetApp E-Series manage iSCSI interface configuration
- [netapp_e_iscsi_target module](netapp_e_iscsi_target_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-iscsi-target-module) – NetApp E-Series manage iSCSI target configuration
- [netapp_e_ldap module](netapp_e_ldap_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-ldap-module) – NetApp E-Series manage LDAP integration to use for authentication
- [netapp_e_lun_mapping module](netapp_e_lun_mapping_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-lun-mapping-module) – NetApp E-Series create, delete, or modify lun mappings
- [netapp_e_mgmt_interface module](netapp_e_mgmt_interface_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-mgmt-interface-module) – NetApp E-Series management interface configuration
- [netapp_e_snapshot_group module](netapp_e_snapshot_group_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-snapshot-group-module) – NetApp E-Series manage snapshot groups
- [netapp_e_snapshot_images module](netapp_e_snapshot_images_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-snapshot-images-module) – NetApp E-Series create and delete snapshot images
- [netapp_e_snapshot_volume module](netapp_e_snapshot_volume_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-snapshot-volume-module) – NetApp E-Series manage snapshot volumes.
- [netapp_e_storage_system module](netapp_e_storage_system_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-storage-system-module) – NetApp E-Series Web Services Proxy manage storage arrays
- [netapp_e_storagepool module](netapp_e_storagepool_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-storagepool-module) – NetApp E-Series manage volume groups and disk pools
- [netapp_e_syslog module](netapp_e_syslog_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-syslog-module) – NetApp E-Series manage syslog settings
- [netapp_e_volume module](netapp_e_volume_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-volume-module) – NetApp E-Series manage storage volumes (standard and thin)
- [netapp_e_volume_copy module](netapp_e_volume_copy_module.md#ansible-collections-netapp-eseries-santricity-netapp-e-volume-copy-module) – NetApp E-Series create volume copy pairs

### Lookup Plugins

- [santricity_host lookup](santricity_host_lookup.md#ansible-collections-netapp-eseries-santricity-santricity-host-lookup) –
- [santricity_host_detail lookup](santricity_host_detail_lookup.md#ansible-collections-netapp-eseries-santricity-santricity-host-detail-lookup) – Expands the host information from santricity_host lookup
- [santricity_lun_mapping lookup](santricity_lun_mapping_lookup.md#ansible-collections-netapp-eseries-santricity-santricity-lun-mapping-lookup) –
- [santricity_storage_pool lookup](santricity_storage_pool_lookup.md#ansible-collections-netapp-eseries-santricity-santricity-storage-pool-lookup) – Storage pool information
- [santricity_volume lookup](santricity_volume_lookup.md#ansible-collections-netapp-eseries-santricity-santricity-volume-lookup) –

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

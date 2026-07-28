---
collection: ansible
version: "8"
title: "Inspur.Ispim"
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/ispim/index.html
fetched_at: 2026-07-28T01:02:41+00:00
---
# Inspur.Ispim

Collection version 1.3.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Inspur server supports ansible management device.

**Author:**

- Baoshan Wang <[wangbaoshan@inspur.com](mailto:wangbaoshan%40inspur.com)>

**Supported ansible-core versions:**

- 2.10 or newer

- [Issue Tracker](https://github.com/ispim/inspur.ispim/issues)
- [Repository (Sources)](https://github.com/ispim/inspur.ispim)

## [Plugin Index](index.md#id2)

These are the plugins in the inspur.ispim collection:

### Modules

- [ad_group module](ad_group_module.md#ansible-collections-inspur-ispim-ad-group-module) – Manage active directory group information
- [ad_group_info module](ad_group_info_module.md#ansible-collections-inspur-ispim-ad-group-info-module) – Get active directory group information
- [ad_info module](ad_info_module.md#ansible-collections-inspur-ispim-ad-info-module) – Get active directory information
- [adapter_info module](adapter_info_module.md#ansible-collections-inspur-ispim-adapter-info-module) – Get adapter information
- [add_ldisk module](add_ldisk_module.md#ansible-collections-inspur-ispim-add-ldisk-module) – Create logical disk
- [alert_policy_info module](alert_policy_info_module.md#ansible-collections-inspur-ispim-alert-policy-info-module) – Get alert policy
- [audit_log_info module](audit_log_info_module.md#ansible-collections-inspur-ispim-audit-log-info-module) – Get BMC audit log information
- [auto_capture_info module](auto_capture_info_module.md#ansible-collections-inspur-ispim-auto-capture-info-module) – Get auto capture screen information
- [backplane_info module](backplane_info_module.md#ansible-collections-inspur-ispim-backplane-info-module) – Get disk backplane information
- [backup module](backup_module.md#ansible-collections-inspur-ispim-backup-module) – Backup server settings
- [bios_export module](bios_export_module.md#ansible-collections-inspur-ispim-bios-export-module) – Export BIOS config
- [bios_import module](bios_import_module.md#ansible-collections-inspur-ispim-bios-import-module) – Import BIOS config
- [bios_info module](bios_info_module.md#ansible-collections-inspur-ispim-bios-info-module) – Get BIOS setup
- [bmc_info module](bmc_info_module.md#ansible-collections-inspur-ispim-bmc-info-module) – Get BMC information
- [boot_image_info module](boot_image_info_module.md#ansible-collections-inspur-ispim-boot-image-info-module) – Get bmc boot image information
- [boot_option_info module](boot_option_info_module.md#ansible-collections-inspur-ispim-boot-option-info-module) – Get BIOS boot options
- [clear_audit_log module](clear_audit_log_module.md#ansible-collections-inspur-ispim-clear-audit-log-module) – Clear BMC audit log
- [clear_event_log module](clear_event_log_module.md#ansible-collections-inspur-ispim-clear-event-log-module) – Clear event log
- [clear_system_log module](clear_system_log_module.md#ansible-collections-inspur-ispim-clear-system-log-module) – Clear BMC system log
- [collect_blackbox module](collect_blackbox_module.md#ansible-collections-inspur-ispim-collect-blackbox-module) – Collect blackbox log
- [collect_log module](collect_log_module.md#ansible-collections-inspur-ispim-collect-log-module) – Collect logs
- [connect_media_info module](connect_media_info_module.md#ansible-collections-inspur-ispim-connect-media-info-module) – Get remote images redirection information
- [cpu_info module](cpu_info_module.md#ansible-collections-inspur-ispim-cpu-info-module) – Get CPU information
- [del_session module](del_session_module.md#ansible-collections-inspur-ispim-del-session-module) – Delete session
- [dns_info module](dns_info_module.md#ansible-collections-inspur-ispim-dns-info-module) – Get dns information
- [download_auto_screenshot module](download_auto_screenshot_module.md#ansible-collections-inspur-ispim-download-auto-screenshot-module) – Download auto screenshots
- [download_manual_screenshot module](download_manual_screenshot_module.md#ansible-collections-inspur-ispim-download-manual-screenshot-module) – Download manual screenshots
- [edit_ad module](edit_ad_module.md#ansible-collections-inspur-ispim-edit-ad-module) – Set active directory information
- [edit_alert_policy module](edit_alert_policy_module.md#ansible-collections-inspur-ispim-edit-alert-policy-module) – Set alert policy
- [edit_auto_capture module](edit_auto_capture_module.md#ansible-collections-inspur-ispim-edit-auto-capture-module) – Set auto capture screen
- [edit_bios module](edit_bios_module.md#ansible-collections-inspur-ispim-edit-bios-module) – Set BIOS setup attributes
- [edit_boot_image module](edit_boot_image_module.md#ansible-collections-inspur-ispim-edit-boot-image-module) – Set bmc boot image
- [edit_boot_option module](edit_boot_option_module.md#ansible-collections-inspur-ispim-edit-boot-option-module) – Set BIOS boot options
- [edit_connect_media module](edit_connect_media_module.md#ansible-collections-inspur-ispim-edit-connect-media-module) – Start/Stop virtual media Image
- [edit_dns module](edit_dns_module.md#ansible-collections-inspur-ispim-edit-dns-module) – Set dns information
- [edit_event_log_policy module](edit_event_log_policy_module.md#ansible-collections-inspur-ispim-edit-event-log-policy-module) – Set event log policy
- [edit_fan module](edit_fan_module.md#ansible-collections-inspur-ispim-edit-fan-module) – Set fan information
- [edit_fru module](edit_fru_module.md#ansible-collections-inspur-ispim-edit-fru-module) – Set fru settings
- [edit_ipv4 module](edit_ipv4_module.md#ansible-collections-inspur-ispim-edit-ipv4-module) – Set ipv4 information
- [edit_ipv6 module](edit_ipv6_module.md#ansible-collections-inspur-ispim-edit-ipv6-module) – Set ipv6 information
- [edit_kvm module](edit_kvm_module.md#ansible-collections-inspur-ispim-edit-kvm-module) – Set KVM
- [edit_ldap module](edit_ldap_module.md#ansible-collections-inspur-ispim-edit-ldap-module) – Set ldap information
- [edit_ldisk module](edit_ldisk_module.md#ansible-collections-inspur-ispim-edit-ldisk-module) – Set logical disk
- [edit_log_setting module](edit_log_setting_module.md#ansible-collections-inspur-ispim-edit-log-setting-module) – Set bmc system and audit log setting
- [edit_m6_log_setting module](edit_m6_log_setting_module.md#ansible-collections-inspur-ispim-edit-m6-log-setting-module) – Set bmc system and audit log setting
- [edit_manual_capture module](edit_manual_capture_module.md#ansible-collections-inspur-ispim-edit-manual-capture-module) – Set manual capture screen
- [edit_media_instance module](edit_media_instance_module.md#ansible-collections-inspur-ispim-edit-media-instance-module) – Set Virtual Media Instance
- [edit_ncsi module](edit_ncsi_module.md#ansible-collections-inspur-ispim-edit-ncsi-module) – Set ncsi information
- [edit_network module](edit_network_module.md#ansible-collections-inspur-ispim-edit-network-module) – Set network information
- [edit_network_bond module](edit_network_bond_module.md#ansible-collections-inspur-ispim-edit-network-bond-module) – Set network bond
- [edit_network_link module](edit_network_link_module.md#ansible-collections-inspur-ispim-edit-network-link-module) – Set network link
- [edit_ntp module](edit_ntp_module.md#ansible-collections-inspur-ispim-edit-ntp-module) – Set NTP
- [edit_pdisk module](edit_pdisk_module.md#ansible-collections-inspur-ispim-edit-pdisk-module) – Set physical disk
- [edit_power_budget module](edit_power_budget_module.md#ansible-collections-inspur-ispim-edit-power-budget-module) – Set power budget information
- [edit_power_restore module](edit_power_restore_module.md#ansible-collections-inspur-ispim-edit-power-restore-module) – Set power restore information
- [edit_power_status module](edit_power_status_module.md#ansible-collections-inspur-ispim-edit-power-status-module) – Set power status information
- [edit_preserve_config module](edit_preserve_config_module.md#ansible-collections-inspur-ispim-edit-preserve-config-module) – Set preserve config
- [edit_psu_config module](edit_psu_config_module.md#ansible-collections-inspur-ispim-edit-psu-config-module) – Set psu config information
- [edit_psu_peak module](edit_psu_peak_module.md#ansible-collections-inspur-ispim-edit-psu-peak-module) – Set psu peak information
- [edit_restore_factory_default module](edit_restore_factory_default_module.md#ansible-collections-inspur-ispim-edit-restore-factory-default-module) – Set preserver config
- [edit_service module](edit_service_module.md#ansible-collections-inspur-ispim-edit-service-module) – Set service settings
- [edit_smtp module](edit_smtp_module.md#ansible-collections-inspur-ispim-edit-smtp-module) – Set SMTP information
- [edit_smtp_com module](edit_smtp_com_module.md#ansible-collections-inspur-ispim-edit-smtp-com-module) – Set SMTP information
- [edit_smtp_dest module](edit_smtp_dest_module.md#ansible-collections-inspur-ispim-edit-smtp-dest-module) – Set SMTP information
- [edit_snmp module](edit_snmp_module.md#ansible-collections-inspur-ispim-edit-snmp-module) – Set snmp
- [edit_snmp_trap module](edit_snmp_trap_module.md#ansible-collections-inspur-ispim-edit-snmp-trap-module) – Set snmp trap
- [edit_threshold module](edit_threshold_module.md#ansible-collections-inspur-ispim-edit-threshold-module) – Set threshold information
- [edit_uid module](edit_uid_module.md#ansible-collections-inspur-ispim-edit-uid-module) – Set UID
- [edit_virtual_media module](edit_virtual_media_module.md#ansible-collections-inspur-ispim-edit-virtual-media-module) – Set virtual media
- [edit_vlan module](edit_vlan_module.md#ansible-collections-inspur-ispim-edit-vlan-module) – Set vlan information
- [event_log_info module](event_log_info_module.md#ansible-collections-inspur-ispim-event-log-info-module) – Get event log information
- [event_log_policy_info module](event_log_policy_info_module.md#ansible-collections-inspur-ispim-event-log-policy-info-module) – Get event log policy information
- [fan_info module](fan_info_module.md#ansible-collections-inspur-ispim-fan-info-module) – Get fan information
- [fru_info module](fru_info_module.md#ansible-collections-inspur-ispim-fru-info-module) – Get fru information
- [fw_version_info module](fw_version_info_module.md#ansible-collections-inspur-ispim-fw-version-info-module) – Get firmware version information
- [gpu_info module](gpu_info_module.md#ansible-collections-inspur-ispim-gpu-info-module) – Get GPU information
- [hard_disk_info module](hard_disk_info_module.md#ansible-collections-inspur-ispim-hard-disk-info-module) – Get hard disk information
- [kvm_info module](kvm_info_module.md#ansible-collections-inspur-ispim-kvm-info-module) – Get KVM information
- [ldap_group module](ldap_group_module.md#ansible-collections-inspur-ispim-ldap-group-module) – Manage ldap group information
- [ldap_group_info module](ldap_group_info_module.md#ansible-collections-inspur-ispim-ldap-group-info-module) – Get ldap group information
- [ldap_info module](ldap_info_module.md#ansible-collections-inspur-ispim-ldap-info-module) – Get ldap information
- [ldisk_info module](ldisk_info_module.md#ansible-collections-inspur-ispim-ldisk-info-module) – Get logical disks information
- [log_setting_info module](log_setting_info_module.md#ansible-collections-inspur-ispim-log-setting-info-module) – Get bmc log setting information
- [media_instance_info module](media_instance_info_module.md#ansible-collections-inspur-ispim-media-instance-info-module) – Get Virtual Media Instance information
- [mem_info module](mem_info_module.md#ansible-collections-inspur-ispim-mem-info-module) – Get memory information
- [ncsi_info module](ncsi_info_module.md#ansible-collections-inspur-ispim-ncsi-info-module) – Get ncsi information
- [network_bond_info module](network_bond_info_module.md#ansible-collections-inspur-ispim-network-bond-info-module) – Get network bond information
- [network_info module](network_info_module.md#ansible-collections-inspur-ispim-network-info-module) – Get network information
- [network_link_info module](network_link_info_module.md#ansible-collections-inspur-ispim-network-link-info-module) – Get network link information
- [ntp_info module](ntp_info_module.md#ansible-collections-inspur-ispim-ntp-info-module) – Get NTP information
- [onboard_disk_info module](onboard_disk_info_module.md#ansible-collections-inspur-ispim-onboard-disk-info-module) – Get onboard disks information
- [pcie_info module](pcie_info_module.md#ansible-collections-inspur-ispim-pcie-info-module) – Get PCIE information
- [pdisk_info module](pdisk_info_module.md#ansible-collections-inspur-ispim-pdisk-info-module) – Get physical disks information
- [power_budget_info module](power_budget_info_module.md#ansible-collections-inspur-ispim-power-budget-info-module) – Get power budget information
- [power_consumption_info module](power_consumption_info_module.md#ansible-collections-inspur-ispim-power-consumption-info-module) – Get power consumption information
- [power_restore_info module](power_restore_info_module.md#ansible-collections-inspur-ispim-power-restore-info-module) – Get power restore information
- [power_status_info module](power_status_info_module.md#ansible-collections-inspur-ispim-power-status-info-module) – Get power status information
- [preserve_config_info module](preserve_config_info_module.md#ansible-collections-inspur-ispim-preserve-config-info-module) – Get preserve config information
- [psu_config_info module](psu_config_info_module.md#ansible-collections-inspur-ispim-psu-config-info-module) – Get psu config information
- [psu_info module](psu_info_module.md#ansible-collections-inspur-ispim-psu-info-module) – Get psu information
- [psu_peak_info module](psu_peak_info_module.md#ansible-collections-inspur-ispim-psu-peak-info-module) – Get psu peak information
- [raid_info module](raid_info_module.md#ansible-collections-inspur-ispim-raid-info-module) – Get RAID/HBA card and controller information
- [reset_bmc module](reset_bmc_module.md#ansible-collections-inspur-ispim-reset-bmc-module) – BMC reset
- [reset_kvm module](reset_kvm_module.md#ansible-collections-inspur-ispim-reset-kvm-module) – KVM reset
- [restore module](restore_module.md#ansible-collections-inspur-ispim-restore-module) – Restore server settings
- [self_test_info module](self_test_info_module.md#ansible-collections-inspur-ispim-self-test-info-module) – Get self test information
- [sensor_info module](sensor_info_module.md#ansible-collections-inspur-ispim-sensor-info-module) – Get sensor information
- [server_info module](server_info_module.md#ansible-collections-inspur-ispim-server-info-module) – Get server status information
- [service_info module](service_info_module.md#ansible-collections-inspur-ispim-service-info-module) – Get service information
- [session_info module](session_info_module.md#ansible-collections-inspur-ispim-session-info-module) – Get online session information
- [smtp_info module](smtp_info_module.md#ansible-collections-inspur-ispim-smtp-info-module) – Get SMTP information
- [snmp_info module](snmp_info_module.md#ansible-collections-inspur-ispim-snmp-info-module) – Get snmp get/set information
- [snmp_trap_info module](snmp_trap_info_module.md#ansible-collections-inspur-ispim-snmp-trap-info-module) – Get snmp trap information
- [support_info module](support_info_module.md#ansible-collections-inspur-ispim-support-info-module) – Get support information
- [system_log_info module](system_log_info_module.md#ansible-collections-inspur-ispim-system-log-info-module) – Get BMC system log information
- [temp_info module](temp_info_module.md#ansible-collections-inspur-ispim-temp-info-module) – Get temp information
- [threshold_info module](threshold_info_module.md#ansible-collections-inspur-ispim-threshold-info-module) – Get threshold information
- [uid_info module](uid_info_module.md#ansible-collections-inspur-ispim-uid-info-module) – Get UID information
- [update_cpld module](update_cpld_module.md#ansible-collections-inspur-ispim-update-cpld-module) – Update CPLD
- [update_fw module](update_fw_module.md#ansible-collections-inspur-ispim-update-fw-module) – Update firmware
- [user module](user_module.md#ansible-collections-inspur-ispim-user-module) – Manage user
- [user_group module](user_group_module.md#ansible-collections-inspur-ispim-user-group-module) – Manage user group
- [user_group_info module](user_group_info_module.md#ansible-collections-inspur-ispim-user-group-info-module) – Get user group information
- [user_info module](user_info_module.md#ansible-collections-inspur-ispim-user-info-module) – Get user information
- [virtual_media_info module](virtual_media_info_module.md#ansible-collections-inspur-ispim-virtual-media-info-module) – Get Virtual Media information
- [volt_info module](volt_info_module.md#ansible-collections-inspur-ispim-volt-info-module) – Get volt information

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

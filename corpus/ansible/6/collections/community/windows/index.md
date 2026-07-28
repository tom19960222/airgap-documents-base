---
collection: ansible
version: "6"
title: "Community.Windows"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/
fetched_at: 2026-07-28T00:25:18+00:00
---
# Community.Windows

Collection version 1.11.1

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible collection for community Windows plugins.

**Authors:**

- Jordan Borean @jborean93
- Matt Davis @nitzmahone

**Supported ansible-core versions:**

- 2.11 or newer

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)

## [Communication](index.md#id2)

- Matrix room `#windows:ansible.im`: [General usage and support questions](https://matrix.to/#/#windows:ansible.im).
- IRC channel `#ansible-windows` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible-windows).

## [Plugin Index](index.md#id3)

These are the plugins in the community.windows collection:

### Modules

- [psexec module](psexec_module.md#ansible-collections-community-windows-psexec-module) – Runs commands on a remote Windows host based on the PsExec model
- [win_audit_policy_system module](win_audit_policy_system_module.md#ansible-collections-community-windows-win-audit-policy-system-module) – Used to make changes to the system wide Audit Policy
- [win_audit_rule module](win_audit_rule_module.md#ansible-collections-community-windows-win-audit-rule-module) – Adds an audit rule to files, folders, or registry keys
- [win_auto_logon module](win_auto_logon_module.md#ansible-collections-community-windows-win-auto-logon-module) – Adds or Sets auto logon registry keys.
- [win_certificate_info module](win_certificate_info_module.md#ansible-collections-community-windows-win-certificate-info-module) – Get information on certificates from a Windows Certificate Store
- [win_computer_description module](win_computer_description_module.md#ansible-collections-community-windows-win-computer-description-module) – Set windows description, owner and organization
- [win_credential module](win_credential_module.md#ansible-collections-community-windows-win-credential-module) – Manages Windows Credentials in the Credential Manager
- [win_data_deduplication module](win_data_deduplication_module.md#ansible-collections-community-windows-win-data-deduplication-module) – Module to enable Data Deduplication on a volume.
- [win_defrag module](win_defrag_module.md#ansible-collections-community-windows-win-defrag-module) – Consolidate fragmented files on local volumes
- [win_dhcp_lease module](win_dhcp_lease_module.md#ansible-collections-community-windows-win-dhcp-lease-module) – Manage Windows Server DHCP Leases
- [win_disk_facts module](win_disk_facts_module.md#ansible-collections-community-windows-win-disk-facts-module) – Show the attached disks and disk information of the target host
- [win_disk_image module](win_disk_image_module.md#ansible-collections-community-windows-win-disk-image-module) – Manage ISO/VHD/VHDX mounts on Windows hosts
- [win_dns_record module](win_dns_record_module.md#ansible-collections-community-windows-win-dns-record-module) – Manage Windows Server DNS records
- [win_dns_zone module](win_dns_zone_module.md#ansible-collections-community-windows-win-dns-zone-module) – Manage Windows Server DNS Zones
- [win_domain_computer module](win_domain_computer_module.md#ansible-collections-community-windows-win-domain-computer-module) – Manage computers in Active Directory
- [win_domain_group module](win_domain_group_module.md#ansible-collections-community-windows-win-domain-group-module) – Creates, modifies or removes domain groups
- [win_domain_group_membership module](win_domain_group_membership_module.md#ansible-collections-community-windows-win-domain-group-membership-module) – Manage Windows domain group membership
- [win_domain_object_info module](win_domain_object_info_module.md#ansible-collections-community-windows-win-domain-object-info-module) – Gather information an Active Directory object
- [win_domain_ou module](win_domain_ou_module.md#ansible-collections-community-windows-win-domain-ou-module) – Manage Active Directory Organizational Units
- [win_domain_user module](win_domain_user_module.md#ansible-collections-community-windows-win-domain-user-module) – Manages Windows Active Directory user accounts
- [win_dotnet_ngen module](win_dotnet_ngen_module.md#ansible-collections-community-windows-win-dotnet-ngen-module) – Runs ngen to recompile DLLs after .NET updates
- [win_eventlog module](win_eventlog_module.md#ansible-collections-community-windows-win-eventlog-module) – Manage Windows event logs
- [win_eventlog_entry module](win_eventlog_entry_module.md#ansible-collections-community-windows-win-eventlog-entry-module) – Write entries to Windows event logs
- [win_feature_info module](win_feature_info_module.md#ansible-collections-community-windows-win-feature-info-module) – Gather information about Windows features
- [win_file_compression module](win_file_compression_module.md#ansible-collections-community-windows-win-file-compression-module) – Alters the compression of files and directories on NTFS partitions.
- [win_file_version module](win_file_version_module.md#ansible-collections-community-windows-win-file-version-module) – Get DLL or EXE file build version
- [win_firewall module](win_firewall_module.md#ansible-collections-community-windows-win-firewall-module) – Enable or disable the Windows Firewall
- [win_firewall_rule module](win_firewall_rule_module.md#ansible-collections-community-windows-win-firewall-rule-module) – Windows firewall automation
- [win_format module](win_format_module.md#ansible-collections-community-windows-win-format-module) – Formats an existing volume or a new volume on an existing partition on Windows
- [win_hosts module](win_hosts_module.md#ansible-collections-community-windows-win-hosts-module) – Manages hosts file entries on Windows.
- [win_hotfix module](win_hotfix_module.md#ansible-collections-community-windows-win-hotfix-module) – Install and uninstalls Windows hotfixes
- [win_http_proxy module](win_http_proxy_module.md#ansible-collections-community-windows-win-http-proxy-module) – Manages proxy settings for WinHTTP
- [win_iis_virtualdirectory module](win_iis_virtualdirectory_module.md#ansible-collections-community-windows-win-iis-virtualdirectory-module) – Configures a virtual directory in IIS
- [win_iis_webapplication module](win_iis_webapplication_module.md#ansible-collections-community-windows-win-iis-webapplication-module) – Configures IIS web applications
- [win_iis_webapppool module](win_iis_webapppool_module.md#ansible-collections-community-windows-win-iis-webapppool-module) – Configure IIS Web Application Pools
- [win_iis_webbinding module](win_iis_webbinding_module.md#ansible-collections-community-windows-win-iis-webbinding-module) – Configures a IIS Web site binding
- [win_iis_website module](win_iis_website_module.md#ansible-collections-community-windows-win-iis-website-module) – Configures a IIS Web site
- [win_inet_proxy module](win_inet_proxy_module.md#ansible-collections-community-windows-win-inet-proxy-module) – Manages proxy settings for WinINet and Internet Explorer
- [win_initialize_disk module](win_initialize_disk_module.md#ansible-collections-community-windows-win-initialize-disk-module) – Initializes disks on Windows Server
- [win_lineinfile module](win_lineinfile_module.md#ansible-collections-community-windows-win-lineinfile-module) – Ensure a particular line is in a file, or replace an existing line using a back-referenced regular expression
- [win_listen_ports_facts module](win_listen_ports_facts_module.md#ansible-collections-community-windows-win-listen-ports-facts-module) – Recopilates the facts of the listening ports of the machine
- [win_mapped_drive module](win_mapped_drive_module.md#ansible-collections-community-windows-win-mapped-drive-module) – Map network drives for users
- [win_msg module](win_msg_module.md#ansible-collections-community-windows-win-msg-module) – Sends a message to logged in users on Windows hosts
- [win_net_adapter_feature module](win_net_adapter_feature_module.md#ansible-collections-community-windows-win-net-adapter-feature-module) – Enable or disable certain network adapters.
- [win_netbios module](win_netbios_module.md#ansible-collections-community-windows-win-netbios-module) – Manage NetBIOS over TCP/IP settings on Windows.
- [win_nssm module](win_nssm_module.md#ansible-collections-community-windows-win-nssm-module) – Install a service using NSSM
- [win_pagefile module](win_pagefile_module.md#ansible-collections-community-windows-win-pagefile-module) – Query or change pagefile configuration
- [win_partition module](win_partition_module.md#ansible-collections-community-windows-win-partition-module) – Creates, changes and removes partitions on Windows Server
- [win_pester module](win_pester_module.md#ansible-collections-community-windows-win-pester-module) – Run Pester tests on Windows hosts
- [win_power_plan module](win_power_plan_module.md#ansible-collections-community-windows-win-power-plan-module) – Changes the power plan of a Windows system
- [win_product_facts module](win_product_facts_module.md#ansible-collections-community-windows-win-product-facts-module) – Provides Windows product and license information
- [win_psexec module](win_psexec_module.md#ansible-collections-community-windows-win-psexec-module) – Runs commands (remotely) as another (privileged) user
- [win_psmodule module](win_psmodule_module.md#ansible-collections-community-windows-win-psmodule-module) – Adds or removes a Windows PowerShell module
- [win_psmodule_info module](win_psmodule_info_module.md#ansible-collections-community-windows-win-psmodule-info-module) – Gather information about PowerShell Modules
- [win_psrepository module](win_psrepository_module.md#ansible-collections-community-windows-win-psrepository-module) – Adds, removes or updates a Windows PowerShell repository.
- [win_psrepository_copy module](win_psrepository_copy_module.md#ansible-collections-community-windows-win-psrepository-copy-module) – Copies registered PSRepositories to other user profiles
- [win_psrepository_info module](win_psrepository_info_module.md#ansible-collections-community-windows-win-psrepository-info-module) – Gather information about PSRepositories
- [win_psscript module](win_psscript_module.md#ansible-collections-community-windows-win-psscript-module) – Install and manage PowerShell scripts from a PSRepository
- [win_psscript_info module](win_psscript_info_module.md#ansible-collections-community-windows-win-psscript-info-module) – Gather information about installed PowerShell Scripts
- [win_pssession_configuration module](win_pssession_configuration_module.md#ansible-collections-community-windows-win-pssession-configuration-module) – Manage PSSession Configurations
- [win_rabbitmq_plugin module](win_rabbitmq_plugin_module.md#ansible-collections-community-windows-win-rabbitmq-plugin-module) – Manage RabbitMQ plugins
- [win_rds_cap module](win_rds_cap_module.md#ansible-collections-community-windows-win-rds-cap-module) – Manage Connection Authorization Policies (CAP) on a Remote Desktop Gateway server
- [win_rds_rap module](win_rds_rap_module.md#ansible-collections-community-windows-win-rds-rap-module) – Manage Resource Authorization Policies (RAP) on a Remote Desktop Gateway server
- [win_rds_settings module](win_rds_settings_module.md#ansible-collections-community-windows-win-rds-settings-module) – Manage main settings of a Remote Desktop Gateway server
- [win_region module](win_region_module.md#ansible-collections-community-windows-win-region-module) – Set the region and format settings
- [win_regmerge module](win_regmerge_module.md#ansible-collections-community-windows-win-regmerge-module) – Merges the contents of a registry file into the Windows registry
- [win_robocopy module](win_robocopy_module.md#ansible-collections-community-windows-win-robocopy-module) – Synchronizes the contents of two directories using Robocopy
- [win_route module](win_route_module.md#ansible-collections-community-windows-win-route-module) – Add or remove a static route
- [win_say module](win_say_module.md#ansible-collections-community-windows-win-say-module) – Text to speech module for Windows to speak messages and optionally play sounds
- [win_scheduled_task module](win_scheduled_task_module.md#ansible-collections-community-windows-win-scheduled-task-module) – Manage scheduled tasks
- [win_scheduled_task_stat module](win_scheduled_task_stat_module.md#ansible-collections-community-windows-win-scheduled-task-stat-module) – Get information about Windows Scheduled Tasks
- [win_scoop module](win_scoop_module.md#ansible-collections-community-windows-win-scoop-module) – Manage packages using Scoop
- [win_scoop_bucket module](win_scoop_bucket_module.md#ansible-collections-community-windows-win-scoop-bucket-module) – Manage Scoop buckets
- [win_security_policy module](win_security_policy_module.md#ansible-collections-community-windows-win-security-policy-module) – Change local security policy settings
- [win_shortcut module](win_shortcut_module.md#ansible-collections-community-windows-win-shortcut-module) – Manage shortcuts on Windows
- [win_snmp module](win_snmp_module.md#ansible-collections-community-windows-win-snmp-module) – Configures the Windows SNMP service
- [win_timezone module](win_timezone_module.md#ansible-collections-community-windows-win-timezone-module) – Sets Windows machine timezone
- [win_toast module](win_toast_module.md#ansible-collections-community-windows-win-toast-module) – Sends Toast windows notification to logged in users on Windows 10 or later hosts
- [win_unzip module](win_unzip_module.md#ansible-collections-community-windows-win-unzip-module) – Unzips compressed files and archives on the Windows node
- [win_user_profile module](win_user_profile_module.md#ansible-collections-community-windows-win-user-profile-module) – Manages the Windows user profiles.
- [win_wait_for_process module](win_wait_for_process_module.md#ansible-collections-community-windows-win-wait-for-process-module) – Waits for a process to exist or not exist before continuing.
- [win_wakeonlan module](win_wakeonlan_module.md#ansible-collections-community-windows-win-wakeonlan-module) – Send a magic Wake-on-LAN (WoL) broadcast packet
- [win_webpicmd module](win_webpicmd_module.md#ansible-collections-community-windows-win-webpicmd-module) – Installs packages using Web Platform Installer command-line
- [win_xml module](win_xml_module.md#ansible-collections-community-windows-win-xml-module) – Manages XML file content on Windows hosts
- [win_zip module](win_zip_module.md#ansible-collections-community-windows-win-zip-module) – Compress file or directory as zip archive on the Windows node

### Lookup Plugins

- [laps_password lookup](laps_password_lookup.md#ansible-collections-community-windows-laps-password-lookup) – Retrieves the LAPS password for a server.

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

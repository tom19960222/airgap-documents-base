---
collection: ansible
version: "8"
title: "Community.Vmware"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/index.html
fetched_at: 2026-07-28T01:02:24+00:00
---
# Community.Vmware

Collection version 3.11.1

- [Description](index.md#description)
- [Scenario Guide](index.md#scenario-guide)
- [Developer Guide](index.md#developer-guide)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

**Author:**

- Ansible (<https://github.com/ansible>)

**Supported ansible-core versions:**

- 2.13.0 or newer

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)

## [Scenario Guide](index.md#id2)

- [VMware Guide](docsite/scenario_guide.md)

## [Developer Guide](index.md#id3)

- [Guidelines for VMware module development](docsite/dev_guide.md)

## [Plugin Index](index.md#id4)

These are the plugins in the community.vmware collection:

### Modules

- [vcenter_domain_user_group_info module](vcenter_domain_user_group_info_module.md#ansible-collections-community-vmware-vcenter-domain-user-group-info-module) – Gather user or group information of a domain
- [vcenter_extension module](vcenter_extension_module.md#ansible-collections-community-vmware-vcenter-extension-module) – Register/deregister vCenter Extensions
- [vcenter_extension_info module](vcenter_extension_info_module.md#ansible-collections-community-vmware-vcenter-extension-info-module) – Gather info vCenter extensions
- [vcenter_folder module](vcenter_folder_module.md#ansible-collections-community-vmware-vcenter-folder-module) – Manage folders on given datacenter
- [vcenter_license module](vcenter_license_module.md#ansible-collections-community-vmware-vcenter-license-module) – Manage VMware vCenter license keys
- [vcenter_root_password_expiration module](vcenter_root_password_expiration_module.md#ansible-collections-community-vmware-vcenter-root-password-expiration-module) – root password expiration of vCSA
- [vcenter_standard_key_provider module](vcenter_standard_key_provider_module.md#ansible-collections-community-vmware-vcenter-standard-key-provider-module) – Add, reconfigure or remove Standard Key Provider on vCenter server
- [vmware_about_info module](vmware_about_info_module.md#ansible-collections-community-vmware-vmware-about-info-module) – Provides information about VMware server to which user is connecting to
- [vmware_category module](vmware_category_module.md#ansible-collections-community-vmware-vmware-category-module) – Manage VMware categories
- [vmware_category_info module](vmware_category_info_module.md#ansible-collections-community-vmware-vmware-category-info-module) – Gather info about VMware tag categories
- [vmware_cfg_backup module](vmware_cfg_backup_module.md#ansible-collections-community-vmware-vmware-cfg-backup-module) – Backup / Restore / Reset ESXi host configuration
- [vmware_cluster module](vmware_cluster_module.md#ansible-collections-community-vmware-vmware-cluster-module) – Manage VMware vSphere clusters
- [vmware_cluster_dpm module](vmware_cluster_dpm_module.md#ansible-collections-community-vmware-vmware-cluster-dpm-module) – Manage Distributed Power Management (DPM) on VMware vSphere clusters
- [vmware_cluster_drs module](vmware_cluster_drs_module.md#ansible-collections-community-vmware-vmware-cluster-drs-module) – Manage Distributed Resource Scheduler (DRS) on VMware vSphere clusters
- [vmware_cluster_drs_recommendations module](vmware_cluster_drs_recommendations_module.md#ansible-collections-community-vmware-vmware-cluster-drs-recommendations-module) – Apply DRS Recommendations
- [vmware_cluster_ha module](vmware_cluster_ha_module.md#ansible-collections-community-vmware-vmware-cluster-ha-module) – Manage High Availability (HA) on VMware vSphere clusters
- [vmware_cluster_info module](vmware_cluster_info_module.md#ansible-collections-community-vmware-vmware-cluster-info-module) – Gather info about clusters available in given vCenter
- [vmware_cluster_vcls module](vmware_cluster_vcls_module.md#ansible-collections-community-vmware-vmware-cluster-vcls-module) – Override the default vCLS (vSphere Cluster Services) VM disk placement for this cluster.
- [vmware_cluster_vsan module](vmware_cluster_vsan_module.md#ansible-collections-community-vmware-vmware-cluster-vsan-module) – Manages virtual storage area network (vSAN) configuration on VMware vSphere clusters
- [vmware_content_deploy_ovf_template module](vmware_content_deploy_ovf_template_module.md#ansible-collections-community-vmware-vmware-content-deploy-ovf-template-module) – Deploy Virtual Machine from ovf template stored in content library.
- [vmware_content_deploy_template module](vmware_content_deploy_template_module.md#ansible-collections-community-vmware-vmware-content-deploy-template-module) – Deploy Virtual Machine from template stored in content library.
- [vmware_content_library_info module](vmware_content_library_info_module.md#ansible-collections-community-vmware-vmware-content-library-info-module) – Gather information about VMWare Content Library
- [vmware_content_library_manager module](vmware_content_library_manager_module.md#ansible-collections-community-vmware-vmware-content-library-manager-module) – Create, update and delete VMware content library
- [vmware_custom_attribute module](vmware_custom_attribute_module.md#ansible-collections-community-vmware-vmware-custom-attribute-module) – Manage custom attributes definitions
- [vmware_custom_attribute_manager module](vmware_custom_attribute_manager_module.md#ansible-collections-community-vmware-vmware-custom-attribute-manager-module) – Manage custom attributes from VMware for the given vSphere object
- [vmware_datacenter module](vmware_datacenter_module.md#ansible-collections-community-vmware-vmware-datacenter-module) – Manage VMware vSphere Datacenters
- [vmware_datacenter_info module](vmware_datacenter_info_module.md#ansible-collections-community-vmware-vmware-datacenter-info-module) – Gather information about VMware vSphere Datacenters
- [vmware_datastore module](vmware_datastore_module.md#ansible-collections-community-vmware-vmware-datastore-module) – Configure Datastores
- [vmware_datastore_cluster module](vmware_datastore_cluster_module.md#ansible-collections-community-vmware-vmware-datastore-cluster-module) – Manage VMware vSphere datastore clusters
- [vmware_datastore_cluster_manager module](vmware_datastore_cluster_manager_module.md#ansible-collections-community-vmware-vmware-datastore-cluster-manager-module) – Manage VMware vSphere datastore cluster’s members
- [vmware_datastore_info module](vmware_datastore_info_module.md#ansible-collections-community-vmware-vmware-datastore-info-module) – Gather info about datastores available in given vCenter
- [vmware_datastore_maintenancemode module](vmware_datastore_maintenancemode_module.md#ansible-collections-community-vmware-vmware-datastore-maintenancemode-module) – Place a datastore into maintenance mode
- [vmware_deploy_ovf module](vmware_deploy_ovf_module.md#ansible-collections-community-vmware-vmware-deploy-ovf-module) – Deploys a VMware virtual machine from an OVF or OVA file, placed on file system or HTTP server
- [vmware_drs_group module](vmware_drs_group_module.md#ansible-collections-community-vmware-vmware-drs-group-module) – Creates vm/host group in a given cluster.
- [vmware_drs_group_info module](vmware_drs_group_info_module.md#ansible-collections-community-vmware-vmware-drs-group-info-module) – Gathers info about DRS VM/Host groups on the given cluster
- [vmware_drs_group_manager module](vmware_drs_group_manager_module.md#ansible-collections-community-vmware-vmware-drs-group-manager-module) – Manage VMs and Hosts in DRS group.
- [vmware_drs_rule_info module](vmware_drs_rule_info_module.md#ansible-collections-community-vmware-vmware-drs-rule-info-module) – Gathers info about DRS rule on the given cluster
- [vmware_dvs_host module](vmware_dvs_host_module.md#ansible-collections-community-vmware-vmware-dvs-host-module) – Add or remove a host from distributed virtual switch
- [vmware_dvs_portgroup module](vmware_dvs_portgroup_module.md#ansible-collections-community-vmware-vmware-dvs-portgroup-module) – Create or remove a Distributed vSwitch portgroup.
- [vmware_dvs_portgroup_find module](vmware_dvs_portgroup_find_module.md#ansible-collections-community-vmware-vmware-dvs-portgroup-find-module) – Find portgroup(s) in a VMware environment
- [vmware_dvs_portgroup_info module](vmware_dvs_portgroup_info_module.md#ansible-collections-community-vmware-vmware-dvs-portgroup-info-module) – Gathers info DVS portgroup configurations
- [vmware_dvswitch module](vmware_dvswitch_module.md#ansible-collections-community-vmware-vmware-dvswitch-module) – Create or remove a Distributed Switch
- [vmware_dvswitch_info module](vmware_dvswitch_info_module.md#ansible-collections-community-vmware-vmware-dvswitch-info-module) – Gathers info dvswitch configurations
- [vmware_dvswitch_lacp module](vmware_dvswitch_lacp_module.md#ansible-collections-community-vmware-vmware-dvswitch-lacp-module) – Manage LACP configuration on a Distributed Switch
- [vmware_dvswitch_nioc module](vmware_dvswitch_nioc_module.md#ansible-collections-community-vmware-vmware-dvswitch-nioc-module) – Manage distributed switch Network IO Control
- [vmware_dvswitch_pvlans module](vmware_dvswitch_pvlans_module.md#ansible-collections-community-vmware-vmware-dvswitch-pvlans-module) – Manage Private VLAN configuration of a Distributed Switch
- [vmware_dvswitch_uplink_pg module](vmware_dvswitch_uplink_pg_module.md#ansible-collections-community-vmware-vmware-dvswitch-uplink-pg-module) – Manage uplink portgroup configuration of a Distributed Switch
- [vmware_evc_mode module](vmware_evc_mode_module.md#ansible-collections-community-vmware-vmware-evc-mode-module) – Enable/Disable EVC mode on vCenter
- [vmware_export_ovf module](vmware_export_ovf_module.md#ansible-collections-community-vmware-vmware-export-ovf-module) – Exports a VMware virtual machine to an OVF file, device files and a manifest file
- [vmware_first_class_disk module](vmware_first_class_disk_module.md#ansible-collections-community-vmware-vmware-first-class-disk-module) – Manage VMware vSphere First Class Disks
- [vmware_folder_info module](vmware_folder_info_module.md#ansible-collections-community-vmware-vmware-folder-info-module) – Provides information about folders in a datacenter
- [vmware_guest module](vmware_guest_module.md#ansible-collections-community-vmware-vmware-guest-module) – Manages virtual machines in vCenter
- [vmware_guest_boot_info module](vmware_guest_boot_info_module.md#ansible-collections-community-vmware-vmware-guest-boot-info-module) – Gather info about boot options for the given virtual machine
- [vmware_guest_boot_manager module](vmware_guest_boot_manager_module.md#ansible-collections-community-vmware-vmware-guest-boot-manager-module) – Manage boot options for the given virtual machine
- [vmware_guest_controller module](vmware_guest_controller_module.md#ansible-collections-community-vmware-vmware-guest-controller-module) – Manage disk or USB controllers related to virtual machine in given vCenter infrastructure
- [vmware_guest_cross_vc_clone module](vmware_guest_cross_vc_clone_module.md#ansible-collections-community-vmware-vmware-guest-cross-vc-clone-module) – Cross-vCenter VM/template clone
- [vmware_guest_custom_attribute_defs module](vmware_guest_custom_attribute_defs_module.md#ansible-collections-community-vmware-vmware-guest-custom-attribute-defs-module) – Manage custom attributes definitions for virtual machine from VMware
- [vmware_guest_custom_attributes module](vmware_guest_custom_attributes_module.md#ansible-collections-community-vmware-vmware-guest-custom-attributes-module) – Manage custom attributes from VMware for the given virtual machine
- [vmware_guest_customization_info module](vmware_guest_customization_info_module.md#ansible-collections-community-vmware-vmware-guest-customization-info-module) – Gather info about VM customization specifications
- [vmware_guest_disk module](vmware_guest_disk_module.md#ansible-collections-community-vmware-vmware-guest-disk-module) – Manage disks related to virtual machine in given vCenter infrastructure
- [vmware_guest_disk_info module](vmware_guest_disk_info_module.md#ansible-collections-community-vmware-vmware-guest-disk-info-module) – Gather info about disks of given virtual machine
- [vmware_guest_file_operation module](vmware_guest_file_operation_module.md#ansible-collections-community-vmware-vmware-guest-file-operation-module) – Files operation in a VMware guest operating system without network
- [vmware_guest_find module](vmware_guest_find_module.md#ansible-collections-community-vmware-vmware-guest-find-module) – Find the folder path(s) for a virtual machine by name or UUID
- [vmware_guest_info module](vmware_guest_info_module.md#ansible-collections-community-vmware-vmware-guest-info-module) – Gather info about a single VM
- [vmware_guest_instant_clone module](vmware_guest_instant_clone_module.md#ansible-collections-community-vmware-vmware-guest-instant-clone-module) – Instant Clone VM
- [vmware_guest_move module](vmware_guest_move_module.md#ansible-collections-community-vmware-vmware-guest-move-module) – Moves virtual machines in vCenter
- [vmware_guest_network module](vmware_guest_network_module.md#ansible-collections-community-vmware-vmware-guest-network-module) – Manage network adapters of specified virtual machine in given vCenter infrastructure
- [vmware_guest_powerstate module](vmware_guest_powerstate_module.md#ansible-collections-community-vmware-vmware-guest-powerstate-module) – Manages power states of virtual machines in vCenter
- [vmware_guest_register_operation module](vmware_guest_register_operation_module.md#ansible-collections-community-vmware-vmware-guest-register-operation-module) – VM inventory registration operation
- [vmware_guest_screenshot module](vmware_guest_screenshot_module.md#ansible-collections-community-vmware-vmware-guest-screenshot-module) – Create a screenshot of the Virtual Machine console.
- [vmware_guest_sendkey module](vmware_guest_sendkey_module.md#ansible-collections-community-vmware-vmware-guest-sendkey-module) – Send USB HID codes to the Virtual Machine’s keyboard.
- [vmware_guest_serial_port module](vmware_guest_serial_port_module.md#ansible-collections-community-vmware-vmware-guest-serial-port-module) – Manage serial ports on an existing VM
- [vmware_guest_snapshot module](vmware_guest_snapshot_module.md#ansible-collections-community-vmware-vmware-guest-snapshot-module) – Manages virtual machines snapshots in vCenter
- [vmware_guest_snapshot_info module](vmware_guest_snapshot_info_module.md#ansible-collections-community-vmware-vmware-guest-snapshot-info-module) – Gather info about virtual machine’s snapshots in vCenter
- [vmware_guest_storage_policy module](vmware_guest_storage_policy_module.md#ansible-collections-community-vmware-vmware-guest-storage-policy-module) – Set VM Home and disk(s) storage policy profiles.
- [vmware_guest_tools_info module](vmware_guest_tools_info_module.md#ansible-collections-community-vmware-vmware-guest-tools-info-module) – Gather info about VMware tools installed in VM
- [vmware_guest_tools_upgrade module](vmware_guest_tools_upgrade_module.md#ansible-collections-community-vmware-vmware-guest-tools-upgrade-module) – Module to upgrade VMTools
- [vmware_guest_tools_wait module](vmware_guest_tools_wait_module.md#ansible-collections-community-vmware-vmware-guest-tools-wait-module) – Wait for VMware tools to become available
- [vmware_guest_tpm module](vmware_guest_tpm_module.md#ansible-collections-community-vmware-vmware-guest-tpm-module) – Add or remove vTPM device for specified VM.
- [vmware_guest_vgpu module](vmware_guest_vgpu_module.md#ansible-collections-community-vmware-vmware-guest-vgpu-module) – Modify vGPU video card profile of the specified virtual machine in the given vCenter infrastructure
- [vmware_guest_vgpu_info module](vmware_guest_vgpu_info_module.md#ansible-collections-community-vmware-vmware-guest-vgpu-info-module) – Gather information about vGPU profiles of the specified virtual machine in the given vCenter infrastructure
- [vmware_guest_video module](vmware_guest_video_module.md#ansible-collections-community-vmware-vmware-guest-video-module) – Modify video card configurations of specified virtual machine in given vCenter infrastructure
- [vmware_host module](vmware_host_module.md#ansible-collections-community-vmware-vmware-host-module) – Add, remove, or move an ESXi host to, from, or within vCenter
- [vmware_host_acceptance module](vmware_host_acceptance_module.md#ansible-collections-community-vmware-vmware-host-acceptance-module) – Manage the host acceptance level of an ESXi host
- [vmware_host_active_directory module](vmware_host_active_directory_module.md#ansible-collections-community-vmware-vmware-host-active-directory-module) – Joins an ESXi host system to an Active Directory domain or leaves it
- [vmware_host_auto_start module](vmware_host_auto_start_module.md#ansible-collections-community-vmware-vmware-host-auto-start-module) – Manage the auto power ON or OFF for vm on ESXi host
- [vmware_host_capability_info module](vmware_host_capability_info_module.md#ansible-collections-community-vmware-vmware-host-capability-info-module) – Gathers info about an ESXi host’s capability information
- [vmware_host_config_info module](vmware_host_config_info_module.md#ansible-collections-community-vmware-vmware-host-config-info-module) – Gathers info about an ESXi host’s advance configuration information
- [vmware_host_config_manager module](vmware_host_config_manager_module.md#ansible-collections-community-vmware-vmware-host-config-manager-module) – Manage advanced system settings of an ESXi host
- [vmware_host_custom_attributes module](vmware_host_custom_attributes_module.md#ansible-collections-community-vmware-vmware-host-custom-attributes-module) – Manage custom attributes from VMware for the given ESXi host
- [vmware_host_datastore module](vmware_host_datastore_module.md#ansible-collections-community-vmware-vmware-host-datastore-module) – Manage a datastore on ESXi host
- [vmware_host_disk_info module](vmware_host_disk_info_module.md#ansible-collections-community-vmware-vmware-host-disk-info-module) – Gathers information about disks attached to given ESXi host/s.
- [vmware_host_dns module](vmware_host_dns_module.md#ansible-collections-community-vmware-vmware-host-dns-module) – Manage DNS configuration of an ESXi host system
- [vmware_host_dns_info module](vmware_host_dns_info_module.md#ansible-collections-community-vmware-vmware-host-dns-info-module) – Gathers info about an ESXi host’s DNS configuration information
- [vmware_host_facts module](vmware_host_facts_module.md#ansible-collections-community-vmware-vmware-host-facts-module) – Gathers facts about remote ESXi hostsystem
- [vmware_host_feature_info module](vmware_host_feature_info_module.md#ansible-collections-community-vmware-vmware-host-feature-info-module) – Gathers info about an ESXi host’s feature capability information
- [vmware_host_firewall_info module](vmware_host_firewall_info_module.md#ansible-collections-community-vmware-vmware-host-firewall-info-module) – Gathers info about an ESXi host’s firewall configuration information
- [vmware_host_firewall_manager module](vmware_host_firewall_manager_module.md#ansible-collections-community-vmware-vmware-host-firewall-manager-module) – Manage firewall configurations about an ESXi host
- [vmware_host_graphics module](vmware_host_graphics_module.md#ansible-collections-community-vmware-vmware-host-graphics-module) – Manage Host Graphic Settings
- [vmware_host_hyperthreading module](vmware_host_hyperthreading_module.md#ansible-collections-community-vmware-vmware-host-hyperthreading-module) – Enables/Disables Hyperthreading optimization for an ESXi host system
- [vmware_host_ipv6 module](vmware_host_ipv6_module.md#ansible-collections-community-vmware-vmware-host-ipv6-module) – Enables/Disables IPv6 support for an ESXi host system
- [vmware_host_iscsi module](vmware_host_iscsi_module.md#ansible-collections-community-vmware-vmware-host-iscsi-module) – Manage the iSCSI configuration of ESXi host
- [vmware_host_iscsi_info module](vmware_host_iscsi_info_module.md#ansible-collections-community-vmware-vmware-host-iscsi-info-module) – Gather iSCSI configuration information of ESXi host
- [vmware_host_kernel_manager module](vmware_host_kernel_manager_module.md#ansible-collections-community-vmware-vmware-host-kernel-manager-module) – Manage kernel module options on ESXi hosts
- [vmware_host_lockdown module](vmware_host_lockdown_module.md#ansible-collections-community-vmware-vmware-host-lockdown-module) – Manage administrator permission for the local administrative account for the ESXi host
- [vmware_host_lockdown_exceptions module](vmware_host_lockdown_exceptions_module.md#ansible-collections-community-vmware-vmware-host-lockdown-exceptions-module) – Manage Lockdown Mode Exception Users
- [vmware_host_logbundle module](vmware_host_logbundle_module.md#ansible-collections-community-vmware-vmware-host-logbundle-module) – Fetch logbundle file from ESXi
- [vmware_host_logbundle_info module](vmware_host_logbundle_info_module.md#ansible-collections-community-vmware-vmware-host-logbundle-info-module) – Gathers manifest info for logbundle
- [vmware_host_ntp module](vmware_host_ntp_module.md#ansible-collections-community-vmware-vmware-host-ntp-module) – Manage NTP server configuration of an ESXi host
- [vmware_host_ntp_info module](vmware_host_ntp_info_module.md#ansible-collections-community-vmware-vmware-host-ntp-info-module) – Gathers info about NTP configuration on an ESXi host
- [vmware_host_package_info module](vmware_host_package_info_module.md#ansible-collections-community-vmware-vmware-host-package-info-module) – Gathers info about available packages on an ESXi host
- [vmware_host_passthrough module](vmware_host_passthrough_module.md#ansible-collections-community-vmware-vmware-host-passthrough-module) – Manage PCI device passthrough settings on host
- [vmware_host_powermgmt_policy module](vmware_host_powermgmt_policy_module.md#ansible-collections-community-vmware-vmware-host-powermgmt-policy-module) – Manages the Power Management Policy of an ESXI host system
- [vmware_host_powerstate module](vmware_host_powerstate_module.md#ansible-collections-community-vmware-vmware-host-powerstate-module) – Manages power states of host systems in vCenter
- [vmware_host_scanhba module](vmware_host_scanhba_module.md#ansible-collections-community-vmware-vmware-host-scanhba-module) – Rescan host HBA’s and optionally refresh the storage system
- [vmware_host_scsidisk_info module](vmware_host_scsidisk_info_module.md#ansible-collections-community-vmware-vmware-host-scsidisk-info-module) – Gather information about SCSI disk attached to the given ESXi
- [vmware_host_service_info module](vmware_host_service_info_module.md#ansible-collections-community-vmware-vmware-host-service-info-module) – Gathers info about an ESXi host’s services
- [vmware_host_service_manager module](vmware_host_service_manager_module.md#ansible-collections-community-vmware-vmware-host-service-manager-module) – Manage services on a given ESXi host
- [vmware_host_snmp module](vmware_host_snmp_module.md#ansible-collections-community-vmware-vmware-host-snmp-module) – Configures SNMP on an ESXi host system
- [vmware_host_sriov module](vmware_host_sriov_module.md#ansible-collections-community-vmware-vmware-host-sriov-module) – Manage SR-IOV settings on host
- [vmware_host_ssl_info module](vmware_host_ssl_info_module.md#ansible-collections-community-vmware-vmware-host-ssl-info-module) – Gather info of ESXi host system about SSL
- [vmware_host_tcpip_stacks module](vmware_host_tcpip_stacks_module.md#ansible-collections-community-vmware-vmware-host-tcpip-stacks-module) – Manage the TCP/IP Stacks configuration of ESXi host
- [vmware_host_user_manager module](vmware_host_user_manager_module.md#ansible-collections-community-vmware-vmware-host-user-manager-module) – Manage users of ESXi
- [vmware_host_vmhba_info module](vmware_host_vmhba_info_module.md#ansible-collections-community-vmware-vmware-host-vmhba-info-module) – Gathers info about vmhbas available on the given ESXi host
- [vmware_host_vmnic_info module](vmware_host_vmnic_info_module.md#ansible-collections-community-vmware-vmware-host-vmnic-info-module) – Gathers info about vmnics available on the given ESXi host
- [vmware_local_role_info module](vmware_local_role_info_module.md#ansible-collections-community-vmware-vmware-local-role-info-module) – Gather info about local roles on an ESXi host or vCenter
- [vmware_local_role_manager module](vmware_local_role_manager_module.md#ansible-collections-community-vmware-vmware-local-role-manager-module) – Manage local roles on an ESXi host or vCenter
- [vmware_local_user_info module](vmware_local_user_info_module.md#ansible-collections-community-vmware-vmware-local-user-info-module) – Gather info about users on the given ESXi host
- [vmware_local_user_manager module](vmware_local_user_manager_module.md#ansible-collections-community-vmware-vmware-local-user-manager-module) – Manage local users on an ESXi host
- [vmware_maintenancemode module](vmware_maintenancemode_module.md#ansible-collections-community-vmware-vmware-maintenancemode-module) – Place a host into maintenance mode
- [vmware_migrate_vmk module](vmware_migrate_vmk_module.md#ansible-collections-community-vmware-vmware-migrate-vmk-module) – Migrate a VMK interface from VSS to VDS
- [vmware_object_custom_attributes_info module](vmware_object_custom_attributes_info_module.md#ansible-collections-community-vmware-vmware-object-custom-attributes-info-module) – Gather custom attributes of an object
- [vmware_object_rename module](vmware_object_rename_module.md#ansible-collections-community-vmware-vmware-object-rename-module) – Renames VMware objects
- [vmware_object_role_permission module](vmware_object_role_permission_module.md#ansible-collections-community-vmware-vmware-object-role-permission-module) – Manage local roles on an ESXi host or vCenter
- [vmware_object_role_permission_info module](vmware_object_role_permission_info_module.md#ansible-collections-community-vmware-vmware-object-role-permission-info-module) – Gather information about object’s permissions
- [vmware_portgroup module](vmware_portgroup_module.md#ansible-collections-community-vmware-vmware-portgroup-module) – Create a VMware portgroup
- [vmware_portgroup_info module](vmware_portgroup_info_module.md#ansible-collections-community-vmware-vmware-portgroup-info-module) – Gathers info about an ESXi host’s Port Group configuration
- [vmware_recommended_datastore module](vmware_recommended_datastore_module.md#ansible-collections-community-vmware-vmware-recommended-datastore-module) – Returns the recommended datastore from a SDRS-enabled datastore cluster
- [vmware_resource_pool module](vmware_resource_pool_module.md#ansible-collections-community-vmware-vmware-resource-pool-module) – Add/remove resource pools to/from vCenter
- [vmware_resource_pool_info module](vmware_resource_pool_info_module.md#ansible-collections-community-vmware-vmware-resource-pool-info-module) – Gathers info about resource pool information
- [vmware_tag module](vmware_tag_module.md#ansible-collections-community-vmware-vmware-tag-module) – Manage VMware tags
- [vmware_tag_info module](vmware_tag_info_module.md#ansible-collections-community-vmware-vmware-tag-info-module) – Manage VMware tag info
- [vmware_tag_manager module](vmware_tag_manager_module.md#ansible-collections-community-vmware-vmware-tag-manager-module) – Manage association of VMware tags with VMware objects
- [vmware_target_canonical_info module](vmware_target_canonical_info_module.md#ansible-collections-community-vmware-vmware-target-canonical-info-module) – Return canonical (NAA) from an ESXi host system
- [vmware_vasa module](vmware_vasa_module.md#ansible-collections-community-vmware-vmware-vasa-module) – Manage VMware Virtual Volumes storage provider
- [vmware_vasa_info module](vmware_vasa_info_module.md#ansible-collections-community-vmware-vmware-vasa-info-module) – Gather information about vSphere VASA providers.
- [vmware_vc_infraprofile_info module](vmware_vc_infraprofile_info_module.md#ansible-collections-community-vmware-vmware-vc-infraprofile-info-module) – List and Export VMware vCenter infra profile configs.
- [vmware_vcenter_settings module](vmware_vcenter_settings_module.md#ansible-collections-community-vmware-vmware-vcenter-settings-module) – Configures general settings on a vCenter server
- [vmware_vcenter_settings_info module](vmware_vcenter_settings_info_module.md#ansible-collections-community-vmware-vmware-vcenter-settings-info-module) – Gather info vCenter settings
- [vmware_vcenter_statistics module](vmware_vcenter_statistics_module.md#ansible-collections-community-vmware-vmware-vcenter-statistics-module) – Configures statistics on a vCenter server
- [vmware_vm_config_option module](vmware_vm_config_option_module.md#ansible-collections-community-vmware-vmware-vm-config-option-module) – Return supported guest ID list and VM recommended config option for specific guest OS
- [vmware_vm_host_drs_rule module](vmware_vm_host_drs_rule_module.md#ansible-collections-community-vmware-vmware-vm-host-drs-rule-module) – Creates vm/host group in a given cluster
- [vmware_vm_info module](vmware_vm_info_module.md#ansible-collections-community-vmware-vmware-vm-info-module) – Return basic info pertaining to a VMware machine guest
- [vmware_vm_shell module](vmware_vm_shell_module.md#ansible-collections-community-vmware-vmware-vm-shell-module) – Run commands in a VMware guest operating system
- [vmware_vm_storage_policy module](vmware_vm_storage_policy_module.md#ansible-collections-community-vmware-vmware-vm-storage-policy-module) – Create vSphere storage policies
- [vmware_vm_storage_policy_info module](vmware_vm_storage_policy_info_module.md#ansible-collections-community-vmware-vmware-vm-storage-policy-info-module) – Gather information about vSphere storage profile defined storage policy information.
- [vmware_vm_vm_drs_rule module](vmware_vm_vm_drs_rule_module.md#ansible-collections-community-vmware-vmware-vm-vm-drs-rule-module) – Configure VMware DRS Affinity rule for virtual machines in the given cluster
- [vmware_vm_vss_dvs_migrate module](vmware_vm_vss_dvs_migrate_module.md#ansible-collections-community-vmware-vmware-vm-vss-dvs-migrate-module) – Migrates a virtual machine from a standard vswitch to distributed
- [vmware_vmkernel module](vmware_vmkernel_module.md#ansible-collections-community-vmware-vmware-vmkernel-module) – Manages a VMware VMkernel Adapter of an ESXi host.
- [vmware_vmkernel_info module](vmware_vmkernel_info_module.md#ansible-collections-community-vmware-vmware-vmkernel-info-module) – Gathers VMKernel info about an ESXi host
- [vmware_vmotion module](vmware_vmotion_module.md#ansible-collections-community-vmware-vmware-vmotion-module) – Move a virtual machine using vMotion, and/or its vmdks using storage vMotion.
- [vmware_vsan_cluster module](vmware_vsan_cluster_module.md#ansible-collections-community-vmware-vmware-vsan-cluster-module) – Configure VSAN clustering on an ESXi host
- [vmware_vsan_hcl_db module](vmware_vsan_hcl_db_module.md#ansible-collections-community-vmware-vmware-vsan-hcl-db-module) – Manages the vSAN Hardware Compatibility List (HCL) database
- [vmware_vsan_health_info module](vmware_vsan_health_info_module.md#ansible-collections-community-vmware-vmware-vsan-health-info-module) – Gather information about a VMware vSAN cluster’s health
- [vmware_vsan_release_catalog module](vmware_vsan_release_catalog_module.md#ansible-collections-community-vmware-vmware-vsan-release-catalog-module) – Uploads the vSAN Release Catalog
- [vmware_vspan_session module](vmware_vspan_session_module.md#ansible-collections-community-vmware-vmware-vspan-session-module) – Create or remove a Port Mirroring session.
- [vmware_vswitch module](vmware_vswitch_module.md#ansible-collections-community-vmware-vmware-vswitch-module) – Manage a VMware Standard Switch to an ESXi host.
- [vmware_vswitch_info module](vmware_vswitch_info_module.md#ansible-collections-community-vmware-vmware-vswitch-info-module) – Gathers info about an ESXi host’s vswitch configurations
- [vsan_health_silent_checks module](vsan_health_silent_checks_module.md#ansible-collections-community-vmware-vsan-health-silent-checks-module) – Silence vSAN health checks
- [vsphere_copy module](vsphere_copy_module.md#ansible-collections-community-vmware-vsphere-copy-module) – Copy a file to a VMware datastore
- [vsphere_file module](vsphere_file_module.md#ansible-collections-community-vmware-vsphere-file-module) – Manage files on a vCenter datastore

### Connection Plugins

- [vmware_tools connection](vmware_tools_connection.md#ansible-collections-community-vmware-vmware-tools-connection) – Execute tasks inside a VM via VMware Tools

### Httpapi Plugins

- [vmware httpapi](vmware_httpapi.md#ansible-collections-community-vmware-vmware-httpapi) – HttpApi Plugin for VMware REST API

### Inventory Plugins

- [vmware_host_inventory inventory](vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory) – VMware ESXi hostsystem inventory source
- [vmware_vm_inventory inventory](vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory) – VMware Guest inventory source

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

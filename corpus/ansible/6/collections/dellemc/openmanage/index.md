---
collection: ansible
version: "6"
title: "Dellemc.Openmanage"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/index.html
fetched_at: 2026-07-27T16:41:54+00:00
---
# Dellemc.Openmanage

Collection version 5.5.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Dell EMC OpenManage Ansible Modules allows data center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration, deployment, and update of Dell EMC PowerEdge Servers and modular infrastructure by leveraging the management automation capabilities in-built into the Integrated Dell Remote Access Controller (iDRAC), OpenManage Enterprise and OpenManage Enterprise Modular.

**Authors:**

- Rajeev Arakkal <[Rajeev_Arakkal@Dell.com](mailto:Rajeev_Arakkal%40Dell.com)>
- Jagadeesh N V <[Jagadeesh_N_V@Dell.com](mailto:Jagadeesh_N_V%40Dell.com)>
- Felix Stephen <[Felix_S@Dell.com](mailto:Felix_S%40Dell.com)>
- Sachin Apagundi <[Sachin_Apagundi@Dell.com](mailto:Sachin_Apagundi%40Dell.com)>
- Sajna N Shetty <[Sajna_Shetty@Dell.com](mailto:Sajna_Shetty%40Dell.com)>
- Anooja Vardhineni <[Anooja_Vardhineni@Dellteam.com](mailto:Anooja_Vardhineni%40Dellteam.com)>
- Husniya Hameed <[Husniya.Hameed@Dellteam.com](mailto:Husniya.Hameed%40Dellteam.com)>

**Supported ansible-core versions:**

- 2.10.0 or newer

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)

## [Plugin Index](index.md#id2)

These are the plugins in the dellemc.openmanage collection:

### Modules

- [dellemc_configure_idrac_eventing module](dellemc_configure_idrac_eventing_module.md#ansible-collections-dellemc-openmanage-dellemc-configure-idrac-eventing-module) – Configures the iDRAC eventing related attributes
- [dellemc_configure_idrac_services module](dellemc_configure_idrac_services_module.md#ansible-collections-dellemc-openmanage-dellemc-configure-idrac-services-module) – Configures the iDRAC services related attributes
- [dellemc_get_firmware_inventory module](dellemc_get_firmware_inventory_module.md#ansible-collections-dellemc-openmanage-dellemc-get-firmware-inventory-module) – Get Firmware Inventory
- [dellemc_get_system_inventory module](dellemc_get_system_inventory_module.md#ansible-collections-dellemc-openmanage-dellemc-get-system-inventory-module) – Get the PowerEdge Server System Inventory
- [dellemc_idrac_lc_attributes module](dellemc_idrac_lc_attributes_module.md#ansible-collections-dellemc-openmanage-dellemc-idrac-lc-attributes-module) – Enable or disable Collect System Inventory on Restart (CSIOR) property for all iDRAC/LC jobs
- [dellemc_idrac_storage_volume module](dellemc_idrac_storage_volume_module.md#ansible-collections-dellemc-openmanage-dellemc-idrac-storage-volume-module) – Configures the RAID configuration attributes
- [dellemc_system_lockdown_mode module](dellemc_system_lockdown_mode_module.md#ansible-collections-dellemc-openmanage-dellemc-system-lockdown-mode-module) – Configures system lockdown mode for iDRAC
- [idrac_bios module](idrac_bios_module.md#ansible-collections-dellemc-openmanage-idrac-bios-module) – Configure the BIOS attributes
- [idrac_certificates module](idrac_certificates_module.md#ansible-collections-dellemc-openmanage-idrac-certificates-module) – Configure certificates for iDRAC
- [idrac_firmware module](idrac_firmware_module.md#ansible-collections-dellemc-openmanage-idrac-firmware-module) – Firmware update from a repository on a network share (CIFS, NFS, HTTP, HTTPS, FTP)
- [idrac_firmware_info module](idrac_firmware_info_module.md#ansible-collections-dellemc-openmanage-idrac-firmware-info-module) – Get Firmware Inventory
- [idrac_lifecycle_controller_job_status_info module](idrac_lifecycle_controller_job_status_info_module.md#ansible-collections-dellemc-openmanage-idrac-lifecycle-controller-job-status-info-module) – Get the status of a Lifecycle Controller job
- [idrac_lifecycle_controller_jobs module](idrac_lifecycle_controller_jobs_module.md#ansible-collections-dellemc-openmanage-idrac-lifecycle-controller-jobs-module) – Delete the Lifecycle Controller Jobs
- [idrac_lifecycle_controller_logs module](idrac_lifecycle_controller_logs_module.md#ansible-collections-dellemc-openmanage-idrac-lifecycle-controller-logs-module) – Export Lifecycle Controller logs to a network share or local path.
- [idrac_lifecycle_controller_status_info module](idrac_lifecycle_controller_status_info_module.md#ansible-collections-dellemc-openmanage-idrac-lifecycle-controller-status-info-module) – Get the status of the Lifecycle Controller
- [idrac_network module](idrac_network_module.md#ansible-collections-dellemc-openmanage-idrac-network-module) – Configures the iDRAC network attributes
- [idrac_os_deployment module](idrac_os_deployment_module.md#ansible-collections-dellemc-openmanage-idrac-os-deployment-module) – Boot to a network ISO image
- [idrac_redfish_storage_controller module](idrac_redfish_storage_controller_module.md#ansible-collections-dellemc-openmanage-idrac-redfish-storage-controller-module) – Configures the physical disk, virtual disk, and storage controller settings
- [idrac_reset module](idrac_reset_module.md#ansible-collections-dellemc-openmanage-idrac-reset-module) – Reset iDRAC
- [idrac_server_config_profile module](idrac_server_config_profile_module.md#ansible-collections-dellemc-openmanage-idrac-server-config-profile-module) – Export or Import iDRAC Server Configuration Profile (SCP)
- [idrac_syslog module](idrac_syslog_module.md#ansible-collections-dellemc-openmanage-idrac-syslog-module) – Enable or disable the syslog on iDRAC
- [idrac_system_info module](idrac_system_info_module.md#ansible-collections-dellemc-openmanage-idrac-system-info-module) – Get the PowerEdge Server System Inventory
- [idrac_timezone_ntp module](idrac_timezone_ntp_module.md#ansible-collections-dellemc-openmanage-idrac-timezone-ntp-module) – Configures time zone and NTP on iDRAC
- [idrac_user module](idrac_user_module.md#ansible-collections-dellemc-openmanage-idrac-user-module) – Configure settings for user accounts
- [ome_active_directory module](ome_active_directory_module.md#ansible-collections-dellemc-openmanage-ome-active-directory-module) – Configure Active Directory groups to be used with Directory Services on OpenManage Enterprise and OpenManage Enterprise Modular
- [ome_application_alerts_smtp module](ome_application_alerts_smtp_module.md#ansible-collections-dellemc-openmanage-ome-application-alerts-smtp-module) – This module allows to configure SMTP or email configurations
- [ome_application_alerts_syslog module](ome_application_alerts_syslog_module.md#ansible-collections-dellemc-openmanage-ome-application-alerts-syslog-module) – Configure syslog forwarding settings on OpenManage Enterprise and OpenManage Enterprise Modular
- [ome_application_certificate module](ome_application_certificate_module.md#ansible-collections-dellemc-openmanage-ome-application-certificate-module) – This module allows to generate a CSR and upload the certificate
- [ome_application_console_preferences module](ome_application_console_preferences_module.md#ansible-collections-dellemc-openmanage-ome-application-console-preferences-module) – Configure console preferences on OpenManage Enterprise.
- [ome_application_network_address module](ome_application_network_address_module.md#ansible-collections-dellemc-openmanage-ome-application-network-address-module) – Updates the network configuration on OpenManage Enterprise
- [ome_application_network_proxy module](ome_application_network_proxy_module.md#ansible-collections-dellemc-openmanage-ome-application-network-proxy-module) – Updates the proxy configuration on OpenManage Enterprise
- [ome_application_network_settings module](ome_application_network_settings_module.md#ansible-collections-dellemc-openmanage-ome-application-network-settings-module) – This module allows you to configure the session inactivity timeout settings
- [ome_application_network_time module](ome_application_network_time_module.md#ansible-collections-dellemc-openmanage-ome-application-network-time-module) – Updates the network time on OpenManage Enterprise
- [ome_application_network_webserver module](ome_application_network_webserver_module.md#ansible-collections-dellemc-openmanage-ome-application-network-webserver-module) – Updates the Web server configuration on OpenManage Enterprise
- [ome_application_security_settings module](ome_application_security_settings_module.md#ansible-collections-dellemc-openmanage-ome-application-security-settings-module) – Configure the login security properties
- [ome_chassis_slots module](ome_chassis_slots_module.md#ansible-collections-dellemc-openmanage-ome-chassis-slots-module) – Rename sled slots on OpenManage Enterprise Modular
- [ome_configuration_compliance_baseline module](ome_configuration_compliance_baseline_module.md#ansible-collections-dellemc-openmanage-ome-configuration-compliance-baseline-module) – Create, modify, and delete a configuration compliance baseline and remediate non-compliant devices on OpenManage Enterprise
- [ome_configuration_compliance_info module](ome_configuration_compliance_info_module.md#ansible-collections-dellemc-openmanage-ome-configuration-compliance-info-module) – Device compliance report for devices managed in OpenManage Enterprise
- [ome_device_group module](ome_device_group_module.md#ansible-collections-dellemc-openmanage-ome-device-group-module) – Add devices to a static device group on OpenManage Enterprise
- [ome_device_info module](ome_device_info_module.md#ansible-collections-dellemc-openmanage-ome-device-info-module) – Retrieves the information of devices inventoried by OpenManage Enterprise
- [ome_device_local_access_configuration module](ome_device_local_access_configuration_module.md#ansible-collections-dellemc-openmanage-ome-device-local-access-configuration-module) – Configure local access settings on OpenManage Enterprise Modular.
- [ome_device_location module](ome_device_location_module.md#ansible-collections-dellemc-openmanage-ome-device-location-module) – Configure device location settings on OpenManage Enterprise Modular
- [ome_device_mgmt_network module](ome_device_mgmt_network_module.md#ansible-collections-dellemc-openmanage-ome-device-mgmt-network-module) – Configure network settings of devices on OpenManage Enterprise Modular
- [ome_device_network_services module](ome_device_network_services_module.md#ansible-collections-dellemc-openmanage-ome-device-network-services-module) – Configure chassis network services settings on OpenManage Enterprise Modular
- [ome_device_power_settings module](ome_device_power_settings_module.md#ansible-collections-dellemc-openmanage-ome-device-power-settings-module) – Configure chassis power settings on OpenManage Enterprise Modular
- [ome_device_quick_deploy module](ome_device_quick_deploy_module.md#ansible-collections-dellemc-openmanage-ome-device-quick-deploy-module) – Configure Quick Deploy settings on OpenManage Enterprise Modular.
- [ome_diagnostics module](ome_diagnostics_module.md#ansible-collections-dellemc-openmanage-ome-diagnostics-module) – Export technical support logs(TSR) to network share location
- [ome_discovery module](ome_discovery_module.md#ansible-collections-dellemc-openmanage-ome-discovery-module) – Create, modify, or delete a discovery job on OpenManage Enterprise
- [ome_domain_user_groups module](ome_domain_user_groups_module.md#ansible-collections-dellemc-openmanage-ome-domain-user-groups-module) – Create, modify, or delete an Active Directory user group on OpenManage Enterprise and OpenManage Enterprise Modular
- [ome_firmware module](ome_firmware_module.md#ansible-collections-dellemc-openmanage-ome-firmware-module) – Update firmware on PowerEdge devices and its components through OpenManage Enterprise
- [ome_firmware_baseline module](ome_firmware_baseline_module.md#ansible-collections-dellemc-openmanage-ome-firmware-baseline-module) – Create, modify, or delete a firmware baseline on OpenManage Enterprise or OpenManage Enterprise Modular
- [ome_firmware_baseline_compliance_info module](ome_firmware_baseline_compliance_info_module.md#ansible-collections-dellemc-openmanage-ome-firmware-baseline-compliance-info-module) – Retrieves baseline compliance details on OpenManage Enterprise
- [ome_firmware_baseline_info module](ome_firmware_baseline_info_module.md#ansible-collections-dellemc-openmanage-ome-firmware-baseline-info-module) – Retrieves baseline details from OpenManage Enterprise
- [ome_firmware_catalog module](ome_firmware_catalog_module.md#ansible-collections-dellemc-openmanage-ome-firmware-catalog-module) – Create, modify, or delete a firmware catalog on OpenManage Enterprise or OpenManage Enterprise Modular
- [ome_groups module](ome_groups_module.md#ansible-collections-dellemc-openmanage-ome-groups-module) – Manages static device groups on OpenManage Enterprise
- [ome_identity_pool module](ome_identity_pool_module.md#ansible-collections-dellemc-openmanage-ome-identity-pool-module) – Manages identity pool settings on OpenManage Enterprise
- [ome_job_info module](ome_job_info_module.md#ansible-collections-dellemc-openmanage-ome-job-info-module) – Get job details for a given job ID or an entire job queue on OpenMange Enterprise
- [ome_network_port_breakout module](ome_network_port_breakout_module.md#ansible-collections-dellemc-openmanage-ome-network-port-breakout-module) – This module allows to automate the port portioning or port breakout to logical sub ports
- [ome_network_vlan module](ome_network_vlan_module.md#ansible-collections-dellemc-openmanage-ome-network-vlan-module) – Create, modify & delete a VLAN
- [ome_network_vlan_info module](ome_network_vlan_info_module.md#ansible-collections-dellemc-openmanage-ome-network-vlan-info-module) – Retrieves the information about networks VLAN(s) present in OpenManage Enterprise
- [ome_powerstate module](ome_powerstate_module.md#ansible-collections-dellemc-openmanage-ome-powerstate-module) – Performs the power management operations on OpenManage Enterprise
- [ome_profile module](ome_profile_module.md#ansible-collections-dellemc-openmanage-ome-profile-module) – Create, modify, delete, assign, unassign and migrate a profile on OpenManage Enterprise
- [ome_server_interface_profile_info module](ome_server_interface_profile_info_module.md#ansible-collections-dellemc-openmanage-ome-server-interface-profile-info-module) – Retrieves the information of server interface profile on OpenManage Enterprise Modular.
- [ome_server_interface_profiles module](ome_server_interface_profiles_module.md#ansible-collections-dellemc-openmanage-ome-server-interface-profiles-module) – Configure server interface profiles
- [ome_smart_fabric module](ome_smart_fabric_module.md#ansible-collections-dellemc-openmanage-ome-smart-fabric-module) – Create, modify or delete a fabric on OpenManage Enterprise Modular
- [ome_smart_fabric_uplink module](ome_smart_fabric_uplink_module.md#ansible-collections-dellemc-openmanage-ome-smart-fabric-uplink-module) – Create, modify or delete a uplink for a fabric on OpenManage Enterprise Modular
- [ome_template module](ome_template_module.md#ansible-collections-dellemc-openmanage-ome-template-module) – Create, modify, deploy, delete, export, import and clone a template on OpenManage Enterprise
- [ome_template_identity_pool module](ome_template_identity_pool_module.md#ansible-collections-dellemc-openmanage-ome-template-identity-pool-module) – Attach or detach an identity pool to a requested template on OpenManage Enterprise
- [ome_template_info module](ome_template_info_module.md#ansible-collections-dellemc-openmanage-ome-template-info-module) – Retrieves template details from OpenManage Enterprise
- [ome_template_network_vlan module](ome_template_network_vlan_module.md#ansible-collections-dellemc-openmanage-ome-template-network-vlan-module) – Set tagged and untagged vlans to native network card supported by a template on OpenManage Enterprise
- [ome_user module](ome_user_module.md#ansible-collections-dellemc-openmanage-ome-user-module) – Create, modify or delete a user on OpenManage Enterprise
- [ome_user_info module](ome_user_info_module.md#ansible-collections-dellemc-openmanage-ome-user-info-module) – Retrieves details of all accounts or a specific account on OpenManage Enterprise
- [redfish_event_subscription module](redfish_event_subscription_module.md#ansible-collections-dellemc-openmanage-redfish-event-subscription-module) – Manage Redfish Subscriptions
- [redfish_firmware module](redfish_firmware_module.md#ansible-collections-dellemc-openmanage-redfish-firmware-module) – To perform a component firmware update using the image file available on the local or remote system
- [redfish_powerstate module](redfish_powerstate_module.md#ansible-collections-dellemc-openmanage-redfish-powerstate-module) – Manage device power state
- [redfish_storage_volume module](redfish_storage_volume_module.md#ansible-collections-dellemc-openmanage-redfish-storage-volume-module) – Manages the storage volume configuration

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

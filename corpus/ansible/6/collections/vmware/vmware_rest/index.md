---
collection: ansible
version: "6"
title: "Vmware.Vmware_Rest"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/index.html
fetched_at: 2026-07-27T16:42:11+00:00
---
# Vmware.Vmware_Rest

Collection version 2.2.0

- [Description](index.md#description)
- [Scenario Guide](index.md#scenario-guide)
- [Developer Guide](index.md#developer-guide)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

**Author:**

- Ansible (<https://github.com/ansible>)

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)

## [Scenario Guide](index.md#id2)

- [VMware Guide (REST)](docsite/guide_vmware_rest.md)

## [Developer Guide](index.md#id3)

- [Guidelines for VMware REST module development](docsite/dev_guide.md)

## [Plugin Index](index.md#id4)

These are the plugins in the vmware.vmware_rest collection:

### Modules

- [appliance_access_consolecli module](appliance_access_consolecli_module.md#ansible-collections-vmware-vmware-rest-appliance-access-consolecli-module) – Set enabled state of the console-based controlled CLI (TTY1).
- [appliance_access_consolecli_info module](appliance_access_consolecli_info_module.md#ansible-collections-vmware-vmware-rest-appliance-access-consolecli-info-module) – Get enabled state of the console-based controlled CLI (TTY1).
- [appliance_access_dcui module](appliance_access_dcui_module.md#ansible-collections-vmware-vmware-rest-appliance-access-dcui-module) – Set enabled state of Direct Console User Interface (DCUI TTY2).
- [appliance_access_dcui_info module](appliance_access_dcui_info_module.md#ansible-collections-vmware-vmware-rest-appliance-access-dcui-info-module) – Get enabled state of Direct Console User Interface (DCUI TTY2).
- [appliance_access_shell module](appliance_access_shell_module.md#ansible-collections-vmware-vmware-rest-appliance-access-shell-module) – Set enabled state of BASH, that is, access to BASH from within the controlled CLI.
- [appliance_access_shell_info module](appliance_access_shell_info_module.md#ansible-collections-vmware-vmware-rest-appliance-access-shell-info-module) – Get enabled state of BASH, that is, access to BASH from within the controlled CLI.
- [appliance_access_ssh module](appliance_access_ssh_module.md#ansible-collections-vmware-vmware-rest-appliance-access-ssh-module) – Set enabled state of the SSH-based controlled CLI.
- [appliance_access_ssh_info module](appliance_access_ssh_info_module.md#ansible-collections-vmware-vmware-rest-appliance-access-ssh-info-module) – Get enabled state of the SSH-based controlled CLI.
- [appliance_health_applmgmt_info module](appliance_health_applmgmt_info_module.md#ansible-collections-vmware-vmware-rest-appliance-health-applmgmt-info-module) – Get health status of applmgmt services.
- [appliance_health_database_info module](appliance_health_database_info_module.md#ansible-collections-vmware-vmware-rest-appliance-health-database-info-module) – Returns the health status of the database.
- [appliance_health_databasestorage_info module](appliance_health_databasestorage_info_module.md#ansible-collections-vmware-vmware-rest-appliance-health-databasestorage-info-module) – Get database storage health.
- [appliance_health_load_info module](appliance_health_load_info_module.md#ansible-collections-vmware-vmware-rest-appliance-health-load-info-module) – Get load health.
- [appliance_health_mem_info module](appliance_health_mem_info_module.md#ansible-collections-vmware-vmware-rest-appliance-health-mem-info-module) – Get memory health.
- [appliance_health_softwarepackages_info module](appliance_health_softwarepackages_info_module.md#ansible-collections-vmware-vmware-rest-appliance-health-softwarepackages-info-module) – Get information on available software updates available in the remote vSphere Update Manager repository
- [appliance_health_storage_info module](appliance_health_storage_info_module.md#ansible-collections-vmware-vmware-rest-appliance-health-storage-info-module) – Get storage health.
- [appliance_health_swap_info module](appliance_health_swap_info_module.md#ansible-collections-vmware-vmware-rest-appliance-health-swap-info-module) – Get swap health.
- [appliance_health_system_info module](appliance_health_system_info_module.md#ansible-collections-vmware-vmware-rest-appliance-health-system-info-module) – Get overall health of system.
- [appliance_infraprofile_configs module](appliance_infraprofile_configs_module.md#ansible-collections-vmware-vmware-rest-appliance-infraprofile-configs-module) – Exports the desired profile specification.
- [appliance_infraprofile_configs_info module](appliance_infraprofile_configs_info_module.md#ansible-collections-vmware-vmware-rest-appliance-infraprofile-configs-info-module) – List all the profiles which are registered.
- [appliance_localaccounts_globalpolicy module](appliance_localaccounts_globalpolicy_module.md#ansible-collections-vmware-vmware-rest-appliance-localaccounts-globalpolicy-module) – Set the global password policy.
- [appliance_localaccounts_globalpolicy_info module](appliance_localaccounts_globalpolicy_info_module.md#ansible-collections-vmware-vmware-rest-appliance-localaccounts-globalpolicy-info-module) – Get the global password policy.
- [appliance_localaccounts_info module](appliance_localaccounts_info_module.md#ansible-collections-vmware-vmware-rest-appliance-localaccounts-info-module) – Get the local user account information.
- [appliance_monitoring_info module](appliance_monitoring_info_module.md#ansible-collections-vmware-vmware-rest-appliance-monitoring-info-module) – Get monitored item info
- [appliance_monitoring_query module](appliance_monitoring_query_module.md#ansible-collections-vmware-vmware-rest-appliance-monitoring-query-module) – Get monitoring data.
- [appliance_networking module](appliance_networking_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-module) – Reset and restarts network configuration on all interfaces, also this will renew the DHCP lease for DHCP IP address.
- [appliance_networking_dns_domains module](appliance_networking_dns_domains_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-dns-domains-module) – Set DNS search domains.
- [appliance_networking_dns_domains_info module](appliance_networking_dns_domains_info_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-dns-domains-info-module) – Get list of DNS search domains.
- [appliance_networking_dns_hostname module](appliance_networking_dns_hostname_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-dns-hostname-module) – Set the Fully Qualified Domain Name.
- [appliance_networking_dns_hostname_info module](appliance_networking_dns_hostname_info_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-dns-hostname-info-module) – Get the Fully Qualified Doman Name.
- [appliance_networking_dns_servers module](appliance_networking_dns_servers_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-dns-servers-module) – Set the DNS server configuration
- [appliance_networking_dns_servers_info module](appliance_networking_dns_servers_info_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-dns-servers-info-module) – Get DNS server configuration.
- [appliance_networking_firewall_inbound module](appliance_networking_firewall_inbound_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-firewall-inbound-module) – Set the ordered list of firewall rules to allow or deny traffic from one or more incoming IP addresses
- [appliance_networking_firewall_inbound_info module](appliance_networking_firewall_inbound_info_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-firewall-inbound-info-module) – Get the ordered list of firewall rules
- [appliance_networking_info module](appliance_networking_info_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-info-module) – Get Networking information for all configured interfaces.
- [appliance_networking_interfaces_info module](appliance_networking_interfaces_info_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-interfaces-info-module) – Get information about a particular network interface.
- [appliance_networking_interfaces_ipv4 module](appliance_networking_interfaces_ipv4_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-interfaces-ipv4-module) – Set IPv4 network configuration for specific network interface.
- [appliance_networking_interfaces_ipv4_info module](appliance_networking_interfaces_ipv4_info_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-interfaces-ipv4-info-module) – Get IPv4 network configuration for specific NIC.
- [appliance_networking_interfaces_ipv6 module](appliance_networking_interfaces_ipv6_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-interfaces-ipv6-module) – Set IPv6 network configuration for specific interface.
- [appliance_networking_interfaces_ipv6_info module](appliance_networking_interfaces_ipv6_info_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-interfaces-ipv6-info-module) – Get IPv6 network configuration for specific interface.
- [appliance_networking_noproxy module](appliance_networking_noproxy_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-noproxy-module) – Sets servers for which no proxy configuration should be applied
- [appliance_networking_noproxy_info module](appliance_networking_noproxy_info_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-noproxy-info-module) – Returns servers for which no proxy configuration will be applied.
- [appliance_networking_proxy module](appliance_networking_proxy_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-proxy-module) – Configures which proxy server to use for the specified protocol
- [appliance_networking_proxy_info module](appliance_networking_proxy_info_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-proxy-info-module) – Gets the proxy configuration for a specific protocol.
- [appliance_ntp module](appliance_ntp_module.md#ansible-collections-vmware-vmware-rest-appliance-ntp-module) – Set NTP servers
- [appliance_ntp_info module](appliance_ntp_info_module.md#ansible-collections-vmware-vmware-rest-appliance-ntp-info-module) – Get the NTP configuration status
- [appliance_services module](appliance_services_module.md#ansible-collections-vmware-vmware-rest-appliance-services-module) – Restarts a service
- [appliance_services_info module](appliance_services_info_module.md#ansible-collections-vmware-vmware-rest-appliance-services-info-module) – Returns the state of a service.
- [appliance_shutdown module](appliance_shutdown_module.md#ansible-collections-vmware-vmware-rest-appliance-shutdown-module) – Cancel pending shutdown action.
- [appliance_shutdown_info module](appliance_shutdown_info_module.md#ansible-collections-vmware-vmware-rest-appliance-shutdown-info-module) – Get details about the pending shutdown action.
- [appliance_system_globalfips module](appliance_system_globalfips_module.md#ansible-collections-vmware-vmware-rest-appliance-system-globalfips-module) – Enable/Disable Global FIPS mode for the appliance
- [appliance_system_globalfips_info module](appliance_system_globalfips_info_module.md#ansible-collections-vmware-vmware-rest-appliance-system-globalfips-info-module) – Get current appliance FIPS settings.
- [appliance_system_storage module](appliance_system_storage_module.md#ansible-collections-vmware-vmware-rest-appliance-system-storage-module) – Resize all partitions to 100 percent of disk size.
- [appliance_system_storage_info module](appliance_system_storage_info_module.md#ansible-collections-vmware-vmware-rest-appliance-system-storage-info-module) – Get disk to partition mapping.
- [appliance_system_time_info module](appliance_system_time_info_module.md#ansible-collections-vmware-vmware-rest-appliance-system-time-info-module) – Get system time.
- [appliance_system_time_timezone module](appliance_system_time_timezone_module.md#ansible-collections-vmware-vmware-rest-appliance-system-time-timezone-module) – Set time zone.
- [appliance_system_time_timezone_info module](appliance_system_time_timezone_info_module.md#ansible-collections-vmware-vmware-rest-appliance-system-time-timezone-info-module) – Get time zone.
- [appliance_system_version_info module](appliance_system_version_info_module.md#ansible-collections-vmware-vmware-rest-appliance-system-version-info-module) – Get the version.
- [appliance_timesync module](appliance_timesync_module.md#ansible-collections-vmware-vmware-rest-appliance-timesync-module) – Set time synchronization mode.
- [appliance_timesync_info module](appliance_timesync_info_module.md#ansible-collections-vmware-vmware-rest-appliance-timesync-info-module) – Get time synchronization mode.
- [appliance_update_info module](appliance_update_info_module.md#ansible-collections-vmware-vmware-rest-appliance-update-info-module) – Gets the current status of the appliance update.
- [appliance_vmon_service module](appliance_vmon_service_module.md#ansible-collections-vmware-vmware-rest-appliance-vmon-service-module) – Lists details of services managed by vMon.
- [appliance_vmon_service_info module](appliance_vmon_service_info_module.md#ansible-collections-vmware-vmware-rest-appliance-vmon-service-info-module) – Returns the state of a service.
- [content_configuration module](content_configuration_module.md#ansible-collections-vmware-vmware-rest-content-configuration-module) – Updates the configuration
- [content_configuration_info module](content_configuration_info_module.md#ansible-collections-vmware-vmware-rest-content-configuration-info-module) – Retrieves the current configuration values.
- [content_library_item_info module](content_library_item_info_module.md#ansible-collections-vmware-vmware-rest-content-library-item-info-module) – Returns the [{@link](mailto:{%40link) ItemModel} with the given identifier.
- [content_locallibrary module](content_locallibrary_module.md#ansible-collections-vmware-vmware-rest-content-locallibrary-module) – Creates a new local library.
- [content_locallibrary_info module](content_locallibrary_info_module.md#ansible-collections-vmware-vmware-rest-content-locallibrary-info-module) – Returns a given local library.
- [content_subscribedlibrary module](content_subscribedlibrary_module.md#ansible-collections-vmware-vmware-rest-content-subscribedlibrary-module) – Creates a new subscribed library
- [content_subscribedlibrary_info module](content_subscribedlibrary_info_module.md#ansible-collections-vmware-vmware-rest-content-subscribedlibrary-info-module) – Returns a given subscribed library.
- [vcenter_cluster_info module](vcenter_cluster_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-cluster-info-module) – Retrieves information about the cluster corresponding to [{@param.name](mailto:{%40param.name) cluster}.
- [vcenter_datacenter module](vcenter_datacenter_module.md#ansible-collections-vmware-vmware-rest-vcenter-datacenter-module) – Create a new datacenter in the vCenter inventory
- [vcenter_datacenter_info module](vcenter_datacenter_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-datacenter-info-module) – Retrieves information about the datacenter corresponding to [{@param.name](mailto:{%40param.name) datacenter}.
- [vcenter_datastore_info module](vcenter_datastore_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-datastore-info-module) – Retrieves information about the datastore indicated by [{@param.name](mailto:{%40param.name) datastore}.
- [vcenter_folder_info module](vcenter_folder_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-folder-info-module) – Returns information about at most 1000 visible (subject to permission checks) folders in vCenter matching the [{@link](mailto:{%40link) FilterSpec}.
- [vcenter_host module](vcenter_host_module.md#ansible-collections-vmware-vmware-rest-vcenter-host-module) – Add a new standalone host in the vCenter inventory
- [vcenter_host_info module](vcenter_host_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-host-info-module) – Returns information about at most 2500 visible (subject to permission checks) hosts in vCenter matching the [{@link](mailto:{%40link) FilterSpec}.
- [vcenter_network_info module](vcenter_network_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-network-info-module) – Returns information about at most 1000 visible (subject to permission checks) networks in vCenter matching the [{@link](mailto:{%40link) FilterSpec}.
- [vcenter_ovf_libraryitem module](vcenter_ovf_libraryitem_module.md#ansible-collections-vmware-vmware-rest-vcenter-ovf-libraryitem-module) – Creates a library item in content library from a virtual machine or virtual appliance
- [vcenter_resourcepool module](vcenter_resourcepool_module.md#ansible-collections-vmware-vmware-rest-vcenter-resourcepool-module) – Creates a resource pool.
- [vcenter_resourcepool_info module](vcenter_resourcepool_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-resourcepool-info-module) – Retrieves information about the resource pool indicated by [{@param.name](mailto:{%40param.name) resourcePool}.
- [vcenter_storage_policies_info module](vcenter_storage_policies_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-storage-policies-info-module) – Returns information about at most 1024 visible (subject to permission checks) storage solicies availabe in vCenter
- [vcenter_vm module](vcenter_vm_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-module) – Creates a virtual machine.
- [vcenter_vm_guest_customization module](vcenter_vm_guest_customization_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-customization-module) – Applies a customization specification on the virtual machine
- [vcenter_vm_guest_filesystem_directories module](vcenter_vm_guest_filesystem_directories_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-filesystem-directories-module) – Creates a directory in the guest operating system
- [vcenter_vm_guest_identity_info module](vcenter_vm_guest_identity_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-identity-info-module) – Return information about the guest.
- [vcenter_vm_guest_localfilesystem_info module](vcenter_vm_guest_localfilesystem_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-localfilesystem-info-module) – Returns details of the local file systems in the guest operating system.
- [vcenter_vm_guest_networking_info module](vcenter_vm_guest_networking_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-networking-info-module) – Returns information about the network configuration in the guest operating system.
- [vcenter_vm_guest_networking_interfaces_info module](vcenter_vm_guest_networking_interfaces_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-networking-interfaces-info-module) – Returns information about the networking interfaces in the guest operating system.
- [vcenter_vm_guest_networking_routes_info module](vcenter_vm_guest_networking_routes_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-networking-routes-info-module) – Returns information about network routing in the guest operating system.
- [vcenter_vm_guest_operations_info module](vcenter_vm_guest_operations_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-operations-info-module) – Get information about the guest operation status.
- [vcenter_vm_guest_power module](vcenter_vm_guest_power_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-power-module) – Issues a request to the guest operating system asking it to perform a soft shutdown, standby (suspend) or soft reboot
- [vcenter_vm_guest_power_info module](vcenter_vm_guest_power_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-power-info-module) – Returns information about the guest operating system power state.
- [vcenter_vm_hardware module](vcenter_vm_hardware_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-module) – Updates the virtual hardware settings of a virtual machine.
- [vcenter_vm_hardware_adapter_sata module](vcenter_vm_hardware_adapter_sata_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-adapter-sata-module) – Adds a virtual SATA adapter to the virtual machine.
- [vcenter_vm_hardware_adapter_sata_info module](vcenter_vm_hardware_adapter_sata_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-adapter-sata-info-module) – Returns information about a virtual SATA adapter.
- [vcenter_vm_hardware_adapter_scsi module](vcenter_vm_hardware_adapter_scsi_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-adapter-scsi-module) – Adds a virtual SCSI adapter to the virtual machine.
- [vcenter_vm_hardware_adapter_scsi_info module](vcenter_vm_hardware_adapter_scsi_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-adapter-scsi-info-module) – Returns information about a virtual SCSI adapter.
- [vcenter_vm_hardware_boot module](vcenter_vm_hardware_boot_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-boot-module) – Updates the boot-related settings of a virtual machine.
- [vcenter_vm_hardware_boot_device module](vcenter_vm_hardware_boot_device_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-boot-device-module) – Sets the virtual devices that will be used to boot the virtual machine
- [vcenter_vm_hardware_boot_device_info module](vcenter_vm_hardware_boot_device_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-boot-device-info-module) – Returns an ordered list of boot devices for the virtual machine
- [vcenter_vm_hardware_boot_info module](vcenter_vm_hardware_boot_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-boot-info-module) – Returns the boot-related settings of a virtual machine.
- [vcenter_vm_hardware_cdrom module](vcenter_vm_hardware_cdrom_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-cdrom-module) – Adds a virtual CD-ROM device to the virtual machine.
- [vcenter_vm_hardware_cdrom_info module](vcenter_vm_hardware_cdrom_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-cdrom-info-module) – Returns information about a virtual CD-ROM device.
- [vcenter_vm_hardware_cpu module](vcenter_vm_hardware_cpu_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-cpu-module) – Updates the CPU-related settings of a virtual machine.
- [vcenter_vm_hardware_cpu_info module](vcenter_vm_hardware_cpu_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-cpu-info-module) – Returns the CPU-related settings of a virtual machine.
- [vcenter_vm_hardware_disk module](vcenter_vm_hardware_disk_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-disk-module) – Adds a virtual disk to the virtual machine
- [vcenter_vm_hardware_disk_info module](vcenter_vm_hardware_disk_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-disk-info-module) – Returns information about a virtual disk.
- [vcenter_vm_hardware_ethernet module](vcenter_vm_hardware_ethernet_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-ethernet-module) – Adds a virtual Ethernet adapter to the virtual machine.
- [vcenter_vm_hardware_ethernet_info module](vcenter_vm_hardware_ethernet_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-ethernet-info-module) – Returns information about a virtual Ethernet adapter.
- [vcenter_vm_hardware_floppy module](vcenter_vm_hardware_floppy_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-floppy-module) – Adds a virtual floppy drive to the virtual machine.
- [vcenter_vm_hardware_floppy_info module](vcenter_vm_hardware_floppy_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-floppy-info-module) – Returns information about a virtual floppy drive.
- [vcenter_vm_hardware_info module](vcenter_vm_hardware_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-info-module) – Returns the virtual hardware settings of a virtual machine.
- [vcenter_vm_hardware_memory module](vcenter_vm_hardware_memory_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-memory-module) – Updates the memory-related settings of a virtual machine.
- [vcenter_vm_hardware_memory_info module](vcenter_vm_hardware_memory_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-memory-info-module) – Returns the memory-related settings of a virtual machine.
- [vcenter_vm_hardware_parallel module](vcenter_vm_hardware_parallel_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-parallel-module) – Adds a virtual parallel port to the virtual machine.
- [vcenter_vm_hardware_parallel_info module](vcenter_vm_hardware_parallel_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-parallel-info-module) – Returns information about a virtual parallel port.
- [vcenter_vm_hardware_serial module](vcenter_vm_hardware_serial_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-serial-module) – Adds a virtual serial port to the virtual machine.
- [vcenter_vm_hardware_serial_info module](vcenter_vm_hardware_serial_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-serial-info-module) – Returns information about a virtual serial port.
- [vcenter_vm_info module](vcenter_vm_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-info-module) – Returns information about a virtual machine.
- [vcenter_vm_libraryitem_info module](vcenter_vm_libraryitem_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-libraryitem-info-module) – Returns the information about the library item associated with the virtual machine.
- [vcenter_vm_power module](vcenter_vm_power_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-power-module) – Operate a boot, hard shutdown, hard reset or hard suspend on a guest.
- [vcenter_vm_power_info module](vcenter_vm_power_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-power-info-module) – Returns the power state information of a virtual machine.
- [vcenter_vm_storage_policy module](vcenter_vm_storage_policy_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-storage-policy-module) – Updates the storage policy configuration of a virtual machine and/or its associated virtual hard disks.
- [vcenter_vm_storage_policy_compliance module](vcenter_vm_storage_policy_compliance_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-storage-policy-compliance-module) – Returns the storage policy Compliance [{@link](mailto:{%40link) Info} of a virtual machine after explicitly re-computing compliance check.
- [vcenter_vm_storage_policy_compliance_info module](vcenter_vm_storage_policy_compliance_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-storage-policy-compliance-info-module) – Returns the cached storage policy compliance information of a virtual machine.
- [vcenter_vm_storage_policy_info module](vcenter_vm_storage_policy_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-storage-policy-info-module) – Returns Information about Storage Policy associated with a virtual machine’s home directory and/or its virtual hard disks.
- [vcenter_vm_tools module](vcenter_vm_tools_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-tools-module) – Update the properties of VMware Tools.
- [vcenter_vm_tools_info module](vcenter_vm_tools_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-tools-info-module) – Get the properties of VMware Tools.
- [vcenter_vm_tools_installer module](vcenter_vm_tools_installer_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-tools-installer-module) – Connects the VMware Tools CD installer as a CD-ROM for the guest operating system
- [vcenter_vm_tools_installer_info module](vcenter_vm_tools_installer_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-tools-installer-info-module) – Get information about the VMware Tools installer.
- [vcenter_vmtemplate_libraryitems module](vcenter_vmtemplate_libraryitems_module.md#ansible-collections-vmware-vmware-rest-vcenter-vmtemplate-libraryitems-module) – Creates a library item in content library from a virtual machine
- [vcenter_vmtemplate_libraryitems_info module](vcenter_vmtemplate_libraryitems_info_module.md#ansible-collections-vmware-vmware-rest-vcenter-vmtemplate-libraryitems-info-module) – Returns information about a virtual machine template contained in the library item specified by [{@param.name](mailto:{%40param.name) templateLibraryItem}

### Lookup Plugins

- [cluster_moid lookup](cluster_moid_lookup.md#ansible-collections-vmware-vmware-rest-cluster-moid-lookup) – Look up MoID for vSphere cluster objects using vCenter REST API
- [datacenter_moid lookup](datacenter_moid_lookup.md#ansible-collections-vmware-vmware-rest-datacenter-moid-lookup) – Look up MoID for vSphere datacenter objects using vCenter REST API
- [datastore_moid lookup](datastore_moid_lookup.md#ansible-collections-vmware-vmware-rest-datastore-moid-lookup) – Look up MoID for vSphere datastore objects using vCenter REST API
- [folder_moid lookup](folder_moid_lookup.md#ansible-collections-vmware-vmware-rest-folder-moid-lookup) – Look up MoID for vSphere folder objects using vCenter REST API
- [host_moid lookup](host_moid_lookup.md#ansible-collections-vmware-vmware-rest-host-moid-lookup) – Look up MoID for vSphere host objects using vCenter REST API
- [network_moid lookup](network_moid_lookup.md#ansible-collections-vmware-vmware-rest-network-moid-lookup) – Look up MoID for vSphere network objects using vCenter REST API
- [resource_pool_moid lookup](resource_pool_moid_lookup.md#ansible-collections-vmware-vmware-rest-resource-pool-moid-lookup) – Look up MoID for vSphere resource pool objects using vCenter REST API
- [vm_moid lookup](vm_moid_lookup.md#ansible-collections-vmware-vmware-rest-vm-moid-lookup) – Look up MoID for vSphere vm objects using vCenter REST API

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

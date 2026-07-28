---
collection: ansible
version: "6"
title: "Wti.Remote"
source_url: https://docs.ansible.com/projects/ansible/6/collections/wti/remote/index.html
fetched_at: 2026-07-27T16:42:12+00:00
---
# Wti.Remote

Collection version 1.0.4

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Modules for interacting with WTI remote OOB and PDU devices

**Author:**

- Ken Partridge <[kenp@wti.com](mailto:kenp%40wti.com)> (@wtinetworkgear)

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
[Homepage](https://www.wti.com)
[Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)

## [Plugin Index](index.md#id2)

These are the plugins in the wti.remote collection:

### Modules

- [cpm_alarm_info module](cpm_alarm_info_module.md#ansible-collections-wti-remote-cpm-alarm-info-module) – Get alarm information from WTI OOB and PDU devices
- [cpm_config_backup module](cpm_config_backup_module.md#ansible-collections-wti-remote-cpm-config-backup-module) – Get parameters from WTI OOB and PDU devices
- [cpm_config_restore module](cpm_config_restore_module.md#ansible-collections-wti-remote-cpm-config-restore-module) – Send operational parameters to WTI OOB and PDU devices
- [cpm_current_info module](cpm_current_info_module.md#ansible-collections-wti-remote-cpm-current-info-module) – Get the Current Information of a WTI device
- [cpm_firmware_info module](cpm_firmware_info_module.md#ansible-collections-wti-remote-cpm-firmware-info-module) – Get firmware information from WTI OOB and PDU devices
- [cpm_firmware_update module](cpm_firmware_update_module.md#ansible-collections-wti-remote-cpm-firmware-update-module) – Set Serial port parameters in WTI OOB and PDU devices
- [cpm_hostname_config module](cpm_hostname_config_module.md#ansible-collections-wti-remote-cpm-hostname-config-module) – Set Hostname (Site ID), Location, Asset Tag parameters in WTI OOB and PDU devices.
- [cpm_hostname_info module](cpm_hostname_info_module.md#ansible-collections-wti-remote-cpm-hostname-info-module) – Get Hostname (Site ID), Location, Asset Tag parameters in WTI OOB and PDU devices
- [cpm_interface_config module](cpm_interface_config_module.md#ansible-collections-wti-remote-cpm-interface-config-module) – Set network interface parameters in WTI OOB and PDU devices
- [cpm_interface_info module](cpm_interface_info_module.md#ansible-collections-wti-remote-cpm-interface-info-module) – Get network interface parameters from WTI OOB and PDU devices
- [cpm_iptables_config module](cpm_iptables_config_module.md#ansible-collections-wti-remote-cpm-iptables-config-module) – Set network IPTables parameters in WTI OOB and PDU devices
- [cpm_iptables_info module](cpm_iptables_info_module.md#ansible-collections-wti-remote-cpm-iptables-info-module) – Get network IPTABLES parameters from WTI OOB and PDU devices
- [cpm_plugconfig module](cpm_plugconfig_module.md#ansible-collections-wti-remote-cpm-plugconfig-module) – Get and Set Plug Parameters on WTI OOB and PDU power devices
- [cpm_plugcontrol module](cpm_plugcontrol_module.md#ansible-collections-wti-remote-cpm-plugcontrol-module) – Get and Set Plug actions on WTI OOB and PDU power devices
- [cpm_power_info module](cpm_power_info_module.md#ansible-collections-wti-remote-cpm-power-info-module) – Get the Power Information of a WTI device
- [cpm_serial_port_action_info module](cpm_serial_port_action_info_module.md#ansible-collections-wti-remote-cpm-serial-port-action-info-module) – Get Serial port connection status in WTI OOB and PDU devices
- [cpm_serial_port_action_set module](cpm_serial_port_action_set_module.md#ansible-collections-wti-remote-cpm-serial-port-action-set-module) – Set Serial port connection/disconnection commands in WTI OOB and PDU devices
- [cpm_serial_port_config module](cpm_serial_port_config_module.md#ansible-collections-wti-remote-cpm-serial-port-config-module) – Set Serial port parameters in WTI OOB and PDU devices
- [cpm_serial_port_info module](cpm_serial_port_info_module.md#ansible-collections-wti-remote-cpm-serial-port-info-module) – Get Serial port parameters in WTI OOB and PDU devices
- [cpm_snmp_config module](cpm_snmp_config_module.md#ansible-collections-wti-remote-cpm-snmp-config-module) – Set network IPTables parameters in WTI OOB and PDU devices
- [cpm_snmp_info module](cpm_snmp_info_module.md#ansible-collections-wti-remote-cpm-snmp-info-module) – Get network SNMP parameters from WTI OOB and PDU devices
- [cpm_status_info module](cpm_status_info_module.md#ansible-collections-wti-remote-cpm-status-info-module) – Get general status information from WTI OOB and PDU devices
- [cpm_syslog_client_config module](cpm_syslog_client_config_module.md#ansible-collections-wti-remote-cpm-syslog-client-config-module) – Set network SYSLOG Client parameters in WTI OOB and PDU devices
- [cpm_syslog_client_info module](cpm_syslog_client_info_module.md#ansible-collections-wti-remote-cpm-syslog-client-info-module) – Get network SYSLOG Client parameters from WTI OOB and PDU devices
- [cpm_syslog_server_config module](cpm_syslog_server_config_module.md#ansible-collections-wti-remote-cpm-syslog-server-config-module) – Set network SYSLOG Server parameters in WTI OOB and PDU devices
- [cpm_syslog_server_info module](cpm_syslog_server_info_module.md#ansible-collections-wti-remote-cpm-syslog-server-info-module) – Get network SYSLOG Server parameters from WTI OOB and PDU devices
- [cpm_temp_info module](cpm_temp_info_module.md#ansible-collections-wti-remote-cpm-temp-info-module) – Get temperature information from WTI OOB and PDU devices
- [cpm_time_config module](cpm_time_config_module.md#ansible-collections-wti-remote-cpm-time-config-module) – Set Time/Date parameters in WTI OOB and PDU devices.
- [cpm_time_info module](cpm_time_info_module.md#ansible-collections-wti-remote-cpm-time-info-module) – Get Time/Date parameters in WTI OOB and PDU devices
- [cpm_user module](cpm_user_module.md#ansible-collections-wti-remote-cpm-user-module) – Get various status and parameters from WTI OOB and PDU devices

### Lookup Plugins

- [cpm_alarm_info lookup](cpm_alarm_info_lookup.md#ansible-collections-wti-remote-cpm-alarm-info-lookup) – Get alarm information from WTI OOB and PDU devices
- [cpm_config_backup lookup](cpm_config_backup_lookup.md#ansible-collections-wti-remote-cpm-config-backup-lookup) – Get parameters from WTI OOB and PDU devices
- [cpm_config_restore lookup](cpm_config_restore_lookup.md#ansible-collections-wti-remote-cpm-config-restore-lookup) – Send operational parameters to WTI OOB and PDU devices
- [cpm_current_info lookup](cpm_current_info_lookup.md#ansible-collections-wti-remote-cpm-current-info-lookup) – Get the Current Information of a WTI device
- [cpm_firmware_info lookup](cpm_firmware_info_lookup.md#ansible-collections-wti-remote-cpm-firmware-info-lookup) – Get firmware information from WTI OOB and PDU devices
- [cpm_firmware_update lookup](cpm_firmware_update_lookup.md#ansible-collections-wti-remote-cpm-firmware-update-lookup) – Set Serial port parameters in WTI OOB and PDU devices
- [cpm_hostname_config lookup](cpm_hostname_config_lookup.md#ansible-collections-wti-remote-cpm-hostname-config-lookup) – Set Hostname (Site ID), Location, Asset Tag parameters in WTI OOB and PDU devices.
- [cpm_hostname_info lookup](cpm_hostname_info_lookup.md#ansible-collections-wti-remote-cpm-hostname-info-lookup) – Get Hostname (Site ID), Location, Asset Tag parameters in WTI OOB and PDU devices
- [cpm_interface_config lookup](cpm_interface_config_lookup.md#ansible-collections-wti-remote-cpm-interface-config-lookup) – Set network interface parameters in WTI OOB and PDU devices
- [cpm_interface_info lookup](cpm_interface_info_lookup.md#ansible-collections-wti-remote-cpm-interface-info-lookup) – Get network interface parameters from WTI OOB and PDU devices
- [cpm_iptables_config lookup](cpm_iptables_config_lookup.md#ansible-collections-wti-remote-cpm-iptables-config-lookup) – Set network IPTables parameters in WTI OOB and PDU devices
- [cpm_iptables_info lookup](cpm_iptables_info_lookup.md#ansible-collections-wti-remote-cpm-iptables-info-lookup) – Get network IPTABLES parameters from WTI OOB and PDU devices
- [cpm_metering lookup](cpm_metering_lookup.md#ansible-collections-wti-remote-cpm-metering-lookup) – Get Power and Current data from WTI OOB/Combo and PDU devices
- [cpm_plugconfig lookup](cpm_plugconfig_lookup.md#ansible-collections-wti-remote-cpm-plugconfig-lookup) – Get and Set Plug Parameters on WTI OOB and PDU power devices
- [cpm_plugcontrol lookup](cpm_plugcontrol_lookup.md#ansible-collections-wti-remote-cpm-plugcontrol-lookup) – Get and Set Plug actions on WTI OOB and PDU power devices
- [cpm_power_info lookup](cpm_power_info_lookup.md#ansible-collections-wti-remote-cpm-power-info-lookup) – Get the Power Information of a WTI device
- [cpm_serial_port_action_info lookup](cpm_serial_port_action_info_lookup.md#ansible-collections-wti-remote-cpm-serial-port-action-info-lookup) – Get Serial port connection status in WTI OOB and PDU devices
- [cpm_serial_port_action_set lookup](cpm_serial_port_action_set_lookup.md#ansible-collections-wti-remote-cpm-serial-port-action-set-lookup) – Set Serial port connection/disconnection commands in WTI OOB and PDU devices
- [cpm_serial_port_config lookup](cpm_serial_port_config_lookup.md#ansible-collections-wti-remote-cpm-serial-port-config-lookup) – Set Serial port parameters in WTI OOB and PDU devices
- [cpm_serial_port_info lookup](cpm_serial_port_info_lookup.md#ansible-collections-wti-remote-cpm-serial-port-info-lookup) – Get Serial port parameters in WTI OOB and PDU devices
- [cpm_snmp_config lookup](cpm_snmp_config_lookup.md#ansible-collections-wti-remote-cpm-snmp-config-lookup) – Set network IPTables parameters in WTI OOB and PDU devices
- [cpm_snmp_info lookup](cpm_snmp_info_lookup.md#ansible-collections-wti-remote-cpm-snmp-info-lookup) – Get network SNMP parameters from WTI OOB and PDU devices
- [cpm_status lookup](cpm_status_lookup.md#ansible-collections-wti-remote-cpm-status-lookup) – Get status and parameters from WTI OOB and PDU devices.
- [cpm_status_info lookup](cpm_status_info_lookup.md#ansible-collections-wti-remote-cpm-status-info-lookup) – Get general status information from WTI OOB and PDU devices
- [cpm_syslog_client_config lookup](cpm_syslog_client_config_lookup.md#ansible-collections-wti-remote-cpm-syslog-client-config-lookup) – Set network SYSLOG Client parameters in WTI OOB and PDU devices
- [cpm_syslog_client_info lookup](cpm_syslog_client_info_lookup.md#ansible-collections-wti-remote-cpm-syslog-client-info-lookup) – Get network SYSLOG Client parameters from WTI OOB and PDU devices
- [cpm_syslog_server_config lookup](cpm_syslog_server_config_lookup.md#ansible-collections-wti-remote-cpm-syslog-server-config-lookup) – Set network SYSLOG Server parameters in WTI OOB and PDU devices
- [cpm_syslog_server_info lookup](cpm_syslog_server_info_lookup.md#ansible-collections-wti-remote-cpm-syslog-server-info-lookup) – Get network SYSLOG Server parameters from WTI OOB and PDU devices
- [cpm_temp_info lookup](cpm_temp_info_lookup.md#ansible-collections-wti-remote-cpm-temp-info-lookup) – Get temperature information from WTI OOB and PDU devices
- [cpm_time_config lookup](cpm_time_config_lookup.md#ansible-collections-wti-remote-cpm-time-config-lookup) – Set Time/Date parameters in WTI OOB and PDU devices.
- [cpm_time_info lookup](cpm_time_info_lookup.md#ansible-collections-wti-remote-cpm-time-info-lookup) – Get Time/Date parameters in WTI OOB and PDU devices
- [cpm_user lookup](cpm_user_lookup.md#ansible-collections-wti-remote-cpm-user-lookup) – Get various status and parameters from WTI OOB and PDU devices

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

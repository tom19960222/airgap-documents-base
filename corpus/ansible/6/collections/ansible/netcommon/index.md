---
collection: ansible
version: "6"
title: "Ansible.Netcommon"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/index.html
fetched_at: 2026-07-27T16:41:32+00:00
---
# Ansible.Netcommon

Collection version 3.1.3

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Collection with common content to help automate the management of network, security, and cloud devices.

**Author:**

- Ansible Network Community (ansible-network)

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)

## [Plugin Index](index.md#id2)

These are the plugins in the ansible.netcommon collection:

### Modules

- [cli_command module](cli_command_module.md#ansible-collections-ansible-netcommon-cli-command-module) – Run a cli command on cli-based network devices
- [cli_config module](cli_config_module.md#ansible-collections-ansible-netcommon-cli-config-module) – Push text based configuration to network devices over network_cli
- [grpc_config module](grpc_config_module.md#ansible-collections-ansible-netcommon-grpc-config-module) – Fetch configuration/state data from gRPC enabled target hosts.
- [grpc_get module](grpc_get_module.md#ansible-collections-ansible-netcommon-grpc-get-module) – Fetch configuration/state data from gRPC enabled target hosts.
- [net_banner module](net_banner_module.md#ansible-collections-ansible-netcommon-net-banner-module) – (deprecated, removed after 2022-06-01) Manage multiline banners on network devices
- [net_get module](net_get_module.md#ansible-collections-ansible-netcommon-net-get-module) – Copy a file from a network device to Ansible Controller
- [net_interface module](net_interface_module.md#ansible-collections-ansible-netcommon-net-interface-module) – (deprecated, removed after 2022-06-01) Manage Interface on network devices
- [net_l2_interface module](net_l2_interface_module.md#ansible-collections-ansible-netcommon-net-l2-interface-module) – (deprecated, removed after 2022-06-01) Manage Layer-2 interface on network devices
- [net_l3_interface module](net_l3_interface_module.md#ansible-collections-ansible-netcommon-net-l3-interface-module) – (deprecated, removed after 2022-06-01) Manage L3 interfaces on network devices
- [net_linkagg module](net_linkagg_module.md#ansible-collections-ansible-netcommon-net-linkagg-module) – (deprecated, removed after 2022-06-01) Manage link aggregation groups on network devices
- [net_lldp module](net_lldp_module.md#ansible-collections-ansible-netcommon-net-lldp-module) – (deprecated, removed after 2022-06-01) Manage LLDP service configuration on network devices
- [net_lldp_interface module](net_lldp_interface_module.md#ansible-collections-ansible-netcommon-net-lldp-interface-module) – (deprecated, removed after 2022-06-01) Manage LLDP interfaces configuration on network devices
- [net_logging module](net_logging_module.md#ansible-collections-ansible-netcommon-net-logging-module) – (deprecated, removed after 2022-06-01) Manage logging on network devices
- [net_ping module](net_ping_module.md#ansible-collections-ansible-netcommon-net-ping-module) – Tests reachability using ping from a network device
- [net_put module](net_put_module.md#ansible-collections-ansible-netcommon-net-put-module) – Copy a file from Ansible Controller to a network device
- [net_static_route module](net_static_route_module.md#ansible-collections-ansible-netcommon-net-static-route-module) – (deprecated, removed after 2022-06-01) Manage static IP routes on network appliances (routers, switches et. al.)
- [net_system module](net_system_module.md#ansible-collections-ansible-netcommon-net-system-module) – (deprecated, removed after 2022-06-01) Manage the system attributes on network devices
- [net_user module](net_user_module.md#ansible-collections-ansible-netcommon-net-user-module) – (deprecated, removed after 2022-06-01) Manage the aggregate of local users on network device
- [net_vlan module](net_vlan_module.md#ansible-collections-ansible-netcommon-net-vlan-module) – (deprecated, removed after 2022-06-01) Manage VLANs on network devices
- [net_vrf module](net_vrf_module.md#ansible-collections-ansible-netcommon-net-vrf-module) – (deprecated, removed after 2022-06-01) Manage VRFs on network devices
- [netconf_config module](netconf_config_module.md#ansible-collections-ansible-netcommon-netconf-config-module) – netconf device configuration
- [netconf_get module](netconf_get_module.md#ansible-collections-ansible-netcommon-netconf-get-module) – Fetch configuration/state data from NETCONF enabled network devices.
- [netconf_rpc module](netconf_rpc_module.md#ansible-collections-ansible-netcommon-netconf-rpc-module) – Execute operations on NETCONF enabled network devices.
- [network_resource module](network_resource_module.md#ansible-collections-ansible-netcommon-network-resource-module) – Manage resource modules
- [restconf_config module](restconf_config_module.md#ansible-collections-ansible-netcommon-restconf-config-module) – Handles create, update, read and delete of configuration data on RESTCONF enabled devices.
- [restconf_get module](restconf_get_module.md#ansible-collections-ansible-netcommon-restconf-get-module) – Fetch configuration/state data from RESTCONF enabled devices.
- [telnet module](telnet_module.md#ansible-collections-ansible-netcommon-telnet-module) – Executes a low-down and dirty telnet command

### Become Plugins

- [enable become](enable_become.md#ansible-collections-ansible-netcommon-enable-become) – Switch to elevated permissions on a network device

### Cache Plugins

- [memory cache](memory_cache.md#ansible-collections-ansible-netcommon-memory-cache) – RAM backed, non persistent cache.

### Connection Plugins

- [grpc connection](grpc_connection.md#ansible-collections-ansible-netcommon-grpc-connection) – Provides a persistent connection using the gRPC protocol
- [httpapi connection](httpapi_connection.md#ansible-collections-ansible-netcommon-httpapi-connection) – Use httpapi to run command on network appliances
- [libssh connection](libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection) – Run tasks using libssh for ssh connection
- [napalm connection](napalm_connection.md#ansible-collections-ansible-netcommon-napalm-connection) – Provides persistent connection using NAPALM
- [netconf connection](netconf_connection.md#ansible-collections-ansible-netcommon-netconf-connection) – Provides a persistent connection using the netconf protocol
- [network_cli connection](network_cli_connection.md#ansible-collections-ansible-netcommon-network-cli-connection) – Use network_cli to run command on network appliances
- [persistent connection](persistent_connection.md#ansible-collections-ansible-netcommon-persistent-connection) – Use a persistent unix socket for connection

### Httpapi Plugins

- [restconf httpapi](restconf_httpapi.md#ansible-collections-ansible-netcommon-restconf-httpapi) – HttpApi Plugin for devices supporting Restconf API

### Netconf Plugins

- [default netconf](default_netconf.md#ansible-collections-ansible-netcommon-default-netconf) – Use default netconf plugin to run standard netconf commands as per RFC

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

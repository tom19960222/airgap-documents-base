---
collection: ansible
version: "8"
title: "Ansible.Netcommon"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/index.html
fetched_at: 2026-07-28T01:01:49+00:00
---
# Ansible.Netcommon

Collection version 5.3.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Collection with common content to help automate the management of network, security, and cloud devices.

**Author:**

- Ansible Network Community (ansible-network)

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)

## [Plugin Index](index.md#id2)

These are the plugins in the ansible.netcommon collection:

### Modules

- [cli_backup module](cli_backup_module.md#ansible-collections-ansible-netcommon-cli-backup-module) – Back up device configuration from network devices over network_cli
- [cli_command module](cli_command_module.md#ansible-collections-ansible-netcommon-cli-command-module) – Run a cli command on cli-based network devices
- [cli_config module](cli_config_module.md#ansible-collections-ansible-netcommon-cli-config-module) – Push text based configuration to network devices over network_cli
- [grpc_config module](grpc_config_module.md#ansible-collections-ansible-netcommon-grpc-config-module) – Fetch configuration/state data from gRPC enabled target hosts.
- [grpc_get module](grpc_get_module.md#ansible-collections-ansible-netcommon-grpc-get-module) – Fetch configuration/state data from gRPC enabled target hosts.
- [net_get module](net_get_module.md#ansible-collections-ansible-netcommon-net-get-module) – Copy a file from a network device to Ansible Controller
- [net_ping module](net_ping_module.md#ansible-collections-ansible-netcommon-net-ping-module) – Tests reachability using ping from a network device
- [net_put module](net_put_module.md#ansible-collections-ansible-netcommon-net-put-module) – Copy a file from Ansible Controller to a network device
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

### Cliconf Plugins

- [default cliconf](default_cliconf.md#ansible-collections-ansible-netcommon-default-cliconf) – General purpose cliconf plugin for new platforms

### Connection Plugins

- [grpc connection](grpc_connection.md#ansible-collections-ansible-netcommon-grpc-connection) – Provides a persistent connection using the gRPC protocol
- [httpapi connection](httpapi_connection.md#ansible-collections-ansible-netcommon-httpapi-connection) – Use httpapi to run command on network appliances
- [libssh connection](libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection) – Run tasks using libssh for ssh connection
- [netconf connection](netconf_connection.md#ansible-collections-ansible-netcommon-netconf-connection) – Provides a persistent connection using the netconf protocol
- [network_cli connection](network_cli_connection.md#ansible-collections-ansible-netcommon-network-cli-connection) – Use network_cli to run command on network appliances
- [persistent connection](persistent_connection.md#ansible-collections-ansible-netcommon-persistent-connection) – Use a persistent unix socket for connection

### Filter Plugins

- [comp_type5 filter](comp_type5_filter.md#ansible-collections-ansible-netcommon-comp-type5-filter) – The comp_type5 filter plugin.
- [hash_salt filter](hash_salt_filter.md#ansible-collections-ansible-netcommon-hash-salt-filter) – The hash_salt filter plugin.
- [parse_cli filter](parse_cli_filter.md#ansible-collections-ansible-netcommon-parse-cli-filter) – parse_cli filter plugin.
- [parse_cli_textfsm filter](parse_cli_textfsm_filter.md#ansible-collections-ansible-netcommon-parse-cli-textfsm-filter) – parse_cli_textfsm filter plugin.
- [parse_xml filter](parse_xml_filter.md#ansible-collections-ansible-netcommon-parse-xml-filter) – The parse_xml filter plugin.
- [pop_ace filter](pop_ace_filter.md#ansible-collections-ansible-netcommon-pop-ace-filter) – Remove ace entries from a acl source of truth.
- [type5_pw filter](type5_pw_filter.md#ansible-collections-ansible-netcommon-type5-pw-filter) – The type5_pw filter plugin.
- [vlan_expander filter](vlan_expander_filter.md#ansible-collections-ansible-netcommon-vlan-expander-filter) – The vlan_expander filter plugin.
- [vlan_parser filter](vlan_parser_filter.md#ansible-collections-ansible-netcommon-vlan-parser-filter) – The vlan_parser filter plugin.

### Httpapi Plugins

- [restconf httpapi](restconf_httpapi.md#ansible-collections-ansible-netcommon-restconf-httpapi) – HttpApi Plugin for devices supporting Restconf API

### Netconf Plugins

- [default netconf](default_netconf.md#ansible-collections-ansible-netcommon-default-netconf) – Use default netconf plugin to run standard netconf commands as per RFC

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.

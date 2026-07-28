---
collection: ansible
version: "6"
title: "community.network.ce_info_center_global module – Manages outputting logs on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_info_center_global_module.html
fetched_at: 2026-07-27T17:17:28+00:00
---
# community.network.ce_info_center_global module – Manages outputting logs on HUAWEI CloudEngine switches.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ce_info_center_global`.

- [Synopsis](ce_info_center_global_module.md#synopsis)
- [Parameters](ce_info_center_global_module.md#parameters)
- [Notes](ce_info_center_global_module.md#notes)
- [Examples](ce_info_center_global_module.md#examples)
- [Return Values](ce_info_center_global_module.md#return-values)

## [Synopsis](ce_info_center_global_module.md#id1)

- This module offers the ability to be output to the log buffer, log file, console, terminal, or log host on HUAWEI CloudEngine switches.

## [Parameters](ce_info_center_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **channel_cfg_name**  string | Channel name.The value is a string of 1 to 30 case-sensitive characters. The default value is console.  Default: `"console"` |
| **channel_id**  string | Number for channel. The value is an integer ranging from 0 to 9. The default value is 0. |
| **channel_name**  string | Channel name. The value is a string of 1 to 30 case-sensitive characters. |
| **channel_out_direct**  string | Direction of information output.  Choices:   - `"console"` - `"monitor"` - `"trapbuffer"` - `"logbuffer"` - `"snmp"` - `"logfile"` |
| **facility**  string | Log record tool.  Choices:   - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` |
| **filter_feature_name**  string | Feature name of the filtered log. The value is a string of 1 to 31 case-insensitive characters. |
| **filter_log_name**  string | Name of the filtered log. The value is a string of 1 to 63 case-sensitive characters. |
| **info_center_enable**  string | Whether the info-center function is enabled. The value is of the Boolean type.  Choices:   - `"true"` - `"false"` |
| **ip_type**  string | Log server address type, IPv4 or IPv6.  Choices:   - `"ipv4"` - `"ipv6"` |
| **is_default_vpn**  boolean | Use the default VPN or not.  Choices:   - `false` ← (default) - `true` |
| **level**  string | Level of logs saved on a log server.  Choices:   - `"emergencies"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"informational"` - `"debugging"` |
| **logfile_max_num**  string | Maximum number of log files of the same type. The default value is 200.  The value range for log files is[3, 500], for security files is [1, 3],and for operation files is [1, 7]. |
| **logfile_max_size**  string | Maximum size (in MB) of a log file. The default value is 32.  The value range for log files is [4, 8, 16, 32], for security files is [1, 4],  and for operation files is [1, 4].  Choices:   - `"4"` - `"8"` - `"16"` - `"32"`   Default: `32` |
| **packet_priority**  string | Set the priority of the syslog packet.The value is an integer ranging from 0 to 7. The default value is 0. |
| **server_domain**  string | Server name. The value is a string of 1 to 255 case-sensitive characters. |
| **server_ip**  string | Log server address, IPv4 or IPv6 type. The value is a string of 0 to 255 characters. The value can be an valid IPv4 or IPv6 address. |
| **server_port**  string | Number of a port sending logs.The value is an integer ranging from 1 to 65535. For UDP, the default value is 514. For TCP, the default value is 601. For TSL, the default value is 6514. |
| **source_ip**  string | Log source ip address, IPv4 or IPv6 type. The value is a string of 0 to 255. The value can be an valid IPv4 or IPv6 address. |
| **ssl_policy_name**  string | SSL policy name. The value is a string of 1 to 23 case-sensitive characters. |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **suppress_enable**  string | Whether a device is enabled to suppress duplicate statistics. The value is of the Boolean type.  Choices:   - `"false"` - `"true"` |
| **timestamp**  string | Log server timestamp. The value is of the enumerated type and case-sensitive.  Choices:   - `"UTC"` - `"localtime"` |
| **transport_mode**  string | Transport mode. The value is of the enumerated type and case-sensitive.  Choices:   - `"tcp"` - `"udp"` |
| **vrf_name**  string | VPN name on a log server. The value is a string of 1 to 31 case-sensitive characters. The default value is _public_. |

## [Notes](ce_info_center_global_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_info_center_global_module.md#id4)

```yaml+jinja
- name: Info center global module test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: Config info-center enable
    community.network.ce_info_center_global:
      info_center_enable: true
      state: present
      provider: "{{ cli }}"

  - name: Config statistic-suppress enable
    community.network.ce_info_center_global:
      suppress_enable: true
      state: present
      provider: "{{ cli }}"

  - name: Config info-center syslog packet-priority 1
    community.network.ce_info_center_global:
      packet_priority: 2
      state: present
      provider: "{{ cli }}"

  - name: Config info-center channel 1 name aaa
    community.network.ce_info_center_global:
      channel_id: 1
      channel_cfg_name: aaa
      state: present
      provider: "{{ cli }}"

  - name: Config info-center logfile size 10
    community.network.ce_info_center_global:
      logfile_max_num: 10
      state: present
      provider: "{{ cli }}"

  - name: Config info-center console channel 1
    community.network.ce_info_center_global:
      channel_out_direct: console
      channel_id: 1
      state: present
      provider: "{{ cli }}"

  - name: Config info-center filter-id bymodule-alias snmp snmp_ipunlock
    community.network.ce_info_center_global:
      filter_feature_name: SNMP
      filter_log_name: SNMP_IPLOCK
      state: present
      provider: "{{ cli }}"

  - name: Config info-center max-logfile-number 16
    community.network.ce_info_center_global:
      logfile_max_size: 16
      state: present
      provider: "{{ cli }}"

  - name: Config syslog loghost domain.
    community.network.ce_info_center_global:
      server_domain: aaa
      vrf_name: aaa
      channel_id: 1
      transport_mode: tcp
      facility: local4
      server_port: 100
      level: alert
      timestamp: UTC
      state: present
      provider: "{{ cli }}"
```

## [Return Values](ce_info_center_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{"server_domain_info": [{"chnlId": "1", "chnlName": "monitor", "facility": "local4", "isBriefFmt": "false", "isDefaultVpn": "true", "level": "alert", "serverDomain": "aaa", "serverPort": "100", "sourceIP": "0.0.0.0", "sslPolicyName": null, "timestamp": "localtime", "transportMode": "tcp", "vrfName": "_public_"}, {"chnlId": "1", "chnlName": "monitor", "facility": "local4", "isBriefFmt": "false", "isDefaultVpn": "false", "level": "alert", "serverDomain": "aaa", "serverPort": "100", "sourceIP": "0.0.0.0", "sslPolicyName": "gmc", "timestamp": "UTC", "transportMode": "tcp", "vrfName": "aaa"}]}` |
| **existing**  dictionary | k/v pairs of existing rollback  Returned: always  Sample: `{"server_domain_info": [{"chnlId": "1", "chnlName": "monitor", "facility": "local4", "isBriefFmt": "false", "isDefaultVpn": "false", "level": "alert", "serverDomain": "aaa", "serverPort": "100", "sourceIP": "0.0.0.0", "sslPolicyName": "gmc", "timestamp": "UTC", "transportMode": "tcp", "vrfName": "aaa"}]}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"channel_id": "1", "facility": "local4", "is_default_vpn": true, "level": "alert", "server_domain": "aaa", "server_port": "100", "state": "present", "timestamp": "localtime", "transport_mode": "tcp"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["info-center loghost domain aaa level alert port 100 facility local4 channel 1 localtime transport tcp"]` |

### Authors

- Li Yanfeng (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)

---
collection: ansible
version: "8"
title: "community.network.ce_aaa_server_host module – Manages AAA server host configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_aaa_server_host_module.html
fetched_at: 2026-07-28T01:55:10+00:00
---
# community.network.ce_aaa_server_host module – Manages AAA server host configuration on HUAWEI CloudEngine switches.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ce_aaa_server_host`.

- [Synopsis](ce_aaa_server_host_module.md#synopsis)
- [Parameters](ce_aaa_server_host_module.md#parameters)
- [Notes](ce_aaa_server_host_module.md#notes)
- [Examples](ce_aaa_server_host_module.md#examples)
- [Return Values](ce_aaa_server_host_module.md#return-values)

## [Synopsis](ce_aaa_server_host_module.md#id1)

- Manages AAA server host configuration on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_aaa_server_host

## [Parameters](ce_aaa_server_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hwtacacs_is_public_net**  boolean | Set the public-net.  **Choices:**   - `false` ← (default) - `true` |
| **hwtacacs_is_secondary_server**  boolean | Whether the server is secondary.  **Choices:**   - `false` ← (default) - `true` |
| **hwtacacs_server_host_name**  string | Hwtacacs server host name. |
| **hwtacacs_server_ip**  string | Server IPv4 address. Must be a valid unicast IP address. The value is a string of 0 to 255 characters, in dotted decimal notation. |
| **hwtacacs_server_ipv6**  string | Server IPv6 address. Must be a valid unicast IP address. The total length is 128 bits. |
| **hwtacacs_server_type**  string | Hwtacacs server type.  **Choices:**   - `"Authentication"` - `"Authorization"` - `"Accounting"` - `"Common"` |
| **hwtacacs_template**  string | Name of a HWTACACS template. The value is a string of 1 to 32 case-insensitive characters. |
| **hwtacacs_vpn_name**  string | VPN instance name. |
| **local_ftp_dir**  string | FTP user directory. The value is a string of 1 to 255 characters. |
| **local_password**  string | Login password of a user. The password can contain letters, numbers, and special characters. The value is a string of 1 to 255 characters. |
| **local_service_type**  string | The type of local user login through, such as ftp ssh snmp telnet. |
| **local_user_group**  string | Name of the user group where the user belongs. The user inherits all the rights of the user group. The value is a string of 1 to 32 characters. |
| **local_user_level**  string | Login level of a local user. The value is an integer ranging from 0 to 15. |
| **local_user_name**  string | Name of a local user. The value is a string of 1 to 253 characters. |
| **radius_group_name**  string | RADIUS server group’s name. The value is a string of 1 to 32 case-insensitive characters. |
| **radius_server_ip**  string | IPv4 address of configured server. The value is a string of 0 to 255 characters, in dotted decimal notation. |
| **radius_server_ipv6**  string | IPv6 address of configured server. The total length is 128 bits. |
| **radius_server_mode**  string | Configured primary or secondary server for a particular server.  **Choices:**   - `"Secondary-server"` - `"Primary-server"` |
| **radius_server_name**  string | Hostname of configured server. The value is a string of 0 to 255 case-sensitive characters. |
| **radius_server_port**  string | Configured server port for a particular server. The value is an integer ranging from 1 to 65535. |
| **radius_server_type**  string | Type of Radius Server.  **Choices:**   - `"Authentication"` - `"Accounting"` |
| **radius_vpn_name**  string | Set VPN instance. The value is a string of 1 to 31 case-sensitive characters. |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_aaa_server_host_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_aaa_server_host_module.md#id4)

```yaml+jinja
- name: AAA server host test
  hosts: cloudengine
  connection: local
  gather_facts: false

  tasks:

  - name: "Config local user when use local scheme"
    community.network.ce_aaa_server_host:
      state: present
      local_user_name: user1
      local_password: 123456

  - name: "Undo local user when use local scheme"
    community.network.ce_aaa_server_host:
      state: absent
      local_user_name: user1
      local_password: 123456

  - name: "Config radius server ip"
    community.network.ce_aaa_server_host:
      state: present
      radius_group_name: group1
      radius_server_type: Authentication
      radius_server_ip: 10.1.10.1
      radius_server_port: 2000
      radius_server_mode: Primary-server
      radius_vpn_name: _public_

  - name: "Undo radius server ip"
    community.network.ce_aaa_server_host:
      state: absent
      radius_group_name: group1
      radius_server_type: Authentication
      radius_server_ip: 10.1.10.1
      radius_server_port: 2000
      radius_server_mode: Primary-server
      radius_vpn_name: _public_

  - name: "Config hwtacacs server ip"
    community.network.ce_aaa_server_host:
      state: present
      hwtacacs_template: template
      hwtacacs_server_ip: 10.10.10.10
      hwtacacs_server_type: Authorization
      hwtacacs_vpn_name: _public_

  - name: "Undo hwtacacs server ip"
    community.network.ce_aaa_server_host:
      state: absent
      hwtacacs_template: template
      hwtacacs_server_ip: 10.10.10.10
      hwtacacs_server_type: Authorization
      hwtacacs_vpn_name: _public_
```

## [Return Values](ce_aaa_server_host_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  **Returned:** always  **Sample:** `{"radius server ipv4": [["10.1.10.1", "Authentication", "2000", "Primary-server", "_public_"]]}` |
| **existing**  dictionary | k/v pairs of existing aaa server host  **Returned:** always  **Sample:** `{"radius server ipv4": []}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"hwtacacs_is_public_net": "false", "hwtacacs_is_secondary_server": "false", "hwtacacs_server_ip": "10.135.182.157", "hwtacacs_server_type": "Authorization", "hwtacacs_template": "wdz", "hwtacacs_vpn_name": "_public_", "local_password": "******", "state": "present"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["hwtacacs server template test", "hwtacacs server authorization 10.135.182.157 vpn-instance test_vpn public-net"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)

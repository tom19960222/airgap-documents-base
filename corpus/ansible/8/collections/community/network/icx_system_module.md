---
collection: ansible
version: "8"
title: "community.network.icx_system module – Manage the system attributes on Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/icx_system_module.html
fetched_at: 2026-07-28T01:56:53+00:00
---
# community.network.icx_system module – Manage the system attributes on Ruckus ICX 7000 series switches

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
> To use it in a playbook, specify: `community.network.icx_system`.

- [Synopsis](icx_system_module.md#synopsis)
- [Parameters](icx_system_module.md#parameters)
- [Notes](icx_system_module.md#notes)
- [Examples](icx_system_module.md#examples)
- [Return Values](icx_system_module.md#return-values)

## [Synopsis](icx_system_module.md#id1)

- This module provides declarative management of node system attributes on Ruckus ICX 7000 series switches. It provides an option to configure host system parameters or remove those parameters from the device active configuration.

Aliases: network.icx.icx_system

## [Parameters](icx_system_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aaa_servers**  list / elements=string | Configures radius/tacacs server |
| **acct_port_num**  string | Configures the accounting UDP port. The default value is 1813. |
| **acct_type**  string | Usage of the accounting port.  **Choices:**   - `"accounting-only"` - `"authentication-only"` - `"authorization-only"` - `"default"` |
| **auth_key**  string | Configure the key for the server |
| **auth_key_type**  list / elements=string | List of authentication level specified in the choices  **Choices:**   - `"dot1x"` - `"mac-auth"` - `"web-auth"` |
| **auth_port_num**  string | Configures the authentication UDP port. The default value is 1812. |
| **auth_port_type**  string | specifies the type of the authentication port  **Choices:**   - `"auth-port"` |
| **hostname**  string | Configures the host name of the RADIUS server |
| **type**  string | specify the type of the server  **Choices:**   - `"radius"` - `"tacacs"` |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  **Choices:**   - `false` - `true` ← (default) |
| **domain_name**  list / elements=string | Configure the IP domain name on the remote device to the provided value. Value should be in the dotted name form and will be appended to the hostname to create a fully-qualified domain name. |
| **domain_search**  list / elements=string | Provides the list of domain names to append to the hostname for the purpose of doing name resolution. This argument accepts a list of names and will be reconciled with the current active configuration on the running node. |
| **hostname**  string | Configure the device hostname parameter. This option takes an ASCII string value. |
| **name_servers**  list / elements=string | List of DNS name servers by IP address to use to perform name resolution lookups. |
| **state**  string | State of the configuration values in the device’s current active configuration. When set to *present*, the values should be configured in the device active configuration and when set to *absent* the values should not be in the device active configuration  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](icx_system_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1.
> - For information on using ICX platform, see [the ICX OS Platform Options guide](user_guide/platform_icx.md).

## [Examples](icx_system_module.md#id4)

```yaml+jinja
- name: Configure hostname and domain name
  community.network.icx_system:
    hostname: icx
    domain_search:
      - ansible.com
      - redhat.com
      - ruckus.com

- name: Configure radius server of type auth-port
  community.network.icx_system:
    aaa_servers:
      - type: radius
        hostname: radius-server
        auth_port_type: auth-port
        auth_port_num: 1821
        acct_port_num: 1321
        acct_type: accounting-only
        auth_key: abc
        auth_key_type:
          - dot1x
          - mac-auth

- name: Configure tacacs server
  community.network.icx_system:
    aaa_servers:
      - type: tacacs
        hostname: tacacs-server
        auth_port_type: auth-port
        auth_port_num: 1821
        acct_port_num: 1321
        acct_type: accounting-only
        auth_key: xyz

- name: Configure name servers
  community.network.icx_system:
    name_servers:
      - 8.8.8.8
      - 8.8.4.4
```

## [Return Values](icx_system_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["hostname icx", "ip domain name test.example.com", "radius-server host 172.16.10.12 auth-port 2083 acct-port 1850 default key abc dot1x mac-auth", "tacacs-server host 10.2.3.4 auth-port 4058 authorization-only key xyz"]` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)

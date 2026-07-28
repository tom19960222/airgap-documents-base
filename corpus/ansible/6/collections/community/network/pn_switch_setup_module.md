---
collection: ansible
version: "6"
title: "community.network.pn_switch_setup module – CLI command to modify switch-setup"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_switch_setup_module.html
fetched_at: 2026-07-27T17:19:32+00:00
---
# community.network.pn_switch_setup module – CLI command to modify switch-setup

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
> To use it in a playbook, specify: `community.network.pn_switch_setup`.

- [Synopsis](pn_switch_setup_module.md#synopsis)
- [Parameters](pn_switch_setup_module.md#parameters)
- [Examples](pn_switch_setup_module.md#examples)
- [Return Values](pn_switch_setup_module.md#return-values)

## [Synopsis](pn_switch_setup_module.md#id1)

- This module can be used to modify switch setup.

## [Parameters](pn_switch_setup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_analytics_store**  string | type of disk storage for analytics.  Choices:   - `"default"` - `"optimized"` |
| **pn_banner**  string | Banner to display on server-switch. |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_date**  string | Date. |
| **pn_dns_ip**  string | DNS IP address. |
| **pn_dns_secondary_ip**  string | secondary DNS IP address. |
| **pn_domain_name**  string | Domain name. |
| **pn_enable_host_ports**  boolean | Enable host ports by default.  Choices:   - `false` - `true` |
| **pn_eula_accepted**  string | Accept EULA.  Choices:   - `"true"` - `"false"` |
| **pn_eula_timestamp**  string | EULA timestamp. |
| **pn_force**  boolean | Force analytics-store change even if it involves removing data.  Choices:   - `false` - `true` |
| **pn_gateway_ip**  string | gateway IPv4 address. |
| **pn_gateway_ip6**  string | Gateway IPv6 address. |
| **pn_in_band_ip**  string | data in-band IP address. |
| **pn_in_band_ip6**  string | Data in-band IPv6 address. |
| **pn_in_band_ip6_assign**  string | Data IPv6 address assignment.  Choices:   - `"none"` - `"autoconf"` |
| **pn_in_band_netmask**  string | Data in-band netmask. |
| **pn_in_band_netmask_ip6**  string | Data in-band IPv6 netmask. |
| **pn_loopback_ip**  string | loopback IPv4 address. |
| **pn_loopback_ip6**  string | loopback IPv6 address. |
| **pn_mgmt_ip**  string | Management IP address. |
| **pn_mgmt_ip6**  string | IPv6 address. |
| **pn_mgmt_ip6_assignment**  string | IPv6 address assignment.  Choices:   - `"none"` - `"autoconf"` |
| **pn_mgmt_ip_assignment**  string | IP address assignment.  Choices:   - `"none"` - `"dhcp"` |
| **pn_mgmt_netmask**  string | Netmask. |
| **pn_mgmt_netmask_ip6**  string | IPv6 netmask. |
| **pn_motd**  string | Message of the Day. |
| **pn_ntp_secondary_server**  string | Secondary NTP server. |
| **pn_ntp_server**  string | NTP server. |
| **pn_password**  string | plain text password. |
| **pn_switch_name**  string | switch name. |
| **pn_timezone**  string | Timezone to be configured. |
| **state**  string / required | State the action to perform. Use `update` to modify the switch-setup.  Choices:   - `"update"` |

## [Examples](pn_switch_setup_module.md#id3)

```yaml+jinja
- name: Modify switch
  community.network.pn_switch_setup:
    pn_cliswitch: "sw01"
    state: "update"
    pn_timezone: "America/New_York"
    pn_in_band_ip: "20.20.1.1"
    pn_in_band_netmask: "24"

- name: Modify switch
  community.network.pn_switch_setup:
    pn_cliswitch: "sw01"
    state: "update"
    pn_in_band_ip6: "2001:0db8:85a3::8a2e:0370:7334"
    pn_in_band_netmask_ip6: "127"
```

## [Return Values](pn_switch_setup_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the switch-setup command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the switch-setup command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)

---
collection: ansible
version: "6"
title: "community.network.pn_admin_service module – CLI command to modify admin-service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_admin_service_module.html
fetched_at: 2026-07-27T17:19:15+00:00
---
# community.network.pn_admin_service module – CLI command to modify admin-service

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
> To use it in a playbook, specify: `community.network.pn_admin_service`.

- [Synopsis](pn_admin_service_module.md#synopsis)
- [Parameters](pn_admin_service_module.md#parameters)
- [Examples](pn_admin_service_module.md#examples)
- [Return Values](pn_admin_service_module.md#return-values)

## [Synopsis](pn_admin_service_module.md#id1)

- This module is used to modify services on the server-switch.

## [Parameters](pn_admin_service_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn__if**  string | administrative service interface.  Choices:   - `"mgmt"` - `"data"` |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_icmp**  boolean | Internet Message Control Protocol (ICMP) to enable or disable.  Choices:   - `false` - `true` |
| **pn_net_api**  boolean | Netvisor API to enable or disable APIs.  Choices:   - `false` - `true` |
| **pn_nfs**  boolean | Network File System (NFS) to enable or disable.  Choices:   - `false` - `true` |
| **pn_snmp**  boolean | Simple Network Monitoring Protocol (SNMP) to enable or disable.  Choices:   - `false` - `true` |
| **pn_ssh**  boolean | Secure Shell to enable or disable.  Choices:   - `false` - `true` |
| **pn_web**  boolean | Web (HTTP) to enable or disable.  Choices:   - `false` - `true` |
| **pn_web_log**  boolean | Web logging to enable or disable.  Choices:   - `false` - `true` |
| **pn_web_port**  string | Web (HTTP) port to enable or disable. |
| **pn_web_ssl**  boolean | Web SSL (HTTPS) to enable or disable.  Choices:   - `false` - `true` |
| **pn_web_ssl_port**  string | Web SSL (HTTPS) port to enable or disable. |
| **state**  string / required | State the action to perform. Use `update` to modify the admin-service.  Choices:   - `"update"` |

## [Examples](pn_admin_service_module.md#id3)

```yaml+jinja
- name: Admin service functionality
  community.network.pn_admin_service:
    pn_cliswitch: "sw01"
    state: "update"
    pn__if: "mgmt"
    pn_web: False
    pn_icmp: True

- name: Admin service functionality
  community.network.pn_admin_service:
    pn_cliswitch: "sw01"
    state: "update"
    pn_web: False
    pn__if: "mgmt"
    pn_snmp: True
    pn_net_api: True
    pn_ssh: True
```

## [Return Values](pn_admin_service_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the admin-service command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the admin-service command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)

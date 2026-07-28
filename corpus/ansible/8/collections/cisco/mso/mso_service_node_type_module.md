---
collection: ansible
version: "8"
title: "cisco.mso.mso_service_node_type module – Manage Service Node Types"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/mso/mso_service_node_type_module.html
fetched_at: 2026-07-28T01:38:16+00:00
---
# cisco.mso.mso_service_node_type module – Manage Service Node Types

> **Note:**
>
> This module is part of the [cisco.mso collection](https://galaxy.ansible.com/ui/repo/published/cisco/mso/) (version 2.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.mso`.
> You need further requirements to be able to use this module,
> see [Requirements](mso_service_node_type_module.md#ansible-collections-cisco-mso-mso-service-node-type-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_service_node_type`.

- [Synopsis](mso_service_node_type_module.md#synopsis)
- [Requirements](mso_service_node_type_module.md#requirements)
- [Parameters](mso_service_node_type_module.md#parameters)
- [Notes](mso_service_node_type_module.md#notes)
- [Examples](mso_service_node_type_module.md#examples)

## [Synopsis](mso_service_node_type_module.md#id1)

- Manage Service Node Types on Cisco ACI Multi-Site.

## [Requirements](mso_service_node_type_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_service_node_type_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **display_name**  string | The name of the node type as displayed on the MSO web interface. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_login_domain` will be used if this attribute is not specified. |
| **name**  string | The name of the node type. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **timeout**  integer | The socket level timeout in seconds.  The default value is 30 seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead. |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `false` when using a HTTPAPI connection plugin (mso or nd) and `true` when using the legacy connection method (only for mso).  **Choices:**   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |

## [Notes](mso_service_node_type_module.md#id4)

> **Note:**
>
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [Examples](mso_service_node_type_module.md#id5)

```yaml+jinja
- name: Add a new Service Node Type
  cisco.mso.mso_schema_service_node:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    name: ips
    display_name: ips
    state: present
  delegate_to: localhost

- name: Remove a Service Node Type
  cisco.mso.mso_schema_service_node:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    name: ips
    state: absent
  delegate_to: localhost

- name: Query a specific Service Node Type
  cisco.mso.mso_schema_service_node:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    name: ips
    state: query
  delegate_to: localhost

- name: Query all Service Node Types
  cisco.mso.mso_schema_service_node:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost
```

### Authors

- Shreyas Srish (@shrsr)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
- [Homepage](https://cisco.com/go/aci)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

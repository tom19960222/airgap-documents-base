---
collection: ansible
version: "6"
title: "cisco.mso.mso_tenant module – Manage tenants"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/mso/mso_tenant_module.html
fetched_at: 2026-07-27T17:01:26+00:00
---
# cisco.mso.mso_tenant module – Manage tenants

> **Note:**
>
> This module is part of the [cisco.mso collection](https://galaxy.ansible.com/cisco/mso) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.mso`.
> You need further requirements to be able to use this module,
> see [Requirements](mso_tenant_module.md#ansible-collections-cisco-mso-mso-tenant-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_tenant`.

- [Synopsis](mso_tenant_module.md#synopsis)
- [Requirements](mso_tenant_module.md#requirements)
- [Parameters](mso_tenant_module.md#parameters)
- [Notes](mso_tenant_module.md#notes)
- [Examples](mso_tenant_module.md#examples)

## [Synopsis](mso_tenant_module.md#id1)

- Manage tenants on Cisco ACI Multi-Site.

## [Requirements](mso_tenant_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_tenant_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | The description for this tenant. |
| **display_name**  string | The name of the tenant to be displayed in the web UI. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  Choices:   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **sites**  list / elements=string | A list of associated sites for this tenant.  Using this property will replace any existing associated sites. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **tenant**  aliases: name  string | The name of the tenant. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead.  Default: `30` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `no` when using a HTTPAPI connection plugin (mso or nd) and `yes` when using the legacy connection method (only for mso).  Choices:   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **users**  list / elements=string | A list of associated users for this tenant.  Using this property will replace any existing associated users.  Admin user is always added to the associated user list irrespective of this parameter being used. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |

## [Notes](mso_tenant_module.md#id4)

> **Note:**
>
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [Examples](mso_tenant_module.md#id5)

```yaml+jinja
- name: Add a new tenant
  cisco.mso.mso_tenant:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    tenant: north_europe
    display_name: North European Datacenter
    description: This tenant manages the NEDC environment.
    state: present
  delegate_to: localhost

- name: Remove a tenant
  cisco.mso.mso_tenant:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    tenant: north_europe
    state: absent
  delegate_to: localhost

- name: Query a tenant
  cisco.mso.mso_tenant:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    tenant: north_europe
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all tenants
  cisco.mso.mso_tenant:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost
  register: query_result
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
[Homepage](https://cisco.com/go/aci)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

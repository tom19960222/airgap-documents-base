---
collection: ansible
version: "8"
title: "cisco.mso.mso_schema_site_bd_subnet module – Manage site-local BD subnets in schema template"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/mso/mso_schema_site_bd_subnet_module.html
fetched_at: 2026-07-28T01:37:50+00:00
---
# cisco.mso.mso_schema_site_bd_subnet module – Manage site-local BD subnets in schema template

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
> see [Requirements](mso_schema_site_bd_subnet_module.md#ansible-collections-cisco-mso-mso-schema-site-bd-subnet-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_schema_site_bd_subnet`.

- [Synopsis](mso_schema_site_bd_subnet_module.md#synopsis)
- [Requirements](mso_schema_site_bd_subnet_module.md#requirements)
- [Parameters](mso_schema_site_bd_subnet_module.md#parameters)
- [Notes](mso_schema_site_bd_subnet_module.md#notes)
- [See Also](mso_schema_site_bd_subnet_module.md#see-also)
- [Examples](mso_schema_site_bd_subnet_module.md#examples)

## [Synopsis](mso_schema_site_bd_subnet_module.md#id1)

- Manage site-local BD subnets in schema template on Cisco ACI Multi-Site.

## [Requirements](mso_schema_site_bd_subnet_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_schema_site_bd_subnet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bd**  aliases: name  string / required | The name of the BD. |
| **description**  string | The description of this subnet. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **is_virtual_ip**  boolean | Treat as Virtual IP Address  **Choices:**   - `false` ← (default) - `true` |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_login_domain` will be used if this attribute is not specified. |
| **no_default_gateway**  boolean | Whether this subnet has a default gateway.  **Choices:**   - `false` ← (default) - `true` |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **primary**  boolean | Treat as Primary Subnet.  There can be only one primary subnet per address family under a BD.  This option can only be used on versions of MSO that are 3.1.1h or greater.  **Choices:**   - `false` ← (default) - `true` |
| **querier**  boolean | Whether this subnet is an IGMP querier.  **Choices:**   - `false` ← (default) - `true` |
| **schema**  string / required | The name of the schema. |
| **scope**  string | The scope of the subnet.  **Choices:**   - `"private"` - `"public"` |
| **shared**  boolean | Whether this subnet is shared between VRFs.  **Choices:**   - `false` ← (default) - `true` |
| **site**  string / required | The name of the site. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **subnet**  aliases: ip  string | The IP range in CIDR notation. |
| **template**  string / required | The name of the template. |
| **timeout**  integer | The socket level timeout in seconds.  The default value is 30 seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead. |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `false` when using a HTTPAPI connection plugin (mso or nd) and `true` when using the legacy connection method (only for mso).  **Choices:**   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |

## [Notes](mso_schema_site_bd_subnet_module.md#id4)

> **Note:**
>
> - The ACI MultiSite PATCH API has a deficiency requiring some objects to be referenced by index. This can cause silent corruption on concurrent access when changing/removing on object as the wrong object may be referenced. This module is affected by this deficiency.
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [See Also](mso_schema_site_bd_subnet_module.md#id5)

> **See also:**
>
> [cisco.mso.mso_schema_site_bd](mso_schema_site_bd_module.md#ansible-collections-cisco-mso-mso-schema-site-bd-module)
> :   Manage site-local Bridge Domains (BDs) in schema template.
>
> [cisco.mso.mso_schema_template_bd](mso_schema_template_bd_module.md#ansible-collections-cisco-mso-mso-schema-template-bd-module)
> :   Manage Bridge Domains (BDs) in schema templates.

## [Examples](mso_schema_site_bd_subnet_module.md#id6)

```yaml+jinja
- name: Add a new site BD subnet
  cisco.mso.mso_schema_site_bd_subnet:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    bd: BD1
    subnet: 11.11.11.0/24
    state: present
  delegate_to: localhost

- name: Remove a site BD subnet
  cisco.mso.mso_schema_site_bd_subnet:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    bd: BD1
    subnet: 11.11.11.0/24
    state: absent
  delegate_to: localhost

- name: Query a specific site BD subnet
  cisco.mso.mso_schema_site_bd_subnet:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    bd: BD1
    subnet: 11.11.11.0/24
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all site BD subnets
  cisco.mso.mso_schema_site_bd_subnet:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    bd: BD1
    state: query
  delegate_to: localhost
  register: query_result
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
- [Homepage](https://cisco.com/go/aci)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

---
collection: ansible
version: "8"
title: "cisco.mso.mso_schema_template_anp_epg_useg_attribute module – Manage EPG uSeg Attributes in schema templates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/mso/mso_schema_template_anp_epg_useg_attribute_module.html
fetched_at: 2026-07-28T01:38:01+00:00
---
# cisco.mso.mso_schema_template_anp_epg_useg_attribute module – Manage EPG uSeg Attributes in schema templates

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
> see [Requirements](mso_schema_template_anp_epg_useg_attribute_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-epg-useg-attribute-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_schema_template_anp_epg_useg_attribute`.

- [Synopsis](mso_schema_template_anp_epg_useg_attribute_module.md#synopsis)
- [Requirements](mso_schema_template_anp_epg_useg_attribute_module.md#requirements)
- [Parameters](mso_schema_template_anp_epg_useg_attribute_module.md#parameters)
- [Notes](mso_schema_template_anp_epg_useg_attribute_module.md#notes)
- [Examples](mso_schema_template_anp_epg_useg_attribute_module.md#examples)

## [Synopsis](mso_schema_template_anp_epg_useg_attribute_module.md#id1)

- Manage uSeg Attributes in the schema template EPGs on Cisco ACI Multi-Site.

## [Requirements](mso_schema_template_anp_epg_useg_attribute_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_schema_template_anp_epg_useg_attribute_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **anp**  string / required | The name of the Application Profile. |
| **description**  aliases: descr  string | The description of the uSeg Attribute. |
| **epg**  string / required | The name of the EPG. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_login_domain` will be used if this attribute is not specified. |
| **name**  aliases: useg  string | The name and display name of the uSeg Attribute. |
| **operator**  string | The operator type of the uSeg Attribute.  **Choices:**   - `"equals"` - `"contains"` - `"starts_with"` - `"ends_with"` |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **schema**  string / required | The name of the Schema. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **template**  string / required | The name of the Template. |
| **timeout**  integer | The socket level timeout in seconds.  The default value is 30 seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead. |
| **type**  aliases: attribute_type  string | The type of the uSeg Attribute.  **Choices:**   - `"vm_name"` - `"ip"` - `"mac"` - `"vmm_domain"` - `"vm_operating_system"` - `"vm_tag"` - `"vm_hypervisor_identifier"` - `"dns"` - `"vm_datacenter"` - `"vm_identifier"` - `"vnic_dn"` |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `false` when using a HTTPAPI connection plugin (mso or nd) and `true` when using the legacy connection method (only for mso).  **Choices:**   - `false` - `true` |
| **useg_subnet**  boolean | The uSeg Subnet can only be used when the *attribute_type* is IP.  Use `false` to set the custom uSeg Subnet IP address to the uSeg Attribute.  Use `true` to set the uSeg Subnet IP address to 0.0.0.0.  **Choices:**   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |
| **value**  aliases: attribute_value  string | The value of the uSeg Attribute. |

## [Notes](mso_schema_template_anp_epg_useg_attribute_module.md#id4)

> **Note:**
>
> - Due to restrictions of the MSO REST API concurrent modifications to EPG subnets can be dangerous and corrupt data.
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [Examples](mso_schema_template_anp_epg_useg_attribute_module.md#id5)

```yaml+jinja
- name: Add an uSeg attr with attribute_type - ip
  cisco.mso.mso_schema_template_anp_epg_useg_attribute:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    anp: ANP 1
    epg: EPG 1
    name: useg_attr_ip
    attribute_type: ip
    useg_subnet: false
    value: 10.0.0.0/24
    state: present
  delegate_to: localhost

- name: Query a specific EPG uSeg attr with name
  cisco.mso.mso_schema_template_anp_epg_useg_attribute:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    anp: ANP 1
    epg: EPG 1
    name: useg_attr_ip
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all EPG uSeg attrs
  cisco.mso.mso_schema_template_anp_epg_useg_attribute:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    anp: ANP 1
    epg: EPG 1
    state: query
  delegate_to: localhost
  register: query_result

- name: Remove a uSeg attr from an EPG with name
  cisco.mso.mso_schema_template_anp_epg_useg_attribute:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    anp: ANP 1
    epg: EPG 1
    name: useg_attr_ip
    state: absent
  delegate_to: localhost
```

### Authors

- Sabari Jaganathan (@sajagana)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
- [Homepage](https://cisco.com/go/aci)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

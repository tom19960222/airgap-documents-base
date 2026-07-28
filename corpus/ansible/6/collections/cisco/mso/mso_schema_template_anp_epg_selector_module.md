---
collection: ansible
version: "6"
title: "cisco.mso.mso_schema_template_anp_epg_selector module – Manage EPG selector in schema templates"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/mso/mso_schema_template_anp_epg_selector_module.html
fetched_at: 2026-07-27T17:01:10+00:00
---
# cisco.mso.mso_schema_template_anp_epg_selector module – Manage EPG selector in schema templates

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
> see [Requirements](mso_schema_template_anp_epg_selector_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-epg-selector-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_schema_template_anp_epg_selector`.

- [Synopsis](mso_schema_template_anp_epg_selector_module.md#synopsis)
- [Requirements](mso_schema_template_anp_epg_selector_module.md#requirements)
- [Parameters](mso_schema_template_anp_epg_selector_module.md#parameters)
- [Notes](mso_schema_template_anp_epg_selector_module.md#notes)
- [See Also](mso_schema_template_anp_epg_selector_module.md#see-also)
- [Examples](mso_schema_template_anp_epg_selector_module.md#examples)

## [Synopsis](mso_schema_template_anp_epg_selector_module.md#id1)

- Manage EPG selector in schema templates on Cisco ACI Multi-Site.

## [Requirements](mso_schema_template_anp_epg_selector_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_schema_template_anp_epg_selector_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **anp**  string / required | The name of the ANP. |
| **epg**  string / required | The name of the EPG to manage. |
| **expressions**  list / elements=dictionary | Expressions associated to this selector. |
| **operator**  string / required | The operator associated to the expression.  Choices:   - `"not_in"` - `"in"` - `"equals"` - `"not_equals"` - `"has_key"` - `"does_not_have_key"` |
| **type**  aliases: tag  string / required | The name of the expression. |
| **value**  string | The value associated to the expression.  If the operator is in or not_in, the value should be a comma separated str. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  Choices:   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **schema**  string / required | The name of the schema. |
| **selector**  string | The name of the selector. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **template**  string / required | The name of the template to change. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead.  Default: `30` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `no` when using a HTTPAPI connection plugin (mso or nd) and `yes` when using the legacy connection method (only for mso).  Choices:   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |

## [Notes](mso_schema_template_anp_epg_selector_module.md#id4)

> **Note:**
>
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [See Also](mso_schema_template_anp_epg_selector_module.md#id5)

> **See also:**
>
> [cisco.mso.mso_schema_template_anp_epg](mso_schema_template_anp_epg_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-epg-module)
> :   Manage Endpoint Groups (EPGs) in schema templates.

## [Examples](mso_schema_template_anp_epg_selector_module.md#id6)

```yaml+jinja
- name: Add a selector to an EPG
  cisco.mso.mso_schema_template_anp_epg_selector:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    anp: ANP 1
    epg: EPG 1
    selector: selector_1
    expressions:
      - type: expression_1
        operator: in
        value: test
    state: present
  delegate_to: localhost

- name: Remove a Selector
  cisco.mso.mso_schema_template_anp_epg_selector:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    anp: ANP 1
    epg: EPG 1
    selector: selector_1
    state: absent
  delegate_to: localhost

- name: Query a specific Selector
  cisco.mso.mso_schema_template_anp_epg_selector:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    anp: ANP 1
    epg: EPG 1
    selector: selector_1
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all Selectors
  cisco.mso.mso_schema_template_anp_epg_selector:
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
```

### Authors

- Cindy Zhao (@cizhao)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
[Homepage](https://cisco.com/go/aci)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

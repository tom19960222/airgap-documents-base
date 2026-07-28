---
collection: ansible
version: "8"
title: "cisco.mso.mso_schema_template_external_epg module – Manage external EPGs in schema templates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/mso/mso_schema_template_external_epg_module.html
fetched_at: 2026-07-28T01:38:08+00:00
---
# cisco.mso.mso_schema_template_external_epg module – Manage external EPGs in schema templates

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
> see [Requirements](mso_schema_template_external_epg_module.md#ansible-collections-cisco-mso-mso-schema-template-external-epg-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_schema_template_external_epg`.

- [Synopsis](mso_schema_template_external_epg_module.md#synopsis)
- [Requirements](mso_schema_template_external_epg_module.md#requirements)
- [Parameters](mso_schema_template_external_epg_module.md#parameters)
- [Notes](mso_schema_template_external_epg_module.md#notes)
- [Examples](mso_schema_template_external_epg_module.md#examples)

## [Synopsis](mso_schema_template_external_epg_module.md#id1)

- Manage external EPGs in schema templates on Cisco ACI Multi-Site.

Aliases: mso_schema_template_externalepg

## [Requirements](mso_schema_template_external_epg_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_schema_template_external_epg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **anp**  dictionary | The anp associated with the external epg. |
| **name**  string / required | The name of the anp to associate with. |
| **schema**  string | The schema that defines the referenced anp.  If this parameter is unspecified, it defaults to the current schema. |
| **template**  string | The template that defines the referenced anp.  If this parameter is unspecified, it defaults to the current template. |
| **description**  string | The description of external EPG is supported on versions of MSO that are 3.3 or greater. |
| **display_name**  string | The name as displayed on the MSO web interface. |
| **external_epg**  aliases: name, externalepg  string | The name of the external EPG to manage. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **l3out**  dictionary | The L3Out associated with the external epg. |
| **name**  string / required | The name of the L3Out to associate with. |
| **schema**  string | The schema that defines the referenced L3Out.  If this parameter is unspecified, it defaults to the current schema. |
| **template**  string | The template that defines the referenced L3Out.  If this parameter is unspecified, it defaults to the current template. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_login_domain` will be used if this attribute is not specified. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **preferred_group**  boolean | Preferred Group is enabled for this External EPG or not.  **Choices:**   - `false` - `true` |
| **schema**  string / required | The name of the schema. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **template**  string / required | The name of the template. |
| **timeout**  integer | The socket level timeout in seconds.  The default value is 30 seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead. |
| **type**  string | The type of external epg.  anp needs to be associated with external epg when the type is cloud.  l3out can be associated with external epg when the type is on-premise.  **Choices:**   - `"on-premise"` ← (default) - `"cloud"` |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `false` when using a HTTPAPI connection plugin (mso or nd) and `true` when using the legacy connection method (only for mso).  **Choices:**   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |
| **vrf**  dictionary | The VRF associated with the external epg. |
| **name**  string / required | The name of the VRF to associate with. |
| **schema**  string | The schema that defines the referenced VRF.  If this parameter is unspecified, it defaults to the current schema. |
| **template**  string | The template that defines the referenced VRF.  If this parameter is unspecified, it defaults to the current template. |

## [Notes](mso_schema_template_external_epg_module.md#id4)

> **Note:**
>
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [Examples](mso_schema_template_external_epg_module.md#id5)

```yaml+jinja
- name: Add a new external EPG
  cisco.mso.mso_schema_template_external_epg:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    external_epg: External EPG 1
    vrf:
      name: VRF
      schema: Schema 1
      template: Template 1
    state: present
  delegate_to: localhost

- name: Add a new external EPG with external epg in cloud
  cisco.mso.mso_schema_template_external_epg:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    external_epg: External EPG 1
    type: cloud
    vrf:
      name: VRF
      schema: Schema 1
      template: Template 1
    anp:
      name: ANP1
      schema: Schema 1
      template: Template 1
    state: present
  delegate_to: localhost

- name: Remove an external EPG
  cisco.mso.mso_schema_template_external_epg:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    external_epg: external EPG1
    state: absent
  delegate_to: localhost

- name: Query a specific external EPGs
  cisco.mso.mso_schema_template_external_epg:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    external_epg: external EPG1
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all external EPGs
  cisco.mso.mso_schema_template_external_epg:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
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

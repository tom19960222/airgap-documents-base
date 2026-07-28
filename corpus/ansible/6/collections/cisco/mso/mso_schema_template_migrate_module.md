---
collection: ansible
version: "6"
title: "cisco.mso.mso_schema_template_migrate module – Migrate Bridge Domains (BDs) and EPGs between templates"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/mso/mso_schema_template_migrate_module.html
fetched_at: 2026-07-27T17:01:21+00:00
---
# cisco.mso.mso_schema_template_migrate module – Migrate Bridge Domains (BDs) and EPGs between templates

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
> see [Requirements](mso_schema_template_migrate_module.md#ansible-collections-cisco-mso-mso-schema-template-migrate-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_schema_template_migrate`.

- [Synopsis](mso_schema_template_migrate_module.md#synopsis)
- [Requirements](mso_schema_template_migrate_module.md#requirements)
- [Parameters](mso_schema_template_migrate_module.md#parameters)
- [Notes](mso_schema_template_migrate_module.md#notes)
- [Examples](mso_schema_template_migrate_module.md#examples)

## [Synopsis](mso_schema_template_migrate_module.md#id1)

- Migrate BDs and EPGs between templates of same and different schemas.

## [Requirements](mso_schema_template_migrate_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_schema_template_migrate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bds**  list / elements=string | The name of the BDs to migrate. |
| **epgs**  list / elements=dictionary | The name of the EPGs and the ANP it is in to migrate. |
| **anp**  string / required | The name of the anp to migrate. |
| **epg**  string / required | The name of the EPG to migrate. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  Choices:   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **schema**  string / required | The name of the schema. |
| **state**  string | Use `present` for adding.  Default: `"present"` |
| **target_schema**  string / required | The name of the target_schema. |
| **target_template**  string / required | The name of the target_template. |
| **template**  string / required | The name of the template. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead.  Default: `30` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `no` when using a HTTPAPI connection plugin (mso or nd) and `yes` when using the legacy connection method (only for mso).  Choices:   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |

## [Notes](mso_schema_template_migrate_module.md#id4)

> **Note:**
>
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [Examples](mso_schema_template_migrate_module.md#id5)

```yaml+jinja
- name: Migration of objects between templates of same schema
  mso_schema_template_migrate:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    target_schema: Schema 1
    target_template: Template 2
    bds:
    - BD
    epgs:
    - epg: EPG1
      anp: ANP
    state: present
  delegate_to: localhost

- name: Migration of objects between templates of different schema
  mso_schema_template_migrate:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    target_schema: Schema 2
    target_template: Template 2
    bds:
    - BD
    epgs:
    - epg: EPG1
      anp: ANP
    state: present
  delegate_to: localhost

- name: Migration of BD object between templates of same schema
  mso_schema_template_migrate:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    target_schema: Schema 1
    target_template: Template 2
    bds:
    - BD
    - BD1
    state: present
  delegate_to: localhost

- name: Migration of BD object between templates of different schema
  mso_schema_template_migrate:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    target_schema: Schema 2
    target_template: Template 2
    bds:
    - BD
    - BD1
    state: present
  delegate_to: localhost

- name: Migration of EPG objects between templates of same schema
  mso_schema_template_migrate:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    target_schema: Schema 2
    target_template: Template 2
    epgs:
    - epg: EPG1
      anp: ANP
    - epg: EPG2
      anp: ANP2
    state: present
  delegate_to: localhost

- name: Migration of EPG objects between templates of different schema
  mso_schema_template_migrate:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    target_schema: Schema 2
    target_template: Template 2
    epgs:
    - epg: EPG1
      anp: ANP
    - epg: EPG2
      anp: ANP2
    state: present
  delegate_to: localhost
```

### Authors

- Anvitha Jain (@anvitha-jain)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
[Homepage](https://cisco.com/go/aci)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

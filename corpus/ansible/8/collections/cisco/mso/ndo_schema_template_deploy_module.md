---
collection: ansible
version: "8"
title: "cisco.mso.ndo_schema_template_deploy module – Deploy schema templates to sites for NDO v3.7 and higher"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/mso/ndo_schema_template_deploy_module.html
fetched_at: 2026-07-28T01:38:20+00:00
---
# cisco.mso.ndo_schema_template_deploy module – Deploy schema templates to sites for NDO v3.7 and higher

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
> see [Requirements](ndo_schema_template_deploy_module.md#ansible-collections-cisco-mso-ndo-schema-template-deploy-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.ndo_schema_template_deploy`.

- [Synopsis](ndo_schema_template_deploy_module.md#synopsis)
- [Requirements](ndo_schema_template_deploy_module.md#requirements)
- [Parameters](ndo_schema_template_deploy_module.md#parameters)
- [Notes](ndo_schema_template_deploy_module.md#notes)
- [See Also](ndo_schema_template_deploy_module.md#see-also)
- [Examples](ndo_schema_template_deploy_module.md#examples)

## [Synopsis](ndo_schema_template_deploy_module.md#id1)

- Deploy schema templates to sites.
- Prior to deploy or redeploy a schema validation is executed.
- When schema validation fails, [cisco.mso.ndo_schema_template_deploy](ndo_schema_template_deploy_module.md#ansible-collections-cisco-mso-ndo-schema-template-deploy-module) fails and deploy or redeploy will not be executed.
- Only supports NDO v3.7 and higher

## [Requirements](ndo_schema_template_deploy_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](ndo_schema_template_deploy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_login_domain` will be used if this attribute is not specified. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **schema**  string / required | The name of the schema. |
| **sites**  list / elements=string | The name of the site(s). |
| **state**  string | Use `deploy` to deploy schema template.  Use `redeploy` to redeploy schema template.  Use `undeploy` to undeploy schema template from a site.  Use `query` to get deployment status.  **Choices:**   - `"deploy"` ← (default) - `"redeploy"` - `"undeploy"` - `"query"` |
| **template**  string / required | The name of the template. |
| **timeout**  integer | The socket level timeout in seconds.  The default value is 30 seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead. |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `false` when using a HTTPAPI connection plugin (mso or nd) and `true` when using the legacy connection method (only for mso).  **Choices:**   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |

## [Notes](ndo_schema_template_deploy_module.md#id4)

> **Note:**
>
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [See Also](ndo_schema_template_deploy_module.md#id5)

> **See also:**
>
> [cisco.mso.mso_schema_site](mso_schema_site_module.md#ansible-collections-cisco-mso-mso-schema-site-module)
> :   Manage sites in schemas.
>
> [cisco.mso.mso_schema_template](mso_schema_template_module.md#ansible-collections-cisco-mso-mso-schema-template-module)
> :   Manage templates in schemas.

## [Examples](ndo_schema_template_deploy_module.md#id6)

```yaml+jinja
- name: Deploy a schema template
  cisco.mso.ndo_schema_template_deploy:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    state: deploy
  delegate_to: localhost

- name: Redeploy a schema template
  cisco.mso.ndo_schema_template_deploy:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    state: redeploy
  delegate_to: localhost

- name: Undeploy a schema template
  cisco.mso.ndo_schema_template_deploy:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    sites: [ Site1, Site2 ]
    state: undeploy
  delegate_to: localhost

- name: Query a schema template deploy status
  cisco.mso.ndo_schema_template_deploy:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    state: query
  delegate_to: localhost
```

### Authors

- Akini Ross (@akinross)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
- [Homepage](https://cisco.com/go/aci)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

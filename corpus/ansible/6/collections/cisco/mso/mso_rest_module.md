---
collection: ansible
version: "6"
title: "cisco.mso.mso_rest module – Direct access to the Cisco MSO REST API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/mso/mso_rest_module.html
fetched_at: 2026-07-27T17:00:50+00:00
---
# cisco.mso.mso_rest module – Direct access to the Cisco MSO REST API

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
> see [Requirements](mso_rest_module.md#ansible-collections-cisco-mso-mso-rest-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_rest`.

- [Synopsis](mso_rest_module.md#synopsis)
- [Requirements](mso_rest_module.md#requirements)
- [Parameters](mso_rest_module.md#parameters)
- [Notes](mso_rest_module.md#notes)
- [See Also](mso_rest_module.md#see-also)
- [Examples](mso_rest_module.md#examples)

## [Synopsis](mso_rest_module.md#id1)

- Enables the management of the Cisco MSO fabric through direct access to the Cisco MSO REST API.
- This module is not idempotent and does not report changes.

## [Requirements](mso_rest_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_rest_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content**  aliases: payload  any | Sets the payload of the API request directly.  This may be convenient to template simple requests.  For anything complex use the `template` lookup plugin (see examples). |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead. |
| **method**  aliases: action  string | The HTTP method of the request.  Using `delete` is typically used for deleting objects.  Using `get` is typically used for querying objects.  Using `post` is typically used for modifying objects.  Using `put` is typically used for modifying existing objects.  Using `patch` is typically also used for modifying existing objects.  Choices:   - `"delete"` - `"get"` ← (default) - `"post"` - `"put"` - `"patch"` |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  Choices:   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **path**  aliases: uri  string / required | URI being used to execute API calls. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead.  Default: `30` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `no` when using a HTTPAPI connection plugin (mso or nd) and `yes` when using the legacy connection method (only for mso).  Choices:   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |

## [Notes](mso_rest_module.md#id4)

> **Note:**
>
> - Most payloads are known not to be idempotent, so be careful when constructing payloads.
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [See Also](mso_rest_module.md#id5)

> **See also:**
>
> [cisco.mso.mso_tenant](mso_tenant_module.md#ansible-collections-cisco-mso-mso-tenant-module)
> :   Manage tenants.

## [Examples](mso_rest_module.md#id6)

```yaml+jinja
- name: Add schema (JSON)
  cisco.mso.mso_rest:
    host: mso
    username: admin
    password: SomeSecretPassword
    path: /mso/api/v1/schemas
    method: post
    content:
      {
          "displayName": "{{ mso_schema | default('ansible_test') }}",
          "templates": [{
              "name": "Template_1",
              "tenantId": "{{ add_tenant.jsondata.id }}",
              "displayName": "Template_1",
              "templateSubType": [],
              "templateType": "stretched-template",
              "anps": [],
              "contracts": [],
              "vrfs": [],
              "bds": [],
              "filters": [],
              "externalEpgs": [],
              "serviceGraphs": [],
              "intersiteL3outs": []
          }],
          "sites": [],
          "_updateVersion": 0
      }
  delegate_to: localhost

- name: Query schema
  cisco.mso.mso_rest:
    host: mso
    username: admin
    password: SomeSecretPassword
    path: /mso/api/v1/schemas
    method: get
  delegate_to: localhost

- name: Patch schema (YAML)
  cisco.mso.mso_rest:
    host: mso
    username: admin
    password: SomeSecretPassword
    path: "/mso/api/v1/schemas/{{ add_schema.jsondata.id }}"
    method: patch
    content:
      - op: add
        path: /templates/Template_1/anps/-
        value:
          name: AP2
          displayName: AP2
          epgs: []
        _updateVersion: 0
  delegate_to: localhost

- name: Add a tenant from a templated payload file from templates
  cisco.mso.mso_rest:
    host: mso
    username: admin
    password: SomeSecretPassword
    method: post
    path: /api/v1/tenants
    content: "{{ lookup('template', 'mso/tenant.json.j2') }}"
  delegate_to: localhost
```

### Authors

- Anvitha Jain (@anvitha-jain)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
[Homepage](https://cisco.com/go/aci)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

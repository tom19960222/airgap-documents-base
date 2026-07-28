---
collection: ansible
version: "8"
title: "cisco.mso.mso_schema_site_anp_epg_bulk_staticport module – Manage site-local EPG static ports in bulk in schema template"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/mso/mso_schema_site_anp_epg_bulk_staticport_module.html
fetched_at: 2026-07-28T01:37:44+00:00
---
# cisco.mso.mso_schema_site_anp_epg_bulk_staticport module – Manage site-local EPG static ports in bulk in schema template

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
> see [Requirements](mso_schema_site_anp_epg_bulk_staticport_module.md#ansible-collections-cisco-mso-mso-schema-site-anp-epg-bulk-staticport-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_schema_site_anp_epg_bulk_staticport`.

- [Synopsis](mso_schema_site_anp_epg_bulk_staticport_module.md#synopsis)
- [Requirements](mso_schema_site_anp_epg_bulk_staticport_module.md#requirements)
- [Parameters](mso_schema_site_anp_epg_bulk_staticport_module.md#parameters)
- [Notes](mso_schema_site_anp_epg_bulk_staticport_module.md#notes)
- [See Also](mso_schema_site_anp_epg_bulk_staticport_module.md#see-also)
- [Examples](mso_schema_site_anp_epg_bulk_staticport_module.md#examples)

## [Synopsis](mso_schema_site_anp_epg_bulk_staticport_module.md#id1)

- Manage site-local EPG static ports in bulk in schema template on Cisco ACI Multi-Site.

## [Requirements](mso_schema_site_anp_epg_bulk_staticport_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_schema_site_anp_epg_bulk_staticport_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **anp**  string / required | The name of the ANP. |
| **deployment_immediacy**  string | The deployment immediacy of the static port.  `immediate` means **Deploy immediate**.  `lazy` means **deploy on demand**.  **Choices:**   - `"immediate"` - `"lazy"` ← (default) |
| **epg**  string / required | The name of the EPG. |
| **fex**  string | The fex id of the static port. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **leaf**  string | The leaf of the static port. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_login_domain` will be used if this attribute is not specified. |
| **mode**  string | The mode of the static port.  `native` means **Access (802.1p**).  `regular` means **Trunk**.  `untagged` means **Access (untagged**).  **Choices:**   - `"native"` - `"regular"` - `"untagged"` ← (default) |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **path**  string | The path of the static port. |
| **pod**  string | The pod of the static port. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **primary_micro_segment_vlan**  integer | Primary micro-seg VLAN of static port. |
| **schema**  string / required | The name of the schema. |
| **site**  string / required | The name of the site. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **static_ports**  list / elements=dictionary | List of static port configurations and elements in the form of a dictionary.  Module level attributes will be overridden by the path level attributes.  Making changes to an item in the list will update the whole payload. |
| **deployment_immediacy**  string | The deployment immediacy of the static port.  `immediate` means **Deploy immediate**.  `lazy` means **deploy on demand**.  **Choices:**   - `"immediate"` - `"lazy"` |
| **fex**  string | The fex id of the static port. |
| **leaf**  string | The leaf of the static port. |
| **mode**  string | The mode of the static port.  `native` means **Access (802.1p**).  `regular` means **Trunk**.  `untagged` means **Access (untagged**).  **Choices:**   - `"native"` - `"regular"` - `"untagged"` |
| **path**  string | The path of the static port.  Path has to be unique for each static port in a particular leaf. |
| **pod**  string | The pod of the static port. |
| **primary_micro_segment_vlan**  integer | Primary micro-seg VLAN of the static port. |
| **type**  string | The path type of the static port  vpc is used for a Virtual Port Channel  dpc is used for a Direct Port Channel  port is used for a single interface  **Choices:**   - `"port"` - `"vpc"` - `"dpc"` |
| **vlan**  integer | The port encap VLAN id of the static port. |
| **template**  string / required | The name of the template. |
| **timeout**  integer | The socket level timeout in seconds.  The default value is 30 seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead. |
| **type**  string | The path type of the static port  vpc is used for a Virtual Port Channel  dpc is used for a Direct Port Channel  port is used for a single interface  **Choices:**   - `"port"` ← (default) - `"vpc"` - `"dpc"` |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `false` when using a HTTPAPI connection plugin (mso or nd) and `true` when using the legacy connection method (only for mso).  **Choices:**   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |
| **vlan**  integer | The port encap VLAN id of the static port. |

## [Notes](mso_schema_site_anp_epg_bulk_staticport_module.md#id4)

> **Note:**
>
> - The ACI MultiSite PATCH API has a deficiency requiring some objects to be referenced by index. This can cause silent corruption on concurrent access when changing/removing an object as the wrong object may be referenced. This module is affected by this deficiency.
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [See Also](mso_schema_site_anp_epg_bulk_staticport_module.md#id5)

> **See also:**
>
> [cisco.mso.mso_schema_site_anp_epg](mso_schema_site_anp_epg_module.md#ansible-collections-cisco-mso-mso-schema-site-anp-epg-module)
> :   Manage site-local Endpoint Groups (EPGs) in schema template.
>
> [cisco.mso.mso_schema_template_anp_epg](mso_schema_template_anp_epg_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-epg-module)
> :   Manage Endpoint Groups (EPGs) in schema templates.

## [Examples](mso_schema_site_anp_epg_bulk_staticport_module.md#id6)

```yaml+jinja
- name: Add a new static port to a site EPG
  cisco.mso.mso_schema_site_anp_epg_bulk_staticport:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    anp: ANP1
    epg: EPG1
    type: port
    pod: pod-1
    leaf: 101
    path: eth1/1
    vlan: 126
    deployment_immediacy: immediate
    static_ports:
      - path: eth1/2
        leaf: 102
      - path: eth1/3
        vlan: 124
    state: present
  delegate_to: localhost

- name: Add a new static fex port to a site EPG
  cisco.mso.mso_schema_site_anp_epg_bulk_staticport:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    anp: ANP1
    epg: EPG1
    type: port
    pod: pod-1
    leaf: 101
    path: eth1/1
    vlan: 126
    deployment_immediacy: lazy
    static_ports:
      - path: eth1/2
        leaf: 102
      - path: eth1/3
        vlan: 124
      - fex: 151
    state: present
  delegate_to: localhost

- name: Add a new static VPC to a site EPG
  cisco.mso.mso_schema_site_anp_epg_bulk_staticport:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    anp: ANP1
    epg: EPG1
    type: port
    pod: pod-1
    leaf: 101
    path: eth1/1
    vlan: 126
    static_ports:
      - path: eth1/2
        leaf: 102
      - path: eth1/3
        vlan: 124
      - fex: 151
      - leaf: 101-102
        path: ansible_polgrp
        vlan: 127
        type: vpc
        mode: untagged
        deployment_immediacy: lazy
    state: present
  delegate_to: localhost

- name: Remove static ports from a site EPG
  cisco.mso.mso_schema_site_anp_epg_bulk_staticport:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    anp: ANP1
    epg: EPG1
    state: absent
  delegate_to: localhost

- name: Query all site EPG static ports
  cisco.mso.mso_schema_site_anp_epg_bulk_staticport:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    anp: ANP1
    state: query
  delegate_to: localhost
  register: query_result
```

### Authors

- Anvitha Jain (@anvjain)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
- [Homepage](https://cisco.com/go/aci)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

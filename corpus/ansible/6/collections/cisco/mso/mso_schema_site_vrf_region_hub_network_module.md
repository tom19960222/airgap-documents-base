---
collection: ansible
version: "6"
title: "cisco.mso.mso_schema_site_vrf_region_hub_network module – Manage site-local VRF region hub network in schema template"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/mso/mso_schema_site_vrf_region_hub_network_module.html
fetched_at: 2026-07-27T17:01:06+00:00
---
# cisco.mso.mso_schema_site_vrf_region_hub_network module – Manage site-local VRF region hub network in schema template

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
> see [Requirements](mso_schema_site_vrf_region_hub_network_module.md#ansible-collections-cisco-mso-mso-schema-site-vrf-region-hub-network-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_schema_site_vrf_region_hub_network`.

- [Synopsis](mso_schema_site_vrf_region_hub_network_module.md#synopsis)
- [Requirements](mso_schema_site_vrf_region_hub_network_module.md#requirements)
- [Parameters](mso_schema_site_vrf_region_hub_network_module.md#parameters)
- [Notes](mso_schema_site_vrf_region_hub_network_module.md#notes)
- [See Also](mso_schema_site_vrf_region_hub_network_module.md#see-also)
- [Examples](mso_schema_site_vrf_region_hub_network_module.md#examples)

## [Synopsis](mso_schema_site_vrf_region_hub_network_module.md#id1)

- Manage site-local VRF region hub network in schema template on Cisco ACI Multi-Site.
- The ‘Hub Network’ feature was introduced in Multi-Site Orchestrator (MSO) version 3.0(1) for AWS and version 3.0(2) for Azure.

## [Requirements](mso_schema_site_vrf_region_hub_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_schema_site_vrf_region_hub_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **hub_network**  dictionary | The hub network to be managed. |
| **name**  string / required | The name of the hub network.  The hub-default is the default created hub network. |
| **tenant**  string / required | The tenant name of the hub network. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  Choices:   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **region**  string / required | The name of the region. |
| **schema**  string / required | The name of the schema. |
| **site**  string / required | The name of the site. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **template**  string / required | The name of the template. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead.  Default: `30` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `no` when using a HTTPAPI connection plugin (mso or nd) and `yes` when using the legacy connection method (only for mso).  Choices:   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **vrf**  string / required | The name of the VRF. |

## [Notes](mso_schema_site_vrf_region_hub_network_module.md#id4)

> **Note:**
>
> - The ACI MultiSite PATCH API has a deficiency requiring some objects to be referenced by index. This can cause silent corruption on concurrent access when changing/removing on object as the wrong object may be referenced. This module is affected by this deficiency.
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [See Also](mso_schema_site_vrf_region_hub_network_module.md#id5)

> **See also:**
>
> [cisco.mso.mso_schema_site_vrf_region](mso_schema_site_vrf_region_module.md#ansible-collections-cisco-mso-mso-schema-site-vrf-region-module)
> :   Manage site-local VRF regions in schema template.
>
> [cisco.mso.mso_schema_template_vrf](mso_schema_template_vrf_module.md#ansible-collections-cisco-mso-mso-schema-template-vrf-module)
> :   Manage VRFs in schema templates.

## [Examples](mso_schema_site_vrf_region_hub_network_module.md#id6)

```yaml+jinja
- name: Add a new site VRF region hub network
  cisco.mso.mso_schema_site_vrf_region_hub_network:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    vrf: VRF1
    region: us-west-1
    hub_network:
      name: hub-default
      tenant: infra
    state: present
  delegate_to: localhost

- name: Remove a site VRF region hub network
  cisco.mso.mso_schema_site_vrf_region_hub_network:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    vrf: VRF1
    state: absent
  delegate_to: localhost

- name: Query site VRF region hub network
  cisco.mso.mso_schema_site_vrf_region_hub_network:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    vrf: VRF1
    region: us-west-1
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

---
collection: ansible
version: "6"
title: "cisco.mso.mso_schema_site_vrf_region_cidr_subnet module – Manage site-local VRF regions in schema template"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/mso/mso_schema_site_vrf_region_cidr_subnet_module.html
fetched_at: 2026-07-27T17:01:06+00:00
---
# cisco.mso.mso_schema_site_vrf_region_cidr_subnet module – Manage site-local VRF regions in schema template

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
> see [Requirements](mso_schema_site_vrf_region_cidr_subnet_module.md#ansible-collections-cisco-mso-mso-schema-site-vrf-region-cidr-subnet-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_schema_site_vrf_region_cidr_subnet`.

- [Synopsis](mso_schema_site_vrf_region_cidr_subnet_module.md#synopsis)
- [Requirements](mso_schema_site_vrf_region_cidr_subnet_module.md#requirements)
- [Parameters](mso_schema_site_vrf_region_cidr_subnet_module.md#parameters)
- [Notes](mso_schema_site_vrf_region_cidr_subnet_module.md#notes)
- [See Also](mso_schema_site_vrf_region_cidr_subnet_module.md#see-also)
- [Examples](mso_schema_site_vrf_region_cidr_subnet_module.md#examples)

## [Synopsis](mso_schema_site_vrf_region_cidr_subnet_module.md#id1)

- Manage site-local VRF regions in schema template on Cisco ACI Multi-Site.

## [Requirements](mso_schema_site_vrf_region_cidr_subnet_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_schema_site_vrf_region_cidr_subnet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cidr**  string / required | The IP range of for the region CIDR. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **hosted_vrf**  string | The name of hosted vrf associated with region CIDR subnet.  This is supported on versions of MSO that are 3.3 or greater. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  Choices:   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **private_link_label**  string | The private link label used to represent this subnet.  This parameter is available for MSO version greater than 3.3. |
| **region**  string / required | The name of the region. |
| **schema**  string / required | The name of the schema. |
| **site**  string / required | The name of the site. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **subnet**  aliases: ip  string | The IP subnet of this region CIDR. |
| **template**  string / required | The name of the template. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead.  Default: `30` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `no` when using a HTTPAPI connection plugin (mso or nd) and `yes` when using the legacy connection method (only for mso).  Choices:   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **vgw**  aliases: hub_network  boolean | Whether this subnet is used for the Azure Gateway in Azure.  Whether this subnet is used for the Transit Gateway Attachment in AWS.  Choices:   - `false` - `true` |
| **vrf**  string / required | The name of the VRF. |
| **zone**  aliases: name  string | The name of the zone for the region CIDR subnet.  This argument is required for AWS sites. |

## [Notes](mso_schema_site_vrf_region_cidr_subnet_module.md#id4)

> **Note:**
>
> - The ACI MultiSite PATCH API has a deficiency requiring some objects to be referenced by index. This can cause silent corruption on concurrent access when changing/removing on object as the wrong object may be referenced. This module is affected by this deficiency.
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [See Also](mso_schema_site_vrf_region_cidr_subnet_module.md#id5)

> **See also:**
>
> [cisco.mso.mso_schema_site_vrf_region_cidr](mso_schema_site_vrf_region_cidr_module.md#ansible-collections-cisco-mso-mso-schema-site-vrf-region-cidr-module)
> :   Manage site-local VRF region CIDRs in schema template.
>
> [cisco.mso.mso_schema_template_vrf](mso_schema_template_vrf_module.md#ansible-collections-cisco-mso-mso-schema-template-vrf-module)
> :   Manage VRFs in schema templates.

## [Examples](mso_schema_site_vrf_region_cidr_subnet_module.md#id6)

```yaml+jinja
- name: Add a new site VRF region CIDR subnet
  cisco.mso.mso_schema_site_vrf_region_cidr_subnet:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    vrf: VRF1
    region: us-west-1
    cidr: 14.14.14.1/24
    subnet: 14.14.14.2/24
    zone: us-west-1a
    state: present
  delegate_to: localhost

- name: Remove a site VRF region CIDR subnet
  cisco.mso.mso_schema_site_vrf_region_cidr_subnet:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    vrf: VRF1
    region: us-west-1
    cidr: 14.14.14.1/24
    subnet: 14.14.14.2/24
    state: absent
  delegate_to: localhost

- name: Query a specific site VRF region CIDR subnet
  cisco.mso.mso_schema_site_vrf_region_cidr_subnet:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    vrf: VRF1
    region: us-west-1
    cidr: 14.14.14.1/24
    subnet: 14.14.14.2/24
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all site VRF region CIDR subnet
  cisco.mso.mso_schema_site_vrf_region_cidr_subnet:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    vrf: VRF1
    region: us-west-1
    cidr: 14.14.14.1/24
    state: query
  delegate_to: localhost
  register: query_result
```

### Authors

- Dag Wieers (@dagwieers)
- Lionel Hercot (@lhercot)
- Anvitha Jain (@anvitha-jain)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
[Homepage](https://cisco.com/go/aci)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

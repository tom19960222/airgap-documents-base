---
collection: ansible
version: "6"
title: "cisco.mso.mso_schema_template_anp_epg module – Manage Endpoint Groups (EPGs) in schema templates"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/mso/mso_schema_template_anp_epg_module.html
fetched_at: 2026-07-27T17:01:09+00:00
---
# cisco.mso.mso_schema_template_anp_epg module – Manage Endpoint Groups (EPGs) in schema templates

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
> see [Requirements](mso_schema_template_anp_epg_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-epg-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_schema_template_anp_epg`.

- [Synopsis](mso_schema_template_anp_epg_module.md#synopsis)
- [Requirements](mso_schema_template_anp_epg_module.md#requirements)
- [Parameters](mso_schema_template_anp_epg_module.md#parameters)
- [Notes](mso_schema_template_anp_epg_module.md#notes)
- [See Also](mso_schema_template_anp_epg_module.md#see-also)
- [Examples](mso_schema_template_anp_epg_module.md#examples)

## [Synopsis](mso_schema_template_anp_epg_module.md#id1)

- Manage EPGs in schema templates on Cisco ACI Multi-Site.

## [Requirements](mso_schema_template_anp_epg_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_schema_template_anp_epg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_type**  string | This parameter indicates how the service will be accessed.  It is only available when epg_type is service.  Choices:   - `"private"` - `"public"` - `"public_and_private"` |
| **anp**  string / required | The name of the ANP. |
| **bd**  dictionary | The BD associated to this ANP. |
| **name**  string / required | The name of the BD to associate with. |
| **schema**  string | The schema that defines the referenced BD.  If this parameter is unspecified, it defaults to the current schema. |
| **template**  string | The template that defines the referenced BD. |
| **deployment_type**  string | The deployment_type parameter indicates how and where the service is deployed.  This parameter is available only when epg_type is service.  Choices:   - `"cloud_native"` - `"cloud_native_managed"` - `"third_party"` |
| **description**  string | The description as displayed on the MSO web interface.  The description is supported on versions of MSO that are 3.3 or greater. |
| **display_name**  string | The name as displayed on the MSO web interface. |
| **epg**  aliases: name  string | The name of the EPG to manage. |
| **epg_type**  string | The EPG type parameter is supported on versions of MSO that are 3.3 or greater.  Choices:   - `"application"` - `"service"` |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **intersite_multicast_source**  boolean | Whether intersite multicast source is enabled.  When not specified, this parameter defaults to `no`.  Choices:   - `false` - `true` |
| **intra_epg_isolation**  string | Whether intra EPG isolation is enforced.  When not specified, this parameter defaults to `unenforced`.  Choices:   - `"enforced"` - `"unenforced"` |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  Choices:   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **preferred_group**  boolean | Whether this EPG is added to preferred group or not.  When not specified, this parameter defaults to `no`.  Choices:   - `false` - `true` |
| **proxy_arp**  boolean | Whether proxy arp is enabled.  When not specified, this parameter defaults to `no`.  Choices:   - `false` - `true` |
| **qos_level**  string | Quality of Service (QoS) allows you to classify the network traffic in the fabric.  It helps prioritize and police the traffic flow to help avoid congestion in the network.  The Contract QoS Level parameter is supported on versions of MSO that are 3.1 or greater. |
| **schema**  string / required | The name of the schema. |
| **service_type**  string | The service_type parameter refers to the type of cloud services.  Only certain deployment types, and certain access types within each deployment type, are supported for each service type.  This parameter is available only when epg_type is service. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **subnets**  list / elements=dictionary | The subnets associated to this ANP. |
| **description**  string | The description of this subnet. |
| **no_default_gateway**  boolean | Whether this subnet has a default gateway.  Choices:   - `false` ← (default) - `true` |
| **scope**  string | The scope of the subnet.  Choices:   - `"private"` ← (default) - `"public"` |
| **shared**  boolean | Whether this subnet is shared between VRFs.  Choices:   - `false` ← (default) - `true` |
| **subnet**  aliases: ip  string / required | The IP range in CIDR notation. |
| **template**  string / required | The name of the template. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead.  Default: `30` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `no` when using a HTTPAPI connection plugin (mso or nd) and `yes` when using the legacy connection method (only for mso).  Choices:   - `false` - `true` |
| **useg_epg**  boolean | Whether this is a USEG EPG.  Choices:   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **vrf**  dictionary | The VRF associated to this ANP. |
| **name**  string / required | The name of the VRF to associate with. |
| **schema**  string | The schema that defines the referenced VRF.  If this parameter is unspecified, it defaults to the current schema. |
| **template**  string | The template that defines the referenced VRF. |

## [Notes](mso_schema_template_anp_epg_module.md#id4)

> **Note:**
>
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [See Also](mso_schema_template_anp_epg_module.md#id5)

> **See also:**
>
> [cisco.mso.mso_schema_template_anp](mso_schema_template_anp_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-module)
> :   Manage Application Network Profiles (ANPs) in schema templates.
>
> [cisco.mso.mso_schema_template_anp_epg_subnet](mso_schema_template_anp_epg_subnet_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-epg-subnet-module)
> :   Manage EPG subnets in schema templates.
>
> [cisco.mso.mso_schema_template_bd](mso_schema_template_bd_module.md#ansible-collections-cisco-mso-mso-schema-template-bd-module)
> :   Manage Bridge Domains (BDs) in schema templates.
>
> [cisco.mso.mso_schema_template_contract_filter](mso_schema_template_contract_filter_module.md#ansible-collections-cisco-mso-mso-schema-template-contract-filter-module)
> :   Manage contract filters in schema templates.

## [Examples](mso_schema_template_anp_epg_module.md#id6)

```yaml+jinja
- name: Add a new EPG
  cisco.mso.mso_schema_template_anp_epg:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    anp: ANP 1
    epg: EPG 1
    bd:
     name: bd1
    vrf:
     name: vrf1
    state: present
  delegate_to: localhost

- name: Add a new EPG with preferred group.
  cisco.mso.mso_schema_template_anp_epg:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    anp: ANP 1
    epg: EPG 1
    state: present
    preferred_group: yes
  delegate_to: localhost

- name: Remove an EPG
  cisco.mso.mso_schema_template_anp_epg:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    anp: ANP 1
    epg: EPG 1
    bd:
     name: bd1
    vrf:
     name: vrf1
    state: absent
  delegate_to: localhost

- name: Query a specific EPG
  cisco.mso.mso_schema_template_anp_epg:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    anp: ANP 1
    epg: EPG 1
    bd:
     name: bd1
    vrf:
     name: vrf1
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all EPGs
  cisco.mso.mso_schema_template_anp_epg:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    anp: ANP 1
    epg: EPG 1
    bd:
     name: bd1
    vrf:
     name: vrf1
    state: query
  delegate_to: localhost
  register: query_result
```

### Authors

- Dag Wieers (@dagwieers)
- Anvitha Jain (@anvitha-jain)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
[Homepage](https://cisco.com/go/aci)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

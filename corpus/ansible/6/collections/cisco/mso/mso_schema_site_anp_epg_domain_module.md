---
collection: ansible
version: "6"
title: "cisco.mso.mso_schema_site_anp_epg_domain module – Manage site-local EPG domains in schema template"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/mso/mso_schema_site_anp_epg_domain_module.html
fetched_at: 2026-07-27T17:00:55+00:00
---
# cisco.mso.mso_schema_site_anp_epg_domain module – Manage site-local EPG domains in schema template

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
> see [Requirements](mso_schema_site_anp_epg_domain_module.md#ansible-collections-cisco-mso-mso-schema-site-anp-epg-domain-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_schema_site_anp_epg_domain`.

- [Synopsis](mso_schema_site_anp_epg_domain_module.md#synopsis)
- [Requirements](mso_schema_site_anp_epg_domain_module.md#requirements)
- [Parameters](mso_schema_site_anp_epg_domain_module.md#parameters)
- [Notes](mso_schema_site_anp_epg_domain_module.md#notes)
- [See Also](mso_schema_site_anp_epg_domain_module.md#see-also)
- [Examples](mso_schema_site_anp_epg_domain_module.md#examples)

## [Synopsis](mso_schema_site_anp_epg_domain_module.md#id1)

- Manage site-local EPG domains in schema template on Cisco ACI Multi-Site.

## [Requirements](mso_schema_site_anp_epg_domain_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_schema_site_anp_epg_domain_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_micro_segmentation**  boolean | Specifies microsegmentation is enabled or not. This attribute can only be used with vmmDomain domain association.  Choices:   - `false` - `true` |
| **anp**  string / required | The name of the ANP. |
| **deployment_immediacy**  string | The deployment immediacy of the domain.  `immediate` means **Deploy immediate**.  `lazy` means **deploy on demand**.  Choices:   - `"immediate"` - `"lazy"` |
| **domain_association_type**  string | The type of domain to associate.  Choices:   - `"vmmDomain"` - `"l3ExtDomain"` - `"l2ExtDomain"` - `"physicalDomain"` - `"fibreChannelDomain"` |
| **domain_profile**  string | The domain profile name. |
| **enhanced_lagpolicy_dn**  string | Distinguished name of EPG lagpolicy. This attribute can only be used with vmmDomain domain association. |
| **enhanced_lagpolicy_name**  string | EPG enhanced lagpolicy name. This attribute can only be used with vmmDomain domain association. |
| **epg**  string / required | The name of the EPG. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead. |
| **micro_seg_vlan**  integer | Virtual LAN for microsegmentation. This attribute can only be used with vmmDomain domain association. |
| **micro_seg_vlan_type**  string | Virtual LAN type for microsegmentation. This attribute can only be used with vmmDomain domain association.  vlan is currently the only accepted value. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  Choices:   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **port_encap_vlan**  integer | Virtual LAN type for port encap. This attribute can only be used with vmmDomain domain association. |
| **port_encap_vlan_type**  string | Virtual LAN type for port encap. This attribute can only be used with vmmDomain domain association.  vlan is currently the only accepted value. |
| **resolution_immediacy**  string | Determines when the policies should be resolved and available.  Defaults to `lazy` when unset during creation.  Choices:   - `"immediate"` - `"lazy"` - `"pre-provision"` |
| **schema**  string / required | The name of the schema. |
| **site**  string / required | The name of the site. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **switch_type**  string | Which switch type to use with this domain association. This attribute can only be used with vmmDomain domain association. |
| **switching_mode**  string | Which switching mode to use with this domain association. This attribute can only be used with vmmDomain domain association. |
| **template**  string / required | The name of the template. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead.  Default: `30` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `no` when using a HTTPAPI connection plugin (mso or nd) and `yes` when using the legacy connection method (only for mso).  Choices:   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **vlan_encap_mode**  string | Which VLAN enacap mode to use. This attribute can only be used with vmmDomain domain association.  Choices:   - `"static"` - `"dynamic"` |

## [Notes](mso_schema_site_anp_epg_domain_module.md#id4)

> **Note:**
>
> - The ACI MultiSite PATCH API has a deficiency requiring some objects to be referenced by index. This can cause silent corruption on concurrent access when changing/removing on object as the wrong object may be referenced. This module is affected by this deficiency.
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [See Also](mso_schema_site_anp_epg_domain_module.md#id5)

> **See also:**
>
> [cisco.mso.mso_schema_site_anp_epg](mso_schema_site_anp_epg_module.md#ansible-collections-cisco-mso-mso-schema-site-anp-epg-module)
> :   Manage site-local Endpoint Groups (EPGs) in schema template.
>
> [cisco.mso.mso_schema_template_anp_epg](mso_schema_template_anp_epg_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-epg-module)
> :   Manage Endpoint Groups (EPGs) in schema templates.

## [Examples](mso_schema_site_anp_epg_domain_module.md#id6)

```yaml+jinja
- name: Add a new domain to a site EPG
  cisco.mso.mso_schema_site_anp_epg_domain:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    anp: ANP1
    epg: EPG1
    domain_association_type: vmmDomain
    domain_profile: 'VMware-VMM'
    deployment_immediacy: lazy
    resolution_immediacy: pre-provision
    state: present
  delegate_to: localhost

- name: Remove a domain from a site EPG
  cisco.mso.mso_schema_site_anp_epg_domain:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    anp: ANP1
    epg: EPG1
    domain_association_type: vmmDomain
    domain_profile: 'VMware-VMM'
    deployment_immediacy: lazy
    resolution_immediacy: pre-provision
    state: absent
  delegate_to: localhost

- name: Query a domain associated with a specific site EPG
  cisco.mso.mso_schema_site_anp_epg_domain:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    anp: ANP1
    epg: EPG1
    domain_association_type: vmmDomain
    domain_profile: 'VMware-VMM'
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all domains associated with a site EPG
  cisco.mso.mso_schema_site_anp_epg_domain:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema1
    site: Site1
    template: Template1
    anp: ANP1
    epg: EPG1
    state: query
  delegate_to: localhost
  register: query_result
```

### Authors

- Nirav Katarmal (@nkatarmal-crest)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
[Homepage](https://cisco.com/go/aci)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

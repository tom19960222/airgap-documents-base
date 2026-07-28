---
collection: ansible
version: "8"
title: "cisco.aci.aci_epg_to_domain module – Bind EPGs to Domains (fv:RsDomAtt)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/aci/aci_epg_to_domain_module.html
fetched_at: 2026-07-28T01:19:29+00:00
---
# cisco.aci.aci_epg_to_domain module – Bind EPGs to Domains (fv:RsDomAtt)

> **Note:**
>
> This module is part of the [cisco.aci collection](https://galaxy.ansible.com/ui/repo/published/cisco/aci/) (version 2.8.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.aci`.
>
> To use it in a playbook, specify: `cisco.aci.aci_epg_to_domain`.

- [Synopsis](aci_epg_to_domain_module.md#synopsis)
- [Parameters](aci_epg_to_domain_module.md#parameters)
- [Notes](aci_epg_to_domain_module.md#notes)
- [See Also](aci_epg_to_domain_module.md#see-also)
- [Examples](aci_epg_to_domain_module.md#examples)
- [Return Values](aci_epg_to_domain_module.md#return-values)

## [Synopsis](aci_epg_to_domain_module.md#id1)

- Bind EPGs to Physical and Virtual Domains on Cisco ACI fabrics.

## [Parameters](aci_epg_to_domain_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_useg**  string | Allows micro-segmentation.  The APIC defaults to `encap` when unset during creation.  **Choices:**   - `"encap"` - `"useg"` |
| **annotation**  string | User-defined string for annotating an object.  If the value is not specified in the task, the value of environment variable `ACI_ANNOTATION` will be used instead.  If the value is not specified in the task and environment variable `ACI_ANNOTATION` then the default value will be used.  **Default:** `"orchestrator:ansible"` |
| **ap**  aliases: app_profile, app_profile_name  string | Name of an existing application network profile, that will contain the EPGs. |
| **certificate_name**  aliases: cert_name  string | The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.  If a `private_key` filename was provided, this defaults to the `private_key` basename, without extension.  If PEM-formatted content was provided for `private_key`, this defaults to the `username` value.  If the value is not specified in the task, the value of environment variable `ACI_CERTIFICATE_NAME` will be used instead. |
| **custom_epg_name**  string | The custom epg name in VMM domain association. |
| **delimiter**  string | The delimiter.  **Choices:**   - `"|"` - `"~"` - `"!"` - `"@"` - `"^"` - `"+"` - `"="` |
| **deploy_immediacy**  string | Determines when the policy is pushed to hardware Policy CAM.  The APIC defaults to `lazy` when unset during creation.  **Choices:**   - `"immediate"` - `"lazy"` |
| **domain**  aliases: domain_name, domain_profile  string | Name of the physical or virtual domain being associated with the EPG. |
| **domain_type**  aliases: type  string | Specify whether the Domain is a physical (phys), a virtual (vmm) or an L2 external domain association (l2dom).  **Choices:**   - `"l2dom"` - `"phys"` - `"vmm"` |
| **encap**  integer | The VLAN encapsulation for the EPG when binding a VMM Domain with static `encap_mode`.  This acts as the secondary encap when using useg.  Accepted values range between `1` and `4096`. |
| **encap_mode**  string | The encapsulation method to be used.  The APIC defaults to `auto` when unset during creation.  If vxlan is selected, switching_mode must be “AVE”.  **Choices:**   - `"auto"` - `"vlan"` - `"vxlan"` |
| **enhanced_lag_policy**  aliases: lag_policy  string | Name of the VMM Domain Enhanced Lag Policy. |
| **epg**  aliases: epg_name, name  string | Name of the end point group. |
| **forged_transmits**  string | Allow forged transmits. A forged transmit occurs when a network adapter starts sending out traffic that identifies itself as something else.  **Choices:**   - `"accept"` - `"reject"` ← (default) |
| **host**  aliases: hostname  string | IP Address or hostname of APIC resolvable by Ansible control host.  If the value is not specified in the task, the value of environment variable `ACI_HOST` will be used instead. |
| **mac_changes**  string | Allows definition of new MAC addresses for the network adapter within the virtual machine (VM).  **Choices:**   - `"accept"` - `"reject"` ← (default) |
| **netflow**  boolean | Determines if netflow should be enabled.  The APIC defaults to `false` when unset during creation.  **Choices:**   - `false` - `true` |
| **number_of_ports**  integer | The number of ports. |
| **output_level**  string | Influence the output of this ACI module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **output_path**  string | Path to a file that will be used to dump the ACI JSON configuration objects generated by the module.  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_PATH` will be used instead. |
| **password**  string | The password to use for authentication.  This option is mutual exclusive with `private_key`. If `private_key` is provided too, it will be used instead.  If the value is not specified in the task, the value of environment variables `ACI_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `ACI_PORT` will be used instead. |
| **port_allocation**  string | The port allocation method.  **Choices:**   - `"elastic"` - `"fixed"` |
| **port_binding**  string | The port binding method.  **Choices:**   - `"dynamic"` - `"ephemeral"` - `"static"` |
| **primary_encap**  integer | Determines the primary VLAN ID when using useg.  Accepted values range between `1` and `4096`. |
| **private_key**  aliases: cert_key  string | Either a PEM-formatted private key file or the private key content used for signature-based authentication.  This value also influences the default `certificate_name` that is used.  This option is mutual exclusive with `password`. If `password` is provided too, it will be ignored.  If the value is not specified in the task, the value of environment variable `ACI_PRIVATE_KEY` or `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **promiscuous**  string | Allow/Disallow promiscuous mode in vmm domain  **Choices:**   - `"accept"` - `"reject"` ← (default) |
| **resolution_immediacy**  string | Determines when the policies should be resolved and available.  The APIC defaults to `lazy` when unset during creation.  **Choices:**   - `"immediate"` - `"lazy"` - `"pre-provision"` |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **switching_mode**  string | Switching Mode used by the switch  **Choices:**   - `"AVE"` - `"native"` ← (default) |
| **tenant**  aliases: tenant_name  string | Name of an existing tenant. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `ACI_TIMEOUT` will be used instead.  The default value is 30. |
| **untagged_vlan**  boolean | The access vlan is untagged.  **Choices:**   - `false` - `true` |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `ACI_USE_PROXY` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `ACI_USE_SSL` will be used instead.  The default value is true when the connection is local.  **Choices:**   - `false` - `true` |
| **username**  aliases: user  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `ACI_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead.  The default value is admin. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `ACI_VALIDATE_CERTS` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |
| **vm_provider**  string | The VM platform for VMM Domains.  Support for Kubernetes was added in ACI v3.0.  Support for CloudFoundry, OpenShift and Red Hat was added in ACI v3.1.  **Choices:**   - `"cloudfoundry"` - `"kubernetes"` - `"microsoft"` - `"openshift"` - `"openstack"` - `"redhat"` - `"vmware"` |
| **vmm_uplink_active**  list / elements=string | A list of active uplink IDs.  The order decides the order in which active uplinks take over for a failed uplink.  At least one active uplink must remain specified in the list when an active uplink was previously configured. |
| **vmm_uplink_standby**  list / elements=string | A list of standby uplink IDs.  At least one standby uplink must remain specified in the list when no active uplink is configured. |

## [Notes](aci_epg_to_domain_module.md#id3)

> **Note:**
>
> - The `tenant`, `ap`, `epg`, and `domain` used must exist before using this module in your playbook. The [cisco.aci.aci_tenant](aci_tenant_module.md#ansible-collections-cisco-aci-aci-tenant-module) [cisco.aci.aci_ap](aci_ap_module.md#ansible-collections-cisco-aci-aci-ap-module), [cisco.aci.aci_epg](aci_epg_module.md#ansible-collections-cisco-aci-aci-epg-module) [cisco.aci.aci_domain](aci_domain_module.md#ansible-collections-cisco-aci-aci-domain-module) modules can be used for this.
> - OpenStack VMM domains must not be created using this module. The OpenStack VMM domain is created directly by the Cisco APIC Neutron plugin as part of the installation and configuration. This module can be used to query status of an OpenStack VMM domain.

## [See Also](aci_epg_to_domain_module.md#id4)

> **See also:**
>
> [cisco.aci.aci_ap](aci_ap_module.md#ansible-collections-cisco-aci-aci-ap-module)
> :   Manage top level Application Profile (AP) objects (fv:Ap).
>
> [cisco.aci.aci_epg](aci_epg_module.md#ansible-collections-cisco-aci-aci-epg-module)
> :   Manage End Point Groups (EPG) objects (fv:AEPg).
>
> [cisco.aci.aci_domain](aci_domain_module.md#ansible-collections-cisco-aci-aci-domain-module)
> :   Manage physical, virtual, bridged, routed or FC domain profiles (phys:DomP, vmm:DomP, l2ext:DomP, l3ext:DomP, fc:DomP).
>
> [APIC Management Information Model reference](https://developer.cisco.com/docs/apic-mim-ref/)
> :   More information about the internal APIC class **fv:RsDomAtt**.
>
> [Cisco ACI Guide](../../../scenario_guides/guide_aci.md#aci-guide)
> :   Detailed information on how to manage your ACI infrastructure using Ansible.
>
> [Developing Cisco ACI modules](https://docs.ansible.com/ansible/6/dev_guide/developing_modules_general_aci.html#aci-dev-guide "(in Ansible v6)")
> :   Detailed guide on how to write your own Cisco ACI modules to contribute.

## [Examples](aci_epg_to_domain_module.md#id5)

```yaml+jinja
- name: Add a new physical domain to EPG binding
  cisco.aci.aci_epg_to_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: anstest
    ap: anstest
    epg: anstest
    domain: anstest
    domain_type: phys
    state: present
  delegate_to: localhost

- name: Remove an existing physical domain to EPG binding
  cisco.aci.aci_epg_to_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: anstest
    ap: anstest
    epg: anstest
    domain: anstest
    domain_type: phys
    state: absent
  delegate_to: localhost

- name: Query a specific physical domain to EPG binding
  cisco.aci.aci_epg_to_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: anstest
    ap: anstest
    epg: anstest
    domain: anstest
    domain_type: phys
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all domain to EPG bindings
  cisco.aci.aci_epg_to_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost
  register: query_result
```

## [Return Values](aci_epg_to_domain_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **current**  list / elements=string | The existing configuration from the APIC after the module has finished  **Returned:** success  **Sample:** `[{"fvTenant": {"attributes": {"descr": "Production environment", "dn": "uni/tn-production", "name": "production", "nameAlias": "", "ownerKey": "", "ownerTag": ""}}}]` |
| **error**  dictionary | The error information as returned from the APIC  **Returned:** failure  **Sample:** `{"code": "122", "text": "unknown managed object class foo"}` |
| **filter_string**  string | The filter string used for the request  **Returned:** failure or debug  **Sample:** `"?rsp-prop-include=config-only"` |
| **method**  string | The HTTP method used for the request to the APIC  **Returned:** failure or debug  **Sample:** `"POST"` |
| **previous**  list / elements=string | The original configuration from the APIC before the module has started  **Returned:** info  **Sample:** `[{"fvTenant": {"attributes": {"descr": "Production", "dn": "uni/tn-production", "name": "production", "nameAlias": "", "ownerKey": "", "ownerTag": ""}}}]` |
| **proposed**  dictionary | The assembled configuration from the user-provided parameters  **Returned:** info  **Sample:** `{"fvTenant": {"attributes": {"descr": "Production environment", "name": "production"}}}` |
| **raw**  string | The raw output returned by the APIC REST API (xml or json)  **Returned:** parse error  **Sample:** `"<?xml version=\"1.0\" encoding=\"UTF-8\"?><imdata totalCount=\"1\"><error code=\"122\" text=\"unknown managed object class foo\"/></imdata>"` |
| **response**  string | The HTTP response from the APIC  **Returned:** failure or debug  **Sample:** `"OK (30 bytes)"` |
| **sent**  list / elements=string | The actual/minimal configuration pushed to the APIC  **Returned:** info  **Sample:** `{"fvTenant": {"attributes": {"descr": "Production environment"}}}` |
| **status**  integer | The HTTP status from the APIC  **Returned:** failure or debug  **Sample:** `200` |
| **url**  string | The HTTP url used for the request to the APIC  **Returned:** failure or debug  **Sample:** `"https://10.11.12.13/api/mo/uni/tn-production.json"` |

### Authors

- Jacob McGill (@jmcgill298)
- Shreyas Srish (@shrsr)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-aci/issues)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-aci)

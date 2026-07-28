---
collection: ansible
version: "8"
title: "cisco.aci.aci_l3out module – Manage Layer 3 Outside (L3Out) objects (l3ext:Out)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/aci/aci_l3out_module.html
fetched_at: 2026-07-28T01:20:14+00:00
---
# cisco.aci.aci_l3out module – Manage Layer 3 Outside (L3Out) objects (l3ext:Out)

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
> To use it in a playbook, specify: `cisco.aci.aci_l3out`.

- [Synopsis](aci_l3out_module.md#synopsis)
- [Parameters](aci_l3out_module.md#parameters)
- [Notes](aci_l3out_module.md#notes)
- [See Also](aci_l3out_module.md#see-also)
- [Examples](aci_l3out_module.md#examples)
- [Return Values](aci_l3out_module.md#return-values)

## [Synopsis](aci_l3out_module.md#id1)

- Manage Layer 3 Outside (L3Out) on Cisco ACI fabrics.

## [Parameters](aci_l3out_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **annotation**  string | User-defined string for annotating an object.  If the value is not specified in the task, the value of environment variable `ACI_ANNOTATION` will be used instead.  If the value is not specified in the task and environment variable `ACI_ANNOTATION` then the default value will be used.  **Default:** `"orchestrator:ansible"` |
| **asn**  aliases: as_number  integer | The AS number for the L3Out.  Only applicable when using ‘eigrp’ as the l3protocol. |
| **certificate_name**  aliases: cert_name  string | The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.  If a `private_key` filename was provided, this defaults to the `private_key` basename, without extension.  If PEM-formatted content was provided for `private_key`, this defaults to the `username` value.  If the value is not specified in the task, the value of environment variable `ACI_CERTIFICATE_NAME` will be used instead. |
| **description**  aliases: descr  string | Description for the L3Out. |
| **domain**  aliases: ext_routed_domain_name, routed_domain  string | Name of the external L3 domain being associated with the L3Out. |
| **dscp**  aliases: target  string | The target Differentiated Service (DSCP) value.  The APIC defaults to `unspecified` when unset during creation.  **Choices:**   - `"AF11"` - `"AF12"` - `"AF13"` - `"AF21"` - `"AF22"` - `"AF23"` - `"AF31"` - `"AF32"` - `"AF33"` - `"AF41"` - `"AF42"` - `"AF43"` - `"CS0"` - `"CS1"` - `"CS2"` - `"CS3"` - `"CS4"` - `"CS5"` - `"CS6"` - `"CS7"` - `"EF"` - `"VA"` - `"unspecified"` |
| **host**  aliases: hostname  string | IP Address or hostname of APIC resolvable by Ansible control host.  If the value is not specified in the task, the value of environment variable `ACI_HOST` will be used instead. |
| **l3out**  aliases: l3out_name, name  string | Name of L3Out being created. |
| **l3protocol**  list / elements=string | Routing protocol for the L3Out.  Protocols already associated with an l3out must be provided again when the l3out is modified if the associated protocols are to be kept.  The Protocols are otherwise deleted if not provided each time an l3out is modified.  First example, to add BGP protocol to an l3out with OSPF protocol, the user must enter `[ bgp, ospf ]` even though “ospf” was provided before.  Second example, to change the protocol from OSPF to EIGRP, the user must simply enter `[ eigrp ]` and the previous OSPF protocol will be deleted.  To remove all existing protocols, the user must enter `[ static ]`.  **Choices:**   - `"bgp"` - `"eigrp"` - `"ospf"` - `"pim"` - `"static"` |
| **mpls**  string | Indicate whether MPLS (Multi-Protocol Label Switching) is enabled or not.  The APIC defaults to `no` when unset during creation.  **Choices:**   - `"no"` - `"yes"` |
| **name_alias**  string | The alias for the current object. This relates to the nameAlias field in ACI. |
| **ospf**  dictionary | Parameters for the OSPF protocol. |
| **area_cost**  integer | The OSPF area cost.  The APIC defaults to `1` when unset during creation. |
| **area_ctrl**  list / elements=string | The controls of redistribution and summary LSA generation into NSSA and Stub areas.  The APIC defaults to `redistribute,summary` when unset during creation.  **Choices:**   - `"redistribute"` - `"summary"` - `"suppress-fa"` - `"unspecified"` |
| **area_id**  string | The OSPF Area ID.  An area is a logical collection of OSPF networks, routers, and links that have the same area identification.  A router within an area must maintain a topological database for the area to which it belongs.  The router doesn’t have detailed information about network topology outside of its area, thereby reducing the size of its database.  Areas limit the scope of route information distribution. It is not possible to do route update filtering within an area.  The link-state database (LSDB) of routers within the same area must be synchronized and be exactly the same.  However, route summarization and filtering is possible between different areas.  The main benefit of creating areas is a reduction in the number of routes to propagate-by the filtering and the summarization of routes.  Areas are identified by an area ID.  Cisco IOS software supports area IDs expressed in IP address format or decimal format, for example, area 0.0.0.0 is equal to area 0.  The APIC defaults to `1` when unset during creation. |
| **area_type**  string | The OSPF area type.  The APIC defaults to `nssa` when unset during creation.  **Choices:**   - `"nssa"` - `"regular"` - `"stub"` |
| **description**  aliases: descr  string | Specifies the description of a policy component. |
| **multipod_internal**  string | Start OSPF in WAN instance instead of default.  The APIC defaults to `no` when unset during creation.  **Choices:**   - `"no"` - `"yes"` |
| **name_alias**  string | The alias for the current object. This relates to the nameAlias field in ACI. |
| **output_level**  string | Influence the output of this ACI module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **output_path**  string | Path to a file that will be used to dump the ACI JSON configuration objects generated by the module.  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_PATH` will be used instead. |
| **owner_key**  string | User-defined string for the ownerKey attribute of an ACI object.  This attribute represents a key for enabling clients to own their data for entity correlation.  If the value is not specified in the task, the value of environment variable `ACI_OWNER_KEY` will be used instead. |
| **owner_tag**  string | User-defined string for the ownerTag attribute of an ACI object.  This attribute represents a tag for enabling clients to add their own data.  For example, to indicate who created this object.  If the value is not specified in the task, the value of environment variable `ACI_OWNER_TAG` will be used instead. |
| **password**  string | The password to use for authentication.  This option is mutual exclusive with `private_key`. If `private_key` is provided too, it will be used instead.  If the value is not specified in the task, the value of environment variables `ACI_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `ACI_PORT` will be used instead. |
| **private_key**  aliases: cert_key  string | Either a PEM-formatted private key file or the private key content used for signature-based authentication.  This value also influences the default `certificate_name` that is used.  This option is mutual exclusive with `password`. If `password` is provided too, it will be ignored.  If the value is not specified in the task, the value of environment variable `ACI_PRIVATE_KEY` or `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **route_control**  aliases: route_control_enforcement  list / elements=string | Route Control enforcement direction. The only allowed values are export or import,export.  The APIC defaults to `export` when unset during creation.  **Choices:**   - `"export"` - `"import"` |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **tenant**  aliases: tenant_name  string | Name of an existing tenant. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `ACI_TIMEOUT` will be used instead.  The default value is 30. |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `ACI_USE_PROXY` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `ACI_USE_SSL` will be used instead.  The default value is true when the connection is local.  **Choices:**   - `false` - `true` |
| **username**  aliases: user  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `ACI_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead.  The default value is admin. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `ACI_VALIDATE_CERTS` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |
| **vrf**  aliases: vrf_name  string | Name of the VRF being associated with the L3Out. |

## [Notes](aci_l3out_module.md#id3)

> **Note:**
>
> - The `tenant` and `domain` and `vrf` used must exist before using this module in your playbook.
> - The [cisco.aci.aci_tenant](aci_tenant_module.md#ansible-collections-cisco-aci-aci-tenant-module) and [cisco.aci.aci_domain](aci_domain_module.md#ansible-collections-cisco-aci-aci-domain-module) and [cisco.aci.aci_vrf](aci_vrf_module.md#ansible-collections-cisco-aci-aci-vrf-module) modules can be used for this.

## [See Also](aci_l3out_module.md#id4)

> **See also:**
>
> [cisco.aci.aci_tenant](aci_tenant_module.md#ansible-collections-cisco-aci-aci-tenant-module)
> :   Manage tenants (fv:Tenant).
>
> [cisco.aci.aci_domain](aci_domain_module.md#ansible-collections-cisco-aci-aci-domain-module)
> :   Manage physical, virtual, bridged, routed or FC domain profiles (phys:DomP, vmm:DomP, l2ext:DomP, l3ext:DomP, fc:DomP).
>
> [cisco.aci.aci_vrf](aci_vrf_module.md#ansible-collections-cisco-aci-aci-vrf-module)
> :   Manage contexts or VRFs (fv:Ctx).
>
> [APIC Management Information Model reference](https://developer.cisco.com/docs/apic-mim-ref/)
> :   More information about the internal APIC class **l3ext:Out**.
>
> [Cisco ACI Guide](../../../scenario_guides/guide_aci.md#aci-guide)
> :   Detailed information on how to manage your ACI infrastructure using Ansible.
>
> [Developing Cisco ACI modules](https://docs.ansible.com/ansible/6/dev_guide/developing_modules_general_aci.html#aci-dev-guide "(in Ansible v6)")
> :   Detailed guide on how to write your own Cisco ACI modules to contribute.

## [Examples](aci_l3out_module.md#id5)

```yaml+jinja
- name: Add a new L3Out
  cisco.aci.aci_l3out:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    name: prod_l3out
    description: L3Out for Production tenant
    domain: l3dom_prod
    vrf: prod
    l3protocol: ospf
    ospf:
      area_cost: 1
      area_ctrl: [ summary, redistribute ]
      area_id: 0.0.0.1
      area_type: regular
      multipod_internal: no
    state: present
  delegate_to: localhost

- name: Delete L3Out
  cisco.aci.aci_l3out:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    name: prod_l3out
    state: absent
  delegate_to: localhost

- name: Query L3Out information
  cisco.aci.aci_l3out:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    name: prod_l3out
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all L3Outs
  cisco.aci.aci_l3out:
    host: apic
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost
  register: query_all_result
```

## [Return Values](aci_l3out_module.md#id6)

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

- Rostyslav Davydenko (@rost-d)
- Gaspard Micol (@gmicol)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-aci/issues)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-aci)

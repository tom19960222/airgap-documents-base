---
collection: ansible
version: "8"
title: "cisco.aci.aci_bd module – Manage Bridge Domains (BD) objects (fv:BD)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/aci/aci_bd_module.html
fetched_at: 2026-07-28T01:18:54+00:00
---
# cisco.aci.aci_bd module – Manage Bridge Domains (BD) objects (fv:BD)

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
> To use it in a playbook, specify: `cisco.aci.aci_bd`.

- [Synopsis](aci_bd_module.md#synopsis)
- [Parameters](aci_bd_module.md#parameters)
- [Notes](aci_bd_module.md#notes)
- [See Also](aci_bd_module.md#see-also)
- [Examples](aci_bd_module.md#examples)
- [Return Values](aci_bd_module.md#return-values)

## [Synopsis](aci_bd_module.md#id1)

- Manages Bridge Domains (BD) on Cisco ACI fabrics.

## [Parameters](aci_bd_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **annotation**  string | User-defined string for annotating an object.  If the value is not specified in the task, the value of environment variable `ACI_ANNOTATION` will be used instead.  If the value is not specified in the task and environment variable `ACI_ANNOTATION` then the default value will be used.  **Default:** `"orchestrator:ansible"` |
| **arp_flooding**  boolean | Determines if the Bridge Domain should flood ARP traffic.  The APIC defaults to `false` when unset during creation.  **Choices:**   - `false` - `true` |
| **bd**  aliases: bd_name, name  string | The name of the Bridge Domain. |
| **bd_type**  string | The type of traffic on the Bridge Domain.  The APIC defaults to `ethernet` when unset during creation.  **Choices:**   - `"ethernet"` - `"fc"` |
| **certificate_name**  aliases: cert_name  string | The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.  If a `private_key` filename was provided, this defaults to the `private_key` basename, without extension.  If PEM-formatted content was provided for `private_key`, this defaults to the `username` value.  If the value is not specified in the task, the value of environment variable `ACI_CERTIFICATE_NAME` will be used instead. |
| **description**  string | Description for the Bridge Domain. |
| **enable_multicast**  boolean | Determines if PIM is enabled.  The APIC defaults to `false` when unset during creation.  **Choices:**   - `false` - `true` |
| **enable_routing**  boolean | Determines if IP forwarding should be allowed.  The APIC defaults to `true` when unset during creation.  **Choices:**   - `false` - `true` |
| **endpoint_clear**  boolean | Clears all End Points in all Leaves when `true`.  The value is not reset to disabled once End Points have been cleared; that requires a second task.  The APIC defaults to `false` when unset during creation.  **Choices:**   - `false` - `true` |
| **endpoint_move_detect**  string | Determines if GARP should be enabled to detect when End Points move.  **Choices:**   - `"default"` - `"garp"` |
| **endpoint_retention_action**  string | Determines if the Bridge Domain should inherit or resolve the End Point Retention Policy.  The APIC defaults to `resolve` when unset during creation.  **Choices:**   - `"inherit"` - `"resolve"` |
| **endpoint_retention_policy**  string | The name of the End Point Retention Policy the Bridge Domain should use when overriding the default End Point Retention Policy. |
| **host**  aliases: hostname  string | IP Address or hostname of APIC resolvable by Ansible control host.  If the value is not specified in the task, the value of environment variable `ACI_HOST` will be used instead. |
| **igmp_snoop_policy**  string | The name of the IGMP Snooping Policy the Bridge Domain should use when overriding the default IGMP Snooping Policy. |
| **ip_learning**  boolean | Determines if the Bridge Domain should learn End Point IPs.  The APIC defaults to `true` when unset during creation.  **Choices:**   - `false` - `true` |
| **ipv6_l3_unknown_multicast**  string | Determines the forwarding method to use for IPv6 unknown multicast destinations.  The APIC defaults to `flood` when unset during creation.  **Choices:**   - `"flood"` - `"opt-flood"` |
| **ipv6_nd_policy**  string | The name of the IPv6 Neighbor Discovery Policy the Bridge Domain should use when overridding the default IPV6 ND Policy. |
| **l2_unknown_unicast**  string | Determines what forwarding method to use for unknown l2 destinations.  The APIC defaults to `proxy` when unset during creation.  **Choices:**   - `"proxy"` - `"flood"` |
| **l3_unknown_multicast**  string | Determines the forwarding method to use for unknown multicast destinations.  The APIC defaults to `flood` when unset during creation.  **Choices:**   - `"flood"` - `"opt-flood"` |
| **limit_ip_learn**  boolean | Determines if the BD should limit IP learning to only subnets owned by the Bridge Domain.  The APIC defaults to `true` when unset during creation.  **Choices:**   - `false` - `true` |
| **mac_address**  aliases: mac  string | The MAC Address to assign to the `bd` instead of using the default.  The APIC defaults to `00:22:BD:F8:19:FF` when unset during creation. |
| **multi_dest**  string | Determines the forwarding method for L2 multicast, broadcast, and link layer traffic.  The APIC defaults to `bd-flood` when unset during creation.  **Choices:**   - `"bd-flood"` - `"drop"` - `"encap-flood"` |
| **name_alias**  string | The alias for the current object. This relates to the nameAlias field in ACI. |
| **output_level**  string | Influence the output of this ACI module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **output_path**  string | Path to a file that will be used to dump the ACI JSON configuration objects generated by the module.  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_PATH` will be used instead. |
| **owner_key**  string | User-defined string for the ownerKey attribute of an ACI object.  This attribute represents a key for enabling clients to own their data for entity correlation.  If the value is not specified in the task, the value of environment variable `ACI_OWNER_KEY` will be used instead. |
| **owner_tag**  string | User-defined string for the ownerTag attribute of an ACI object.  This attribute represents a tag for enabling clients to add their own data.  For example, to indicate who created this object.  If the value is not specified in the task, the value of environment variable `ACI_OWNER_TAG` will be used instead. |
| **password**  string | The password to use for authentication.  This option is mutual exclusive with `private_key`. If `private_key` is provided too, it will be used instead.  If the value is not specified in the task, the value of environment variables `ACI_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `ACI_PORT` will be used instead. |
| **private_key**  aliases: cert_key  string | Either a PEM-formatted private key file or the private key content used for signature-based authentication.  This value also influences the default `certificate_name` that is used.  This option is mutual exclusive with `password`. If `password` is provided too, it will be ignored.  If the value is not specified in the task, the value of environment variable `ACI_PRIVATE_KEY` or `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **route_profile**  string | The Route Profile to associate with the Bridge Domain. |
| **route_profile_l3out**  string | The L3 Out that contains the associated Route Profile. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **tenant**  aliases: tenant_name  string | The name of the Tenant. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `ACI_TIMEOUT` will be used instead.  The default value is 30. |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `ACI_USE_PROXY` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `ACI_USE_SSL` will be used instead.  The default value is true when the connection is local.  **Choices:**   - `false` - `true` |
| **username**  aliases: user  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `ACI_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead.  The default value is admin. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `ACI_VALIDATE_CERTS` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |
| **vrf**  aliases: vrf_name  string | The name of the VRF. |

## [Notes](aci_bd_module.md#id3)

> **Note:**
>
> - The `tenant` used must exist before using this module in your playbook. The [cisco.aci.aci_tenant](aci_tenant_module.md#ansible-collections-cisco-aci-aci-tenant-module) module can be used for this.

## [See Also](aci_bd_module.md#id4)

> **See also:**
>
> [cisco.aci.aci_tenant](aci_tenant_module.md#ansible-collections-cisco-aci-aci-tenant-module)
> :   Manage tenants (fv:Tenant).
>
> [APIC Management Information Model reference](https://developer.cisco.com/docs/apic-mim-ref/)
> :   More information about the internal APIC class **fv:BD**.
>
> [Cisco ACI Guide](../../../scenario_guides/guide_aci.md#aci-guide)
> :   Detailed information on how to manage your ACI infrastructure using Ansible.
>
> [Developing Cisco ACI modules](https://docs.ansible.com/ansible/6/dev_guide/developing_modules_general_aci.html#aci-dev-guide "(in Ansible v6)")
> :   Detailed guide on how to write your own Cisco ACI modules to contribute.

## [Examples](aci_bd_module.md#id5)

```yaml+jinja
- name: Add Bridge Domain
  cisco.aci.aci_bd:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: false
    tenant: prod
    bd: web_servers
    mac_address: 00:22:BD:F8:19:FE
    vrf: prod_vrf
    state: present
  delegate_to: localhost

- name: Add an FC Bridge Domain
  cisco.aci.aci_bd:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: false
    tenant: prod
    bd: storage
    bd_type: fc
    vrf: fc_vrf
    enable_routing: false
    state: present
  delegate_to: localhost

- name: Modify a Bridge Domain
  cisco.aci.aci_bd:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: true
    tenant: prod
    bd: web_servers
    arp_flooding: true
    l2_unknown_unicast: flood
    state: present
  delegate_to: localhost

- name: Query All Bridge Domains
  cisco.aci.aci_bd:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: true
    state: query
  delegate_to: localhost
  register: query_result

- name: Query a Bridge Domain
  cisco.aci.aci_bd:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: true
    tenant: prod
    bd: web_servers
    state: query
  delegate_to: localhost
  register: query_result

- name: Delete a Bridge Domain
  cisco.aci.aci_bd:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: true
    tenant: prod
    bd: web_servers
    state: absent
  delegate_to: localhost
```

## [Return Values](aci_bd_module.md#id6)

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

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-aci/issues)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-aci)

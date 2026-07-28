---
collection: ansible
version: "8"
title: "cisco.aci.aci_filter_entry module – Manage filter entries (vz:Entry)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/aci/aci_filter_entry_module.html
fetched_at: 2026-07-28T01:19:49+00:00
---
# cisco.aci.aci_filter_entry module – Manage filter entries (vz:Entry)

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
> To use it in a playbook, specify: `cisco.aci.aci_filter_entry`.

- [Synopsis](aci_filter_entry_module.md#synopsis)
- [Parameters](aci_filter_entry_module.md#parameters)
- [Notes](aci_filter_entry_module.md#notes)
- [See Also](aci_filter_entry_module.md#see-also)
- [Examples](aci_filter_entry_module.md#examples)
- [Return Values](aci_filter_entry_module.md#return-values)

## [Synopsis](aci_filter_entry_module.md#id1)

- Manage filter entries for a filter on Cisco ACI fabrics.

## [Parameters](aci_filter_entry_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **annotation**  string | User-defined string for annotating an object.  If the value is not specified in the task, the value of environment variable `ACI_ANNOTATION` will be used instead.  If the value is not specified in the task and environment variable `ACI_ANNOTATION` then the default value will be used.  **Default:** `"orchestrator:ansible"` |
| **arp_flag**  string | The arp flag to use when the ether_type is arp.  The APIC defaults to `unspecified` when unset during creation.  **Choices:**   - `"arp_reply"` - `"arp_request"` - `"unspecified"` |
| **certificate_name**  aliases: cert_name  string | The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.  If a `private_key` filename was provided, this defaults to the `private_key` basename, without extension.  If PEM-formatted content was provided for `private_key`, this defaults to the `username` value.  If the value is not specified in the task, the value of environment variable `ACI_CERTIFICATE_NAME` will be used instead. |
| **description**  aliases: descr  string | Description for the Filter Entry. |
| **destination_port**  aliases: dst_port  string | Used to set both destination start and end ports to the same value when ip_protocol is tcp or udp.  Accepted values are any valid TCP/UDP port range.  The APIC defaults to `unspecified` when unset during creation. |
| **destination_port_end**  aliases: dst_port_end  string | Used to set the destination end port when ip_protocol is tcp or udp.  Accepted values are any valid TCP/UDP port range.  The APIC defaults to `unspecified` when unset during creation. |
| **destination_port_start**  aliases: dst_port_start  string | Used to set the destination start port when ip_protocol is tcp or udp.  Accepted values are any valid TCP/UDP port range.  The APIC defaults to `unspecified` when unset during creation. |
| **entry**  aliases: entry_name, filter_entry, name  string | Then name of the Filter Entry. |
| **ether_type**  string | The Ethernet type.  The APIC defaults to `unspecified` when unset during creation.  **Choices:**   - `"arp"` - `"fcoe"` - `"ip"` - `"ipv4"` - `"ipv6"` - `"mac_security"` - `"mpls_ucast"` - `"trill"` - `"unspecified"` |
| **filter**  aliases: filter_name  string | The name of Filter that the entry should belong to. |
| **host**  aliases: hostname  string | IP Address or hostname of APIC resolvable by Ansible control host.  If the value is not specified in the task, the value of environment variable `ACI_HOST` will be used instead. |
| **icmp6_msg_type**  string | ICMPv6 message type; used when ip_protocol is icmpv6.  The APIC defaults to `unspecified` when unset during creation.  **Choices:**   - `"dst_unreachable"` - `"echo_request"` - `"echo_reply"` - `"neighbor_advertisement"` - `"neighbor_solicitation"` - `"redirect"` - `"time_exceeded"` - `"unspecified"` |
| **icmp_msg_type**  string | ICMPv4 message type; used when ip_protocol is icmp.  The APIC defaults to `unspecified` when unset during creation.  **Choices:**   - `"dst_unreachable"` - `"echo"` - `"echo_reply"` - `"src_quench"` - `"time_exceeded"` - `"unspecified"` |
| **ip_protocol**  string | The IP Protocol type when ether_type is ip.  The APIC defaults to `unspecified` when unset during creation.  **Choices:**   - `"eigrp"` - `"egp"` - `"icmp"` - `"icmpv6"` - `"igmp"` - `"igp"` - `"l2tp"` - `"ospfigp"` - `"pim"` - `"tcp"` - `"udp"` - `"unspecified"` |
| **match_only_fragments**  boolean | The match only packet fragments of the filter entry.  When enabled `true` the rule applies to any fragments with offset greater than 0 (all fragments except first).  When disabled `false` it applies to all packets (including all fragments)  The APIC defaults to `false` when unset during creation.  **Choices:**   - `false` - `true` |
| **name_alias**  string | The alias for the current object. This relates to the nameAlias field in ACI. |
| **output_level**  string | Influence the output of this ACI module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **output_path**  string | Path to a file that will be used to dump the ACI JSON configuration objects generated by the module.  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_PATH` will be used instead. |
| **password**  string | The password to use for authentication.  This option is mutual exclusive with `private_key`. If `private_key` is provided too, it will be used instead.  If the value is not specified in the task, the value of environment variables `ACI_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `ACI_PORT` will be used instead. |
| **private_key**  aliases: cert_key  string | Either a PEM-formatted private key file or the private key content used for signature-based authentication.  This value also influences the default `certificate_name` that is used.  This option is mutual exclusive with `password`. If `password` is provided too, it will be ignored.  If the value is not specified in the task, the value of environment variable `ACI_PRIVATE_KEY` or `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **source_port**  aliases: src_port  string | Used to set both source start and end ports to the same value when ip_protocol is tcp or udp.  Accepted values are any valid TCP/UDP port range.  The APIC defaults to `unspecified` when unset during creation. |
| **source_port_end**  aliases: src_port_end  string | Used to set the source end port when ip_protocol is tcp or udp.  Accepted values are any valid TCP/UDP port range.  The APIC defaults to `unspecified` when unset during creation. |
| **source_port_start**  aliases: src_port_start  string | Used to set the source start port when ip_protocol is tcp or udp.  Accepted values are any valid TCP/UDP port range.  The APIC defaults to `unspecified` when unset during creation. |
| **state**  string | present, absent, query  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **stateful**  boolean | Determines the statefulness of the filter entry.  **Choices:**   - `false` - `true` |
| **tcp_flags**  list / elements=string | The TCP flags of the filter entry.  The TCP `established` cannot be combined with other tcp rules.  The APIC defaults to `unspecified` when unset during creation.  **Choices:**   - `"acknowledgment"` - `"established"` - `"finish"` - `"reset"` - `"synchronize"` - `"unspecified"` |
| **tenant**  aliases: tenant_name  string | The name of the tenant. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `ACI_TIMEOUT` will be used instead.  The default value is 30. |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `ACI_USE_PROXY` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `ACI_USE_SSL` will be used instead.  The default value is true when the connection is local.  **Choices:**   - `false` - `true` |
| **username**  aliases: user  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `ACI_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead.  The default value is admin. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `ACI_VALIDATE_CERTS` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |

## [Notes](aci_filter_entry_module.md#id3)

> **Note:**
>
> - The `tenant` and `filter` used must exist before using this module in your playbook. The [cisco.aci.aci_tenant](aci_tenant_module.md#ansible-collections-cisco-aci-aci-tenant-module) and [cisco.aci.aci_filter](aci_filter_module.md#ansible-collections-cisco-aci-aci-filter-module) modules can be used for this.

## [See Also](aci_filter_entry_module.md#id4)

> **See also:**
>
> [cisco.aci.aci_tenant](aci_tenant_module.md#ansible-collections-cisco-aci-aci-tenant-module)
> :   Manage tenants (fv:Tenant).
>
> [cisco.aci.aci_filter](aci_filter_module.md#ansible-collections-cisco-aci-aci-filter-module)
> :   Manages top level filter objects (vz:Filter).
>
> [APIC Management Information Model reference](https://developer.cisco.com/docs/apic-mim-ref/)
> :   More information about the internal APIC class **vz:Entry**.
>
> [Cisco ACI Guide](../../../scenario_guides/guide_aci.md#aci-guide)
> :   Detailed information on how to manage your ACI infrastructure using Ansible.
>
> [Developing Cisco ACI modules](https://docs.ansible.com/ansible/6/dev_guide/developing_modules_general_aci.html#aci-dev-guide "(in Ansible v6)")
> :   Detailed guide on how to write your own Cisco ACI modules to contribute.

## [Examples](aci_filter_entry_module.md#id5)

```yaml+jinja
- name: Create a filter entry
  cisco.aci.aci_filter_entry:
    host: apic
    username: admin
    password: SomeSecretPassword
    entry: https_allow
    filter: web_filter
    tenant: prod
    ether_type: ip
    ip_protocol: tcp
    dst_port_start: 443
    dst_port_end: 443
    source_port_start: 20
    source_port_end: 22
    tcp_flags:
      - acknowledgment
      - finish
    state: present
  delegate_to: localhost

- name: Create a filter entry with the match only packet fragments enabled
  cisco.aci.aci_filter_entry:
    host: apic
    username: admin
    password: SomeSecretPassword
    entry: https_allow
    filter: web_filter
    tenant: prod
    ether_type: ip
    ip_protocol: tcp
    match_only_fragments: true
    state: present
  delegate_to: localhost

- name: Delete a filter entry
  cisco.aci.aci_filter_entry:
    host: apic
    username: admin
    password: SomeSecretPassword
    entry: https_allow
    filter: web_filter
    tenant: prod
    state: absent
  delegate_to: localhost

- name: Query all filter entries
  cisco.aci.aci_filter_entry:
    host: apic
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost
  register: query_result

- name: Query a specific filter entry
  cisco.aci.aci_filter_entry:
    host: apic
    username: admin
    password: SomeSecretPassword
    entry: https_allow
    filter: web_filter
    tenant: prod
    state: query
  delegate_to: localhost
  register: query_result
```

## [Return Values](aci_filter_entry_module.md#id6)

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

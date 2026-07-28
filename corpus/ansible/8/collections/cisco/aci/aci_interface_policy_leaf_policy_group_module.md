---
collection: ansible
version: "8"
title: "cisco.aci.aci_interface_policy_leaf_policy_group module – Manage fabric interface policy leaf policy groups (infra:AccBndlGrp, infra:AccPortGrp)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/aci/aci_interface_policy_leaf_policy_group_module.html
fetched_at: 2026-07-28T01:20:00+00:00
---
# cisco.aci.aci_interface_policy_leaf_policy_group module – Manage fabric interface policy leaf policy groups (infra:AccBndlGrp, infra:AccPortGrp)

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
> To use it in a playbook, specify: `cisco.aci.aci_interface_policy_leaf_policy_group`.

- [Synopsis](aci_interface_policy_leaf_policy_group_module.md#synopsis)
- [Parameters](aci_interface_policy_leaf_policy_group_module.md#parameters)
- [Notes](aci_interface_policy_leaf_policy_group_module.md#notes)
- [See Also](aci_interface_policy_leaf_policy_group_module.md#see-also)
- [Examples](aci_interface_policy_leaf_policy_group_module.md#examples)
- [Return Values](aci_interface_policy_leaf_policy_group_module.md#return-values)

## [Synopsis](aci_interface_policy_leaf_policy_group_module.md#id1)

- Manage fabric interface policy leaf policy groups on Cisco ACI fabrics.

## [Parameters](aci_interface_policy_leaf_policy_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aep**  aliases: aep_name  string | The name of the attached entity profile (AEP) used by the leaf interface policy group. |
| **annotation**  string | User-defined string for annotating an object.  If the value is not specified in the task, the value of environment variable `ACI_ANNOTATION` will be used instead.  If the value is not specified in the task and environment variable `ACI_ANNOTATION` then the default value will be used.  **Default:** `"orchestrator:ansible"` |
| **cdp_policy**  aliases: cdp_policy_name  string | The name of the cdp policy used by the leaf interface policy group. |
| **certificate_name**  aliases: cert_name  string | The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.  If a `private_key` filename was provided, this defaults to the `private_key` basename, without extension.  If PEM-formatted content was provided for `private_key`, this defaults to the `username` value.  If the value is not specified in the task, the value of environment variable `ACI_CERTIFICATE_NAME` will be used instead. |
| **copp_policy**  aliases: copp_policy_name  string | The name of the copp policy used by the leaf interface policy group. |
| **description**  aliases: descr  string | The description of the leaf interface policy group. |
| **dwdm**  aliases: dwdm_name  string | The name of the dwdm used by the leaf interface policy group. |
| **egress_data_plane_policing_policy**  aliases: egress_data_plane_policing_policy_name  string | The name of the egress data plane policing policy used by the leaf interface policy group. |
| **fibre_channel_interface_policy**  aliases: fibre_channel_interface_policy_name  string | The name of the fibre channel interface policy used by the leaf interface policy group. |
| **host**  aliases: hostname  string | IP Address or hostname of APIC resolvable by Ansible control host.  If the value is not specified in the task, the value of environment variable `ACI_HOST` will be used instead. |
| **ingress_data_plane_policing_policy**  aliases: ingress_data_plane_policing_policy_name  string | The name of the ingress data plane policing policy used by the leaf interface policy group. |
| **l2_interface_policy**  aliases: l2_interface_policy_name  string | The name of the l2 interface policy used by the leaf interface policy group. |
| **lag_type**  aliases: lag_type_name  string / required | Selector for the type of leaf interface policy group.  `leaf` for Leaf Access Port Policy Group  `link` for Port Channel (PC)  `node` for Virtual Port Channel (VPC)  **Choices:**   - `"leaf"` - `"link"` - `"node"` |
| **link_flap_policy**  aliases: link_flap_policy_name  string | The name of the link flap policy used by the leaf interface policy group. |
| **link_level_flow_control**  aliases: link_level_flow_control_name  string | The name of the link level flow control used by the leaf interface policy group. |
| **link_level_policy**  aliases: link_level_policy_name  string | The name of the link level policy used by the leaf interface policy group. |
| **lldp_policy**  aliases: lldp_policy_name  string | The name of the lldp policy used by the leaf interface policy group. |
| **mac_sec_interface_policy**  aliases: mac_sec_interface_policy_name  string | The name of the mac sec interface policy used by the leaf interface policy group. |
| **mcp_policy**  aliases: mcp_policy_name  string | The name of the mcp policy used by the leaf interface policy group. |
| **monitoring_policy**  aliases: monitoring_policy_name  string | The name of the monitoring policy used by the leaf interface policy group. |
| **name_alias**  string | The alias for the current object. This relates to the nameAlias field in ACI. |
| **output_level**  string | Influence the output of this ACI module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **output_path**  string | Path to a file that will be used to dump the ACI JSON configuration objects generated by the module.  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_PATH` will be used instead. |
| **owner_key**  string | User-defined string for the ownerKey attribute of an ACI object.  This attribute represents a key for enabling clients to own their data for entity correlation.  If the value is not specified in the task, the value of environment variable `ACI_OWNER_KEY` will be used instead. |
| **owner_tag**  string | User-defined string for the ownerTag attribute of an ACI object.  This attribute represents a tag for enabling clients to add their own data.  For example, to indicate who created this object.  If the value is not specified in the task, the value of environment variable `ACI_OWNER_TAG` will be used instead. |
| **password**  string | The password to use for authentication.  This option is mutual exclusive with `private_key`. If `private_key` is provided too, it will be used instead.  If the value is not specified in the task, the value of environment variables `ACI_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **poe_interface_policy**  aliases: poe_interface_policy_name  string | The name of the poe interface policy used by the leaf interface policy group. |
| **policy_group**  aliases: name, policy_group_name  string | The name of the leaf interface policy group. |
| **port**  integer | Port number to be used for REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `ACI_PORT` will be used instead. |
| **port_authentication**  aliases: port_authentication_name  string | The name of the port authentication used by the leaf interface policy group. |
| **port_channel_policy**  aliases: port_channel_policy_name  string | The name of the port channel policy used by the leaf interface policy group. |
| **port_security_policy**  aliases: port_security_policy_name  string | The name of the port security policy used by the leaf interface policy group. |
| **priority_flow_control_policy**  aliases: priority_flow_control_policy_name  string | The name of the priority flow control policy used by the leaf interface policy group. |
| **private_key**  aliases: cert_key  string | Either a PEM-formatted private key file or the private key content used for signature-based authentication.  This value also influences the default `certificate_name` that is used.  This option is mutual exclusive with `password`. If `password` is provided too, it will be ignored.  If the value is not specified in the task, the value of environment variable `ACI_PRIVATE_KEY` or `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **slow_drain_policy**  aliases: slow_drain_policy_name  string | The name of the slow drain policy used by the leaf interface policy group. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **storm_control_interface_policy**  aliases: storm_control_interface_policy_name  string | The name of the storm control interface policy used by the leaf interface policy group. |
| **stp_interface_policy**  aliases: stp_interface_policy_name  string | The name of the stp interface policy used by the leaf interface policy group. |
| **sync_e_interface_policy**  aliases: sync_e_interface_policy_name  string | The name of the syncE interface policy used by the leaf interface policy group.  Only availavle in APIC version 5.2 or later. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `ACI_TIMEOUT` will be used instead.  The default value is 30. |
| **transceiver_policy**  dictionary | The name of the transceiver policy used by the leaf interface policy group.  Only availavle in APIC version 6.0(2h) or later. |
| **name**  aliases: transceiver_policy_name  string / required | The name of the transceiver policy. |
| **type**  aliases: transceiver_policy_type  string / required | The type of the transceiver policy.  **Choices:**   - `"zr"` - `"zrp"` |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `ACI_USE_PROXY` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `ACI_USE_SSL` will be used instead.  The default value is true when the connection is local.  **Choices:**   - `false` - `true` |
| **username**  aliases: user  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `ACI_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead.  The default value is admin. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `ACI_VALIDATE_CERTS` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |

## [Notes](aci_interface_policy_leaf_policy_group_module.md#id3)

> **Note:**
>
> - When using the module please select the appropriate link_aggregation_type (lag_type).
> - `link` for Port Channel(PC), `node` for Virtual Port Channel(VPC) and `leaf` for Leaf Access Port Policy Group.

## [See Also](aci_interface_policy_leaf_policy_group_module.md#id4)

> **See also:**
>
> [APIC Management Information Model reference](https://developer.cisco.com/docs/apic-mim-ref/)
> :   More information about the internal APIC classes **infra:AccBndlGrp** and **infra:AccPortGrp**.
>
> [Cisco ACI Guide](../../../scenario_guides/guide_aci.md#aci-guide)
> :   Detailed information on how to manage your ACI infrastructure using Ansible.
>
> [Developing Cisco ACI modules](https://docs.ansible.com/ansible/6/dev_guide/developing_modules_general_aci.html#aci-dev-guide "(in Ansible v6)")
> :   Detailed guide on how to write your own Cisco ACI modules to contribute.

## [Examples](aci_interface_policy_leaf_policy_group_module.md#id5)

```yaml+jinja
- name: Create a Port Channel (PC) Interface Policy Group
  cisco.aci.aci_interface_policy_leaf_policy_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    lag_type: link
    policy_group: policygroupname
    description: policygroupname description
    link_level_policy: linklevelpolicy
    cdp_policy: cdppolicy
    lldp_policy: lldppolicy
    port_channel_policy: lacppolicy
    state: present
  delegate_to: localhost

- name: Create a Virtual Port Channel (VPC) Interface Policy Group
  cisco.aci.aci_interface_policy_leaf_policy_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    lag_type: node
    policy_group: policygroupname
    link_level_policy: linklevelpolicy
    cdp_policy: cdppolicy
    lldp_policy: lldppolicy
    port_channel_policy: lacppolicy
    state: present
  delegate_to: localhost

- name: Create a Leaf Access Port Policy Group
  cisco.aci.aci_interface_policy_leaf_policy_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    lag_type: leaf
    policy_group: policygroupname
    link_level_policy: linklevelpolicy
    cdp_policy: cdppolicy
    lldp_policy: lldppolicy
    state: present
  delegate_to: localhost

- name: Query all Leaf Access Port Policy Groups of type link
  cisco.aci.aci_interface_policy_leaf_policy_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    lag_type: link
    state: query
  delegate_to: localhost
  register: query_result

- name: Query a specific Lead Access Port Policy Group
  cisco.aci.aci_interface_policy_leaf_policy_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    lag_type: leaf
    policy_group: policygroupname
    state: query
  delegate_to: localhost
  register: query_result

- name: Delete an Interface policy Leaf Policy Group
  cisco.aci.aci_interface_policy_leaf_policy_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    lag_type: leaf
    policy_group: policygroupname
    state: absent
  delegate_to: localhost
```

## [Return Values](aci_interface_policy_leaf_policy_group_module.md#id6)

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

- Bruno Calogero (@brunocalogero)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-aci/issues)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-aci)

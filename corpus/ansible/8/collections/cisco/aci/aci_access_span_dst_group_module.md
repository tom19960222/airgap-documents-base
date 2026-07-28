---
collection: ansible
version: "8"
title: "cisco.aci.aci_access_span_dst_group module – Manage Access SPAN destination groups (span:DestGrp)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/aci/aci_access_span_dst_group_module.html
fetched_at: 2026-07-28T01:18:46+00:00
---
# cisco.aci.aci_access_span_dst_group module – Manage Access SPAN destination groups (span:DestGrp)

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
> To use it in a playbook, specify: `cisco.aci.aci_access_span_dst_group`.

- [Synopsis](aci_access_span_dst_group_module.md#synopsis)
- [Parameters](aci_access_span_dst_group_module.md#parameters)
- [See Also](aci_access_span_dst_group_module.md#see-also)
- [Examples](aci_access_span_dst_group_module.md#examples)
- [Return Values](aci_access_span_dst_group_module.md#return-values)

## [Synopsis](aci_access_span_dst_group_module.md#id1)

- Manage Access SPAN destination groups on Cisco ACI fabrics.

## [Parameters](aci_access_span_dst_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_interface**  dictionary | The destination access interface.  The *access_interface* and *destination_epg* cannot be configured simultaneously. |
| **mtu**  integer | The MTU truncation size for the packets.  The APIC defaults to `1518` when unset during creation. |
| **node**  aliases: node_id  integer / required | The node id part of the destination path. |
| **path**  string / required | The interface part of the destination path.  When path is of type port a interface like `eth1/7` must be provided.  When path is of type direct_port_channel the name of a policy group like `test_PolGrp` must be provided. |
| **pod**  aliases: pod_id, pod_number  integer / required | The pod id part of the destination path. |
| **annotation**  string | User-defined string for annotating an object.  If the value is not specified in the task, the value of environment variable `ACI_ANNOTATION` will be used instead.  If the value is not specified in the task and environment variable `ACI_ANNOTATION` then the default value will be used.  **Default:** `"orchestrator:ansible"` |
| **certificate_name**  aliases: cert_name  string | The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.  If a `private_key` filename was provided, this defaults to the `private_key` basename, without extension.  If PEM-formatted content was provided for `private_key`, this defaults to the `username` value.  If the value is not specified in the task, the value of environment variable `ACI_CERTIFICATE_NAME` will be used instead. |
| **description**  aliases: descr  string | The description of the Access SPAN destination group. |
| **destination_epg**  dictionary | The destination end point group.  The *access_interface* and *destination_epg* cannot be configured simultaneously. |
| **ap**  aliases: ap_name, app_profile, app_profile_name  string / required | The name of application profile. |
| **destination_ip**  string / required | The destination IP address. |
| **dscp**  string | The DSCP value for sending the monitored packets using ERSPAN.  The APIC defaults to `unspecified` when unset during creation.  **Choices:**   - `"CS0"` - `"CS1"` - `"CS2"` - `"CS3"` - `"CS4"` - `"CS5"` - `"CS6"` - `"CS7"` - `"EF"` - `"VA"` - `"AF11"` - `"AF12"` - `"AF13"` - `"AF21"` - `"AF22"` - `"AF23"` - `"AF31"` - `"AF32"` - `"AF33"` - `"AF41"` - `"AF42"` - `"AF43"` - `"unspecified"` |
| **epg**  aliases: epg_name  string / required | The name of the end point group. |
| **flow_id**  integer | The flow ID of the SPAN packet.  The APIC defaults to `1` when unset during creation. |
| **mtu**  integer | The MTU truncation size for the packets.  The APIC defaults to `1518` when unset during creation. |
| **source_ip**  string / required | The source IP address or prefix. |
| **span_version**  string | The SPAN version.  The APIC defaults to `version_2` when unset during creation.  **Choices:**   - `"version_1"` - `"version_2"` |
| **tenant**  aliases: tenant_name  string / required | The name of the tenant. |
| **ttl**  integer | The time to live of the span session packets.  The APIC defaults to `64` when unset during creation. |
| **version_enforced**  boolean | Enforce SPAN version.  **Choices:**   - `false` - `true` |
| **destination_group**  aliases: name, dst_group  string | The name of the Access SPAN destination group. |
| **host**  aliases: hostname  string | IP Address or hostname of APIC resolvable by Ansible control host.  If the value is not specified in the task, the value of environment variable `ACI_HOST` will be used instead. |
| **name_alias**  string | The alias for the current object. This relates to the nameAlias field in ACI. |
| **output_level**  string | Influence the output of this ACI module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **output_path**  string | Path to a file that will be used to dump the ACI JSON configuration objects generated by the module.  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_PATH` will be used instead. |
| **owner_key**  string | User-defined string for the ownerKey attribute of an ACI object.  This attribute represents a key for enabling clients to own their data for entity correlation.  If the value is not specified in the task, the value of environment variable `ACI_OWNER_KEY` will be used instead. |
| **owner_tag**  string | User-defined string for the ownerTag attribute of an ACI object.  This attribute represents a tag for enabling clients to add their own data.  For example, to indicate who created this object.  If the value is not specified in the task, the value of environment variable `ACI_OWNER_TAG` will be used instead. |
| **password**  string | The password to use for authentication.  This option is mutual exclusive with `private_key`. If `private_key` is provided too, it will be used instead.  If the value is not specified in the task, the value of environment variables `ACI_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `ACI_PORT` will be used instead. |
| **private_key**  aliases: cert_key  string | Either a PEM-formatted private key file or the private key content used for signature-based authentication.  This value also influences the default `certificate_name` that is used.  This option is mutual exclusive with `password`. If `password` is provided too, it will be ignored.  If the value is not specified in the task, the value of environment variable `ACI_PRIVATE_KEY` or `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `ACI_TIMEOUT` will be used instead.  The default value is 30. |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `ACI_USE_PROXY` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `ACI_USE_SSL` will be used instead.  The default value is true when the connection is local.  **Choices:**   - `false` - `true` |
| **username**  aliases: user  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `ACI_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead.  The default value is admin. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `ACI_VALIDATE_CERTS` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |

## [See Also](aci_access_span_dst_group_module.md#id3)

> **See also:**
>
> [APIC Management Information Model reference](https://developer.cisco.com/docs/apic-mim-ref/)
> :   More information about the internal APIC class **span:DestGrp**.
>
> [Cisco ACI Guide](../../../scenario_guides/guide_aci.md#aci-guide)
> :   Detailed information on how to manage your ACI infrastructure using Ansible.
>
> [Developing Cisco ACI modules](https://docs.ansible.com/ansible/6/dev_guide/developing_modules_general_aci.html#aci-dev-guide "(in Ansible v6)")
> :   Detailed guide on how to write your own Cisco ACI modules to contribute.

## [Examples](aci_access_span_dst_group_module.md#id4)

```yaml+jinja
- name: Add a Access SPAN destination group of type EPG
  cisco.aci.aci_access_span_dst_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    destination_group: group1
    description: Test span
    destination_epg:
      tenant: Test1
      ap: ap1
      epg: ep1
      span_version: version_1
      version_enforced: false
      destination_ip: 10.0.0.1
      source_ip: 10.0.2.1
      ttl: 2
      mtu: 1500
      flow_id: 1
      dscp: CS1
    state: present
  delegate_to: localhost

- name: Add a Access SPAN destination group of type access interface port
  cisco.aci.aci_access_span_dst_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    destination_group: group1
    description: Test span
    access_interface:
      pod: 1
      node: 101
      path: 1/1
      mtu: 1500
    state: present
  delegate_to: localhost

- name: Add a Access SPAN destination group of type access interface direct_port_channel
  cisco.aci.aci_access_span_dst_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    destination_group: group1
    description: Test span
    access_interface:
      pod: 1
      node: 101
      path: Switch101_1-ports-1-2_PolGrp
      mtu: 1500
    state: present
  delegate_to: localhost

- name: Remove a Access SPAN destination group
  cisco.aci.aci_access_span_dst_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    destination_group: group1
    state: absent
  delegate_to: localhost

- name: Query a Access SPAN destination group
  cisco.aci.aci_access_span_dst_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    destination_group: group1
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all Access SPAN destination groups
  cisco.aci.aci_access_span_dst_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost
  register: query_result
```

## [Return Values](aci_access_span_dst_group_module.md#id5)

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

- Akini Ross (@akinross)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-aci/issues)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-aci)

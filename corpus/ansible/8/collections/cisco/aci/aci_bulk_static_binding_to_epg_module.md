---
collection: ansible
version: "8"
title: "cisco.aci.aci_bulk_static_binding_to_epg module – Bind static paths to EPGs (fv:RsPathAtt)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/aci/aci_bulk_static_binding_to_epg_module.html
fetched_at: 2026-07-28T01:19:00+00:00
---
# cisco.aci.aci_bulk_static_binding_to_epg module – Bind static paths to EPGs (fv:RsPathAtt)

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
> To use it in a playbook, specify: `cisco.aci.aci_bulk_static_binding_to_epg`.

- [Synopsis](aci_bulk_static_binding_to_epg_module.md#synopsis)
- [Parameters](aci_bulk_static_binding_to_epg_module.md#parameters)
- [Notes](aci_bulk_static_binding_to_epg_module.md#notes)
- [See Also](aci_bulk_static_binding_to_epg_module.md#see-also)
- [Examples](aci_bulk_static_binding_to_epg_module.md#examples)
- [Return Values](aci_bulk_static_binding_to_epg_module.md#return-values)

## [Synopsis](aci_bulk_static_binding_to_epg_module.md#id1)

- Bind static paths to EPGs on Cisco ACI fabrics.

## [Parameters](aci_bulk_static_binding_to_epg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **annotation**  string | User-defined string for annotating an object.  If the value is not specified in the task, the value of environment variable `ACI_ANNOTATION` will be used instead.  If the value is not specified in the task and environment variable `ACI_ANNOTATION` then the default value will be used.  **Default:** `"orchestrator:ansible"` |
| **ap**  aliases: app_profile, app_profile_name  string | The name of the application profile. |
| **certificate_name**  aliases: cert_name  string | The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.  If a `private_key` filename was provided, this defaults to the `private_key` basename, without extension.  If PEM-formatted content was provided for `private_key`, this defaults to the `username` value.  If the value is not specified in the task, the value of environment variable `ACI_CERTIFICATE_NAME` will be used instead. |
| **deploy_immediacy**  string | The Deployment Immediacy of Static EPG on PC, VPC or Interface.  The APIC defaults to `lazy` when unset during creation.  **Choices:**   - `"immediate"` - `"lazy"` |
| **description**  aliases: descr  string | Description for the static path to EPG binding. |
| **encap_id**  aliases: vlan, vlan_id  integer | The encapsulation ID associating the `epg` with the interface path.  This acts as the secondary `encap_id` when using micro-segmentation.  Accepted values are any valid encap ID for specified encap, currently ranges between `1` and `4096`. |
| **epg**  aliases: epg_name  string | The name of the end point group. |
| **host**  aliases: hostname  string | IP Address or hostname of APIC resolvable by Ansible control host.  If the value is not specified in the task, the value of environment variable `ACI_HOST` will be used instead. |
| **interface_configs**  list / elements=dictionary | List of interface configurations, elements in the form of a dictionary.  Module level attributes will be overridden by the path level attributes. |
| **deploy_immediacy**  string | The Deployment Immediacy of Static EPG on PC, VPC or Interface.  The APIC defaults to `lazy` when unset during creation.  **Choices:**   - `"immediate"` - `"lazy"` |
| **description**  aliases: descr  string | Description for the static path to EPG binding. |
| **encap_id**  aliases: vlan, vlan_id  integer | The encapsulation ID associating the `epg` with the interface path.  This acts as the secondary `encap_id` when using micro-segmentation.  Accepted values are any valid encap ID for specified encap, currently ranges between `1` and `4096`. |
| **extpaths**  list / elements=string | The `extpaths` integer value part of the tDn.  `extpaths` is only used if `interface_type` is `fex`, `fex_vpc` or `fex_port_channel`.  When `interface_type` is `fex_vpc`, then `extpaths` is a list with both fex IDs.  Usually something like `1011`. |
| **interface**  string / required | The `interface` string value part of the tDn.  Usually a policy group like `test-IntPolGrp` or an interface of the following format `1/7` depending on `interface_type`. |
| **interface_mode**  aliases: interface_mode_name, mode  string | Determines how layer 2 tags will be read from and added to frames.  Values `802.1p` and `native` are identical.  Values `access` and `untagged` are identical.  Values `regular`, `tagged` and `trunk` are identical.  The APIC defaults to `trunk` when unset during creation.  **Choices:**   - `"802.1p"` - `"access"` - `"native"` - `"regular"` - `"tagged"` - `"trunk"` - `"untagged"` |
| **interface_type**  string | The type of interface for the static EPG deployment.  **Choices:**   - `"fex"` - `"port_channel"` - `"switch_port"` - `"vpc"` - `"fex_port_channel"` - `"fex_vpc"` |
| **leafs**  aliases: leaves, nodes, paths, switches  list / elements=string / required | The switch ID(s) that the `interface` belongs to.  When `interface_type` is `switch_port`, `port_channel`, or `fex`, then `leafs` is a string of the leaf ID.  When `interface_type` is `vpc`, then `leafs` is a list with both leaf IDs.  The `leafs` value is usually something like ‘101’ or ‘101-102’ depending on `connection_type`. |
| **pod_id**  aliases: pod, pod_number  integer / required | The pod number part of the tDn.  `pod_id` is usually an integer below `10`. |
| **primary_encap_id**  aliases: primary_vlan, primary_vlan_id  string | Determines the primary encapsulation ID associating the `epg` with the interface path when using micro-segmentation.  Accepted values are any valid encap ID for specified encap, currently ranges between `1` and `4096` and `unknown`.  `unknown` is the default value and using `unknown` disables the Micro-Segmentation. |
| **interface_mode**  aliases: interface_mode_name, mode  string | Determines how layer 2 tags will be read from and added to frames.  Values `802.1p` and `native` are identical.  Values `access` and `untagged` are identical.  Values `regular`, `tagged` and `trunk` are identical.  The APIC defaults to `trunk` when unset during creation.  **Choices:**   - `"802.1p"` - `"access"` - `"native"` - `"regular"` - `"tagged"` - `"trunk"` - `"untagged"` |
| **interface_type**  string | The type of interface for the static EPG deployment.  **Choices:**   - `"fex"` - `"port_channel"` - `"switch_port"` ← (default) - `"vpc"` - `"fex_port_channel"` - `"fex_vpc"` |
| **output_level**  string | Influence the output of this ACI module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **output_path**  string | Path to a file that will be used to dump the ACI JSON configuration objects generated by the module.  If the value is not specified in the task, the value of environment variable `ACI_OUTPUT_PATH` will be used instead. |
| **password**  string | The password to use for authentication.  This option is mutual exclusive with `private_key`. If `private_key` is provided too, it will be used instead.  If the value is not specified in the task, the value of environment variables `ACI_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `ACI_PORT` will be used instead. |
| **primary_encap_id**  aliases: primary_vlan, primary_vlan_id  string | Determines the primary encapsulation ID associating the `epg` with the interface path when using micro-segmentation.  Accepted values are any valid encap ID for specified encap, currently ranges between `1` and `4096` and `unknown`.  `unknown` is the default value and using `unknown` disables the Micro-Segmentation. |
| **private_key**  aliases: cert_key  string | Either a PEM-formatted private key file or the private key content used for signature-based authentication.  This value also influences the default `certificate_name` that is used.  This option is mutual exclusive with `password`. If `password` is provided too, it will be ignored.  If the value is not specified in the task, the value of environment variable `ACI_PRIVATE_KEY` or `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **tenant**  aliases: tenant_name  string | Name of the tenant. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `ACI_TIMEOUT` will be used instead.  The default value is 30. |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `ACI_USE_PROXY` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `ACI_USE_SSL` will be used instead.  The default value is true when the connection is local.  **Choices:**   - `false` - `true` |
| **username**  aliases: user  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `ACI_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead.  The default value is admin. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `ACI_VALIDATE_CERTS` will be used instead.  The default value is true.  **Choices:**   - `false` - `true` |

## [Notes](aci_bulk_static_binding_to_epg_module.md#id3)

> **Note:**
>
> - The `tenant`, `ap`, `epg` used must exist before using this module in your playbook. The [cisco.aci.aci_tenant](aci_tenant_module.md#ansible-collections-cisco-aci-aci-tenant-module), [cisco.aci.aci_ap](aci_ap_module.md#ansible-collections-cisco-aci-aci-ap-module), [cisco.aci.aci_epg](aci_epg_module.md#ansible-collections-cisco-aci-aci-epg-module) modules can be used for this.

## [See Also](aci_bulk_static_binding_to_epg_module.md#id4)

> **See also:**
>
> [cisco.aci.aci_tenant](aci_tenant_module.md#ansible-collections-cisco-aci-aci-tenant-module)
> :   Manage tenants (fv:Tenant).
>
> [cisco.aci.aci_ap](aci_ap_module.md#ansible-collections-cisco-aci-aci-ap-module)
> :   Manage top level Application Profile (AP) objects (fv:Ap).
>
> [cisco.aci.aci_epg](aci_epg_module.md#ansible-collections-cisco-aci-aci-epg-module)
> :   Manage End Point Groups (EPG) objects (fv:AEPg).
>
> [APIC Management Information Model reference](https://developer.cisco.com/docs/apic-mim-ref/)
> :   More information about the internal APIC class **fv:RsPathAtt**.
>
> [Cisco ACI Guide](../../../scenario_guides/guide_aci.md#aci-guide)
> :   Detailed information on how to manage your ACI infrastructure using Ansible.
>
> [Developing Cisco ACI modules](https://docs.ansible.com/ansible/6/dev_guide/developing_modules_general_aci.html#aci-dev-guide "(in Ansible v6)")
> :   Detailed guide on how to write your own Cisco ACI modules to contribute.

## [Examples](aci_bulk_static_binding_to_epg_module.md#id5)

```yaml+jinja
- name: Create list of interfaces using module level attributes
  cisco.aci.aci_bulk_static_binding_to_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: accessport-code-cert
    ap: accessport_code_app
    epg: accessport_epg1
    encap_id: 221
    interface_mode: trunk
    deploy_immediacy: lazy
    description: "Module level attributes used to create interfaces"
    interface_configs:
      - interface: 1/7
        leafs: 101
        pod: 1
      - interface: 1/7
        leafs: 107
        pod: 7
      - interface: 1/8
        leafs: 108
        pod: 8
        encap_id: 108
    state: present
  delegate_to: localhost

- name: Create/Update list of interfaces using path level attributes
  cisco.aci.aci_bulk_static_binding_to_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: accessport-code-cert
    ap: accessport_code_app
    epg: accessport_epg1
    interface_configs:
      - interface: 1/7
        leafs: 101
        pod: 1
        encap_id: 221
        interface_mode: trunk
        deploy_immediacy: lazy
        description: "Path level attributes used to create/update interfaces"
      - interface: 1/7
        leafs: 107
        pod: 7
        encap_id: 221
        interface_mode: trunk
        deploy_immediacy: lazy
        description: "Path level attributes used to create/update interfaces"
      - interface: 1/8
        leafs: 108
        pod: 8
        encap_id: 108
        interface_mode: trunk
        deploy_immediacy: lazy
        description: "Path level attributes used to create/update interfaces"
    state: present
  delegate_to: localhost

- name: Query all interfaces of an EPG
  cisco.aci.aci_bulk_static_binding_to_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: accessport-code-cert
    ap: accessport_code_app
    epg: accessport_epg1
    state: query
  delegate_to: localhost

- name: Query all interfaces
  cisco.aci.aci_bulk_static_binding_to_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost

- name: Remove list of interfaces
  cisco.aci.aci_bulk_static_binding_to_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: accessport-code-cert
    ap: accessport_code_app
    epg: accessport_epg1
    encap_id: 221
    interface_mode: trunk
    deploy_immediacy: lazy
    interface_configs:
      - interface: 1/7
        leafs: 101
        pod: 1
      - interface: 1/7
        leafs: 107
        pod: 7
      - interface: 1/8
        leafs: 108
        pod: 8
        encap_id: 108
    state: absent
  delegate_to: localhost
```

## [Return Values](aci_bulk_static_binding_to_epg_module.md#id6)

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
- Marcel Zehnder (@maercu)
- Sabari Jaganathan (@sajagana)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-aci/issues)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-aci)

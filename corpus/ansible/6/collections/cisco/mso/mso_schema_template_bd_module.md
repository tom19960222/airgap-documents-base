---
collection: ansible
version: "6"
title: "cisco.mso.mso_schema_template_bd module – Manage Bridge Domains (BDs) in schema templates"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/mso/mso_schema_template_bd_module.html
fetched_at: 2026-07-27T17:01:11+00:00
---
# cisco.mso.mso_schema_template_bd module – Manage Bridge Domains (BDs) in schema templates

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
> see [Requirements](mso_schema_template_bd_module.md#ansible-collections-cisco-mso-mso-schema-template-bd-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_schema_template_bd`.

- [Synopsis](mso_schema_template_bd_module.md#synopsis)
- [Requirements](mso_schema_template_bd_module.md#requirements)
- [Parameters](mso_schema_template_bd_module.md#parameters)
- [Notes](mso_schema_template_bd_module.md#notes)
- [Examples](mso_schema_template_bd_module.md#examples)

## [Synopsis](mso_schema_template_bd_module.md#id1)

- Manage BDs in schema templates on Cisco ACI Multi-Site.

## [Requirements](mso_schema_template_bd_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_schema_template_bd_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **arp_flooding**  boolean | ARP Flooding  Choices:   - `false` - `true` |
| **bd**  aliases: name  string | The name of the BD to manage. |
| **description**  string | The description of BD is supported on versions of MSO that are 3.3 or greater. |
| **dhcp_policies**  list / elements=dictionary | A list DHCP Policies to be assciated with the BD  This option can only be used on versions of MSO that are 3.1.1h or greater. |
| **dhcp_option_policy**  dictionary | The DHCP Option Policy |
| **name**  string / required | The name of the DHCP Option Policy |
| **version**  integer / required | The version of the DHCP Option Policy |
| **name**  string / required | The name of the DHCP Relay Policy |
| **version**  integer / required | The version of DHCP Relay Policy |
| **dhcp_policy**  dictionary | The DHCP Policy |
| **dhcp_option_policy**  dictionary | The DHCP Option Policy |
| **name**  string / required | The name of the DHCP Option Policy |
| **version**  integer / required | The version of the DHCP Option Policy |
| **name**  string / required | The name of the DHCP Relay Policy |
| **version**  integer / required | The version of DHCP Relay Policy |
| **display_name**  string | The name as displayed on the MSO web interface. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **intersite_bum_traffic**  boolean | Whether to allow intersite BUM traffic.  Choices:   - `false` - `true` |
| **ipv6_unknown_multicast_flooding**  string | IPv6 Unknown Multicast Flooding can either be Flood or Optimized Flooding  Choices:   - `"flood"` - `"optimized_flooding"` |
| **layer2_stretch**  boolean | Whether to enable L2 stretch.  Choices:   - `false` - `true` ← (default) |
| **layer2_unknown_unicast**  string | Layer2 unknown unicast.  Choices:   - `"flood"` - `"proxy"` |
| **layer3_multicast**  boolean | Whether to enable L3 multicast.  Choices:   - `false` - `true` |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead. |
| **multi_destination_flooding**  string | Multi-Destination Flooding can either be Flood in BD, Drop or Flood in Encapsulation.  Flood in Encapsulation is only supported on versions of MSO that are 3.3 or greater.  Choices:   - `"flood_in_bd"` - `"drop"` - `"encap-flood"` |
| **optimize_wan_bandwidth**  boolean | Whether to optimize WAN bandwidth.  Choices:   - `false` - `true` |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  Choices:   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **schema**  string / required | The name of the schema. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **subnets**  list / elements=dictionary | The subnets associated to this BD. |
| **description**  string | The description of this subnet. |
| **no_default_gateway**  boolean | Whether this subnet has a default gateway.  Choices:   - `false` ← (default) - `true` |
| **primary**  boolean | Treat as Primary Subnet.  There can be only one primary subnet per address family under a BD.  This option can only be used on versions of MSO that are 3.1.1h or greater.  Choices:   - `false` ← (default) - `true` |
| **querier**  boolean | Whether this subnet is an IGMP querier.  Choices:   - `false` ← (default) - `true` |
| **scope**  string | The scope of the subnet.  Choices:   - `"private"` ← (default) - `"public"` |
| **shared**  boolean | Whether this subnet is shared between VRFs.  Choices:   - `false` ← (default) - `true` |
| **subnet**  aliases: ip  string / required | The IP range in CIDR notation. |
| **virtual**  boolean | Treat as Virtual IP Address.  Choices:   - `false` ← (default) - `true` |
| **template**  string / required | The name of the template.  Display Name of template for operations can only be used in some versions of mso.  Use the name of template instead of Display Name to avoid discrepency. |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead.  Default: `30` |
| **unicast_routing**  boolean | Unicast Routing  This option can only be used on versions of MSO that are 3.1.1h or greater.  Choices:   - `false` - `true` |
| **unknown_multicast_flooding**  string | Unknown Multicast Flooding can either be Flood or Optimized Flooding.  Choices:   - `"flood"` - `"optimized_flooding"` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `no` when using a HTTPAPI connection plugin (mso or nd) and `yes` when using the legacy connection method (only for mso).  Choices:   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **virtual_mac_address**  string | Virtual MAC Address |
| **vrf**  dictionary | The VRF associated to this BD. This is required only when creating a new BD. |
| **name**  string / required | The name of the VRF to associate with. |
| **schema**  string | The schema that defines the referenced VRF.  If this parameter is unspecified, it defaults to the current schema. |
| **template**  string | The template that defines the referenced VRF.  If this parameter is unspecified, it defaults to the current template. |

## [Notes](mso_schema_template_bd_module.md#id4)

> **Note:**
>
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [Examples](mso_schema_template_bd_module.md#id5)

```yaml+jinja
- name: Add a new BD
  cisco.mso.mso_schema_template_bd:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    bd: BD 1
    vrf:
      name: VRF1
    state: present
  delegate_to: localhost

- name: Add a new BD from another Schema
  mso_schema_template_bd:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    bd: BD 1
    vrf:
      name: VRF1
      schema: Schema Origin
      template: Template Origin
    state: present
  delegate_to: localhost

- name: Add bd with options available on version 3.1
  mso_schema_template_bd:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    bd: BD 1
    intersite_bum_traffic: true
    optimize_wan_bandwidth: false
    layer2_stretch: true
    layer2_unknown_unicast: flood
    layer3_multicast: false
    unknown_multicast_flooding: flood
    multi_destination_flooding: drop
    ipv6_unknown_multicast_flooding: flood
    arp_flooding: false
    virtual_mac_address: 00:00:5E:00:01:3C
    subnets:
    - subnet: 10.0.0.128/24
    - subnet: 10.0.1.254/24
      description: 1234567890
    - ip: 192.168.0.254/24
      description: "My description for a subnet"
      scope: private
      shared: false
      no_default_gateway: true
    vrf:
      name: vrf1
      schema: Test
      template: Template1
    dhcp_policy:
      name: ansible_test
      version: 1
      dhcp_option_policy:
        name: ansible_test_option
        version: 1
    state: present

- name: Add bd with options available on version 3.1.1h or greater
  mso_schema_template_bd:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    bd: BD 1
    intersite_bum_traffic: true
    optimize_wan_bandwidth: false
    layer2_stretch: true
    layer2_unknown_unicast: flood
    layer3_multicast: false
    unknown_multicast_flooding: flood
    multi_destination_flooding: drop
    ipv6_unknown_multicast_flooding: flood
    arp_flooding: false
    virtual_mac_address: 00:00:5E:00:01:3C
    unicast_routing: true
    subnets:
    - subnet: 10.0.0.128/24
      primary: true
    - subnet: 10.0.1.254/24
      description: 1234567890
      virtual: true
    - ip: 192.168.0.254/24
      description: "My description for a subnet"
      scope: private
      shared: false
      no_default_gateway: true
    vrf:
      name: vrf1
      schema: Schema1
      template: Template1
    dhcp_policies:
      - name: ansible_test
        version: 1
        dhcp_option_policy:
          name: ansible_test_option
          version: 1
      - name: ansible_test2
        version: 1
        dhcp_option_policy:
          name: ansible_test_option2
          version: 1
      - name: ansible_test3
        version: 1
        dhcp_option_policy:
          name: ansible_test_option
          version: 1
    state: present
  delegate_to: localhost

- name: Remove a BD
  cisco.mso.mso_schema_template_bd:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    bd: BD1
    state: absent
  delegate_to: localhost

- name: Query a specific BD
  cisco.mso.mso_schema_template_bd:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    bd: BD1
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all BDs
  cisco.mso.mso_schema_template_bd:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    schema: Schema 1
    template: Template 1
    state: query
  delegate_to: localhost
  register: query_result
```

### Authors

- Dag Wieers (@dagwieers)
- Shreyas Srish (@shrsr)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
[Homepage](https://cisco.com/go/aci)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

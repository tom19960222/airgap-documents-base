---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_routedomain module – Manage route domains on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_routedomain_module.html
fetched_at: 2026-07-27T17:27:41+00:00
---
# f5networks.f5_modules.bigip_routedomain module – Manage route domains on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_routedomain`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_routedomain_module.md#synopsis)
- [Parameters](bigip_routedomain_module.md#parameters)
- [Notes](bigip_routedomain_module.md#notes)
- [Examples](bigip_routedomain_module.md#examples)
- [Return Values](bigip_routedomain_module.md#return-values)

## [Synopsis](bigip_routedomain_module.md#id1)

- Manage route domains on a BIG-IP system. A route domain is a BIG-IP configuration object that isolates network traffic for a particular application on the network.

## [Parameters](bigip_routedomain_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bwc_policy**  string | The bandwidth controller for the route domain. |
| **connection_limit**  integer | The maximum number of concurrent connections allowed for the route domain. Setting this to `0` turns off connection limits. |
| **description**  string | Specifies descriptive text that identifies the route domain. |
| **flow_eviction_policy**  string | The eviction policy to use with this route domain. Apply an eviction policy to provide customized responses to flow overflows and slow flows on the route domain. |
| **fw_enforced_policy**  string | Specifies an AFM policy to be attached to route domain.  To remove attached AFM policy use `""` or `none` as values. |
| **id**  integer | The unique identifying integer representing the route domain.  This field is required when creating a new route domain.  In version 2.5, this value is no longer used to reference a route domain when making modifications to it (for instance during update and delete operations). Instead, the `name` parameter is used. In version 2.6, the `name` value will become a required parameter. |
| **name**  string | The name of the route domain. |
| **parent**  string | Specifies the route domain the system searches when it cannot find a route in the configured domain. |
| **partition**  string | Partition on which you want to create the route domain. Partitions cannot be updated once they are created.  Default: `"Common"` |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **routing_protocol**  list / elements=string | Dynamic routing protocols for the system to use in the route domain.  Choices:   - `"none"` - `"BFD"` - `"BGP"` - `"IS-IS"` - `"OSPFv2"` - `"OSPFv3"` - `"PIM"` - `"RIP"` - `"RIPng"` |
| **service_policy**  string | Service policy to associate with the route domain. |
| **state**  string | Whether the route domain should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **strict**  boolean | Specifies whether the system enforces cross-routing restrictions or not.  Choices:   - `false` - `true` |
| **vlans**  list / elements=string | VLANs for the system to use in the route domain. |

## [Notes](bigip_routedomain_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_routedomain_module.md#id4)

```yaml+jinja
- name: Create a route domain
  bigip_routedomain:
    name: foo
    id: 1234
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Set VLANs on the route domain
  bigip_routedomain:
    name: bar
    state: present
    vlans:
      - net1
      - foo
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_routedomain_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bwc_policy**  string | The new bandwidth controller.  Returned: changed  Sample: `"/Common/foo"` |
| **connection_limit**  integer | The new connection limit for the route domain.  Returned: changed  Sample: `100` |
| **description**  string | The description of the route domain.  Returned: changed  Sample: `"route domain foo"` |
| **flow_eviction_policy**  string | The new eviction policy to use with this route domain.  Returned: changed  Sample: `"/Common/default-eviction-policy"` |
| **fw_enforced_policy**  string | Specifies the AFM policy to be attached to route domain.  Returned: changed  Sample: `"/Common/afm-blocking-policy"` |
| **id**  integer | The ID of the route domain that was changed.  Returned: changed  Sample: `2` |
| **parent**  integer | The new parent route domain.  Returned: changed  Sample: `0` |
| **routing_protocol**  list / elements=string | List of routing protocols applied to the route domain.  Returned: changed  Sample: `["bfd", "bgp"]` |
| **service_policy**  string | The new service policy to use with this route domain.  Returned: changed  Sample: `"/Common-my-service-policy"` |
| **strict**  string | The new strict isolation setting.  Returned: changed  Sample: `"enabled"` |
| **vlans**  list / elements=string | List of new VLANs to which the route domain is applied.  Returned: changed  Sample: `["/Common/http-tunnel", "/Common/socks-tunnel"]` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

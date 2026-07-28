---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_selfip module – Manage Self-IPs on a BIG-IP system"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_selfip_module.html
fetched_at: 2026-07-27T17:27:42+00:00
---
# f5networks.f5_modules.bigip_selfip module – Manage Self-IPs on a BIG-IP system

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_selfip`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_selfip_module.md#synopsis)
- [Parameters](bigip_selfip_module.md#parameters)
- [Notes](bigip_selfip_module.md#notes)
- [Examples](bigip_selfip_module.md#examples)
- [Return Values](bigip_selfip_module.md#return-values)

## [Synopsis](bigip_selfip_module.md#id1)

- Manage Self-IP addresses on a BIG-IP system.

## [Parameters](bigip_selfip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | The IP addresses for the new self IP. This value is ignored upon update as addresses themselves cannot be changed after they are created.  This value is required when creating new self IPs. |
| **allow_service**  list / elements=string | Configure port lockdown for the self IP. By default, the self IP has a “default deny” policy. This can be changed to allow TCP and UDP ports, as well as specific protocols. This list should contain `protocol`:`port` values. |
| **description**  string | Description of the traffic selector. |
| **fw_enforced_policy**  string  added in f5networks.f5_modules 1.1.0 | Specifies an AFM policy to attach to Self IP. |
| **name**  string / required | The name of the self IP to create.  If this parameter is not specified, it defaults to the value supplied in the `address` parameter. |
| **netmask**  string | The netmask for the self IP. When creating a new self IP, this value is required. |
| **partition**  string | Device partition to manage resources on. You can set different partitions for self IPs, but the address used may not match any other address used by a self IP. Thus, self IPs are not isolated by partitions as other resources on a BIG-IP are.  Default: `"Common"` |
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
| **route_domain**  integer | The route domain id of the system. When creating a new self IP, if this value is not specified, the default value is `0`.  This value cannot be changed after it is set. |
| **state**  string | When `present`, guarantees the self IP exists with the provided attributes.  When `absent`, removes the self IP from the system.  Choices:   - `"absent"` - `"present"` ← (default) |
| **traffic_group**  string | The traffic group for the self IP addresses in an active-active, redundant load balancer configuration. When creating a new self IP, if this value is not specified, the default is `/Common/traffic-group-local-only`. |
| **vlan**  string | The VLAN for the new self IPs. When creating a new self IP, this value is required. |

## [Notes](bigip_selfip_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_selfip_module.md#id4)

```yaml+jinja
- name: Create Self IP
  bigip_selfip:
    address: 10.10.10.10
    name: self1
    netmask: 255.255.255.0
    vlan: vlan1
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create Self IP with a Route Domain
  bigip_selfip:
    name: self1
    address: 10.10.10.10
    netmask: 255.255.255.0
    vlan: vlan1
    route_domain: 10
    allow_service: default
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Delete Self IP
  bigip_selfip:
    name: self1
    state: absent
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Allow management web UI to be accessed on this Self IP
  bigip_selfip:
    name: self1
    state: absent
    allow_service:
      - tcp:443
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Allow HTTPS and SSH access to this Self IP
  bigip_selfip:
    name: self1
    state: absent
    allow_service:
      - tcp:443
      - tcp:22
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Allow all services access to this Self IP
  bigip_selfip:
    name: self1
    state: absent
    allow_service:
      - all
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Allow only GRE and IGMP protocols access to this Self IP
  bigip_selfip:
    name: self1
    state: absent
    allow_service:
      - gre:0
      - igmp:0
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Allow all TCP, but no other protocols access to this Self IP
  bigip_selfip:
    name: self1
    state: absent
    allow_service:
      - tcp:0
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_selfip_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address**  string | The address for the self IP.  Returned: changed  Sample: `"192.0.2.10"` |
| **allow_service**  list / elements=string | Services that are allowed via this self IP.  Returned: changed  Sample: `["igmp:0", "tcp:22", "udp:53"]` |
| **fw_enforced_policy**  string | Specifies an AFM policy to be attached to the self IP.  Returned: changed  Sample: `"/Common/afm-blocking-policy"` |
| **name**  string | The name of the self IP.  Returned: created  Sample: `"self1"` |
| **netmask**  string | The netmask of the self IP.  Returned: changed  Sample: `"255.255.255.0"` |
| **traffic_group**  string | The traffic group of which the self IP is a member.  Returned: changed  Sample: `"traffic-group-local-only"` |
| **vlan**  string | The VLAN set on the self IP.  Returned: changed  Sample: `"vlan1"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

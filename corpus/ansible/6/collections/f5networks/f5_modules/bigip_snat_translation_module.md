---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_snat_translation module – Manage SNAT translations on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_snat_translation_module.html
fetched_at: 2026-07-27T17:27:45+00:00
---
# f5networks.f5_modules.bigip_snat_translation module – Manage SNAT translations on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_snat_translation`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_snat_translation_module.md#synopsis)
- [Parameters](bigip_snat_translation_module.md#parameters)
- [Notes](bigip_snat_translation_module.md#notes)
- [Examples](bigip_snat_translation_module.md#examples)
- [Return Values](bigip_snat_translation_module.md#return-values)

## [Synopsis](bigip_snat_translation_module.md#id1)

- Manage SNAT translations on a BIG-IP system.

## [Parameters](bigip_snat_translation_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  aliases: ip  string | Specifies the IP address of the SNAT translation. When `state` is `present`, `enabled`, or `disabled`, this parameter is required.  This parameter cannot be updated after it is set. |
| **arp**  boolean | If `yes`, specifies the NAT sends ARP requests.  Choices:   - `false` - `true` |
| **connection_limit**  integer | Specifies a limit on the number of connections a translation address must reach before it no longer initiates a connection. The default value of `0` indicates the setting is disabled.  The accepted value range is `0 - 65535`. |
| **description**  string | Description of snat-translation. `none or ''` sets a default description of null. |
| **ip_idle_timeout**  string | Specifies the amount of time connections to an IP address initiated using a SNAT address are allowed to remain idle before being automatically disconnected. `indefinite` prevents the connection from timing out.  The accepted value range is `0 - 4294967295` seconds. Specifying `indefinite` sets it to the maximum value. |
| **name**  string / required | The name of SNAT translation. |
| **partition**  string | Device partition to manage resources on.  Required with state `absent` when a partition other than Common is used. |
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
| **state**  string | The SNAT translation state. If `absent`, deletes the SNAT translation if it exists. `present` creates the SNAT translation and enables it. If `enabled`, enables the SNAT translation if it exists. If `disabled`, creates the SNAT translation if needed, and sets the state to `disabled`.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |
| **tcp_idle_timeout**  string | Specifies the amount of time that TCP connections initiated using a SNAT address are allowed to remain idle before being automatically disconnected. `indefinite` prevents the connection from timing out.  The accepted value range is `0 - 4294967295` seconds. Specifying `indefinite` sets it to the maximum value. |
| **traffic_group**  string | The traffic group for the snat-translation address. When creating a new address, if this value is not specified, the default is `/Common/traffic-group-1`. |
| **udp_idle_timeout**  string | Specifies the amount of time UDP connections initiated using a SNAT address are allowed to remain idle before being automatically disconnected. `indefinite` prevents the connection from timing out.  The accepted value range is `0 - 4294967295` seconds. Specifying `indefinite` sets it to the maximum value. |

## [Notes](bigip_snat_translation_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_snat_translation_module.md#id4)

```yaml+jinja
- name: Create a SNAT translation 'my-snat-translation'
  bigip_snat_translation:
    name: my-snat-pool
    state: present
    address: 10.10.10.10
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Modify a SNAT translation 'my-snat-translation'
  bigip_snat_translation:
    name: my-snat-pool
    state: present
    address: 10.10.10.10
    arp: no
    connection_limit: 300
    ip_idle_timeout: 1800
    tcp_idle_timeout: 1800
    udp_idle_timeout: 1800
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Disable a SNAT translation 'my-snat-translation'
  bigip_snat_translation:
    name: my-snat-pool
    state: disabled
    address: 10.10.10.10
    arp: no
    connection_limit: 300
    ip_idle_timeout: 1800
    tcp_idle_timeout: 1800
    udp_idle_timeout: 1800
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Enable a SNAT translation 'my-snat-translation'
  bigip_snat_translation:
    name: my-snat-pool
    state: enabled
    address: 10.10.10.10
    arp: no
    connection_limit: 300
    ip_idle_timeout: 1800
    tcp_idle_timeout: 1800
    udp_idle_timeout: 1800
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Create using partition other then /Common on a SNAT translation 'my-new-snat-translation'
  bigip_snat_translation:
    name: my-new-snat-pool
    state: enabled
    address: 10.10.10.10
    arp: no
    connection_limit: 300
    ip_idle_timeout: 1800
    partition: ansible
    tcp_idle_timeout: 1800
    udp_idle_timeout: 1800
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Modify using traffic group other then /Common/traffic-group-1 on a SNAT translation 'my-new-snat-translation'
  bigip_snat_translation:
    name: my-new-snat-pool
    state: enabled
    address: 10.10.10.10
    arp: no
    connection_limit: 300
    ip_idle_timeout: 1800
    partition: ansible
    tcp_idle_timeout: 1800
    traffic_group: /Common/ansible
    udp_idle_timeout: 1800
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_snat_translation_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address**  string | IP address used for SNAT translation.  Returned: changed and success  Sample: `"10.10.10.10"` |
| **arp**  boolean | Whether snat-translation sends arp requests.  Returned: changed  Sample: `true` |
| **connection_limit**  integer | The new connection limit of the virtual address.  Returned: changed  Sample: `1000` |
| **description**  string | Description of the snat-translation.  Returned: changed  Sample: `"My snat-translation"` |
| **ip_idle_timeout**  string | IP idle timeout value for the snat-translation.  Returned: changed  Sample: `"300"` |
| **state**  string | The new state of the snat-translation.  Returned: changed  Sample: `"disabled"` |
| **tcp_idle_timeout**  string | TCP idle timeout value for the snat-translation.  Returned: changed  Sample: `"1800"` |
| **traffic_group**  string | Assigned traffic group.  Returned: changed  Sample: `"/Common/traffic-group-1"` |
| **udp_idle_timeout**  string | UDP idle timeout value for the snat-translation.  Returned: changed  Sample: `"indefinite"` |

### Authors

- Greg Crosby (@crosbygw)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

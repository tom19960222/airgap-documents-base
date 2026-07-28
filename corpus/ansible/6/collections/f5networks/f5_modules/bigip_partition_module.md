---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_partition module – Manage BIG-IP partitions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_partition_module.html
fetched_at: 2026-07-27T17:27:22+00:00
---
# f5networks.f5_modules.bigip_partition module – Manage BIG-IP partitions

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_partition`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_partition_module.md#synopsis)
- [Parameters](bigip_partition_module.md#parameters)
- [Notes](bigip_partition_module.md#notes)
- [Examples](bigip_partition_module.md#examples)
- [Return Values](bigip_partition_module.md#return-values)

## [Synopsis](bigip_partition_module.md#id1)

- Manage partitions on the BIG-IP.

## [Parameters](bigip_partition_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | The description to attach to the partition. |
| **name**  string / required | Name of the partition. |
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
| **route_domain**  integer | The default Route Domain to assign to the partition. If no route domain is specified, the default route domain for the system (typically zero) will be used only when creating a new partition. |
| **state**  string | Whether the partition should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_partition_module.md#id3)

> **Note:**
>
> - Requires BIG-IP software version >= 12
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_partition_module.md#id4)

```yaml+jinja
- name: Create partition "foo" using the default route domain
  bigip_partition:
    name: foo
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create partition "bar" using a custom route domain
  bigip_partition:
    name: bar
    route_domain: 3
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Change route domain of partition "foo"
  bigip_partition:
    name: foo
    route_domain: 8
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set a description for partition "foo"
  bigip_partition:
    name: foo
    description: Tenant CompanyA
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Delete the "foo" partition
  bigip_partition:
    name: foo
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_partition_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The description of the partition.  Returned: changed and success  Sample: `"Example partition"` |
| **route_domain**  integer | Name of the route domain associated with the partition.  Returned: changed and success  Sample: `0` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

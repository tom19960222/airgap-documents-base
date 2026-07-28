---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_snat_pool module – Manage SNAT pools on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_snat_pool_module.html
fetched_at: 2026-07-28T02:07:15+00:00
---
# f5networks.f5_modules.bigip_snat_pool module – Manage SNAT pools on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_snat_pool`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_snat_pool_module.md#synopsis)
- [Parameters](bigip_snat_pool_module.md#parameters)
- [Notes](bigip_snat_pool_module.md#notes)
- [Examples](bigip_snat_pool_module.md#examples)
- [Return Values](bigip_snat_pool_module.md#return-values)

## [Synopsis](bigip_snat_pool_module.md#id1)

- Manage SNAT pools on a BIG-IP system.

## [Parameters](bigip_snat_pool_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | An optional description of the SNAT pool. |
| **members**  aliases: member  list / elements=string | List of members to put in the SNAT pool. When `state` is `present`, this parameter is required, otherwise it is optional.  The members can be either IP addresses or names of the SNAT translation objects. |
| **name**  string / required | The name of the SNAT pool. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **provider**  dictionary  *added in f5networks.f5_modules 1.0.0* | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP or the BIG-IQ.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host or the BIG-IQ host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  **Default:** `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP or the BIG-IQ. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | Whether the SNAT pool should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_snat_pool_module.md#id3)

> **Note:**
>
> - When the `bigip_snat_pool` object is removed, it also removes any associated `bigip_snat_translation` objects.
> - This is a BIG-IP behavior not module behavior, and it only occurs when the `bigip_snat_translation` objects are also not referenced by another `bigip_snat_pool`.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_snat_pool_module.md#id4)

```yaml+jinja
- name: Add the SNAT pool 'my-snat-pool'
  bigip_snat_pool:
    name: my-snat-pool
    state: present
    members:
      - 10.10.10.10
      - 20.20.20.20
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Change the SNAT pool's members to a single member
  bigip_snat_pool:
    name: my-snat-pool
    state: present
    member: 30.30.30.30
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove the SNAT pool 'my-snat-pool'
  bigip_snat_pool:
    name: johnd
    state: absent
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add the SNAT pool 'my-snat-pool' with a description
  bigip_snat_pool:
    name: my-snat-pool
    state: present
    members:
      - 10.10.10.10
      - 20.20.20.20
    description: A SNAT pool description
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_snat_pool_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **members**  list / elements=string | List of members that are part of the SNAT pool.  **Returned:** changed and success  **Sample:** `["['10.10.10.10']"]` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

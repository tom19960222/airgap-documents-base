---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_device_auth_radius_server module – Manages the RADIUS server configuration of the device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_device_auth_radius_server_module.html
fetched_at: 2026-07-28T02:05:49+00:00
---
# f5networks.f5_modules.bigip_device_auth_radius_server module – Manages the RADIUS server configuration of the device

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_auth_radius_server`.

New in f5networks.f5_modules 1.3.0

- [Synopsis](bigip_device_auth_radius_server_module.md#synopsis)
- [Parameters](bigip_device_auth_radius_server_module.md#parameters)
- [Notes](bigip_device_auth_radius_server_module.md#notes)
- [Examples](bigip_device_auth_radius_server_module.md#examples)
- [Return Values](bigip_device_auth_radius_server_module.md#return-values)

## [Synopsis](bigip_device_auth_radius_server_module.md#id1)

- Manages a device’s RADIUS server configuration.
- Used in tandem with the `bigip_device_auth_radius` module.

## [Parameters](bigip_device_auth_radius_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | The description of the RADIUS server. |
| **ip**  string | The IP address of the server.  This parameter is mandatory when creating a new resource. |
| **name**  string / required | Specifies the name of the RADIUS server to manage. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **port**  integer | The port of the server.  Valid range of values is between `0` and `65535` inclusive. |
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
| **secret**  string | Specifies the secret used for accessing RADIUS server.  This parameter is mandatory when creating a new resource. |
| **state**  string | When `state` is `present`, ensures the RADIUS server exists.  When `state` is `absent`, ensures the RADIUS server is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Specifies the timeout value in seconds.  Valid range of values is between `1` and `60` inclusive. |
| **update_secret**  string | `always` will update passwords if the `secret` is specified.  `on_create` will only set the password for newly created servers.  **Choices:**   - `"always"` ← (default) - `"on_create"` |

## [Notes](bigip_device_auth_radius_server_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_auth_radius_server_module.md#id4)

```yaml+jinja
- name: Create a RADIUS server configuration
  bigip_device_auth_radius_server:
    name: "ansible_test"
    ip: "1.1.1.1"
    port: 1812
    secret: "secret"
    timeout: 5
    update_secret: on_create
    state: present
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Update RADIUS server configuration
  bigip_device_auth_radius_server:
    name: "ansible_test"
    ip: "10.10.10.1"
    description: "this is a test"
    port: 1813
    timeout: 10
    state: present
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove RADIUS server configuration
  bigip_device_auth_radius_server:
    name: "ansible_test"
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_device_auth_radius_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | User defined description of the RADIUS server.  **Returned:** changed  **Sample:** `"this is my server"` |
| **ip**  string | IP address of the RADIUS Server.  **Returned:** changed  **Sample:** `"1.1.1.1"` |
| **port**  integer | RADIUS service port.  **Returned:** changed  **Sample:** `1812` |
| **timeout**  integer | Timeout value.  **Returned:** changed  **Sample:** `3` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

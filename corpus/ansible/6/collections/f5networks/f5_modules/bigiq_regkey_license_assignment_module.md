---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigiq_regkey_license_assignment module – Manage regkey license assignment on BIG-IPs from a BIG-IQ"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigiq_regkey_license_assignment_module.html
fetched_at: 2026-07-27T17:28:11+00:00
---
# f5networks.f5_modules.bigiq_regkey_license_assignment module – Manage regkey license assignment on BIG-IPs from a BIG-IQ

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigiq_regkey_license_assignment`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigiq_regkey_license_assignment_module.md#synopsis)
- [Parameters](bigiq_regkey_license_assignment_module.md#parameters)
- [Notes](bigiq_regkey_license_assignment_module.md#notes)
- [Examples](bigiq_regkey_license_assignment_module.md#examples)

## [Synopsis](bigiq_regkey_license_assignment_module.md#id1)

- Manages the assignment of regkey licenses on a BIG-IQ. Assignment means the license is assigned to a BIG-IP, or it needs to be assigned to a BIG-IP. Additionally, this module supports revoking the assignments from BIG-IP devices.

## [Parameters](bigiq_regkey_license_assignment_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **device**  string / required | When `managed` is `no`, specifies the address, or hostname, where the BIG-IQ can reach the remote device to register.  When `managed` is `yes`, specifies the managed device, or device UUID, that you want to register.  If `managed` is `yes`, it is very important you do not have more than one device with the same name. BIG-IQ internally recognizes devices by their ID, and therefore, this module cannot guarantee the correct device will be registered. The device returned is the device that is used. |
| **device_password**  string | The password of the `device_username`.  When `managed` is `no`, this parameter is required. |
| **device_port**  integer | Specifies the port of the remote device to connect to.  If this parameter is not specified, the default is `443`.  Default: `443` |
| **device_username**  string | The username used to connect to the remote device.  This username should be one that has sufficient privileges on the remote device to do licensing. Usually this is the `Administrator` role.  When `managed` is `no`, this parameter is required. |
| **key**  string / required | The registration key you want to assign from the pool. |
| **managed**  boolean | Whether the specified device is a managed or un-managed device.  When `state` is `present`, this parameter is required.  Choices:   - `false` - `true` |
| **pool**  string / required | The registration key pool to use. |
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
| **state**  string | When `present`, ensures the device is assigned the specified license.  When `absent`, ensures the license is revoked from the remote device and freed on the BIG-IQ.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](bigiq_regkey_license_assignment_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigiq_regkey_license_assignment_module.md#id4)

```yaml+jinja
- name: Register an unmanaged device
  bigiq_regkey_license_assignment:
    pool: my-regkey-pool
    key: XXXX-XXXX-XXXX-XXXX-XXXX
    device: 1.1.1.1
    managed: no
    device_username: admin
    device_password: secret
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Register a managed device, by name
  bigiq_regkey_license_assignment:
    pool: my-regkey-pool
    key: XXXX-XXXX-XXXX-XXXX-XXXX
    device: bigi1.foo.com
    managed: yes
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Register a managed device, by UUID
  bigiq_regkey_license_assignment:
    pool: my-regkey-pool
    key: XXXX-XXXX-XXXX-XXXX-XXXX
    device: 7141a063-7cf8-423f-9829-9d40599fa3e0
    managed: yes
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

### Authors

- Tim Rupp (@caphrim007)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

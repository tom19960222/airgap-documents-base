---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_wait module – Wait for a BIG-IP condition before continuing"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_wait_module.html
fetched_at: 2026-07-27T17:28:04+00:00
---
# f5networks.f5_modules.bigip_wait module – Wait for a BIG-IP condition before continuing

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_wait`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_wait_module.md#synopsis)
- [Parameters](bigip_wait_module.md#parameters)
- [Notes](bigip_wait_module.md#notes)
- [Examples](bigip_wait_module.md#examples)

## [Synopsis](bigip_wait_module.md#id1)

- With this module, you can wait for BIG-IP to be “ready”, meaning the BIG-IP is ready to accept configuration.
- This module can take into account situations where the device is in the middle of rebooting due to a configuration change.

## [Parameters](bigip_wait_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **delay**  integer | Number of seconds to wait before starting to poll.  Default: `0` |
| **msg**  string | This overrides the normal error message from a failure to meet the required conditions. |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **ssh_keyfile**  path | Specifies the SSH keyfile to use to authenticate the connection to the remote device. This argument is only used for *cli* transports.  You may omit this option by setting the environment variable `ANSIBLE_NET_SSH_KEYFILE`. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **sleep**  integer | Number of seconds to sleep between checks. Before version 2.3 this was hardcoded to 1 second.  Default: `1` |
| **timeout**  integer | Maximum number of seconds to wait.  When used without other conditions, it is equivalent of just sleeping.  The default timeout is deliberately set to 2 hours because there is no individual REST API.  Default: `7200` |
| **type**  string | The type of the BIG-IP.  Defaults to `standard`, the other choice is `vcmp`.  This choice defines which module or service Ansible looks for to establish that the device has recovered, so ensure to specify the correct choice, especially when running this against VCMP.  Choices:   - `"standard"` ← (default) - `"vcmp"` |

## [Notes](bigip_wait_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_wait_module.md#id4)

```yaml+jinja
- name: Wait for BIG-IP to be ready to take configuration
  bigip_wait:
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Wait a maximum of 300 seconds for BIG-IP to be ready to take configuration
  bigip_wait:
    timeout: 300
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Wait for BIG-IP to be ready, don't start checking for 10 seconds
  bigip_wait:
    delay: 10
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_cli_script module – Manage CLI scripts on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_cli_script_module.html
fetched_at: 2026-07-27T17:26:18+00:00
---
# f5networks.f5_modules.bigip_cli_script module – Manage CLI scripts on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_cli_script`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_cli_script_module.md#synopsis)
- [Parameters](bigip_cli_script_module.md#parameters)
- [Notes](bigip_cli_script_module.md#notes)
- [Examples](bigip_cli_script_module.md#examples)
- [Return Values](bigip_cli_script_module.md#return-values)

## [Synopsis](bigip_cli_script_module.md#id1)

- Manages CLI scripts on a BIG-IP. CLI scripts, otherwise known as tmshell scripts or TMSH scripts, allow you to create custom scripts that can run to manage objects within a BIG-IP.

## [Parameters](bigip_cli_script_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **content**  string | The content of the script.  This parameter is typically used in conjunction with Ansible’s `file` or template lookup plugins. See the examples in this documentation. |
| **description**  string | Description of the cli script. |
| **name**  string / required | Specifies the name of the script. |
| **partition**  string | Device partition on which to manage resources.  Default: `"Common"` |
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
| **state**  string | When `present`, ensures the script exists.  When `absent`, ensures the script is removed.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_cli_script_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_cli_script_module.md#id4)

```yaml+jinja
- name: Create a cli script from an existing file
  bigip_cli_script:
    name: foo
    content: "{{ lookup('file', '/absolute/path/to/cli/script.tcl') }}"
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a cli script from a jinja template representing a cli script
  bigip_cli_script:
    name: foo
    content: "{{ lookup('template', '/absolute/path/to/cli/script.tcl') }}"
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_cli_script_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **param1**  boolean | The new param1 value of the resource.  Returned: changed  Sample: `true` |
| **param2**  string | The new param2 value of the resource.  Returned: changed  Sample: `"Foo is bar"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_config module – Manage BIG-IP configuration sections"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_config_module.html
fetched_at: 2026-07-27T17:26:20+00:00
---
# f5networks.f5_modules.bigip_config module – Manage BIG-IP configuration sections

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_config`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_config_module.md#synopsis)
- [Parameters](bigip_config_module.md#parameters)
- [Notes](bigip_config_module.md#notes)
- [Examples](bigip_config_module.md#examples)
- [Return Values](bigip_config_module.md#return-values)

## [Synopsis](bigip_config_module.md#id1)

- Manages a BIG-IP configuration by allowing TMSH commands that modify the running configuration, or merge SCF formatted files into the running configuration. Additionally, this module is of significant importance because it allows you to save your running configuration to disk. Since all F5 modules manipulate the running configuration, it is important you use this module to save that running config.

## [Parameters](bigip_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **merge_content**  string | Loads the specified configuration that you want to merge into the running configuration. This is equivalent to using the `tmsh` command `load sys config from-terminal merge`.  If you need to read the configuration from a file or template, use Ansible’s `file` or `template` lookup plugins respectively. |
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
| **reset**  boolean | Loads the default configuration on the device.  If this option is specified, the default configuration will be loaded before any commands or other provided configuration is run.  Choices:   - `false` ← (default) - `true` |
| **save**  boolean | The `save` argument instructs the module to save the running-config to startup-config.  This operation is performed after any changes are made to the current running config. If no changes are made, the configuration is still saved to the startup config.  This option will always cause the module to return **changed**.  Choices:   - `false` - `true` ← (default) |
| **verify**  boolean | Validates the specified configuration to see whether it is valid to replace the running configuration.  The running configuration will not be changed.  When this parameter is set to `yes`, no change will be reported by the module.  Choices:   - `false` ← (default) - `true` |

## [Notes](bigip_config_module.md#id3)

> **Note:**
>
> - This module requires that sys db variable on device `systemauth.disablebash` is set to `false`.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_config_module.md#id4)

```yaml+jinja
- name: Save the running configuration of the BIG-IP
  bigip_config:
    save: yes
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  delegate_to: localhost

- name: Reset the BIG-IP configuration, for example, to RMA the device
  bigip_config:
    reset: yes
    save: yes
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  delegate_to: localhost

- name: Load an SCF configuration
  bigip_config:
    merge_content: "{{ lookup('file', '/path/to/config.scf') }}"
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stdout**  list / elements=string | The set of responses from the options.  Returned: always  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list.  Returned: always  Sample: `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

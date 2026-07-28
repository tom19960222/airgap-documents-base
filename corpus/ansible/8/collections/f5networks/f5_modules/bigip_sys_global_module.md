---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_sys_global module – Manage BIG-IP global settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_sys_global_module.html
fetched_at: 2026-07-28T02:07:26+00:00
---
# f5networks.f5_modules.bigip_sys_global module – Manage BIG-IP global settings

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_sys_global`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_sys_global_module.md#synopsis)
- [Parameters](bigip_sys_global_module.md#parameters)
- [Notes](bigip_sys_global_module.md#notes)
- [Examples](bigip_sys_global_module.md#examples)
- [Return Values](bigip_sys_global_module.md#return-values)

## [Synopsis](bigip_sys_global_module.md#id1)

- Manage BIG-IP global settings.

## [Parameters](bigip_sys_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **banner_text**  string | Specifies the text to present in the advisory banner. |
| **console_timeout**  integer | Specifies the number of seconds of inactivity before the system logs off a user that is logged on. |
| **gui_audit**  boolean  *added in f5networks.f5_modules 1.23.0* | `true` or `false`, specifies whether or not system GUI log audit messages.  **Choices:**   - `false` - `true` |
| **gui_setup**  boolean | `true` or `false`, the Setup utility in the browser-based Configuration utility.  **Choices:**   - `false` - `true` |
| **lcd_display**  boolean | When `true`, specifies the system menu displays on the LCD screen on the front of the unit. This setting has no effect when used on the VE platform.  **Choices:**   - `false` - `true` |
| **mgmt_dhcp**  boolean | Specifies whether or not to enable DHCP client on the management interface.  **Choices:**   - `false` - `true` |
| **net_reboot**  boolean | When `true`, specifies the next time you reboot the system, the system boots to an ISO image on the network, rather than an internal media drive.  **Choices:**   - `false` - `true` |
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
| **quiet_boot**  boolean | When `true`, specifies the system suppresses informational text on the console during the boot cycle. When `no`, the system presents messages and informational text on the console during the boot cycle.  **Choices:**   - `false` - `true` |
| **security_banner**  boolean | Specifies whether the system displays an advisory message on the login screen.  **Choices:**   - `false` - `true` |
| **state**  string | The state of the variable on the system. When `present`, guarantees an existing variable is set to `value`.  **Choices:**   - `"present"` ← (default) |

## [Notes](bigip_sys_global_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_sys_global_module.md#id4)

```yaml+jinja
- name: Disable the setup utility
  bigip_sys_global:
    gui_setup: false
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_sys_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **banner_text**  string | The new text to present in the advisory banner.  **Returned:** changed  **Sample:** `"This is a corporate device. Do not touch."` |
| **console_timeout**  integer | The new number of seconds of inactivity before the system logs off a user that is logged on.  **Returned:** changed  **Sample:** `600` |
| **gui_audit**  boolean | The new setting for GUI auditing.  **Returned:** changed  **Sample:** `true` |
| **gui_setup**  boolean | The new setting for the Setup utility.  **Returned:** changed  **Sample:** `true` |
| **lcd_display**  boolean | The new setting for displaying the system menu on the LCD.  **Returned:** changed  **Sample:** `true` |
| **mgmt_dhcp**  boolean | The new setting for whether the mgmt interface should use DHCP or not.  **Returned:** changed  **Sample:** `true` |
| **net_reboot**  boolean | The new setting for whether the system should boot to an ISO on the network or not.  **Returned:** changed  **Sample:** `true` |
| **quiet_boot**  boolean | The new setting for whether the system should suppress information to the console during boot or not.  **Returned:** changed  **Sample:** `true` |
| **security_banner**  boolean | The new setting for whether the system should display an advisory message on the login screen or not.  **Returned:** changed  **Sample:** `true` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

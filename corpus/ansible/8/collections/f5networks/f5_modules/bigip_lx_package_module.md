---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_lx_package module – Manages Javascript LX packages on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_lx_package_module.html
fetched_at: 2026-07-28T02:06:33+00:00
---
# f5networks.f5_modules.bigip_lx_package module – Manages Javascript LX packages on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
> You need further requirements to be able to use this module,
> see [Requirements](bigip_lx_package_module.md#ansible-collections-f5networks-f5-modules-bigip-lx-package-module-requirements) for details.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_lx_package`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_lx_package_module.md#synopsis)
- [Requirements](bigip_lx_package_module.md#requirements)
- [Parameters](bigip_lx_package_module.md#parameters)
- [Notes](bigip_lx_package_module.md#notes)
- [Examples](bigip_lx_package_module.md#examples)

## [Synopsis](bigip_lx_package_module.md#id1)

- Manages Javascript LX packages on a BIG-IP. This module allows you to deploy LX packages to the BIG-IP and manage their lifecycle.

## [Requirements](bigip_lx_package_module.md#id2)

The below requirements are needed on the host that executes this module.

- Requires BIG-IP >= 12.1.0
- The ‘rpm’ tool installed on the Ansible controller

## [Parameters](bigip_lx_package_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **package**  path | The LX package that you want to upload or remove. When `state` is `present`, and you intend to use this module in a `role`, we recommend you use the `{{ role_path }}` variable. An example is provided in the `EXAMPLES` section.  When `state` is `absent`, it is not necessary for the package to exist on the Ansible controller. If the full path to the package is provided, the fileame will specifically be cherry-picked from it to properly remove the package. |
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
| **retain_package_file**  boolean  *added in f5networks.f5_modules 1.4.0* | Specifies whether the install file should be deleted on successful installation of the package.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Whether the LX package should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_lx_package_module.md#id4)

> **Note:**
>
> - Requires the RPM tool be installed on the host. This can be accomplished in different ways on each platform. On Debian based systems with `apt`; `apt-get install rpm`. On Mac with `brew`; `brew install rpm`. This command is already present on RedHat based systems.
> - Requires BIG-IP >= 12.1.0, because the required functionality is missing on prior versions.
> - The module name `bigip_iapplx_package` has been deprecated in favor of `bigip_lx_package`.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_lx_package_module.md#id5)

```yaml+jinja
- name: Install AS3
  bigip_lx_package:
    package: f5-appsvcs-3.5.0-3.noarch.rpm
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Add an LX package stored in a role
  bigip_lx_package:
    package: "{{ roles_path }}/files/MyApp-0.1.0-0001.noarch.rpm'"
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove an LX package
  bigip_lx_package:
    package: MyApp-0.1.0-0001.noarch.rpm
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Install AS3 and don't delete package file
  bigip_lx_package:
    package: f5-appsvcs-3.5.0-3.noarch.rpm
    retain_package_file: true
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

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

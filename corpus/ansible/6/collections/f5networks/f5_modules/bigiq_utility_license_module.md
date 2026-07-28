---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigiq_utility_license module – Manage utility licenses on a BIG-IQ"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigiq_utility_license_module.html
fetched_at: 2026-07-27T17:28:12+00:00
---
# f5networks.f5_modules.bigiq_utility_license module – Manage utility licenses on a BIG-IQ

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
> You need further requirements to be able to use this module,
> see [Requirements](bigiq_utility_license_module.md#ansible-collections-f5networks-f5-modules-bigiq-utility-license-module-requirements) for details.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigiq_utility_license`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigiq_utility_license_module.md#synopsis)
- [Requirements](bigiq_utility_license_module.md#requirements)
- [Parameters](bigiq_utility_license_module.md#parameters)
- [Notes](bigiq_utility_license_module.md#notes)
- [Examples](bigiq_utility_license_module.md#examples)

## [Synopsis](bigiq_utility_license_module.md#id1)

- Manages utility licenses on a BIG-IQ. Utility licenses are one form of license that BIG-IQ can distribute. These licenses, unlike regkey licenses, do not require a pool to be created before creation. Additionally, when assigning them, you assign by offering instead of key.

## [Requirements](bigiq_utility_license_module.md#id2)

The below requirements are needed on the host that executes this module.

- BIG-IQ >= 5.3.0

## [Parameters](bigiq_utility_license_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accept_eula**  boolean | A key that signifies you accept the F5 EULA for this license.  A copy of the EULA can be found here <https://askf5.f5.com/csp/article/K12902>  This is required when `state` is `present`.  Choices:   - `false` - `true` |
| **license_key**  string / required | The license key to install and activate. |
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
| **state**  string | The state of the utility license on the system.  When `present`, guarantees the license exists.  When `absent`, removes the license from the system.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](bigiq_utility_license_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigiq_utility_license_module.md#id5)

```yaml+jinja
- name: Add a utility license to the system
  bigiq_utility_license:
    license_key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
    accept_eula: yes
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Remove a utility license from the system
  bigiq_utility_license:
    license_key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
    state: absent
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

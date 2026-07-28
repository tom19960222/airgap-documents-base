---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigiq_regkey_license module – Manages licenses in a BIG-IQ registration key pool"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigiq_regkey_license_module.html
fetched_at: 2026-07-28T02:07:42+00:00
---
# f5networks.f5_modules.bigiq_regkey_license module – Manages licenses in a BIG-IQ registration key pool

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
> see [Requirements](bigiq_regkey_license_module.md#ansible-collections-f5networks-f5-modules-bigiq-regkey-license-module-requirements) for details.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigiq_regkey_license`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigiq_regkey_license_module.md#synopsis)
- [Requirements](bigiq_regkey_license_module.md#requirements)
- [Parameters](bigiq_regkey_license_module.md#parameters)
- [Notes](bigiq_regkey_license_module.md#notes)
- [Examples](bigiq_regkey_license_module.md#examples)
- [Return Values](bigiq_regkey_license_module.md#return-values)

## [Synopsis](bigiq_regkey_license_module.md#id1)

- Manages licenses in a BIG-IQ registration key pool.

## [Requirements](bigiq_regkey_license_module.md#id2)

The below requirements are needed on the host that executes this module.

- BIG-IQ >= 5.3.0

## [Parameters](bigiq_regkey_license_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accept_eula**  boolean | A key that signifies you accept the F5 EULA for this license.  A copy of the EULA can be found here <https://askf5.f5.com/csp/article/K12902>  This is required when `state` is `present`.  **Choices:**   - `false` - `true` |
| **addon_keys**  list / elements=string  *added in f5networks.f5_modules 1.16.0* | The addon keys to put in the pool. |
| **description**  string | Description of the license. |
| **license_key**  string / required | The license key to put in the pool. |
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
| **regkey_pool**  string / required | The registration key pool in which you want to place the license.  You must give your registration pools unique names. While BIG-IQ does not require this, this module does. If you do not, the behavior of the module is undefined and you may end up putting licenses in the wrong registration key pool. |
| **state**  string | The state of the regkey license in the pool on the system.  When `present`, guarantees the license exists in the pool.  When `absent`, removes the license from the pool.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](bigiq_regkey_license_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigiq_regkey_license_module.md#id5)

```yaml+jinja
- name: Add a registration key license to a pool
  bigiq_regkey_license:
    regkey_pool: foo-pool
    license_key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
    accept_eula: true
    provider:
      password: secret
      server: cm.mydomain.com
      user: admin
  delegate_to: localhost

- name: Add a registration key license with addon keys to a pool
  bigiq_regkey_license:
    regkey_pool: foo-pool
    license_key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
    addon_keys:
      - YYYY-YYY-YYY
      - ZZZZ-ZZZ-ZZZ
    accept_eula: true
    provider:
      password: secret
      server: cm.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove a registration key license from a pool
  bigiq_regkey_license:
    regkey_pool: foo-pool
    license_key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
    state: absent
    provider:
      password: secret
      server: cm.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigiq_regkey_license_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The new description of the license key.  **Returned:** changed  **Sample:** `"My license for BIG-IP 1"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior(@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

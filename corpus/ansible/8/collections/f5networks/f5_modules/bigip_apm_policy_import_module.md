---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_apm_policy_import module – Manage BIG-IP APM policy or APM access profile imports"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_apm_policy_import_module.html
fetched_at: 2026-07-28T02:05:36+00:00
---
# f5networks.f5_modules.bigip_apm_policy_import module – Manage BIG-IP APM policy or APM access profile imports

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_apm_policy_import`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_apm_policy_import_module.md#synopsis)
- [Parameters](bigip_apm_policy_import_module.md#parameters)
- [Notes](bigip_apm_policy_import_module.md#notes)
- [Examples](bigip_apm_policy_import_module.md#examples)
- [Return Values](bigip_apm_policy_import_module.md#return-values)

## [Synopsis](bigip_apm_policy_import_module.md#id1)

- Manage BIG-IP APM policy or APM access profile imports.

## [Parameters](bigip_apm_policy_import_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | When set to `true` any existing policy with the same name will be overwritten by the new import.  If a policy does not exist, this setting is ignored.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | The name of the APM policy or APM access profile to create or override. |
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
| **reuse_objects**  boolean | When set to `true` and objects referred within the policy exist on the BIG-IP, those will be used instead of the objects defined in the policy.  Reusing existing objects reduces configuration size.  The configuration of existing objects might differ to the configuration of the objects defined in the policy!  **Choices:**   - `false` - `true` ← (default) |
| **source**  path | Full path to a file to be imported into the BIG-IP APM. |
| **type**  string | Specifies the type of item to export from the device.  **Choices:**   - `"profile_access"` ← (default) - `"access_policy"` - `"profile_api_protection"` |

## [Notes](bigip_apm_policy_import_module.md#id3)

> **Note:**
>
> - Due to ID685681 it is not possible to execute ng_\* tools via REST API on v12.x and 13.x, once this is fixed this restriction will be removed.
> - Requires BIG-IP >= 14.0.0
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_apm_policy_import_module.md#id4)

```yaml+jinja
- name: Import APM profile
  bigip_apm_policy_import:
    name: new_apm_profile
    source: /root/apm_profile.tar.gz
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Import APM policy
  bigip_apm_policy_import:
    name: new_apm_policy
    source: /root/apm_policy.tar.gz
    type: access_policy
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Override existing APM policy
  bigip_asm_policy:
    name: new_apm_policy
    source: /root/apm_policy.tar.gz
    force: true
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Import APM profile without re-using existing configuration objects
  bigip_apm_policy_import:
    name: new_apm_profile
    source: /root/apm_profile.tar.gz
    reuse_objects: false
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_apm_policy_import_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **force**  boolean | Set when overwriting an existing policy or profile.  **Returned:** changed  **Sample:** `true` |
| **name**  string | Name of the APM policy or APM access profile to be created/overwritten.  **Returned:** changed  **Sample:** `"APM_policy_global"` |
| **reuse_objects**  boolean | Set when reusing existing objects on the BIG-IP.  **Returned:** changed  **Sample:** `true` |
| **source**  string | Local path to APM policy file.  **Returned:** changed  **Sample:** `"/root/some_policy.tar.gz"` |
| **type**  string | Set to specify type of item to export.  **Returned:** changed  **Sample:** `"access_policy"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

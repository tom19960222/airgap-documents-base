---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_apm_policy_fetch module – Exports the APM policy or APM access profile from remote nodes."
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_apm_policy_fetch_module.html
fetched_at: 2026-07-27T17:26:11+00:00
---
# f5networks.f5_modules.bigip_apm_policy_fetch module – Exports the APM policy or APM access profile from remote nodes.

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_apm_policy_fetch`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_apm_policy_fetch_module.md#synopsis)
- [Parameters](bigip_apm_policy_fetch_module.md#parameters)
- [Notes](bigip_apm_policy_fetch_module.md#notes)
- [Examples](bigip_apm_policy_fetch_module.md#examples)
- [Return Values](bigip_apm_policy_fetch_module.md#return-values)

## [Synopsis](bigip_apm_policy_fetch_module.md#id1)

- Exports the APM policy or APM access profile from remote nodes.

## [Parameters](bigip_apm_policy_fetch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dest**  path | A directory to save the file into. |
| **file**  string | The name of the file to be created on the remote device for downloading. |
| **force**  boolean | If `no`, the file will only be transferred if it does not exist in the the destination.  Choices:   - `false` - `true` ← (default) |
| **name**  string / required | The name of the APM policy or APM access profile exported to create a file on the remote device for downloading. |
| **partition**  string | Device partition which contains the APM policy or APM access profile to export.  Default: `"Common"` |
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
| **type**  string | Specifies the type of item to export from the device.  Choices:   - `"profile_access"` ← (default) - `"access_policy"` |

## [Notes](bigip_apm_policy_fetch_module.md#id3)

> **Note:**
>
> - Due to ID685681 it is not possible to execute ng_\* tools via REST API on v12.x and 13.x, once this is fixed this restriction will be removed.
> - Requires BIG-IP >= 14.0.0
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_apm_policy_fetch_module.md#id4)

```yaml+jinja
- name: Export APM access profile
  bigip_apm_policy_fetch:
    name: foobar
    file: export_foo
    dest: /root/download
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Export APM access policy
  bigip_apm_policy_fetch:
    name: foobar
    file: export_foo
    dest: /root/download
    type: access_policy
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Export APM access profile, autogenerate name
  bigip_apm_policy_fetch:
    name: foobar
    dest: /root/download
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_apm_policy_fetch_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dest**  string | Local path to download the exported APM policy.  Returned: changed  Sample: `"/root/downloads/profile-foobar_file.conf.tar.gz"` |
| **file**  string | Name of the exported file on the remote BIG-IP to download. If not specified, then this will be a randomly generated filename.  Returned: changed  Sample: `"foobar_file"` |
| **name**  string | Name of the APM policy or APM access profile to be exported.  Returned: changed  Sample: `"APM_policy_global"` |
| **type**  string | Set to specify the type of item to export.  Returned: changed  Sample: `"access_policy"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

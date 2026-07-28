---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_asm_policy_fetch module – Exports the ASM policy from remote nodes."
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_asm_policy_fetch_module.html
fetched_at: 2026-07-27T17:26:13+00:00
---
# f5networks.f5_modules.bigip_asm_policy_fetch module – Exports the ASM policy from remote nodes.

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_asm_policy_fetch`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_asm_policy_fetch_module.md#synopsis)
- [Parameters](bigip_asm_policy_fetch_module.md#parameters)
- [Notes](bigip_asm_policy_fetch_module.md#notes)
- [Examples](bigip_asm_policy_fetch_module.md#examples)
- [Return Values](bigip_asm_policy_fetch_module.md#return-values)

## [Synopsis](bigip_asm_policy_fetch_module.md#id1)

- Exports the ASM policy from remote nodes.

## [Parameters](bigip_asm_policy_fetch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **base64**  boolean | If `yes`, the returned `inline` ASM policy content is Base64 encoded.  Only applies to `inline` ASM policy exports.  Choices:   - `false` - `true` |
| **binary**  boolean | If `yes`, the exported ASM policy is in binary format.  Only applies to `file` ASM policy exports.  Choices:   - `false` - `true` |
| **compact**  boolean | If `yes`, only the ASM policy custom settings is exported.  Only applies to XML type ASM policy exports.  Choices:   - `false` - `true` |
| **dest**  path | A directory to save the policy file into.  This option is ignored when `inline` is set to c(yes). |
| **file**  string | The name of the file to be created on the remote device for downloading.  When `binary` is set to `no` the ASM policy is in XML format. |
| **force**  boolean | If `no`, the file will only be transferred if it does not exist in the the destination.  Choices:   - `false` - `true` ← (default) |
| **inline**  boolean | If `yes`, the ASM policy is exported `inline` as a string instead of a file.  The policy can be be retrieved in the playbook `result` dictionary under the `inline_policy` key.  Choices:   - `false` - `true` |
| **name**  string / required | The name of the policy exported to create a file on the remote device for downloading. |
| **partition**  string | Device partition which contains the ASM policy to export.  Default: `"Common"` |
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

## [Notes](bigip_asm_policy_fetch_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_asm_policy_fetch_module.md#id4)

```yaml+jinja
- name: Export policy in binary format
  bigip_asm_policy_fetch:
    name: foobar
    file: export_foo
    dest: /root/download
    binary: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Export policy inline base64 encoded format
  bigip_asm_policy_fetch:
    name: foobar
    inline: yes
    base64: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Export policy in XML format
  bigip_asm_policy_fetch:
    name: foobar
    file: export_foo
    dest: /root/download
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Export compact policy in XML format
  bigip_asm_policy_fetch:
    name: foobar
    file: export_foo.xml
    dest: /root/download/
    compact: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Export policy in binary format, autogenerate name
  bigip_asm_policy_fetch:
    name: foobar
    dest: /root/download/
    binary: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_asm_policy_fetch_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **base64**  boolean | Set to encode inline export in Base64 format.  Returned: changed  Sample: `false` |
| **binary**  boolean | Set to export the ASM policy in binary format.  Returned: changed  Sample: `true` |
| **compact**  boolean | Set only to export custom ASM policy settings.  Returned: changed  Sample: `false` |
| **dest**  string | Local path to download the exported ASM policy.  Returned: changed  Sample: `"/root/downloads/foobar.xml"` |
| **file**  string | Name of the policy file on the remote BIG-IP to download. If not specified, then this is a randomly generated filename.  Returned: changed  Sample: `"foobar.xml"` |
| **inline**  boolean | Set when the ASM policy to be exported is inline  Returned: changed  Sample: `true` |
| **name**  string | Name of the ASM policy to be exported.  Returned: changed  Sample: `"Asm_APP1_Transparent"` |

### Authors

- Wojciech Wypior (@wojtek0806)
- Nitin Khanna (@nitinthewiz)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

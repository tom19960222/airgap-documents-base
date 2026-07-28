---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_asm_policy_import module – Manage BIG-IP ASM policy imports"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_asm_policy_import_module.html
fetched_at: 2026-07-27T17:26:14+00:00
---
# f5networks.f5_modules.bigip_asm_policy_import module – Manage BIG-IP ASM policy imports

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_asm_policy_import`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_asm_policy_import_module.md#synopsis)
- [Parameters](bigip_asm_policy_import_module.md#parameters)
- [Notes](bigip_asm_policy_import_module.md#notes)
- [Examples](bigip_asm_policy_import_module.md#examples)
- [Return Values](bigip_asm_policy_import_module.md#return-values)

## [Synopsis](bigip_asm_policy_import_module.md#id1)

- Manage the policy imports for BIG-IP ASM policies.

## [Parameters](bigip_asm_policy_import_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **base64**  boolean | Indicates if the imported policy string is encoded in Base64.  This parameter only takes effect when using the `inline` method of import.  Choices:   - `false` - `true` |
| **encoding**  string | Specifies the desired application language of the imported policy.  The imported policy cannot be a `parent` type or attached to a `parent` policy when `auto-detect` encoding is set.  When importing a policy to attach to a `parent` policy, the `encoding` of the imported policy, if different, must be set to be the same value as `parent_policy`, otherwise import will fail.  This parameter is available on TMOS version 13.x and later and only takes effect when the `inline` import method is used.  Choices:   - `"windows-874"` - `"utf-8"` - `"koi8-r"` - `"windows-1253"` - `"iso-8859-10"` - `"gbk"` - `"windows-1256"` - `"windows-1250"` - `"iso-8859-13"` - `"iso-8859-9"` - `"windows-1251"` - `"iso-8859-6"` - `"big5"` - `"gb2312"` - `"iso-8859-1"` - `"windows-1252"` - `"iso-8859-4"` - `"iso-8859-2"` - `"iso-8859-3"` - `"gb18030"` - `"shift_jis"` - `"iso-8859-8"` - `"euc-kr"` - `"iso-8859-5"` - `"iso-8859-7"` - `"windows-1255"` - `"euc-jp"` - `"iso-8859-15"` - `"windows-1257"` - `"iso-8859-16"` - `"auto-detect"` |
| **force**  boolean | When set to `yes`, any existing policy with the same name will be overwritten by the new import.  This works for both inline and file imports, if the policy does not exist this setting is ignored.  Choices:   - `false` ← (default) - `true` |
| **inline**  string | When specified, the ASM policy is created from a provided string.  Content needs to be provided in a valid XML format, otherwise the operation will fail. |
| **name**  string / required | The ASM policy to create or override. |
| **parent_policy**  string | The parent policy to which the newly imported policy should be attached as child.  When `parent_policy` is specified, the imported `policy_type` must not be `parent`.  This parameter is available on TMOS version 13.x and later and only takes effect when `inline` import method is used. |
| **partition**  string | Device partition on which to create the policy.  This parameter is also applied to indicate the partition of the `parent` policy.  Default: `"Common"` |
| **policy_type**  string | The type of the policy to import.  When `policy_type` is `security`, the policy is imported as an application security policy that you can apply to a virtual server.  When `policy_type` is `parent`, the policy becomes a parent to which other Security policies attach, inheriting its attributes. This policy type cannot be applied to Virtual Servers.  This parameter is available on TMOS version 13.x and later and only takes effect when the `inline` import method is used.  Choices:   - `"security"` ← (default) - `"parent"` |
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
| **retain_inheritance_settings**  boolean | Indicates if an imported security type policy should retain settings when attached to parent policy.  This parameter is available on TMOS version 13.x and later and only takes effect when the `inline` import method is used.  Choices:   - `false` - `true` |
| **source**  path | Full path to a policy file to be imported into the BIG-IP ASM.  Policy files exported from newer versions of BIG-IP cannot be imported into older versions of BIG-IP. However, policy files from older versions of BIG-IP can be imported into newer versions of BIG-IP.  The file format can be binary or XML. |

## [Notes](bigip_asm_policy_import_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_asm_policy_import_module.md#id4)

```yaml+jinja
- name: Import ASM policy
  bigip_asm_policy_import:
    name: new_asm_policy
    file: /root/asm_policy.xml
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Import ASM policy inline
  bigip_asm_policy_import:
    name: foo-policy4
    inline: <xml>content</xml>
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Override existing ASM policy
  bigip_asm_policy:
    name: new_asm_policy
    source: /root/asm_policy_new.xml
    force: yes
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_asm_policy_import_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **base64**  boolean | Indicates if the imported policy string is encoded in Base64.  Returned: changed  Sample: `true` |
| **encoding**  string | The desired application language of the imported policy.  Returned: changed  Sample: `"utf-8"` |
| **force**  boolean | Set when overwriting an existing policy.  Returned: changed  Sample: `true` |
| **inline**  string | Contents of a policy as an inline string.  Returned: changed  Sample: `"<xml>foobar contents</xml>"` |
| **name**  string | Name of the ASM policy to be created/overwritten.  Returned: changed  Sample: `"Asm_APP1_Transparent"` |
| **parent_policy**  string | The parent policy to which the newly imported policy should be attached as child.  Returned: changed  Sample: `"/Common/parent"` |
| **policy_type**  string | The type of the policy to import.  Returned: changed  Sample: `"security"` |
| **retain_inheritance_settings**  boolean | Indicate if an imported security type policy should retain settings when attached to the parent policy.  Returned: changed  Sample: `true` |
| **source**  string | Local path to an ASM policy file.  Returned: changed  Sample: `"/root/some_policy.xml"` |

### Authors

- Wojciech Wypior (@wojtek0806)
- Nitin Khanna (@nitinthewiz)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

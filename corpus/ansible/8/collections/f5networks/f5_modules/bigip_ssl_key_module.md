---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_ssl_key module – Import/Delete SSL keys from BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_ssl_key_module.html
fetched_at: 2026-07-28T02:07:22+00:00
---
# f5networks.f5_modules.bigip_ssl_key module – Import/Delete SSL keys from BIG-IP

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
> see [Requirements](bigip_ssl_key_module.md#ansible-collections-f5networks-f5-modules-bigip-ssl-key-module-requirements) for details.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_ssl_key`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_ssl_key_module.md#synopsis)
- [Requirements](bigip_ssl_key_module.md#requirements)
- [Parameters](bigip_ssl_key_module.md#parameters)
- [Notes](bigip_ssl_key_module.md#notes)
- [Examples](bigip_ssl_key_module.md#examples)
- [Return Values](bigip_ssl_key_module.md#return-values)

## [Synopsis](bigip_ssl_key_module.md#id1)

- This module imports/deletes SSL keys on a BIG-IP. Keys can be imported from key files on the local disk, in PEM format.

## [Requirements](bigip_ssl_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- BIG-IP >= v12

## [Parameters](bigip_ssl_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content**  aliases: key_content  string | Sets the contents of a key directly to the specified value. This is used with lookup plugins or for anything with formatting or templating. This must be provided when `state` is `present`. |
| **name**  string / required | The name of the key. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **passphrase**  string | Passphrase on key. |
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
| **state**  string | When `present`, ensures the key is uploaded to the device. When `absent`, ensures the key is removed from the device. If the key is currently in use, the module is not able to remove the key.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **true_names**  boolean  *added in f5networks.f5_modules 1.24.0* | When `true`, the module does not append `.key` extension to the given key name.  When `false`, the module appends `.key` extension to the given key name.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](bigip_ssl_key_module.md#id4)

> **Note:**
>
> - This module does not behave like other modules you might include in roles, where referencing files or templates first looks in the role’s files or templates directory. To have the module behave that way, use the Ansible file or template lookup (see Examples). The lookups behave as expected in a role context.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_ssl_key_module.md#id5)

```yaml+jinja
- name: Use a file lookup to import key
  bigip_ssl_key:
    name: key-name
    state: present
    content: "{{ lookup('file', '/path/to/key.key') }}"
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Delete key
  bigip_ssl_key:
    name: key-name
    state: absent
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_ssl_key_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **key_checksum**  string | SHA1 checksum of the key.  **Returned:** changed and created  **Sample:** `"cf23df2207d99a74fbe169e3eba035e633b65d94"` |
| **key_filename**  string | The name of the SSL certificate key. The `key_filename` and `cert_filename` will be similar to each other, however the `key_filename` will have a `.key` extension.  **Returned:** created  **Sample:** `"cert1.key"` |
| **key_source_path**  string | Path on BIG-IP where the source of the key is stored.  **Returned:** created  **Sample:** `"/var/config/rest/downloads/cert1.key"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

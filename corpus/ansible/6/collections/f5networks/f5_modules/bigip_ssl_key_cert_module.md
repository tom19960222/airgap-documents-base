---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_ssl_key_cert module – Import/Delete SSL keys and certs from BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_ssl_key_cert_module.html
fetched_at: 2026-07-27T17:27:52+00:00
---
# f5networks.f5_modules.bigip_ssl_key_cert module – Import/Delete SSL keys and certs from BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_ssl_key_cert`.

New in f5networks.f5_modules 1.6.0

- [Synopsis](bigip_ssl_key_cert_module.md#synopsis)
- [Parameters](bigip_ssl_key_cert_module.md#parameters)
- [Notes](bigip_ssl_key_cert_module.md#notes)
- [Examples](bigip_ssl_key_cert_module.md#examples)

## [Synopsis](bigip_ssl_key_cert_module.md#id1)

- This module imports/deletes SSL keys and certificates on a BIG-IP. Keys can be imported from key files on the local disk, in PEM format. Certificates can be imported from certificate and key files on the local disk, in PEM format.

## [Parameters](bigip_ssl_key_cert_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cert_content**  string | Sets the contents of a certificate directly to the specified value. This is used with lookup plugins or for anything with formatting or  `content` must be provided when `state` is `present`. |
| **cert_name**  string | SSL certificate name. This is the cert name used when importing a certificate into the BIG-IP. It also determines the filenames of the objects on the LTM. |
| **issuer_cert**  string | Issuer certificate used for OCSP monitoring.  This parameter is only valid on versions of BIG-IP 13.0.0 or above. |
| **key_content**  string | Sets the contents of a key directly to the specified value. This is used with lookup plugins, or for anything with formatting or templating. This must be provided when `state` is `present`. |
| **key_name**  string | The name of the key. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **passphrase**  string | Passphrase on key. |
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
| **state**  string | When `present`, ensures the key and/or cert is uploaded to the device. When `absent`, ensures the key and/or cert is removed from the device. If the key and/or cert is currently in use, the module will not be able to remove the key.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_ssl_key_cert_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_ssl_key_cert_module.md#id4)

```yaml+jinja
- name: Import both key and cert
  bigip_ssl_key_cert:
    key_content: "{{ lookup('file', 'key.pem') }}"
    key_name: cert1
    cert_content: "{{ lookup('file', 'cert.pem') }}"
    cert_name: cert1
    state: present
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

### Authors

- Nitin Khanna (@nitinthewiz)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

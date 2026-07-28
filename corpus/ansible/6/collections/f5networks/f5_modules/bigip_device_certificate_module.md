---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_device_certificate module – Manage self-signed device certificates"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_device_certificate_module.html
fetched_at: 2026-07-27T17:26:25+00:00
---
# f5networks.f5_modules.bigip_device_certificate module – Manage self-signed device certificates

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_certificate`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_certificate_module.md#synopsis)
- [Parameters](bigip_device_certificate_module.md#parameters)
- [Notes](bigip_device_certificate_module.md#notes)
- [Examples](bigip_device_certificate_module.md#examples)
- [Return Values](bigip_device_certificate_module.md#return-values)

## [Synopsis](bigip_device_certificate_module.md#id1)

- Module used to create and/or renew self-signed device certificates for BIG-IP.

## [Parameters](bigip_device_certificate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **add_to_trusted**  boolean | Specified if the certificate should be added to the trusted client and server certificate files.  Choices:   - `false` ← (default) - `true` |
| **cert_name**  string | Specifies the full name of the certificate file.  If the name is not default `server.crt`, the module will configure `httpd` to use them prior to restarting the `httpd` daemon.  Default: `"server.crt"` |
| **days_valid**  integer / required | Specifies the interval for which the self-signed certificate is valid.  The maximum value is 25 years: `9125` days |
| **force**  boolean | When `yes`, will update or overwrite the existing certificate when it is not expired on the device.  When `no`, the certificate will only be updated/overwritten if expired.  Generally should be `yes` only in cases where you need to update certificate that is about to expire.  This option is also needed when generating a new certificate to replace non-expired one.  Choices:   - `false` ← (default) - `true` |
| **issuer**  dictionary | Certificate properties, required when generating new certificates. |
| **common_name**  string | Specifies the Common Name attribute for the certificate. |
| **country**  string | Specifies the Country name attribute for the certificate. |
| **division**  string | Specifies the department name attribute for the certificate. |
| **email**  string | Specifies the email address of the domain administrator. |
| **locality**  string | Specifies the city or town name for the certificate. |
| **organization**  string | Specifies the Organization attribute for the certificate. |
| **state**  string | Specifies the State or Province attribute for the certificate. |
| **key_name**  string | Specifies the full name of the key file.  If the name is not default `server.key`, the module will configure `httpd` to use them prior to restarting the `httpd` daemon.  Default: `"server.key"` |
| **key_size**  integer | Specifies the desired key size in bits.  Mandatory option when generating a new certificate.  Choices:   - `512` - `1024` - `2048` ← (default) - `4096` |
| **new_cert**  boolean | Specified if the module should generate a new certificate.  When `yes`, the device certificate and key will be replaced.  Choices:   - `false` ← (default) - `true` |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `22` |
| **ssh_keyfile**  path | Specifies the SSH keyfile to use to authenticate the connection to the remote device. This argument is only used for *cli* transports.  You may omit this option by setting the environment variable `ANSIBLE_NET_SSH_KEYFILE`. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |

## [Notes](bigip_device_certificate_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_certificate_module.md#id4)

```yaml+jinja
- name: Update expired certificate
  bigip_device_certificate:
    days_valid: 365
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
      transport: cli
      server_port: 22
  delegate_to: localhost

- name: Update expired certificate non-default names
  bigip_device_certificate:
    days_valid: 60
    cert_name: custom.crt
    key_name: custom.key
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
      transport: cli
      server_port: 22
  delegate_to: localhost

- name: Force update not expired certificate
  bigip_device_certificate:
    days_valid: 365
    force: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
      transport: cli
      server_port: 22
  delegate_to: localhost

- name: Create a new certificate to replace expired certificate
  bigip_device_certificate:
    days_valid: 365
    new_cert: yes
    issuer:
      country: US
      state: WA
      common_name: foobar.foo.local
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
      transport: cli
      server_port: 22
  delegate_to: localhost

- name: Force create a new custom named certificate to replace not expired certificate
  bigip_device_certificate:
    days_valid: 365
    cert_name: custom.crt
    key_name: custom.key
    new_cert: yes
    force: yes
    issuer:
      country: US
      state: WA
      common_name: foobar.foo.local
    key_size: 2048
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
      transport: cli
      server_port: 22
  delegate_to: localhost
```

## [Return Values](bigip_device_certificate_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cert_name**  string | The full name of the certificate file.  Returned: changed  Sample: `"common.crt"` |
| **days_valid**  integer | The interval for which the self-signed certificate is valid.  Returned: changed  Sample: `365` |
| **issuer**  complex | Specifies certificate properties.  Returned: changed |
| **common_name**  string | The Common Name attribute of the certificate.  Returned: changed  Sample: `"foo.bar.local"` |
| **country**  string | The Country name attribute of the certificate.  Returned: changed  Sample: `"US"` |
| **division**  string | The department name attribute of the certificate.  Returned: changed  Sample: `"IT"` |
| **email**  string | The domain administrator’s email address.  Returned: changed  Sample: `"admin@foo.bar.local"` |
| **locality**  string | The city or town name attribute of the certificate.  Returned: changed  Sample: `"Seattle"` |
| **organization**  string | The Organization attribute of the certificate.  Returned: changed  Sample: `"F5"` |
| **state**  string | The State or Province attribute of the certificate.  Returned: changed  Sample: `"WA"` |
| **key_name**  string | The full name of the key file.  Returned: changed  Sample: `"common.key"` |
| **key_size**  integer | The desired key size in bits.  Returned: changed  Sample: `2048` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

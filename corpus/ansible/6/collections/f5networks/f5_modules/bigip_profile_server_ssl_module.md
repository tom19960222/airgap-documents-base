---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_profile_server_ssl module – Manages server SSL profiles on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_profile_server_ssl_module.html
fetched_at: 2026-07-27T17:27:35+00:00
---
# f5networks.f5_modules.bigip_profile_server_ssl module – Manages server SSL profiles on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_server_ssl`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_server_ssl_module.md#synopsis)
- [Parameters](bigip_profile_server_ssl_module.md#parameters)
- [Notes](bigip_profile_server_ssl_module.md#notes)
- [Examples](bigip_profile_server_ssl_module.md#examples)
- [Return Values](bigip_profile_server_ssl_module.md#return-values)

## [Synopsis](bigip_profile_server_ssl_module.md#id1)

- Manages server SSL profiles on a BIG-IP system.

## [Parameters](bigip_profile_server_ssl_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **certificate**  string | Specifies the name of the certificate the system uses for server-side SSL processing. |
| **chain**  string | Specifies the certificates-key chain to associate with the SSL profile. |
| **cipher_group**  string  added in f5networks.f5_modules 1.12.0 | Specifies the cipher group to assign to this profile.  When the `ciphers` parameter is in use, the `cipher_group` must be set to either `none` or `''`.  When creating a new profile with `cipher_group`, if the parent profile has `ciphers` set by default, the `cipher` parameter must be set to `none` or `''` during creation.  The parameter only works on TMOS version 13.x and later. |
| **ciphers**  string | Specifies the list of ciphers the system supports. When creating a new profile, the default cipher list is provided by the parent profile.  When the `cipher_group` parameter is in use, the `ciphers` parameter needs to be set to either `none` or `''`. |
| **key**  string | Specifies the file name of the SSL key. |
| **name**  string / required | Specifies the name of the profile. |
| **ocsp_profile**  string | Specifies the name of the OCSP profile for purpose of validating the status of server certificate. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed.  Default: `"/Common/serverssl"` |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **passphrase**  string | Specifies a passphrase used to encrypt the key. |
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
| **renegotiation**  boolean | Enables or disables SSL renegotiation.  When creating a new profile, the setting is provided by the parent profile.  Choices:   - `false` - `true` |
| **secure_renegotiation**  string | Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.  When `request` is set, the system requests secure renegotiation of SSL connections.  `require` is a default setting and when set, the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.  With the `require-strict` setting, the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers.  Choices:   - `"require"` - `"require-strict"` - `"request"` |
| **server_certificate**  string | Specifies the way the system handles server certificates.  When `ignore`, specifies the system ignores certificates from server systems.  When `require`, specifies the system requires a server to present a valid certificate.  Choices:   - `"ignore"` - `"require"` |
| **server_name**  string | Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile. |
| **sni_default**  boolean | Indicates the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.  When creating a new profile, the setting is provided by the parent profile.  There can be only one SSL profile with this setting enabled.  Choices:   - `false` - `true` |
| **sni_require**  boolean | Requires the network peers also provide SNI support. This setting only takes effect when `sni_default` is `yes`.  When creating a new profile, the setting is provided by the parent profile.  Choices:   - `false` - `true` |
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | `always` allows users to update passwords if they choose to do so. `on_create` only sets the password for newly created profiles.  Choices:   - `"always"` ← (default) - `"on_create"` |

## [Notes](bigip_profile_server_ssl_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_server_ssl_module.md#id4)

```yaml+jinja
- name: Create a new server SSL profile
  bigip_profile_server_ssl:
    name: foo
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create server SSL profile with specific cipher group
  bigip_profile_server_ssl:
    state: present
    name: foo_group
    ciphers: "none"
    cipher_group: "/Common/f5-secure"
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_profile_server_ssl_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cipher_group**  string | The cipher group applied to the profile.  Returned: changed  Sample: `"/Common/f5-secure"` |
| **ciphers**  string | The ciphers applied to the profile.  Returned: changed  Sample: `"!SSLv3:!SSLv2:ECDHE+AES-GCM+SHA256:ECDHE-RSA-AES128-CBC-SHA"` |
| **renegotiation**  boolean | Renegotiation of SSL sessions.  Returned: changed  Sample: `true` |
| **secure_renegotiation**  string | The method of secure SSL renegotiation.  Returned: changed  Sample: `"request"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

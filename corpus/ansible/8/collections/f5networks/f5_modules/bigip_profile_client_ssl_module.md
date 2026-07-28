---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_profile_client_ssl module – Manages client SSL profiles on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_profile_client_ssl_module.html
fetched_at: 2026-07-28T02:06:57+00:00
---
# f5networks.f5_modules.bigip_profile_client_ssl module – Manages client SSL profiles on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_client_ssl`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_client_ssl_module.md#synopsis)
- [Parameters](bigip_profile_client_ssl_module.md#parameters)
- [Notes](bigip_profile_client_ssl_module.md#notes)
- [Examples](bigip_profile_client_ssl_module.md#examples)
- [Return Values](bigip_profile_client_ssl_module.md#return-values)

## [Synopsis](bigip_profile_client_ssl_module.md#id1)

- Manages client SSL profiles on a BIG-IP device.

## [Parameters](bigip_profile_client_ssl_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **advertised_cert_authority**  string | Specifies the CAs the system advertises to clients is being trusted by the profile. |
| **allow_expired_crl**  boolean | Instructs the system to use the specified CRL file even if it has expired.  **Choices:**   - `false` - `true` |
| **allow_non_ssl**  boolean | Enables or disables acceptance of non-SSL connections.  When creating a new profile, the setting is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **cache_size**  integer  *added in f5networks.f5_modules 1.0.0* | Specifies the number of sessions in the SSL session cache.  The valid value range is between 0 and 4194304 inclusive.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **cache_timeout**  integer  *added in f5networks.f5_modules 1.0.0* | Specifies the timeout value in seconds of the SSL session cache entries.  Acceptable values are between 0 and 86400 inclusive.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **cert_auth_depth**  integer | Specifies the maximum number of certificates to be traversed in a client certificate chain. |
| **cert_key_chain**  list / elements=dictionary | One or more certificates and keys to associate with the SSL profile. This option is always a list. The keys in the list dictate the details of the client/key/chain combination. Note that BIG-IPs can only have one of each type of each certificate/key type. This means you can only have one RSA, one DSA, and one ECDSA per profile. If you attempt to assign two RSA, DSA, or ECDSA certificate/key combo, the device rejects it.  This list is a complex list that specifies a number of keys. |
| **cert**  string / required | Specifies a certificate name for use. |
| **chain**  string | Contains a certificate chain relevant to the certificate and key mentioned previously.  This key is optional. |
| **key**  string / required | Contains a key name. |
| **passphrase**  string | Contains the passphrase of the key file, if required.  Passphrases are encrypted on the remote BIG-IP device. Therefore, there is no way to compare them when updating a client SSL profile. Due to this, if you specify a passphrase, this module will always register a `changed` event. |
| **true_names**  boolean  *added in f5networks.f5_modules 1.1.0* | When `true`, the module does not append `.crt` and `.key` extensions to the given certificate and key names.  When `false`, the module appends `.crt` and `.key` extensions to the given certificate and key names.  **Choices:**   - `false` ← (default) - `true` |
| **cipher_group**  string  *added in f5networks.f5_modules 1.2.0* | Specifies the cipher group to assign to this profile.  When the `ciphers` parameter is in use, the `cipher_group` must be set to either `none` or `''`.  When creating a new profile with `cipher_group`, if the parent profile has `ciphers` set by default, the `cipher` parameter must be set to `none` or `''` during creation.  The parameter only works on TMOS version 13.x and later. |
| **ciphers**  string | Specifies the list of ciphers the system supports.  When the `cipher_group` parameter is in use, the `ciphers` parameter needs to be set to either `none` or `''`. |
| **client_auth_crl**  string | Specifies the name of a file containing a list of revoked client certificates. |
| **client_auth_frequency**  string | Specifies the frequency of client authentication for an SSL session.  When `once`, specifies the system authenticates the client once for an SSL session.  When `always`, specifies the system authenticates the client once for an SSL session and also upon reuse of that session.  **Choices:**   - `"once"` - `"always"` |
| **client_certificate**  string | Specifies the way the system handles client certificates.  When `ignore`, specifies the system ignores certificates from client systems.  When `require`, specifies the system requires a client to present a valid certificate.  When `request`, specifies the system requests a valid certificate from a client but always authenticate the client.  **Choices:**   - `"ignore"` - `"require"` - `"request"` |
| **name**  string / required | Specifies the name of the profile. |
| **options**  list / elements=string | Options the system uses for SSL processing in the form of a list. When creating a new profile, the list is provided by the parent profile.  When `''` or `none`, all options for SSL processing are disabled.  **Choices:**   - `"netscape-reuse-cipher-change-bug"` - `"microsoft-big-sslv3-buffer"` - `"msie-sslv2-rsa-padding"` - `"ssleay-080-client-dh-bug"` - `"tls-d5-bug"` - `"tls-block-padding-bug"` - `"dont-insert-empty-fragments"` - `"no-ssl"` - `"no-dtls"` - `"no-session-resumption-on-renegotiation"` - `"no-tlsv1.1"` - `"no-tlsv1.2"` - `"no-tlsv1.3"` - `"single-dh-use"` - `"ephemeral-rsa"` - `"cipher-server-preference"` - `"tls-rollback-bug"` - `"no-sslv2"` - `"no-sslv3"` - `"no-tls"` - `"no-tlsv1"` - `"pkcs1-check-1"` - `"pkcs1-check-2"` - `"netscape-ca-dn-bug"` - `"netscape-demo-cipher-change-bug"` - `"none"` |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `clientssl` parent on the `Common` partition. |
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
| **renegotiation**  boolean | Enables or disables SSL renegotiation.  When creating a new profile, the setting is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **retain_certificate**  boolean | When `true`, the client certificate is retained in SSL session.  **Choices:**   - `false` - `true` |
| **secure_renegotiation**  string | Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.  When `request`, the system requests secure renegotiation of SSL connections.  `require` is a default setting and when set, the system permits initial SSL handshakes from clients, but terminates renegotiations from unpatched clients.  With the `require-strict` setting, the system requires strict renegotiation of SSL connections. In this mode, the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers.  **Choices:**   - `"require"` - `"require-strict"` - `"request"` |
| **server_name**  string | Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.  The server name can also be a wildcard string containing the asterisk `*` character. |
| **sni_default**  boolean | Indicates the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.  When creating a new profile, the setting is provided by the parent profile.  There can be only one SSL profile with this setting enabled.  **Choices:**   - `false` - `true` |
| **sni_require**  boolean | Requires the network peers also provide SNI support. This setting only takes effect when `sni_default` is set to `true`.  When creating a new profile, the setting is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **strict_resume**  boolean | Enables or disables the resumption of SSL sessions after an unclean shutdown.  When creating a new profile, the setting is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **trusted_cert_authority**  string | Specifies a client CA the system trusts. |

## [Notes](bigip_profile_client_ssl_module.md#id3)

> **Note:**
>
> - Requires BIG-IP software version >= 12
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_client_ssl_module.md#id4)

```yaml+jinja
- name: Create client SSL profile
  bigip_profile_client_ssl:
    state: present
    name: my_profile
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Create client SSL profile with specific ciphers
  bigip_profile_client_ssl:
    state: present
    name: my_profile
    ciphers: "!SSLv3:!SSLv2:ECDHE+AES-GCM+SHA256:ECDHE-RSA-AES128-CBC-SHA"
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Create client SSL profile with specific cipher group
  bigip_profile_client_ssl:
    state: present
    name: my_profile
    ciphers: "none"
    cipher_group: "/Common/f5-secure"
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Create client SSL profile with specific SSL options
  bigip_profile_client_ssl:
    state: present
    name: my_profile
    options:
      - no-sslv2
      - no-sslv3
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Create client SSL profile require secure renegotiation
  bigip_profile_client_ssl:
    state: present
    name: my_profile
    secure_renegotiation: request
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Create a client SSL profile with a cert/key/chain setting
  bigip_profile_client_ssl:
    state: present
    name: my_profile
    cert_key_chain:
      - cert: bigip_ssl_cert1
        key: bigip_ssl_key1
        chain: bigip_ssl_cert1
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_profile_client_ssl_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allow_non_ssl**  boolean | Acceptance of non-SSL connections.  **Returned:** changed  **Sample:** `true` |
| **cache_size**  integer | Specifies the number of sessions in the SSL session cache.  **Returned:** changed  **Sample:** `2000` |
| **cache_timeout**  integer | Specifies the timeout value in seconds of the SSL session cache entries.  **Returned:** changed  **Sample:** `1800` |
| **cipher_group**  string | The cipher group applied to the profile.  **Returned:** changed  **Sample:** `"/Common/f5-secure"` |
| **ciphers**  string | The ciphers applied to the profile.  **Returned:** changed  **Sample:** `"!SSLv3:!SSLv2:ECDHE+AES-GCM+SHA256:ECDHE-RSA-AES128-CBC-SHA"` |
| **options**  list / elements=string | The list of options for SSL processing.  **Returned:** changed  **Sample:** `["no-sslv2", "no-sslv3"]` |
| **renegotiation**  boolean | Renegotiation of SSL sessions.  **Returned:** changed  **Sample:** `true` |
| **secure_renegotiation**  string | The method of secure SSL renegotiation.  **Returned:** changed  **Sample:** `"request"` |
| **strict_resume**  boolean | Resumption of SSL sessions after an unclean shutdown.  **Returned:** changed  **Sample:** `true` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

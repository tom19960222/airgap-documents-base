---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_device_auth_ldap module – Manage LDAP device authentication settings on BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_device_auth_ldap_module.html
fetched_at: 2026-07-27T17:26:23+00:00
---
# f5networks.f5_modules.bigip_device_auth_ldap module – Manage LDAP device authentication settings on BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_auth_ldap`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_auth_ldap_module.md#synopsis)
- [Parameters](bigip_device_auth_ldap_module.md#parameters)
- [Notes](bigip_device_auth_ldap_module.md#notes)
- [Examples](bigip_device_auth_ldap_module.md#examples)
- [Return Values](bigip_device_auth_ldap_module.md#return-values)

## [Synopsis](bigip_device_auth_ldap_module.md#id1)

- Manage LDAP device authentication settings on BIG-IP.

## [Parameters](bigip_device_auth_ldap_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bind_dn**  string | Specifies the distinguished name for the Active Directory or LDAP server user ID.  The BIG-IP client authentication module does not support Active Directory or LDAP servers that do not perform bind referral when authenticating referred accounts.  Therefore, if you plan to use Active Directory or LDAP as your authentication source and want to use referred accounts, make sure your servers perform bind referral. |
| **bind_password**  string | Specifies a password for the Active Directory or LDAP server user ID. |
| **ca_cert**  aliases: ssl_ca_cert  string | Specifies the name of an SSL certificate from a certificate authority (CA).  To remove this value, use the reserved value `none`. |
| **check_member_attr**  boolean | Checks the member attribute of the user in the remote LDAP or AD group.  Choices:   - `false` - `true` |
| **client_cert**  aliases: ssl_client_cert  string | Specifies the name of an SSL client certificate.  To remove this value, use the reserved value `none`. |
| **client_key**  aliases: ssl_client_key  string | Specifies the name of an SSL client key.  To remove this value, use the reserved value `none`. |
| **fallback_to_local**  boolean | Specifies the system uses the Local authentication method if the remote authentication method is not available.  Option only available on `TMOS 13.0.0` and above.  Choices:   - `false` - `true` |
| **login_ldap_attr**  string | Specifies the LDAP directory attribute containing the local user name that is associated with the selected directory entry.  If this parameter is not specified, when configuring LDAP device authentication for the first time, the default port is `samaccountname`. |
| **port**  integer | Specifies the port the system uses for access to the remote host server.  When configuring LDAP device authentication for the first time, the default port is `389` if this parameter is not specified. |
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
| **remote_directory_tree**  string | Specifies the file location (tree) of the user authentication database on the server. |
| **scope**  string | Specifies the level of the remote Active Directory or LDAP directory the system should search for the user authentication.  Choices:   - `"sub"` - `"one"` - `"base"` |
| **servers**  list / elements=string | Specifies the LDAP servers the system must use to obtain authentication information. You must specify a server when you create an LDAP configuration object. |
| **source_type**  string  added in f5networks.f5_modules 1.13.0 | Specifies the auth source for user authentication, should be used with `use_for_auth`.  Choices:   - `"ldap"` ← (default) - `"active-directory"` |
| **ssl**  string | Specifies whether the system uses an SSL port to communicate with the LDAP server.  Choices:   - `"yes"` - `"no"` - `"start-tls"` |
| **state**  string | When `present`, ensures the device authentication method exists.  When `absent`, ensures the device authentication method does not exist.  When `state` equal to (absent), before you can delete the LDAP configuration, the system must set auth to some alternative. The system ships with a system auth called `local`, therefore the system authentication type is set to that value on the device upon removal of LDAP configuration.  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | `always` always updates the `bind_password`.  `on_create` only sets the `bind_password` for newly created authentication mechanisms.  Choices:   - `"always"` ← (default) - `"on_create"` |
| **use_for_auth**  boolean | Specifies whether or not this auth source is put in use on the system.  If `yes`, the module sets the current system auth type to the value of `ldap`.  If `no`, the module sets the authentication type to `local`, similar behavior to when `state` is `absent`, without removing the configured LDAP resource.  Choices:   - `false` - `true` |
| **user_template**  string | Specifies the distinguished name of the user who is logging on.  You specify the template as a variable that the system replaces with user-specific information during the logon attempt.  For example, you could specify a user template such as `%s@siterequest.com` or `uxml:id=%s,ou=people,dc=siterequest,dc=com`.  When a user attempts to log on, the system replaces `%s` with the name the user specified in the Basic Authentication dialog box, and passes that as the distinguished name for the bind operation.  The system passes the associated password as the password for the bind operation.  This field can contain only one `%s` and cannot contain any other format specifiers. |
| **validate_certs**  aliases: ssl_check_peer  boolean | Specifies whether the system checks an SSL peer, as a result of which the system requires and verifies the server certificate.  Choices:   - `false` - `true` |

## [Notes](bigip_device_auth_ldap_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_auth_ldap_module.md#id4)

```yaml+jinja
- name: Create an LDAP authentication object
  bigip_device_auth_ldap:
    name: foo
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_device_auth_ldap_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bind_dn**  string | The distinguished name for the Active Directory or LDAP server user ID.  Returned: changed  Sample: `"user@foobar.local"` |
| **ca_cert**  string | The name of an SSL certificate from a certificate authority.  Returned: changed  Sample: `"My-Trusted-CA-Bundle.crt"` |
| **check_member_attr**  boolean | The user’s member attribute in the remote LDAP or AD group.  Returned: changed  Sample: `true` |
| **client_cert**  string | The name of an SSL client certificate.  Returned: changed  Sample: `"MyCert.crt"` |
| **client_key**  string | The name of an SSL client key.  Returned: changed  Sample: `"MyKey.key"` |
| **fallback_to_local**  boolean | Specifies the system uses the Local authentication method as fallback  Returned: changed  Sample: `true` |
| **login_ldap_attr**  string | The LDAP directory attribute containing the local user name associated with the selected directory entry.  Returned: changed  Sample: `"samaccountname"` |
| **port**  integer | The port the system uses for access to the remote LDAP server.  Returned: changed  Sample: `389` |
| **remote_directory_tree**  string | File location (tree) of the user authentication database on the server.  Returned: changed  Sample: `"CN=Users,DC=FOOBAR,DC=LOCAL"` |
| **scope**  string | The level of the remote Active Directory or LDAP directory searched for user authentication.  Returned: changed  Sample: `"base"` |
| **servers**  list / elements=string | LDAP servers used by the system to obtain authentication information.  Returned: changed  Sample: `["192.168.1.1", "192.168.1.2"]` |
| **ssl**  string | Specifies whether the system uses an SSL port to communicate with the LDAP server.  Returned: changed  Sample: `"start-tls"` |
| **user_template**  string | The distinguished name of the user who is logging on.  Returned: changed  Sample: `"uid=%s,ou=people,dc=foobar,dc=local"` |
| **validate_certs**  boolean | Indicates if the system checks an SSL peer.  Returned: changed  Sample: `true` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

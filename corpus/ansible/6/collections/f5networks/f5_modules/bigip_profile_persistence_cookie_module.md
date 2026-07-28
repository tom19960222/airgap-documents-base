---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_profile_persistence_cookie module – Manage cookie persistence profiles on BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_profile_persistence_cookie_module.html
fetched_at: 2026-07-27T17:27:33+00:00
---
# f5networks.f5_modules.bigip_profile_persistence_cookie module – Manage cookie persistence profiles on BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_persistence_cookie`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_persistence_cookie_module.md#synopsis)
- [Parameters](bigip_profile_persistence_cookie_module.md#parameters)
- [Notes](bigip_profile_persistence_cookie_module.md#notes)
- [Examples](bigip_profile_persistence_cookie_module.md#examples)
- [Return Values](bigip_profile_persistence_cookie_module.md#return-values)

## [Synopsis](bigip_profile_persistence_cookie_module.md#id1)

- Manage cookie persistence profiles on BIG-IP system.

## [Parameters](bigip_profile_persistence_cookie_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **always_send**  boolean | Sends the cookie persistence entry on every reply, even if the entry has previously been supplied to the client.  Choices:   - `false` - `true` |
| **cookie_encryption**  string | Specifies the way in which the cookie encryption format is used.  When `disabled`, generates the cookie format unencrypted.  When `preferred`, generates an encrypted cookie, but accepts both encrypted and unencrypted formats.  When `required`, cookie format must be encrypted.  Choices:   - `"disabled"` - `"preferred"` - `"required"` |
| **cookie_method**  string | Specifies the type of cookie processing the system uses.  When `hash`, specifies the server provides the cookie, which the system then maps consistently to a specific node. This persistence type requires a `cookie_name` value.  When `insert`, specifies the system inserts server information, in the form of a cookie, into the header of the server response.  When `passive`, specifies the server provides the cookie, formatted with the correct server information and timeout. This persistence type requires a `cookie_name` value.  When `rewrite`, specifies the system intercepts the BIGipCookie header, sent from the server, and overwrites the name and value of that cookie.  Choices:   - `"hash"` - `"insert"` - `"passive"` - `"rewrite"` |
| **cookie_name**  string | Specifies a unique name for the cookie. |
| **description**  string | Description of the profile. |
| **encrypt_cookie_pool_name**  boolean | Specifies whether the pool-name in the inserted BIG-IP default cookie should be encrypted.  Choices:   - `false` - `true` |
| **encryption_passphrase**  string | Specifies a passphrase to be used for cookie encryption. |
| **expiration**  dictionary | Specifies the expiration time of the cookie. By default the system generates and uses a session cookie. This cookie expires when the user session expires (when the browser is closed). |
| **days**  integer | Cookie expiration time in days. The value must be in range from `0` to `24855` days. |
| **hours**  integer | Cookie expiration time in hours. The value must be in the range from `0` to `23` hours. |
| **minutes**  integer | Cookie expiration time in minutes. The value must be in the range from `0` to `59` minutes. |
| **seconds**  integer | Cookie expiration time in seconds. The value must be in the range from `0` to `59` seconds.  Default: `0` |
| **http_only**  boolean | Specifies whether the httponly attribute should be enabled or disabled for the inserted cookies.  Choices:   - `false` - `true` |
| **match_across_pools**  boolean | When `yes`, specifies the system can use any pool that contains this persistence record.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **match_across_services**  boolean | When `yes`, specifies all persistent connections from a client IP address that go to the same virtual IP address also go to the same node.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **match_across_virtuals**  boolean | When `yes`, specifies all persistent connections from the same client IP address go to the same node.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **name**  string / required | Specifies the name of the profile. |
| **override_connection_limit**  boolean | When `yes`, specifies the system allows you to specify that pool member connection limits will be overridden for persisted clients.  Per-virtual connection limits remain hard limits and are not overridden.  Choices:   - `false` - `true` |
| **parent**  string | Specifies the profile from which this profile inherits settings.  When creating a new profile, if this parameter is not specified, the default is the system-supplied `cookie` profile.  Default: `"cookie"` |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
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
| **secure**  boolean | Specifies whether the secure attribute should be enabled or disabled for the inserted cookies.  Choices:   - `false` - `true` |
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | `always` will allow updating passphrases if the user chooses to do so. `on_create` will only set the passphrase for newly created profiles.  Choices:   - `"always"` ← (default) - `"on_create"` |

## [Notes](bigip_profile_persistence_cookie_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_persistence_cookie_module.md#id4)

```yaml+jinja
- name: Create a persistence cookie profile
  bigip_profile_persistence_cookie:
    name: foo
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
- name: Create a persistence cookie profile with expiration time
  bigip_profile_persistence_cookie:
    name: foo
    expiration:
      days: 7
      hours: 12
      minutes: 30
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_profile_persistence_cookie_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **always_send**  boolean | The new Always Send value.  Returned: changed  Sample: `false` |
| **cookie_encryption**  string | The new Cookie Encryption type.  Returned: changed  Sample: `"preferred"` |
| **cookie_method**  string | The new Cookie Method.  Returned: changed  Sample: `"insert"` |
| **cookie_name**  string | The new Cookie Name value.  Returned: changed  Sample: `"cookie1"` |
| **description**  string | The new description.  Returned: changed  Sample: `"My description"` |
| **encrypt_cookie_pool_name**  boolean | The new Encrypt Cookie Pool Name value.  Returned: changed  Sample: `true` |
| **expiration**  complex | The expiration time of the cookie.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **days**  integer | Cookie expiration time in days.  Returned: changed  Sample: `125` |
| **hours**  integer | Cookie expiration time in hours.  Returned: changed  Sample: `22` |
| **minutes**  integer | Cookie expiration time in minutes.  Returned: changed  Sample: `58` |
| **seconds**  integer | Cookie expiration time in seconds.  Returned: changed  Sample: `20` |
| **http_only**  boolean | The new HTTP Only value.  Returned: changed  Sample: `true` |
| **match_across_pools**  boolean | The new Match Across Pools value.  Returned: changed  Sample: `true` |
| **match_across_services**  boolean | The new Match Across Services value.  Returned: changed  Sample: `false` |
| **match_across_virtuals**  boolean | The new Match Across Virtuals value.  Returned: changed  Sample: `true` |
| **override_connection_limit**  boolean | The new Override Connection Limit value.  Returned: changed  Sample: `false` |
| **parent**  string | The parent profile.  Returned: changed  Sample: `"/Common/cookie"` |
| **secure**  boolean | The new Secure Cookie value.  Returned: changed  Sample: `false` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

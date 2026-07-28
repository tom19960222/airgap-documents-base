---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_profile_http2 module – Manage HTTP2 profiles on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_profile_http2_module.html
fetched_at: 2026-07-27T17:27:31+00:00
---
# f5networks.f5_modules.bigip_profile_http2 module – Manage HTTP2 profiles on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_http2`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_http2_module.md#synopsis)
- [Parameters](bigip_profile_http2_module.md#parameters)
- [Notes](bigip_profile_http2_module.md#notes)
- [Examples](bigip_profile_http2_module.md#examples)
- [Return Values](bigip_profile_http2_module.md#return-values)

## [Synopsis](bigip_profile_http2_module.md#id1)

- Manage HTTP2 profiles on a BIG-IP system.

## [Parameters](bigip_profile_http2_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **activation_modes**  list / elements=string | Specifies what will cause an incoming connection to be handled as a HTTP/2 connection.  The `alpn` and `always` are mutually exclusive.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `"alpn"` - `"always"` |
| **description**  string | Description of the profile. |
| **enforce_tls_requirements**  boolean | Specifies whether the system requires TLS for communications between specified senders and recipients.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **frame_size**  integer | Specifies the size of data frames, in bytes, that HTTP/2 sends to the client.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  The valid value range in bytes is `1024 - 16384`. |
| **header_table_size**  integer | Specifies the size of the header table, in bytes.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  The valid value range in bytes is `0 - 65535`. |
| **idle_timeout**  integer | Specifies the number of seconds an HTTP/2 connection is idly left open before being shut down.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **insert_header**  boolean | Specifies whether an HTTP header indicating the use of HTTP/2 should be inserted into the request that goes to the server.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **insert_header_name**  string | Specifies the name of the HTTP header controlled by `insert_header` parameter.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **name**  string / required | Specifies the name of the profile. |
| **parent**  string | Specifies the profile from which this profile inherits settings.  When creating a new profile, if this parameter is not specified, the default is the system-supplied `http2` profile. |
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
| **receive_window**  integer | Specifies the way the HTTP/2 profile performs flow control.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  The valid value range in kilobytes is `16 - 128`. |
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **streams**  integer | Specifies the number of outstanding concurrent requests allowed on a single HTTP/2 connection.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  The valid value range is `1 - 256`. |
| **write_size**  integer | Specifies the total size of combined data frames, in bytes, that HTTP/2 sends in a single write.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  The valid value range in bytes is `2048 - 32768`. |

## [Notes](bigip_profile_http2_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_http2_module.md#id4)

```yaml+jinja
- name: Create HTTP2 profile
  bigip_profile_http2:
    name: my_profile
    insert_header: yes
    insert_header_name: FOO
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Remove HTTP profile
  bigip_profile_http2:
    name: my_profile
    state: absent
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add HTTP profile set activation modes
  bigip_profile_http:
    name: my_profile
    activation_modes:
      - always
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_profile_http2_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **activation_modes**  list / elements=string | Specifies HTTP/2 connection handling modes.  Returned: changed  Sample: `["always"]` |
| **description**  string | Description of the profile.  Returned: changed  Sample: `"My profile"` |
| **enforce_tls_requirements**  boolean | Specifies whether the system requires TLS for communications.  Returned: changed  Sample: `true` |
| **frame_size**  integer | The size of the data frames.  Returned: changed  Sample: `30` |
| **insert_header_name**  string | Specifies the name of the HTTP2 header.  Returned: changed  Sample: `"X-HTTP2"` |
| **streams**  integer | The number of outstanding concurrent requests allowed on a single HTTP/2 connection.  Returned: changed  Sample: `30` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

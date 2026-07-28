---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_profile_sip module – Manage SIP profiles on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_profile_sip_module.html
fetched_at: 2026-07-27T17:27:36+00:00
---
# f5networks.f5_modules.bigip_profile_sip module – Manage SIP profiles on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_sip`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_sip_module.md#synopsis)
- [Parameters](bigip_profile_sip_module.md#parameters)
- [Notes](bigip_profile_sip_module.md#notes)
- [Examples](bigip_profile_sip_module.md#examples)
- [Return Values](bigip_profile_sip_module.md#return-values)

## [Synopsis](bigip_profile_sip_module.md#id1)

- Manage SIP profiles on a BIG-IP system.

## [Parameters](bigip_profile_sip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **community**  string | When the `dialog_aware` is `yes` and the configuration requires multiple SIP virtual server-profile pairings, this string value indicates whether the pair belongs to the same SIP proxy functional group. |
| **description**  string | Description of the profile.  To remove the entry completely, set a value of `''`. |
| **dialog_aware**  boolean | When `yes`, the system gathers SIP dialog information and automatically forwards SIP messages belonging to the known SIP dialog.  Choices:   - `false` - `true` |
| **enable_sip_firewall**  boolean | Specifies whether the Advanced Firewall Manager (AFM) policy is enabled.  When `yes`, the SIP Security settings configured in the DoS Profile in AFM apply to the virtual servers that use this profile.  Choices:   - `false` - `true` |
| **insert_record_route_header**  boolean | When `yes`, inserts a Record-Route SIP header, which indicates the next hop for the following SIP request messages.  Choices:   - `false` - `true` |
| **insert_via_header**  boolean | When `yes`, inserts a Via header in the forwarded SIP request.  Via headers indicate the path taken through proxy devices and transports used. The response message uses this routing information.  Choices:   - `false` - `true` |
| **log_profile**  string | Specifies the logging settings the publisher uses to send log messages.  The format of the name can be either be prepended by partition (`/Common/foo`), or specified just as an object name (`foo`).  To remove the entry. set a value of `''`, however the profile `log_publisher` must also be set as `''`. |
| **log_publisher**  string | Specifies the publisher defined to log messages.  Format of the name can be either be prepended by partition (`/Common/foo`), or specified just as an object name (`foo`).  To remove the entry. set a value of `''`, however the profile `log_profile` must also be set as `''`. |
| **max_size**  integer | Specifies the maximum SIP message size that the BIG-IP system accepts.  The accepted value range is `0 - 4294967295` bytes. |
| **name**  string / required | Specifies the name of the SIP profile to manage. |
| **parent**  string | Specifies the profile from which this profile inherits settings.  When creating a new profile, if this parameter is not specified, the default is the system-supplied `sip` profile. |
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
| **secure_via_header**  boolean | When checked (enabled), inserts a secure Via header in the forwarded SIP request.  A secure Via header indicates where the message originated.  This parameter causes the inserted Via header to specify Transport Layer Security. For this option to take effect, `insert_via_header` must be set to (yes).  Choices:   - `false` - `true` |
| **security**  boolean | When `yes`. enables the use of enhanced Horizontal Security Layer (HSL) security checking.  Choices:   - `false` - `true` |
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **terminate_on_bye**  boolean | When `yes`, closes a connection when a BYE transaction finishes.  A BYE transaction is a message an application sends to another application when it is ready to close the connection between the two.  Choices:   - `false` - `true` |
| **user_via_header**  string | When `insert_via_header` is `yes`, specifies the Via value the system inserts as the top Via header in a SIP REQUEST message.  The valid value must include SIP protocol and sent_by settings, for example: `SIP/2.0/UDP 10.10.10.10:5060`.  To remove the entry completely, set a value of `''`. |

## [Notes](bigip_profile_sip_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_sip_module.md#id4)

```yaml+jinja
- name: Create a SIP profile
  bigip_profile_sip:
    name: foo
    parent: sip
    log_profile: alg_log
    log_publisher: foo-publisher
    description: this is a new profile
    security: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Update SIP profile
  bigip_profile_sip:
    name: foo
    insert_record_route_header: yes
    enable_sip_firewall: yes
    insert_via_header: yes
    user_via_header: "SIP/2.0/UDP 10.10.10.10:5060"
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Delete a SIP profile
  bigip_profile_sip:
    name: foo
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_profile_sip_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **community**  string | Indicates whether the pair belongs to the same SIP proxy functional group.  Returned: changed  Sample: `"foo_community"` |
| **description**  string | Description of the profile.  Returned: changed  Sample: `"custom description"` |
| **dialog_aware**  boolean | Specifies if the system gathers SIP dialog information.  Returned: changed  Sample: `false` |
| **enable_sip_firewall**  boolean | Specifies whether the Advanced Firewall Manager policy is enabled.  Returned: changed  Sample: `true` |
| **insert_record_route_header**  boolean | Specifies if the system will insert a Record-Route SIP header.  Returned: changed  Sample: `true` |
| **insert_via_header**  boolean | Specifies if the system will insert a Via header in the forwarded SIP request.  Returned: changed  Sample: `true` |
| **log_profile**  string | The logging settings the publisher uses to send log messages.  Returned: changed  Sample: `"/Common/alg_profile"` |
| **log_publisher**  string | The publisher defined to log messages.  Returned: changed  Sample: `"/Common/foo_publisher"` |
| **max_size**  boolean | Specifies if the system will close a connection when a BYE transaction finishes.  Returned: changed  Sample: `false` |
| **parent**  string | Specifies the profile from which this profile inherits settings.  Returned: changed  Sample: `"/Common/sip"` |
| **secure_via_header**  boolean | Specifies if the system will insert a secure Via header in the forwarded SIP request.  Returned: changed  Sample: `false` |
| **security**  boolean | Enables the use of enhanced Horizontal Security Layer security checking.  Returned: changed  Sample: `true` |
| **terminate_on_bye**  boolean | Specifies if the system will close a connection when a BYE transaction finishes.  Returned: changed  Sample: `false` |
| **user_via_header**  string | The value the system inserts as the top Via header in a SIP REQUEST message.  Returned: changed  Sample: `"SIP/2.0/UDP 10.10.10.10:5060"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

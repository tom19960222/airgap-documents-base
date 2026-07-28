---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_smtp module – Manages SMTP settings on the BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_smtp_module.html
fetched_at: 2026-07-27T17:27:43+00:00
---
# f5networks.f5_modules.bigip_smtp module – Manages SMTP settings on the BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_smtp`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_smtp_module.md#synopsis)
- [Parameters](bigip_smtp_module.md#parameters)
- [Notes](bigip_smtp_module.md#notes)
- [Examples](bigip_smtp_module.md#examples)
- [Return Values](bigip_smtp_module.md#return-values)

## [Synopsis](bigip_smtp_module.md#id1)

- Allows configuring of the BIG-IP to send mail via an SMTP server by configuring the parameters of an SMTP server.

## [Parameters](bigip_smtp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **authentication**  boolean | Credentials can be set on an SMTP server’s configuration even if that authentication is not used (for example, staging configs or emergency changes). This parameter acts as a switch to make the specified `smtp_server_username` and `smtp_server_password` parameters active or not.  When `yes`, the authentication parameters are active.  When `no`, the authentication parameters are inactive.  Choices:   - `false` - `true` |
| **encryption**  string | Specifies whether the SMTP server requires an encrypted connection in order to send mail.  Choices:   - `"none"` - `"ssl"` - `"tls"` |
| **from_address**  string | Email address from which the email is being sent. This is the “Reply-to” address the recipient sees. |
| **local_host_name**  string | Hostname used in SMTP headers in the format of a fully qualified domain name. This setting does not refer to the hostname of the BIG-IP system. |
| **name**  string / required | Specifies the name of the SMTP server configuration. |
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
| **smtp_server**  string | SMTP server host name in the format of a fully qualified domain name.  This value is required when creating a new SMTP configuration. |
| **smtp_server_password**  string | Password the SMTP server requires when validating a user. |
| **smtp_server_port**  integer | Specifies the SMTP port number.  When creating a new SMTP configuration, the default is `25` when `encryption` is `none` or `tls`. The default is `465` when `ssl` is selected. |
| **smtp_server_username**  string | User name the SMTP server requires when validating a user. |
| **state**  string | When `present`, ensures the SMTP configuration exists.  When `absent`, ensures the SMTP configuration does not exist.  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | Passwords are stored encrypted, so the module cannot know if the supplied `smtp_server_password` is the same or different than the existing password. This parameter controls the updating of the `smtp_server_password` credential.  When `always`, the system always updates the password.  When `on_create`, the system only sets the password for newly created SMTP server configurations.  Choices:   - `"always"` ← (default) - `"on_create"` |

## [Notes](bigip_smtp_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_smtp_module.md#id4)

```yaml+jinja
- name: Create a base SMTP server configuration
  bigip_smtp:
    name: my-smtp
    smtp_server: 1.1.1.1
    smtp_server_username: mail-admin
    smtp_server_password: mail-secret
    local_host_name: smtp.mydomain.com
    from_address: no-reply@mydomain.com
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_smtp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **authentication**  boolean | Whether the authentication parameters are active or not.  Returned: changed  Sample: `true` |
| **encryption**  string | The new `encryption` value of the SMTP configuration.  Returned: changed  Sample: `"tls"` |
| **from_address**  string | The new `from_address` value of the SMTP configuration.  Returned: changed  Sample: `"no-reply@mydomain.com"` |
| **local_host_name**  string | The new `local_host_name` value of the SMTP configuration.  Returned: changed  Sample: `"smtp.mydomain.com"` |
| **smtp_server**  string | The new `smtp_server` value of the SMTP configuration.  Returned: changed  Sample: `"mail.mydomain.com"` |
| **smtp_server_port**  integer | The new `smtp_server_port` value of the SMTP configuration.  Returned: changed  Sample: `25` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

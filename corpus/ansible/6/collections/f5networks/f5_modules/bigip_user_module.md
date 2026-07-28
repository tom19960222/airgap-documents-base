---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_user module – Manage user accounts and user attributes on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_user_module.html
fetched_at: 2026-07-27T17:28:00+00:00
---
# f5networks.f5_modules.bigip_user module – Manage user accounts and user attributes on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_user`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_user_module.md#synopsis)
- [Parameters](bigip_user_module.md#parameters)
- [Notes](bigip_user_module.md#notes)
- [Examples](bigip_user_module.md#examples)
- [Return Values](bigip_user_module.md#return-values)

## [Synopsis](bigip_user_module.md#id1)

- Manage user accounts and user attributes on a BIG-IP system. Typically this module operates only on REST API users and not CLI users. When specifying `root`, you may only change the password. Your other parameters are ignored in this case. Changing the `root` password is not an idempotent operation. Therefore, it changes the password every time this module attempts to change it.

## [Parameters](bigip_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **full_name**  string | Full name of the user. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **partition_access**  list / elements=string | Specifies the administrative partition to which the user has access. `partition_access` is required when creating a new account, and should be in the form “partition:role”.  Valid roles include `acceleration-policy-editor`, `admin`, `application-editor`, `auditor`, `certificate-manager`, `guest`, `irule-manager`, `manager`, `no-access`, `operator`, `resource-admin`, `user-manager`, `web-application-security-administrator`, and `web-application-security-editor`.  The partition portion the of tuple should be an existing partition or the value ‘all’. |
| **password_credential**  string | Set the user’s password to this unencrypted value. `password_credential` is required when creating a new account. |
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
| **shell**  string | Optionally set the users shell.  Choices:   - `"bash"` - `"none"` - `"tmsh"` |
| **state**  string | Whether the account should exist or not, taking action if the state is different from what is stated.  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | `always` allows the user to update passwords. `on_create` only sets the password for newly created users.  When `username_credential` is `root`, this value is forced to `always`.  Choices:   - `"always"` ← (default) - `"on_create"` |
| **username_credential**  aliases: name  string / required | Name of the user to create, remove, or modify.  The `root` user may not be removed. |

## [Notes](bigip_user_module.md#id3)

> **Note:**
>
> - Requires BIG-IP versions >= 12.0.0
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_user_module.md#id4)

```yaml+jinja
- name: Add the user 'johnd' as an admin
  bigip_user:
    username_credential: johnd
    password_credential: password
    full_name: John Doe
    partition_access:
      - all:admin
    update_password: on_create
    state: present
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Change the user "johnd's" role and shell
  bigip_user:
    username_credential: johnd
    partition_access:
      - NewPartition:manager
    shell: tmsh
    state: present
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Make the user 'johnd' an admin and set to advanced shell
  bigip_user:
    name: johnd
    partition_access:
      - all:admin
    shell: bash
    state: present
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove the user 'johnd'
  bigip_user:
    name: johnd
    state: absent
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Update password
  bigip_user:
    state: present
    username_credential: johnd
    password_credential: newsupersecretpassword
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

# Note that the second time this task runs, it would fail because
# The password has been changed. Therefore, it is recommended that
# you either,
#
#   * Put this in its own playbook that you run when you need to
#   * Put this task in a `block`
#   * Include `ignore_errors` on this task
- name: Change the Admin password
  bigip_user:
    state: present
    username_credential: admin
    password_credential: NewSecretPassword
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Change the root user's password
  bigip_user:
    username_credential: root
    password_credential: secret
    state: present
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **full_name**  string | Full name of the user.  Returned: changed and success  Sample: `"John Doe"` |
| **partition_access**  list / elements=string | List of strings containing the user’s roles and to which partitions they are applied. They are specified in the form “partition:role”.  Returned: changed and success  Sample: `["all:admin"]` |
| **shell**  string | The shell assigned to the user account.  Returned: changed and success  Sample: `"tmsh"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

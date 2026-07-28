---
collection: ansible
version: "6"
title: "cisco.mso.mso_user module – Manage users"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/mso/mso_user_module.html
fetched_at: 2026-07-27T17:01:27+00:00
---
# cisco.mso.mso_user module – Manage users

> **Note:**
>
> This module is part of the [cisco.mso collection](https://galaxy.ansible.com/cisco/mso) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.mso`.
> You need further requirements to be able to use this module,
> see [Requirements](mso_user_module.md#ansible-collections-cisco-mso-mso-user-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_user`.

- [Synopsis](mso_user_module.md#synopsis)
- [Requirements](mso_user_module.md#requirements)
- [Parameters](mso_user_module.md#parameters)
- [Notes](mso_user_module.md#notes)
- [Examples](mso_user_module.md#examples)

## [Synopsis](mso_user_module.md#id1)

- Manage users on Cisco ACI Multi-Site.

## [Requirements](mso_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_status**  string | The status of the user account.  Choices:   - `"active"` - `"inactive"` |
| **domain**  string | The domain this user belongs to.  When creating new users, this defaults to `Local`. |
| **email**  string | The email address of the user.  This parameter is required when creating new users. |
| **first_name**  string | The first name of the user.  This parameter is required when creating new users. |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **last_name**  string | The last name of the user.  This parameter is required when creating new users. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  Choices:   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **phone**  string | The phone number of the user.  This parameter is required when creating new users. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **roles**  list / elements=string | The roles for this user and their access types (read or write).  Access type defaults to `write`. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **timeout**  integer | The socket level timeout in seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead.  Default: `30` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `no` when using a HTTPAPI connection plugin (mso or nd) and `yes` when using the legacy connection method (only for mso).  Choices:   - `false` - `true` |
| **user**  aliases: name  string | The name of the user. |
| **user_password**  string | The password of the user. |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `yes`.  Choices:   - `false` - `true` |

## [Notes](mso_user_module.md#id4)

> **Note:**
>
> - A default installation of ACI Multi-Site ships with admin password ‘we1come!’ which requires a password change on first login. See the examples of how to change the ‘admin’ password using Ansible.
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [Examples](mso_user_module.md#id5)

```yaml+jinja
- name: Update initial admin password
  cisco.mso.mso_user:
    host: mso_host
    username: admin
    password: initialPassword
    validate_certs: false
    user: admin
    user_password: newPassword
    state: present
  delegate_to: localhost

- name: Add a new user
  cisco.mso.mso_user:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    validate_certs: false
    user: dag
    user_password: userPassword
    first_name: Dag
    last_name: Wieers
    email: dag@wieers.com
    phone: +32 478 436 299
    roles:
    - name: siteManager
      access_type: write
    - name: schemaManager
      access_type: read
    state: present
  delegate_to: localhost

- name: Add a new user
  cisco.mso.mso_user:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    validate_certs: false
    user: dag
    first_name: Dag
    last_name: Wieers
    email: dag@wieers.com
    phone: +32 478 436 299
    roles:
    - powerUser
  delegate_to: localhost

- name: Remove a user
  cisco.mso.mso_user:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    validate_certs: false
    user: dag
    state: absent
  delegate_to: localhost

- name: Query a user
  cisco.mso.mso_user:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    validate_certs: false
    user: dag
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all users
  cisco.mso.mso_user:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    validate_certs: false
    state: query
  delegate_to: localhost
  register: query_result
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
[Homepage](https://cisco.com/go/aci)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

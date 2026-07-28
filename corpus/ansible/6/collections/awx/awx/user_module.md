---
collection: ansible
version: "6"
title: "awx.awx.user module – create, update, or destroy Automation Platform Controller users."
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/user_module.html
fetched_at: 2026-07-27T16:45:35+00:00
---
# awx.awx.user module – create, update, or destroy Automation Platform Controller users.

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/awx/awx) (version 21.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
>
> To use it in a playbook, specify: `awx.awx.user`.

- [Synopsis](user_module.md#synopsis)
- [Parameters](user_module.md#parameters)
- [Notes](user_module.md#notes)
- [Examples](user_module.md#examples)

## [Synopsis](user_module.md#id1)

- Create, update, or destroy Automation Platform Controller users. See <https://www.ansible.com/tower> for an overview.

## [Parameters](user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **email**  string | Email address of the user. |
| **first_name**  string | First name of the user. |
| **is_superuser**  aliases: superuser  boolean | Designates that this user has all permissions without explicitly assigning them.  Choices:   - `false` ← (default) - `true` |
| **is_system_auditor**  aliases: auditor  boolean | User is a system wide auditor.  Choices:   - `false` ← (default) - `true` |
| **last_name**  string | Last name of the user. |
| **new_username**  string | Setting this option will change the existing username (looked up via the name field. |
| **organization**  string | The user will be created as a member of that organization (needed for organization admins to create new organization users). |
| **password**  string | Write-only field used to change the password. |
| **state**  string | Desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_secrets**  boolean | `true` will always change password if user specifies password, even if API gives $encrypted$ for password.  `false` will only set the password if other values change too.  Choices:   - `false` - `true` ← (default) |
| **username**  string / required | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |

## [Notes](user_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](user_module.md#id4)

```yaml+jinja
- name: Add user
  user:
    username: jdoe
    password: foobarbaz
    email: jdoe@example.org
    first_name: John
    last_name: Doe
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add user as a system administrator
  user:
    username: jdoe
    password: foobarbaz
    email: jdoe@example.org
    superuser: yes
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add user as a system auditor
  user:
    username: jdoe
    password: foobarbaz
    email: jdoe@example.org
    auditor: yes
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add user as a member of an organization (permissions on the organization are required)
  user:
    username: jdoe
    password: foobarbaz
    email: jdoe@example.org
    organization: devopsorg
    state: present

- name: Delete user
  user:
    username: jdoe
    email: jdoe@example.org
    state: absent
    controller_config_file: "~/tower_cli.cfg"
```

### Authors

- John Westcott IV (@john-westcott-iv)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)

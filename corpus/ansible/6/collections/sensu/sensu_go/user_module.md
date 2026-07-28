---
collection: ansible
version: "6"
title: "sensu.sensu_go.user module – Manage Sensu users"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/user_module.html
fetched_at: 2026-07-28T00:19:51+00:00
---
# sensu.sensu_go.user module – Manage Sensu users

> **Note:**
>
> This module is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/sensu/sensu_go) (version 1.13.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
> You need further requirements to be able to use this module,
> see [Requirements](user_module.md#ansible-collections-sensu-sensu-go-user-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.user`.

New in sensu.sensu_go 1.0.0

- [Synopsis](user_module.md#synopsis)
- [Requirements](user_module.md#requirements)
- [Parameters](user_module.md#parameters)
- [See Also](user_module.md#see-also)
- [Examples](user_module.md#examples)
- [Return Values](user_module.md#return-values)

## [Synopsis](user_module.md#id1)

- Create, update, activate or deactivate Sensu user.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/reference/rbac/#users>.

## [Requirements](user_module.md#id2)

The below requirements are needed on the host that executes this module.

- bcrypt (when managing Sensu Go 5.21.0 or newer)
- python >= 2.7

## [Parameters](user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  added in sensu.sensu_go 1.3.0 | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  added in sensu.sensu_go 1.5.0 | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  Default: `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"admin"` |
| **verify**  boolean  added in sensu.sensu_go 1.5.0 | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  Choices:   - `false` - `true` ← (default) |
| **groups**  list / elements=string | List of groups user belongs to. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **password**  string | Password for the user.  Required if user with a desired name does not exist yet on the backend and *password_hash* is not set.  If both *password* and *password_hash* are set, *password_hash* is ignored and calculated from the *password* if required. |
| **password_hash**  string  added in sensu.sensu_go 1.8.0 | Bcrypt password hash for the user.  Use `sensuctl user hash-password PASSWORD` to generate a hash.  Required if user with a desired name does not exist yet on the backend and *password* is not set.  If both *password* and *password_hash* are set, *password_hash* is ignored and calculated from the *password* if required.  Sensu Go < 5.21.0 does not support creating/updating users using hashed passwords. Use *password* parameter if you need to manage such Sensu Go installations.  At the moment, change detection does not work properly when using password hashes because the Sensu Go backend does not expose enough information via its API. |
| **state**  string | Desired state of the user.  Users cannot actually be deleted, only deactivated.  Choices:   - `"enabled"` ← (default) - `"disabled"` |

## [See Also](user_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.user_info](user_info_module.md#ansible-collections-sensu-sensu-go-user-info-module)
> :   List Sensu users.

## [Examples](user_module.md#id5)

```yaml+jinja
- name: Create a user
  sensu.sensu_go.user:
    auth:
      url: http://localhost:8080
    name: awesome_username
    password: hidden_password?
    groups:
      - dev
      - prod

- name: Use pre-hashed password
  sensu.sensu_go.user:
    auth:
      url: http://localhost:8080
    name: awesome_username
    password_hash: $5f$14$.brXRviMZpbaleSq9kjoUuwm67V/s4IziOLGHjEqxJbzPsreQAyNm

- name: Deactivate a user
  sensu.sensu_go.user:
    name: awesome_username
    state: disabled
```

## [Return Values](user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu user.  Returned: success  Sample: `{"disabled": false, "groups": ["ops", "dev"], "password": "USER_PASSWORD", "password_hash": "$5f$14$.brXRviMZpbaleSq9kjoUuwm67V/s4IziOLGHjEqxJbzPsreQAyNm", "username": "alice"}` |

### Authors

- Paul Arthur (@flowerysong)
- Aljaz Kosir (@aljazkosir)
- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)

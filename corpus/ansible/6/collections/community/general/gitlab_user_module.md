---
collection: ansible
version: "6"
title: "community.general.gitlab_user module – Creates/updates/deletes/blocks/unblocks GitLab Users"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/gitlab_user_module.html
fetched_at: 2026-07-27T17:09:13+00:00
---
# community.general.gitlab_user module – Creates/updates/deletes/blocks/unblocks GitLab Users

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](gitlab_user_module.md#ansible-collections-community-general-gitlab-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_user`.

- [Synopsis](gitlab_user_module.md#synopsis)
- [Requirements](gitlab_user_module.md#requirements)
- [Parameters](gitlab_user_module.md#parameters)
- [Notes](gitlab_user_module.md#notes)
- [Examples](gitlab_user_module.md#examples)
- [Return Values](gitlab_user_module.md#return-values)

## [Synopsis](gitlab_user_module.md#id1)

- When the user does not exist in GitLab, it will be created.
- When the user exists and state=absent, the user will be deleted.
- When the user exists and state=blocked, the user will be blocked.
- When changes are made to user, the user will be updated.

## [Requirements](gitlab_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- administrator rights on the GitLab server
- python >= 2.7
- python-gitlab python module
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_level**  string | The access level to the group. One of the following can be used.  guest  reporter  developer  master (alias for maintainer)  maintainer  owner  Choices:   - `"guest"` ← (default) - `"reporter"` - `"developer"` - `"master"` - `"maintainer"` - `"owner"` |
| **api_job_token**  string  added in community.general 4.2.0 | GitLab CI job token for logging in. |
| **api_oauth_token**  string  added in community.general 4.2.0 | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **confirm**  boolean | Require confirmation.  Choices:   - `false` - `true` ← (default) |
| **email**  string | The email that belongs to the user.  Required only if `state` is set to `present`. |
| **external**  boolean | Define external parameter for this user.  Choices:   - `false` ← (default) - `true` |
| **group**  string | Id or Full path of parent group in the form of group/name.  Add user as a member to this group. |
| **identities**  list / elements=dictionary  added in community.general 3.3.0 | List of identities to be added/updated for this user.  To remove all other identities from this user, set *overwrite_identities=true*. |
| **extern_uid**  string | User ID for external identity. |
| **provider**  string | The name of the external identity provider |
| **isadmin**  boolean | Grant admin privileges to the user.  Choices:   - `false` ← (default) - `true` |
| **name**  string | Name of the user you want to create.  Required only if `state` is set to `present`. |
| **overwrite_identities**  boolean  added in community.general 3.3.0 | Overwrite identities with identities added in this module.  This means that all identities that the user has and that are not listed in *identities* are removed from the user.  This is only done if a list is provided for *identities*. To remove all identities, provide an empty list.  Choices:   - `false` ← (default) - `true` |
| **password**  string | The password of the user.  GitLab server enforces minimum password length to 8, set this value with 8 or more characters. |
| **reset_password**  boolean  added in community.general 3.3.0 | Whether the user can change its password or not.  Choices:   - `false` ← (default) - `true` |
| **sshkey_expires_at**  string  added in community.general 3.1.0 | The expiration date of the SSH public key in ISO 8601 format `YYYY-MM-DDTHH:MM:SSZ`.  This is only used when adding new SSH public keys. |
| **sshkey_file**  string | The SSH public key itself. |
| **sshkey_name**  string | The name of the SSH public key. |
| **state**  string | Create, delete or block a user.  Choices:   - `"present"` ← (default) - `"absent"` - `"blocked"` - `"unblocked"` |
| **username**  string / required | The username of the user. |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  Choices:   - `false` - `true` ← (default) |

## [Notes](gitlab_user_module.md#id4)

> **Note:**
>
> - From community.general 0.2.0 and onwards, name, email and password are optional while deleting the user.

## [Examples](gitlab_user_module.md#id5)

```yaml+jinja
- name: "Delete GitLab User"
  community.general.gitlab_user:
    api_url: https://gitlab.example.com/
    api_token: "{{ access_token }}"
    validate_certs: false
    username: myusername
    state: absent

- name: "Create GitLab User"
  community.general.gitlab_user:
    api_url: https://gitlab.example.com/
    validate_certs: true
    api_username: dj-wasabi
    api_password: "MySecretPassword"
    name: My Name
    username: myusername
    password: mysecretpassword
    email: me@example.com
    sshkey_name: MySSH
    sshkey_file: ssh-rsa AAAAB3NzaC1yc...
    state: present
    group: super_group/mon_group
    access_level: owner

- name: "Create GitLab User using external identity provider"
  community.general.gitlab_user:
    api_url: https://gitlab.example.com/
    validate_certs: true
    api_token: "{{ access_token }}"
    name: My Name
    username: myusername
    password: mysecretpassword
    email: me@example.com
    identities:
    - provider: Keycloak
      extern_uid: f278f95c-12c7-4d51-996f-758cc2eb11bc
    state: present
    group: super_group/mon_group
    access_level: owner

- name: "Block GitLab User"
  community.general.gitlab_user:
    api_url: https://gitlab.example.com/
    api_token: "{{ access_token }}"
    validate_certs: false
    username: myusername
    state: blocked

- name: "Unblock GitLab User"
  community.general.gitlab_user:
    api_url: https://gitlab.example.com/
    api_token: "{{ access_token }}"
    validate_certs: false
    username: myusername
    state: unblocked
```

## [Return Values](gitlab_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error**  string | the error message returned by the GitLab API  Returned: failed  Sample: `"400: path is already in use"` |
| **msg**  string | Success or failure message  Returned: always  Sample: `"Success"` |
| **result**  dictionary | json parsed response from the server  Returned: always |
| **user**  dictionary | API object  Returned: always |

### Authors

- Werner Dijkerman (@dj-wasabi)
- Guillaume Martinez (@Lunik)
- Lennert Mertens (@LennertMertens)
- Stef Graces (@stgrace)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

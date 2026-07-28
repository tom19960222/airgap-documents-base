---
collection: ansible
version: "8"
title: "community.network.avi_useraccount module – Avi UserAccount Module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/avi_useraccount_module.html
fetched_at: 2026-07-28T01:55:03+00:00
---
# community.network.avi_useraccount module – Avi UserAccount Module

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](avi_useraccount_module.md#ansible-collections-community-network-avi-useraccount-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_useraccount`.

- [Synopsis](avi_useraccount_module.md#synopsis)
- [Requirements](avi_useraccount_module.md#requirements)
- [Parameters](avi_useraccount_module.md#parameters)
- [Notes](avi_useraccount_module.md#notes)
- [Examples](avi_useraccount_module.md#examples)
- [Return Values](avi_useraccount_module.md#return-values)

## [Synopsis](avi_useraccount_module.md#id1)

- This module can be used for updating the password of a user.
- This module is useful for setting up admin password for Controller bootstrap.

Aliases: network.avi.avi_useraccount

## [Requirements](avi_useraccount_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_useraccount_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  **Default:** `"16.4.4"` |
| **avi_credentials**  dictionary | Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details. |
| **api_version**  string | Avi controller version  **Default:** `"16.4.4"` |
| **controller**  string | Avi controller IP or SQDN |
| **csrftoken**  string | Avi controller API csrftoken to reuse existing session with session id  **Default:** `""` |
| **password**  string | Avi controller password |
| **port**  string | Avi controller port |
| **session_id**  string | Avi controller API session id to reuse existing session with csrftoken  **Default:** `""` |
| **tenant**  string | Avi controller tenant  **Default:** `"admin"` |
| **tenant_uuid**  string | Avi controller tenant UUID  **Default:** `""` |
| **timeout**  string | Avi controller request timeout  **Default:** `300` |
| **token**  string | Avi controller API token  **Default:** `""` |
| **username**  string | Avi controller username |
| **avi_disable_session_cache_as_fact**  boolean | It disables avi session information to be cached as a fact.  **Choices:**   - `false` ← (default) - `true` |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **force_change**  string | If specifically set to true then old password is tried first for controller and then the new password is tried. If not specified this flag then the new password is tried first.  **Default:** `false` |
| **old_password**  string | Old password for update password or default password for bootstrap. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  **Default:** `"admin"` |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  **Default:** `""` |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |

## [Notes](avi_useraccount_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_useraccount_module.md#id5)

```yaml+jinja
- name: Update user password
  community.network.avi_useraccount:
    controller: ""
    username: ""
    password: new_password
    old_password: ""
    api_version: ""
    force_change: false

- name: Update user password using avi_credentials
  community.network.avi_useraccount:
    avi_credentials: ""
    old_password: ""
    force_change: false
```

## [Return Values](avi_useraccount_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | Avi REST resource  **Returned:** success, changed |

### Authors

- Chaitanya Deshpande (@chaitanyaavi)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)

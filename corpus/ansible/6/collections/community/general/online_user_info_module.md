---
collection: ansible
version: "6"
title: "community.general.online_user_info module – Gather information about Online user"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/online_user_info_module.html
fetched_at: 2026-07-27T17:11:32+00:00
---
# community.general.online_user_info module – Gather information about Online user

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.online_user_info`.

- [Synopsis](online_user_info_module.md#synopsis)
- [Parameters](online_user_info_module.md#parameters)
- [Notes](online_user_info_module.md#notes)
- [Examples](online_user_info_module.md#examples)
- [Return Values](online_user_info_module.md#return-values)

## [Synopsis](online_user_info_module.md#id1)

- Gather information about the user.

## [Parameters](online_user_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Online API in seconds.  Default: `30` |
| **api_token**  aliases: oauth_token  string / required | Online OAuth token. |
| **api_url**  aliases: base_url  string | Online API URL  Default: `"https://api.online.net"` |
| **validate_certs**  boolean | Validate SSL certs of the Online API.  Choices:   - `false` - `true` ← (default) |

## [Notes](online_user_info_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://console.online.net/en/api/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence `ONLINE_TOKEN`, `ONLINE_API_KEY`, `ONLINE_OAUTH_TOKEN`, `ONLINE_API_TOKEN`
> - If one wants to use a different `api_url` one can also set the `ONLINE_API_URL` environment variable.

## [Examples](online_user_info_module.md#id4)

```yaml+jinja
- name: Gather Online user info
  community.general.online_user_info:
  register: result

- ansible.builtin.debug:
    msg: "{{ result.online_user_info }}"
```

## [Return Values](online_user_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **online_user_info**  dictionary | Response from Online API.  For more details please refer to: <https://console.online.net/en/api/>.  Returned: success  Sample: `{"online_user_info": {"company": "foobar LLC", "email": "foobar@example.com", "first_name": "foo", "id": 42, "last_name": "bar", "login": "foobar"}}` |

### Authors

- Remy Leone (@remyleone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

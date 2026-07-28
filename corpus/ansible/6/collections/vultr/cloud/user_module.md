---
collection: ansible
version: "6"
title: "vultr.cloud.user module – Manages users on Vultr"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vultr/cloud/user_module.html
fetched_at: 2026-07-28T00:23:09+00:00
---
# vultr.cloud.user module – Manages users on Vultr

> **Note:**
>
> This module is part of the [vultr.cloud collection](https://galaxy.ansible.com/vultr/cloud) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vultr.cloud`.
>
> To use it in a playbook, specify: `vultr.cloud.user`.

New in vultr.cloud 1.0.0

- [Synopsis](user_module.md#synopsis)
- [Parameters](user_module.md#parameters)
- [Notes](user_module.md#notes)
- [Examples](user_module.md#examples)
- [Return Values](user_module.md#return-values)

## [Synopsis](user_module.md#id1)

- Create, update and remove users.

## [Parameters](user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **acls**  aliases: acl  list / elements=string | List of ACLs this users should have.  Required if `state=present`.  One or more of the choices list, some depend on each other.  Choices:   - `"manage_users"` - `"subscriptions_view"` - `"subscriptions"` - `"provisioning"` - `"billing"` - `"support"` - `"abuse"` - `"dns"` - `"upgrade"` - `"objstore"` - `"loadbalancer"` |
| **api_enabled**  boolean | Whether the API is enabled or not.  Choices:   - `false` - `true` ← (default) |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  Default: `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  Default: `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  Default: `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  Default: `60` |
| **email**  string | Email of the user.  Required if `state=present`. |
| **force**  boolean | Password will only be changed with enforcement.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Name of the user |
| **password**  string | Password of the user.  Only considered while creating a user or when `force=yes`. |
| **state**  string | State of the user.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  Choices:   - `false` - `true` ← (default) |

## [Notes](user_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](user_module.md#id4)

```yaml+jinja
- name: Ensure a user exists
  vultr.cloud.user:
    name: john
    email: john.doe@example.com
    password: s3cr3t
    acls:
    - manage_users
    - subscriptions

- name: Remove a user
  vultr.cloud.user:
    name: john
    state: absent
```

## [Return Values](user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  Returned: success |
| **api_endpoint**  string | Endpoint used for the API requests.  Returned: success  Sample: `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  Returned: success  Sample: `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  Returned: success  Sample: `12` |
| **api_timeout**  integer | Timeout used for the API requests.  Returned: success  Sample: `60` |
| **vultr_user**  dictionary | Response from Vultr API.  Returned: success |
| **acls**  list / elements=string | List of ACLs of the user.  Returned: success  Sample: `["manage_users", "support", "upgrade"]` |
| **api_enabled**  boolean | Whether the API is enabled or not.  Returned: success  Sample: `true` |
| **api_key**  string | API key of the user.  Returned: only after resource was created  Sample: `"567E6K567E6K567E6K567E6K567E6K"` |
| **email**  string | Email of the user.  Returned: success  Sample: `"john@example.com"` |
| **id**  string | ID of the user.  Returned: success  Sample: `"7d726ffe-9be2-4f88-8cda-fa7eba1da2b5"` |
| **name**  string | Name of the user.  Returned: success  Sample: `"john"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
[Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)

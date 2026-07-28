---
collection: ansible
version: "8"
title: "community.general.redis_data_incr module – Increment keys in Redis"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/redis_data_incr_module.html
fetched_at: 2026-07-28T01:49:55+00:00
---
# community.general.redis_data_incr module – Increment keys in Redis

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](redis_data_incr_module.md#ansible-collections-community-general-redis-data-incr-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.redis_data_incr`.

New in community.general 4.0.0

- [Synopsis](redis_data_incr_module.md#synopsis)
- [Requirements](redis_data_incr_module.md#requirements)
- [Parameters](redis_data_incr_module.md#parameters)
- [Attributes](redis_data_incr_module.md#attributes)
- [Notes](redis_data_incr_module.md#notes)
- [See Also](redis_data_incr_module.md#see-also)
- [Examples](redis_data_incr_module.md#examples)
- [Return Values](redis_data_incr_module.md#return-values)

## [Synopsis](redis_data_incr_module.md#id1)

- Increment integers or float keys in Redis database and get new value.
- Default increment for all keys is 1. For specific increments use the `increment_int` and `increment_float` options.

Aliases: database.misc.redis_data_incr

## [Requirements](redis_data_incr_module.md#id2)

The below requirements are needed on the host that executes this module.

- redis
- certifi

## [Parameters](redis_data_incr_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_certs**  string | Path to root certificates file. If not set and `tls` is set to `true`, certifi ca-certificates will be used. |
| **increment_float**  float | Float amount to increment the key by.  This only works with keys that contain float values in their string representation. |
| **increment_int**  integer | Integer amount to increment the key by. |
| **key**  string / required | Database key. |
| **login_host**  string | Specify the target host running the database.  **Default:** `"localhost"` |
| **login_password**  string | Specify the password to authenticate with.  Usually not used when target is localhost. |
| **login_port**  integer | Specify the port to connect to.  **Default:** `6379` |
| **login_user**  string | Specify the user to authenticate with.  Requires [redis](https://pypi.org/project/redis) >= 3.4.0. |
| **tls**  boolean | Specify whether or not to use TLS for the connection.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Specify whether or not to validate TLS certificates.  This should only be turned off for personally controlled sites or with `localhost` as target.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](redis_data_incr_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **partial**  For `check_mode` to work, the specified `login_user` needs permission to run the `GET` command on the key, otherwise the module will fail.  When using `check_mode` the module will try to calculate the value that Redis would return. If the key is not present, 0.0 is used as value. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](redis_data_incr_module.md#id5)

> **Note:**
>
> - Requires the `redis` Python package on the remote host. You can install it with pip (`pip install redis`) or with a package manager. Information on the library can be found at <https://github.com/andymccurdy/redis-py>.

## [See Also](redis_data_incr_module.md#id6)

> **See also:**
>
> [community.general.redis_data](redis_data_module.md#ansible-collections-community-general-redis-data-module)
> :   Set key value pairs in Redis.
>
> [community.general.redis_data_info](redis_data_info_module.md#ansible-collections-community-general-redis-data-info-module)
> :   Get value of key in Redis database.
>
> [community.general.redis](redis_module.md#ansible-collections-community-general-redis-module)
> :   Various redis commands, replica and flush.

## [Examples](redis_data_incr_module.md#id7)

```yaml+jinja
- name: Increment integer key foo on localhost with no username and print new value
  community.general.redis_data_incr:
    login_host: localhost
    login_password: supersecret
    key: foo
    increment_int: 1
  register: result
- name: Print new value
  debug:
    var: result.value

- name: Increment float key foo by 20.4
  community.general.redis_data_incr:
    login_host: redishost
    login_user: redisuser
    login_password: somepass
    key: foo
    increment_float: '20.4'
```

## [Return Values](redis_data_incr_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | A short message.  **Returned:** always  **Sample:** `"Incremented key: foo by 20.4 to 65.9"` |
| **value**  float | Incremented value of key  **Returned:** on success  **Sample:** `4039.4` |

### Authors

- Andreas Botzner (@paginabianca)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

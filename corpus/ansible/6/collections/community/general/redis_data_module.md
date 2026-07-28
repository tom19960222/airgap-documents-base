---
collection: ansible
version: "6"
title: "community.general.redis_data module – Set key value pairs in Redis"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/redis_data_module.html
fetched_at: 2026-07-27T17:12:39+00:00
---
# community.general.redis_data module – Set key value pairs in Redis

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
> see [Requirements](redis_data_module.md#ansible-collections-community-general-redis-data-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.redis_data`.

New in community.general 3.7.0

- [Synopsis](redis_data_module.md#synopsis)
- [Requirements](redis_data_module.md#requirements)
- [Parameters](redis_data_module.md#parameters)
- [Notes](redis_data_module.md#notes)
- [See Also](redis_data_module.md#see-also)
- [Examples](redis_data_module.md#examples)
- [Return Values](redis_data_module.md#return-values)

## [Synopsis](redis_data_module.md#id1)

- Set key value pairs in Redis database.

## [Requirements](redis_data_module.md#id2)

The below requirements are needed on the host that executes this module.

- redis
- certifi

## [Parameters](redis_data_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_certs**  string | Path to root certificates file. If not set and *tls* is set to `true`, certifi ca-certificates will be used. |
| **existing**  boolean | Only set key if it already exists.  Choices:   - `false` - `true` |
| **expiration**  integer | Expiration time in milliseconds. Setting this flag will always result in a change in the database. |
| **keep_ttl**  boolean | Retain the time to live associated with the key.  Choices:   - `false` - `true` |
| **key**  string / required | Database key. |
| **login_host**  string | Specify the target host running the database.  Default: `"localhost"` |
| **login_password**  string | Specify the password to authenticate with.  Usually not used when target is localhost. |
| **login_port**  integer | Specify the port to connect to.  Default: `6379` |
| **login_user**  string | Specify the user to authenticate with.  Requires [redis](https://pypi.org/project/redis) >= 3.4.0. |
| **non_existing**  boolean | Only set key if it does not already exist.  Choices:   - `false` - `true` |
| **state**  string | State of the key.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tls**  boolean | Specify whether or not to use TLS for the connection.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Specify whether or not to validate TLS certificates.  This should only be turned off for personally controlled sites or with `localhost` as target.  Choices:   - `false` - `true` ← (default) |
| **value**  string | Value that key should be set to. |

## [Notes](redis_data_module.md#id4)

> **Note:**
>
> - Requires the `redis` Python package on the remote host. You can install it with pip (`pip install redis`) or with a package manager. Information on the library can be found at <https://github.com/andymccurdy/redis-py>.

## [See Also](redis_data_module.md#id5)

> **See also:**
>
> [community.general.redis_data_incr](redis_data_incr_module.md#ansible-collections-community-general-redis-data-incr-module)
> :   Increment keys in Redis.
>
> [community.general.redis_data_info](redis_data_info_module.md#ansible-collections-community-general-redis-data-info-module)
> :   Get value of key in Redis database.
>
> [community.general.redis](redis_module.md#ansible-collections-community-general-redis-module)
> :   Various redis commands, replica and flush.

## [Examples](redis_data_module.md#id6)

```yaml+jinja
- name: Set key foo=bar on localhost with no username
  community.general.redis_data:
    login_host: localhost
    login_password: supersecret
    key: foo
    value: bar
    state: present

- name: Set key foo=bar if non existing with expiration of 30s
  community.general.redis_data:
    login_host: localhost
    login_password: supersecret
    key: foo
    value: bar
    non_existing: true
    expiration: 30000
    state: present

- name: Set key foo=bar if existing and keep current TTL
  community.general.redis_data:
    login_host: localhost
    login_password: supersecret
    key: foo
    value: bar
    existing: true
    keep_ttl: true

- name: Set key foo=bar on redishost with custom ca-cert file
  community.general.redis_data:
    login_host: redishost
    login_password: supersecret
    login_user: someuser
    validate_certs: true
    ssl_ca_certs: /path/to/ca/certs
    key: foo
    value: bar

- name: Delete key foo on localhost with no username
  community.general.redis_data:
    login_host: localhost
    login_password: supersecret
    key: foo
    state: absent
```

## [Return Values](redis_data_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | A short message.  Returned: always  Sample: `"Set key: foo to bar"` |
| **old_value**  string | Value of key before setting.  Returned: on_success if state is `present` and key exists in database.  Sample: `"old_value_of_key"` |
| **value**  string | Value key was set to.  Returned: on success if state is `present`.  Sample: `"new_value_of_key"` |

### Authors

- Andreas Botzner (@paginabianca)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

---
collection: ansible
version: "6"
title: "community.general.redis module – Various redis commands, replica and flush"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/redis_module.html
fetched_at: 2026-07-27T17:12:39+00:00
---
# community.general.redis module – Various redis commands, replica and flush

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
> see [Requirements](redis_module.md#ansible-collections-community-general-redis-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.redis`.

- [Synopsis](redis_module.md#synopsis)
- [Requirements](redis_module.md#requirements)
- [Parameters](redis_module.md#parameters)
- [Notes](redis_module.md#notes)
- [See Also](redis_module.md#see-also)
- [Examples](redis_module.md#examples)

## [Synopsis](redis_module.md#id1)

- Unified utility to interact with redis instances.

## [Requirements](redis_module.md#id2)

The below requirements are needed on the host that executes this module.

- certifi
- redis

## [Parameters](redis_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_certs**  string  added in community.general 4.6.0 | Path to root certificates file. If not set and *tls* is set to `true`, certifi ca-certificates will be used. |
| **command**  string | The selected redis command  `config` ensures a configuration setting on an instance.  `flush` flushes all the instance or a specified db.  `replica` sets a redis instance in replica or master mode. (`slave` is an alias for `replica`.)  Choices:   - `"config"` - `"flush"` - `"replica"` - `"slave"` |
| **db**  integer | The database to flush (used in db mode) [flush command] |
| **flush_mode**  string | Type of flush (all the dbs in a redis instance or a specific one) [flush command]  Choices:   - `"all"` ← (default) - `"db"` |
| **login_host**  string | Specify the target host running the database.  Default: `"localhost"` |
| **login_password**  string | Specify the password to authenticate with.  Usually not used when target is localhost. |
| **login_port**  integer | Specify the port to connect to.  Default: `6379` |
| **login_user**  string  added in community.general 4.6.0 | Specify the user to authenticate with.  Requires [redis](https://pypi.org/project/redis) >= 3.4.0. |
| **master_host**  string | The host of the master instance [replica command] |
| **master_port**  integer | The port of the master instance [replica command] |
| **name**  string | A redis config key. |
| **replica_mode**  aliases: slave_mode  string | The mode of the redis instance [replica command]  `slave` is an alias for `replica`.  Choices:   - `"master"` - `"replica"` ← (default) - `"slave"` |
| **tls**  boolean  added in community.general 4.6.0 | Specify whether or not to use TLS for the connection.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean  added in community.general 4.6.0 | Specify whether or not to validate TLS certificates.  This should only be turned off for personally controlled sites or with `localhost` as target.  Choices:   - `false` - `true` ← (default) |
| **value**  string | A redis config value. When memory size is needed, it is possible to specify it in the usal form of 1KB, 2M, 400MB where the base is 1024. Units are case insensitive i.e. 1m = 1mb = 1M = 1MB. |

## [Notes](redis_module.md#id4)

> **Note:**
>
> - Requires the redis-py Python package on the remote host. You can install it with pip (pip install redis) or with a package manager. <https://github.com/andymccurdy/redis-py>
> - If the redis master instance we are making replica of is password protected this needs to be in the redis.conf in the masterauth variable
> - Requires the `redis` Python package on the remote host. You can install it with pip (`pip install redis`) or with a package manager. Information on the library can be found at <https://github.com/andymccurdy/redis-py>.

## [See Also](redis_module.md#id5)

> **See also:**
>
> [community.general.redis_info](redis_info_module.md#ansible-collections-community-general-redis-info-module)
> :   Gather information about Redis servers.

## [Examples](redis_module.md#id6)

```yaml+jinja
- name: Set local redis instance to be a replica of melee.island on port 6377
  community.general.redis:
    command: replica
    master_host: melee.island
    master_port: 6377

- name: Deactivate replica mode
  community.general.redis:
    command: replica
    replica_mode: master

- name: Flush all the redis db
  community.general.redis:
    command: flush
    flush_mode: all

- name: Flush only one db in a redis instance
  community.general.redis:
    command: flush
    db: 1
    flush_mode: db

- name: Configure local redis to have 10000 max clients
  community.general.redis:
    command: config
    name: maxclients
    value: 10000

- name: Configure local redis maxmemory to 4GB
  community.general.redis:
    command: config
    name: maxmemory
    value: 4GB

- name: Configure local redis to have lua time limit of 100 ms
  community.general.redis:
    command: config
    name: lua-time-limit
    value: 100
```

### Authors

- Xabier Larrakoetxea (@slok)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

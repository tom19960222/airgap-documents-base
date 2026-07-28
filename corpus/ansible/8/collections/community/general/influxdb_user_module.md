---
collection: ansible
version: "8"
title: "community.general.influxdb_user module – Manage InfluxDB users"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/influxdb_user_module.html
fetched_at: 2026-07-28T01:46:31+00:00
---
# community.general.influxdb_user module – Manage InfluxDB users

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
> see [Requirements](influxdb_user_module.md#ansible-collections-community-general-influxdb-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.influxdb_user`.

- [Synopsis](influxdb_user_module.md#synopsis)
- [Requirements](influxdb_user_module.md#requirements)
- [Parameters](influxdb_user_module.md#parameters)
- [Attributes](influxdb_user_module.md#attributes)
- [Examples](influxdb_user_module.md#examples)

## [Synopsis](influxdb_user_module.md#id1)

- Manage InfluxDB users.

Aliases: database.influxdb.influxdb_user

## [Requirements](influxdb_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- influxdb >= 0.9

## [Parameters](influxdb_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin**  boolean | Whether the user should be in the admin role or not.  Since version 2.8, the role will also be updated.  **Choices:**   - `false` ← (default) - `true` |
| **grants**  list / elements=dictionary | Privileges to grant to this user.  Takes a list of dicts containing the “database” and “privilege” keys.  If this argument is not provided, the current grants will be left alone.  If an empty list is provided, all grants for the user will be removed. |
| **hostname**  string | The hostname or IP address on which InfluxDB server is listening.  Since Ansible 2.5, defaulted to localhost.  **Default:** `"localhost"` |
| **password**  aliases: login_password  string | Password that will be used to authenticate against InfluxDB server.  Alias `login_password` added in Ansible 2.5.  **Default:** `"root"` |
| **path**  string  *added in community.general 0.2.0* | The path on which InfluxDB server is accessible  Only available when using python-influxdb >= 5.1.0  **Default:** `""` |
| **port**  integer | The port on which InfluxDB server is listening  **Default:** `8086` |
| **proxies**  dictionary | HTTP(S) proxy to use for Requests to connect to InfluxDB server.  **Default:** `{}` |
| **retries**  integer | Number of retries client will try before aborting.  `0` indicates try until success.  Only available when using python-influxdb >= 4.1.0  **Default:** `3` |
| **ssl**  boolean | Use https instead of http to connect to InfluxDB server.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | State of the user.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | Number of seconds Requests will wait for client to establish a connection. |
| **udp_port**  integer | UDP port to connect to InfluxDB server.  **Default:** `4444` |
| **use_udp**  boolean | Use UDP to connect to InfluxDB server.  **Choices:**   - `false` ← (default) - `true` |
| **user_name**  string / required | Name of the user. |
| **user_password**  string | Password to be set for the user. |
| **username**  aliases: login_username  string | Username that will be used to authenticate against InfluxDB server.  Alias `login_username` added in Ansible 2.5.  **Default:** `"root"` |
| **validate_certs**  boolean | If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](influxdb_user_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](influxdb_user_module.md#id5)

```yaml+jinja
- name: Create a user on localhost using default login credentials
  community.general.influxdb_user:
    user_name: john
    user_password: s3cr3t

- name: Create a user on localhost using custom login credentials
  community.general.influxdb_user:
    user_name: john
    user_password: s3cr3t
    login_username: "{{ influxdb_username }}"
    login_password: "{{ influxdb_password }}"

- name: Create an admin user on a remote host using custom login credentials
  community.general.influxdb_user:
    user_name: john
    user_password: s3cr3t
    admin: true
    hostname: "{{ influxdb_hostname }}"
    login_username: "{{ influxdb_username }}"
    login_password: "{{ influxdb_password }}"

- name: Create a user on localhost with privileges
  community.general.influxdb_user:
    user_name: john
    user_password: s3cr3t
    login_username: "{{ influxdb_username }}"
    login_password: "{{ influxdb_password }}"
    grants:
      - database: 'collectd'
        privilege: 'WRITE'
      - database: 'graphite'
        privilege: 'READ'

- name: Destroy a user using custom login credentials
  community.general.influxdb_user:
    user_name: john
    login_username: "{{ influxdb_username }}"
    login_password: "{{ influxdb_password }}"
    state: absent
```

### Authors

- Vitaliy Zhhuta (@zhhuta)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

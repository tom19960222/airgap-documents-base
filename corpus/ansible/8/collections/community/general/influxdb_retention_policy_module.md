---
collection: ansible
version: "8"
title: "community.general.influxdb_retention_policy module – Manage InfluxDB retention policies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/influxdb_retention_policy_module.html
fetched_at: 2026-07-28T01:46:30+00:00
---
# community.general.influxdb_retention_policy module – Manage InfluxDB retention policies

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
> see [Requirements](influxdb_retention_policy_module.md#ansible-collections-community-general-influxdb-retention-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.influxdb_retention_policy`.

- [Synopsis](influxdb_retention_policy_module.md#synopsis)
- [Requirements](influxdb_retention_policy_module.md#requirements)
- [Parameters](influxdb_retention_policy_module.md#parameters)
- [Attributes](influxdb_retention_policy_module.md#attributes)
- [Examples](influxdb_retention_policy_module.md#examples)

## [Synopsis](influxdb_retention_policy_module.md#id1)

- Manage InfluxDB retention policies.

Aliases: database.influxdb.influxdb_retention_policy

## [Requirements](influxdb_retention_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- influxdb >= 0.9
- requests

## [Parameters](influxdb_retention_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **database_name**  string / required | Name of the database. |
| **default**  boolean | Sets the retention policy as default retention policy.  **Choices:**   - `false` ← (default) - `true` |
| **duration**  string | Determines how long InfluxDB should keep the data. If specified, it should be `INF` or at least one hour. If not specified, `INF` is assumed. Supports complex duration expressions with multiple units.  Required only if `state` is set to `present`. |
| **hostname**  string | The hostname or IP address on which InfluxDB server is listening.  Since Ansible 2.5, defaulted to localhost.  **Default:** `"localhost"` |
| **password**  aliases: login_password  string | Password that will be used to authenticate against InfluxDB server.  Alias `login_password` added in Ansible 2.5.  **Default:** `"root"` |
| **path**  string  *added in community.general 0.2.0* | The path on which InfluxDB server is accessible  Only available when using python-influxdb >= 5.1.0  **Default:** `""` |
| **policy_name**  string / required | Name of the retention policy. |
| **port**  integer | The port on which InfluxDB server is listening  **Default:** `8086` |
| **proxies**  dictionary | HTTP(S) proxy to use for Requests to connect to InfluxDB server.  **Default:** `{}` |
| **replication**  integer | Determines how many independent copies of each point are stored in the cluster.  Required only if `state` is set to `present`. |
| **retries**  integer | Number of retries client will try before aborting.  `0` indicates try until success.  Only available when using python-influxdb >= 4.1.0  **Default:** `3` |
| **shard_group_duration**  string  *added in community.general 2.0.0* | Determines the time range covered by a shard group. If specified it must be at least one hour. If none, it’s determined by InfluxDB by the rentention policy’s duration. Supports complex duration expressions with multiple units. |
| **ssl**  boolean | Use https instead of http to connect to InfluxDB server.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string  *added in community.general 3.1.0* | State of the retention policy.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | Number of seconds Requests will wait for client to establish a connection. |
| **udp_port**  integer | UDP port to connect to InfluxDB server.  **Default:** `4444` |
| **use_udp**  boolean | Use UDP to connect to InfluxDB server.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: login_username  string | Username that will be used to authenticate against InfluxDB server.  Alias `login_username` added in Ansible 2.5.  **Default:** `"root"` |
| **validate_certs**  boolean | If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](influxdb_retention_policy_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](influxdb_retention_policy_module.md#id5)

```yaml+jinja
# Example influxdb_retention_policy command from Ansible Playbooks
- name: Create 1 hour retention policy
  community.general.influxdb_retention_policy:
      hostname: "{{ influxdb_ip_address }}"
      database_name: "{{ influxdb_database_name }}"
      policy_name: test
      duration: 1h
      replication: 1
      ssl: true
      validate_certs: true
      state: present

- name: Create 1 day retention policy with 1 hour shard group duration
  community.general.influxdb_retention_policy:
      hostname: "{{ influxdb_ip_address }}"
      database_name: "{{ influxdb_database_name }}"
      policy_name: test
      duration: 1d
      replication: 1
      shard_group_duration: 1h
      state: present

- name: Create 1 week retention policy with 1 day shard group duration
  community.general.influxdb_retention_policy:
      hostname: "{{ influxdb_ip_address }}"
      database_name: "{{ influxdb_database_name }}"
      policy_name: test
      duration: 1w
      replication: 1
      shard_group_duration: 1d
      state: present

- name: Create infinite retention policy with 1 week of shard group duration
  community.general.influxdb_retention_policy:
      hostname: "{{ influxdb_ip_address }}"
      database_name: "{{ influxdb_database_name }}"
      policy_name: test
      duration: INF
      replication: 1
      ssl: false
      validate_certs: false
      shard_group_duration: 1w
      state: present

- name: Create retention policy with complex durations
  community.general.influxdb_retention_policy:
      hostname: "{{ influxdb_ip_address }}"
      database_name: "{{ influxdb_database_name }}"
      policy_name: test
      duration: 5d1h30m
      replication: 1
      ssl: false
      validate_certs: false
      shard_group_duration: 1d10h30m
      state: present

- name: Drop retention policy
  community.general.influxdb_retention_policy:
      hostname: "{{ influxdb_ip_address }}"
      database_name: "{{ influxdb_database_name }}"
      policy_name: test
      state: absent
```

### Authors

- Kamil Szczygiel (@kamsz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

---
collection: ansible
version: "8"
title: "community.general.influxdb_query module – Query data points from InfluxDB"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/influxdb_query_module.html
fetched_at: 2026-07-28T01:46:29+00:00
---
# community.general.influxdb_query module – Query data points from InfluxDB

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
> see [Requirements](influxdb_query_module.md#ansible-collections-community-general-influxdb-query-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.influxdb_query`.

- [Synopsis](influxdb_query_module.md#synopsis)
- [Requirements](influxdb_query_module.md#requirements)
- [Parameters](influxdb_query_module.md#parameters)
- [Attributes](influxdb_query_module.md#attributes)
- [Examples](influxdb_query_module.md#examples)
- [Return Values](influxdb_query_module.md#return-values)

## [Synopsis](influxdb_query_module.md#id1)

- Query data points from InfluxDB.

Aliases: database.influxdb.influxdb_query

## [Requirements](influxdb_query_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- influxdb >= 0.9

## [Parameters](influxdb_query_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **database_name**  string / required | Name of the database. |
| **hostname**  string | The hostname or IP address on which InfluxDB server is listening.  Since Ansible 2.5, defaulted to localhost.  **Default:** `"localhost"` |
| **password**  aliases: login_password  string | Password that will be used to authenticate against InfluxDB server.  Alias `login_password` added in Ansible 2.5.  **Default:** `"root"` |
| **path**  string  *added in community.general 0.2.0* | The path on which InfluxDB server is accessible  Only available when using python-influxdb >= 5.1.0  **Default:** `""` |
| **port**  integer | The port on which InfluxDB server is listening  **Default:** `8086` |
| **proxies**  dictionary | HTTP(S) proxy to use for Requests to connect to InfluxDB server.  **Default:** `{}` |
| **query**  string / required | Query to be executed. |
| **retries**  integer | Number of retries client will try before aborting.  `0` indicates try until success.  Only available when using python-influxdb >= 4.1.0  **Default:** `3` |
| **ssl**  boolean | Use https instead of http to connect to InfluxDB server.  **Choices:**   - `false` ← (default) - `true` |
| **timeout**  integer | Number of seconds Requests will wait for client to establish a connection. |
| **udp_port**  integer | UDP port to connect to InfluxDB server.  **Default:** `4444` |
| **use_udp**  boolean | Use UDP to connect to InfluxDB server.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: login_username  string | Username that will be used to authenticate against InfluxDB server.  Alias `login_username` added in Ansible 2.5.  **Default:** `"root"` |
| **validate_certs**  boolean | If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](influxdb_query_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](influxdb_query_module.md#id5)

```yaml+jinja
- name: Query connections
  community.general.influxdb_query:
    hostname: "{{ influxdb_ip_address }}"
    database_name: "{{ influxdb_database_name }}"
    query: "select mean(value) from connections"
  register: connection

- name: Query connections with tags filters
  community.general.influxdb_query:
    hostname: "{{ influxdb_ip_address }}"
    database_name: "{{ influxdb_database_name }}"
    query: "select mean(value) from connections where region='zue01' and host='server01'"
  register: connection

- name: Print results from the query
  ansible.builtin.debug:
    var: connection.query_results
```

## [Return Values](influxdb_query_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **query_results**  list / elements=string | Result from the query  **Returned:** success  **Sample:** `[{"mean": 1245.5333333333333, "time": "1970-01-01T00:00:00Z"}]` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

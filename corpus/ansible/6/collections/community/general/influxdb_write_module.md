---
collection: ansible
version: "6"
title: "community.general.influxdb_write module – Write data points into InfluxDB"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/influxdb_write_module.html
fetched_at: 2026-07-27T17:09:47+00:00
---
# community.general.influxdb_write module – Write data points into InfluxDB

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
> see [Requirements](influxdb_write_module.md#ansible-collections-community-general-influxdb-write-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.influxdb_write`.

- [Synopsis](influxdb_write_module.md#synopsis)
- [Requirements](influxdb_write_module.md#requirements)
- [Parameters](influxdb_write_module.md#parameters)
- [Examples](influxdb_write_module.md#examples)

## [Synopsis](influxdb_write_module.md#id1)

- Write data points into InfluxDB.

## [Requirements](influxdb_write_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- influxdb >= 0.9

## [Parameters](influxdb_write_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **data_points**  list / elements=dictionary / required | Data points as dict to write into the database. |
| **database_name**  string / required | Name of the database. |
| **hostname**  string | The hostname or IP address on which InfluxDB server is listening.  Since Ansible 2.5, defaulted to localhost.  Default: `"localhost"` |
| **password**  aliases: login_password  string | Password that will be used to authenticate against InfluxDB server.  Alias `login_password` added in Ansible 2.5.  Default: `"root"` |
| **path**  string  added in community.general 0.2.0 | The path on which InfluxDB server is accessible  Only available when using python-influxdb >= 5.1.0  Default: `""` |
| **port**  integer | The port on which InfluxDB server is listening  Default: `8086` |
| **proxies**  dictionary | HTTP(S) proxy to use for Requests to connect to InfluxDB server.  Default: `{}` |
| **retries**  integer | Number of retries client will try before aborting.  `0` indicates try until success.  Only available when using python-influxdb >= 4.1.0  Default: `3` |
| **ssl**  boolean | Use https instead of http to connect to InfluxDB server.  Choices:   - `false` ← (default) - `true` |
| **timeout**  integer | Number of seconds Requests will wait for client to establish a connection. |
| **udp_port**  integer | UDP port to connect to InfluxDB server.  Default: `4444` |
| **use_udp**  boolean | Use UDP to connect to InfluxDB server.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: login_username  string | Username that will be used to authenticate against InfluxDB server.  Alias `login_username` added in Ansible 2.5.  Default: `"root"` |
| **validate_certs**  boolean | If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](influxdb_write_module.md#id4)

```yaml+jinja
- name: Write points into database
  community.general.influxdb_write:
      hostname: "{{influxdb_ip_address}}"
      database_name: "{{influxdb_database_name}}"
      data_points:
        - measurement: connections
          tags:
            host: server01
            region: us-west
          time: "{{ ansible_date_time.iso8601 }}"
          fields:
            value: 2000
        - measurement: connections
          tags:
            host: server02
            region: us-east
          time: "{{ ansible_date_time.iso8601 }}"
          fields:
            value: 3000
```

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

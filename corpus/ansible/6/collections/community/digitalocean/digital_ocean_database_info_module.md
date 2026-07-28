---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_database_info module – Gather information about DigitalOcean databases"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_database_info_module.html
fetched_at: 2026-07-27T17:06:38+00:00
---
# community.digitalocean.digital_ocean_database_info module – Gather information about DigitalOcean databases

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/community/digitalocean) (version 1.22.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_database_info`.

New in community.digitalocean 1.3.0

- [Synopsis](digital_ocean_database_info_module.md#synopsis)
- [Parameters](digital_ocean_database_info_module.md#parameters)
- [Examples](digital_ocean_database_info_module.md#examples)
- [Return Values](digital_ocean_database_info_module.md#return-values)

## [Synopsis](digital_ocean_database_info_module.md#id1)

- Gather information about DigitalOcean databases.

## [Parameters](digital_ocean_database_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **id**  aliases: database_id  integer | A unique ID that can be used to identify and reference a database cluster. |
| **name**  string | A unique, human-readable name for the database cluster. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](digital_ocean_database_info_module.md#id3)

```yaml+jinja
- name: Gather all DigitalOcean databases
  community.digitalocean.digital_ocean_database_info:
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_KEY') }}"
  register: my_databases
```

## [Return Values](digital_ocean_database_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  list / elements=string | List of DigitalOcean databases  Returned: success  Sample: `[{"connection": {"database": "", "host": "testdatabase1-do-user-3097135-0.b.db.ondigitalocean.com", "password": "REDACTED", "port": 25061, "protocol": "rediss", "ssl": true, "uri": "rediss://default:REDACTED@testdatabase1-do-user-3097135-0.b.db.ondigitalocean.com:25061", "user": "default"}, "created_at": "2021-04-21T15:41:14Z", "db_names": null, "engine": "redis", "id": "37de10e4-808b-4f4b-b25f-7b5b3fd194ac", "maintenance_window": {"day": "monday", "hour": "11:33:47", "pending": false}, "name": "testdatabase1", "num_nodes": 1, "private_connection": {"database": "", "host": "private-testdatabase1-do-user-3097135-0.b.db.ondigitalocean.com", "password": "REDACTED", "port": 25061, "protocol": "rediss", "ssl": true, "uri": "rediss://default:REDACTED@private-testdatabase1-do-user-3097135-0.b.db.ondigitalocean.com:25061", "user": "default"}, "private_network_uuid": "0db3519b-9efc-414a-8868-8f2e6934688c", "region": "nyc1", "size": "db-s-1vcpu-1gb", "status": "online", "tags": null, "users": null, "version": "6"}, "..."]` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)

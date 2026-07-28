---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_database module – Create and delete a DigitalOcean database"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_database_module.html
fetched_at: 2026-07-28T01:42:55+00:00
---
# community.digitalocean.digital_ocean_database module – Create and delete a DigitalOcean database

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/ui/repo/published/community/digitalocean/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_database`.

New in community.digitalocean 1.3.0

- [Synopsis](digital_ocean_database_module.md#synopsis)
- [Parameters](digital_ocean_database_module.md#parameters)
- [Examples](digital_ocean_database_module.md#examples)
- [Return Values](digital_ocean_database_module.md#return-values)

## [Synopsis](digital_ocean_database_module.md#id1)

- Create and delete a database in DigitalOcean and optionally wait for it to be online.
- DigitalOcean’s managed database service simplifies the creation and management of highly available database clusters.
- Currently, it offers support for PostgreSQL, Redis, MySQL, and MongoDB.

## [Parameters](digital_ocean_database_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  **Default:** `"https://api.digitalocean.com/v2"` |
| **engine**  string / required | A slug representing the database engine used for the cluster.  The possible values are `pg` for PostgreSQL, `mysql` for MySQL, `redis` for Redis, and `mongodb` for MongoDB.  **Choices:**   - `"pg"` - `"mysql"` - `"redis"` - `"mongodb"` |
| **id**  aliases: database_id  integer | A unique ID that can be used to identify and reference a database cluster. |
| **name**  string / required | A unique, human-readable name for the database cluster. |
| **num_nodes**  integer | The number of nodes in the database cluster.  Valid choices are 1, 2 or 3.  **Choices:**   - `1` ← (default) - `2` - `3` |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **private_network_uuid**  string | A string specifying the UUID of the VPC to which the database cluster is assigned. |
| **project_name**  aliases: project  string | Project to assign the resource to (project name, not UUID).  Defaults to the default project of the account (empty string).  Currently only supported when creating databases.  **Default:** `""` |
| **region**  aliases: region_id  string / required | The slug identifier for the region where the database cluster is located. |
| **size**  aliases: size_id  string / required | The slug identifier representing the size of the nodes in the database cluster.  See <https://docs.digitalocean.com/reference/api/api-reference/#operation/create_database_cluster> for supported sizes. |
| **state**  string | Indicates the desired state of the target.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | An array of tags that have been applied to the database cluster. |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  **Default:** `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **version**  string | A string representing the version of the database engine in use for the cluster.  For `pg`, versions are 10, 11 and 12.  For `mysql`, version is 8.  For `redis`, version is 5.  For `mongodb`, version is 4. |
| **wait**  boolean | Wait for the database to be online before returning.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long before wait gives up, in seconds, when creating a database.  **Default:** `600` |

## [Examples](digital_ocean_database_module.md#id3)

```yaml+jinja
- name: Create a Redis database
  community.digitalocean.digital_ocean_database:
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_KEY') }}"
    state: present
    name: testdatabase1
    engine: redis
    size: db-s-1vcpu-1gb
    region: nyc1
    num_nodes: 1
  register: my_database

- name: Create a Redis database (and assign to Project "test")
  community.digitalocean.digital_ocean_database:
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_KEY') }}"
    state: present
    name: testdatabase1
    engine: redis
    size: db-s-1vcpu-1gb
    region: nyc1
    num_nodes: 1
    project_name: test
  register: my_database
```

## [Return Values](digital_ocean_database_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **assign_status**  string | Assignment status (ok, not_found, assigned, already_assigned, service_down)  **Returned:** changed  **Sample:** `"assigned"` |
| **data**  dictionary | A DigitalOcean database  **Returned:** success  **Sample:** `{"database": {"connection": {"database": "", "host": "testdatabase1-do-user-3097135-0.b.db.ondigitalocean.com", "password": "REDACTED", "port": 25061, "protocol": "rediss", "ssl": true, "uri": "rediss://default:REDACTED@testdatabase1-do-user-3097135-0.b.db.ondigitalocean.com:25061", "user": "default"}, "created_at": "2021-04-21T15:41:14Z", "db_names": null, "engine": "redis", "id": "37de10e4-808b-4f4b-b25f-7b5b3fd194ac", "maintenance_window": {"day": "monday", "hour": 41627, "pending": false}, "name": "testdatabase1", "num_nodes": 1, "private_connection": {"database": "", "host": "private-testdatabase1-do-user-3097135-0.b.db.ondigitalocean.com", "password": "REDIS", "port": 25061, "protocol": "rediss", "ssl": true, "uri": "rediss://default:REDACTED@private-testdatabase1-do-user-3097135-0.b.db.ondigitalocean.com:25061", "user": "default"}, "private_network_uuid": "0db3519b-9efc-414a-8868-8f2e6934688c,", "region": "nyc1", "size": "db-s-1vcpu-1gb", "status": "online", "tags": null, "users": null, "version": 6}}` |
| **msg**  string | Informational or error message encountered during execution  **Returned:** changed  **Sample:** `"No project named test2 found"` |
| **resources**  dictionary | Resource assignment involved in project assignment  **Returned:** changed  **Sample:** `{"assigned_at": "2021-10-25T17:39:38Z", "links": {"self": "https://api.digitalocean.com/v2/databases/126355fa-b147-40a6-850a-c44f5d2ad418"}, "status": "assigned", "urn": "do:dbaas:126355fa-b147-40a6-850a-c44f5d2ad418"}` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)

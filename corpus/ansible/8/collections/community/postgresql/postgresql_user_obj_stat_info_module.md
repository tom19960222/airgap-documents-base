---
collection: ansible
version: "8"
title: "community.postgresql.postgresql_user_obj_stat_info module – Gather statistics about PostgreSQL user objects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/postgresql/postgresql_user_obj_stat_info_module.html
fetched_at: 2026-07-28T01:58:41+00:00
---
# community.postgresql.postgresql_user_obj_stat_info module – Gather statistics about PostgreSQL user objects

> **Note:**
>
> This module is part of the [community.postgresql collection](https://galaxy.ansible.com/ui/repo/published/community/postgresql/) (version 2.4.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.postgresql`.
> You need further requirements to be able to use this module,
> see [Requirements](postgresql_user_obj_stat_info_module.md#ansible-collections-community-postgresql-postgresql-user-obj-stat-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_user_obj_stat_info`.

New in community.postgresql 0.2.0

- [Synopsis](postgresql_user_obj_stat_info_module.md#synopsis)
- [Requirements](postgresql_user_obj_stat_info_module.md#requirements)
- [Parameters](postgresql_user_obj_stat_info_module.md#parameters)
- [Attributes](postgresql_user_obj_stat_info_module.md#attributes)
- [Notes](postgresql_user_obj_stat_info_module.md#notes)
- [See Also](postgresql_user_obj_stat_info_module.md#see-also)
- [Examples](postgresql_user_obj_stat_info_module.md#examples)
- [Return Values](postgresql_user_obj_stat_info_module.md#return-values)

## [Synopsis](postgresql_user_obj_stat_info_module.md#id1)

- Gathers statistics about PostgreSQL user objects.

## [Requirements](postgresql_user_obj_stat_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_user_obj_stat_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **connect_params**  dictionary  *added in community.postgresql 2.3.0* | Any additional parameters to be passed to libpg.  These parameters take precedence.  **Default:** `{}` |
| **db**  aliases: login_db  string | Name of database to connect. |
| **filter**  list / elements=string | Limit the collected information by comma separated string or YAML list.  Allowable values are `functions`, `indexes`, `tables`.  By default, collects all subsets.  Unsupported values are ignored. |
| **login_host**  aliases: host  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  **Default:** `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  **Default:** `""` |
| **login_unix_socket**  aliases: unix_socket  string | Path to a Unix domain socket for local connections.  **Default:** `""` |
| **login_user**  aliases: login  string | The username this module should use to establish its PostgreSQL session.  **Default:** `"postgres"` |
| **port**  aliases: login_port  integer | Database port to connect to.  **Default:** `5432` |
| **schema**  string | Restrict the output by certain schema. |
| **session_role**  string | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_cert**  path  *added in community.postgresql 2.4.0* | Specifies the file name of the client SSL certificate. |
| **ssl_key**  path  *added in community.postgresql 2.4.0* | Specifies the location for the secret key used for the client certificate. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  **Choices:**   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **trust_input**  boolean  *added in community.postgresql 0.2.0* | If `false`, check the value of *session_role* is potentially dangerous.  It makes sense to use `false` only when SQL injections via *session_role* are possible.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](postgresql_user_obj_stat_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](postgresql_user_obj_stat_info_module.md#id5)

> **Note:**
>
> - `size` and `total_size` returned values are presented in bytes.
> - For tracking function statistics the PostgreSQL `track_functions` parameter must be enabled. See <https://www.postgresql.org/docs/current/runtime-config-statistics.html> for more information.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses `psycopg2`, a Python PostgreSQL database adapter. You must ensure that `psycopg2` is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the `postgresql`, `libpq-dev`, and `python-psycopg2` packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_user_obj_stat_info_module.md#id6)

> **See also:**
>
> [community.postgresql.postgresql_info](postgresql_info_module.md#ansible-collections-community-postgresql-postgresql-info-module)
> :   Gather information about PostgreSQL servers.
>
> [community.postgresql.postgresql_ping](postgresql_ping_module.md#ansible-collections-community-postgresql-postgresql-ping-module)
> :   Check remote PostgreSQL server availability.
>
> [PostgreSQL statistics collector reference](https://www.postgresql.org/docs/current/monitoring-stats.html)
> :   Complete reference of the PostgreSQL statistics collector documentation.

## [Examples](postgresql_user_obj_stat_info_module.md#id7)

```yaml+jinja
- name: Collect information about all supported user objects of the acme database
  community.postgresql.postgresql_user_obj_stat_info:
    db: acme

- name: Collect information about all supported user objects in the custom schema of the acme database
  community.postgresql.postgresql_user_obj_stat_info:
    db: acme
    schema: custom

- name: Collect information about user tables and indexes in the acme database
  community.postgresql.postgresql_user_obj_stat_info:
    db: acme
    filter: tables, indexes
```

## [Return Values](postgresql_user_obj_stat_info_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **functions**  dictionary | User function statistics.  **Returned:** success  **Sample:** `{"public": {"inc": {"calls": 1, "funcid": 26722, "self_time": 0.23, "total_time": 0.23}}}` |
| **indexes**  dictionary | User index statistics.  **Returned:** success  **Sample:** `{"public": {"test_id_idx": {"...": null, "idx_scan": 0, "idx_tup_fetch": 0, "idx_tup_read": 0, "relname": "test", "size": 8192}}}` |
| **tables**  dictionary | User table statistics.  **Returned:** success  **Sample:** `{"public": {"test": {"...": null, "analyze_count": 3, "n_dead_tup": 0, "n_live_tup": 0, "seq_scan": 2, "size": 0, "total_size": 8192}}}` |

### Authors

- Andrew Klychkov (@Andersson007)
- Thomas O’Donnell (@andytom)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
- [Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
- [Communication](index.md#communication-for-community-postgresql)

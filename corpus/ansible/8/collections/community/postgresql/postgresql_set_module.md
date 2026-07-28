---
collection: ansible
version: "8"
title: "community.postgresql.postgresql_set module – Change a PostgreSQL server configuration parameter"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/postgresql/postgresql_set_module.html
fetched_at: 2026-07-28T01:58:36+00:00
---
# community.postgresql.postgresql_set module – Change a PostgreSQL server configuration parameter

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
> see [Requirements](postgresql_set_module.md#ansible-collections-community-postgresql-postgresql-set-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_set`.

- [Synopsis](postgresql_set_module.md#synopsis)
- [Requirements](postgresql_set_module.md#requirements)
- [Parameters](postgresql_set_module.md#parameters)
- [Attributes](postgresql_set_module.md#attributes)
- [Notes](postgresql_set_module.md#notes)
- [See Also](postgresql_set_module.md#see-also)
- [Examples](postgresql_set_module.md#examples)
- [Return Values](postgresql_set_module.md#return-values)

## [Synopsis](postgresql_set_module.md#id1)

- Allows to change a PostgreSQL server configuration parameter.
- The module uses ALTER SYSTEM command and applies changes by reload server configuration.
- ALTER SYSTEM is used for changing server configuration parameters across the entire database cluster.
- It can be more convenient and safe than the traditional method of manually editing the postgresql.conf file.
- ALTER SYSTEM writes the given parameter setting to the $PGDATA/postgresql.auto.conf file, which is read in addition to postgresql.conf.
- The module allows to reset parameter to boot_val (cluster initial value) by *reset=true* or remove parameter string from postgresql.auto.conf and reload *value=default* (for settings with postmaster context restart is required).
- After change you can see in the ansible output the previous and the new parameter value and other information using returned values and [ansible.builtin.debug](../../ansible/builtin/debug_module.md#ansible-collections-ansible-builtin-debug-module) module.

## [Requirements](postgresql_set_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_set_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **connect_params**  dictionary  *added in community.postgresql 2.3.0* | Any additional parameters to be passed to libpg.  These parameters take precedence.  **Default:** `{}` |
| **db**  aliases: login_db  string | Name of database to connect. |
| **login_host**  aliases: host  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  **Default:** `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  **Default:** `""` |
| **login_unix_socket**  aliases: unix_socket  string | Path to a Unix domain socket for local connections.  **Default:** `""` |
| **login_user**  aliases: login  string | The username this module should use to establish its PostgreSQL session.  **Default:** `"postgres"` |
| **name**  string / required | Name of PostgreSQL server parameter. Pay attention that parameters are case sensitive (see examples below). |
| **port**  aliases: login_port  integer | Database port to connect to.  **Default:** `5432` |
| **reset**  boolean | Restore parameter to initial state (boot_val). Mutually exclusive with *value*.  **Choices:**   - `false` ← (default) - `true` |
| **session_role**  string | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_cert**  path  *added in community.postgresql 2.4.0* | Specifies the file name of the client SSL certificate. |
| **ssl_key**  path  *added in community.postgresql 2.4.0* | Specifies the location for the secret key used for the client certificate. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  **Choices:**   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **trust_input**  boolean  *added in community.postgresql 0.2.0* | If `false`, check whether values of parameters are potentially dangerous.  It makes sense to use `false` only when SQL injections are possible.  **Choices:**   - `false` - `true` ← (default) |
| **value**  string | Parameter value to set.  To remove parameter string from postgresql.auto.conf and reload the server configuration you must pass *value=default*. With *value=default* the playbook always returns changed is true. |

## [Attributes](postgresql_set_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](postgresql_set_module.md#id5)

> **Note:**
>
> - Supported version of PostgreSQL is 9.4 and later.
> - Pay attention, change setting with ‘postmaster’ context can return changed is true when actually nothing changes because the same value may be presented in several different form, for example, 1024MB, 1GB, etc. However in pg_settings system view it can be defined like 131072 number of 8kB pages. The final check of the parameter value cannot compare it because the server was not restarted and the value in pg_settings is not updated yet.
> - For some parameters restart of PostgreSQL server is required. See official documentation <https://www.postgresql.org/docs/current/view-pg-settings.html>.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses `psycopg2`, a Python PostgreSQL database adapter. You must ensure that `psycopg2` is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the `postgresql`, `libpq-dev`, and `python-psycopg2` packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_set_module.md#id6)

> **See also:**
>
> [community.postgresql.postgresql_info](postgresql_info_module.md#ansible-collections-community-postgresql-postgresql-info-module)
> :   Gather information about PostgreSQL servers.
>
> [PostgreSQL server configuration](https://www.postgresql.org/docs/current/runtime-config.html)
> :   General information about PostgreSQL server configuration.
>
> [PostgreSQL view pg_settings reference](https://www.postgresql.org/docs/current/view-pg-settings.html)
> :   Complete reference of the pg_settings view documentation.
>
> [PostgreSQL ALTER SYSTEM command reference](https://www.postgresql.org/docs/current/sql-altersystem.html)
> :   Complete reference of the ALTER SYSTEM command documentation.

## [Examples](postgresql_set_module.md#id7)

```yaml+jinja
- name: Restore wal_keep_segments parameter to initial state
  community.postgresql.postgresql_set:
    name: wal_keep_segments
    reset: true

# Set work_mem parameter to 32MB and show what's been changed and restart is required or not
# (output example: "msg": "work_mem 4MB >> 64MB restart_req: False")
- name: Set work mem parameter
  community.postgresql.postgresql_set:
    name: work_mem
    value: 32mb
  register: set

- name: Print the result if the setting changed
  ansible.builtin.debug:
    msg: "{{ set.name }} {{ set.prev_val_pretty }} >> {{ set.value_pretty }} restart_req: {{ set.restart_required }}"
  when: set.changed
# Ensure that the restart of PostgreSQL server must be required for some parameters.
# In this situation you see the same parameter in prev_val_pretty and value_pretty, but 'changed=True'
# (If you passed the value that was different from the current server setting).

- name: Set log_min_duration_statement parameter to 1 second
  community.postgresql.postgresql_set:
    name: log_min_duration_statement
    value: 1s

- name: Set wal_log_hints parameter to default value (remove parameter from postgresql.auto.conf)
  community.postgresql.postgresql_set:
    name: wal_log_hints
    value: default

- name: Set TimeZone parameter (careful, case sensitive)
  community.postgresql.postgresql_set:
    name: TimeZone
    value: 'Europe/Paris'
```

## [Return Values](postgresql_set_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **context**  string | PostgreSQL setting context.  **Returned:** success  **Sample:** `"user"` |
| **name**  string | Name of PostgreSQL server parameter.  **Returned:** success  **Sample:** `"shared_buffers"` |
| **prev_val_pretty**  string | Information about previous state of the parameter.  **Returned:** success  **Sample:** `"4MB"` |
| **restart_required**  boolean | Information about parameter current state.  **Returned:** success  **Sample:** `true` |
| **value**  dictionary | Dictionary that contains the current parameter value (at the time of playbook finish).  Pay attention that for real change some parameters restart of PostgreSQL server is required.  Returns the current value in the check mode.  **Returned:** success  **Sample:** `{"unit": "b", "value": 67108864}` |
| **value_pretty**  string | Information about current state of the parameter.  **Returned:** success  **Sample:** `"64MB"` |

### Authors

- Andrew Klychkov (@Andersson007)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
- [Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
- [Communication](index.md#communication-for-community-postgresql)

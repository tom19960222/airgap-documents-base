---
collection: ansible
version: "8"
title: "community.postgresql.postgresql_tablespace module – Add or remove PostgreSQL tablespaces from remote hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/postgresql/postgresql_tablespace_module.html
fetched_at: 2026-07-28T01:58:39+00:00
---
# community.postgresql.postgresql_tablespace module – Add or remove PostgreSQL tablespaces from remote hosts

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
> see [Requirements](postgresql_tablespace_module.md#ansible-collections-community-postgresql-postgresql-tablespace-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_tablespace`.

- [Synopsis](postgresql_tablespace_module.md#synopsis)
- [Requirements](postgresql_tablespace_module.md#requirements)
- [Parameters](postgresql_tablespace_module.md#parameters)
- [Attributes](postgresql_tablespace_module.md#attributes)
- [Notes](postgresql_tablespace_module.md#notes)
- [See Also](postgresql_tablespace_module.md#see-also)
- [Examples](postgresql_tablespace_module.md#examples)
- [Return Values](postgresql_tablespace_module.md#return-values)

## [Synopsis](postgresql_tablespace_module.md#id1)

- Adds or removes PostgreSQL tablespaces from remote hosts.

## [Requirements](postgresql_tablespace_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_tablespace_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **connect_params**  dictionary  *added in community.postgresql 2.3.0* | Any additional parameters to be passed to libpg.  These parameters take precedence.  **Default:** `{}` |
| **db**  aliases: login_db  string | Name of database to connect to and run queries against. |
| **location**  aliases: path  path | Path to the tablespace directory in the file system.  Ensure that the location exists and has right privileges. |
| **login_host**  aliases: host  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  **Default:** `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  **Default:** `""` |
| **login_unix_socket**  aliases: unix_socket  string | Path to a Unix domain socket for local connections.  **Default:** `""` |
| **login_user**  aliases: login  string | The username this module should use to establish its PostgreSQL session.  **Default:** `"postgres"` |
| **owner**  string | Name of the role to set as an owner of the tablespace.  If this option is not specified, the tablespace owner is a role that creates the tablespace. |
| **port**  aliases: login_port  integer | Database port to connect to.  **Default:** `5432` |
| **rename_to**  string | New name of the tablespace.  The new name cannot begin with pg_, as such names are reserved for system tablespaces. |
| **session_role**  string | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **set**  dictionary | Dict of tablespace options to set. Supported from PostgreSQL 9.0.  For more information see <https://www.postgresql.org/docs/current/sql-createtablespace.html>.  When reset is passed as an option’s value, if the option was set previously, it will be removed. |
| **ssl_cert**  path  *added in community.postgresql 2.4.0* | Specifies the file name of the client SSL certificate. |
| **ssl_key**  path  *added in community.postgresql 2.4.0* | Specifies the location for the secret key used for the client certificate. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  **Choices:**   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | Tablespace state.  *state=present* implies the tablespace must be created if it doesn’t exist.  *state=absent* implies the tablespace must be removed if present. *state=absent* is mutually exclusive with *location*, *owner*, i(set).  See the Notes section for information about check mode restrictions.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tablespace**  aliases: name  string / required | Name of the tablespace to add or remove. |
| **trust_input**  boolean  *added in community.postgresql 0.2.0* | If `false`, check whether values of parameters *tablespace*, *location*, *owner*, *rename_to*, *session_role*, *settings_list* are potentially dangerous.  It makes sense to use `false` only when SQL injections via the parameters are possible.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](postgresql_tablespace_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **partial**  *state=absent* and *state=present* (the second one if the tablespace doesn’t exist) do not support check mode because the corresponding PostgreSQL DROP and CREATE TABLESPACE commands can not be run inside the transaction block. | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](postgresql_tablespace_module.md#id5)

> **Note:**
>
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses `psycopg2`, a Python PostgreSQL database adapter. You must ensure that `psycopg2` is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the `postgresql`, `libpq-dev`, and `python-psycopg2` packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_tablespace_module.md#id6)

> **See also:**
>
> [PostgreSQL tablespaces](https://www.postgresql.org/docs/current/manage-ag-tablespaces.html)
> :   General information about PostgreSQL tablespaces.
>
> [CREATE TABLESPACE reference](https://www.postgresql.org/docs/current/sql-createtablespace.html)
> :   Complete reference of the CREATE TABLESPACE command documentation.
>
> [ALTER TABLESPACE reference](https://www.postgresql.org/docs/current/sql-altertablespace.html)
> :   Complete reference of the ALTER TABLESPACE command documentation.
>
> [DROP TABLESPACE reference](https://www.postgresql.org/docs/current/sql-droptablespace.html)
> :   Complete reference of the DROP TABLESPACE command documentation.

## [Examples](postgresql_tablespace_module.md#id7)

```yaml+jinja
- name: Create a new tablespace called acme and set bob as an its owner
  community.postgresql.postgresql_tablespace:
    name: acme
    owner: bob
    location: /data/foo

- name: Create a new tablespace called bar with tablespace options
  community.postgresql.postgresql_tablespace:
    name: bar
    set:
      random_page_cost: 1
      seq_page_cost: 1

- name: Reset random_page_cost option
  community.postgresql.postgresql_tablespace:
    name: bar
    set:
      random_page_cost: reset

- name: Rename the tablespace from bar to pcie_ssd
  community.postgresql.postgresql_tablespace:
    name: bar
    rename_to: pcie_ssd

- name: Drop tablespace called bloat
  community.postgresql.postgresql_tablespace:
    name: bloat
    state: absent
```

## [Return Values](postgresql_tablespace_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **location**  string | Path to the tablespace in the file system.  **Returned:** v  **Sample:** `"/incredible/fast/ssd"` |
| **newname**  string | New tablespace name.  **Returned:** if existent  **Sample:** `"new_ssd"` |
| **options**  dictionary | Tablespace options.  **Returned:** success  **Sample:** `{"random_page_cost": 1, "seq_page_cost": 1}` |
| **owner**  string | Tablespace owner.  **Returned:** success  **Sample:** `"Bob"` |
| **queries**  string | List of queries that was tried to be executed.  **Returned:** success  **Sample:** `"[\"CREATE TABLESPACE bar LOCATION '/incredible/ssd'\"]"` |
| **state**  string | Tablespace state at the end of execution.  **Returned:** success  **Sample:** `"present"` |
| **tablespace**  string | Tablespace name.  **Returned:** success  **Sample:** `"ssd"` |

### Authors

- Flavien Chantelot (@Dorn-)
- Antoine Levy-Lambert (@antoinell)
- Andrew Klychkov (@Andersson007)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
- [Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
- [Communication](index.md#communication-for-community-postgresql)

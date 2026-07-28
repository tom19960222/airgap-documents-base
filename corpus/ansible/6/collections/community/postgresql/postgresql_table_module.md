---
collection: ansible
version: "6"
title: "community.postgresql.postgresql_table module – Create, drop, or modify a PostgreSQL table"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/postgresql/postgresql_table_module.html
fetched_at: 2026-07-27T17:20:30+00:00
---
# community.postgresql.postgresql_table module – Create, drop, or modify a PostgreSQL table

> **Note:**
>
> This module is part of the [community.postgresql collection](https://galaxy.ansible.com/community/postgresql) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.postgresql`.
> You need further requirements to be able to use this module,
> see [Requirements](postgresql_table_module.md#ansible-collections-community-postgresql-postgresql-table-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_table`.

- [Synopsis](postgresql_table_module.md#synopsis)
- [Requirements](postgresql_table_module.md#requirements)
- [Parameters](postgresql_table_module.md#parameters)
- [Notes](postgresql_table_module.md#notes)
- [See Also](postgresql_table_module.md#see-also)
- [Examples](postgresql_table_module.md#examples)
- [Return Values](postgresql_table_module.md#return-values)

## [Synopsis](postgresql_table_module.md#id1)

- Allows to create, drop, rename, truncate a table, or change some table attributes.

## [Requirements](postgresql_table_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_table_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **cascade**  boolean | Automatically drop objects that depend on the table (such as views). Used with *state=absent* only.  Choices:   - `false` ← (default) - `true` |
| **columns**  list / elements=string | Columns that are needed. |
| **connect_params**  dictionary  added in community.postgresql 2.3.0 | Any additional parameters to be passed to libpg.  These parameters take precedence.  Default: `{}` |
| **db**  aliases: login_db  string | Name of database to connect and where the table will be created.  Default: `""` |
| **including**  string | Keywords that are used with like parameter, may be DEFAULTS, CONSTRAINTS, INDEXES, STORAGE, COMMENTS or ALL. Needs *like* specified. Mutually exclusive with *columns*, *rename*, and *truncate*. |
| **like**  string | Create a table like another table (with similar DDL). Mutually exclusive with *columns*, *rename*, and *truncate*. |
| **login_host**  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  Default: `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  Default: `""` |
| **login_unix_socket**  string | Path to a Unix domain socket for local connections.  Default: `""` |
| **login_user**  string | The username this module should use to establish its PostgreSQL session.  Default: `"postgres"` |
| **owner**  string | Set a table owner. |
| **port**  aliases: login_port  integer | Database port to connect to.  Default: `5432` |
| **rename**  string | New table name. Mutually exclusive with *tablespace*, *owner*, *unlogged*, *like*, *including*, *columns*, *truncate*, and *storage_params*. |
| **session_role**  string | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  Choices:   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | The table state. *state=absent* is mutually exclusive with *tablespace*, *owner*, *unlogged*, *like*, *including*, *columns*, *truncate*, *storage_params* and, *rename*.  Choices:   - `"absent"` - `"present"` ← (default) |
| **storage_params**  list / elements=string | Storage parameters like fillfactor, autovacuum_vacuum_treshold, etc. Mutually exclusive with *rename* and *truncate*. |
| **table**  aliases: name  string / required | Table name. |
| **tablespace**  string | Set a tablespace for the table. |
| **truncate**  boolean | Truncate a table. Mutually exclusive with *tablespace*, *owner*, *unlogged*, *like*, *including*, *columns*, *rename*, and *storage_params*.  Choices:   - `false` ← (default) - `true` |
| **trust_input**  boolean  added in community.postgresql 0.2.0 | If `false`, check whether values of parameters are potentially dangerous.  It makes sense to use `false` only when SQL injections are possible.  Choices:   - `false` - `true` ← (default) |
| **unlogged**  boolean | Create an unlogged table.  Choices:   - `false` ← (default) - `true` |

## [Notes](postgresql_table_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.
> - If you do not pass db parameter, tables will be created in the database named postgres.
> - PostgreSQL allows to create columnless table, so columns param is optional.
> - Unlogged tables are available from PostgreSQL server version 9.1.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses psycopg2, a Python PostgreSQL database adapter. You must ensure that psycopg2 is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the postgresql, libpq-dev, and python-psycopg2 packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_table_module.md#id5)

> **See also:**
>
> [community.postgresql.postgresql_sequence](postgresql_sequence_module.md#ansible-collections-community-postgresql-postgresql-sequence-module)
> :   Create, drop, or alter a PostgreSQL sequence.
>
> [community.postgresql.postgresql_idx](postgresql_idx_module.md#ansible-collections-community-postgresql-postgresql-idx-module)
> :   Create or drop indexes from a PostgreSQL database.
>
> [community.postgresql.postgresql_info](postgresql_info_module.md#ansible-collections-community-postgresql-postgresql-info-module)
> :   Gather information about PostgreSQL servers.
>
> [community.postgresql.postgresql_tablespace](postgresql_tablespace_module.md#ansible-collections-community-postgresql-postgresql-tablespace-module)
> :   Add or remove PostgreSQL tablespaces from remote hosts.
>
> [community.postgresql.postgresql_owner](postgresql_owner_module.md#ansible-collections-community-postgresql-postgresql-owner-module)
> :   Change an owner of PostgreSQL database object.
>
> [community.postgresql.postgresql_privs](postgresql_privs_module.md#ansible-collections-community-postgresql-postgresql-privs-module)
> :   Grant or revoke privileges on PostgreSQL database objects.
>
> [community.postgresql.postgresql_copy](postgresql_copy_module.md#ansible-collections-community-postgresql-postgresql-copy-module)
> :   Copy data between a file/program and a PostgreSQL table.
>
> [CREATE TABLE reference](https://www.postgresql.org/docs/current/sql-createtable.html)
> :   Complete reference of the CREATE TABLE command documentation.
>
> [ALTER TABLE reference](https://www.postgresql.org/docs/current/sql-altertable.html)
> :   Complete reference of the ALTER TABLE command documentation.
>
> [DROP TABLE reference](https://www.postgresql.org/docs/current/sql-droptable.html)
> :   Complete reference of the DROP TABLE command documentation.
>
> [PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html)
> :   Complete reference of the PostgreSQL data types documentation.

## [Examples](postgresql_table_module.md#id6)

```yaml+jinja
- name: Create tbl2 in the acme database with the DDL like tbl1 with testuser as an owner
  community.postgresql.postgresql_table:
    db: acme
    name: tbl2
    like: tbl1
    owner: testuser

- name: Create tbl2 in the acme database and tablespace ssd with the DDL like tbl1 including comments and indexes
  community.postgresql.postgresql_table:
    db: acme
    table: tbl2
    like: tbl1
    including: comments, indexes
    tablespace: ssd

- name: Create test_table with several columns in ssd tablespace with fillfactor=10 and autovacuum_analyze_threshold=1
  community.postgresql.postgresql_table:
    name: test_table
    columns:
    - id bigserial primary key
    - num bigint
    - stories text
    tablespace: ssd
    storage_params:
    - fillfactor=10
    - autovacuum_analyze_threshold=1

- name: Create an unlogged table in schema acme
  community.postgresql.postgresql_table:
    name: acme.useless_data
    columns: waste_id int
    unlogged: true

- name: Rename table foo to bar
  community.postgresql.postgresql_table:
    table: foo
    rename: bar

- name: Rename table foo from schema acme to bar
  community.postgresql.postgresql_table:
    name: acme.foo
    rename: bar

- name: Set owner to someuser
  community.postgresql.postgresql_table:
    name: foo
    owner: someuser

- name: Change tablespace of foo table to new_tablespace and set owner to new_user
  community.postgresql.postgresql_table:
    name: foo
    tablespace: new_tablespace
    owner: new_user

- name: Truncate table foo
  community.postgresql.postgresql_table:
    name: foo
    truncate: true

- name: Drop table foo from schema acme
  community.postgresql.postgresql_table:
    name: acme.foo
    state: absent

- name: Drop table bar cascade
  community.postgresql.postgresql_table:
    name: bar
    state: absent
    cascade: true
```

## [Return Values](postgresql_table_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **owner**  string | Table owner.  Returned: always  Sample: `"postgres"` |
| **queries**  string | List of executed queries.  Returned: always  Sample: `"['CREATE TABLE \"test_table\" (id bigint)']"` |
| **state**  string | Table state.  Returned: always  Sample: `"present"` |
| **storage_params**  list / elements=string | Storage parameters.  Returned: always  Sample: `["fillfactor=100", "autovacuum_analyze_threshold=1"]` |
| **table**  string | Name of a table.  Returned: always  Sample: `"foo"` |
| **tablespace**  string | Tablespace.  Returned: always  Sample: `"ssd_tablespace"` |

### Authors

- Andrei Klychkov (@Andersson007)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
[Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
[Communication](index.md#communication-for-community-postgresql)

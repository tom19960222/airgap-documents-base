---
collection: ansible
version: "6"
title: "community.postgresql.postgresql_db module – Add or remove PostgreSQL databases from a remote host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/postgresql/postgresql_db_module.html
fetched_at: 2026-07-27T17:20:17+00:00
---
# community.postgresql.postgresql_db module – Add or remove PostgreSQL databases from a remote host

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
> see [Requirements](postgresql_db_module.md#ansible-collections-community-postgresql-postgresql-db-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_db`.

- [Synopsis](postgresql_db_module.md#synopsis)
- [Requirements](postgresql_db_module.md#requirements)
- [Parameters](postgresql_db_module.md#parameters)
- [Notes](postgresql_db_module.md#notes)
- [See Also](postgresql_db_module.md#see-also)
- [Examples](postgresql_db_module.md#examples)
- [Return Values](postgresql_db_module.md#return-values)

## [Synopsis](postgresql_db_module.md#id1)

- Add or remove PostgreSQL databases from a remote host.

## [Requirements](postgresql_db_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_db_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **conn_limit**  string | Specifies the database connection limit.  Default: `""` |
| **connect_params**  dictionary  added in community.postgresql 2.3.0 | Any additional parameters to be passed to libpg.  These parameters take precedence.  Default: `{}` |
| **dump_extra_args**  string  added in community.postgresql 0.2.0 | Provides additional arguments when *state* is `dump`.  Cannot be used with dump-file-format-related arguments like ``–format=d``. |
| **encoding**  string | Encoding of the database.  Default: `""` |
| **force**  boolean | Used to forcefully drop a database when the *state* is `absent`, ignored otherwise.  Choices:   - `false` ← (default) - `true` |
| **lc_collate**  string | Collation order (LC_COLLATE) to use in the database must match collation order of template database unless `template0` is used as template.  Default: `""` |
| **lc_ctype**  string | Character classification (LC_CTYPE) to use in the database (e.g. lower, upper, …).  Must match LC_CTYPE of template database unless `template0` is used as template.  Default: `""` |
| **login_host**  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  Default: `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  Default: `""` |
| **login_unix_socket**  string | Path to a Unix domain socket for local connections.  Default: `""` |
| **login_user**  string | The username this module should use to establish its PostgreSQL session.  Default: `"postgres"` |
| **maintenance_db**  string | The value specifies the initial database (which is also called as maintenance DB) that Ansible connects to.  Default: `"postgres"` |
| **name**  aliases: db  string / required | Name of the database to add or remove. |
| **owner**  string | Name of the role to set as owner of the database.  Default: `""` |
| **port**  aliases: login_port  integer | Database port to connect (if needed).  Default: `5432` |
| **session_role**  string | Switch to session_role after connecting.  The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  Choices:   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | The database state.  `present` implies that the database should be created if necessary.  `absent` implies that the database should be removed if present.  `dump` requires a target definition to which the database will be backed up. (Added in Ansible 2.4) Note that in some PostgreSQL versions of pg_dump, which is an embedded PostgreSQL utility and is used by the module, returns rc 0 even when errors occurred (e.g. the connection is forbidden by pg_hba.conf, etc.), so the module returns changed=True but the dump has not actually been done. Please, be sure that your version of pg_dump returns rc 1 in this case.  `restore` also requires a target definition from which the database will be restored. (Added in Ansible 2.4).  The format of the backup will be detected based on the target name.  Supported compression formats for dump and restore include `.pgc`, `.bz2`, `.gz` and `.xz`.  Supported formats for dump and restore include `.sql`, `.tar`, and `.dir` (for the directory format which is supported since collection version 1.4.0).  Restore program is selected by target file format: `.tar`, `.pgc`, and `.dir` are handled by pg_restore, other with pgsql.  .  `rename` is used to rename the database `name` to `target`.  If the database `name` exists, it will be renamed to `target`.  If the database `name` does not exist and the `target` database exists, the module will report that nothing has changed.  If both the databases exist as well as when they have the same value, an error will be raised.  When *state=rename*, in addition to the `name` option, the module requires the `target` option. Other options are ignored. Supported since collection version 1.4.0.  Choices:   - `"absent"` - `"dump"` - `"present"` ← (default) - `"rename"` - `"restore"` |
| **tablespace**  path | The tablespace to set for the database <https://www.postgresql.org/docs/current/sql-alterdatabase.html>.  If you want to move the database back to the default tablespace, explicitly set this to pg_default.  Default: `""` |
| **target**  path | File to back up or restore from.  Used when *state* is `dump` or `restore`.  Default: `""` |
| **target_opts**  string | Additional arguments for pg_dump or restore program (pg_restore or psql, depending on target’s format).  Used when *state* is `dump` or `restore`.  Default: `""` |
| **template**  string | Template used to create the database.  Default: `""` |
| **trust_input**  boolean  added in community.postgresql 0.2.0 | If `false`, check whether values of parameters *owner*, *conn_limit*, *encoding*, *db*, *template*, *tablespace*, *session_role* are potentially dangerous.  It makes sense to use `false` only when SQL injections via the parameters are possible.  Choices:   - `false` - `true` ← (default) |

## [Notes](postgresql_db_module.md#id4)

> **Note:**
>
> - State `dump` and `restore` don’t require *psycopg2* since version 2.8.
> - Supports `check_mode`.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses psycopg2, a Python PostgreSQL database adapter. You must ensure that psycopg2 is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the postgresql, libpq-dev, and python-psycopg2 packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_db_module.md#id5)

> **See also:**
>
> [CREATE DATABASE reference](https://www.postgresql.org/docs/current/sql-createdatabase.html)
> :   Complete reference of the CREATE DATABASE command documentation.
>
> [DROP DATABASE reference](https://www.postgresql.org/docs/current/sql-dropdatabase.html)
> :   Complete reference of the DROP DATABASE command documentation.
>
> [pg_dump reference](https://www.postgresql.org/docs/current/app-pgdump.html)
> :   Complete reference of pg_dump documentation.
>
> [pg_restore reference](https://www.postgresql.org/docs/current/app-pgrestore.html)
> :   Complete reference of pg_restore documentation.
>
> [community.postgresql.postgresql_tablespace](postgresql_tablespace_module.md#ansible-collections-community-postgresql-postgresql-tablespace-module)
> :   Add or remove PostgreSQL tablespaces from remote hosts.
>
> [community.postgresql.postgresql_info](postgresql_info_module.md#ansible-collections-community-postgresql-postgresql-info-module)
> :   Gather information about PostgreSQL servers.
>
> [community.postgresql.postgresql_ping](postgresql_ping_module.md#ansible-collections-community-postgresql-postgresql-ping-module)
> :   Check remote PostgreSQL server availability.

## [Examples](postgresql_db_module.md#id6)

```yaml+jinja
- name: Create a new database with name "acme"
  community.postgresql.postgresql_db:
    name: acme

# Note: If a template different from "template0" is specified,
# encoding and locale settings must match those of the template.
- name: Create a new database with name "acme" and specific encoding and locale # settings
  community.postgresql.postgresql_db:
    name: acme
    encoding: UTF-8
    lc_collate: de_DE.UTF-8
    lc_ctype: de_DE.UTF-8
    template: template0

# Note: Default limit for the number of concurrent connections to
# a specific database is "-1", which means "unlimited"
- name: Create a new database with name "acme" which has a limit of 100 concurrent connections
  community.postgresql.postgresql_db:
    name: acme
    conn_limit: "100"

- name: Dump an existing database to a file
  community.postgresql.postgresql_db:
    name: acme
    state: dump
    target: /tmp/acme.sql

- name: Dump an existing database to a file excluding the test table
  community.postgresql.postgresql_db:
    name: acme
    state: dump
    target: /tmp/acme.sql
    dump_extra_args: --exclude-table=test

- name: Dump an existing database to a file (with compression)
  community.postgresql.postgresql_db:
    name: acme
    state: dump
    target: /tmp/acme.sql.gz

- name: Dump a single schema for an existing database
  community.postgresql.postgresql_db:
    name: acme
    state: dump
    target: /tmp/acme.sql
    target_opts: "-n public"

- name: Dump only table1 and table2 from the acme database
  community.postgresql.postgresql_db:
    name: acme
    state: dump
    target: /tmp/table1_table2.sql
    target_opts: "-t table1 -t table2"

- name: Dump an existing database using the directory format
  community.postgresql.postgresql_db:
    name: acme
    state: dump
    target: /tmp/acme.dir

# Note: In the example below, if database foo exists and has another tablespace
# the tablespace will be changed to foo. Access to the database will be locked
# until the copying of database files is finished.
- name: Create a new database called foo in tablespace bar
  community.postgresql.postgresql_db:
    name: foo
    tablespace: bar

# Rename the database foo to bar.
# If the database foo exists, it will be renamed to bar.
# If the database foo does not exist and the bar database exists,
# the module will report that nothing has changed.
# If both the databases exist, an error will be raised.
- name: Rename the database foo to bar
  community.postgresql.postgresql_db:
    name: foo
    state: rename
    target: bar
```

## [Return Values](postgresql_db_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **executed_commands**  list / elements=string  added in community.postgresql 0.2.0 | List of commands which tried to run.  Returned: always  Sample: `["CREATE DATABASE acme"]` |

### Authors

- Ansible Core Team

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
[Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
[Communication](index.md#communication-for-community-postgresql)

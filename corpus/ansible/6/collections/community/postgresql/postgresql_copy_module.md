---
collection: ansible
version: "6"
title: "community.postgresql.postgresql_copy module – Copy data between a file/program and a PostgreSQL table"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/postgresql/postgresql_copy_module.html
fetched_at: 2026-07-27T17:20:16+00:00
---
# community.postgresql.postgresql_copy module – Copy data between a file/program and a PostgreSQL table

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
> see [Requirements](postgresql_copy_module.md#ansible-collections-community-postgresql-postgresql-copy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_copy`.

- [Synopsis](postgresql_copy_module.md#synopsis)
- [Requirements](postgresql_copy_module.md#requirements)
- [Parameters](postgresql_copy_module.md#parameters)
- [Notes](postgresql_copy_module.md#notes)
- [See Also](postgresql_copy_module.md#see-also)
- [Examples](postgresql_copy_module.md#examples)
- [Return Values](postgresql_copy_module.md#return-values)

## [Synopsis](postgresql_copy_module.md#id1)

- Copy data between a file/program and a PostgreSQL table.

## [Requirements](postgresql_copy_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_copy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **columns**  aliases: column  list / elements=string | List of column names for the src/dst table to COPY FROM/TO. |
| **connect_params**  dictionary  added in community.postgresql 2.3.0 | Any additional parameters to be passed to libpg.  These parameters take precedence.  Default: `{}` |
| **copy_from**  aliases: from  path | Copy data from a file to a table (appending the data to whatever is in the table already).  Mutually exclusive with *copy_to* and *src*. |
| **copy_to**  aliases: to  path | Copy the contents of a table to a file.  Can also copy the results of a SELECT query.  Mutually exclusive with *copy_from* and *dst*. |
| **db**  aliases: login_db  string | Name of database to connect to. |
| **dst**  aliases: destination  string | Copy data to *dst=tablename* from *copy_from=/path/to/data.file*.  Used with *copy_from* only. |
| **login_host**  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  Default: `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  Default: `""` |
| **login_unix_socket**  string | Path to a Unix domain socket for local connections.  Default: `""` |
| **login_user**  string | The username this module should use to establish its PostgreSQL session.  Default: `"postgres"` |
| **options**  dictionary | Options of COPY command.  See the full list of available options <https://www.postgresql.org/docs/current/sql-copy.html>. |
| **port**  aliases: login_port  integer | Database port to connect to.  Default: `5432` |
| **program**  boolean | Mark *src*/*dst* as a program. Data will be copied to/from a program.  See block Examples and PROGRAM arg description <https://www.postgresql.org/docs/current/sql-copy.html>.  Choices:   - `false` ← (default) - `true` |
| **session_role**  string | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **src**  aliases: source  string | Copy data from *copy_from* to *src=tablename*.  Used with *copy_to* only. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  Choices:   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **trust_input**  boolean  added in community.postgresql 0.2.0 | If `false`, check whether values of parameters are potentially dangerous.  It makes sense to use `false` only when SQL injections are possible.  Choices:   - `false` - `true` ← (default) |

## [Notes](postgresql_copy_module.md#id4)

> **Note:**
>
> - Supports PostgreSQL version 9.4+.
> - COPY command is only allowed to database superusers.
> - If *check_mode=true*, we just check the src/dst table availability and return the COPY query that actually has not been executed.
> - If i(check_mode=true) and the source has been passed as SQL, the module will execute it and rolled the transaction back but pay attention it can affect database performance (e.g., if SQL collects a lot of data).
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses psycopg2, a Python PostgreSQL database adapter. You must ensure that psycopg2 is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the postgresql, libpq-dev, and python-psycopg2 packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_copy_module.md#id5)

> **See also:**
>
> [COPY command reference](https://www.postgresql.org/docs/current/sql-copy.html)
> :   Complete reference of the COPY command documentation.

## [Examples](postgresql_copy_module.md#id6)

```yaml+jinja
- name: Copy text TAB-separated data from file /tmp/data.txt to acme table
  community.postgresql.postgresql_copy:
    copy_from: /tmp/data.txt
    dst: acme

- name: Copy CSV (comma-separated) data from file /tmp/data.csv to columns id, name of table acme
  community.postgresql.postgresql_copy:
    copy_from: /tmp/data.csv
    dst: acme
    columns: id,name
    options:
      format: csv

- name: >
    Copy text vertical-bar-separated data from file /tmp/data.txt to bar table.
    The NULL values are specified as N
  community.postgresql.postgresql_copy:
    copy_from: /tmp/data.csv
    dst: bar
    options:
      delimiter: '|'
      null: 'N'

- name: Copy data from acme table to file /tmp/data.txt in text format, TAB-separated
  community.postgresql.postgresql_copy:
    src: acme
    copy_to: /tmp/data.txt

- name: Copy data from SELECT query to/tmp/data.csv in CSV format
  community.postgresql.postgresql_copy:
    src: 'SELECT * FROM acme'
    copy_to: /tmp/data.csv
    options:
      format: csv

- name: Copy CSV data from my_table to gzip
  community.postgresql.postgresql_copy:
    src: my_table
    copy_to: 'gzip > /tmp/data.csv.gz'
    program: true
    options:
      format: csv

- name: >
    Copy data from columns id, name of table bar to /tmp/data.txt.
    Output format is text, vertical-bar-separated, NULL as N
  community.postgresql.postgresql_copy:
    src: bar
    columns:
    - id
    - name
    copy_to: /tmp/data.csv
    options:
      delimiter: '|'
      null: 'N'
```

## [Return Values](postgresql_copy_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dst**  string | Data destination.  Returned: always  Sample: `"/tmp/data.csv"` |
| **queries**  string | List of executed queries.  Returned: always  Sample: `"[\"COPY test_table FROM '/tmp/data_file.txt' (FORMAT csv, DELIMITER ',', NULL 'NULL')\"]"` |
| **src**  string | Data source.  Returned: always  Sample: `"mytable"` |

### Authors

- Andrew Klychkov (@Andersson007)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
[Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
[Communication](index.md#communication-for-community-postgresql)

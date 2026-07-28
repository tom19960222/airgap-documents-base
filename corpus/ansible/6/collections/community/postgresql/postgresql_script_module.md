---
collection: ansible
version: "6"
title: "community.postgresql.postgresql_script module – Run PostgreSQL statements from a file"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/postgresql/postgresql_script_module.html
fetched_at: 2026-07-27T17:20:26+00:00
---
# community.postgresql.postgresql_script module – Run PostgreSQL statements from a file

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
> see [Requirements](postgresql_script_module.md#ansible-collections-community-postgresql-postgresql-script-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_script`.

New in community.postgresql 2.1.0

- [Synopsis](postgresql_script_module.md#synopsis)
- [Requirements](postgresql_script_module.md#requirements)
- [Parameters](postgresql_script_module.md#parameters)
- [Notes](postgresql_script_module.md#notes)
- [See Also](postgresql_script_module.md#see-also)
- [Examples](postgresql_script_module.md#examples)
- [Return Values](postgresql_script_module.md#return-values)

## [Synopsis](postgresql_script_module.md#id1)

- Runs arbitrary PostgreSQL statements from a file.
- The module always reports that the state has changed.
- Does not run against backup files. Use [community.postgresql.postgresql_db](postgresql_db_module.md#ansible-collections-community-postgresql-postgresql-db-module) with *state=restore* to run queries on files made by pg_dump/pg_dumpall utilities.

## [Requirements](postgresql_script_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_script_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **connect_params**  dictionary  added in community.postgresql 2.3.0 | Any additional parameters to be passed to libpg.  These parameters take precedence.  Default: `{}` |
| **db**  aliases: login_db  string | Name of database to connect to and run queries against. |
| **encoding**  string | Set the client encoding for the current session (e.g. `UTF-8`).  The default is the encoding defined by the database. |
| **login_host**  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  Default: `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  Default: `""` |
| **login_unix_socket**  string | Path to a Unix domain socket for local connections.  Default: `""` |
| **login_user**  string | The username this module should use to establish its PostgreSQL session.  Default: `"postgres"` |
| **named_args**  dictionary | Dictionary of key-value arguments to substitute variable placeholders within the file content.  When the value is a list, it will be converted to PostgreSQL array.  Mutually exclusive with *positional_args*. |
| **path**  path | Path to a SQL script on the target machine.  To upload dumps, the preferable way is to use the [community.postgresql.postgresql_db](postgresql_db_module.md#ansible-collections-community-postgresql-postgresql-db-module) module with *state=restore*. |
| **port**  aliases: login_port  integer | Database port to connect to.  Default: `5432` |
| **positional_args**  list / elements=any | List of values to substitute variable placeholders within the file content.  When the value is a list, it will be converted to PostgreSQL array.  Mutually exclusive with *named_args*. |
| **search_path**  list / elements=string | Overrides the list of schemas to search for db objects in. |
| **session_role**  string | Switch to `session_role` after connecting. The specified role must be a role that the current `login_user` is a member of.  Permissions checking for SQL commands is carried out as though the `session_role` were the one that had logged in originally. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  Choices:   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **trust_input**  boolean | If `false`, check whether a value of *session_role* is potentially dangerous.  It makes sense to use `false` only when SQL injections via *session_role* are possible.  Choices:   - `false` - `true` ← (default) |

## [Notes](postgresql_script_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses psycopg2, a Python PostgreSQL database adapter. You must ensure that psycopg2 is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the postgresql, libpq-dev, and python-psycopg2 packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_script_module.md#id5)

> **See also:**
>
> [community.postgresql.postgresql_db](postgresql_db_module.md#ansible-collections-community-postgresql-postgresql-db-module)
> :   Add or remove PostgreSQL databases from a remote host.
>
> [community.postgresql.postgresql_query](postgresql_query_module.md#ansible-collections-community-postgresql-postgresql-query-module)
> :   Run PostgreSQL queries.
>
> [PostgreSQL Schema reference](https://www.postgresql.org/docs/current/ddl-schemas.html)
> :   Complete reference of the PostgreSQL schema documentation.

## [Examples](postgresql_script_module.md#id6)

```yaml+jinja
# Assuming that the file contains
# SELECT * FROM id_talbe WHERE id = %s,
# '%s' will be substituted with 1
- name: Run query from SQL script using UTF-8 client encoding for session and positional args
  community.postgresql.postgresql_script:
    db: test_db
    path: /var/lib/pgsql/test.sql
    positional_args:
      - 1
    encoding: UTF-8

# Assuming that the file contains
# SELECT * FROM test WHERE id = %(id_val)s AND story = %(story_val)s,
# %-values will be substituted with 1 and 'test'
- name: Select query to test_db with named_args
  community.postgresql.postgresql_script:
    db: test_db
    path: /var/lib/pgsql/test.sql
    named_args:
      id_val: 1
      story_val: test

- block:
  # Assuming that the the file contains
  # SELECT * FROM test_array_table WHERE arr_col1 = %s AND arr_col2 = %s
  # Pass list and string vars as positional_args
  - name: Set vars
    ansible.builtin.set_fact:
      my_list:
      - 1
      - 2
      - 3
      my_arr: '{1, 2, 3}'
  - name: Passing positional_args as arrays
    community.postgresql.postgresql_script:
      path: /var/lib/pgsql/test.sql
      positional_args:
        - '{{ my_list }}'
        - '{{ my_arr|string }}'

# Assuming that the the file contains
# SELECT * FROM test_table,
# look into app1 schema first, then,
# if the schema doesn't exist or the table hasn't been found there,
# try to find it in the schema public
- name: Select from test using search_path
  community.postgresql.postgresql_script:
    path: /var/lib/pgsql/test.sql
    search_path:
    - app1
    - public

- block:
    # If you use a variable in positional_args/named_args that can
    # be undefined and you wish to set it as NULL, constructions like
    # "{{ my_var if (my_var is defined) else none | default(none) }}"
    # will not work as expected substituting an empty string instead of NULL.
    # If possible, we suggest using Ansible's DEFAULT_JINJA2_NATIVE configuration
    # (https://docs.ansible.com/ansible/latest/reference_appendices/config.html#default-jinja2-native).
    # Enabling it fixes this problem. If you cannot enable it, the following workaround
    # can be used.
    # You should precheck such a value and define it as NULL when undefined.
    # For example:
    - name: When undefined, set to NULL
      set_fact:
        my_var: NULL
      when: my_var is undefined

    # Then, assuming that the file contains
    # INSERT INTO test_table (col1) VALUES (%s)
    - name: Insert a value using positional arguments
      community.postgresql.postgresql_script:
        path: /var/lib/pgsql/test.sql
        positional_args:
          - '{{ my_var }}'
```

## [Return Values](postgresql_script_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **query**  string | Executed query.  When the `positional_args` or `named_args` options are used, the query contains all variables that were substituted inside the database connector.  Returned: always  Sample: `"SELECT * FROM bar"` |
| **query_result**  list / elements=dictionary | List of dictionaries in the column:value form representing returned rows.  When there are several statements in the script, returns result of the last statement.  Returned: always  Sample: `[{"Column": "Value1"}, {"Column": "Value2"}]` |
| **rowcount**  integer | Number of produced or affected rows.  When there are several statements in the script, returns a number of rows affected by the last statement.  Returned: changed  Sample: `5` |
| **statusmessage**  string | Attribute containing the message returned by the database connector after executing the script content.  When there are several statements in the script, returns a message related to the last statement.  Returned: always  Sample: `"INSERT 0 1"` |

### Authors

- Douglas J Hunley (@hunleyd)
- 1. Hart (@jtelcontar)
- Daniel Scharon (@DanScharon)
- Andrew Klychkov (@Andersson007)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
[Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
[Communication](index.md#communication-for-community-postgresql)

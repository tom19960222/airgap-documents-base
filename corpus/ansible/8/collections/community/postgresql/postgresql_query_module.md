---
collection: ansible
version: "8"
title: "community.postgresql.postgresql_query module – Run PostgreSQL queries"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/postgresql/postgresql_query_module.html
fetched_at: 2026-07-28T01:58:33+00:00
---
# community.postgresql.postgresql_query module – Run PostgreSQL queries

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
> see [Requirements](postgresql_query_module.md#ansible-collections-community-postgresql-postgresql-query-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_query`.

- [Synopsis](postgresql_query_module.md#synopsis)
- [Requirements](postgresql_query_module.md#requirements)
- [Parameters](postgresql_query_module.md#parameters)
- [Attributes](postgresql_query_module.md#attributes)
- [Notes](postgresql_query_module.md#notes)
- [See Also](postgresql_query_module.md#see-also)
- [Examples](postgresql_query_module.md#examples)
- [Return Values](postgresql_query_module.md#return-values)

## [Synopsis](postgresql_query_module.md#id1)

- Runs arbitrary PostgreSQL queries.
- **WARNING** The `path_to_script` and `as_single_query` options as well as the `query_list` and `query_all_results` return values have been **deprecated** and will be removed in community.postgresql 3.0.0, please use the [community.postgresql.postgresql_script](postgresql_script_module.md#ansible-collections-community-postgresql-postgresql-script-module) module to execute statements from scripts.
- Does not run against backup files. Use [community.postgresql.postgresql_db](postgresql_db_module.md#ansible-collections-community-postgresql-postgresql-db-module) with *state=restore* to run queries on files made by pg_dump/pg_dumpall utilities.

## [Requirements](postgresql_query_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_query_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **as_single_query**  boolean  *added in community.postgresql 1.1.0* | This option has been **deprecated** and will be removed in community.postgresql 3.0.0, please use the [community.postgresql.postgresql_script](postgresql_script_module.md#ansible-collections-community-postgresql-postgresql-script-module) module to execute statements from scripts.  If `true`, when reading from the *path_to_script* file, executes its whole content in a single query (not splitting it up into separate queries by semicolons). It brings the following changes in the module’s behavior.  When `true`, the `query_all_results` return value contains only the result of the last statement.  Whether the state is reported as changed or not is determined by the last statement of the file.  Used only when *path_to_script* is specified, otherwise ignored.  If set to `false`, the script can contain only semicolon-separated queries. (see the *path_to_script* option documentation).  **Choices:**   - `false` - `true` ← (default) |
| **autocommit**  boolean | Execute in autocommit mode when the query can’t be run inside a transaction block (e.g., VACUUM).  Mutually exclusive with *check_mode*.  **Choices:**   - `false` ← (default) - `true` |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **connect_params**  dictionary  *added in community.postgresql 2.3.0* | Any additional parameters to be passed to libpg.  These parameters take precedence.  **Default:** `{}` |
| **db**  aliases: login_db  string | Name of database to connect to and run queries against. |
| **encoding**  string  *added in community.postgresql 0.2.0* | Set the client encoding for the current session (e.g. `UTF-8`).  The default is the encoding defined by the database. |
| **login_host**  aliases: host  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  **Default:** `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  **Default:** `""` |
| **login_unix_socket**  aliases: unix_socket  string | Path to a Unix domain socket for local connections.  **Default:** `""` |
| **login_user**  aliases: login  string | The username this module should use to establish its PostgreSQL session.  **Default:** `"postgres"` |
| **named_args**  dictionary | Dictionary of key-value arguments to pass to the query. When the value is a list, it will be converted to PostgreSQL array.  Mutually exclusive with *positional_args*. |
| **path_to_script**  path | This option has been **deprecated** and will be removed in community.postgresql 3.0.0, please use the [community.postgresql.postgresql_script](postgresql_script_module.md#ansible-collections-community-postgresql-postgresql-script-module) module to execute statements from scripts.  Path to a SQL script on the target machine.  If the script contains several queries, they must be semicolon-separated.  To run scripts containing objects with semicolons (for example, function and procedure definitions), use *as_single_query=true*.  To upload dumps or to execute other complex scripts, the preferable way is to use the [community.postgresql.postgresql_db](postgresql_db_module.md#ansible-collections-community-postgresql-postgresql-db-module) module with *state=restore*.  Mutually exclusive with *query*. |
| **port**  aliases: login_port  integer | Database port to connect to.  **Default:** `5432` |
| **positional_args**  list / elements=any | List of values to be passed as positional arguments to the query. When the value is a list, it will be converted to PostgreSQL array.  Mutually exclusive with *named_args*. |
| **query**  any | SQL query string or list of queries to run. Variables can be escaped with psycopg2 syntax <http://initd.org/psycopg/docs/usage.html>. |
| **search_path**  list / elements=string  *added in community.postgresql 1.0.0* | List of schema names to look in. |
| **session_role**  string | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_cert**  path  *added in community.postgresql 2.4.0* | Specifies the file name of the client SSL certificate. |
| **ssl_key**  path  *added in community.postgresql 2.4.0* | Specifies the location for the secret key used for the client certificate. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  **Choices:**   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **trust_input**  boolean  *added in community.postgresql 0.2.0* | If `false`, check whether a value of *session_role* is potentially dangerous.  It makes sense to use `false` only when SQL injections via *session_role* are possible.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](postgresql_query_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](postgresql_query_module.md#id5)

> **Note:**
>
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses `psycopg2`, a Python PostgreSQL database adapter. You must ensure that `psycopg2` is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the `postgresql`, `libpq-dev`, and `python-psycopg2` packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_query_module.md#id6)

> **See also:**
>
> [community.postgresql.postgresql_script](postgresql_script_module.md#ansible-collections-community-postgresql-postgresql-script-module)
> :   Run PostgreSQL statements from a file.
>
> [community.postgresql.postgresql_db](postgresql_db_module.md#ansible-collections-community-postgresql-postgresql-db-module)
> :   Add or remove PostgreSQL databases from a remote host.
>
> [PostgreSQL Schema reference](https://www.postgresql.org/docs/current/ddl-schemas.html)
> :   Complete reference of the PostgreSQL schema documentation.

## [Examples](postgresql_query_module.md#id7)

```yaml+jinja
- name: Simple select query to acme db
  community.postgresql.postgresql_query:
    db: acme
    query: SELECT version()

# The result of each query will be stored in query_all_results return value
- name: Run several queries against acme db
  community.postgresql.postgresql_query:
    db: acme
    query:
    - SELECT version()
    - SELECT id FROM accounts

- name: Select query to db acme with positional arguments and non-default credentials
  community.postgresql.postgresql_query:
    db: acme
    login_user: django
    login_password: mysecretpass
    query: SELECT * FROM acme WHERE id = %s AND story = %s
    positional_args:
    - 1
    - test

- name: Select query to test_db with named_args
  community.postgresql.postgresql_query:
    db: test_db
    query: SELECT * FROM test WHERE id = %(id_val)s AND story = %(story_val)s
    named_args:
      id_val: 1
      story_val: test

- name: Insert query to test_table in db test_db
  community.postgresql.postgresql_query:
    db: test_db
    query: INSERT INTO test_table (id, story) VALUES (2, 'my_long_story')

- name: Use connect_params to add any additional connection parameters that libpg supports
  community.postgresql.postgresql_query:
    connect_params:
      target_session_attrs: read-write
      connect_timeout: 10
    login_host: "host1,host2"
    login_user: "test"
    login_password: "test1234"
    db: 'test'
    query: 'insert into test (test) values (now())'

# WARNING: The path_to_script and as_single_query options have been deprecated
# and will be removed in community.postgresql 3.0.0, please
# use the community.postgresql.postgresql_script module instead.
# If your script contains semicolons as parts of separate objects
# like functions, procedures, and so on, use "as_single_query: true"
- name: Run queries from SQL script using UTF-8 client encoding for session
  community.postgresql.postgresql_query:
    db: test_db
    path_to_script: /var/lib/pgsql/test.sql
    positional_args:
    - 1
    encoding: UTF-8

- name: Example of using autocommit parameter
  community.postgresql.postgresql_query:
    db: test_db
    query: VACUUM
    autocommit: true

- name: >
    Insert data to the column of array type using positional_args.
    Note that we use quotes here, the same as for passing JSON, etc.
  community.postgresql.postgresql_query:
    query: INSERT INTO test_table (array_column) VALUES (%s)
    positional_args:
    - '{1,2,3}'

# Pass list and string vars as positional_args
- name: Set vars
  ansible.builtin.set_fact:
    my_list:
    - 1
    - 2
    - 3
    my_arr: '{1, 2, 3}'

- name: Select from test table by passing positional_args as arrays
  community.postgresql.postgresql_query:
    query: SELECT * FROM test_array_table WHERE arr_col1 = %s AND arr_col2 = %s
    positional_args:
    - '{{ my_list }}'
    - '{{ my_arr|string }}'

# Select from test table looking into app1 schema first, then,
# if the schema doesn't exist or the table hasn't been found there,
# try to find it in the schema public
- name: Select from test using search_path
  community.postgresql.postgresql_query:
    query: SELECT * FROM test_array_table
    search_path:
    - app1
    - public

# If you use a variable in positional_args / named_args that can
# be undefined and you wish to set it as NULL, the constructions like
# "{{ my_var if (my_var is defined) else none | default(none) }}"
# will not work as expected substituting an empty string instead of NULL.
# If possible, we suggest to use Ansible's DEFAULT_JINJA2_NATIVE configuration
# (https://docs.ansible.com/ansible/latest/reference_appendices/config.html#default-jinja2-native).
# Enabling it fixes this problem. If you cannot enable it, the following workaround
# can be used.
# You should precheck such a value and define it as NULL when undefined.
# For example:
- name: When undefined, set to NULL
  set_fact:
    my_var: NULL
  when: my_var is undefined

# Then:
- name: Insert a value using positional arguments
  community.postgresql.postgresql_query:
    query: INSERT INTO test_table (col1) VALUES (%s)
    positional_args:
    - '{{ my_var }}'
```

## [Return Values](postgresql_query_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **query**  string | Executed query.  When reading several queries from a file, it contains only the last one.  **Returned:** success  **Sample:** `"SELECT * FROM bar"` |
| **query_all_results**  list / elements=list | List containing results of all queries executed (one sublist for every query). Useful when running a list of queries.  **Returned:** success  **Sample:** `[[{"Column": "Value1"}, {"Column": "Value2"}], [{"Column": "Value1"}, {"Column": "Value2"}]]` |
| **query_list**  list / elements=string | List of executed queries. Useful when reading several queries from a file.  **Returned:** success  **Sample:** `["SELECT * FROM foo", "SELECT * FROM bar"]` |
| **query_result**  list / elements=dictionary | List of dictionaries in column:value form representing returned rows.  When running queries from a file, returns result of the last query.  **Returned:** success  **Sample:** `[{"Column": "Value1"}, {"Column": "Value2"}]` |
| **rowcount**  integer | Number of produced or affected rows.  When using a script with multiple queries, it contains a total number of produced or affected rows.  **Returned:** changed  **Sample:** `5` |
| **statusmessage**  string | Attribute containing the message returned by the command.  When reading several queries from a file, it contains a message of the last one.  **Returned:** success  **Sample:** `"INSERT 0 1"` |

### Authors

- Felix Archambault (@archf)
- Andrew Klychkov (@Andersson007)
- Will Rouesnel (@wrouesnel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
- [Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
- [Communication](index.md#communication-for-community-postgresql)

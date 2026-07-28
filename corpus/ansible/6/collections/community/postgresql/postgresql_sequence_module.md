---
collection: ansible
version: "6"
title: "community.postgresql.postgresql_sequence module – Create, drop, or alter a PostgreSQL sequence"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/postgresql/postgresql_sequence_module.html
fetched_at: 2026-07-27T17:20:26+00:00
---
# community.postgresql.postgresql_sequence module – Create, drop, or alter a PostgreSQL sequence

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
> see [Requirements](postgresql_sequence_module.md#ansible-collections-community-postgresql-postgresql-sequence-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_sequence`.

- [Synopsis](postgresql_sequence_module.md#synopsis)
- [Requirements](postgresql_sequence_module.md#requirements)
- [Parameters](postgresql_sequence_module.md#parameters)
- [Notes](postgresql_sequence_module.md#notes)
- [See Also](postgresql_sequence_module.md#see-also)
- [Examples](postgresql_sequence_module.md#examples)
- [Return Values](postgresql_sequence_module.md#return-values)

## [Synopsis](postgresql_sequence_module.md#id1)

- Allows to create, drop or change the definition of a sequence generator.

## [Requirements](postgresql_sequence_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_sequence_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **cache**  integer | Cache specifies how many sequence numbers are to be preallocated and stored in memory for faster access. The minimum value is 1 (only one value can be generated at a time, i.e., no cache), and this is also the default. |
| **cascade**  boolean | Automatically drop objects that depend on the sequence, and in turn all objects that depend on those objects.  Ignored if *state=present*.  Only used with *state=absent*.  Choices:   - `false` ← (default) - `true` |
| **connect_params**  dictionary  added in community.postgresql 2.3.0 | Any additional parameters to be passed to libpg.  These parameters take precedence.  Default: `{}` |
| **cycle**  boolean | The cycle option allows the sequence to wrap around when the *maxvalue* or *minvalue* has been reached by an ascending or descending sequence respectively. If the limit is reached, the next number generated will be the minvalue or maxvalue, respectively.  If `false` (NO CYCLE) is specified, any calls to nextval after the sequence has reached its maximum value will return an error. False (NO CYCLE) is the default.  Choices:   - `false` ← (default) - `true` |
| **data_type**  string | Specifies the data type of the sequence. Valid types are bigint, integer, and smallint. bigint is the default. The data type determines the default minimum and maximum values of the sequence. For more info see the documentation <https://www.postgresql.org/docs/current/sql-createsequence.html>.  Supported from PostgreSQL 10.  Choices:   - `"bigint"` - `"integer"` - `"smallint"` |
| **db**  aliases: database, login_db  string | Name of database to connect to and run queries against.  Default: `""` |
| **increment**  integer | Increment specifies which value is added to the current sequence value to create a new value.  A positive value will make an ascending sequence, a negative one a descending sequence. The default value is 1. |
| **login_host**  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  Default: `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  Default: `""` |
| **login_unix_socket**  string | Path to a Unix domain socket for local connections.  Default: `""` |
| **login_user**  string | The username this module should use to establish its PostgreSQL session.  Default: `"postgres"` |
| **maxvalue**  aliases: max  integer | Maxvalue determines the maximum value for the sequence. The default for an ascending sequence is the maximum value of the data type. The default for a descending sequence is -1. |
| **minvalue**  aliases: min  integer | Minvalue determines the minimum value a sequence can generate. The default for an ascending sequence is 1. The default for a descending sequence is the minimum value of the data type. |
| **newschema**  string | The new schema for the *sequence*. Will be used for moving a *sequence* to another *schema*.  Works only for existing sequences. |
| **owner**  string | Set the owner for the *sequence*. |
| **port**  aliases: login_port  integer | Database port to connect to.  Default: `5432` |
| **rename_to**  string | The new name for the *sequence*.  Works only for existing sequences. |
| **schema**  string | The schema of the *sequence*. This is be used to create and relocate a *sequence* in the given schema.  Default: `"public"` |
| **sequence**  aliases: name  string / required | The name of the sequence. |
| **session_role**  string | Switch to session_role after connecting. The specified *session_role* must be a role that the current *login_user* is a member of.  Permissions checking for SQL commands is carried out as though the *session_role* were the one that had logged in originally. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  Choices:   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **start**  integer | Start allows the sequence to begin anywhere. The default starting value is *minvalue* for ascending sequences and *maxvalue* for descending ones. |
| **state**  string | The sequence state.  If *state=absent* other options will be ignored except of *name* and *schema*.  Choices:   - `"absent"` - `"present"` ← (default) |
| **trust_input**  boolean  added in community.postgresql 0.2.0 | If `false`, check whether values of parameters *sequence*, *schema*, *rename_to*, *owner*, *newschema*, *session_role* are potentially dangerous.  It makes sense to use `false` only when SQL injections via the parameters are possible.  Choices:   - `false` - `true` ← (default) |

## [Notes](postgresql_sequence_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.
> - If you do not pass db parameter, sequence will be created in the database named postgres.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses psycopg2, a Python PostgreSQL database adapter. You must ensure that psycopg2 is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the postgresql, libpq-dev, and python-psycopg2 packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_sequence_module.md#id5)

> **See also:**
>
> [community.postgresql.postgresql_table](postgresql_table_module.md#ansible-collections-community-postgresql-postgresql-table-module)
> :   Create, drop, or modify a PostgreSQL table.
>
> [community.postgresql.postgresql_owner](postgresql_owner_module.md#ansible-collections-community-postgresql-postgresql-owner-module)
> :   Change an owner of PostgreSQL database object.
>
> [community.postgresql.postgresql_privs](postgresql_privs_module.md#ansible-collections-community-postgresql-postgresql-privs-module)
> :   Grant or revoke privileges on PostgreSQL database objects.
>
> [community.postgresql.postgresql_tablespace](postgresql_tablespace_module.md#ansible-collections-community-postgresql-postgresql-tablespace-module)
> :   Add or remove PostgreSQL tablespaces from remote hosts.
>
> [CREATE SEQUENCE reference](https://www.postgresql.org/docs/current/sql-createsequence.html)
> :   Complete reference of the CREATE SEQUENCE command documentation.
>
> [ALTER SEQUENCE reference](https://www.postgresql.org/docs/current/sql-altersequence.html)
> :   Complete reference of the ALTER SEQUENCE command documentation.
>
> [DROP SEQUENCE reference](https://www.postgresql.org/docs/current/sql-dropsequence.html)
> :   Complete reference of the DROP SEQUENCE command documentation.

## [Examples](postgresql_sequence_module.md#id6)

```yaml+jinja
- name: Create an ascending bigint sequence called foobar in the default
        database
  community.postgresql.postgresql_sequence:
    name: foobar

- name: Create an ascending integer sequence called foobar, starting at 101
  community.postgresql.postgresql_sequence:
    name: foobar
    data_type: integer
    start: 101

- name: Create an descending sequence called foobar, starting at 101 and
        preallocated 10 sequence numbers in cache
  community.postgresql.postgresql_sequence:
    name: foobar
    increment: -1
    cache: 10
    start: 101

- name: Create an ascending sequence called foobar, which cycle between 1 to 10
  community.postgresql.postgresql_sequence:
    name: foobar
    cycle: true
    min: 1
    max: 10

- name: Create an ascending bigint sequence called foobar in the default
        database with owner foobar
  community.postgresql.postgresql_sequence:
    name: foobar
    owner: foobar

- name: Rename an existing sequence named foo to bar
  community.postgresql.postgresql_sequence:
    name: foo
    rename_to: bar

- name: Change the schema of an existing sequence to foobar
  community.postgresql.postgresql_sequence:
    name: foobar
    newschema: foobar

- name: Change the owner of an existing sequence to foobar
  community.postgresql.postgresql_sequence:
    name: foobar
    owner: foobar

- name: Drop a sequence called foobar
  community.postgresql.postgresql_sequence:
    name: foobar
    state: absent

- name: Drop a sequence called foobar with cascade
  community.postgresql.postgresql_sequence:
    name: foobar
    cascade: true
    state: absent
```

## [Return Values](postgresql_sequence_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cycle**  string | Shows if the sequence cycle or not.  Returned: always  Sample: `"false"` |
| **data_type**  string | Shows the current data type of the sequence.  Returned: always  Sample: `"bigint"` |
| **increment**  integer | The value of increment of the sequence. A positive value will make an ascending sequence, a negative one a descending sequence.  Returned: always  Sample: `-1` |
| **maxvalue**  integer | The value of maxvalue of the sequence.  Returned: always  Sample: `9223372036854775807` |
| **minvalue**  integer | The value of minvalue of the sequence.  Returned: always  Sample: `1` |
| **newname**  string | Shows the new sequence name after rename.  Returned: on success  Sample: `"barfoo"` |
| **newschema**  string | Shows the new schema of the sequence after schema change.  Returned: on success  Sample: `"foobar"` |
| **owner**  string | Shows the current owner of the sequence after the successful run of the task.  Returned: always  Sample: `"postgres"` |
| **queries**  string | List of queries that was tried to be executed.  Returned: always  Sample: `"['CREATE SEQUENCE \"foo\"']"` |
| **schema**  string | Name of the schema of the sequence.  Returned: always  Sample: `"foo"` |
| **sequence**  string | Sequence name.  Returned: always  Sample: `"foobar"` |
| **start**  integer | The value of start of the sequence.  Returned: always  Sample: `12` |
| **state**  string | Sequence state at the end of execution.  Returned: always  Sample: `"present"` |

### Authors

- Tobias Birkefeld (@tcraxs)
- Thomas O’Donnell (@andytom)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
[Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
[Communication](index.md#communication-for-community-postgresql)

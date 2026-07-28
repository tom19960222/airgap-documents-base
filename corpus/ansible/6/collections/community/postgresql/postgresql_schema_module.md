---
collection: ansible
version: "6"
title: "community.postgresql.postgresql_schema module – Add or remove PostgreSQL schema"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/postgresql/postgresql_schema_module.html
fetched_at: 2026-07-27T17:20:25+00:00
---
# community.postgresql.postgresql_schema module – Add or remove PostgreSQL schema

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
> see [Requirements](postgresql_schema_module.md#ansible-collections-community-postgresql-postgresql-schema-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_schema`.

- [Synopsis](postgresql_schema_module.md#synopsis)
- [Requirements](postgresql_schema_module.md#requirements)
- [Parameters](postgresql_schema_module.md#parameters)
- [Notes](postgresql_schema_module.md#notes)
- [See Also](postgresql_schema_module.md#see-also)
- [Examples](postgresql_schema_module.md#examples)
- [Return Values](postgresql_schema_module.md#return-values)

## [Synopsis](postgresql_schema_module.md#id1)

- Add or remove PostgreSQL schema.

## [Requirements](postgresql_schema_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_schema_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **cascade_drop**  boolean | Drop schema with CASCADE to remove child objects.  Choices:   - `false` ← (default) - `true` |
| **connect_params**  dictionary  added in community.postgresql 2.3.0 | Any additional parameters to be passed to libpg.  These parameters take precedence.  Default: `{}` |
| **database**  aliases: db, login_db  string | Name of the database to connect to and add or remove the schema.  Default: `"postgres"` |
| **login_host**  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  Default: `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  Default: `""` |
| **login_unix_socket**  string | Path to a Unix domain socket for local connections.  Default: `""` |
| **login_user**  string | The username this module should use to establish its PostgreSQL session.  Default: `"postgres"` |
| **name**  aliases: schema  string / required | Name of the schema to add or remove. |
| **owner**  string | Name of the role to set as owner of the schema.  Default: `""` |
| **port**  aliases: login_port  integer | Database port to connect to.  Default: `5432` |
| **session_role**  string | Switch to session_role after connecting.  The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  Choices:   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | The schema state.  Choices:   - `"absent"` - `"present"` ← (default) |
| **trust_input**  boolean  added in community.postgresql 0.2.0 | If `false`, check whether values of parameters *schema*, *owner*, *session_role* are potentially dangerous.  It makes sense to use `false` only when SQL injections via the parameters are possible.  Choices:   - `false` - `true` ← (default) |

## [Notes](postgresql_schema_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses psycopg2, a Python PostgreSQL database adapter. You must ensure that psycopg2 is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the postgresql, libpq-dev, and python-psycopg2 packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_schema_module.md#id5)

> **See also:**
>
> [PostgreSQL schemas](https://www.postgresql.org/docs/current/ddl-schemas.html)
> :   General information about PostgreSQL schemas.
>
> [CREATE SCHEMA reference](https://www.postgresql.org/docs/current/sql-createschema.html)
> :   Complete reference of the CREATE SCHEMA command documentation.
>
> [ALTER SCHEMA reference](https://www.postgresql.org/docs/current/sql-alterschema.html)
> :   Complete reference of the ALTER SCHEMA command documentation.
>
> [DROP SCHEMA reference](https://www.postgresql.org/docs/current/sql-dropschema.html)
> :   Complete reference of the DROP SCHEMA command documentation.

## [Examples](postgresql_schema_module.md#id6)

```yaml+jinja
- name: Create a new schema with name acme in test database
  community.postgresql.postgresql_schema:
    db: test
    name: acme

- name: Create a new schema acme with a user bob who will own it
  community.postgresql.postgresql_schema:
    name: acme
    owner: bob

- name: Drop schema "acme" with cascade
  community.postgresql.postgresql_schema:
    name: acme
    state: absent
    cascade_drop: true
```

## [Return Values](postgresql_schema_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **queries**  list / elements=string | List of executed queries.  Returned: always  Sample: `["CREATE SCHEMA \"acme\""]` |
| **schema**  string | Name of the schema.  Returned: success, changed  Sample: `"acme"` |

### Authors

- Flavien Chantelot (@Dorn-)
- Thomas O’Donnell (@andytom)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
[Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
[Communication](index.md#communication-for-community-postgresql)

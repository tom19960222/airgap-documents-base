---
collection: ansible
version: "6"
title: "community.postgresql.postgresql_ext module – Add or remove PostgreSQL extensions from a database"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/postgresql/postgresql_ext_module.html
fetched_at: 2026-07-27T17:20:17+00:00
---
# community.postgresql.postgresql_ext module – Add or remove PostgreSQL extensions from a database

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
> see [Requirements](postgresql_ext_module.md#ansible-collections-community-postgresql-postgresql-ext-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_ext`.

- [Synopsis](postgresql_ext_module.md#synopsis)
- [Requirements](postgresql_ext_module.md#requirements)
- [Parameters](postgresql_ext_module.md#parameters)
- [Notes](postgresql_ext_module.md#notes)
- [See Also](postgresql_ext_module.md#see-also)
- [Examples](postgresql_ext_module.md#examples)
- [Return Values](postgresql_ext_module.md#return-values)

## [Synopsis](postgresql_ext_module.md#id1)

- Add or remove PostgreSQL extensions from a database.

## [Requirements](postgresql_ext_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_ext_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **cascade**  boolean | Automatically install/remove any extensions that this extension depends on that are not already installed/removed (supported since PostgreSQL 9.6).  Choices:   - `false` ← (default) - `true` |
| **connect_params**  dictionary  added in community.postgresql 2.3.0 | Any additional parameters to be passed to libpg.  These parameters take precedence.  Default: `{}` |
| **db**  aliases: login_db  string / required | Name of the database to add or remove the extension to/from. |
| **login_host**  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  Default: `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  Default: `""` |
| **login_unix_socket**  string | Path to a Unix domain socket for local connections.  Default: `""` |
| **login_user**  string | The username this module should use to establish its PostgreSQL session.  Default: `"postgres"` |
| **name**  aliases: ext  string / required | Name of the extension to add or remove. |
| **port**  aliases: login_port  integer | Database port to connect to.  Default: `5432` |
| **schema**  string | Name of the schema to add the extension to. |
| **session_role**  string | Switch to session_role after connecting.  The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  Choices:   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | The database extension state.  Choices:   - `"absent"` - `"present"` ← (default) |
| **trust_input**  boolean  added in community.postgresql 0.2.0 | If `false`, check whether values of parameters *ext*, *schema*, *version*, *session_role* are potentially dangerous.  It makes sense to use `false` only when SQL injections via the parameters are possible.  Choices:   - `false` - `true` ← (default) |
| **version**  string | Extension version to add or update to. Has effect with *state=present* only.  If not specified and extension is not installed in the database, the latest version available will be created.  If extension is already installed, will update to the given version if a valid update path exists.  Downgrading is only supported if the extension provides a downgrade path otherwise the extension must be removed and a lower version of the extension must be made available.  Set *version=latest* to always update the extension to the latest available version. |

## [Notes](postgresql_ext_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - This module uses *psycopg2*, a Python PostgreSQL database adapter.
> - You must ensure that `psycopg2` is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the `postgresql`, `libpq-dev`, and `python-psycopg2` packages on the remote host before using this module.
> - Incomparable versions, for example PostGIS ``unpackaged``, cannot be installed.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses psycopg2, a Python PostgreSQL database adapter. You must ensure that psycopg2 is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the postgresql, libpq-dev, and python-psycopg2 packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_ext_module.md#id5)

> **See also:**
>
> [PostgreSQL extensions](https://www.postgresql.org/docs/current/external-extensions.html)
> :   General information about PostgreSQL extensions.
>
> [CREATE EXTENSION reference](https://www.postgresql.org/docs/current/sql-createextension.html)
> :   Complete reference of the CREATE EXTENSION command documentation.
>
> [ALTER EXTENSION reference](https://www.postgresql.org/docs/current/sql-alterextension.html)
> :   Complete reference of the ALTER EXTENSION command documentation.
>
> [DROP EXTENSION reference](https://www.postgresql.org/docs/current/sql-droppublication.html)
> :   Complete reference of the DROP EXTENSION command documentation.

## [Examples](postgresql_ext_module.md#id6)

```yaml+jinja
- name: Adds postgis extension to the database acme in the schema foo
  community.postgresql.postgresql_ext:
    name: postgis
    db: acme
    schema: foo

- name: Removes postgis extension to the database acme
  community.postgresql.postgresql_ext:
    name: postgis
    db: acme
    state: absent

- name: Adds earthdistance extension to the database template1 cascade
  community.postgresql.postgresql_ext:
    name: earthdistance
    db: template1
    cascade: true

# In the example below, if earthdistance extension is installed,
# it will be removed too because it depends on cube:
- name: Removes cube extension from the database acme cascade
  community.postgresql.postgresql_ext:
    name: cube
    db: acme
    cascade: true
    state: absent

- name: Create extension foo of version 1.2 or update it to that version if it's already created and a valid update path exists
  community.postgresql.postgresql_ext:
    db: acme
    name: foo
    version: 1.2

- name: Create the latest available version of extension foo. If already installed, update it to the latest version
  community.postgresql.postgresql_ext:
    db: acme
    name: foo
    version: latest
```

## [Return Values](postgresql_ext_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **query**  list / elements=string | List of executed queries.  Returned: always  Sample: `["DROP EXTENSION \"acme\""]` |

### Authors

- Daniel Schep (@dschep)
- Thomas O’Donnell (@andytom)
- Sandro Santilli (@strk)
- Andrew Klychkov (@Andersson007)
- Keith Fiske (@keithf4)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
[Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
[Communication](index.md#communication-for-community-postgresql)

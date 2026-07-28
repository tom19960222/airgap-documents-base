---
collection: ansible
version: "8"
title: "community.postgresql.postgresql_owner module – Change an owner of PostgreSQL database object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/postgresql/postgresql_owner_module.html
fetched_at: 2026-07-28T01:58:29+00:00
---
# community.postgresql.postgresql_owner module – Change an owner of PostgreSQL database object

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
> see [Requirements](postgresql_owner_module.md#ansible-collections-community-postgresql-postgresql-owner-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_owner`.

- [Synopsis](postgresql_owner_module.md#synopsis)
- [Requirements](postgresql_owner_module.md#requirements)
- [Parameters](postgresql_owner_module.md#parameters)
- [Attributes](postgresql_owner_module.md#attributes)
- [Notes](postgresql_owner_module.md#notes)
- [See Also](postgresql_owner_module.md#see-also)
- [Examples](postgresql_owner_module.md#examples)
- [Return Values](postgresql_owner_module.md#return-values)

## [Synopsis](postgresql_owner_module.md#id1)

- Change an owner of PostgreSQL database object.
- Also allows to reassign the ownership of database objects owned by a database role to another role.

## [Requirements](postgresql_owner_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_owner_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **connect_params**  dictionary  *added in community.postgresql 2.3.0* | Any additional parameters to be passed to libpg.  These parameters take precedence.  **Default:** `{}` |
| **db**  aliases: login_db  string | Name of database to connect to. |
| **fail_on_role**  boolean | If `true`, fail when *reassign_owned_by* role does not exist. Otherwise just warn and continue.  Mutually exclusive with *obj_name* and *obj_type*.  **Choices:**   - `false` - `true` ← (default) |
| **login_host**  aliases: host  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  **Default:** `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  **Default:** `""` |
| **login_unix_socket**  aliases: unix_socket  string | Path to a Unix domain socket for local connections.  **Default:** `""` |
| **login_user**  aliases: login  string | The username this module should use to establish its PostgreSQL session.  **Default:** `"postgres"` |
| **new_owner**  string / required | Role (user/group) to set as an *obj_name* owner. |
| **obj_name**  string | Name of a database object to change ownership.  Mutually exclusive with *reassign_owned_by*. |
| **obj_type**  aliases: type  string | Type of a database object.  Mutually exclusive with *reassign_owned_by*.  **Choices:**   - `"database"` - `"function"` - `"matview"` - `"sequence"` - `"schema"` - `"table"` - `"tablespace"` - `"view"` |
| **port**  aliases: login_port  integer | Database port to connect to.  **Default:** `5432` |
| **reassign_owned_by**  list / elements=string | Caution - the ownership of all the objects within the specified *db*, owned by this role(s) will be reassigned to *new_owner*.  REASSIGN OWNED is often used to prepare for the removal of one or more roles.  REASSIGN OWNED does not affect objects within other databases.  Execute this command in each database that contains objects owned by a role that is to be removed.  If role(s) exists, always returns changed True.  Cannot reassign ownership of objects that are required by the database system.  Mutually exclusive with `obj_type`. |
| **session_role**  string | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_cert**  path  *added in community.postgresql 2.4.0* | Specifies the file name of the client SSL certificate. |
| **ssl_key**  path  *added in community.postgresql 2.4.0* | Specifies the location for the secret key used for the client certificate. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  **Choices:**   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **trust_input**  boolean  *added in community.postgresql 0.2.0* | If `false`, check whether values of parameters *new_owner*, *obj_name*, *reassign_owned_by*, *session_role* are potentially dangerous.  It makes sense to use `false` only when SQL injections via the parameters are possible.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](postgresql_owner_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](postgresql_owner_module.md#id5)

> **Note:**
>
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses `psycopg2`, a Python PostgreSQL database adapter. You must ensure that `psycopg2` is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the `postgresql`, `libpq-dev`, and `python-psycopg2` packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_owner_module.md#id6)

> **See also:**
>
> [community.postgresql.postgresql_user](postgresql_user_module.md#ansible-collections-community-postgresql-postgresql-user-module)
> :   Create, alter, or remove a user (role) from a PostgreSQL server instance.
>
> [community.postgresql.postgresql_privs](postgresql_privs_module.md#ansible-collections-community-postgresql-postgresql-privs-module)
> :   Grant or revoke privileges on PostgreSQL database objects.
>
> [community.postgresql.postgresql_membership](postgresql_membership_module.md#ansible-collections-community-postgresql-postgresql-membership-module)
> :   Add or remove PostgreSQL roles from groups.
>
> [PostgreSQL REASSIGN OWNED command reference](https://www.postgresql.org/docs/current/sql-reassign-owned.html)
> :   Complete reference of the PostgreSQL REASSIGN OWNED command documentation.

## [Examples](postgresql_owner_module.md#id7)

```yaml+jinja
# Set owner as alice for function myfunc in database bar by ansible ad-hoc command:
# ansible -m postgresql_owner -a "db=bar new_owner=alice obj_name=myfunc obj_type=function"

- name: The same as above by playbook
  community.postgresql.postgresql_owner:
    db: bar
    new_owner: alice
    obj_name: myfunc
    obj_type: function

- name: Set owner as bob for table acme in database bar
  community.postgresql.postgresql_owner:
    db: bar
    new_owner: bob
    obj_name: acme
    obj_type: table

- name: Set owner as alice for view test_view in database bar
  community.postgresql.postgresql_owner:
    db: bar
    new_owner: alice
    obj_name: test_view
    obj_type: view

- name: Set owner as bob for tablespace ssd in database foo
  community.postgresql.postgresql_owner:
    db: foo
    new_owner: bob
    obj_name: ssd
    obj_type: tablespace

- name: Reassign all databases owned by bob to alice and all objects in database bar owned by bob to alice
  community.postgresql.postgresql_owner:
    db: bar
    new_owner: alice
    reassign_owned_by: bob

- name: Reassign all databases owned by bob or bill to alice and all objects in database bar owned by bob or bill to alice
  community.postgresql.postgresql_owner:
    db: bar
    new_owner: alice
    reassign_owned_by:
    - bob
    - bill
```

## [Return Values](postgresql_owner_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **queries**  string | List of executed queries.  **Returned:** success  **Sample:** `"['REASSIGN OWNED BY \"bob\" TO \"alice\"']"` |

### Authors

- Andrew Klychkov (@Andersson007)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
- [Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
- [Communication](index.md#communication-for-community-postgresql)

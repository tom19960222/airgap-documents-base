---
collection: ansible
version: "6"
title: "community.postgresql.postgresql_privs module – Grant or revoke privileges on PostgreSQL database objects"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/postgresql/postgresql_privs_module.html
fetched_at: 2026-07-27T17:20:23+00:00
---
# community.postgresql.postgresql_privs module – Grant or revoke privileges on PostgreSQL database objects

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
> see [Requirements](postgresql_privs_module.md#ansible-collections-community-postgresql-postgresql-privs-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_privs`.

- [Synopsis](postgresql_privs_module.md#synopsis)
- [Requirements](postgresql_privs_module.md#requirements)
- [Parameters](postgresql_privs_module.md#parameters)
- [Notes](postgresql_privs_module.md#notes)
- [See Also](postgresql_privs_module.md#see-also)
- [Examples](postgresql_privs_module.md#examples)
- [Return Values](postgresql_privs_module.md#return-values)

## [Synopsis](postgresql_privs_module.md#id5)

- Grant or revoke privileges on PostgreSQL database objects.
- This module is basically a wrapper around most of the functionality of PostgreSQL’s GRANT and REVOKE statements with detection of changes (GRANT/REVOKE *privs* ON *type* *objs* TO/FROM *roles*).
- **WARNING** The `usage_on_types` option has been **deprecated** and will be removed in community.postgresql 3.0.0, please use the `type` option with value `type` to GRANT/REVOKE permissions on types explicitly.

## [Requirements](postgresql_privs_module.md#id6)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_privs_module.md#id7)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **connect_params**  dictionary  added in community.postgresql 2.3.0 | Any additional parameters to be passed to libpg.  These parameters take precedence.  Default: `{}` |
| **database**  aliases: db, login_db  string / required | Name of database to connect to. |
| **fail_on_role**  boolean | If `true`, fail when target role (for whom privs need to be granted) does not exist. Otherwise just warn and continue.  Choices:   - `false` - `true` ← (default) |
| **grant_option**  aliases: admin_option  boolean | Whether `role` may grant/revoke the specified privileges/group memberships to others.  Set to `false` to revoke GRANT OPTION, leave unspecified to make no changes.  *grant_option* only has an effect if *state* is `present`.  Choices:   - `false` - `true` |
| **host**  aliases: login_host  string | Database host address. If unspecified, connect via Unix socket.  Default: `""` |
| **login**  aliases: login_user  string | The username to authenticate with.  Default: `"postgres"` |
| **login_host**  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  Default: `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  Default: `""` |
| **login_unix_socket**  string | Path to a Unix domain socket for local connections.  Default: `""` |
| **login_user**  string | The username this module should use to establish its PostgreSQL session.  Default: `"postgres"` |
| **objs**  aliases: obj  string | Comma separated list of database objects to set privileges on.  If *type* is `table`, `partition table`, `sequence`, `function` or `procedure`, the special value `ALL_IN_SCHEMA` can be provided instead to specify all database objects of *type* in the schema specified via *schema*. (This also works with PostgreSQL < 9.0.) (`ALL_IN_SCHEMA` is available for `function` and `partition table` since Ansible 2.8).  `procedure` is supported since PostgreSQL 11 and community.postgresql collection 1.3.0.  If *type* is `database`, this parameter can be omitted, in which case privileges are set for the database specified via *database*.  If *type* is `function` or `procedure`, colons (“:”) in object names will be replaced with commas (needed to specify signatures, see examples). |
| **password**  aliases: login_password  string | The password to authenticate with.  Default: `""` |
| **port**  aliases: login_port  integer | Database port to connect to.  Default: `5432` |
| **privs**  aliases: priv  string | Comma separated list of privileges to grant/revoke. |
| **roles**  aliases: role  string / required | Comma separated list of role (user/group) names to set permissions for.  The special value `PUBLIC` can be provided instead to set permissions for the implicitly defined PUBLIC group. |
| **schema**  string | Schema that contains the database objects specified via *objs*.  May only be provided if *type* is `table`, `sequence`, `function`, `procedure`, `type`, or `default_privs`. Defaults to `public` in these cases.  Pay attention, for embedded types when *type=type* *schema* can be `pg_catalog` or `information_schema` respectively.  If not specified, uses `public`. Not to pass any schema, use `not-specified`. |
| **session_role**  string | Switch to session_role after connecting.  The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  Choices:   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | If `present`, the specified privileges are granted, if `absent` they are revoked.  Choices:   - `"absent"` - `"present"` ← (default) |
| **target_roles**  string | A list of existing role (user/group) names to set as the default permissions for database objects subsequently created by them.  Parameter *target_roles* is only available with `type=default_privs`. |
| **trust_input**  boolean  added in community.postgresql 0.2.0 | If `false`, check whether values of parameters *roles*, *target_roles*, *session_role*, *schema* are potentially dangerous.  It makes sense to use `false` only when SQL injections via the parameters are possible.  Choices:   - `false` - `true` ← (default) |
| **type**  string | Type of database object to set privileges on.  The `default_privs` choice is available starting at version 2.7.  The `foreign_data_wrapper` and `foreign_server` object types are available since Ansible version 2.8.  The `type` choice is available since Ansible version 2.10.  The `procedure` is supported since collection version 1.3.0 and PostgreSQL 11.  Choices:   - `"database"` - `"default_privs"` - `"foreign_data_wrapper"` - `"foreign_server"` - `"function"` - `"group"` - `"language"` - `"table"` ← (default) - `"tablespace"` - `"schema"` - `"sequence"` - `"type"` - `"procedure"` |
| **unix_socket**  aliases: login_unix_socket  string | Path to a Unix domain socket for local connections.  Default: `""` |
| **usage_on_types**  boolean  added in community.postgresql 1.2.0 | This option has been **deprecated** and will be removed in community.postgresql 3.0.0, please use the *type* option with value `type` to GRANT/REVOKE permissions on types explicitly.  When adding default privileges, the module always implicitly adds ``USAGE ON TYPES``.  To avoid this behavior, set *usage_on_types* to `false`.  Added to save backwards compatibility.  Used only when adding default privileges, ignored otherwise.  Choices:   - `false` - `true` ← (default) |

## [Notes](postgresql_privs_module.md#id8)

> **Note:**
>
> - Supports `check_mode`.
> - Parameters that accept comma separated lists (*privs*, *objs*, *roles*) have singular alias names (*priv*, *obj*, *role*).
> - To revoke only `GRANT OPTION` for a specific object, set *state* to `present` and *grant_option* to `false` (see examples).
> - Note that when revoking privileges from a role R, this role may still have access via privileges granted to any role R is a member of including `PUBLIC`.
> - Note that when you use `PUBLIC` role, the module always reports that the state has been changed.
> - Note that when revoking privileges from a role R, you do so as the user specified via *login*. If R has been granted the same privileges by another user also, R can still access database objects via these privileges.
> - When revoking privileges, `RESTRICT` is assumed (see PostgreSQL docs).
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses psycopg2, a Python PostgreSQL database adapter. You must ensure that psycopg2 is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the postgresql, libpq-dev, and python-psycopg2 packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_privs_module.md#id9)

> **See also:**
>
> [community.postgresql.postgresql_user](postgresql_user_module.md#ansible-collections-community-postgresql-postgresql-user-module)
> :   Create, alter, or remove a user (role) from a PostgreSQL server instance.
>
> [community.postgresql.postgresql_owner](postgresql_owner_module.md#ansible-collections-community-postgresql-postgresql-owner-module)
> :   Change an owner of PostgreSQL database object.
>
> [community.postgresql.postgresql_membership](postgresql_membership_module.md#ansible-collections-community-postgresql-postgresql-membership-module)
> :   Add or remove PostgreSQL roles from groups.
>
> [PostgreSQL privileges](https://www.postgresql.org/docs/current/ddl-priv.html)
> :   General information about PostgreSQL privileges.
>
> [PostgreSQL GRANT command reference](https://www.postgresql.org/docs/current/sql-grant.html)
> :   Complete reference of the PostgreSQL GRANT command documentation.
>
> [PostgreSQL REVOKE command reference](https://www.postgresql.org/docs/current/sql-revoke.html)
> :   Complete reference of the PostgreSQL REVOKE command documentation.

## [Examples](postgresql_privs_module.md#id10)

```yaml+jinja
# On database "library":
# GRANT SELECT, INSERT, UPDATE ON TABLE public.books, public.authors
# TO librarian, reader WITH GRANT OPTION
- name: Grant privs to librarian and reader on database library
  community.postgresql.postgresql_privs:
    database: library
    state: present
    privs: SELECT,INSERT,UPDATE
    type: table
    objs: books,authors
    schema: public
    roles: librarian,reader
    grant_option: true

- name: Same as above leveraging default values
  community.postgresql.postgresql_privs:
    db: library
    privs: SELECT,INSERT,UPDATE
    objs: books,authors
    roles: librarian,reader
    grant_option: true

# REVOKE GRANT OPTION FOR INSERT ON TABLE books FROM reader
# Note that role "reader" will be *granted* INSERT privilege itself if this
# isn't already the case (since state: present).
- name: Revoke privs from reader
  community.postgresql.postgresql_privs:
    db: library
    state: present
    priv: INSERT
    obj: books
    role: reader
    grant_option: false

# "public" is the default schema. This also works for PostgreSQL 8.x.
- name: REVOKE INSERT, UPDATE ON ALL TABLES IN SCHEMA public FROM reader
  community.postgresql.postgresql_privs:
    db: library
    state: absent
    privs: INSERT,UPDATE
    objs: ALL_IN_SCHEMA
    role: reader

- name: GRANT ALL PRIVILEGES ON SCHEMA public, math TO librarian
  community.postgresql.postgresql_privs:
    db: library
    privs: ALL
    type: schema
    objs: public,math
    role: librarian

# Note the separation of arguments with colons.
- name: GRANT ALL PRIVILEGES ON FUNCTION math.add(int, int) TO librarian, reader
  community.postgresql.postgresql_privs:
    db: library
    privs: ALL
    type: function
    obj: add(int:int)
    schema: math
    roles: librarian,reader

# Note that group role memberships apply cluster-wide and therefore are not
# restricted to database "library" here.
- name: GRANT librarian, reader TO alice, bob WITH ADMIN OPTION
  community.postgresql.postgresql_privs:
    db: library
    type: group
    objs: librarian,reader
    roles: alice,bob
    admin_option: true

# Note that here "db: postgres" specifies the database to connect to, not the
# database to grant privileges on (which is specified via the "objs" param)
- name: GRANT ALL PRIVILEGES ON DATABASE library TO librarian
  community.postgresql.postgresql_privs:
    db: postgres
    privs: ALL
    type: database
    obj: library
    role: librarian

# If objs is omitted for type "database", it defaults to the database
# to which the connection is established
- name: GRANT ALL PRIVILEGES ON DATABASE library TO librarian
  community.postgresql.postgresql_privs:
    db: library
    privs: ALL
    type: database
    role: librarian

# Available since version 2.7
# Objs must be set, ALL_DEFAULT to TABLES/SEQUENCES/TYPES/FUNCTIONS
# ALL_DEFAULT works only with privs=ALL
# For specific
- name: ALTER DEFAULT PRIVILEGES ON DATABASE library TO librarian
  community.postgresql.postgresql_privs:
    db: library
    objs: ALL_DEFAULT
    privs: ALL
    type: default_privs
    role: librarian
    grant_option: true

# Available since version 2.7
# Objs must be set, ALL_DEFAULT to TABLES/SEQUENCES/TYPES/FUNCTIONS
# ALL_DEFAULT works only with privs=ALL
# For specific
- name: ALTER DEFAULT PRIVILEGES ON DATABASE library TO reader, step 1
  community.postgresql.postgresql_privs:
    db: library
    objs: TABLES,SEQUENCES
    privs: SELECT
    type: default_privs
    role: reader

- name: ALTER DEFAULT PRIVILEGES ON DATABASE library TO reader, step 2
  community.postgresql.postgresql_privs:
    db: library
    objs: TYPES
    privs: USAGE
    type: default_privs
    role: reader

# Available since version 2.8
- name: GRANT ALL PRIVILEGES ON FOREIGN DATA WRAPPER fdw TO reader
  community.postgresql.postgresql_privs:
    db: test
    objs: fdw
    privs: ALL
    type: foreign_data_wrapper
    role: reader

# Available since community.postgresql 0.2.0
- name: GRANT ALL PRIVILEGES ON TYPE customtype TO reader
  community.postgresql.postgresql_privs:
    db: test
    objs: customtype
    privs: ALL
    type: type
    role: reader

# Available since version 2.8
- name: GRANT ALL PRIVILEGES ON FOREIGN SERVER fdw_server TO reader
  community.postgresql.postgresql_privs:
    db: test
    objs: fdw_server
    privs: ALL
    type: foreign_server
    role: reader

# Available since version 2.8
# Grant 'execute' permissions on all functions in schema 'common' to role 'caller'
- name: GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA common TO caller
  community.postgresql.postgresql_privs:
    type: function
    state: present
    privs: EXECUTE
    roles: caller
    objs: ALL_IN_SCHEMA
    schema: common

# Available since collection version 1.3.0
# Grant 'execute' permissions on all procedures in schema 'common' to role 'caller'
# Needs PostreSQL 11 or higher and community.postgresql 1.3.0 or higher
- name: GRANT EXECUTE ON ALL PROCEDURES IN SCHEMA common TO caller
  community.postgresql.postgresql_privs:
    type: prucedure
    state: present
    privs: EXECUTE
    roles: caller
    objs: ALL_IN_SCHEMA
    schema: common

# Available since version 2.8
# ALTER DEFAULT PRIVILEGES FOR ROLE librarian IN SCHEMA library GRANT SELECT ON TABLES TO reader
# GRANT SELECT privileges for new TABLES objects created by librarian as
# default to the role reader.
# For specific
- name: ALTER privs
  community.postgresql.postgresql_privs:
    db: library
    schema: library
    objs: TABLES
    privs: SELECT
    type: default_privs
    role: reader
    target_roles: librarian

# Available since version 2.8
# ALTER DEFAULT PRIVILEGES FOR ROLE librarian IN SCHEMA library REVOKE SELECT ON TABLES FROM reader
# REVOKE SELECT privileges for new TABLES objects created by librarian as
# default from the role reader.
# For specific
- name: ALTER privs
  community.postgresql.postgresql_privs:
    db: library
    state: absent
    schema: library
    objs: TABLES
    privs: SELECT
    type: default_privs
    role: reader
    target_roles: librarian

# Available since community.postgresql 0.2.0
- name: Grant type privileges for pg_catalog.numeric type to alice
  community.postgresql.postgresql_privs:
    type: type
    roles: alice
    privs: ALL
    objs: numeric
    schema: pg_catalog
    db: acme

- name: Alter default privileges grant usage on schemas to datascience
  community.postgresql.postgresql_privs:
    database: test
    type: default_privs
    privs: usage
    objs: schemas
    role: datascience
```

## [Return Values](postgresql_privs_module.md#id11)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **queries**  list / elements=string | List of executed queries.  Returned: always  Sample: `["REVOKE GRANT OPTION FOR INSERT ON TABLE \"books\" FROM \"reader\";"]` |

### Authors

- Bernhard Weitzhofer (@b6d)
- Tobias Birkefeld (@tcraxs)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
[Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
[Communication](index.md#communication-for-community-postgresql)

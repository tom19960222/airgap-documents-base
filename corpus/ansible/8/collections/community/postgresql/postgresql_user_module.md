---
collection: ansible
version: "8"
title: "community.postgresql.postgresql_user module – Create, alter, or remove a user (role) from a PostgreSQL server instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/postgresql/postgresql_user_module.html
fetched_at: 2026-07-28T01:58:40+00:00
---
# community.postgresql.postgresql_user module – Create, alter, or remove a user (role) from a PostgreSQL server instance

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
> see [Requirements](postgresql_user_module.md#ansible-collections-community-postgresql-postgresql-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_user`.

- [Synopsis](postgresql_user_module.md#synopsis)
- [Requirements](postgresql_user_module.md#requirements)
- [Parameters](postgresql_user_module.md#parameters)
- [Attributes](postgresql_user_module.md#attributes)
- [Notes](postgresql_user_module.md#notes)
- [See Also](postgresql_user_module.md#see-also)
- [Examples](postgresql_user_module.md#examples)
- [Return Values](postgresql_user_module.md#return-values)

## [Synopsis](postgresql_user_module.md#id1)

- Creates, alters, or removes a user (role) from a PostgreSQL server instance (“cluster” in PostgreSQL terminology) and, optionally, grants the user access to an existing database or tables.
- A user is a role with login privilege.
- You can also use it to grant or revoke user’s privileges in a particular database.
- You cannot remove a user while it still has any privileges granted to it in any database.
- Set *fail_on_user* to `false` to make the module ignore failures when trying to remove a user. In this case, the module reports if changes happened as usual and separately reports whether the user has been removed or not.
- **WARNING** The *priv* option has been **deprecated** and will be removed in community.postgresql 3.0.0. Please use the [community.postgresql.postgresql_privs](postgresql_privs_module.md#ansible-collections-community-postgresql-postgresql-privs-module) module instead.
- **WARNING** The *groups* option has been **deprecated** ans will be removed in community.postgresql 3.0.0. Please use the [community.postgresql.postgresql_membership](postgresql_membership_module.md#ansible-collections-community-postgresql-postgresql-membership-module) module instead.

## [Requirements](postgresql_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, verifies that the server’s certificate is signed by one of these authorities. |
| **comment**  string  *added in community.postgresql 0.2.0* | Adds a comment on the user (equivalent to the `COMMENT ON ROLE` statement). |
| **conn_limit**  integer | Specifies the user (role) connection limit. |
| **connect_params**  dictionary  *added in community.postgresql 2.3.0* | Any additional parameters to be passed to libpg.  These parameters take precedence.  **Default:** `{}` |
| **db**  aliases: login_db  string | Name of database to connect to and where user’s permissions are granted.  **Default:** `""` |
| **encrypted**  boolean | Whether the password is stored hashed in the database.  You can specify an unhashed password, and PostgreSQL ensures the stored password is hashed when *encrypted=true* is set. If you specify a hashed password, the module uses it as-is, regardless of the setting of *encrypted*.  Note: Postgresql 10 and newer does not support unhashed passwords.  Previous to Ansible 2.6, this was `false` by default.  **Choices:**   - `false` - `true` ← (default) |
| **expires**  string | The date at which the user’s password is to expire.  If set to `'infinity'`, user’s password never expires.  Note that this value must be a valid SQL date and time type. |
| **fail_on_user**  aliases: fail_on_role  boolean | If `true`, fails when the user (role) cannot be removed. Otherwise just log and continue.  **Choices:**   - `false` - `true` ← (default) |
| **groups**  list / elements=string | This option has been **deprecated** and will be removed in community.postgresql 3.0.0. Please use the *postgresql_membership* module to GRANT/REVOKE group/role memberships instead.  The list of groups (roles) that you want to grant to the user. |
| **login_host**  aliases: host  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  **Default:** `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  **Default:** `""` |
| **login_unix_socket**  aliases: unix_socket  string | Path to a Unix domain socket for local connections.  **Default:** `""` |
| **login_user**  aliases: login  string | The username this module should use to establish its PostgreSQL session.  **Default:** `"postgres"` |
| **name**  aliases: user  string / required | Name of the user (role) to add or remove. |
| **no_password_changes**  boolean | If `true`, does not inspect the database for password changes. If the user already exists, skips all password related checks. Useful when `pg_authid` is not accessible (such as in AWS RDS). Otherwise, makes password changes as necessary.  **Choices:**   - `false` ← (default) - `true` |
| **password**  string | Set the user’s password, before 1.4 this was required.  Password can be passed unhashed or hashed (MD5-hashed).  An unhashed password is automatically hashed when saved into the database if *encrypted* is set, otherwise it is saved in plain text format.  When passing an MD5-hashed password, you must generate it with the format `'str["md5"] + md5[ password + username ]'`, resulting in a total of 35 characters. An easy way to do this is `` echo "md5`echo -n 'verysecretpasswordJOE' | md5sum | awk '{print $1}'`" ``.  Note that if the provided password string is already in MD5-hashed format, then it is used as-is, regardless of *encrypted* option. |
| **port**  aliases: login_port  integer | Database port to connect to.  **Default:** `5432` |
| **priv**  string | This option has been **deprecated** and will be removed in community.postgresql 3.0.0. Please use the [community.postgresql.postgresql_privs](postgresql_privs_module.md#ansible-collections-community-postgresql-postgresql-privs-module) module to GRANT/REVOKE permissions instead.  Slash-separated PostgreSQL privileges string: `priv1/priv2`, where you can define the user’s privileges for the database ( allowed options - ‘CREATE’, ‘CONNECT’, ‘TEMPORARY’, ‘TEMP’, ‘ALL’. For example `CONNECT` ) or for table ( allowed options - ‘SELECT’, ‘INSERT’, ‘UPDATE’, ‘DELETE’, ‘TRUNCATE’, ‘REFERENCES’, ‘TRIGGER’, ‘ALL’. For example `table:SELECT` ). Mixed example of this string: `CONNECT/CREATE/table1:SELECT/table2:INSERT`.  When *priv* contains tables, the module uses the schema `public` by default. If you need to specify a different schema, use the `schema_name.table_name` notation, for example, `pg_catalog.pg_stat_database:SELECT`. |
| **role_attr_flags**  string | PostgreSQL user attributes string in the format: CREATEDB,CREATEROLE,SUPERUSER.  Note that ‘[NO]CREATEUSER’ is deprecated.  To create a simple role for using it like a group, use `NOLOGIN` flag.  See the full list of supported flags in documentation for your PostgreSQL version.  **Default:** `""` |
| **session_role**  string | Switch to session role after connecting.  The specified session role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session role were the one that had logged in originally. |
| **ssl_cert**  path  *added in community.postgresql 2.4.0* | Specifies the file name of the client SSL certificate. |
| **ssl_key**  path  *added in community.postgresql 2.4.0* | Specifies the location for the secret key used for the client certificate. |
| **ssl_mode**  string | Determines how an SSL session is negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  **Choices:**   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | The user (role) state.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **trust_input**  boolean  *added in community.postgresql 0.2.0* | If `false`, checks whether values of options *name*, *password*, *privs*, *expires*, *role_attr_flags*, *groups*, *comment*, *session_role* are potentially dangerous.  It makes sense to use `false` only when SQL injections through the options are possible.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](postgresql_user_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](postgresql_user_module.md#id5)

> **Note:**
>
> - The module creates a user (role) with login privilege by default. Use `NOLOGIN` *role_attr_flags* to change this behaviour.
> - If you specify `PUBLIC` as the user (role), then the privilege changes apply to all users (roles). You may not specify password or role_attr_flags when the `PUBLIC` user is specified.
> - SCRAM-SHA-256-hashed passwords (SASL Authentication) require PostgreSQL version 10 or newer. On the previous versions the whole hashed string is used as a password.
> - Working with SCRAM-SHA-256-hashed passwords, be sure you use the *environment:* variable `PGOPTIONS: "-c password_encryption=scram-sha-256"` (see the provided example).
> - On some systems (such as AWS RDS), `pg_authid` is not accessible, thus, the module cannot compare the current and desired `password`. In this case, the module assumes that the passwords are different and changes it reporting that the state has been changed. To skip all password related checks for existing users, use *no_password_changes=true*.
> - On some systems (such as AWS RDS), `SUPERUSER` is unavailable. This means the `SUPERUSER` and `NOSUPERUSER` *role_attr_flags* should not be specified to preserve idempotency and avoid InsufficientPrivilege errors.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses `psycopg2`, a Python PostgreSQL database adapter. You must ensure that `psycopg2` is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the `postgresql`, `libpq-dev`, and `python-psycopg2` packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_user_module.md#id6)

> **See also:**
>
> [community.postgresql.postgresql_privs](postgresql_privs_module.md#ansible-collections-community-postgresql-postgresql-privs-module)
> :   Grant or revoke privileges on PostgreSQL database objects.
>
> [community.postgresql.postgresql_membership](postgresql_membership_module.md#ansible-collections-community-postgresql-postgresql-membership-module)
> :   Add or remove PostgreSQL roles from groups.
>
> [community.postgresql.postgresql_owner](postgresql_owner_module.md#ansible-collections-community-postgresql-postgresql-owner-module)
> :   Change an owner of PostgreSQL database object.
>
> [PostgreSQL database roles](https://www.postgresql.org/docs/current/user-manag.html)
> :   Complete reference of the PostgreSQL database roles documentation.
>
> [PostgreSQL SASL Authentication](https://www.postgresql.org/docs/current/sasl-authentication.html)
> :   Complete reference of the PostgreSQL SASL Authentication.

## [Examples](postgresql_user_module.md#id7)

```yaml+jinja
# This example uses the 'priv' argument which is deprecated.
# You should use the 'postgresql_privs' module instead.
- name: Connect to acme database, create django user, and grant access to database and products table
  community.postgresql.postgresql_user:
    db: acme
    name: django
    password: ceec4eif7ya
    priv: "CONNECT/products:ALL"
    expires: "Jan 31 2020"

- name: Add a comment on django user
  community.postgresql.postgresql_user:
    db: acme
    name: django
    comment: This is a test user

# Connect to default database, create rails user, set its password (MD5- or SHA256-hashed),
# and grant privilege to create other databases and demote rails from super user status if user exists
# the hash from the corresponding pg_authid entry.
- name: Create rails user, set MD5-hashed password, grant privs
  community.postgresql.postgresql_user:
    name: rails
    password: md59543f1d82624df2b31672ec0f7050460
    # password: SCRAM-SHA-256$4096:zFuajwIVdli9mK=NJkcv1Q++$JC4gWIrEHmF6sqRbEiZw5FFW45HUPrpVzNdoM72o730+;fqA4vLN3mCZGbhcbQyvNYY7anCrUTsem1eCh/4YA94=
    role_attr_flags: CREATEDB,NOSUPERUSER
  # When using sha256-hashed password:
  #environment:
  #  PGOPTIONS: "-c password_encryption=scram-sha-256"

# This example uses the 'priv' argument which is deprecated.
# You should use the 'postgresql_privs' module instead.
- name: Connect to acme database and remove test user privileges from there
  community.postgresql.postgresql_user:
    db: acme
    name: test
    priv: "ALL/products:ALL"
    state: absent
    fail_on_user: false

# This example uses the 'priv' argument which is deprecated.
# You should use the 'postgresql_privs' module instead.
- name: Connect to test database, remove test user from cluster
  community.postgresql.postgresql_user:
    db: test
    name: test
    priv: ALL
    state: absent

# This example uses the 'priv' argument which is deprecated.
# You should use the 'postgresql_privs' module instead.
- name: Connect to acme database and set user's password with no expire date
  community.postgresql.postgresql_user:
    db: acme
    name: django
    password: mysupersecretword
    priv: "CONNECT/products:ALL"
    expires: infinity

# Example privileges string format
# INSERT,UPDATE/table:SELECT/anothertable:ALL

- name: Connect to test database and remove an existing user's password
  community.postgresql.postgresql_user:
    db: test
    user: test
    password: ""

# This example uses the `group` argument which is deprecated.
# You should use the `postgresql_membership` module instead.
- name: Create user test and grant group user_ro and user_rw to it
  community.postgresql.postgresql_user:
    name: test
    groups:
    - user_ro
    - user_rw

# Create user with a cleartext password if it does not exist or update its password.
# The password will be encrypted with SCRAM algorithm (available since PostgreSQL 10)
- name: Create appclient user with SCRAM-hashed password
  community.postgresql.postgresql_user:
    name: appclient
    password: "secret123"
  environment:
    PGOPTIONS: "-c password_encryption=scram-sha-256"

# This example uses the 'priv' argument which is deprecated.
# You should use the 'postgresql_privs' module instead.
- name: Create a user, grant SELECT on pg_catalog.pg_stat_database
  community.postgresql.postgresql_user:
    name: monitoring
    priv: 'pg_catalog.pg_stat_database:SELECT'
```

## [Return Values](postgresql_user_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **queries**  list / elements=string | List of executed queries.  **Returned:** success  **Sample:** `["CREATE USER \"alice\"", "GRANT CONNECT ON DATABASE \"acme\" TO \"alice\""]` |

### Authors

- Ansible Core Team

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
- [Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
- [Communication](index.md#communication-for-community-postgresql)

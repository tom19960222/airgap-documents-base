---
collection: ansible
version: "6"
title: "community.postgresql.postgresql_membership module – Add or remove PostgreSQL roles from groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/postgresql/postgresql_membership_module.html
fetched_at: 2026-07-27T17:20:20+00:00
---
# community.postgresql.postgresql_membership module – Add or remove PostgreSQL roles from groups

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
> see [Requirements](postgresql_membership_module.md#ansible-collections-community-postgresql-postgresql-membership-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_membership`.

- [Synopsis](postgresql_membership_module.md#synopsis)
- [Requirements](postgresql_membership_module.md#requirements)
- [Parameters](postgresql_membership_module.md#parameters)
- [Notes](postgresql_membership_module.md#notes)
- [See Also](postgresql_membership_module.md#see-also)
- [Examples](postgresql_membership_module.md#examples)
- [Return Values](postgresql_membership_module.md#return-values)

## [Synopsis](postgresql_membership_module.md#id1)

- Adds or removes PostgreSQL roles from groups (other roles).
- Users are roles with login privilege.
- Groups are PostgreSQL roles usually without LOGIN privilege.
- Common use case:
- 1. add a new group (groups) by [community.postgresql.postgresql_user](postgresql_user_module.md#ansible-collections-community-postgresql-postgresql-user-module) module with *role_attr_flags=NOLOGIN*
- 2. grant them desired privileges by [community.postgresql.postgresql_privs](postgresql_privs_module.md#ansible-collections-community-postgresql-postgresql-privs-module) module
- 3. add desired PostgreSQL users to the new group (groups) by this module

## [Requirements](postgresql_membership_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_membership_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **connect_params**  dictionary  added in community.postgresql 2.3.0 | Any additional parameters to be passed to libpg.  These parameters take precedence.  Default: `{}` |
| **db**  aliases: login_db  string | Name of database to connect to. |
| **fail_on_role**  boolean | If `true`, fail when group or target_role doesn’t exist. If `false`, just warn and continue.  Choices:   - `false` - `true` ← (default) |
| **groups**  aliases: group, source_role, source_roles  list / elements=string / required | The list of groups (roles) that need to be granted to or revoked from *target_roles*. |
| **login_host**  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  Default: `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  Default: `""` |
| **login_unix_socket**  string | Path to a Unix domain socket for local connections.  Default: `""` |
| **login_user**  string | The username this module should use to establish its PostgreSQL session.  Default: `"postgres"` |
| **port**  aliases: login_port  integer | Database port to connect to.  Default: `5432` |
| **session_role**  string | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  Choices:   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | Membership state.  *state=present* implies the *groups*must be granted to *target_roles*.  *state=absent* implies the *groups* must be revoked from *target_roles*.  *state=exact* implies that *target_roles* will be members of only the *groups* (available since community.postgresql 2.2.0). Any other groups will be revoked from *target_roles*.  Choices:   - `"absent"` - `"exact"` - `"present"` ← (default) |
| **target_roles**  aliases: target_role, users, user  list / elements=string / required | The list of target roles (groups will be granted to them). |
| **trust_input**  boolean  added in community.postgresql 0.2.0 | If `false`, check whether values of parameters *groups*, *target_roles*, *session_role* are potentially dangerous.  It makes sense to use `false` only when SQL injections via the parameters are possible.  Choices:   - `false` - `true` ← (default) |

## [Notes](postgresql_membership_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses psycopg2, a Python PostgreSQL database adapter. You must ensure that psycopg2 is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the postgresql, libpq-dev, and python-psycopg2 packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_membership_module.md#id5)

> **See also:**
>
> [community.postgresql.postgresql_user](postgresql_user_module.md#ansible-collections-community-postgresql-postgresql-user-module)
> :   Create, alter, or remove a user (role) from a PostgreSQL server instance.
>
> [community.postgresql.postgresql_privs](postgresql_privs_module.md#ansible-collections-community-postgresql-postgresql-privs-module)
> :   Grant or revoke privileges on PostgreSQL database objects.
>
> [community.postgresql.postgresql_owner](postgresql_owner_module.md#ansible-collections-community-postgresql-postgresql-owner-module)
> :   Change an owner of PostgreSQL database object.
>
> [PostgreSQL role membership reference](https://www.postgresql.org/docs/current/role-membership.html)
> :   Complete reference of the PostgreSQL role membership documentation.
>
> [PostgreSQL role attributes reference](https://www.postgresql.org/docs/current/role-attributes.html)
> :   Complete reference of the PostgreSQL role attributes documentation.

## [Examples](postgresql_membership_module.md#id6)

```yaml+jinja
- name: Grant role read_only to alice and bob
  community.postgresql.postgresql_membership:
    group: read_only
    target_roles:
    - alice
    - bob
    state: present

# you can also use target_roles: alice,bob,etc to pass the role list

- name: Revoke role read_only and exec_func from bob. Ignore if roles don't exist
  community.postgresql.postgresql_membership:
    groups:
    - read_only
    - exec_func
    target_role: bob
    fail_on_role: false
    state: absent

- name: >
    Make sure alice and bob are members only of marketing and sales.
    If they are members of other groups, they will be removed from those groups
  community.postgresql.postgresql_membership:
    group:
    - marketing
    - sales
    target_roles:
    - alice
    - bob
    state: exact

- name: Make sure alice and bob do not belong to any groups
  community.postgresql.postgresql_membership:
    group: []
    target_roles:
    - alice
    - bob
    state: exact
```

## [Return Values](postgresql_membership_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **granted**  dictionary | Dict of granted groups and roles.  Returned: if *state=present*  Sample: `{"ro_group": ["alice", "bob"]}` |
| **queries**  string | List of executed queries.  Returned: always  Sample: `"['GRANT \"user_ro\" TO \"alice\"']"` |
| **revoked**  dictionary | Dict of revoked groups and roles.  Returned: if *state=absent*  Sample: `{"ro_group": ["alice", "bob"]}` |
| **state**  string | Membership state that tried to be set.  Returned: always  Sample: `"present"` |

### Authors

- Andrew Klychkov (@Andersson007)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
[Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
[Communication](index.md#communication-for-community-postgresql)

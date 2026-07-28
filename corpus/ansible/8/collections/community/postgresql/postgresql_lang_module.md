---
collection: ansible
version: "8"
title: "community.postgresql.postgresql_lang module – Adds, removes or changes procedural languages with a PostgreSQL database"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/postgresql/postgresql_lang_module.html
fetched_at: 2026-07-28T01:58:28+00:00
---
# community.postgresql.postgresql_lang module – Adds, removes or changes procedural languages with a PostgreSQL database

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
> see [Requirements](postgresql_lang_module.md#ansible-collections-community-postgresql-postgresql-lang-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_lang`.

- [DEPRECATED](postgresql_lang_module.md#deprecated)
- [Synopsis](postgresql_lang_module.md#synopsis)
- [Requirements](postgresql_lang_module.md#requirements)
- [Parameters](postgresql_lang_module.md#parameters)
- [Attributes](postgresql_lang_module.md#attributes)
- [Notes](postgresql_lang_module.md#notes)
- [See Also](postgresql_lang_module.md#see-also)
- [Examples](postgresql_lang_module.md#examples)
- [Return Values](postgresql_lang_module.md#return-values)
- [Status](postgresql_lang_module.md#status)

## [DEPRECATED](postgresql_lang_module.md#id1)

Removed in:
:   version 4.0.0

Why:
:   As of PostgreSQL 9.1, most procedural languages have been made into extensions.

Alternative:
:   Use [community.postgresql.postgresql_ext](postgresql_ext_module.md#ansible-collections-community-postgresql-postgresql-ext-module) instead.

## [Synopsis](postgresql_lang_module.md#id2)

- Adds, removes or changes procedural languages with a PostgreSQL database.
- This module allows you to add a language, remote a language or change the trust relationship with a PostgreSQL database.
- The module can be used on the machine where executed or on a remote host.
- When removing a language from a database, it is possible that dependencies prevent the database from being removed. In that case, you can specify *cascade=true* to automatically drop objects that depend on the language (such as functions in the language).
- In case the language can’t be deleted because it is required by the database system, you can specify *fail_on_drop=false* to ignore the error.
- Be careful when marking a language as trusted since this could be a potential security breach. Untrusted languages allow only users with the PostgreSQL superuser privilege to use this language to create new functions.

## [Requirements](postgresql_lang_module.md#id3)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_lang_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **cascade**  boolean | When dropping a language, also delete object that depend on this language.  Only used when *state=absent*.  **Choices:**   - `false` ← (default) - `true` |
| **connect_params**  dictionary  *added in community.postgresql 2.3.0* | Any additional parameters to be passed to libpg.  These parameters take precedence.  **Default:** `{}` |
| **db**  aliases: login_db  string / required | Name of database to connect to and where the language will be added, removed or changed. |
| **fail_on_drop**  boolean | If `true`, fail when removing a language. Otherwise just log and continue.  In some cases, it is not possible to remove a language (used by the db-system).  When dependencies block the removal, consider using *cascade*.  **Choices:**   - `false` - `true` ← (default) |
| **force_trust**  boolean | Marks the language as trusted, even if it’s marked as untrusted in pg_pltemplate.  Use with care!  **Choices:**   - `false` ← (default) - `true` |
| **lang**  aliases: name  string / required | Name of the procedural language to add, remove or change. |
| **login_host**  aliases: host  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  **Default:** `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  **Default:** `""` |
| **login_unix_socket**  aliases: unix_socket  string | Path to a Unix domain socket for local connections.  **Default:** `""` |
| **login_user**  aliases: login  string | The username this module should use to establish its PostgreSQL session.  **Default:** `"postgres"` |
| **owner**  string  *added in community.postgresql 0.2.0* | Set an owner for the language.  Ignored when *state=absent*. |
| **port**  aliases: login_port  integer | Database port to connect to.  **Default:** `5432` |
| **session_role**  string | Switch to session_role after connecting.  The specified *session_role* must be a role that the current *login_user* is a member of.  Permissions checking for SQL commands is carried out as though the *session_role* were the one that had logged in originally. |
| **ssl_cert**  path  *added in community.postgresql 2.4.0* | Specifies the file name of the client SSL certificate. |
| **ssl_key**  path  *added in community.postgresql 2.4.0* | Specifies the location for the secret key used for the client certificate. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  **Choices:**   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | The state of the language for the selected database.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **trust**  boolean | Make this language trusted for the selected db.  **Choices:**   - `false` ← (default) - `true` |
| **trust_input**  boolean  *added in community.postgresql 0.2.0* | If `false`, check whether values of parameters *lang*, *session_role*, *owner* are potentially dangerous.  It makes sense to use `false` only when SQL injections via the parameters are possible.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](postgresql_lang_module.md#id5)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](postgresql_lang_module.md#id6)

> **Note:**
>
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses `psycopg2`, a Python PostgreSQL database adapter. You must ensure that `psycopg2` is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the `postgresql`, `libpq-dev`, and `python-psycopg2` packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_lang_module.md#id7)

> **See also:**
>
> [PostgreSQL languages](https://www.postgresql.org/docs/current/xplang.html)
> :   General information about PostgreSQL languages.
>
> [CREATE LANGUAGE reference](https://www.postgresql.org/docs/current/sql-createlanguage.html)
> :   Complete reference of the CREATE LANGUAGE command documentation.
>
> [ALTER LANGUAGE reference](https://www.postgresql.org/docs/current/sql-alterlanguage.html)
> :   Complete reference of the ALTER LANGUAGE command documentation.
>
> [DROP LANGUAGE reference](https://www.postgresql.org/docs/current/sql-droplanguage.html)
> :   Complete reference of the DROP LANGUAGE command documentation.

## [Examples](postgresql_lang_module.md#id8)

```yaml+jinja
- name: Add language pltclu to database testdb if it doesn't exist
  community.postgresql.postgresql_lang: db=testdb lang=pltclu state=present

# Add language pltclu to database testdb if it doesn't exist and mark it as trusted.
# Marks the language as trusted if it exists but isn't trusted yet.
# force_trust makes sure that the language will be marked as trusted
- name: Add language pltclu to database testdb if it doesn't exist and mark it as trusted
  community.postgresql.postgresql_lang:
    db: testdb
    lang: pltclu
    state: present
    trust: true
    force_trust: true

- name: Remove language pltclu from database testdb
  community.postgresql.postgresql_lang:
    db: testdb
    lang: pltclu
    state: absent

- name: Remove language pltclu from database testdb and remove all dependencies
  community.postgresql.postgresql_lang:
    db: testdb
    lang: pltclu
    state: absent
    cascade: true

- name: Remove language c from database testdb but ignore errors if something prevents the removal
  community.postgresql.postgresql_lang:
    db: testdb
    lang: pltclu
    state: absent
    fail_on_drop: false

- name: In testdb change owner of mylang to alice
  community.postgresql.postgresql_lang:
    db: testdb
    lang: mylang
    owner: alice
```

## [Return Values](postgresql_lang_module.md#id9)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **queries**  list / elements=string | List of executed queries.  **Returned:** success  **Sample:** `["CREATE LANGUAGE \"acme\""]` |

## [Status](postgresql_lang_module.md#id10)

- This module will be removed in version 4.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](postgresql_lang_module.md#deprecated).

### Authors

- Jens Depuydt (@jensdepuydt)
- Thomas O’Donnell (@andytom)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
- [Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
- [Communication](index.md#communication-for-community-postgresql)

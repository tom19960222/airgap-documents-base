---
collection: ansible
version: "8"
title: "community.postgresql.postgresql_publication module – Add, update, or remove PostgreSQL publication"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/postgresql/postgresql_publication_module.html
fetched_at: 2026-07-28T01:58:32+00:00
---
# community.postgresql.postgresql_publication module – Add, update, or remove PostgreSQL publication

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
> see [Requirements](postgresql_publication_module.md#ansible-collections-community-postgresql-postgresql-publication-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_publication`.

- [Synopsis](postgresql_publication_module.md#synopsis)
- [Requirements](postgresql_publication_module.md#requirements)
- [Parameters](postgresql_publication_module.md#parameters)
- [Attributes](postgresql_publication_module.md#attributes)
- [Notes](postgresql_publication_module.md#notes)
- [See Also](postgresql_publication_module.md#see-also)
- [Examples](postgresql_publication_module.md#examples)
- [Return Values](postgresql_publication_module.md#return-values)

## [Synopsis](postgresql_publication_module.md#id1)

- Add, update, or remove PostgreSQL publication.

## [Requirements](postgresql_publication_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_publication_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **cascade**  boolean | Drop publication dependencies. Has effect with *state=absent* only.  **Choices:**   - `false` ← (default) - `true` |
| **connect_params**  dictionary  *added in community.postgresql 2.3.0* | Any additional parameters to be passed to libpg.  These parameters take precedence.  **Default:** `{}` |
| **db**  aliases: login_db  string | Name of the database to connect to and where the publication state will be changed. |
| **login_host**  aliases: host  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  **Default:** `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  **Default:** `""` |
| **login_unix_socket**  aliases: unix_socket  string | Path to a Unix domain socket for local connections.  **Default:** `""` |
| **login_user**  aliases: login  string | The username this module should use to establish its PostgreSQL session.  **Default:** `"postgres"` |
| **name**  string / required | Name of the publication to add, update, or remove. |
| **owner**  string | Publication owner.  If *owner* is not defined, the owner will be set as *login_user* or *session_role*. |
| **parameters**  dictionary | Dictionary with optional publication parameters.  Available parameters depend on PostgreSQL version. |
| **port**  aliases: login_port  integer | Database port to connect to.  **Default:** `5432` |
| **session_role**  string  *added in community.postgresql 0.2.0* | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_cert**  path  *added in community.postgresql 2.4.0* | Specifies the file name of the client SSL certificate. |
| **ssl_key**  path  *added in community.postgresql 2.4.0* | Specifies the location for the secret key used for the client certificate. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  **Choices:**   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | The publication state.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tables**  list / elements=string | List of tables to add to the publication.  If no value is set all tables are targeted.  If the publication already exists for specific tables and *tables* is not passed, nothing will be changed.  If you need to add all tables to the publication with the same name, drop existent and create new without passing *tables*. |
| **trust_input**  boolean  *added in community.postgresql 0.2.0* | If `false`, check whether values of parameters *name*, *tables*, *owner*, *session_role*, *params* are potentially dangerous.  It makes sense to use `false` only when SQL injections via the parameters are possible.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](postgresql_publication_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](postgresql_publication_module.md#id5)

> **Note:**
>
> - PostgreSQL version must be 10 or greater.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses `psycopg2`, a Python PostgreSQL database adapter. You must ensure that `psycopg2` is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the `postgresql`, `libpq-dev`, and `python-psycopg2` packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_publication_module.md#id6)

> **See also:**
>
> [CREATE PUBLICATION reference](https://www.postgresql.org/docs/current/sql-createpublication.html)
> :   Complete reference of the CREATE PUBLICATION command documentation.
>
> [ALTER PUBLICATION reference](https://www.postgresql.org/docs/current/sql-alterpublication.html)
> :   Complete reference of the ALTER PUBLICATION command documentation.
>
> [DROP PUBLICATION reference](https://www.postgresql.org/docs/current/sql-droppublication.html)
> :   Complete reference of the DROP PUBLICATION command documentation.

## [Examples](postgresql_publication_module.md#id7)

```yaml+jinja
- name: Create a new publication with name "acme" targeting all tables in database "test"
  community.postgresql.postgresql_publication:
    db: test
    name: acme

- name: Create publication "acme" publishing only prices and vehicles tables
  community.postgresql.postgresql_publication:
    name: acme
    tables:
    - prices
    - vehicles

- name: >
    Create publication "acme", set user alice as an owner, targeting all tables
    Allowable DML operations are INSERT and UPDATE only
  community.postgresql.postgresql_publication:
    name: acme
    owner: alice
    parameters:
      publish: 'insert,update'

- name: >
    Assuming publication "acme" exists and there are targeted
    tables "prices" and "vehicles", add table "stores" to the publication
  community.postgresql.postgresql_publication:
    name: acme
    tables:
    - prices
    - vehicles
    - stores

- name: Remove publication "acme" if exists in database "test"
  community.postgresql.postgresql_publication:
    db: test
    name: acme
    state: absent
```

## [Return Values](postgresql_publication_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **alltables**  boolean | Flag indicates that all tables are published.  **Returned:** if publication exists  **Sample:** `false` |
| **exists**  boolean | Flag indicates the publication exists or not at the end of runtime.  **Returned:** success  **Sample:** `true` |
| **owner**  string | Owner of the publication at the end of runtime.  **Returned:** if publication exists  **Sample:** `"alice"` |
| **parameters**  dictionary | Publication parameters at the end of runtime.  **Returned:** if publication exists  **Sample:** `{"publish": {"delete": false, "insert": false, "update": true}}` |
| **queries**  string | List of executed queries.  **Returned:** success  **Sample:** `"['DROP PUBLICATION \"acme\" CASCADE']"` |
| **tables**  list / elements=string | List of tables in the publication at the end of runtime.  If all tables are published, returns empty list.  **Returned:** if publication exists  **Sample:** `["\"public\".\"prices\"", "\"public\".\"vehicles\""]` |

### Authors

- Loic Blot (@nerzhul)
- Andrew Klychkov (@Andersson007)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
- [Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
- [Communication](index.md#communication-for-community-postgresql)

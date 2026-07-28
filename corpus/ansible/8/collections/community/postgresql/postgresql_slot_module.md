---
collection: ansible
version: "8"
title: "community.postgresql.postgresql_slot module – Add or remove replication slots from a PostgreSQL database"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/postgresql/postgresql_slot_module.html
fetched_at: 2026-07-28T01:58:37+00:00
---
# community.postgresql.postgresql_slot module – Add or remove replication slots from a PostgreSQL database

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
> see [Requirements](postgresql_slot_module.md#ansible-collections-community-postgresql-postgresql-slot-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_slot`.

- [Synopsis](postgresql_slot_module.md#synopsis)
- [Requirements](postgresql_slot_module.md#requirements)
- [Parameters](postgresql_slot_module.md#parameters)
- [Attributes](postgresql_slot_module.md#attributes)
- [Notes](postgresql_slot_module.md#notes)
- [See Also](postgresql_slot_module.md#see-also)
- [Examples](postgresql_slot_module.md#examples)
- [Return Values](postgresql_slot_module.md#return-values)

## [Synopsis](postgresql_slot_module.md#id1)

- Add or remove physical or logical replication slots from a PostgreSQL database.

## [Requirements](postgresql_slot_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_slot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **connect_params**  dictionary  *added in community.postgresql 2.3.0* | Any additional parameters to be passed to libpg.  These parameters take precedence.  **Default:** `{}` |
| **db**  aliases: login_db  string | Name of database to connect to. |
| **immediately_reserve**  boolean | Optional parameter that when `true` specifies that the LSN for this replication slot be reserved immediately, otherwise the default, `false`, specifies that the LSN is reserved on the first connection from a streaming replication client.  Is available from PostgreSQL version 9.6.  Uses only with *slot_type=physical*.  Mutually exclusive with *slot_type=logical*.  **Choices:**   - `false` ← (default) - `true` |
| **login_host**  aliases: host  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  **Default:** `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  **Default:** `""` |
| **login_unix_socket**  aliases: unix_socket  string | Path to a Unix domain socket for local connections.  **Default:** `""` |
| **login_user**  aliases: login  string | The username this module should use to establish its PostgreSQL session.  **Default:** `"postgres"` |
| **name**  aliases: slot_name  string / required | Name of the replication slot to add or remove. |
| **output_plugin**  string | All logical slots must indicate which output plugin decoder they’re using.  This parameter does not apply to physical slots.  It will be ignored with *slot_type=physical*.  **Default:** `"test_decoding"` |
| **port**  aliases: login_port  integer | Database port to connect to.  **Default:** `5432` |
| **session_role**  string | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **slot_type**  string | Slot type.  **Choices:**   - `"logical"` - `"physical"` ← (default) |
| **ssl_cert**  path  *added in community.postgresql 2.4.0* | Specifies the file name of the client SSL certificate. |
| **ssl_key**  path  *added in community.postgresql 2.4.0* | Specifies the location for the secret key used for the client certificate. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  **Choices:**   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | The slot state.  *state=present* implies the slot must be present in the system.  *state=absent* implies the *groups* must be revoked from *target_roles*.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **trust_input**  boolean  *added in community.postgresql 0.2.0* | If `false`, check the value of *session_role* is potentially dangerous.  It makes sense to use `false` only when SQL injections via *session_role* are possible.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](postgresql_slot_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](postgresql_slot_module.md#id5)

> **Note:**
>
> - Physical replication slots were introduced to PostgreSQL with version 9.4, while logical replication slots were added beginning with version 10.0.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses `psycopg2`, a Python PostgreSQL database adapter. You must ensure that `psycopg2` is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the `postgresql`, `libpq-dev`, and `python-psycopg2` packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_slot_module.md#id6)

> **See also:**
>
> [PostgreSQL pg_replication_slots view reference](https://www.postgresql.org/docs/current/view-pg-replication-slots.html)
> :   Complete reference of the PostgreSQL pg_replication_slots view.
>
> [PostgreSQL streaming replication protocol reference](https://www.postgresql.org/docs/current/protocol-replication.html)
> :   Complete reference of the PostgreSQL streaming replication protocol documentation.
>
> [PostgreSQL logical replication protocol reference](https://www.postgresql.org/docs/current/protocol-logical-replication.html)
> :   Complete reference of the PostgreSQL logical replication protocol documentation.

## [Examples](postgresql_slot_module.md#id7)

```yaml+jinja
- name: Create physical_one physical slot if doesn't exist
  become_user: postgres
  community.postgresql.postgresql_slot:
    slot_name: physical_one
    db: ansible

- name: Remove physical_one slot if exists
  become_user: postgres
  community.postgresql.postgresql_slot:
    slot_name: physical_one
    db: ansible
    state: absent

- name: Create logical_one logical slot to the database acme if doesn't exist
  community.postgresql.postgresql_slot:
    name: logical_slot_one
    slot_type: logical
    state: present
    output_plugin: custom_decoder_one
    db: "acme"

- name: Remove logical_one slot if exists from the cluster running on another host and non-standard port
  community.postgresql.postgresql_slot:
    name: logical_one
    login_host: mydatabase.example.org
    port: 5433
    login_user: ourSuperuser
    login_password: thePassword
    state: absent
```

## [Return Values](postgresql_slot_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **name**  string | Name of the slot.  **Returned:** success  **Sample:** `"physical_one"` |
| **queries**  string | List of executed queries.  **Returned:** success  **Sample:** `"[\"SELECT pg_create_physical_replication_slot('physical_one', False, False)\"]"` |

### Authors

- John Scalia (@jscalia)
- Andrew Klychkov (@Andersson007)
- Thomas O’Donnell (@andytom)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
- [Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
- [Communication](index.md#communication-for-community-postgresql)

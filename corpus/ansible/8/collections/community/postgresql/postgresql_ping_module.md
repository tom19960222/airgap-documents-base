---
collection: ansible
version: "8"
title: "community.postgresql.postgresql_ping module – Check remote PostgreSQL server availability"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/postgresql/postgresql_ping_module.html
fetched_at: 2026-07-28T01:58:31+00:00
---
# community.postgresql.postgresql_ping module – Check remote PostgreSQL server availability

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
> see [Requirements](postgresql_ping_module.md#ansible-collections-community-postgresql-postgresql-ping-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_ping`.

- [Synopsis](postgresql_ping_module.md#synopsis)
- [Requirements](postgresql_ping_module.md#requirements)
- [Parameters](postgresql_ping_module.md#parameters)
- [Attributes](postgresql_ping_module.md#attributes)
- [Notes](postgresql_ping_module.md#notes)
- [See Also](postgresql_ping_module.md#see-also)
- [Examples](postgresql_ping_module.md#examples)
- [Return Values](postgresql_ping_module.md#return-values)

## [Synopsis](postgresql_ping_module.md#id1)

- Simple module to check remote PostgreSQL server availability.

## [Requirements](postgresql_ping_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_ping_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **connect_params**  dictionary  *added in community.postgresql 2.3.0* | Any additional parameters to be passed to libpg.  These parameters take precedence.  **Default:** `{}` |
| **db**  aliases: login_db  string | Name of a database to connect to. |
| **login_host**  aliases: host  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  **Default:** `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  **Default:** `""` |
| **login_unix_socket**  aliases: unix_socket  string | Path to a Unix domain socket for local connections.  **Default:** `""` |
| **login_user**  aliases: login  string | The username this module should use to establish its PostgreSQL session.  **Default:** `"postgres"` |
| **port**  aliases: login_port  integer | Database port to connect to.  **Default:** `5432` |
| **session_role**  string  *added in community.postgresql 0.2.0* | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_cert**  path  *added in community.postgresql 2.4.0* | Specifies the file name of the client SSL certificate. |
| **ssl_key**  path  *added in community.postgresql 2.4.0* | Specifies the location for the secret key used for the client certificate. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  **Choices:**   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **trust_input**  boolean  *added in community.postgresql 0.2.0* | If `false`, check whether a value of *session_role* is potentially dangerous.  It makes sense to use `false` only when SQL injections via *session_role* are possible.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](postgresql_ping_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](postgresql_ping_module.md#id5)

> **Note:**
>
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses `psycopg2`, a Python PostgreSQL database adapter. You must ensure that `psycopg2` is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the `postgresql`, `libpq-dev`, and `python-psycopg2` packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_ping_module.md#id6)

> **See also:**
>
> [community.postgresql.postgresql_info](postgresql_info_module.md#ansible-collections-community-postgresql-postgresql-info-module)
> :   Gather information about PostgreSQL servers.

## [Examples](postgresql_ping_module.md#id7)

```yaml+jinja
# PostgreSQL ping dbsrv server from the shell:
# ansible dbsrv -m postgresql_ping

# In the example below you need to generate certificates previously.
# See https://www.postgresql.org/docs/current/libpq-ssl.html for more information.
- name: >
    Ping PostgreSQL server using non-default credentials and SSL
    registering the return values into the result variable for future use
  community.postgresql.postgresql_ping:
    db: protected_db
    login_host: dbsrv
    login_user: secret
    login_password: secret_pass
    ca_cert: /root/root.crt
    ssl_mode: verify-full
  register: result
  # If you need to fail when the server is not available,
  # uncomment the following line:
  #failed_when: not result.is_available

# You can use the registered result with another task
- name: This task should be executed only if the server is available
  # ...
  when: result.is_available == true
```

## [Return Values](postgresql_ping_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **conn_err_msg**  string  *added in community.postgresql 1.7.0* | Connection error message.  **Returned:** if `is_available=true`  **Sample:** `""` |
| **is_available**  boolean | PostgreSQL server availability.  **Returned:** success  **Sample:** `true` |
| **server_version**  dictionary | PostgreSQL server version.  **Returned:** if `is_available=true`  **Sample:** `{"full": "13.2", "major": 13, "minor": 2, "raw": "PostgreSQL 13.2 on x86_64-pc-linux-gnu"}` |

### Authors

- Andrew Klychkov (@Andersson007)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
- [Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
- [Communication](index.md#communication-for-community-postgresql)

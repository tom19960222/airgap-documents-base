---
collection: ansible
version: "6"
title: "community.postgresql.postgresql_subscription module – Add, update, or remove PostgreSQL subscription"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/postgresql/postgresql_subscription_module.html
fetched_at: 2026-07-27T17:20:29+00:00
---
# community.postgresql.postgresql_subscription module – Add, update, or remove PostgreSQL subscription

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
> see [Requirements](postgresql_subscription_module.md#ansible-collections-community-postgresql-postgresql-subscription-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_subscription`.

New in community.postgresql 0.2.0

- [Synopsis](postgresql_subscription_module.md#synopsis)
- [Requirements](postgresql_subscription_module.md#requirements)
- [Parameters](postgresql_subscription_module.md#parameters)
- [Notes](postgresql_subscription_module.md#notes)
- [See Also](postgresql_subscription_module.md#see-also)
- [Examples](postgresql_subscription_module.md#examples)
- [Return Values](postgresql_subscription_module.md#return-values)

## [Synopsis](postgresql_subscription_module.md#id1)

- Add, update, or remove PostgreSQL subscription.

## [Requirements](postgresql_subscription_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_subscription_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **cascade**  boolean | Drop subscription dependencies. Has effect with *state=absent* only.  Ignored when *state* is not `absent`.  Choices:   - `false` ← (default) - `true` |
| **connect_params**  dictionary  added in community.postgresql 2.3.0 | Any additional parameters to be passed to libpg.  These parameters take precedence.  Default: `{}` |
| **connparams**  dictionary | The connection dict param-value to connect to the publisher.  For more information see <https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING>.  Ignored when *state* is not `present`. |
| **db**  aliases: login_db  string / required | Name of the database to connect to and where the subscription state will be changed. |
| **login_host**  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  Default: `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  Default: `""` |
| **login_unix_socket**  string | Path to a Unix domain socket for local connections.  Default: `""` |
| **login_user**  string | The username this module should use to establish its PostgreSQL session.  Default: `"postgres"` |
| **name**  string / required | Name of the subscription to add, update, or remove. |
| **owner**  string | Subscription owner.  If *owner* is not defined, the owner will be set as *login_user* or *session_role*.  Ignored when *state* is not `present`. |
| **port**  aliases: login_port  integer | Database port to connect to.  Default: `5432` |
| **publications**  list / elements=string | The publication names on the publisher to use for the subscription.  Ignored when *state* is not `present`. |
| **session_role**  string  added in community.postgresql 0.2.0 | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  Choices:   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | The subscription state.  `present` implies that if *name* subscription doesn’t exist, it will be created.  `absent` implies that if *name* subscription exists, it will be removed.  `refresh` implies that if *name* subscription exists, it will be refreshed. Fetch missing table information from publisher. Always returns ``changed`` is ``True``. This will start replication of tables that were added to the subscribed-to publications since the last invocation of REFRESH PUBLICATION or since CREATE SUBSCRIPTION. The existing data in the publications that are being subscribed to should be copied once the replication starts.  For more information about `refresh` see <https://www.postgresql.org/docs/current/sql-altersubscription.html>.  Choices:   - `"absent"` - `"present"` ← (default) - `"refresh"` |
| **subsparams**  dictionary | Dictionary of optional parameters for a subscription, e.g. copy_data, enabled, create_slot, etc.  For update the subscription allowed keys are `enabled`, `slot_name`, `synchronous_commit`, `publication_name`.  See available parameters to create a new subscription on <https://www.postgresql.org/docs/current/sql-createsubscription.html>.  Ignored when *state* is not `present`. |
| **trust_input**  boolean  added in community.postgresql 0.2.0 | If `false`, check whether values of parameters *name*, *publications*, *owner*, *session_role*, *connparams*, *subsparams* are potentially dangerous.  It makes sense to use `true` only when SQL injections via the parameters are possible.  Choices:   - `false` - `true` ← (default) |

## [Notes](postgresql_subscription_module.md#id4)

> **Note:**
>
> - PostgreSQL version must be 10 or greater.
> - Supports `check_mode`.
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses psycopg2, a Python PostgreSQL database adapter. You must ensure that psycopg2 is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the postgresql, libpq-dev, and python-psycopg2 packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_subscription_module.md#id5)

> **See also:**
>
> [community.postgresql.postgresql_publication](postgresql_publication_module.md#ansible-collections-community-postgresql-postgresql-publication-module)
> :   Add, update, or remove PostgreSQL publication.
>
> [community.postgresql.postgresql_info](postgresql_info_module.md#ansible-collections-community-postgresql-postgresql-info-module)
> :   Gather information about PostgreSQL servers.
>
> [CREATE SUBSCRIPTION reference](https://www.postgresql.org/docs/current/sql-createsubscription.html)
> :   Complete reference of the CREATE SUBSCRIPTION command documentation.
>
> [ALTER SUBSCRIPTION reference](https://www.postgresql.org/docs/current/sql-altersubscription.html)
> :   Complete reference of the ALTER SUBSCRIPTION command documentation.
>
> [DROP SUBSCRIPTION reference](https://www.postgresql.org/docs/current/sql-dropsubscription.html)
> :   Complete reference of the DROP SUBSCRIPTION command documentation.

## [Examples](postgresql_subscription_module.md#id6)

```yaml+jinja
- name: >
    Create acme subscription in mydb database using acme_publication and
    the following connection parameters to connect to the publisher.
    Set the subscription owner as alice.
  community.postgresql.postgresql_subscription:
    db: mydb
    name: acme
    state: present
    publications: acme_publication
    owner: alice
    connparams:
      host: 127.0.0.1
      port: 5432
      user: repl
      password: replpass
      dbname: mydb

- name: Assuming that acme subscription exists, try to change conn parameters
  community.postgresql.postgresql_subscription:
    db: mydb
    name: acme
    connparams:
      host: 127.0.0.1
      port: 5432
      user: repl
      password: replpass
      connect_timeout: 100

- name: Refresh acme publication
  community.postgresql.postgresql_subscription:
    db: mydb
    name: acme
    state: refresh

- name: Drop acme subscription from mydb with dependencies (cascade=true)
  community.postgresql.postgresql_subscription:
    db: mydb
    name: acme
    state: absent
    cascade: true

- name: Assuming that acme subscription exists and enabled, disable the subscription
  community.postgresql.postgresql_subscription:
    db: mydb
    name: acme
    state: present
    subsparams:
      enabled: false
```

## [Return Values](postgresql_subscription_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **exists**  boolean | Flag indicates the subscription exists or not at the end of runtime.  Returned: always  Sample: `true` |
| **final_state**  dictionary | Subscription configuration at the end of runtime.  Returned: always  Sample: `{"conninfo": {}, "enabled": true, "owner": "postgres", "slotname": "test", "synccommit": true}` |
| **initial_state**  dictionary | Subscription configuration at the beginning of runtime.  Returned: always  Sample: `{"conninfo": {}, "enabled": true, "owner": "postgres", "slotname": "test", "synccommit": true}` |
| **name**  string | Name of the subscription.  Returned: always  Sample: `"acme"` |
| **queries**  string | List of executed queries.  Returned: always  Sample: `"['DROP SUBSCRIPTION \"mysubscription\"']"` |

### Authors

- Andrew Klychkov (@Andersson007)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
[Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
[Communication](index.md#communication-for-community-postgresql)

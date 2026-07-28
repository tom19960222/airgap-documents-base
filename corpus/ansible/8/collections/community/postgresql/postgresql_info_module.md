---
collection: ansible
version: "8"
title: "community.postgresql.postgresql_info module – Gather information about PostgreSQL servers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/postgresql/postgresql_info_module.html
fetched_at: 2026-07-28T01:58:27+00:00
---
# community.postgresql.postgresql_info module – Gather information about PostgreSQL servers

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
> see [Requirements](postgresql_info_module.md#ansible-collections-community-postgresql-postgresql-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_info`.

- [Synopsis](postgresql_info_module.md#synopsis)
- [Requirements](postgresql_info_module.md#requirements)
- [Parameters](postgresql_info_module.md#parameters)
- [Attributes](postgresql_info_module.md#attributes)
- [Notes](postgresql_info_module.md#notes)
- [See Also](postgresql_info_module.md#see-also)
- [Examples](postgresql_info_module.md#examples)
- [Return Values](postgresql_info_module.md#return-values)

## [Synopsis](postgresql_info_module.md#id1)

- Gathers information about PostgreSQL servers.

## [Requirements](postgresql_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **connect_params**  dictionary  *added in community.postgresql 2.3.0* | Any additional parameters to be passed to libpg.  These parameters take precedence.  **Default:** `{}` |
| **db**  aliases: login_db  string | Name of database to connect. |
| **filter**  list / elements=string | Limit the collected information by comma separated string or YAML list.  Allowable values are `version`, `databases`, `in_recovery`, `settings`, `tablespaces`, `roles`, `replications`, `repl_slots`.  By default, collects all subsets.  You can use shell-style (fnmatch) wildcard to pass groups of values (see Examples).  You can use ‘!’ before value (for example, `!settings`) to exclude it from the information.  If you pass including and excluding values to the filter, for example, *filter=!settings,ver*, the excluding values will be ignored. |
| **login_host**  aliases: host  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  **Default:** `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  **Default:** `""` |
| **login_unix_socket**  aliases: unix_socket  string | Path to a Unix domain socket for local connections.  **Default:** `""` |
| **login_user**  aliases: login  string | The username this module should use to establish its PostgreSQL session.  **Default:** `"postgres"` |
| **port**  aliases: login_port  integer | Database port to connect to.  **Default:** `5432` |
| **session_role**  string | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_cert**  path  *added in community.postgresql 2.4.0* | Specifies the file name of the client SSL certificate. |
| **ssl_key**  path  *added in community.postgresql 2.4.0* | Specifies the location for the secret key used for the client certificate. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  **Choices:**   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **trust_input**  boolean  *added in community.postgresql 0.2.0* | If `false`, check whether a value of *session_role* is potentially dangerous.  It makes sense to use `false` only when SQL injections via *session_role* are possible.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](postgresql_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](postgresql_info_module.md#id5)

> **Note:**
>
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses `psycopg2`, a Python PostgreSQL database adapter. You must ensure that `psycopg2` is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the `postgresql`, `libpq-dev`, and `python-psycopg2` packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_info_module.md#id6)

> **See also:**
>
> [community.postgresql.postgresql_ping](postgresql_ping_module.md#ansible-collections-community-postgresql-postgresql-ping-module)
> :   Check remote PostgreSQL server availability.

## [Examples](postgresql_info_module.md#id7)

```yaml+jinja
# Display info from postgres hosts.
# ansible postgres -m postgresql_info

# Display only databases and roles info from all hosts using shell-style wildcards:
# ansible all -m postgresql_info -a 'filter=dat*,rol*'

# Display only replications and repl_slots info from standby hosts using shell-style wildcards:
# ansible standby -m postgresql_info -a 'filter=repl*'

# Display all info from databases hosts except settings:
# ansible databases -m postgresql_info -a 'filter=!settings'

- name: Collect PostgreSQL version and extensions
  become: true
  become_user: postgres
  community.postgresql.postgresql_info:
    filter: ver*,ext*

- name: Collect all info except settings and roles
  become: true
  become_user: postgres
  community.postgresql.postgresql_info:
    filter: "!settings,!roles"

# On FreeBSD with PostgreSQL 9.5 version and lower use pgsql user to become
# and pass "postgres" as a database to connect to
- name: Collect tablespaces and repl_slots info
  become: true
  become_user: pgsql
  community.postgresql.postgresql_info:
    db: postgres
    filter:
    - tablesp*
    - repl_sl*

- name: Collect all info except databases
  become: true
  become_user: postgres
  community.postgresql.postgresql_info:
    filter:
    - "!databases"
```

## [Return Values](postgresql_info_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **databases**  dictionary | Information about databases.  **Returned:** success  **Sample:** `[{"postgres": {"access_priv": "", "collate": "en_US.UTF-8", "ctype": "en_US.UTF-8", "encoding": "UTF8", "owner": "postgres", "size": "7997 kB"}}]` |
| **database_name**  dictionary | Database name.  **Returned:** success  **Sample:** `"template1"` |
| **access_priv**  string | Database access privileges.  **Returned:** success  **Sample:** `"=c/postgres_npostgres=CTc/postgres"` |
| **collate**  string | Database collation <https://www.postgresql.org/docs/current/collation.html>.  **Returned:** success  **Sample:** `"en_US.UTF-8"` |
| **ctype**  string | Database LC_CTYPE <https://www.postgresql.org/docs/current/multibyte.html>.  **Returned:** success  **Sample:** `"en_US.UTF-8"` |
| **encoding**  string | Database encoding <https://www.postgresql.org/docs/current/multibyte.html>.  **Returned:** success  **Sample:** `"UTF8"` |
| **extensions**  dictionary | Extensions <https://www.postgresql.org/docs/current/sql-createextension.html>.  **Returned:** success  **Sample:** `[{"plpgsql": {"description": "PL/pgSQL procedural language", "extversion": {"major": 1, "minor": 0, "raw": "1.0"}}}]` |
| **extdescription**  string | Extension description.  **Returned:** if existent  **Sample:** `"PL/pgSQL procedural language"` |
| **extversion**  dictionary | Extension description.  **Returned:** success |
| **major**  integer | Extension major version.  **Returned:** success  **Sample:** `1` |
| **minor**  integer | Extension minor version.  **Returned:** success  **Sample:** `0` |
| **raw**  string | Extension full version.  **Returned:** success  **Sample:** `"1.0"` |
| **nspname**  string | Namespace where the extension is.  **Returned:** success  **Sample:** `"pg_catalog"` |
| **languages**  dictionary | Procedural languages <https://www.postgresql.org/docs/current/xplang.html>.  **Returned:** success  **Sample:** `{"sql": {"lanacl": "", "lanowner": "postgres"}}` |
| **lanacl**  string | Language access privileges <https://www.postgresql.org/docs/current/catalog-pg-language.html>.  **Returned:** success  **Sample:** `"{postgres=UC/postgres,=U/postgres}"` |
| **lanowner**  string | Language owner <https://www.postgresql.org/docs/current/catalog-pg-language.html>.  **Returned:** success  **Sample:** `"postgres"` |
| **namespaces**  dictionary | Namespaces (schema) <https://www.postgresql.org/docs/current/sql-createschema.html>.  **Returned:** success  **Sample:** `{"pg_catalog": {"nspacl": "{postgres=UC/postgres,=U/postgres}", "nspowner": "postgres"}}` |
| **nspacl**  string | Access privileges <https://www.postgresql.org/docs/current/catalog-pg-namespace.html>.  **Returned:** success  **Sample:** `"{postgres=UC/postgres,=U/postgres}"` |
| **nspowner**  string | Schema owner <https://www.postgresql.org/docs/current/catalog-pg-namespace.html>.  **Returned:** success  **Sample:** `"postgres"` |
| **owner**  string | Database owner <https://www.postgresql.org/docs/current/sql-createdatabase.html>.  **Returned:** success  **Sample:** `"postgres"` |
| **publications**  dictionary  *added in community.postgresql 0.2.0* | Information about logical replication publications (available for PostgreSQL 10 and higher) <https://www.postgresql.org/docs/current/logical-replication-publication.html>.  Content depends on PostgreSQL server version.  **Returned:** if configured  **Sample:** `{"pub1": {"ownername": "postgres", "puballtables": true, "pubinsert": true, "pubupdate": true}}` |
| **size**  string | Database size in bytes.  **Returned:** success  **Sample:** `"8189415"` |
| **subscriptions**  dictionary  *added in community.postgresql 0.2.0* | Information about replication subscriptions (available for PostgreSQL 10 and higher) <https://www.postgresql.org/docs/current/logical-replication-subscription.html>.  Content depends on PostgreSQL server version.  The return values for the superuser and the normal user may differ <https://www.postgresql.org/docs/current/catalog-pg-subscription.html>.  **Returned:** if configured  **Sample:** `[{"my_subscription": {"ownername": "postgres", "subenabled": true, "subpublications": ["first_publication"]}}]` |
| **in_recovery**  boolean | Indicates if the service is in recovery mode or not.  **Returned:** success  **Sample:** `false` |
| **pending_restart_settings**  list / elements=string | List of settings that are pending restart to be set.  **Returned:** success  **Sample:** `["shared_buffers"]` |
| **repl_slots**  dictionary | Replication slots (available in 9.4 and later) <https://www.postgresql.org/docs/current/view-pg-replication-slots.html>.  **Returned:** if existent  **Sample:** `{"slot0": {"active": false, "database": null, "plugin": null, "slot_type": "physical"}}` |
| **active**  boolean | True means that a receiver has connected to it, and it is currently reserving archives.  **Returned:** success  **Sample:** `true` |
| **database**  string | Database name this slot is associated with, or null.  **Returned:** success  **Sample:** `"acme"` |
| **plugin**  string | Base name of the shared object containing the output plugin this logical slot is using, or null for physical slots.  **Returned:** success  **Sample:** `"pgoutput"` |
| **slot_type**  string | The slot type - physical or logical.  **Returned:** success  **Sample:** `"logical"` |
| **replications**  dictionary | Information about the current replications by process PIDs <https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-STATS-VIEWS-TABLE>.  **Returned:** if pg_stat_replication view existent  **Sample:** `[{"76580": {"app_name": "standby1", "backend_start": "2019-02-03 00:14:33.908593+03", "client_addr": "10.10.10.2", "client_hostname": "", "state": "streaming", "usename": "postgres"}}]` |
| **app_name**  string | Name of the application that is connected to this WAL sender.  **Returned:** if existent  **Sample:** `"acme_srv"` |
| **backend_start**  string | Time when this process was started, i.e., when the client connected to this WAL sender.  **Returned:** success  **Sample:** `"2019-02-03 00:14:33.908593+03"` |
| **client_addr**  string | IP address of the client connected to this WAL sender.  If this field is null, it indicates that the client is connected via a Unix socket on the server machine.  **Returned:** success  **Sample:** `"10.0.0.101"` |
| **client_hostname**  string | Host name of the connected client, as reported by a reverse DNS lookup of client_addr.  This field will only be non-null for IP connections, and only when log_hostname is enabled.  **Returned:** success  **Sample:** `"dbsrv1"` |
| **state**  string | Current WAL sender state.  **Returned:** success  **Sample:** `"streaming"` |
| **usename**  string | Name of the user logged into this WAL sender process (‘usename’ is a column name in pg_stat_replication view).  **Returned:** success  **Sample:** `"replication_user"` |
| **roles**  dictionary | Information about roles <https://www.postgresql.org/docs/current/user-manag.html>.  **Returned:** success  **Sample:** `[{"test_role": {"canlogin": true, "member_of": ["user_ro"], "superuser": false, "valid_until": "9999-12-31T23:59:59.999999+00:00"}}]` |
| **canlogin**  boolean | Login privilege <https://www.postgresql.org/docs/current/role-attributes.html>.  **Returned:** success  **Sample:** `true` |
| **member_of**  list / elements=string | Role membership <https://www.postgresql.org/docs/current/role-membership.html>.  **Returned:** success  **Sample:** `["read_only_users"]` |
| **superuser**  boolean | User is a superuser or not.  **Returned:** success  **Sample:** `false` |
| **valid_until**  string | Password expiration date <https://www.postgresql.org/docs/current/sql-alterrole.html>.  **Returned:** success  **Sample:** `"9999-12-31T23:59:59.999999+00:00"` |
| **settings**  dictionary | Information about run-time server parameters <https://www.postgresql.org/docs/current/view-pg-settings.html>.  **Returned:** success  **Sample:** `[{"work_mem": {"boot_val": "4096", "context": "user", "max_val": "2147483647", "min_val": "64", "setting": "8192", "sourcefile": "/var/lib/pgsql/10/data/postgresql.auto.conf", "unit": "kB", "val_in_bytes": 4194304, "vartype": "integer"}}]` |
| **boot_val**  string | Parameter value assumed at server startup if the parameter is not otherwise set.  **Returned:** success  **Sample:** `"4096"` |
| **context**  string | Context required to set the parameter’s value.  For more information see <https://www.postgresql.org/docs/current/view-pg-settings.html>.  **Returned:** success  **Sample:** `"user"` |
| **max_val**  string | Maximum allowed value of the parameter (null for non-numeric values).  **Returned:** success  **Sample:** `"2147483647"` |
| **min_val**  string | Minimum allowed value of the parameter (null for non-numeric values).  **Returned:** success  **Sample:** `"64"` |
| **pending_restart**  boolean | True if the value has been changed in the configuration file but needs a restart; or false otherwise.  Returns only if `settings` is passed.  **Returned:** success  **Sample:** `false` |
| **pretty_val**  string | Value presented in the pretty form.  **Returned:** success  **Sample:** `"2MB"` |
| **setting**  string | Current value of the parameter.  **Returned:** success  **Sample:** `"49152"` |
| **sourcefile**  string | Configuration file the current value was set in.  Null for values set from sources other than configuration files, or when examined by a user who is neither a superuser or a member of pg_read_all_settings.  Helpful when using include directives in configuration files.  **Returned:** success  **Sample:** `"/var/lib/pgsql/10/data/postgresql.auto.conf"` |
| **unit**  string | Implicit unit of the parameter.  **Returned:** success  **Sample:** `"kB"` |
| **val_in_bytes**  integer | Current value of the parameter in bytes.  **Returned:** if supported  **Sample:** `2147483647` |
| **vartype**  string | Parameter type (bool, enum, integer, real, or string).  **Returned:** success  **Sample:** `"integer"` |
| **tablespaces**  dictionary | Information about tablespaces <https://www.postgresql.org/docs/current/catalog-pg-tablespace.html>.  **Returned:** success  **Sample:** `[{"test": {"spcacl": "{postgres=C/postgres,andreyk=C/postgres}", "spcoptions": ["seq_page_cost=1"], "spcowner": "postgres"}}]` |
| **spcacl**  string | Tablespace access privileges.  **Returned:** success  **Sample:** `"{postgres=C/postgres,andreyk=C/postgres}"` |
| **spcoptions**  list / elements=string | Tablespace-level options.  **Returned:** success  **Sample:** `["seq_page_cost=1"]` |
| **spcowner**  string | Owner of the tablespace.  **Returned:** success  **Sample:** `"test_user"` |
| **version**  dictionary | Database server version <https://www.postgresql.org/support/versioning/>.  **Returned:** success  **Sample:** `{"version": {"major": 10, "minor": 6}}` |
| **full**  string  *added in community.postgresql 1.2.0* | Full server version.  **Returned:** success  **Sample:** `"13.2"` |
| **major**  integer | Major server version.  **Returned:** success  **Sample:** `11` |
| **minor**  integer | Minor server version.  **Returned:** success  **Sample:** `1` |
| **patch**  integer  *added in community.postgresql 1.2.0* | Patch server version.  **Returned:** if supported  **Sample:** `5` |
| **raw**  string  *added in community.postgresql 1.2.0* | Full output returned by ``SELECT version()``.  **Returned:** success  **Sample:** `"PostgreSQL 13.2 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 10.2.1 20201125 (Red Hat 10.2.1-9), 64-bit"` |

### Authors

- Andrew Klychkov (@Andersson007)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
- [Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
- [Communication](index.md#communication-for-community-postgresql)

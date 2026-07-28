---
collection: ansible
version: "6"
title: "community.postgresql.postgresql_idx module – Create or drop indexes from a PostgreSQL database"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/postgresql/postgresql_idx_module.html
fetched_at: 2026-07-27T17:20:18+00:00
---
# community.postgresql.postgresql_idx module – Create or drop indexes from a PostgreSQL database

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
> see [Requirements](postgresql_idx_module.md#ansible-collections-community-postgresql-postgresql-idx-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_idx`.

- [Synopsis](postgresql_idx_module.md#synopsis)
- [Requirements](postgresql_idx_module.md#requirements)
- [Parameters](postgresql_idx_module.md#parameters)
- [Notes](postgresql_idx_module.md#notes)
- [See Also](postgresql_idx_module.md#see-also)
- [Examples](postgresql_idx_module.md#examples)
- [Return Values](postgresql_idx_module.md#return-values)

## [Synopsis](postgresql_idx_module.md#id1)

- Create or drop indexes from a PostgreSQL database.

## [Requirements](postgresql_idx_module.md#id2)

The below requirements are needed on the host that executes this module.

- psycopg2

## [Parameters](postgresql_idx_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_rootcert  string | Specifies the name of a file containing SSL certificate authority (CA) certificate(s).  If the file exists, the server’s certificate will be verified to be signed by one of these authorities. |
| **cascade**  boolean | Automatically drop objects that depend on the index, and in turn all objects that depend on those objects.  It used only with *state=absent*.  Mutually exclusive with *concurrent=true*.  Choices:   - `false` ← (default) - `true` |
| **columns**  aliases: column  list / elements=string | List of index columns that need to be covered by index.  Mutually exclusive with *state=absent*. |
| **concurrent**  boolean | Enable or disable concurrent mode (CREATE / DROP INDEX CONCURRENTLY).  Pay attention, if *concurrent=false*, the table will be locked (ACCESS EXCLUSIVE) during the building process. For more information about the lock levels see <https://www.postgresql.org/docs/current/explicit-locking.html>.  If the building process was interrupted for any reason when *cuncurrent=true*, the index becomes invalid. In this case it should be dropped and created again.  Mutually exclusive with *cascade=true*.  Choices:   - `false` - `true` ← (default) |
| **cond**  string | Index conditions.  Mutually exclusive with *state=absent*. |
| **connect_params**  dictionary  added in community.postgresql 2.3.0 | Any additional parameters to be passed to libpg.  These parameters take precedence.  Default: `{}` |
| **db**  aliases: login_db  string | Name of database to connect to and where the index will be created/dropped. |
| **idxname**  aliases: name  string / required | Name of the index to create or drop. |
| **idxtype**  aliases: type  string | Index type (like btree, gist, gin, etc.).  Mutually exclusive with *state=absent*. |
| **login_host**  string | Host running the database.  If you have connection issues when using `localhost`, try to use `127.0.0.1` instead.  Default: `""` |
| **login_password**  string | The password this module should use to establish its PostgreSQL session.  Default: `""` |
| **login_unix_socket**  string | Path to a Unix domain socket for local connections.  Default: `""` |
| **login_user**  string | The username this module should use to establish its PostgreSQL session.  Default: `"postgres"` |
| **port**  aliases: login_port  integer | Database port to connect to.  Default: `5432` |
| **schema**  string | Name of a database schema where the index will be created. |
| **session_role**  string | Switch to session_role after connecting. The specified session_role must be a role that the current login_user is a member of.  Permissions checking for SQL commands is carried out as though the session_role were the one that had logged in originally. |
| **ssl_mode**  string | Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.  See <https://www.postgresql.org/docs/current/static/libpq-ssl.html> for more information on the modes.  Default of `prefer` matches libpq default.  Choices:   - `"allow"` - `"disable"` - `"prefer"` ← (default) - `"require"` - `"verify-ca"` - `"verify-full"` |
| **state**  string | Index state.  `present` implies the index will be created if it does not exist.  `absent` implies the index will be dropped if it exists.  Choices:   - `"absent"` - `"present"` ← (default) |
| **storage_params**  list / elements=string | Storage parameters like fillfactor, vacuum_cleanup_index_scale_factor, etc.  Mutually exclusive with *state=absent*. |
| **table**  string | Table to create index on it.  Mutually exclusive with *state=absent*. |
| **tablespace**  string | Set a tablespace for the index.  Mutually exclusive with *state=absent*. |
| **trust_input**  boolean  added in community.postgresql 0.2.0 | If `false`, check whether values of parameters *idxname*, *session_role*, *schema*, *table*, *columns*, *tablespace*, *storage_params*, *cond* are potentially dangerous.  It makes sense to use `false` only when SQL injections via the parameters are possible.  Choices:   - `false` - `true` ← (default) |
| **unique**  boolean  added in community.postgresql 0.2.0 | Enable unique index.  Only btree currently supports unique indexes.  Choices:   - `false` ← (default) - `true` |

## [Notes](postgresql_idx_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.
> - The index building process can affect database performance.
> - To avoid table locks on production databases, use *concurrent=true* (default behavior).
> - The default authentication assumes that you are either logging in as or sudo’ing to the `postgres` account on the host.
> - To avoid “Peer authentication failed for user postgres” error, use postgres user as a *become_user*.
> - This module uses psycopg2, a Python PostgreSQL database adapter. You must ensure that psycopg2 is installed on the host before using this module.
> - If the remote host is the PostgreSQL server (which is the default case), then PostgreSQL must also be installed on the remote host.
> - For Ubuntu-based systems, install the postgresql, libpq-dev, and python-psycopg2 packages on the remote host before using this module.
> - The ca_cert parameter requires at least Postgres version 8.4 and *psycopg2* version 2.4.3.

## [See Also](postgresql_idx_module.md#id5)

> **See also:**
>
> [community.postgresql.postgresql_table](postgresql_table_module.md#ansible-collections-community-postgresql-postgresql-table-module)
> :   Create, drop, or modify a PostgreSQL table.
>
> [community.postgresql.postgresql_tablespace](postgresql_tablespace_module.md#ansible-collections-community-postgresql-postgresql-tablespace-module)
> :   Add or remove PostgreSQL tablespaces from remote hosts.
>
> [PostgreSQL indexes reference](https://www.postgresql.org/docs/current/indexes.html)
> :   General information about PostgreSQL indexes.
>
> [CREATE INDEX reference](https://www.postgresql.org/docs/current/sql-createindex.html)
> :   Complete reference of the CREATE INDEX command documentation.
>
> [ALTER INDEX reference](https://www.postgresql.org/docs/current/sql-alterindex.html)
> :   Complete reference of the ALTER INDEX command documentation.
>
> [DROP INDEX reference](https://www.postgresql.org/docs/current/sql-dropindex.html)
> :   Complete reference of the DROP INDEX command documentation.

## [Examples](postgresql_idx_module.md#id6)

```yaml+jinja
- name: Create btree index if not exists test_idx concurrently covering columns id and name of table products
  community.postgresql.postgresql_idx:
    db: acme
    table: products
    columns: id,name
    name: test_idx

- name: Create btree index test_idx concurrently with tablespace called ssd and storage parameter
  community.postgresql.postgresql_idx:
    db: acme
    table: products
    columns:
    - id
    - name
    idxname: test_idx
    tablespace: ssd
    storage_params:
    - fillfactor=90

- name: Create gist index test_gist_idx concurrently on column geo_data of table map
  community.postgresql.postgresql_idx:
    db: somedb
    table: map
    idxtype: gist
    columns: geo_data
    idxname: test_gist_idx

# Note: for the example below pg_trgm extension must be installed for gin_trgm_ops
- name: Create gin index gin0_idx not concurrently on column comment of table test
  community.postgresql.postgresql_idx:
    idxname: gin0_idx
    table: test
    columns: comment gin_trgm_ops
    concurrent: false
    idxtype: gin

- name: Drop btree test_idx concurrently
  community.postgresql.postgresql_idx:
    db: mydb
    idxname: test_idx
    state: absent

- name: Drop test_idx cascade
  community.postgresql.postgresql_idx:
    db: mydb
    idxname: test_idx
    state: absent
    cascade: true
    concurrent: false

- name: Create btree index test_idx concurrently on columns id,comment where column id > 1
  community.postgresql.postgresql_idx:
    db: mydb
    table: test
    columns: id,comment
    idxname: test_idx
    cond: id > 1

- name: Create unique btree index if not exists test_unique_idx on column name of table products
  community.postgresql.postgresql_idx:
    db: acme
    table: products
    columns: name
    name: test_unique_idx
    unique: true
    concurrent: false
```

## [Return Values](postgresql_idx_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **name**  string | Index name.  Returned: always  Sample: `"foo_idx"` |
| **query**  string | Query that was tried to be executed.  Returned: always  Sample: `"CREATE INDEX CONCURRENTLY foo_idx ON test_table USING BTREE (id)"` |
| **schema**  string | Schema where index exists.  Returned: always  Sample: `"public"` |
| **state**  string | Index state.  Returned: always  Sample: `"present"` |
| **storage_params**  list / elements=string | Index storage parameters.  Returned: always  Sample: `["fillfactor=90"]` |
| **tablespace**  string | Tablespace where index exists.  Returned: always  Sample: `"ssd"` |
| **valid**  boolean | Index validity.  Returned: always  Sample: `true` |

### Authors

- Andrew Klychkov (@Andersson007)
- Thomas O’Donnell (@andytom)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
[Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
[Communication](index.md#communication-for-community-postgresql)

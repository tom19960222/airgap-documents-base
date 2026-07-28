---
collection: ansible
version: "6"
title: "community.mysql.mysql_db module – Add or remove MySQL databases from a remote host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mysql/mysql_db_module.html
fetched_at: 2026-07-27T17:16:15+00:00
---
# community.mysql.mysql_db module – Add or remove MySQL databases from a remote host

> **Note:**
>
> This module is part of the [community.mysql collection](https://galaxy.ansible.com/community/mysql) (version 3.5.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.mysql`.
> You need further requirements to be able to use this module,
> see [Requirements](mysql_db_module.md#ansible-collections-community-mysql-mysql-db-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mysql.mysql_db`.

- [Synopsis](mysql_db_module.md#synopsis)
- [Requirements](mysql_db_module.md#requirements)
- [Parameters](mysql_db_module.md#parameters)
- [Notes](mysql_db_module.md#notes)
- [See Also](mysql_db_module.md#see-also)
- [Examples](mysql_db_module.md#examples)
- [Return Values](mysql_db_module.md#return-values)

## [Synopsis](mysql_db_module.md#id1)

- Add or remove MySQL databases from a remote host.

## [Requirements](mysql_db_module.md#id2)

The below requirements are needed on the host that executes this module.

- MySQLdb (Python 2.x)
- PyMySQL (Python 2.7 and Python 3.x) or
- mysql (command line binary)
- mysqlclient (Python 3.5+) or
- mysqldump (command line binary)

## [Parameters](mysql_db_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_ca  path | The path to a Certificate Authority (CA) certificate. This option, if used, must specify the same certificate as used by the server. |
| **chdir**  path  added in community.mysql 3.4.0 | Changes the current working directory.  Can be useful, for example, when *state=import* and a dump file contains relative paths. |
| **check_hostname**  boolean  added in community.mysql 1.1.0 | Whether to validate the server host name when an SSL connection is required. Corresponds to MySQL CLIs `--ssl` switch.  Setting this to `false` disables hostname verification. Use with caution.  Requires pymysql >= 0.7.11.  This option has no effect on MySQLdb.  Choices:   - `false` - `true` |
| **check_implicit_admin**  boolean  added in community.mysql 0.1.0 | Check if mysql allows login as root/nopassword before trying supplied credentials.  If success, passed *login_user*/*login_password* will be ignored.  Choices:   - `false` ← (default) - `true` |
| **client_cert**  aliases: ssl_cert  path | The path to a client public key certificate. |
| **client_key**  aliases: ssl_key  path | The path to the client private key. |
| **collation**  string | Collation mode (sorting). This only applies to new table/databases and does not update existing ones, this is a limitation of MySQL.  Default: `""` |
| **config_file**  path | Specify a config file from which user and password are to be read.  The default config file, `~/.my.cnf`, if it exists, will be read, even if *config_file* is not specified.  The default config file, `~/.my.cnf`, if it exists, must contain a `[client]` section as a MySQL connector requirement.  To prevent the default config file from being read, set *config_file* to be an empty string.  Default: `"~/.my.cnf"` |
| **config_overrides_defaults**  boolean  added in community.mysql 0.1.0 | If `yes`, connection parameters from *config_file* will override the default values of *login_host* and *login_port* parameters.  Used when *stat* is `present` or `absent`, ignored otherwise.  It needs Python 3.5+ as the default interpreter on a target host.  Choices:   - `false` ← (default) - `true` |
| **connect_timeout**  integer | The connection timeout when connecting to the MySQL server.  Default: `30` |
| **dump_extra_args**  string  added in community.mysql 0.1.0 | Provide additional arguments for mysqldump. Used when *state=dump* only, ignored otherwise. |
| **encoding**  string | Encoding mode to use, examples include `utf8` or `latin1_swedish_ci`, at creation of database, dump or importation of sql script.  Default: `""` |
| **force**  boolean  added in community.mysql 0.1.0 | Continue dump or import even if we get an SQL error.  Used only when *state* is `dump` or `import`.  Choices:   - `false` ← (default) - `true` |
| **hex_blob**  boolean  added in community.mysql 0.1.0 | Dump binary columns using hexadecimal notation.  Choices:   - `false` ← (default) - `true` |
| **ignore_tables**  list / elements=string | A list of table names that will be ignored in the dump of the form database_name.table_name.  Default: `[]` |
| **login_host**  string | Host running the database.  In some cases for local connections the *login_unix_socket=/path/to/mysqld/socket*, that is usually `/var/run/mysqld/mysqld.sock`, needs to be used instead of *login_host=localhost*.  Default: `"localhost"` |
| **login_password**  string | The password used to authenticate with. |
| **login_port**  integer | Port of the MySQL server. Requires *login_host* be defined as other than localhost if login_port is used.  Default: `3306` |
| **login_unix_socket**  string | The path to a Unix domain socket for local connections.  Use this parameter to avoid the `Please explicitly state intended protocol` error. |
| **login_user**  string | The username used to authenticate with. |
| **master_data**  integer  added in community.mysql 0.1.0 | Option to dump a master replication server to produce a dump file that can be used to set up another server as a slave of the master.  `0` to not include master data.  `1` to generate a ‘CHANGE MASTER TO’ statement required on the slave to start the replication process.  `2` to generate a commented ‘CHANGE MASTER TO’.  Can be used when *state=dump*.  Choices:   - `0` ← (default) - `1` - `2` |
| **name**  aliases: db  list / elements=string / required | Name of the database to add or remove.  *name=all* may only be provided if *state* is `dump` or `import`.  List of databases is provided with *state=dump*, *state=present* and *state=absent*.  If *name=all* it works like –all-databases option for mysqldump (Added in 2.0). |
| **pipefail**  boolean  added in community.mysql 3.4.0 | Use `bash` instead of `sh` and add `-o pipefail` to catch errors from the mysql_dump command when *state=import* and compression is used.  The default is `no` to prevent issues on systems without bash as a default interpreter.  The default will change to `yes` in community.mysql 4.0.0.  Choices:   - `false` ← (default) - `true` |
| **quick**  boolean | Option used for dumping large tables.  Choices:   - `false` - `true` ← (default) |
| **restrict_config_file**  boolean  added in community.mysql 0.1.0 | Read only passed *config_file*.  When *state* is `dump` or `import`, by default the module passes *config_file* parameter using `--defaults-extra-file` command-line argument to `mysql/mysqldump` utilities under the hood that read named option file in addition to usual option files.  If this behavior is undesirable, use `yes` to read only named option file.  Choices:   - `false` ← (default) - `true` |
| **single_transaction**  boolean | Execute the dump in a single transaction.  Choices:   - `false` ← (default) - `true` |
| **skip_lock_tables**  boolean  added in community.mysql 0.1.0 | Skip locking tables for read. Used when *state=dump*, ignored otherwise.  Choices:   - `false` ← (default) - `true` |
| **state**  string | The database state.  Choices:   - `"absent"` - `"dump"` - `"import"` - `"present"` ← (default) |
| **target**  path | Location, on the remote host, of the dump file to read from or write to.  Uncompressed SQL files (`.sql`) as well as bzip2 (`.bz2`), gzip (`.gz`) and xz (Added in 2.0) compressed files are supported. |
| **unsafe_login_password**  boolean  added in community.mysql 0.1.0 | If `no`, the module will safely use a shell-escaped version of the *login_password* value.  It makes sense to use `yes` only if there are special symbols in the value and errors `Access denied` occur.  Used only when *state* is `import` or `dump` and *login_password* is passed, ignored otherwise.  Choices:   - `false` ← (default) - `true` |
| **use_shell**  boolean  added in community.mysql 0.1.0 | Used to prevent `Broken pipe` errors when the imported *target* file is compressed.  If `yes`, the module will internally execute commands via a shell.  Used when *state=import*, ignored otherwise.  Choices:   - `false` ← (default) - `true` |

## [Notes](mysql_db_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.
> - Requires the mysql and mysqldump binaries on the remote host.
> - This module is **not idempotent** when *state* is `import`, and will import the dump file each time if run more than once.
> - To avoid the `Please explicitly state intended protocol` error, use the *login_unix_socket* argument, for example, `login_unix_socket: /run/mysqld/mysqld.sock`.
> - Requires the PyMySQL (Python 2.7 and Python 3.X) or MySQL-python (Python 2.X) package installed on the remote host. The Python package may be installed with apt-get install python-pymysql (Ubuntu; see [ansible.builtin.apt](../../ansible/builtin/apt_module.md#ansible-collections-ansible-builtin-apt-module)) or yum install python2-PyMySQL (RHEL/CentOS/Fedora; see [ansible.builtin.yum](../../ansible/builtin/yum_module.md#ansible-collections-ansible-builtin-yum-module)). You can also use dnf install python2-PyMySQL for newer versions of Fedora; see [ansible.builtin.dnf](../../ansible/builtin/dnf_module.md#ansible-collections-ansible-builtin-dnf-module).
> - Be sure you have mysqlclient, PyMySQL, or MySQLdb library installed on the target machine for the Python interpreter Ansible discovers. For example if ansible discovers and uses Python 3, you need to install the Python 3 version of PyMySQL or mysqlclient. If ansible discovers and uses Python 2, you need to install the Python 2 version of either PyMySQL or MySQL-python.
> - If you have trouble, it may help to force Ansible to use the Python interpreter you need by specifying `ansible_python_interpreter`. For more information, see <https://docs.ansible.com/ansible/latest/reference_appendices/interpreter_discovery.html>.
> - Both `login_password` and `login_user` are required when you are passing credentials. If none are present, the module will attempt to read the credentials from `~/.my.cnf`, and finally fall back to using the MySQL default login of ‘root’ with no password.
> - If there are problems with local connections, using *login_unix_socket=/path/to/mysqld/socket* instead of *login_host=localhost* might help. As an example, the default MariaDB installation of version 10.4 and later uses the unix_socket authentication plugin by default that without using *login_unix_socket=/var/run/mysqld/mysqld.sock* (the default path) causes the error ``Host ‘127.0.0.1’ is not allowed to connect to this MariaDB server``.
> - Alternatively, you can use the mysqlclient library instead of MySQL-python (MySQLdb) which supports both Python 2.X and Python >=3.5. See <https://pypi.org/project/mysqlclient/> how to install it.
> - If credentials from the config file (for example, `/root/.my.cnf`) are not needed to connect to a database server, but the file exists and does not contain a `[client]` section, before any other valid directives, it will be read and this will cause the connection to fail, to prevent this set it to an empty string, (for example `config_file: ''`).

## [See Also](mysql_db_module.md#id5)

> **See also:**
>
> [community.mysql.mysql_info](mysql_info_module.md#ansible-collections-community-mysql-mysql-info-module)
> :   Gather information about MySQL servers.
>
> [community.mysql.mysql_variables](mysql_variables_module.md#ansible-collections-community-mysql-mysql-variables-module)
> :   Manage MySQL global variables.
>
> [community.mysql.mysql_user](mysql_user_module.md#ansible-collections-community-mysql-mysql-user-module)
> :   Adds or removes a user from a MySQL database.
>
> [community.mysql.mysql_replication](mysql_replication_module.md#ansible-collections-community-mysql-mysql-replication-module)
> :   Manage MySQL replication.
>
> [MySQL command-line client reference](https://dev.mysql.com/doc/refman/8.0/en/mysql.html)
> :   Complete reference of the MySQL command-line client documentation.
>
> [mysqldump reference](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)
> :   Complete reference of the ``mysqldump`` client utility documentation.
>
> [CREATE DATABASE reference](https://dev.mysql.com/doc/refman/8.0/en/create-database.html)
> :   Complete reference of the CREATE DATABASE command documentation.
>
> [DROP DATABASE reference](https://dev.mysql.com/doc/refman/8.0/en/drop-database.html)
> :   Complete reference of the DROP DATABASE command documentation.

## [Examples](mysql_db_module.md#id6)

```yaml+jinja
# If you encounter the "Please explicitly state intended protocol" error,
# use the login_unix_socket argument
- name: Create a new database with name 'bobdata'
  community.mysql.mysql_db:
    name: bobdata
    state: present
    login_unix_socket: /run/mysqld/mysqld.sock

- name: Create new databases with names 'foo' and 'bar'
  community.mysql.mysql_db:
    name:
      - foo
      - bar
    state: present

# Copy database dump file to remote host and restore it to database 'my_db'
- name: Copy database dump file
  copy:
    src: dump.sql.bz2
    dest: /tmp

- name: Restore database
  community.mysql.mysql_db:
    name: my_db
    state: import
    target: /tmp/dump.sql.bz2

- name: Restore database ignoring errors
  community.mysql.mysql_db:
    name: my_db
    state: import
    target: /tmp/dump.sql.bz2
    force: yes

- name: Dump multiple databases
  community.mysql.mysql_db:
    state: dump
    name: db_1,db_2
    target: /tmp/dump.sql

- name: Dump multiple databases
  community.mysql.mysql_db:
    state: dump
    name:
      - db_1
      - db_2
    target: /tmp/dump.sql

- name: Dump all databases to hostname.sql
  community.mysql.mysql_db:
    state: dump
    name: all
    target: /tmp/dump.sql

- name: Dump all databases to hostname.sql including master data
  community.mysql.mysql_db:
    state: dump
    name: all
    target: /tmp/dump.sql
    master_data: 1

# Import of sql script with encoding option
- name: >
    Import dump.sql with specific latin1 encoding,
    similar to mysql -u <username> --default-character-set=latin1 -p <password> < dump.sql
  community.mysql.mysql_db:
    state: import
    name: all
    encoding: latin1
    target: /tmp/dump.sql

# Dump of database with encoding option
- name: >
    Dump of Databse with specific latin1 encoding,
    similar to mysqldump -u <username> --default-character-set=latin1 -p <password> <database>
  community.mysql.mysql_db:
    state: dump
    name: db_1
    encoding: latin1
    target: /tmp/dump.sql

- name: Delete database with name 'bobdata'
  community.mysql.mysql_db:
    name: bobdata
    state: absent

- name: Make sure there is neither a database with name 'foo', nor one with name 'bar'
  community.mysql.mysql_db:
    name:
      - foo
      - bar
    state: absent

# Dump database with argument not directly supported by this module
# using dump_extra_args parameter
- name: Dump databases without including triggers
  community.mysql.mysql_db:
    state: dump
    name: foo
    target: /tmp/dump.sql
    dump_extra_args: --skip-triggers

- name: Try to create database as root/nopassword first. If not allowed, pass the credentials
  community.mysql.mysql_db:
    check_implicit_admin: yes
    login_user: bob
    login_password: 123456
    name: bobdata
    state: present

- name: Dump a database with compression and catch errors from mysqldump with bash pipefail
  community.mysql.mysql_db:
    state: dump
    name: foo
    target: /tmp/dump.sql.gz
    pipefail: true
```

## [Return Values](mysql_db_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **db**  string | Database names in string format delimited by white space.  Returned: always  Sample: `"foo bar"` |
| **db_list**  list / elements=string | List of database names.  Returned: always  Sample: `["foo", "bar"]` |
| **executed_commands**  list / elements=string  added in community.mysql 0.1.0 | List of commands which tried to run.  Returned: if executed  Sample: `["CREATE DATABASE acme"]` |

### Authors

- Ansible Core Team

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mysql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.mysql)

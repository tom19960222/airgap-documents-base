---
collection: ansible
version: "6"
title: "community.mysql.mysql_query module – Run MySQL queries"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mysql/mysql_query_module.html
fetched_at: 2026-07-27T17:16:16+00:00
---
# community.mysql.mysql_query module – Run MySQL queries

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
> see [Requirements](mysql_query_module.md#ansible-collections-community-mysql-mysql-query-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mysql.mysql_query`.

New in community.mysql 0.1.0

- [Synopsis](mysql_query_module.md#synopsis)
- [Requirements](mysql_query_module.md#requirements)
- [Parameters](mysql_query_module.md#parameters)
- [Notes](mysql_query_module.md#notes)
- [See Also](mysql_query_module.md#see-also)
- [Examples](mysql_query_module.md#examples)
- [Return Values](mysql_query_module.md#return-values)

## [Synopsis](mysql_query_module.md#id1)

- Runs arbitrary MySQL queries.
- Pay attention, the module does not support check mode! All queries will be executed in autocommit mode.
- To run SQL queries from a file, use [community.mysql.mysql_db](mysql_db_module.md#ansible-collections-community-mysql-mysql-db-module) module.

## [Requirements](mysql_query_module.md#id2)

The below requirements are needed on the host that executes this module.

- mysqlclient (Python 3.5+) or
- PyMySQL (Python 2.7 and Python 3.x) or
- MySQLdb (Python 2.x)

## [Parameters](mysql_query_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_ca  path | The path to a Certificate Authority (CA) certificate. This option, if used, must specify the same certificate as used by the server. |
| **check_hostname**  boolean  added in community.mysql 1.1.0 | Whether to validate the server host name when an SSL connection is required. Corresponds to MySQL CLIs `--ssl` switch.  Setting this to `false` disables hostname verification. Use with caution.  Requires pymysql >= 0.7.11.  This option has no effect on MySQLdb.  Choices:   - `false` - `true` |
| **client_cert**  aliases: ssl_cert  path | The path to a client public key certificate. |
| **client_key**  aliases: ssl_key  path | The path to the client private key. |
| **config_file**  path | Specify a config file from which user and password are to be read.  The default config file, `~/.my.cnf`, if it exists, will be read, even if *config_file* is not specified.  The default config file, `~/.my.cnf`, if it exists, must contain a `[client]` section as a MySQL connector requirement.  To prevent the default config file from being read, set *config_file* to be an empty string.  Default: `"~/.my.cnf"` |
| **connect_timeout**  integer | The connection timeout when connecting to the MySQL server.  Default: `30` |
| **login_db**  string | Name of database to connect to and run queries against. |
| **login_host**  string | Host running the database.  In some cases for local connections the *login_unix_socket=/path/to/mysqld/socket*, that is usually `/var/run/mysqld/mysqld.sock`, needs to be used instead of *login_host=localhost*.  Default: `"localhost"` |
| **login_password**  string | The password used to authenticate with. |
| **login_port**  integer | Port of the MySQL server. Requires *login_host* be defined as other than localhost if login_port is used.  Default: `3306` |
| **login_unix_socket**  string | The path to a Unix domain socket for local connections.  Use this parameter to avoid the `Please explicitly state intended protocol` error. |
| **login_user**  string | The username used to authenticate with. |
| **named_args**  dictionary | Dictionary of key-value arguments to pass to the query.  Mutually exclusive with *positional_args*. |
| **positional_args**  list / elements=string | List of values to be passed as positional arguments to the query.  Mutually exclusive with *named_args*. |
| **query**  any / required | SQL query to run. Multiple queries can be passed using YAML list syntax.  Must be a string or YAML list containing strings.  Note that if you use the `IF EXISTS/IF NOT EXISTS` clauses in your query and `mysqlclient` connector, the module will report that the state has been changed even if it has not. If it is important in your workflow, use the `PyMySQL` connector instead. |
| **single_transaction**  boolean | Where passed queries run in a single transaction (`yes`) or commit them one-by-one (`no`).  Choices:   - `false` ← (default) - `true` |

## [Notes](mysql_query_module.md#id4)

> **Note:**
>
> - To avoid the `Please explicitly state intended protocol` error, use the *login_unix_socket* argument, for example, `login_unix_socket: /run/mysqld/mysqld.sock`.
> - Requires the PyMySQL (Python 2.7 and Python 3.X) or MySQL-python (Python 2.X) package installed on the remote host. The Python package may be installed with apt-get install python-pymysql (Ubuntu; see [ansible.builtin.apt](../../ansible/builtin/apt_module.md#ansible-collections-ansible-builtin-apt-module)) or yum install python2-PyMySQL (RHEL/CentOS/Fedora; see [ansible.builtin.yum](../../ansible/builtin/yum_module.md#ansible-collections-ansible-builtin-yum-module)). You can also use dnf install python2-PyMySQL for newer versions of Fedora; see [ansible.builtin.dnf](../../ansible/builtin/dnf_module.md#ansible-collections-ansible-builtin-dnf-module).
> - Be sure you have mysqlclient, PyMySQL, or MySQLdb library installed on the target machine for the Python interpreter Ansible discovers. For example if ansible discovers and uses Python 3, you need to install the Python 3 version of PyMySQL or mysqlclient. If ansible discovers and uses Python 2, you need to install the Python 2 version of either PyMySQL or MySQL-python.
> - If you have trouble, it may help to force Ansible to use the Python interpreter you need by specifying `ansible_python_interpreter`. For more information, see <https://docs.ansible.com/ansible/latest/reference_appendices/interpreter_discovery.html>.
> - Both `login_password` and `login_user` are required when you are passing credentials. If none are present, the module will attempt to read the credentials from `~/.my.cnf`, and finally fall back to using the MySQL default login of ‘root’ with no password.
> - If there are problems with local connections, using *login_unix_socket=/path/to/mysqld/socket* instead of *login_host=localhost* might help. As an example, the default MariaDB installation of version 10.4 and later uses the unix_socket authentication plugin by default that without using *login_unix_socket=/var/run/mysqld/mysqld.sock* (the default path) causes the error ``Host ‘127.0.0.1’ is not allowed to connect to this MariaDB server``.
> - Alternatively, you can use the mysqlclient library instead of MySQL-python (MySQLdb) which supports both Python 2.X and Python >=3.5. See <https://pypi.org/project/mysqlclient/> how to install it.
> - If credentials from the config file (for example, `/root/.my.cnf`) are not needed to connect to a database server, but the file exists and does not contain a `[client]` section, before any other valid directives, it will be read and this will cause the connection to fail, to prevent this set it to an empty string, (for example `config_file: ''`).

## [See Also](mysql_query_module.md#id5)

> **See also:**
>
> [community.mysql.mysql_db](mysql_db_module.md#ansible-collections-community-mysql-mysql-db-module)
> :   Add or remove MySQL databases from a remote host.

## [Examples](mysql_query_module.md#id6)

```yaml+jinja
# If you encounter the "Please explicitly state intended protocol" error,
# use the login_unix_socket argument
- name: Simple select query to acme db
  community.mysql.mysql_query:
    login_db: acme
    query: SELECT * FROM orders
    login_unix_socket: /run/mysqld/mysqld.sock

- name: Select query to db acme with positional arguments
  community.mysql.mysql_query:
    login_db: acme
    query: SELECT * FROM acme WHERE id = %s AND story = %s
    positional_args:
    - 1
    - test

- name: Select query to test_db with named_args
  community.mysql.mysql_query:
    login_db: test_db
    query: SELECT * FROM test WHERE id = %(id_val)s AND story = %(story_val)s
    named_args:
      id_val: 1
      story_val: test

- name: Run several insert queries against db test_db in single transaction
  community.mysql.mysql_query:
    login_db: test_db
    query:
    - INSERT INTO articles (id, story) VALUES (2, 'my_long_story')
    - INSERT INTO prices (id, price) VALUES (123, '100.00')
    single_transaction: yes
```

## [Return Values](mysql_query_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **executed_queries**  list / elements=string | List of executed queries.  Returned: always  Sample: `["SELECT * FROM bar", "UPDATE bar SET id = 1 WHERE id = 2"]` |
| **query_result**  list / elements=string | List of lists (sublist for each query) containing dictionaries in column:value form representing returned rows.  Returned: changed  Sample: `[[{"Column": "Value1"}, {"Column": "Value2"}], [{"ID": 1}, {"ID": 2}]]` |
| **rowcount**  list / elements=string | Number of affected rows for each subquery.  Returned: changed  Sample: `[5, 1]` |

### Authors

- Andrew Klychkov (@Andersson007)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mysql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.mysql)

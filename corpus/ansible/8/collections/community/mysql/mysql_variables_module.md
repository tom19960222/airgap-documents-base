---
collection: ansible
version: "8"
title: "community.mysql.mysql_variables module – Manage MySQL global variables"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/mysql/mysql_variables_module.html
fetched_at: 2026-07-28T01:54:13+00:00
---
# community.mysql.mysql_variables module – Manage MySQL global variables

> **Note:**
>
> This module is part of the [community.mysql collection](https://galaxy.ansible.com/ui/repo/published/community/mysql/) (version 3.8.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.mysql`.
> You need further requirements to be able to use this module,
> see [Requirements](mysql_variables_module.md#ansible-collections-community-mysql-mysql-variables-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mysql.mysql_variables`.

- [Synopsis](mysql_variables_module.md#synopsis)
- [Requirements](mysql_variables_module.md#requirements)
- [Parameters](mysql_variables_module.md#parameters)
- [Attributes](mysql_variables_module.md#attributes)
- [Notes](mysql_variables_module.md#notes)
- [See Also](mysql_variables_module.md#see-also)
- [Examples](mysql_variables_module.md#examples)
- [Return Values](mysql_variables_module.md#return-values)

## [Synopsis](mysql_variables_module.md#id1)

- Query / Set MySQL variables.

## [Requirements](mysql_variables_module.md#id2)

The below requirements are needed on the host that executes this module.

- mysqlclient (Python 3.5+) or
- PyMySQL (Python 2.7 and Python 3.x) or
- MySQLdb (Python 2.x)

## [Parameters](mysql_variables_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_ca  path | The path to a Certificate Authority (CA) certificate. This option, if used, must specify the same certificate as used by the server. |
| **check_hostname**  boolean  *added in community.mysql 1.1.0* | Whether to validate the server host name when an SSL connection is required. Corresponds to MySQL CLIs `--ssl` switch.  Setting this to `false` disables hostname verification. Use with caution.  Requires pymysql >= 0.7.11.  This option has no effect on MySQLdb.  **Choices:**   - `false` - `true` |
| **client_cert**  aliases: ssl_cert  path | The path to a client public key certificate. |
| **client_key**  aliases: ssl_key  path | The path to the client private key. |
| **config_file**  path | Specify a config file from which user and password are to be read.  The default config file, `~/.my.cnf`, if it exists, will be read, even if *config_file* is not specified.  The default config file, `~/.my.cnf`, if it exists, must contain a `[client]` section as a MySQL connector requirement.  To prevent the default config file from being read, set *config_file* to be an empty string.  **Default:** `"~/.my.cnf"` |
| **connect_timeout**  integer | The connection timeout when connecting to the MySQL server.  **Default:** `30` |
| **login_host**  string | Host running the database.  In some cases for local connections the *login_unix_socket=/path/to/mysqld/socket*, that is usually `/var/run/mysqld/mysqld.sock`, needs to be used instead of *login_host=localhost*.  **Default:** `"localhost"` |
| **login_password**  string | The password used to authenticate with. |
| **login_port**  integer | Port of the MySQL server. Requires *login_host* be defined as other than localhost if login_port is used.  **Default:** `3306` |
| **login_unix_socket**  string | The path to a Unix domain socket for local connections.  Use this parameter to avoid the `Please explicitly state intended protocol` error. |
| **login_user**  string | The username used to authenticate with. |
| **mode**  string  *added in community.mysql 0.1.0* | `global` assigns `value` to a global system variable which will be changed at runtime but won’t persist across server restarts.  `persist` assigns `value` to a global system variable and persists it to the mysqld-auto.cnf option file in the data directory (the variable will survive service restarts).  `persist_only` persists `value` to the mysqld-auto.cnf option file in the data directory but without setting the global variable runtime value (the value will be changed after the next service restart).  Supported by MySQL 8.0 or later.  For more information see <https://dev.mysql.com/doc/refman/8.0/en/set-variable.html>.  **Choices:**   - `"global"` ← (default) - `"persist"` - `"persist_only"` |
| **value**  string | If set, then sets variable value to this. |
| **variable**  string / required | Variable name to operate. |

## [Attributes](mysql_variables_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](mysql_variables_module.md#id5)

> **Note:**
>
> - Requires the PyMySQL (Python 2.7 and Python 3.X) or MySQL-python (Python 2.X) package installed on the remote host. The Python package may be installed with apt-get install python-pymysql (Ubuntu; see [ansible.builtin.apt](../../ansible/builtin/apt_module.md#ansible-collections-ansible-builtin-apt-module)) or yum install python2-PyMySQL (RHEL/CentOS/Fedora; see [ansible.builtin.yum](../../ansible/builtin/yum_module.md#ansible-collections-ansible-builtin-yum-module)). You can also use dnf install python2-PyMySQL for newer versions of Fedora; see [ansible.builtin.dnf](../../ansible/builtin/dnf_module.md#ansible-collections-ansible-builtin-dnf-module).
> - Be sure you have mysqlclient, PyMySQL, or MySQLdb library installed on the target machine for the Python interpreter Ansible discovers. For example if ansible discovers and uses Python 3, you need to install the Python 3 version of PyMySQL or mysqlclient. If ansible discovers and uses Python 2, you need to install the Python 2 version of either PyMySQL or MySQL-python.
> - If you have trouble, it may help to force Ansible to use the Python interpreter you need by specifying `ansible_python_interpreter`. For more information, see <https://docs.ansible.com/ansible/latest/reference_appendices/interpreter_discovery.html>.
> - Both `login_password` and `login_user` are required when you are passing credentials. If none are present, the module will attempt to read the credentials from `~/.my.cnf`, and finally fall back to using the MySQL default login of ‘root’ with no password.
> - If there are problems with local connections, using *login_unix_socket=/path/to/mysqld/socket* instead of *login_host=localhost* might help. As an example, the default MariaDB installation of version 10.4 and later uses the unix_socket authentication plugin by default that without using *login_unix_socket=/var/run/mysqld/mysqld.sock* (the default path) causes the error ``Host ‘127.0.0.1’ is not allowed to connect to this MariaDB server``.
> - Alternatively, you can use the mysqlclient library instead of MySQL-python (MySQLdb) which supports both Python 2.X and Python >=3.5. See <https://pypi.org/project/mysqlclient/> how to install it.
> - If credentials from the config file (for example, `/root/.my.cnf`) are not needed to connect to a database server, but the file exists and does not contain a `[client]` section, before any other valid directives, it will be read and this will cause the connection to fail, to prevent this set it to an empty string, (for example `config_file: ''`).
> - To avoid the `Please explicitly state intended protocol` error, use the *login_unix_socket* argument, for example, `login_unix_socket: /run/mysqld/mysqld.sock`.
> - Alternatively, to avoid using *login_unix_socket* argument on each invocation you can specify the socket path using the `socket` option in your MySQL config file (usually `~/.my.cnf`) on the destination host, for example `socket=/var/lib/mysql/mysql.sock`.

## [See Also](mysql_variables_module.md#id6)

> **See also:**
>
> [community.mysql.mysql_info](mysql_info_module.md#ansible-collections-community-mysql-mysql-info-module)
> :   Gather information about MySQL servers.
>
> [MySQL SET command reference](https://dev.mysql.com/doc/refman/8.0/en/set-statement.html)
> :   Complete reference of the MySQL SET command documentation.

## [Examples](mysql_variables_module.md#id7)

```yaml+jinja
# If you encounter the "Please explicitly state intended protocol" error,
# use the login_unix_socket argument
- name: Check for sync_binlog setting
  community.mysql.mysql_variables:
    variable: sync_binlog
    login_unix_socket: /run/mysqld/mysqld.sock

- name: Set read_only variable to 1 persistently
  community.mysql.mysql_variables:
    variable: read_only
    value: 1
    mode: persist
```

## [Return Values](mysql_variables_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **queries**  list / elements=string  *added in community.mysql 0.1.0* | List of executed queries which modified DB’s state.  **Returned:** if executed  **Sample:** `` ["SET GLOBAL `read_only` = 1"] `` |

### Authors

- Balazs Pocze (@banyek)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.mysql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.mysql)

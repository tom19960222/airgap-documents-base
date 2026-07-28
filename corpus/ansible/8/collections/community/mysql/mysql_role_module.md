---
collection: ansible
version: "8"
title: "community.mysql.mysql_role module – Adds, removes, or updates a MySQL role"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/mysql/mysql_role_module.html
fetched_at: 2026-07-28T01:54:12+00:00
---
# community.mysql.mysql_role module – Adds, removes, or updates a MySQL role

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
> see [Requirements](mysql_role_module.md#ansible-collections-community-mysql-mysql-role-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mysql.mysql_role`.

New in community.mysql 2.2.0

- [Synopsis](mysql_role_module.md#synopsis)
- [Requirements](mysql_role_module.md#requirements)
- [Parameters](mysql_role_module.md#parameters)
- [Attributes](mysql_role_module.md#attributes)
- [Notes](mysql_role_module.md#notes)
- [See Also](mysql_role_module.md#see-also)
- [Examples](mysql_role_module.md#examples)

## [Synopsis](mysql_role_module.md#id1)

- Adds, removes, or updates a MySQL role.
- Roles are supported since MySQL 8.0.0 and MariaDB 10.0.5.

## [Requirements](mysql_role_module.md#id2)

The below requirements are needed on the host that executes this module.

- mysqlclient (Python 3.5+) or
- PyMySQL (Python 2.7 and Python 3.x) or
- MySQLdb (Python 2.x)

## [Parameters](mysql_role_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin**  string | Supported by **MariaDB**.  Name of the admin user of the role (the *login_user*, by default). |
| **append_members**  boolean | Add members defined by the *members* option to the existing ones for this role instead of overwriting them.  Mutually exclusive with the *detach_members* and *admin* option.  **Choices:**   - `false` ← (default) - `true` |
| **append_privs**  boolean | Append the privileges defined by the *priv* option to the existing ones for this role instead of overwriting them. Mutually exclusive with *subtract_privs*.  **Choices:**   - `false` ← (default) - `true` |
| **ca_cert**  aliases: ssl_ca  path | The path to a Certificate Authority (CA) certificate. This option, if used, must specify the same certificate as used by the server. |
| **check_hostname**  boolean  *added in community.mysql 1.1.0* | Whether to validate the server host name when an SSL connection is required. Corresponds to MySQL CLIs `--ssl` switch.  Setting this to `false` disables hostname verification. Use with caution.  Requires pymysql >= 0.7.11.  This option has no effect on MySQLdb.  **Choices:**   - `false` - `true` |
| **check_implicit_admin**  boolean | Check if mysql allows login as root/nopassword before trying supplied credentials.  If success, passed *login_user*/*login_password* will be ignored.  **Choices:**   - `false` ← (default) - `true` |
| **client_cert**  aliases: ssl_cert  path | The path to a client public key certificate. |
| **client_key**  aliases: ssl_key  path | The path to the client private key. |
| **column_case_sensitive**  boolean  *added in community.mysql 3.8.0* | The default is `false`.  When `true`, the module will not uppercase the field in the privileges.  When `false`, the field names will be upper-cased. This was the default before this feature was introduced but since MySQL/MariaDB is case sensitive you should set this to `true` in most cases.  **Choices:**   - `false` - `true` |
| **config_file**  path | Specify a config file from which user and password are to be read.  The default config file, `~/.my.cnf`, if it exists, will be read, even if *config_file* is not specified.  The default config file, `~/.my.cnf`, if it exists, must contain a `[client]` section as a MySQL connector requirement.  To prevent the default config file from being read, set *config_file* to be an empty string.  **Default:** `"~/.my.cnf"` |
| **connect_timeout**  integer | The connection timeout when connecting to the MySQL server.  **Default:** `30` |
| **detach_members**  boolean | Detaches members defined by the *members* option from the role instead of overwriting all the current members.  Mutually exclusive with the *append_members* and *admin* option.  **Choices:**   - `false` ← (default) - `true` |
| **login_host**  string | Host running the database.  In some cases for local connections the *login_unix_socket=/path/to/mysqld/socket*, that is usually `/var/run/mysqld/mysqld.sock`, needs to be used instead of *login_host=localhost*.  **Default:** `"localhost"` |
| **login_password**  string | The password used to authenticate with. |
| **login_port**  integer | Port of the MySQL server. Requires *login_host* be defined as other than localhost if login_port is used.  **Default:** `3306` |
| **login_unix_socket**  string | The path to a Unix domain socket for local connections.  Use this parameter to avoid the `Please explicitly state intended protocol` error. |
| **login_user**  string | The username used to authenticate with. |
| **members**  list / elements=string | List of members of the role.  For users, use the format `username@hostname`. Always specify the hostname part explicitly.  For roles, use the format `rolename`.  Mutually exclusive with *admin*. |
| **members_must_exist**  boolean | When `yes`, the module fails if any user in *members* does not exist.  When `no`, users in *members* which don’t exist are simply skipped.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | Name of the role to add or remove. |
| **priv**  any | MySQL privileges string in the format: `db.table:priv1,priv2`.  You can specify multiple privileges by separating each one using a forward slash: `db.table:priv/db.table:priv`.  The format is based on MySQL `GRANT` statement.  Database and table names can be quoted, MySQL-style.  If column privileges are used, the `priv1,priv2` part must be exactly as returned by a `SHOW GRANT` statement. If not followed, the module will always report changes. It includes grouping columns by permission (`SELECT(col1,col2`) instead of `SELECT(col1`,SELECT(col2))).  Can be passed as a dictionary (see the examples).  Supports GRANTs for procedures and functions (see the examples for the [community.mysql.mysql_user](mysql_user_module.md#ansible-collections-community-mysql-mysql-user-module) module). |
| **set_default_role_all**  boolean | Is not supported by MariaDB and is silently ignored when working with MariaDB.  If `yes`, runs **SET DEFAULT ROLE ALL TO** each of the *members* when changed.  If you want to avoid this behavior, set this option to `no` explicitly.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | If `present` and the role does not exist, creates the role.  If `present` and the role exists, does nothing or updates its attributes.  If `absent`, removes the role.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subtract_privs**  boolean  *added in community.mysql 3.2.0* | Revoke the privileges defined by the *priv* option and keep other existing privileges. If set, invalid privileges in *priv* are ignored. Mutually exclusive with *append_privs*.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](mysql_role_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](mysql_role_module.md#id5)

> **Note:**
>
> - Pay attention that the module runs `SET DEFAULT ROLE ALL TO` all the *members* passed by default when the state has changed. If you want to avoid this behavior, set *set_default_role_all* to `no`.
> - Requires the PyMySQL (Python 2.7 and Python 3.X) or MySQL-python (Python 2.X) package installed on the remote host. The Python package may be installed with apt-get install python-pymysql (Ubuntu; see [ansible.builtin.apt](../../ansible/builtin/apt_module.md#ansible-collections-ansible-builtin-apt-module)) or yum install python2-PyMySQL (RHEL/CentOS/Fedora; see [ansible.builtin.yum](../../ansible/builtin/yum_module.md#ansible-collections-ansible-builtin-yum-module)). You can also use dnf install python2-PyMySQL for newer versions of Fedora; see [ansible.builtin.dnf](../../ansible/builtin/dnf_module.md#ansible-collections-ansible-builtin-dnf-module).
> - Be sure you have mysqlclient, PyMySQL, or MySQLdb library installed on the target machine for the Python interpreter Ansible discovers. For example if ansible discovers and uses Python 3, you need to install the Python 3 version of PyMySQL or mysqlclient. If ansible discovers and uses Python 2, you need to install the Python 2 version of either PyMySQL or MySQL-python.
> - If you have trouble, it may help to force Ansible to use the Python interpreter you need by specifying `ansible_python_interpreter`. For more information, see <https://docs.ansible.com/ansible/latest/reference_appendices/interpreter_discovery.html>.
> - Both `login_password` and `login_user` are required when you are passing credentials. If none are present, the module will attempt to read the credentials from `~/.my.cnf`, and finally fall back to using the MySQL default login of ‘root’ with no password.
> - If there are problems with local connections, using *login_unix_socket=/path/to/mysqld/socket* instead of *login_host=localhost* might help. As an example, the default MariaDB installation of version 10.4 and later uses the unix_socket authentication plugin by default that without using *login_unix_socket=/var/run/mysqld/mysqld.sock* (the default path) causes the error ``Host ‘127.0.0.1’ is not allowed to connect to this MariaDB server``.
> - Alternatively, you can use the mysqlclient library instead of MySQL-python (MySQLdb) which supports both Python 2.X and Python >=3.5. See <https://pypi.org/project/mysqlclient/> how to install it.
> - If credentials from the config file (for example, `/root/.my.cnf`) are not needed to connect to a database server, but the file exists and does not contain a `[client]` section, before any other valid directives, it will be read and this will cause the connection to fail, to prevent this set it to an empty string, (for example `config_file: ''`).
> - To avoid the `Please explicitly state intended protocol` error, use the *login_unix_socket* argument, for example, `login_unix_socket: /run/mysqld/mysqld.sock`.
> - Alternatively, to avoid using *login_unix_socket* argument on each invocation you can specify the socket path using the `socket` option in your MySQL config file (usually `~/.my.cnf`) on the destination host, for example `socket=/var/lib/mysql/mysql.sock`.

## [See Also](mysql_role_module.md#id6)

> **See also:**
>
> [community.mysql.mysql_user](mysql_user_module.md#ansible-collections-community-mysql-mysql-user-module)
> :   Adds or removes a user from a MySQL database.
>
> [MySQL role reference](https://dev.mysql.com/doc/refman/8.0/en/create-role.html)
> :   Complete reference of the MySQL role documentation.

## [Examples](mysql_role_module.md#id7)

```yaml+jinja
# If you encounter the "Please explicitly state intended protocol" error,
# use the login_unix_socket argument, for example, login_unix_socket: /run/mysqld/mysqld.sock

# Example of a .my.cnf file content for setting a root password
# [client]
# user=root
# password=n<_665{vS43y
#
# Example of a privileges dictionary passed through the priv option
# priv:
#   'mydb.*': 'INSERT,UPDATE'
#   'anotherdb.*': 'SELECT'
#   'yetanotherdb.*': 'ALL'
#
# You can also use the string format like in the community.mysql.mysql_user module, for example
# mydb.*:INSERT,UPDATE/anotherdb.*:SELECT/yetanotherdb.*:ALL
#
# For more examples on how to specify privileges, refer to the community.mysql.mysql_user module

# Create a role developers with all database privileges
# and add alice and bob as members.
# The statement 'SET DEFAULT ROLE ALL' to them will be run.
- name: Create role developers, add members
  community.mysql.mysql_role:
    name: developers
    state: present
    priv: '*.*:ALL'
    members:
    - 'alice@%'
    - 'bob@%'

- name: Same as above but do not run SET DEFAULT ROLE ALL TO each member
  community.mysql.mysql_role:
    name: developers
    state: present
    priv: '*.*:ALL'
    members:
    - 'alice@%'
    - 'bob@%'
    set_default_role_all: false

# Assuming that the role developers exists,
# add john to the current members
- name: Add members to an existing role
  community.mysql.mysql_role:
    name: developers
    state: present
    append_members: true
    members:
    - 'joe@localhost'

# Create role readers with the SELECT privilege
# on all tables in the fiction database
- name: Create role developers, add members
  community.mysql.mysql_role:
    name: readers
    state: present
    priv: 'fiction.*:SELECT'

# Assuming that the role readers exists,
# add the UPDATE privilege to the role on all tables in the fiction database
- name: Create role developers, add members
  community.mysql.mysql_role:
    name: readers
    state: present
    priv: 'fiction.*:UPDATE'
    append_privs: true

- name: Create role with the 'SELECT' and 'UPDATE' privileges in db1 and db2
  community.mysql.mysql_role:
    state: present
    name: foo
    priv:
      'db1.*': 'SELECT,UPDATE'
      'db2.*': 'SELECT,UPDATE'

- name: Remove joe from readers
  community.mysql.mysql_role:
    state: present
    name: readers
    members:
    - 'joe@localhost'
    detach_members: true

- name: Remove the role readers if exists
  community.mysql.mysql_role:
    state: absent
    name: readers

- name: Example of using login_unix_socket to connect to the server
  community.mysql.mysql_role:
    name: readers
    state: present
    login_unix_socket: /var/run/mysqld/mysqld.sock

# Pay attention that the admin cannot be changed later
# and will be ignored if a role currently exists.
# To change members, you need to run a separate task using the admin
# of the role as the login_user.
- name: On MariaDB, create the role readers with alice as its admin
  community.mysql.mysql_role:
    state: present
    name: readers
    admin: 'alice@%'

- name: Create the role business, add the role marketing to members
  community.mysql.mysql_role:
    state: present
    name: business
    members:
    - marketing

- name: Ensure the role foo does not have the DELETE privilege
  community.mysql.mysql_role:
    state: present
    name: foo
    subtract_privs: true
    priv:
      'db1.*': DELETE

- name: Add some members to a role and skip not-existent users
  community.mysql.mysql_role:
    state: present
    name: foo
    append_members: true
    members_must_exist: false
    members:
    - 'existing_user@localhost'
    - 'not_existing_user@localhost'

- name: Detach some members from a role and ignore not-existent users
  community.mysql.mysql_role:
    state: present
    name: foo
    detach_members: true
    members_must_exist: false
    members:
    - 'existing_user@localhost'
    - 'not_existing_user@localhost'
```

### Authors

- Andrew Klychkov (@Andersson007)
- Felix Hamme (@betanummeric)
- kmarse (@kmarse)
- Laurent Indermühle (@laurent-indermuehle)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.mysql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.mysql)

---
collection: ansible
version: "6"
title: "community.mysql.mysql_user module – Adds or removes a user from a MySQL database"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mysql/mysql_user_module.html
fetched_at: 2026-07-27T17:16:18+00:00
---
# community.mysql.mysql_user module – Adds or removes a user from a MySQL database

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
> see [Requirements](mysql_user_module.md#ansible-collections-community-mysql-mysql-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mysql.mysql_user`.

- [Synopsis](mysql_user_module.md#synopsis)
- [Requirements](mysql_user_module.md#requirements)
- [Parameters](mysql_user_module.md#parameters)
- [Notes](mysql_user_module.md#notes)
- [See Also](mysql_user_module.md#see-also)
- [Examples](mysql_user_module.md#examples)

## [Synopsis](mysql_user_module.md#id1)

- Adds or removes a user from a MySQL database.

## [Requirements](mysql_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- mysqlclient (Python 3.5+) or
- PyMySQL (Python 2.7 and Python 3.x) or
- MySQLdb (Python 2.x)

## [Parameters](mysql_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **append_privs**  boolean | Append the privileges defined by priv to the existing ones for this user instead of overwriting existing ones. Mutually exclusive with *subtract_privs*.  Choices:   - `false` ← (default) - `true` |
| **ca_cert**  aliases: ssl_ca  path | The path to a Certificate Authority (CA) certificate. This option, if used, must specify the same certificate as used by the server. |
| **check_hostname**  boolean  added in community.mysql 1.1.0 | Whether to validate the server host name when an SSL connection is required. Corresponds to MySQL CLIs `--ssl` switch.  Setting this to `false` disables hostname verification. Use with caution.  Requires pymysql >= 0.7.11.  This option has no effect on MySQLdb.  Choices:   - `false` - `true` |
| **check_implicit_admin**  boolean | Check if mysql allows login as root/nopassword before trying supplied credentials.  If success, passed *login_user*/*login_password* will be ignored.  Choices:   - `false` ← (default) - `true` |
| **client_cert**  aliases: ssl_cert  path | The path to a client public key certificate. |
| **client_key**  aliases: ssl_key  path | The path to the client private key. |
| **config_file**  path | Specify a config file from which user and password are to be read.  The default config file, `~/.my.cnf`, if it exists, will be read, even if *config_file* is not specified.  The default config file, `~/.my.cnf`, if it exists, must contain a `[client]` section as a MySQL connector requirement.  To prevent the default config file from being read, set *config_file* to be an empty string.  Default: `"~/.my.cnf"` |
| **connect_timeout**  integer | The connection timeout when connecting to the MySQL server.  Default: `30` |
| **encrypted**  boolean | Indicate that the ‘password’ field is a `mysql_native_password` hash.  Choices:   - `false` ← (default) - `true` |
| **force_context**  boolean  added in community.mysql 3.1.0 | Sets the С(mysql) system database as context for the executed statements (it will be used as a database to connect to). Useful if you use binlog / replication filters in MySQL as per default the statements can not be caught by a binlog / replication filter, they require a database to be set to work, otherwise the replication can break down.  See <https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#option_mysqld_binlog-ignore-db> for a description on how binlog filters work (filtering on the primary).  See <https://dev.mysql.com/doc/refman/8.0/en/replication-options-replica.html#option_mysqld_replicate-ignore-db> for a description on how replication filters work (filtering on the replica).  Choices:   - `false` ← (default) - `true` |
| **host**  string | The ‘host’ part of the MySQL username.  Default: `"localhost"` |
| **host_all**  boolean | Override the host option, making ansible apply changes to all hostnames for a given user.  This option cannot be used when creating users.  Choices:   - `false` ← (default) - `true` |
| **login_host**  string | Host running the database.  In some cases for local connections the *login_unix_socket=/path/to/mysqld/socket*, that is usually `/var/run/mysqld/mysqld.sock`, needs to be used instead of *login_host=localhost*.  Default: `"localhost"` |
| **login_password**  string | The password used to authenticate with. |
| **login_port**  integer | Port of the MySQL server. Requires *login_host* be defined as other than localhost if login_port is used.  Default: `3306` |
| **login_unix_socket**  string | The path to a Unix domain socket for local connections.  Use this parameter to avoid the `Please explicitly state intended protocol` error. |
| **login_user**  string | The username used to authenticate with. |
| **name**  string / required | Name of the user (role) to add or remove. |
| **password**  string | Set the user’s password. Only for `mysql_native_password` authentication. For other authentication plugins see the combination of *plugin*, *plugin_hash_string*, *plugin_auth_string*. |
| **plugin**  string  added in community.mysql 0.1.0 | User’s plugin to authenticate (``CREATE USER user IDENTIFIED WITH plugin``). |
| **plugin_auth_string**  string  added in community.mysql 0.1.0 | User’s plugin auth_string (``CREATE USER user IDENTIFIED WITH plugin BY plugin_auth_string``). |
| **plugin_hash_string**  string  added in community.mysql 0.1.0 | User’s plugin hash string (``CREATE USER user IDENTIFIED WITH plugin AS plugin_hash_string``). |
| **priv**  any | MySQL privileges string in the format: `db.table:priv1,priv2`.  Multiple privileges can be specified by separating each one using a forward slash: `db.table1:priv/db.table2:priv`.  The format is based on MySQL `GRANT` statement.  Database and table names can be quoted, MySQL-style.  If column privileges are used, the `priv1,priv2` part must be exactly as returned by a `SHOW GRANT` statement. If not followed, the module will always report changes. It includes grouping columns by permission (`SELECT(col1,col2`) instead of `SELECT(col1`,SELECT(col2))).  Can be passed as a dictionary (see the examples).  Supports GRANTs for procedures and functions (see the examples).  Note: If you pass the same `db.table` combination to this parameter two or more times with different privileges, for example, `'*.*:SELECT/*.*:SHOW VIEW'`, only the last one will be applied, in this example, it will be `SHOW VIEW` respectively. Use `'*.*:SELECT,SHOW VIEW'` instead to apply both. |
| **resource_limits**  dictionary  added in community.mysql 0.1.0 | Limit the user for certain server resources. Provided since MySQL 5.6 / MariaDB 10.2.  Available options are `MAX_QUERIES_PER_HOUR: num`, `MAX_UPDATES_PER_HOUR: num`, `MAX_CONNECTIONS_PER_HOUR: num`, `MAX_USER_CONNECTIONS: num`.  Used when *state=present*, ignored otherwise. |
| **sql_log_bin**  boolean | Whether binary logging should be enabled or disabled for the connection.  Choices:   - `false` - `true` ← (default) |
| **state**  string | Whether the user should exist.  When `absent`, removes the user.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subtract_privs**  boolean  added in community.mysql 3.2.0 | Revoke the privileges defined by the *priv* option and keep other existing privileges. If set, invalid privileges in *priv* are ignored. Mutually exclusive with *append_privs*.  Choices:   - `false` ← (default) - `true` |
| **tls_requires**  dictionary  added in community.mysql 1.0.0 | Set requirement for secure transport as a dictionary of requirements (see the examples).  Valid requirements are SSL, X509, SUBJECT, ISSUER, CIPHER.  SUBJECT, ISSUER and CIPHER are complementary, and mutually exclusive with SSL and X509.  <https://mariadb.com/kb/en/securing-connections-for-client-and-server/#requiring-tls>. |
| **update_password**  string | `always` will update passwords if they differ. This affects *password* and the combination of *plugin*, *plugin_hash_string*, *plugin_auth_string*.  `on_create` will only set the password or the combination of plugin, plugin_hash_string, plugin_auth_string for newly created users.  `on_new_username` works like `on_create`, but it tries to reuse an existing password: If one different user with the same username exists, or multiple different users with the same username and equal `plugin` and `authentication_string` attribute, the existing `plugin` and `authentication_string` are used for the new user instead of the *password*, *plugin*, *plugin_hash_string* or *plugin_auth_string* argument.  Choices:   - `"always"` ← (default) - `"on_create"` - `"on_new_username"` |

## [Notes](mysql_user_module.md#id4)

> **Note:**
>
> - MySQL server installs with default *login_user* of `root` and no password. To secure this user as part of an idempotent playbook, you must create at least two tasks: 1) change the root user’s password, without providing any *login_user*/*login_password* details, 2) drop a `~/.my.cnf` file containing the new root credentials. Subsequent runs of the playbook will then succeed by reading the new credentials from the file.
> - Currently, there is only support for the `mysql_native_password` encrypted password hash module.
> - Supports (check_mode).
> - To avoid the `Please explicitly state intended protocol` error, use the *login_unix_socket* argument, for example, `login_unix_socket: /run/mysqld/mysqld.sock`.
> - Requires the PyMySQL (Python 2.7 and Python 3.X) or MySQL-python (Python 2.X) package installed on the remote host. The Python package may be installed with apt-get install python-pymysql (Ubuntu; see [ansible.builtin.apt](../../ansible/builtin/apt_module.md#ansible-collections-ansible-builtin-apt-module)) or yum install python2-PyMySQL (RHEL/CentOS/Fedora; see [ansible.builtin.yum](../../ansible/builtin/yum_module.md#ansible-collections-ansible-builtin-yum-module)). You can also use dnf install python2-PyMySQL for newer versions of Fedora; see [ansible.builtin.dnf](../../ansible/builtin/dnf_module.md#ansible-collections-ansible-builtin-dnf-module).
> - Be sure you have mysqlclient, PyMySQL, or MySQLdb library installed on the target machine for the Python interpreter Ansible discovers. For example if ansible discovers and uses Python 3, you need to install the Python 3 version of PyMySQL or mysqlclient. If ansible discovers and uses Python 2, you need to install the Python 2 version of either PyMySQL or MySQL-python.
> - If you have trouble, it may help to force Ansible to use the Python interpreter you need by specifying `ansible_python_interpreter`. For more information, see <https://docs.ansible.com/ansible/latest/reference_appendices/interpreter_discovery.html>.
> - Both `login_password` and `login_user` are required when you are passing credentials. If none are present, the module will attempt to read the credentials from `~/.my.cnf`, and finally fall back to using the MySQL default login of ‘root’ with no password.
> - If there are problems with local connections, using *login_unix_socket=/path/to/mysqld/socket* instead of *login_host=localhost* might help. As an example, the default MariaDB installation of version 10.4 and later uses the unix_socket authentication plugin by default that without using *login_unix_socket=/var/run/mysqld/mysqld.sock* (the default path) causes the error ``Host ‘127.0.0.1’ is not allowed to connect to this MariaDB server``.
> - Alternatively, you can use the mysqlclient library instead of MySQL-python (MySQLdb) which supports both Python 2.X and Python >=3.5. See <https://pypi.org/project/mysqlclient/> how to install it.
> - If credentials from the config file (for example, `/root/.my.cnf`) are not needed to connect to a database server, but the file exists and does not contain a `[client]` section, before any other valid directives, it will be read and this will cause the connection to fail, to prevent this set it to an empty string, (for example `config_file: ''`).

## [See Also](mysql_user_module.md#id5)

> **See also:**
>
> [community.mysql.mysql_info](mysql_info_module.md#ansible-collections-community-mysql-mysql-info-module)
> :   Gather information about MySQL servers.
>
> [MySQL access control and account management reference](https://dev.mysql.com/doc/refman/8.0/en/access-control.html)
> :   Complete reference of the MySQL access control and account management documentation.
>
> [MySQL provided privileges reference](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html)
> :   Complete reference of the MySQL provided privileges documentation.

## [Examples](mysql_user_module.md#id6)

```yaml+jinja
# If you encounter the "Please explicitly state intended protocol" error,
# use the login_unix_socket argument
- name: Removes anonymous user account for localhost
  community.mysql.mysql_user:
    name: ''
    host: localhost
    state: absent
    login_unix_socket: /run/mysqld/mysqld.sock

- name: Removes all anonymous user accounts
  community.mysql.mysql_user:
    name: ''
    host_all: yes
    state: absent

- name: Create database user with name 'bob' and password '12345' with all database privileges
  community.mysql.mysql_user:
    name: bob
    password: 12345
    priv: '*.*:ALL'
    state: present

- name: Create database user using hashed password with all database privileges
  community.mysql.mysql_user:
    name: bob
    password: '*EE0D72C1085C46C5278932678FBE2C6A782821B4'
    encrypted: yes
    priv: '*.*:ALL'
    state: present

- name: Create database user with password and all database privileges and 'WITH GRANT OPTION'
  community.mysql.mysql_user:
    name: bob
    password: 12345
    priv: '*.*:ALL,GRANT'
    state: present

- name: Create user with password, all database privileges and 'WITH GRANT OPTION' in db1 and db2
  community.mysql.mysql_user:
    state: present
    name: bob
    password: 12345dd
    priv:
      'db1.*': 'ALL,GRANT'
      'db2.*': 'ALL,GRANT'

# Use 'PROCEDURE' instead of 'FUNCTION' to apply GRANTs for a MySQL procedure instead.
- name: Grant a user the right to execute a function
  community.mysql.mysql_user:
    name: readonly
    password: 12345
    priv:
      FUNCTION my_db.my_function: EXECUTE
    state: present

- name: Modify user to require TLS connection with a valid client certificate
  community.mysql.mysql_user:
    name: bob
    tls_requires:
      x509:
    state: present

- name: Modify user to require TLS connection with a specific client certificate and cipher
  community.mysql.mysql_user:
    name: bob
    tls_requires:
      subject: '/CN=alice/O=MyDom, Inc./C=US/ST=Oregon/L=Portland'
      cipher: 'ECDHE-ECDSA-AES256-SHA384'

- name: Modify user to no longer require SSL
  community.mysql.mysql_user:
    name: bob
    tls_requires:

- name: Ensure no user named 'sally'@'localhost' exists, also passing in the auth credentials
  community.mysql.mysql_user:
    login_user: root
    login_password: 123456
    name: sally
    state: absent

# check_implicit_admin example
- name: >
    Ensure no user named 'sally'@'localhost' exists, also passing in the auth credentials.
    If mysql allows root/nopassword login, try it without the credentials first.
    If it's not allowed, pass the credentials
  community.mysql.mysql_user:
    check_implicit_admin: yes
    login_user: root
    login_password: 123456
    name: sally
    state: absent

- name: Ensure no user named 'sally' exists at all
  community.mysql.mysql_user:
    name: sally
    host_all: yes
    state: absent

- name: Specify grants composed of more than one word
  community.mysql.mysql_user:
    name: replication
    password: 12345
    priv: "*.*:REPLICATION CLIENT"
    state: present

- name: Revoke all privileges for user 'bob' and password '12345'
  community.mysql.mysql_user:
    name: bob
    password: 12345
    priv: "*.*:USAGE"
    state: present

# Example privileges string format
# mydb.*:INSERT,UPDATE/anotherdb.*:SELECT/yetanotherdb.*:ALL

- name: Example using login_unix_socket to connect to server
  community.mysql.mysql_user:
    name: root
    password: abc123
    login_unix_socket: /var/run/mysqld/mysqld.sock

- name: Example of skipping binary logging while adding user 'bob'
  community.mysql.mysql_user:
    name: bob
    password: 12345
    priv: "*.*:USAGE"
    state: present
    sql_log_bin: no

- name: Create user 'bob' authenticated with plugin 'AWSAuthenticationPlugin'
  community.mysql.mysql_user:
    name: bob
    plugin: AWSAuthenticationPlugin
    plugin_hash_string: RDS
    priv: '*.*:ALL'
    state: present

- name: Limit bob's resources to 10 queries per hour and 5 connections per hour
  community.mysql.mysql_user:
    name: bob
    resource_limits:
      MAX_QUERIES_PER_HOUR: 10
      MAX_CONNECTIONS_PER_HOUR: 5

- name: Ensure bob does not have the DELETE privilege
  community.mysql.mysql_user:
    name: bob
    subtract_privs: yes
    priv:
      'db1.*': DELETE

# Example .my.cnf file for setting the root password
# [client]
# user=root
# password=n<_665{vS43y
```

### Authors

- Jonathan Mainguy (@Jmainguy)
- Benjamin Malynovytch (@bmalynovytch)
- Lukasz Tomaszkiewicz (@tomaszkiewicz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mysql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.mysql)

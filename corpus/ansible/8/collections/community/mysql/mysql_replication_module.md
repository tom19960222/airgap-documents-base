---
collection: ansible
version: "8"
title: "community.mysql.mysql_replication module – Manage MySQL replication"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/mysql/mysql_replication_module.html
fetched_at: 2026-07-28T01:54:11+00:00
---
# community.mysql.mysql_replication module – Manage MySQL replication

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
> see [Requirements](mysql_replication_module.md#ansible-collections-community-mysql-mysql-replication-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mysql.mysql_replication`.

- [Synopsis](mysql_replication_module.md#synopsis)
- [Requirements](mysql_replication_module.md#requirements)
- [Parameters](mysql_replication_module.md#parameters)
- [Attributes](mysql_replication_module.md#attributes)
- [Notes](mysql_replication_module.md#notes)
- [See Also](mysql_replication_module.md#see-also)
- [Examples](mysql_replication_module.md#examples)
- [Return Values](mysql_replication_module.md#return-values)

## [Synopsis](mysql_replication_module.md#id1)

- Manages MySQL server replication, replica, primary status, get and change primary host.

## [Requirements](mysql_replication_module.md#id2)

The below requirements are needed on the host that executes this module.

- mysqlclient (Python 3.5+) or
- PyMySQL (Python 2.7 and Python 3.x) or
- MySQLdb (Python 2.x)

## [Parameters](mysql_replication_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_ca  path | The path to a Certificate Authority (CA) certificate. This option, if used, must specify the same certificate as used by the server. |
| **channel**  string  *added in community.mysql 0.1.0* | Name of replication channel.  Multi-source replication is supported from MySQL 5.7.  Mutually exclusive with *connection_name*.  For more information see <https://dev.mysql.com/doc/refman/8.0/en/replication-multi-source.html>. |
| **check_hostname**  boolean  *added in community.mysql 1.1.0* | Whether to validate the server host name when an SSL connection is required. Corresponds to MySQL CLIs `--ssl` switch.  Setting this to `false` disables hostname verification. Use with caution.  Requires pymysql >= 0.7.11.  This option has no effect on MySQLdb.  **Choices:**   - `false` - `true` |
| **client_cert**  aliases: ssl_cert  path | The path to a client public key certificate. |
| **client_key**  aliases: ssl_key  path | The path to the client private key. |
| **config_file**  path | Specify a config file from which user and password are to be read.  The default config file, `~/.my.cnf`, if it exists, will be read, even if *config_file* is not specified.  The default config file, `~/.my.cnf`, if it exists, must contain a `[client]` section as a MySQL connector requirement.  To prevent the default config file from being read, set *config_file* to be an empty string.  **Default:** `"~/.my.cnf"` |
| **connect_timeout**  integer | The connection timeout when connecting to the MySQL server.  **Default:** `30` |
| **connection_name**  string  *added in community.mysql 0.1.0* | Name of the primary connection.  Supported from MariaDB 10.0.1.  Mutually exclusive with *channel*.  For more information see <https://mariadb.com/kb/en/library/multi-source-replication/>. |
| **fail_on_error**  boolean  *added in community.mysql 0.1.0* | Fails on error when calling mysql.  **Choices:**   - `false` ← (default) - `true` |
| **login_host**  string | Host running the database.  In some cases for local connections the *login_unix_socket=/path/to/mysqld/socket*, that is usually `/var/run/mysqld/mysqld.sock`, needs to be used instead of *login_host=localhost*.  **Default:** `"localhost"` |
| **login_password**  string | The password used to authenticate with. |
| **login_port**  integer | Port of the MySQL server. Requires *login_host* be defined as other than localhost if login_port is used.  **Default:** `3306` |
| **login_unix_socket**  string | The path to a Unix domain socket for local connections.  Use this parameter to avoid the `Please explicitly state intended protocol` error. |
| **login_user**  string | The username used to authenticate with. |
| **mode**  string | Module operating mode. Could be `changeprimary` (CHANGE MASTER TO), `getprimary` (SHOW MASTER STATUS), `getreplica` (SHOW REPLICA STATUS), `startreplica` (START REPLICA), `stopreplica` (STOP REPLICA), `resetprimary` (RESET MASTER) - supported since community.mysql 0.1.0, `resetreplica` (RESET REPLICA), `resetreplicaall` (RESET REPLICA ALL).  **Choices:**   - `"changeprimary"` - `"getprimary"` - `"getreplica"` ← (default) - `"startreplica"` - `"stopreplica"` - `"resetprimary"` - `"resetreplica"` - `"resetreplicaall"` |
| **primary_auto_position**  aliases: master_auto_position  boolean | Whether the host uses GTID based replication or not.  Same as the `MASTER_AUTO_POSITION` mysql variable.  **Choices:**   - `false` ← (default) - `true` |
| **primary_connect_retry**  aliases: master_connect_retry  integer | Same as the `MASTER_CONNECT_RETRY` mysql variable. |
| **primary_delay**  aliases: master_delay  integer  *added in community.mysql 0.1.0* | Time lag behind the primary’s state (in seconds).  Same as the `MASTER_DELAY` mysql variable.  Available from MySQL 5.6.  For more information see <https://dev.mysql.com/doc/refman/8.0/en/replication-delayed.html>. |
| **primary_host**  aliases: master_host  string | Same as the `MASTER_HOST` mysql variable. |
| **primary_log_file**  aliases: master_log_file  string | Same as the `MASTER_LOG_FILE` mysql variable. |
| **primary_log_pos**  aliases: master_log_pos  integer | Same as the `MASTER_LOG_POS` mysql variable. |
| **primary_password**  aliases: master_password  string | Same as the `MASTER_PASSWORD` mysql variable. |
| **primary_port**  aliases: master_port  integer | Same as the `MASTER_PORT` mysql variable. |
| **primary_ssl**  aliases: master_ssl  boolean | Same as the `MASTER_SSL` mysql variable.  When setting it to `yes`, the connection attempt only succeeds if an encrypted connection can be established.  For details, refer to [MySQL encrypted replication documentation](https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html).  The default is `false`.  **Choices:**   - `false` - `true` |
| **primary_ssl_ca**  aliases: master_ssl_ca  string | Same as the `MASTER_SSL_CA` mysql variable.  For details, refer to [MySQL encrypted replication documentation](https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html). |
| **primary_ssl_capath**  aliases: master_ssl_capath  string | Same as the `MASTER_SSL_CAPATH` mysql variable.  For details, refer to [MySQL encrypted replication documentation](https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html). |
| **primary_ssl_cert**  aliases: master_ssl_cert  string | Same as the `MASTER_SSL_CERT` mysql variable.  For details, refer to [MySQL encrypted replication documentation](https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html). |
| **primary_ssl_cipher**  aliases: master_ssl_cipher  string | Same as the `MASTER_SSL_CIPHER` mysql variable.  Specifies a colon-separated list of one or more ciphers permitted by the replica for the replication connection.  For details, refer to [MySQL encrypted replication documentation](https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html). |
| **primary_ssl_key**  aliases: master_ssl_key  string | Same as the `MASTER_SSL_KEY` mysql variable.  For details, refer to [MySQL encrypted replication documentation](https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html). |
| **primary_ssl_verify_server_cert**  boolean  *added in community.mysql 3.5.0* | Same as mysql variable.  **Choices:**   - `false` ← (default) - `true` |
| **primary_use_gtid**  aliases: master_use_gtid  string  *added in community.mysql 0.1.0* | Configures the replica to use the MariaDB Global Transaction ID.  `disabled` equals MASTER_USE_GTID=no command.  To find information about available values see <https://mariadb.com/kb/en/library/change-master-to/#master_use_gtid>.  Available since MariaDB 10.0.2.  **Choices:**   - `"current_pos"` - `"replica_pos"` - `"disabled"` |
| **primary_user**  aliases: master_user  string | Same as the `MASTER_USER` mysql variable. |
| **relay_log_file**  string | Same as mysql variable. |
| **relay_log_pos**  integer | Same as mysql variable. |

## [Attributes](mysql_replication_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](mysql_replication_module.md#id5)

> **Note:**
>
> - If an empty value for the parameter of string type is needed, use an empty string.
> - Requires the PyMySQL (Python 2.7 and Python 3.X) or MySQL-python (Python 2.X) package installed on the remote host. The Python package may be installed with apt-get install python-pymysql (Ubuntu; see [ansible.builtin.apt](../../ansible/builtin/apt_module.md#ansible-collections-ansible-builtin-apt-module)) or yum install python2-PyMySQL (RHEL/CentOS/Fedora; see [ansible.builtin.yum](../../ansible/builtin/yum_module.md#ansible-collections-ansible-builtin-yum-module)). You can also use dnf install python2-PyMySQL for newer versions of Fedora; see [ansible.builtin.dnf](../../ansible/builtin/dnf_module.md#ansible-collections-ansible-builtin-dnf-module).
> - Be sure you have mysqlclient, PyMySQL, or MySQLdb library installed on the target machine for the Python interpreter Ansible discovers. For example if ansible discovers and uses Python 3, you need to install the Python 3 version of PyMySQL or mysqlclient. If ansible discovers and uses Python 2, you need to install the Python 2 version of either PyMySQL or MySQL-python.
> - If you have trouble, it may help to force Ansible to use the Python interpreter you need by specifying `ansible_python_interpreter`. For more information, see <https://docs.ansible.com/ansible/latest/reference_appendices/interpreter_discovery.html>.
> - Both `login_password` and `login_user` are required when you are passing credentials. If none are present, the module will attempt to read the credentials from `~/.my.cnf`, and finally fall back to using the MySQL default login of ‘root’ with no password.
> - If there are problems with local connections, using *login_unix_socket=/path/to/mysqld/socket* instead of *login_host=localhost* might help. As an example, the default MariaDB installation of version 10.4 and later uses the unix_socket authentication plugin by default that without using *login_unix_socket=/var/run/mysqld/mysqld.sock* (the default path) causes the error ``Host ‘127.0.0.1’ is not allowed to connect to this MariaDB server``.
> - Alternatively, you can use the mysqlclient library instead of MySQL-python (MySQLdb) which supports both Python 2.X and Python >=3.5. See <https://pypi.org/project/mysqlclient/> how to install it.
> - If credentials from the config file (for example, `/root/.my.cnf`) are not needed to connect to a database server, but the file exists and does not contain a `[client]` section, before any other valid directives, it will be read and this will cause the connection to fail, to prevent this set it to an empty string, (for example `config_file: ''`).
> - To avoid the `Please explicitly state intended protocol` error, use the *login_unix_socket* argument, for example, `login_unix_socket: /run/mysqld/mysqld.sock`.
> - Alternatively, to avoid using *login_unix_socket* argument on each invocation you can specify the socket path using the `socket` option in your MySQL config file (usually `~/.my.cnf`) on the destination host, for example `socket=/var/lib/mysql/mysql.sock`.

## [See Also](mysql_replication_module.md#id6)

> **See also:**
>
> [community.mysql.mysql_info](mysql_info_module.md#ansible-collections-community-mysql-mysql-info-module)
> :   Gather information about MySQL servers.
>
> [MySQL replication reference](https://dev.mysql.com/doc/refman/8.0/en/replication.html)
> :   Complete reference of the MySQL replication documentation.
>
> [MySQL encrypted replication reference.](https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html)
> :   Setting up MySQL replication to use encrypted connection.
>
> [MariaDB replication reference](https://mariadb.com/kb/en/library/setting-up-replication/)
> :   Complete reference of the MariaDB replication documentation.

## [Examples](mysql_replication_module.md#id7)

```yaml+jinja
# If you encounter the "Please explicitly state intended protocol" error,
# use the login_unix_socket argument
- name: Stop mysql replica thread
  community.mysql.mysql_replication:
    mode: stopreplica
    login_unix_socket: /run/mysqld/mysqld.sock

- name: Get primary binlog file name and binlog position
  community.mysql.mysql_replication:
    mode: getprimary

- name: Change primary to primary server 192.0.2.1 and use binary log 'mysql-bin.000009' with position 4578
  community.mysql.mysql_replication:
    mode: changeprimary
    primary_host: 192.0.2.1
    primary_log_file: mysql-bin.000009
    primary_log_pos: 4578

- name: Check replica status using port 3308
  community.mysql.mysql_replication:
    mode: getreplica
    login_host: ansible.example.com
    login_port: 3308

- name: On MariaDB change primary to use GTID current_pos
  community.mysql.mysql_replication:
    mode: changeprimary
    primary_use_gtid: current_pos

- name: Change primary to use replication delay 3600 seconds
  community.mysql.mysql_replication:
    mode: changeprimary
    primary_host: 192.0.2.1
    primary_delay: 3600

- name: Start MariaDB replica with connection name primary-1
  community.mysql.mysql_replication:
    mode: startreplica
    connection_name: primary-1

- name: Stop replication in channel primary-1
  community.mysql.mysql_replication:
    mode: stopreplica
    channel: primary-1

- name: >
    Run RESET MASTER command which will delete all existing binary log files
    and reset the binary log index file on the primary
  community.mysql.mysql_replication:
    mode: resetprimary

- name: Run start replica and fail the task on errors
  community.mysql.mysql_replication:
    mode: startreplica
    connection_name: primary-1
    fail_on_error: true

- name: Change primary and fail on error (like when replica thread is running)
  community.mysql.mysql_replication:
    mode: changeprimary
    fail_on_error: true
```

## [Return Values](mysql_replication_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **queries**  list / elements=string  *added in community.mysql 0.1.0* | List of executed queries which modified DB’s state.  **Returned:** always  **Sample:** `["CHANGE MASTER TO MASTER_HOST='primary2.example.com',MASTER_PORT=3306"]` |

### Authors

- Balazs Pocze (@banyek)
- Andrew Klychkov (@Andersson007)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.mysql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.mysql)

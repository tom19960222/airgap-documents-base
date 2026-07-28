---
collection: ansible
version: "8"
title: "community.mysql.mysql_info module – Gather information about MySQL servers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/mysql/mysql_info_module.html
fetched_at: 2026-07-28T01:54:10+00:00
---
# community.mysql.mysql_info module – Gather information about MySQL servers

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
> see [Requirements](mysql_info_module.md#ansible-collections-community-mysql-mysql-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.mysql.mysql_info`.

- [Synopsis](mysql_info_module.md#synopsis)
- [Requirements](mysql_info_module.md#requirements)
- [Parameters](mysql_info_module.md#parameters)
- [Attributes](mysql_info_module.md#attributes)
- [Notes](mysql_info_module.md#notes)
- [See Also](mysql_info_module.md#see-also)
- [Examples](mysql_info_module.md#examples)
- [Return Values](mysql_info_module.md#return-values)

## [Synopsis](mysql_info_module.md#id1)

- Gathers information about MySQL servers.

## [Requirements](mysql_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- mysqlclient (Python 3.5+) or
- PyMySQL (Python 2.7 and Python 3.x) or
- MySQLdb (Python 2.x)

## [Parameters](mysql_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ssl_ca  path | The path to a Certificate Authority (CA) certificate. This option, if used, must specify the same certificate as used by the server. |
| **check_hostname**  boolean  *added in community.mysql 1.1.0* | Whether to validate the server host name when an SSL connection is required. Corresponds to MySQL CLIs `--ssl` switch.  Setting this to `false` disables hostname verification. Use with caution.  Requires pymysql >= 0.7.11.  This option has no effect on MySQLdb.  **Choices:**   - `false` - `true` |
| **client_cert**  aliases: ssl_cert  path | The path to a client public key certificate. |
| **client_key**  aliases: ssl_key  path | The path to the client private key. |
| **config_file**  path | Specify a config file from which user and password are to be read.  The default config file, `~/.my.cnf`, if it exists, will be read, even if *config_file* is not specified.  The default config file, `~/.my.cnf`, if it exists, must contain a `[client]` section as a MySQL connector requirement.  To prevent the default config file from being read, set *config_file* to be an empty string.  **Default:** `"~/.my.cnf"` |
| **connect_timeout**  integer | The connection timeout when connecting to the MySQL server.  **Default:** `30` |
| **exclude_fields**  list / elements=string  *added in community.mysql 0.1.0* | List of fields which are not needed to collect.  Supports elements: `db_size`. Unsupported elements will be ignored. |
| **filter**  list / elements=string | Limit the collected information by comma separated string or YAML list.  Allowable values are `version`, `databases`, `settings`, `global_status`, `users`, `users_info`, `engines`, `master_status`, `slave_status`, `slave_hosts`.  By default, collects all subsets.  You can use ‘!’ before value (for example, `!settings`) to exclude it from the information.  If you pass including and excluding values to the filter, for example, *filter=!settings,version*, the excluding values, `!settings` in this case, will be ignored. |
| **login_db**  string | Database name to connect to.  It makes sense if *login_user* is allowed to connect to a specific database only. |
| **login_host**  string | Host running the database.  In some cases for local connections the *login_unix_socket=/path/to/mysqld/socket*, that is usually `/var/run/mysqld/mysqld.sock`, needs to be used instead of *login_host=localhost*.  **Default:** `"localhost"` |
| **login_password**  string | The password used to authenticate with. |
| **login_port**  integer | Port of the MySQL server. Requires *login_host* be defined as other than localhost if login_port is used.  **Default:** `3306` |
| **login_unix_socket**  string | The path to a Unix domain socket for local connections.  Use this parameter to avoid the `Please explicitly state intended protocol` error. |
| **login_user**  string | The username used to authenticate with. |
| **return_empty_dbs**  boolean | Includes names of empty databases to returned dictionary.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](mysql_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |

## [Notes](mysql_info_module.md#id5)

> **Note:**
>
> - Calculating the size of a database might be slow, depending on the number and size of tables in it. To avoid this, use *exclude_fields=db_size*.
> - Requires the PyMySQL (Python 2.7 and Python 3.X) or MySQL-python (Python 2.X) package installed on the remote host. The Python package may be installed with apt-get install python-pymysql (Ubuntu; see [ansible.builtin.apt](../../ansible/builtin/apt_module.md#ansible-collections-ansible-builtin-apt-module)) or yum install python2-PyMySQL (RHEL/CentOS/Fedora; see [ansible.builtin.yum](../../ansible/builtin/yum_module.md#ansible-collections-ansible-builtin-yum-module)). You can also use dnf install python2-PyMySQL for newer versions of Fedora; see [ansible.builtin.dnf](../../ansible/builtin/dnf_module.md#ansible-collections-ansible-builtin-dnf-module).
> - Be sure you have mysqlclient, PyMySQL, or MySQLdb library installed on the target machine for the Python interpreter Ansible discovers. For example if ansible discovers and uses Python 3, you need to install the Python 3 version of PyMySQL or mysqlclient. If ansible discovers and uses Python 2, you need to install the Python 2 version of either PyMySQL or MySQL-python.
> - If you have trouble, it may help to force Ansible to use the Python interpreter you need by specifying `ansible_python_interpreter`. For more information, see <https://docs.ansible.com/ansible/latest/reference_appendices/interpreter_discovery.html>.
> - Both `login_password` and `login_user` are required when you are passing credentials. If none are present, the module will attempt to read the credentials from `~/.my.cnf`, and finally fall back to using the MySQL default login of ‘root’ with no password.
> - If there are problems with local connections, using *login_unix_socket=/path/to/mysqld/socket* instead of *login_host=localhost* might help. As an example, the default MariaDB installation of version 10.4 and later uses the unix_socket authentication plugin by default that without using *login_unix_socket=/var/run/mysqld/mysqld.sock* (the default path) causes the error ``Host ‘127.0.0.1’ is not allowed to connect to this MariaDB server``.
> - Alternatively, you can use the mysqlclient library instead of MySQL-python (MySQLdb) which supports both Python 2.X and Python >=3.5. See <https://pypi.org/project/mysqlclient/> how to install it.
> - If credentials from the config file (for example, `/root/.my.cnf`) are not needed to connect to a database server, but the file exists and does not contain a `[client]` section, before any other valid directives, it will be read and this will cause the connection to fail, to prevent this set it to an empty string, (for example `config_file: ''`).
> - To avoid the `Please explicitly state intended protocol` error, use the *login_unix_socket* argument, for example, `login_unix_socket: /run/mysqld/mysqld.sock`.
> - Alternatively, to avoid using *login_unix_socket* argument on each invocation you can specify the socket path using the `socket` option in your MySQL config file (usually `~/.my.cnf`) on the destination host, for example `socket=/var/lib/mysql/mysql.sock`.

## [See Also](mysql_info_module.md#id6)

> **See also:**
>
> [community.mysql.mysql_variables](mysql_variables_module.md#ansible-collections-community-mysql-mysql-variables-module)
> :   Manage MySQL global variables.
>
> [community.mysql.mysql_db](mysql_db_module.md#ansible-collections-community-mysql-mysql-db-module)
> :   Add or remove MySQL databases from a remote host.
>
> [community.mysql.mysql_user](mysql_user_module.md#ansible-collections-community-mysql-mysql-user-module)
> :   Adds or removes a user from a MySQL database.
>
> [community.mysql.mysql_replication](mysql_replication_module.md#ansible-collections-community-mysql-mysql-replication-module)
> :   Manage MySQL replication.

## [Examples](mysql_info_module.md#id7)

```yaml+jinja
# Display info from mysql-hosts group (using creds from ~/.my.cnf to connect):
# ansible mysql-hosts -m mysql_info

# Display only databases and users info:
# ansible mysql-hosts -m mysql_info -a 'filter=databases,users'

# Display all users privileges:
# ansible mysql-hosts -m mysql_info -a 'filter=users_info'

# Display only slave status:
# ansible standby -m mysql_info -a 'filter=slave_status'

# Display all info from databases group except settings:
# ansible databases -m mysql_info -a 'filter=!settings'

# If you encounter the "Please explicitly state intended protocol" error,
# use the login_unix_socket argument
- name: Collect all possible information using passwordless root access
  community.mysql.mysql_info:
    login_user: root
    login_unix_socket: /run/mysqld/mysqld.sock

- name: Get MySQL version with non-default credentials
  community.mysql.mysql_info:
    login_user: mysuperuser
    login_password: mysuperpass
    filter: version

- name: Collect all info except settings and users by root
  community.mysql.mysql_info:
    login_user: root
    login_password: rootpass
    filter: "!settings,!users"

- name: Collect info about databases and version using ~/.my.cnf as a credential file
  become: true
  community.mysql.mysql_info:
    filter:
    - databases
    - version

- name: Collect info about databases and version using ~alice/.my.cnf as a credential file
  become: true
  community.mysql.mysql_info:
    config_file: /home/alice/.my.cnf
    filter:
    - databases
    - version

- name: Collect info about databases including empty and excluding their sizes
  become: true
  community.mysql.mysql_info:
    config_file: /home/alice/.my.cnf
    filter:
    - databases
    exclude_fields: db_size
    return_empty_dbs: true

- name: Clone users from one server to another
  block:
  # Step 1
  - name: Fetch information from a source server
    delegate_to: server_source
    community.mysql.mysql_info:
      filter:
        - users_info
    register: result

  # Step 2
  # Don't work with sha256_password and cache_sha2_password
  - name: Clone users fetched in a previous task to a target server
    community.mysql.mysql_user:
      name: "{{ item.name }}"
      host: "{{ item.host }}"
      plugin: "{{ item.plugin | default(omit) }}"
      plugin_auth_string: "{{ item.plugin_auth_string | default(omit) }}"
      plugin_hash_string: "{{ item.plugin_hash_string | default(omit) }}"
      tls_require: "{{ item.tls_require | default(omit) }}"
      priv: "{{ item.priv | default(omit) }}"
      resource_limits: "{{ item.resource_limits | default(omit) }}"
      column_case_sensitive: true
      state: present
    loop: "{{ result.users_info }}"
    loop_control:
      label: "{{ item.name }}@{{ item.host }}"
    when:
      - item.name != 'root'  # In case you don't want to import admin accounts
      - item.name != 'mariadb.sys'
      - item.name != 'mysql'
```

## [Return Values](mysql_info_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **connector_name**  string  *added in community.mysql 3.6.0* | Name of the python connector used by the module. When the connector is not identified, returns `Unknown`.  **Returned:** always  **Sample:** `"['pymysql', 'MySQLdb']"` |
| **connector_version**  string  *added in community.mysql 3.6.0* | Version of the python connector used by the module. When the connector is not identified, returns `Unknown`.  **Returned:** always  **Sample:** `"['1.0.2']"` |
| **databases**  dictionary | Information about databases.  **Returned:** if not excluded by filter  **Sample:** `[{"information_schema": {"size": 73728}, "mysql": {"size": 656594}}]` |
| **size**  dictionary | Database size in bytes.  **Returned:** if not excluded by filter  **Sample:** `{"size": 656594}` |
| **engines**  dictionary | Information about the server’s storage engines.  **Returned:** if not excluded by filter  **Sample:** `[{"CSV": {"Comment": "CSV storage engine", "Savepoints": "NO", "Support": "YES", "Transactions": "NO", "XA": "NO"}}]` |
| **global_status**  dictionary | Global status information.  **Returned:** if not excluded by filter  **Sample:** `[{"Innodb_buffer_pool_read_requests": 123, "Innodb_buffer_pool_reads": 32}]` |
| **master_status**  dictionary | Master status information.  **Returned:** if master  **Sample:** `[{"Binlog_Do_DB": "", "Binlog_Ignore_DB": "mysql", "File": "mysql-bin.000001", "Position": 769}]` |
| **settings**  dictionary | Global settings (variables) information.  **Returned:** if not excluded by filter  **Sample:** `[{"innodb_open_files": 300, "innodb_page_size\"": 16384}]` |
| **slave_hosts**  dictionary | Slave status information.  **Returned:** if master  **Sample:** `[{"2": {"Host": "", "Master_id": 1, "Port": 3306}}]` |
| **slave_status**  dictionary | Slave status information.  **Returned:** if standby  **Sample:** `[{"192.168.1.101": {"3306": {"replication_user": {"Connect_Retry": 60, "Exec_Master_Log_Pos": 769, "Last_Errno": 0}}}}]` |
| **users**  dictionary | Return a dictionnary of users grouped by host and with global privileges only.  **Returned:** if not excluded by filter  **Sample:** `[{"localhost": {"root": {"Alter_priv": "Y", "Alter_routine_priv": "Y"}}}]` |
| **users_info**  dictionary  *added in community.mysql 3.8.0* | Information about users accounts.  The output can be used as an input of the [community.mysql.mysql_user](mysql_user_module.md#ansible-collections-community-mysql-mysql-user-module) plugin.  Useful when migrating accounts to another server or to create an inventory.  Does not support proxy privileges. If an account has proxy privileges, they won’t appear in the output.  Causes issues with authentications plugins `sha256_password` and `caching_sha2_password`. If the output is fed to [community.mysql.mysql_user](mysql_user_module.md#ansible-collections-community-mysql-mysql-user-module), the ``plugin_auth_string`` will most likely be unreadable due to non-binary characters.  **Returned:** if not excluded by filter  **Sample:** `[{"host": "host.com", "name": "user1", "plugin": "mysql_native_password", "plugin_auth_string": "*1234567", "priv": "db1.*:SELECT/db2.*:SELECT", "resource_limits": {"MAX_USER_CONNECTIONS": 100}}]` |
| **version**  dictionary | Database server version.  **Returned:** if not excluded by filter  **Sample:** `{"version": {"full": "5.5.60-MariaDB", "major": 5, "minor": 5, "release": 60, "suffix": "MariaDB"}}` |
| **full**  string | Full server version.  **Returned:** if not excluded by filter  **Sample:** `"5.5.60-MariaDB"` |
| **major**  integer | Major server version.  **Returned:** if not excluded by filter  **Sample:** `5` |
| **minor**  integer | Minor server version.  **Returned:** if not excluded by filter  **Sample:** `5` |
| **release**  integer | Release server version.  **Returned:** if not excluded by filter  **Sample:** `60` |
| **suffix**  string | Server suffix, for example MySQL, MariaDB, other or none.  **Returned:** if not excluded by filter  **Sample:** `"MariaDB"` |

### Authors

- Andrew Klychkov (@Andersson007)
- Sebastian Gumprich (@rndmh3ro)
- Laurent Indermühle (@laurent-indermuehle)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.mysql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.mysql)

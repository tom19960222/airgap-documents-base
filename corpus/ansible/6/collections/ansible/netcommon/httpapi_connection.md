---
collection: ansible
version: "6"
title: "ansible.netcommon.httpapi connection – Use httpapi to run command on network appliances"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/httpapi_connection.html
fetched_at: 2026-07-27T16:44:38+00:00
---
# ansible.netcommon.httpapi connection – Use httpapi to run command on network appliances

> **Note:**
>
> This connection plugin is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.httpapi`.

New in ansible.netcommon 1.0.0

- [Synopsis](httpapi_connection.md#synopsis)
- [Parameters](httpapi_connection.md#parameters)

## [Synopsis](httpapi_connection.md#id1)

- This connection plugin provides a connection to remote devices over a HTTP(S)-based api.

## [Parameters](httpapi_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **become**  boolean | The become option will instruct the CLI session to attempt privilege escalation on platforms that support it. Normally this means transitioning from user mode to `enable` mode in the CLI session. If become is set to True and the remote device does not support privilege escalation or the privilege has already been elevated, then this option is silently ignored.  Can be configured from the CLI via the `--become` or `-b` options.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [privilege_escalation]   become = false   ``` - Environment variable: [`ANSIBLE_BECOME`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME) - Variable: ansible_become |
| **become_method**  string | This option allows the become method to be specified in for handling privilege escalation. Typically the become_method value is set to `enable` but could be defined as other values.  Default: `"sudo"`  Configuration:   - INI entry:  ```YAML+Jinja   [privilege_escalation]   become_method = sudo   ``` - Environment variable: [`ANSIBLE_BECOME_METHOD`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_METHOD) - Variable: ansible_become_method |
| **host**  string | Specifies the remote device FQDN or IP address to establish the HTTP(S) connection to.  Default: `"inventory_hostname"`  Configuration:   - Variable: inventory_hostname - Variable: ansible_host |
| **import_modules**  boolean | Reduce CPU usage and network module execution time by enabling direct execution. Instead of the module being packaged and executed by the shell, it will be directly executed by the Ansible control node using the same python interpreter as the Ansible process. Note- Incompatible with `asynchronous mode`. Note- Python 3 and Ansible 2.9.16 or greater required. Note- With Ansible 2.9.x fully qualified modules names are required in tasks.  Choices:   - `false` - `true` ← (default)   Configuration:   - INI entry:  ```YAML+Jinja   [ansible_network]   import_modules = true   ``` - Environment variable: [`ANSIBLE_NETWORK_IMPORT_MODULES`](../../environment_variables.md#envvar-ANSIBLE_NETWORK_IMPORT_MODULES) - Variable: ansible_network_import_modules |
| **network_os**  string | Configures the device platform network operating system. This value is used to load the correct httpapi plugin to communicate with the remote device  Configuration:   - Variable: ansible_network_os |
| **password**  string | Configures the user password used to authenticate to the remote device when needed for the device API.  Configuration:   - Variable: ansible_password - Variable: ansible_httpapi_pass - Variable: ansible_httpapi_password |
| **persistent_command_timeout**  integer | Configures, in seconds, the amount of time to wait for a command to return from the remote device. If this timer is exceeded before the command returns, the connection plugin will raise an exception and close.  Default: `30`  Configuration:   - INI entry:  ```YAML+Jinja   [persistent_connection]   command_timeout = 30   ``` - Environment variable: [`ANSIBLE_PERSISTENT_COMMAND_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_PERSISTENT_COMMAND_TIMEOUT) - Variable: ansible_command_timeout |
| **persistent_connect_timeout**  integer | Configures, in seconds, the amount of time to wait when trying to initially establish a persistent connection. If this value expires before the connection to the remote device is completed, the connection will fail.  Default: `30`  Configuration:   - INI entry:  ```YAML+Jinja   [persistent_connection]   connect_timeout = 30   ``` - Environment variable: [`ANSIBLE_PERSISTENT_CONNECT_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_PERSISTENT_CONNECT_TIMEOUT) - Variable: ansible_connect_timeout |
| **persistent_log_messages**  boolean | This flag will enable logging the command executed and response received from target device in the ansible log file. For this option to work ‘log_path’ ansible configuration option is required to be set to a file path with write access.  Be sure to fully understand the security implications of enabling this option as it could create a security vulnerability by logging sensitive information in log file.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [persistent_connection]   log_messages = false   ``` - Environment variable: [`ANSIBLE_PERSISTENT_LOG_MESSAGES`](../../environment_variables.md#envvar-ANSIBLE_PERSISTENT_LOG_MESSAGES) - Variable: ansible_persistent_log_messages |
| **platform_type**  string | Set type of platform.  Configuration:   - Environment variable: [`ANSIBLE_PLATFORM_TYPE`](../../environment_variables.md#envvar-ANSIBLE_PLATFORM_TYPE) - Variable: ansible_platform_type |
| **port**  integer | Specifies the port on the remote device that listens for connections when establishing the HTTP(S) connection.  When unspecified, will pick 80 or 443 based on the value of use_ssl.  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   remote_port = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_PORT`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_PORT) - Variable: ansible_httpapi_port |
| **remote_user**  string | The username used to authenticate to the remote device when the API connection is first established. If the remote_user is not specified, the connection will use the username of the logged in user.  Can be configured from the CLI via the `--user` or `-u` options.  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   remote_user = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_USER) - Variable: ansible_user |
| **session_key**  dictionary | Configures the session key to be used to authenticate to the remote device when needed for the device API.  This should contain a dictionary representing the key name and value for the token.  When specified, *password* is ignored.  Configuration:   - Variable: ansible_httpapi_session_key |
| **use_proxy**  boolean | Whether to use https_proxy for requests.  Choices:   - `false` - `true` ← (default)   Configuration:   - Variable: ansible_httpapi_use_proxy |
| **use_ssl**  boolean | Whether to connect using SSL (HTTPS) or not (HTTP).  Choices:   - `false` ← (default) - `true`   Configuration:   - Variable: ansible_httpapi_use_ssl |
| **validate_certs**  boolean | Whether to validate SSL certificates  Choices:   - `false` - `true` ← (default)   Configuration:   - Variable: ansible_httpapi_validate_certs |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)

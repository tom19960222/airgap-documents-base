---
collection: ansible
version: "8"
title: "ansible.netcommon.persistent connection – Use a persistent unix socket for connection"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/persistent_connection.html
fetched_at: 2026-07-28T01:09:18+00:00
---
# ansible.netcommon.persistent connection – Use a persistent unix socket for connection

> **Note:**
>
> This connection plugin is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.persistent`.

New in ansible.netcommon 1.0.0

- [Synopsis](persistent_connection.md#synopsis)
- [Parameters](persistent_connection.md#parameters)

## [Synopsis](persistent_connection.md#id1)

- This is a helper plugin to allow making other connections persistent.

## [Parameters](persistent_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **import_modules**  boolean | Reduce CPU usage and network module execution time by enabling direct execution. Instead of the module being packaged and executed by the shell, it will be directly executed by the Ansible control node using the same python interpreter as the Ansible process. Note- Incompatible with `asynchronous mode`. Note- Python 3 and Ansible 2.9.16 or greater required. Note- With Ansible 2.9.x fully qualified modules names are required in tasks.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [ansible_network]   import_modules = true   ``` - Environment variable: [`ANSIBLE_NETWORK_IMPORT_MODULES`](../../environment_variables.md#envvar-ANSIBLE_NETWORK_IMPORT_MODULES) - Variable: ansible_network_import_modules |
| **persistent_command_timeout**  integer | Configures, in seconds, the amount of time to wait for a command to return from the remote device. If this timer is exceeded before the command returns, the connection plugin will raise an exception and close.  **Default:** `30`  **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   command_timeout = 30   ``` - Environment variable: [`ANSIBLE_PERSISTENT_COMMAND_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_PERSISTENT_COMMAND_TIMEOUT) - Variable: ansible_command_timeout |
| **persistent_connect_timeout**  integer | Configures, in seconds, the amount of time to wait when trying to initially establish a persistent connection. If this value expires before the connection to the remote device is completed, the connection will fail.  **Default:** `30`  **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   connect_timeout = 30   ``` - Environment variable: [`ANSIBLE_PERSISTENT_CONNECT_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_PERSISTENT_CONNECT_TIMEOUT) - Variable: ansible_connect_timeout |
| **persistent_log_messages**  boolean | This flag will enable logging the command executed and response received from target device in the ansible log file. For this option to work ‘log_path’ ansible configuration option is required to be set to a file path with write access.  Be sure to fully understand the security implications of enabling this option as it could create a security vulnerability by logging sensitive information in log file.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   log_messages = false   ``` - Environment variable: [`ANSIBLE_PERSISTENT_LOG_MESSAGES`](../../environment_variables.md#envvar-ANSIBLE_PERSISTENT_LOG_MESSAGES) - Variable: ansible_persistent_log_messages |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)

---
collection: ansible
version: "8"
title: "ansible.netcommon.netconf connection – Provides a persistent connection using the netconf protocol"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/netconf_connection.html
fetched_at: 2026-07-28T01:05:31+00:00
---
# ansible.netcommon.netconf connection – Provides a persistent connection using the netconf protocol

> **Note:**
>
> This connection plugin is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
> You need further requirements to be able to use this connection plugin,
> see [Requirements](netconf_connection.md#ansible-collections-ansible-netcommon-netconf-connection-requirements) for details.
>
> To use it in a playbook, specify: `ansible.netcommon.netconf`.

New in ansible.netcommon 1.0.0

- [Synopsis](netconf_connection.md#synopsis)
- [Requirements](netconf_connection.md#requirements)
- [Parameters](netconf_connection.md#parameters)

## [Synopsis](netconf_connection.md#id1)

- This connection plugin provides a connection to remote devices over the SSH NETCONF subsystem. This connection plugin is typically used by network devices for sending and receiving RPC calls over NETCONF.
- Note this connection plugin requires ncclient to be installed on the local Ansible controller.

## [Requirements](netconf_connection.md#id2)

The below requirements are needed on the local controller node that executes this connection.

- ncclient

## [Parameters](netconf_connection.md#id3)

| Parameter | Comments |
| --- | --- |
| **host**  string | Specifies the remote device FQDN or IP address to establish the SSH connection to.  **Default:** `"inventory_hostname"`  **Configuration:**   - Variable: inventory_hostname - Variable: ansible_host |
| **host_key_checking**  boolean | Set this to “False” if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   host_key_checking = true   ```  ```YAML+Jinja   [paramiko_connection]   host_key_checking = true   ``` - Environment variable: [`ANSIBLE_HOST_KEY_CHECKING`](../../../reference_appendices/config.md#envvar-ANSIBLE_HOST_KEY_CHECKING) - Environment variable: [`ANSIBLE_SSH_HOST_KEY_CHECKING`](../../environment_variables.md#envvar-ANSIBLE_SSH_HOST_KEY_CHECKING) - Environment variable: [`ANSIBLE_NETCONF_HOST_KEY_CHECKING`](../../environment_variables.md#envvar-ANSIBLE_NETCONF_HOST_KEY_CHECKING) - Variable: ansible_host_key_checking - Variable: ansible_ssh_host_key_checking - Variable: ansible_netconf_host_key_checking |
| **import_modules**  boolean | Reduce CPU usage and network module execution time by enabling direct execution. Instead of the module being packaged and executed by the shell, it will be directly executed by the Ansible control node using the same python interpreter as the Ansible process. Note- Incompatible with `asynchronous mode`. Note- Python 3 and Ansible 2.9.16 or greater required. Note- With Ansible 2.9.x fully qualified modules names are required in tasks.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [ansible_network]   import_modules = true   ``` - Environment variable: [`ANSIBLE_NETWORK_IMPORT_MODULES`](../../environment_variables.md#envvar-ANSIBLE_NETWORK_IMPORT_MODULES) - Variable: ansible_network_import_modules |
| **look_for_keys**  boolean | Enables looking for ssh keys in the usual locations for ssh keys (e.g. :file:`~/.ssh/id_\*`).  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [paramiko_connection]   look_for_keys = true   ``` - Environment variable: [`ANSIBLE_PARAMIKO_LOOK_FOR_KEYS`](../../../reference_appendices/config.md#envvar-ANSIBLE_PARAMIKO_LOOK_FOR_KEYS) |
| **netconf_ssh_config**  string | This variable is used to enable bastion/jump host with netconf connection. If set to True the bastion/jump host ssh settings should be present in ~/.ssh/config file, alternatively it can be set to custom ssh configuration file path to read the bastion/jump host settings.  **Configuration:**   - INI entry:  ```YAML+Jinja   [netconf_connection]   ssh_config = VALUE   ``` - Environment variable: [`ANSIBLE_NETCONF_SSH_CONFIG`](../../../reference_appendices/config.md#envvar-ANSIBLE_NETCONF_SSH_CONFIG) - Variable: ansible_netconf_ssh_config |
| **network_os**  string | Configures the device platform network operating system. This value is used to load a device specific netconf plugin. If this option is not configured (or set to `auto`), then Ansible will attempt to guess the correct network_os to use. If it can not guess a network_os correctly it will use `default`.  **Configuration:**   - Variable: ansible_network_os |
| **password**  string | Configures the user password used to authenticate to the remote device when first establishing the SSH connection.  **Configuration:**   - Variable: ansible_password - Variable: ansible_ssh_pass - Variable: ansible_ssh_password - Variable: ansible_netconf_password |
| **persistent_command_timeout**  integer | Configures, in seconds, the amount of time to wait for a command to return from the remote device. If this timer is exceeded before the command returns, the connection plugin will raise an exception and close.  **Default:** `30`  **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   command_timeout = 30   ``` - Environment variable: [`ANSIBLE_PERSISTENT_COMMAND_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_PERSISTENT_COMMAND_TIMEOUT) - Variable: ansible_command_timeout |
| **persistent_connect_timeout**  integer | Configures, in seconds, the amount of time to wait when trying to initially establish a persistent connection. If this value expires before the connection to the remote device is completed, the connection will fail.  **Default:** `30`  **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   connect_timeout = 30   ``` - Environment variable: [`ANSIBLE_PERSISTENT_CONNECT_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_PERSISTENT_CONNECT_TIMEOUT) - Variable: ansible_connect_timeout |
| **persistent_log_messages**  boolean | This flag will enable logging the command executed and response received from target device in the ansible log file. For this option to work ‘log_path’ ansible configuration option is required to be set to a file path with write access.  Be sure to fully understand the security implications of enabling this option as it could create a security vulnerability by logging sensitive information in log file.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   log_messages = false   ``` - Environment variable: [`ANSIBLE_PERSISTENT_LOG_MESSAGES`](../../environment_variables.md#envvar-ANSIBLE_PERSISTENT_LOG_MESSAGES) - Variable: ansible_persistent_log_messages |
| **port**  integer | Specifies the port on the remote device that listens for connections when establishing the SSH connection.  **Default:** `830`  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   remote_port = 830   ``` - Environment variable: [`ANSIBLE_REMOTE_PORT`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_PORT) - Variable: ansible_port |
| **private_key_file**  string | The private SSH key or certificate file used to authenticate to the remote device when first establishing the SSH connection.  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   private_key_file = VALUE   ``` - Environment variable: [`ANSIBLE_PRIVATE_KEY_FILE`](../../../reference_appendices/config.md#envvar-ANSIBLE_PRIVATE_KEY_FILE) - Variable: ansible_private_key_file |
| **proxy_command**  string | Proxy information for running the connection via a jumphost.  This requires ncclient >= 0.6.10 to be installed on the controller.  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [paramiko_connection]   proxy_command = ""   ``` - Environment variable: [`ANSIBLE_NETCONF_PROXY_COMMAND`](../../environment_variables.md#envvar-ANSIBLE_NETCONF_PROXY_COMMAND) - Variable: ansible_paramiko_proxy_command - Variable: ansible_netconf_proxy_command |
| **remote_user**  string | The username used to authenticate to the remote device when the SSH connection is first established. If the remote_user is not specified, the connection will use the username of the logged in user.  Can be configured from the CLI via the `--user` or `-u` options.  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   remote_user = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_USER) - Variable: ansible_user |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)

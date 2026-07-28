---
collection: ansible
version: "6"
title: "ansible.netcommon.napalm connection – Provides persistent connection using NAPALM"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/napalm_connection.html
fetched_at: 2026-07-27T16:44:39+00:00
---
# ansible.netcommon.napalm connection – Provides persistent connection using NAPALM

> **Note:**
>
> This connection plugin is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
> You need further requirements to be able to use this connection plugin,
> see [Requirements](napalm_connection.md#ansible-collections-ansible-netcommon-napalm-connection-requirements) for details.
>
> To use it in a playbook, specify: `ansible.netcommon.napalm`.

New in ansible.netcommon 1.0.0

- [DEPRECATED](napalm_connection.md#deprecated)
- [Synopsis](napalm_connection.md#synopsis)
- [Requirements](napalm_connection.md#requirements)
- [Parameters](napalm_connection.md#parameters)
- [Status](napalm_connection.md#status)

## [DEPRECATED](napalm_connection.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   I am pretty sure no one has ever tried to use these modules

Alternative:
:   network_cli

## [Synopsis](napalm_connection.md#id2)

- This connection plugin provides connectivity to network devices using the NAPALM network device abstraction library. This library requires certain features to be enabled on network devices depending on the destination device operating system. The connection plugin requires `napalm` to be installed locally on the Ansible controller.

## [Requirements](napalm_connection.md#id3)

The below requirements are needed on the local controller node that executes this connection.

- napalm

## [Parameters](napalm_connection.md#id4)

| Parameter | Comments |
| --- | --- |
| **host**  string | Specifies the remote device FQDN or IP address to establish the SSH connection to.  Default: `"inventory_hostname"`  Configuration:   - Variable: inventory_hostname - Variable: ansible_host |
| **host_key_auto_add**  boolean | By default, Ansible will prompt the user before adding SSH keys to the known hosts file. By enabling this option, unknown host keys will automatically be added to the known hosts file.  Be sure to fully understand the security implications of enabling this option on production systems as it could create a security vulnerability.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [paramiko_connection]   host_key_auto_add = false   ``` - Environment variable: [`ANSIBLE_HOST_KEY_AUTO_ADD`](../../environment_variables.md#envvar-ANSIBLE_HOST_KEY_AUTO_ADD) |
| **import_modules**  boolean | Reduce CPU usage and network module execution time by enabling direct execution. Instead of the module being packaged and executed by the shell, it will be directly executed by the Ansible control node using the same python interpreter as the Ansible process. Note- Incompatible with `asynchronous mode`. Note- Python 3 and Ansible 2.9.16 or greater required. Note- With Ansible 2.9.x fully qualified modules names are required in tasks.  Choices:   - `false` - `true` ← (default)   Configuration:   - INI entry:  ```YAML+Jinja   [ansible_network]   import_modules = true   ``` - Environment variable: [`ANSIBLE_NETWORK_IMPORT_MODULES`](../../environment_variables.md#envvar-ANSIBLE_NETWORK_IMPORT_MODULES) - Variable: ansible_network_import_modules |
| **network_os**  string | Configures the device platform network operating system. This value is used to load a napalm device abstraction.  Configuration:   - Variable: ansible_network_os |
| **password**  string | Configures the user password used to authenticate to the remote device when first establishing the SSH connection.  Configuration:   - Variable: ansible_password - Variable: ansible_ssh_pass - Variable: ansible_ssh_password |
| **persistent_command_timeout**  integer | Configures, in seconds, the amount of time to wait for a command to return from the remote device. If this timer is exceeded before the command returns, the connection plugin will raise an exception and close.  Default: `30`  Configuration:   - INI entry:  ```YAML+Jinja   [persistent_connection]   command_timeout = 30   ``` - Environment variable: [`ANSIBLE_PERSISTENT_COMMAND_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_PERSISTENT_COMMAND_TIMEOUT) - Variable: ansible_command_timeout |
| **persistent_connect_timeout**  integer | Configures, in seconds, the amount of time to wait when trying to initially establish a persistent connection. If this value expires before the connection to the remote device is completed, the connection will fail.  Default: `30`  Configuration:   - INI entry:  ```YAML+Jinja   [persistent_connection]   connect_timeout = 30   ``` - Environment variable: [`ANSIBLE_PERSISTENT_CONNECT_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_PERSISTENT_CONNECT_TIMEOUT) - Variable: ansible_connect_timeout |
| **persistent_log_messages**  boolean | This flag will enable logging the command executed and response received from target device in the ansible log file. For this option to work ‘log_path’ ansible configuration option is required to be set to a file path with write access.  Be sure to fully understand the security implications of enabling this option as it could create a security vulnerability by logging sensitive information in log file.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [persistent_connection]   log_messages = false   ``` - Environment variable: [`ANSIBLE_PERSISTENT_LOG_MESSAGES`](../../environment_variables.md#envvar-ANSIBLE_PERSISTENT_LOG_MESSAGES) - Variable: ansible_persistent_log_messages |
| **port**  integer | Specifies the port on the remote device that listens for connections when establishing the SSH connection.  Default: `22`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   remote_port = 22   ``` - Environment variable: [`ANSIBLE_REMOTE_PORT`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_PORT) - Variable: ansible_port |
| **private_key_file**  string | The private SSH key or certificate file used to authenticate to the remote device when first establishing the SSH connection.  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   private_key_file = VALUE   ``` - Environment variable: [`ANSIBLE_PRIVATE_KEY_FILE`](../../../reference_appendices/config.md#envvar-ANSIBLE_PRIVATE_KEY_FILE) - Variable: ansible_private_key_file |
| **remote_user**  string | The username used to authenticate to the remote device when the SSH connection is first established. If the remote_user is not specified, the connection will use the username of the logged in user.  Can be configured from the CLI via the `--user` or `-u` options.  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   remote_user = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_USER) - Variable: ansible_user |
| **timeout**  integer | Sets the connection time, in seconds, for communicating with the remote device. This timeout is used as the default timeout value for commands when issuing a command to the network CLI. If the command does not return in timeout seconds, an error is generated.  Default: `120` |

## [Status](napalm_connection.md#id5)

- This connection will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](napalm_connection.md#deprecated).

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)

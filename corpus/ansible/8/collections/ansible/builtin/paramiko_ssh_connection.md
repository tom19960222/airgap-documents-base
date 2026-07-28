---
collection: ansible
version: "8"
title: "ansible.builtin.paramiko_ssh connection – Run tasks via python ssh (paramiko)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/paramiko_ssh_connection.html
fetched_at: 2026-07-28T01:05:14+00:00
---
# ansible.builtin.paramiko_ssh connection – Run tasks via python ssh (paramiko)

> **Note:**
>
> This connection plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `paramiko_ssh`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.paramiko_ssh` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same connection plugin name.

- [Synopsis](paramiko_ssh_connection.md#synopsis)
- [Parameters](paramiko_ssh_connection.md#parameters)

## [Synopsis](paramiko_ssh_connection.md#id1)

- Use the python ssh implementation (Paramiko) to connect to targets
- The paramiko transport is provided because many distributions, in particular EL6 and before do not support ControlPersist in their SSH implementations.
- This is needed on the Ansible control machine to be reasonably efficient with connections. Thus paramiko is faster for most users on these platforms. Users with ControlPersist capability can consider using -c ssh or configuring the transport in the configuration file.
- This plugin also borrows a lot of settings from the ssh plugin as they both cover the same protocol.

## [Parameters](paramiko_ssh_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **banner_timeout**  float  *added in ansible-core 2.14* | Configures, in seconds, the amount of time to wait for the SSH banner to be presented. This option is supported by paramiko version 1.15.0 or newer.  **Default:** `30.0`  **Configuration:**   - INI entry:  ```YAML+Jinja   [paramiko_connection]   banner_timeout = 30.0   ``` - Environment variable: [`ANSIBLE_PARAMIKO_BANNER_TIMEOUT`](../../environment_variables.md#envvar-ANSIBLE_PARAMIKO_BANNER_TIMEOUT) |
| **host_key_auto_add**  boolean | Automatically add host keys  **Choices:**   - `false` - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [paramiko_connection]   host_key_auto_add = VALUE   ``` - Environment variable: [`ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD`](../../../reference_appendices/config.md#envvar-ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD) |
| **host_key_checking**  boolean | Set this to “False” if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   host_key_checking = true   ```  ```YAML+Jinja   [paramiko_connection]   host_key_checking = true   ``` - Environment variable: [`ANSIBLE_HOST_KEY_CHECKING`](../../../reference_appendices/config.md#envvar-ANSIBLE_HOST_KEY_CHECKING) - Environment variable: [`ANSIBLE_SSH_HOST_KEY_CHECKING`](../../environment_variables.md#envvar-ANSIBLE_SSH_HOST_KEY_CHECKING) - Environment variable: [`ANSIBLE_PARAMIKO_HOST_KEY_CHECKING`](../../environment_variables.md#envvar-ANSIBLE_PARAMIKO_HOST_KEY_CHECKING) - Variable: ansible_host_key_checking - Variable: ansible_ssh_host_key_checking - Variable: ansible_paramiko_host_key_checking |
| **look_for_keys**  boolean | False to disable searching for private key files in ~/.ssh/  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [paramiko_connection]   look_for_keys = true   ``` - Environment variable: [`ANSIBLE_PARAMIKO_LOOK_FOR_KEYS`](../../../reference_appendices/config.md#envvar-ANSIBLE_PARAMIKO_LOOK_FOR_KEYS) |
| **password**  string | Secret used to either login the ssh server or as a passphrase for ssh keys that require it  Can be set from the CLI via the `--ask-pass` option.  **Configuration:**   - Variable: ansible_password - Variable: ansible_ssh_pass - Variable: ansible_ssh_password - Variable: ansible_paramiko_pass - Variable: ansible_paramiko_password |
| **port**  integer | Remote port to connect to.  **Default:** `22`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   remote_port = 22   ```  ```YAML+Jinja   [paramiko_connection]   remote_port = 22   ```  *added in ansible-core 2.15* - Environment variable: [`ANSIBLE_REMOTE_PORT`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_PORT) - Environment variable: [`ANSIBLE_REMOTE_PARAMIKO_PORT`](../../environment_variables.md#envvar-ANSIBLE_REMOTE_PARAMIKO_PORT)  *added in ansible-core 2.15* - Variable: ansible_port - Variable: ansible_ssh_port - Variable: ansible_paramiko_port  *added in ansible-core 2.15* - Keyword: port |
| **private_key_file**  string | Path to private key file to use for authentication.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   private_key_file = VALUE   ```  ```YAML+Jinja   [paramiko_connection]   private_key_file = VALUE   ```  *added in ansible-core 2.15* - Environment variable: [`ANSIBLE_PRIVATE_KEY_FILE`](../../../reference_appendices/config.md#envvar-ANSIBLE_PRIVATE_KEY_FILE) - Environment variable: [`ANSIBLE_PARAMIKO_PRIVATE_KEY_FILE`](../../environment_variables.md#envvar-ANSIBLE_PARAMIKO_PRIVATE_KEY_FILE)  *added in ansible-core 2.15* - Variable: ansible_private_key_file - Variable: ansible_ssh_private_key_file - Variable: ansible_paramiko_private_key_file  *added in ansible-core 2.15* - CLI argument: –private-key |
| **proxy_command**  string | Proxy information for running the connection via a jumphost  Also this plugin will scan ‘ssh_args’, ‘ssh_extra_args’ and ‘ssh_common_args’ from the ‘ssh’ plugin settings for proxy information if set.  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [paramiko_connection]   proxy_command = ""   ``` - Environment variable: [`ANSIBLE_PARAMIKO_PROXY_COMMAND`](../../environment_variables.md#envvar-ANSIBLE_PARAMIKO_PROXY_COMMAND) - Variable: ansible_paramiko_proxy_command  *added in ansible-core 2.15* |
| **pty**  boolean | SUDO usually requires a PTY, True to give a PTY and False to not give a PTY.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [paramiko_connection]   pty = true   ``` - Environment variable: [`ANSIBLE_PARAMIKO_PTY`](../../environment_variables.md#envvar-ANSIBLE_PARAMIKO_PTY) |
| **record_host_keys**  boolean | Save the host keys to a file  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [paramiko_connection]   record_host_keys = true   ``` - Environment variable: [`ANSIBLE_PARAMIKO_RECORD_HOST_KEYS`](../../environment_variables.md#envvar-ANSIBLE_PARAMIKO_RECORD_HOST_KEYS) |
| **remote_addr**  string | Address of the remote target  **Default:** `"inventory_hostname"`  **Configuration:**   - Variable: inventory_hostname - Variable: ansible_host - Variable: ansible_ssh_host - Variable: ansible_paramiko_host |
| **remote_user**  string | User to login/authenticate as  Can be set from the CLI via the `--user` or `-u` options.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   remote_user = VALUE   ```  ```YAML+Jinja   [paramiko_connection]   remote_user = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_USER) - Environment variable: [`ANSIBLE_PARAMIKO_REMOTE_USER`](../../environment_variables.md#envvar-ANSIBLE_PARAMIKO_REMOTE_USER) - Variable: ansible_user - Variable: ansible_ssh_user - Variable: ansible_paramiko_user - Keyword: remote_user |
| **ssh_args**  string  Removed in: version 2.18  Why: In favor of the “proxy_command” option.  Alternative: proxy_command | Only used in parsing ProxyCommand for use in this plugin.  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   ssh_args = ""   ``` - Environment variable: [`ANSIBLE_SSH_ARGS`](../../environment_variables.md#envvar-ANSIBLE_SSH_ARGS) - Variable: ansible_ssh_args  *added in Ansible 2.7* |
| **ssh_common_args**  string  Removed in: version 2.18  Why: In favor of the “proxy_command” option.  Alternative: proxy_command | Only used in parsing ProxyCommand for use in this plugin.  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   ssh_common_args = ""   ```  *added in Ansible 2.7* - Environment variable: [`ANSIBLE_SSH_COMMON_ARGS`](../../environment_variables.md#envvar-ANSIBLE_SSH_COMMON_ARGS)  *added in Ansible 2.7* - Variable: ansible_ssh_common_args - CLI argument: –ssh-common-args |
| **ssh_extra_args**  string  Removed in: version 2.18  Why: In favor of the “proxy_command” option.  Alternative: proxy_command | Only used in parsing ProxyCommand for use in this plugin.  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   ssh_extra_args = ""   ```  *added in Ansible 2.7* - Environment variable: [`ANSIBLE_SSH_EXTRA_ARGS`](../../environment_variables.md#envvar-ANSIBLE_SSH_EXTRA_ARGS)  *added in Ansible 2.7* - Variable: ansible_ssh_extra_args - CLI argument: –ssh-extra-args |
| **timeout**  integer | Number of seconds until the plugin gives up on failing to establish a TCP connection.  **Default:** `10`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   timeout = 10   ```  ```YAML+Jinja   [ssh_connection]   timeout = 10   ```  *added in ansible-core 2.11*  ```YAML+Jinja   [paramiko_connection]   timeout = 10   ```  *added in ansible-core 2.15* - Environment variable: [`ANSIBLE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_TIMEOUT) - Environment variable: [`ANSIBLE_SSH_TIMEOUT`](../../environment_variables.md#envvar-ANSIBLE_SSH_TIMEOUT)  *added in ansible-core 2.11* - Environment variable: [`ANSIBLE_PARAMIKO_TIMEOUT`](../../environment_variables.md#envvar-ANSIBLE_PARAMIKO_TIMEOUT)  *added in ansible-core 2.15* - Variable: ansible_ssh_timeout  *added in ansible-core 2.11* - Variable: ansible_paramiko_timeout  *added in ansible-core 2.15* - CLI argument: –timeout |
| **use_persistent_connections**  boolean | Toggles the use of persistence for connections  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   use_persistent_connections = false   ``` - Environment variable: [`ANSIBLE_USE_PERSISTENT_CONNECTIONS`](../../../reference_appendices/config.md#envvar-ANSIBLE_USE_PERSISTENT_CONNECTIONS) |
| **use_rsa_sha2_algorithms**  boolean  *added in ansible-core 2.14* | Whether or not to enable RSA SHA2 algorithms for pubkeys and hostkeys  On paramiko versions older than 2.9, this only affects hostkeys  For behavior matching paramiko<2.9 set this to `False`  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [paramiko_connection]   use_rsa_sha2_algorithms = true   ``` - Environment variable: [`ANSIBLE_PARAMIKO_USE_RSA_SHA2_ALGORITHMS`](../../environment_variables.md#envvar-ANSIBLE_PARAMIKO_USE_RSA_SHA2_ALGORITHMS) - Variable: ansible_paramiko_use_rsa_sha2_algorithms |

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)

---
collection: ansible
version: "8"
title: "ansible.netcommon.libssh connection – Run tasks using libssh for ssh connection"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/libssh_connection.html
fetched_at: 2026-07-28T01:09:17+00:00
---
# ansible.netcommon.libssh connection – Run tasks using libssh for ssh connection

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
> To use it in a playbook, specify: `ansible.netcommon.libssh`.

New in ansible.netcommon 1.1.0

- [Synopsis](libssh_connection.md#synopsis)
- [Parameters](libssh_connection.md#parameters)

## [Synopsis](libssh_connection.md#id1)

- Use the ansible-pylibssh python bindings to connect to targets
- The python bindings use libssh C library (<https://www.libssh.org/>) to connect to targets
- This plugin borrows a lot of settings from the ssh plugin as they both cover the same protocol.

## [Parameters](libssh_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **config_file**  path  *added in ansible.netcommon 5.1.0* | Alternate SSH config file location  **Configuration:**   - INI entry:  ```YAML+Jinja   [libssh_connection]   config_file = VALUE   ``` - Environment variable: [`ANSIBLE_LIBSSH_CONFIG_FILE`](../../environment_variables.md#envvar-ANSIBLE_LIBSSH_CONFIG_FILE) - Variable: ansible_libssh_config_file |
| **host_key_auto_add**  boolean | TODO: write it  **Choices:**   - `false` - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [libssh_connection]   host_key_auto_add = VALUE   ``` - Environment variable: [`ANSIBLE_LIBSSH_HOST_KEY_AUTO_ADD`](../../environment_variables.md#envvar-ANSIBLE_LIBSSH_HOST_KEY_AUTO_ADD) |
| **host_key_checking**  boolean | Set this to “False” if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   host_key_checking = true   ```  ```YAML+Jinja   [libssh_connection]   host_key_checking = true   ``` - Environment variable: [`ANSIBLE_HOST_KEY_CHECKING`](../../../reference_appendices/config.md#envvar-ANSIBLE_HOST_KEY_CHECKING) - Environment variable: [`ANSIBLE_SSH_HOST_KEY_CHECKING`](../../environment_variables.md#envvar-ANSIBLE_SSH_HOST_KEY_CHECKING) - Environment variable: [`ANSIBLE_LIBSSH_HOST_KEY_CHECKING`](../../environment_variables.md#envvar-ANSIBLE_LIBSSH_HOST_KEY_CHECKING) - Variable: ansible_host_key_checking - Variable: ansible_ssh_host_key_checking - Variable: ansible_libssh_host_key_checking |
| **look_for_keys**  boolean | TODO: write it  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [libssh_connection]   look_for_keys = true   ``` - Environment variable: [`ANSIBLE_LIBSSH_LOOK_FOR_KEYS`](../../environment_variables.md#envvar-ANSIBLE_LIBSSH_LOOK_FOR_KEYS) |
| **password**  string | Secret used to either login the ssh server or as a passphrase for ssh keys that require it  Can be set from the CLI via the `--ask-pass` option.  **Configuration:**   - Variable: ansible_password - Variable: ansible_ssh_pass - Variable: ansible_ssh_password - Variable: ansible_libssh_pass - Variable: ansible_libssh_password |
| **password_prompt**  string  *added in ansible.netcommon 3.1.0* | Text to match when using keyboard-interactive authentication to determine if the prompt is for the password.  Requires ansible-pylibssh version >= 1.0.0  **Configuration:**   - Variable: ansible_libssh_password_prompt |
| **proxy_command**  string | Proxy information for running the connection via a jumphost.  Also this plugin will scan ‘ssh_args’, ‘ssh_extra_args’ and ‘ssh_common_args’ from the ‘ssh’ plugin settings for proxy information if set.  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [libssh_connection]   proxy_command = ""   ``` - Environment variable: [`ANSIBLE_LIBSSH_PROXY_COMMAND`](../../environment_variables.md#envvar-ANSIBLE_LIBSSH_PROXY_COMMAND) - Variable: ansible_paramiko_proxy_command - Variable: ansible_libssh_proxy_command |
| **pty**  boolean | TODO: write it  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [libssh_connection]   pty = true   ``` - Environment variable: [`ANSIBLE_LIBSSH_PTY`](../../environment_variables.md#envvar-ANSIBLE_LIBSSH_PTY) |
| **remote_addr**  string | Address of the remote target  **Default:** `"inventory_hostname"`  **Configuration:**   - Variable: inventory_hostname - Variable: ansible_host - Variable: ansible_ssh_host - Variable: ansible_libssh_host |
| **remote_user**  string | User to login/authenticate as  Can be set from the CLI via the `--user` or `-u` options.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   remote_user = VALUE   ```  ```YAML+Jinja   [libssh_connection]   remote_user = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_USER) - Environment variable: [`ANSIBLE_LIBSSH_REMOTE_USER`](../../environment_variables.md#envvar-ANSIBLE_LIBSSH_REMOTE_USER) - Variable: ansible_user - Variable: ansible_ssh_user - Variable: ansible_libssh_user |
| **ssh_args**  string  *added in ansible.netcommon 3.2.0* | Arguments to pass to all ssh CLI tools.  ProxyCommand is the only supported argument.  This option is deprecated in favor of *proxy_command* and will be removed in a release after 2026-01-01.  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   ssh_args = VALUE   ``` - Environment variable: [`ANSIBLE_SSH_ARGS`](../../environment_variables.md#envvar-ANSIBLE_SSH_ARGS) - Variable: ansible_ssh_args - CLI argument: –ssh-args |
| **ssh_common_args**  string  *added in ansible.netcommon 3.2.0* | Common extra arguments for all ssh CLI tools.  ProxyCommand is the only supported argument.  This option is deprecated in favor of *proxy_command* and will be removed in a release after 2026-01-01.  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   ssh_common_args = VALUE   ``` - Environment variable: [`ANSIBLE_SSH_COMMON_ARGS`](../../environment_variables.md#envvar-ANSIBLE_SSH_COMMON_ARGS) - Variable: ansible_ssh_common_args - CLI argument: –ssh-common-args |
| **ssh_extra_args**  string  *added in ansible.netcommon 3.2.0* | Extra arguments exclusive to the ‘ssh’ CLI tool.  ProxyCommand is the only supported argument.  This option is deprecated in favor of *proxy_command* and will be removed in a release after 2026-01-01.  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   ssh_extra_args = VALUE   ``` - Environment variable: [`ANSIBLE_SSH_EXTRA_ARGS`](../../environment_variables.md#envvar-ANSIBLE_SSH_EXTRA_ARGS) - Variable: ansible_ssh_extra_args - CLI argument: –ssh-extra-args |
| **use_persistent_connections**  boolean | Toggles the use of persistence for connections  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   use_persistent_connections = false   ``` - Environment variable: [`ANSIBLE_USE_PERSISTENT_CONNECTIONS`](../../../reference_appendices/config.md#envvar-ANSIBLE_USE_PERSISTENT_CONNECTIONS) |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)

---
collection: ansible
version: "8"
title: "ansible.builtin.ssh connection – connect via SSH client binary"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/ssh_connection.html
fetched_at: 2026-07-28T01:05:15+00:00
---
# ansible.builtin.ssh connection – connect via SSH client binary

> **Note:**
>
> This connection plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `ssh`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.ssh` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same connection plugin name.

- [Synopsis](ssh_connection.md#synopsis)
- [Parameters](ssh_connection.md#parameters)
- [Notes](ssh_connection.md#notes)

## [Synopsis](ssh_connection.md#id1)

- This connection plugin allows Ansible to communicate to the target machines through normal SSH command line.
- Ansible does not expose a channel to allow communication between the user and the SSH process to accept a password manually to decrypt an SSH key when using this connection plugin (which is the default). The use of `ssh-agent` is highly recommended.

## [Parameters](ssh_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **control_path**  string | This is the location to save SSH’s ControlPath sockets, it uses SSH’s variable substitution.  Since 2.3, if null (default), ansible will generate a unique hash. Use ``%(directory)s`` to indicate where to use the control dir path setting.  Before 2.3 it defaulted to ``control_path=%(directory)s/ansible-ssh-%%h-%%p-%%r``.  Be aware that this setting is ignored if `-o ControlPath` is set in ssh args.  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   control_path = VALUE   ``` - Environment variable: [`ANSIBLE_SSH_CONTROL_PATH`](../../environment_variables.md#envvar-ANSIBLE_SSH_CONTROL_PATH) - Variable: ansible_control_path  *added in Ansible 2.7* |
| **control_path_dir**  string | This sets the directory to use for ssh control path if the control path setting is null.  Also, provides the ``%(directory)s`` variable for the control path setting.  **Default:** `"~/.ansible/cp"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   control_path_dir = ~/.ansible/cp   ``` - Environment variable: [`ANSIBLE_SSH_CONTROL_PATH_DIR`](../../environment_variables.md#envvar-ANSIBLE_SSH_CONTROL_PATH_DIR) - Variable: ansible_control_path_dir  *added in Ansible 2.7* |
| **host**  string | Hostname/IP to connect to.  **Default:** `"inventory_hostname"`  **Configuration:**   - Variable: inventory_hostname - Variable: ansible_host - Variable: ansible_ssh_host - Variable: delegated_vars[‘ansible_host’] - Variable: delegated_vars[‘ansible_ssh_host’] |
| **host_key_checking**  boolean | Determines if SSH should check host keys.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   host_key_checking = true   ```  ```YAML+Jinja   [ssh_connection]   host_key_checking = true   ``` - Environment variable: [`ANSIBLE_HOST_KEY_CHECKING`](../../../reference_appendices/config.md#envvar-ANSIBLE_HOST_KEY_CHECKING) - Environment variable: [`ANSIBLE_SSH_HOST_KEY_CHECKING`](../../environment_variables.md#envvar-ANSIBLE_SSH_HOST_KEY_CHECKING) - Variable: ansible_host_key_checking - Variable: ansible_ssh_host_key_checking |
| **password**  string | Authentication password for the `remote_user`. Can be supplied as CLI option.  **Configuration:**   - Variable: ansible_password - Variable: ansible_ssh_pass - Variable: ansible_ssh_password |
| **pipelining**  boolean | Pipelining reduces the number of connection operations required to execute a module on the remote server, by executing many Ansible modules without actual file transfers.  This can result in a very significant performance improvement when enabled.  However this can conflict with privilege escalation (become). For example, when using sudo operations you must first disable ‘requiretty’ in the sudoers file for the target hosts, which is why this feature is disabled by default.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   pipelining = false   ```  ```YAML+Jinja   [connection]   pipelining = false   ```  ```YAML+Jinja   [ssh_connection]   pipelining = false   ``` - Environment variable: [`ANSIBLE_PIPELINING`](../../../reference_appendices/config.md#envvar-ANSIBLE_PIPELINING) - Environment variable: [`ANSIBLE_SSH_PIPELINING`](../../environment_variables.md#envvar-ANSIBLE_SSH_PIPELINING) - Variable: ansible_pipelining - Variable: ansible_ssh_pipelining |
| **pkcs11_provider**  string  *added in ansible-core 2.12* | PKCS11 SmartCard provider such as opensc, example: /usr/local/lib/opensc-pkcs11.so  Requires sshpass version 1.06+, sshpass must support the -P option.  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   pkcs11_provider = ""   ``` - Environment variable: [`ANSIBLE_PKCS11_PROVIDER`](../../environment_variables.md#envvar-ANSIBLE_PKCS11_PROVIDER) - Variable: ansible_ssh_pkcs11_provider |
| **port**  integer | Remote port to connect to.  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   remote_port = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_PORT`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_PORT) - Variable: ansible_port - Variable: ansible_ssh_port - Keyword: port |
| **private_key_file**  string | Path to private key file to use for authentication.  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   private_key_file = VALUE   ``` - Environment variable: [`ANSIBLE_PRIVATE_KEY_FILE`](../../../reference_appendices/config.md#envvar-ANSIBLE_PRIVATE_KEY_FILE) - Variable: ansible_private_key_file - Variable: ansible_ssh_private_key_file - CLI argument: –private-key |
| **reconnection_retries**  integer | Number of attempts to connect.  Ansible retries connections only if it gets an SSH error with a return code of 255.  Any errors with return codes other than 255 indicate an issue with program execution.  **Default:** `0`  **Configuration:**   - INI entries:  ```YAML+Jinja   [connection]   retries = 0   ```  ```YAML+Jinja   [ssh_connection]   retries = 0   ``` - Environment variable: [`ANSIBLE_SSH_RETRIES`](../../environment_variables.md#envvar-ANSIBLE_SSH_RETRIES) - Variable: ansible_ssh_retries  *added in Ansible 2.7* |
| **remote_user**  string | User name with which to login to the remote server, normally set by the remote_user keyword.  If no user is supplied, Ansible will let the SSH client binary choose the user as it normally.  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   remote_user = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_USER) - Variable: ansible_user - Variable: ansible_ssh_user - Keyword: remote_user - CLI argument: –user |
| **scp_executable**  string | This defines the location of the scp binary. It defaults to `scp` which will use the first binary available in $PATH.  **Default:** `"scp"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   scp_executable = scp   ``` - Environment variable: [`ANSIBLE_SCP_EXECUTABLE`](../../environment_variables.md#envvar-ANSIBLE_SCP_EXECUTABLE) - Variable: ansible_scp_executable  *added in Ansible 2.7* |
| **scp_extra_args**  string | Extra exclusive to the `scp` CLI  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   scp_extra_args = ""   ```  *added in Ansible 2.7* - Environment variable: [`ANSIBLE_SCP_EXTRA_ARGS`](../../environment_variables.md#envvar-ANSIBLE_SCP_EXTRA_ARGS)  *added in Ansible 2.7* - Variable: ansible_scp_extra_args - CLI argument: –scp-extra-args |
| **scp_if_ssh**  string  Removed in: version 2.17  Why: In favor of the “ssh_transfer_method” option.  Alternative: ssh_transfer_method | Preferred method to use when transferring files over SSH.  When set to *smart*, Ansible will try them until one succeeds or they all fail.  If set to *True*, it will force ‘scp’, if *False* it will use ‘sftp’.  For OpenSSH >=9.0 you must add an additional option to enable scp (scp_extra_args=”-O”)  This setting will overridden by ssh_transfer_method if set.  **Default:** `"smart"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   scp_if_ssh = smart   ``` - Environment variable: [`ANSIBLE_SCP_IF_SSH`](../../environment_variables.md#envvar-ANSIBLE_SCP_IF_SSH) - Variable: ansible_scp_if_ssh  *added in Ansible 2.7* |
| **sftp_batch_mode**  boolean | TODO: write it  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   sftp_batch_mode = true   ``` - Environment variable: [`ANSIBLE_SFTP_BATCH_MODE`](../../environment_variables.md#envvar-ANSIBLE_SFTP_BATCH_MODE) - Variable: ansible_sftp_batch_mode  *added in Ansible 2.7* |
| **sftp_executable**  string | This defines the location of the sftp binary. It defaults to `sftp` which will use the first binary available in $PATH.  **Default:** `"sftp"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   sftp_executable = sftp   ``` - Environment variable: [`ANSIBLE_SFTP_EXECUTABLE`](../../environment_variables.md#envvar-ANSIBLE_SFTP_EXECUTABLE) - Variable: ansible_sftp_executable  *added in Ansible 2.7* |
| **sftp_extra_args**  string | Extra exclusive to the `sftp` CLI  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   sftp_extra_args = ""   ```  *added in Ansible 2.7* - Environment variable: [`ANSIBLE_SFTP_EXTRA_ARGS`](../../environment_variables.md#envvar-ANSIBLE_SFTP_EXTRA_ARGS)  *added in Ansible 2.7* - Variable: ansible_sftp_extra_args - CLI argument: –sftp-extra-args |
| **ssh_args**  string | Arguments to pass to all SSH CLI tools.  **Default:** `"-C -o ControlMaster=auto -o ControlPersist=60s"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   ssh_args = -C -o ControlMaster=auto -o ControlPersist=60s   ``` - Environment variable: [`ANSIBLE_SSH_ARGS`](../../environment_variables.md#envvar-ANSIBLE_SSH_ARGS) - Variable: ansible_ssh_args  *added in Ansible 2.7* |
| **ssh_common_args**  string | Common extra args for all SSH CLI tools.  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   ssh_common_args = ""   ```  *added in Ansible 2.7* - Environment variable: [`ANSIBLE_SSH_COMMON_ARGS`](../../environment_variables.md#envvar-ANSIBLE_SSH_COMMON_ARGS)  *added in Ansible 2.7* - Variable: ansible_ssh_common_args - CLI argument: –ssh-common-args |
| **ssh_executable**  string | This defines the location of the SSH binary. It defaults to `ssh` which will use the first SSH binary available in $PATH.  This option is usually not required, it might be useful when access to system SSH is restricted, or when using SSH wrappers to connect to remote hosts.  **Default:** `"ssh"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   ssh_executable = ssh   ``` - Environment variable: [`ANSIBLE_SSH_EXECUTABLE`](../../environment_variables.md#envvar-ANSIBLE_SSH_EXECUTABLE) - Variable: ansible_ssh_executable  *added in Ansible 2.7* |
| **ssh_extra_args**  string | Extra exclusive to the SSH CLI.  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   ssh_extra_args = ""   ```  *added in Ansible 2.7* - Environment variable: [`ANSIBLE_SSH_EXTRA_ARGS`](../../environment_variables.md#envvar-ANSIBLE_SSH_EXTRA_ARGS)  *added in Ansible 2.7* - Variable: ansible_ssh_extra_args - CLI argument: –ssh-extra-args |
| **ssh_transfer_method**  string | Preferred method to use when transferring files over ssh  Setting to ‘smart’ (default) will try them in order, until one succeeds or they all fail  For OpenSSH >=9.0 you must add an additional option to enable scp (scp_extra_args=”-O”)  Using ‘piped’ creates an ssh pipe with `dd` on either side to copy the data  **Choices:**   - `"sftp"` - `"scp"` - `"piped"` - `"smart"`   **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   transfer_method = VALUE   ``` - Environment variable: [`ANSIBLE_SSH_TRANSFER_METHOD`](../../environment_variables.md#envvar-ANSIBLE_SSH_TRANSFER_METHOD) - Variable: ansible_ssh_transfer_method  *added in ansible-core 2.12* |
| **sshpass_prompt**  string  *added in ansible-base 2.10* | Password prompt that sshpass should search for. Supported by sshpass 1.06 and up.  Defaults to `Enter PIN for` when pkcs11_provider is set.  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   sshpass_prompt = ""   ``` - Environment variable: [`ANSIBLE_SSHPASS_PROMPT`](../../environment_variables.md#envvar-ANSIBLE_SSHPASS_PROMPT) - Variable: ansible_sshpass_prompt |
| **timeout**  integer | This is the default amount of time we will wait while establishing an SSH connection.  It also controls how long we can wait to access reading the connection once established (select on the socket).  **Default:** `10`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   timeout = 10   ```  ```YAML+Jinja   [ssh_connection]   timeout = 10   ```  *added in ansible-core 2.11* - Environment variable: [`ANSIBLE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_TIMEOUT) - Environment variable: [`ANSIBLE_SSH_TIMEOUT`](../../environment_variables.md#envvar-ANSIBLE_SSH_TIMEOUT)  *added in ansible-core 2.11* - Variable: ansible_ssh_timeout  *added in ansible-core 2.11* - CLI argument: –timeout |
| **use_tty**  boolean | add -tt to ssh commands to force tty allocation.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [ssh_connection]   usetty = true   ``` - Environment variable: [`ANSIBLE_SSH_USETTY`](../../environment_variables.md#envvar-ANSIBLE_SSH_USETTY) - Variable: ansible_ssh_use_tty  *added in Ansible 2.7* |

## [Notes](ssh_connection.md#id3)

> **Note:**
>
> - Many options default to `None` here but that only means we do not override the SSH tool’s defaults and/or configuration. For example, if you specify the port in this plugin it will override any `Port` entry in your `.ssh/config`.
> - The ssh CLI tool uses return code 255 as a ‘connection error’, this can conflict with commands/tools that also return 255 as an error code and will look like an ‘unreachable’ condition or ‘connection error’ to this plugin.

### Authors

- ansible (@core)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)

---
collection: ansible
version: "8"
title: "ansible.netcommon.network_cli connection – Use network_cli to run command on network appliances"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/network_cli_connection.html
fetched_at: 2026-07-28T01:04:33+00:00
---
# ansible.netcommon.network_cli connection – Use network_cli to run command on network appliances

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
> see [Requirements](network_cli_connection.md#ansible-collections-ansible-netcommon-network-cli-connection-requirements) for details.
>
> To use it in a playbook, specify: `ansible.netcommon.network_cli`.

New in ansible.netcommon 1.0.0

- [Synopsis](network_cli_connection.md#synopsis)
- [Requirements](network_cli_connection.md#requirements)
- [Parameters](network_cli_connection.md#parameters)

## [Synopsis](network_cli_connection.md#id1)

- This connection plugin provides a connection to remote devices over the SSH and implements a CLI shell. This connection plugin is typically used by network devices for sending and receiving CLi commands to network devices.

## [Requirements](network_cli_connection.md#id2)

The below requirements are needed on the local controller node that executes this connection.

- ansible-pylibssh if using *ssh_type=libssh*

## [Parameters](network_cli_connection.md#id3)

| Parameter | Comments |
| --- | --- |
| **become**  boolean | The become option will instruct the CLI session to attempt privilege escalation on platforms that support it. Normally this means transitioning from user mode to `enable` mode in the CLI session. If become is set to True and the remote device does not support privilege escalation or the privilege has already been elevated, then this option is silently ignored.  Can be configured from the CLI via the `--become` or `-b` options.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [privilege_escalation]   become = false   ``` - Environment variable: [`ANSIBLE_BECOME`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME) - Variable: ansible_become |
| **become_errors**  string | This option determines how privilege escalation failures are handled when *become* is enabled.  When set to `ignore`, the errors are silently ignored. When set to `warn`, a warning message is displayed. The default option `fail`, triggers a failure and halts execution.  **Choices:**   - `"ignore"` - `"warn"` - `"fail"` ← (default)   **Configuration:**   - Variable: ansible_network_become_errors |
| **become_method**  string | This option allows the become method to be specified in for handling privilege escalation. Typically the become_method value is set to `enable` but could be defined as other values.  **Default:** `"sudo"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [privilege_escalation]   become_method = sudo   ``` - Environment variable: [`ANSIBLE_BECOME_METHOD`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_METHOD) - Variable: ansible_become_method |
| **host**  string | Specifies the remote device FQDN or IP address to establish the SSH connection to.  **Default:** `"inventory_hostname"`  **Configuration:**   - Variable: inventory_hostname - Variable: ansible_host |
| **host_key_auto_add**  boolean | By default, Ansible will prompt the user before adding SSH keys to the known hosts file. Since persistent connections such as network_cli run in background processes, the user will never be prompted. By enabling this option, unknown host keys will automatically be added to the known hosts file.  Be sure to fully understand the security implications of enabling this option on production systems as it could create a security vulnerability.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [paramiko_connection]   host_key_auto_add = false   ``` - Environment variable: [`ANSIBLE_HOST_KEY_AUTO_ADD`](../../environment_variables.md#envvar-ANSIBLE_HOST_KEY_AUTO_ADD) |
| **host_key_checking**  boolean | Set this to “False” if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   host_key_checking = true   ```  ```YAML+Jinja   [persistent_connection]   host_key_checking = true   ``` - Environment variable: [`ANSIBLE_HOST_KEY_CHECKING`](../../../reference_appendices/config.md#envvar-ANSIBLE_HOST_KEY_CHECKING) - Environment variable: [`ANSIBLE_SSH_HOST_KEY_CHECKING`](../../environment_variables.md#envvar-ANSIBLE_SSH_HOST_KEY_CHECKING) - Variable: ansible_host_key_checking - Variable: ansible_ssh_host_key_checking |
| **import_modules**  boolean | Reduce CPU usage and network module execution time by enabling direct execution. Instead of the module being packaged and executed by the shell, it will be directly executed by the Ansible control node using the same python interpreter as the Ansible process. Note- Incompatible with `asynchronous mode`. Note- Python 3 and Ansible 2.9.16 or greater required. Note- With Ansible 2.9.x fully qualified modules names are required in tasks.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [ansible_network]   import_modules = true   ``` - Environment variable: [`ANSIBLE_NETWORK_IMPORT_MODULES`](../../environment_variables.md#envvar-ANSIBLE_NETWORK_IMPORT_MODULES) - Variable: ansible_network_import_modules |
| **network_cli_retries**  integer | Number of attempts to connect to remote host. The delay time between the retires increases after every attempt by power of 2 in seconds till either the maximum attempts are exhausted or any of the `persistent_command_timeout` or `persistent_connect_timeout` timers are triggered.  **Default:** `3`  **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   network_cli_retries = 3   ``` - Environment variable: [`ANSIBLE_NETWORK_CLI_RETRIES`](../../environment_variables.md#envvar-ANSIBLE_NETWORK_CLI_RETRIES) - Variable: ansible_network_cli_retries |
| **network_os**  string | Configures the device platform network operating system. This value is used to load the correct terminal and cliconf plugins to communicate with the remote device.  **Configuration:**   - Variable: ansible_network_os |
| **password**  string | Configures the user password used to authenticate to the remote device when first establishing the SSH connection.  **Configuration:**   - Variable: ansible_password - Variable: ansible_ssh_pass - Variable: ansible_ssh_password |
| **persistent_buffer_read_timeout**  float | Configures, in seconds, the amount of time to wait for the data to be read from Paramiko channel after the command prompt is matched. This timeout value ensures that command prompt matched is correct and there is no more data left to be received from remote host.  **Default:** `0.1`  **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   buffer_read_timeout = 0.1   ``` - Environment variable: [`ANSIBLE_PERSISTENT_BUFFER_READ_TIMEOUT`](../../environment_variables.md#envvar-ANSIBLE_PERSISTENT_BUFFER_READ_TIMEOUT) - Variable: ansible_buffer_read_timeout |
| **persistent_command_timeout**  integer | Configures, in seconds, the amount of time to wait for a command to return from the remote device. If this timer is exceeded before the command returns, the connection plugin will raise an exception and close.  **Default:** `30`  **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   command_timeout = 30   ``` - Environment variable: [`ANSIBLE_PERSISTENT_COMMAND_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_PERSISTENT_COMMAND_TIMEOUT) - Variable: ansible_command_timeout |
| **persistent_connect_timeout**  integer | Configures, in seconds, the amount of time to wait when trying to initially establish a persistent connection. If this value expires before the connection to the remote device is completed, the connection will fail.  **Default:** `30`  **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   connect_timeout = 30   ``` - Environment variable: [`ANSIBLE_PERSISTENT_CONNECT_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_PERSISTENT_CONNECT_TIMEOUT) - Variable: ansible_connect_timeout |
| **persistent_log_messages**  boolean | This flag will enable logging the command executed and response received from target device in the ansible log file. For this option to work ‘log_path’ ansible configuration option is required to be set to a file path with write access.  Be sure to fully understand the security implications of enabling this option as it could create a security vulnerability by logging sensitive information in log file.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   log_messages = false   ``` - Environment variable: [`ANSIBLE_PERSISTENT_LOG_MESSAGES`](../../environment_variables.md#envvar-ANSIBLE_PERSISTENT_LOG_MESSAGES) - Variable: ansible_persistent_log_messages |
| **port**  integer | Specifies the port on the remote device that listens for connections when establishing the SSH connection.  **Default:** `22`  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   remote_port = 22   ``` - Environment variable: [`ANSIBLE_REMOTE_PORT`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_PORT) - Variable: ansible_port |
| **private_key_file**  string | The private SSH key or certificate file used to authenticate to the remote device when first establishing the SSH connection.  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   private_key_file = VALUE   ``` - Environment variable: [`ANSIBLE_PRIVATE_KEY_FILE`](../../../reference_appendices/config.md#envvar-ANSIBLE_PRIVATE_KEY_FILE) - Variable: ansible_private_key_file |
| **remote_user**  string | The username used to authenticate to the remote device when the SSH connection is first established. If the remote_user is not specified, the connection will use the username of the logged in user.  Can be configured from the CLI via the `--user` or `-u` options.  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   remote_user = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_USER) - Variable: ansible_user |
| **single_user_mode**  boolean  *added in ansible.netcommon 2.0.0* | This option enables caching of data fetched from the target for re-use. The cache is invalidated when the target device enters configuration mode.  Applicable only for platforms where this has been implemented.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - Environment variable: [`ANSIBLE_NETWORK_SINGLE_USER_MODE`](../../environment_variables.md#envvar-ANSIBLE_NETWORK_SINGLE_USER_MODE) - Variable: ansible_network_single_user_mode |
| **ssh_type**  string | The python package that will be used by the `network_cli` connection plugin to create a SSH connection to remote host.  *libssh* will use the ansible-pylibssh package, which needs to be installed in order to work.  *paramiko* will instead use the paramiko package to manage the SSH connection.  *auto* will use ansible-pylibssh if that package is installed, otherwise will fallback to paramiko.  **Choices:**   - `"libssh"` - `"paramiko"` - `"auto"` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   ssh_type = auto   ``` - Environment variable: [`ANSIBLE_NETWORK_CLI_SSH_TYPE`](../../environment_variables.md#envvar-ANSIBLE_NETWORK_CLI_SSH_TYPE) - Variable: ansible_network_cli_ssh_type |
| **terminal_errors**  string  *added in ansible.netcommon 3.1.0* | This option determines how failures while setting terminal parameters are handled.  When set to `ignore`, the errors are silently ignored. When set to `warn`, a warning message is displayed. The default option `fail`, triggers a failure and halts execution.  **Choices:**   - `"ignore"` - `"warn"` - `"fail"` ← (default)   **Configuration:**   - Variable: ansible_network_terminal_errors |
| **terminal_inital_prompt_newline**  boolean | This boolean flag, that when set to *True* will send newline in the response if any of values in *terminal_initial_prompt* is matched.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - Variable: ansible_terminal_initial_prompt_newline |
| **terminal_initial_answer**  list / elements=string | The answer to reply with if the `terminal_initial_prompt` is matched. The value can be a single answer or a list of answers for multiple terminal_initial_prompt. In case the login menu has multiple prompts the sequence of the prompt and excepted answer should be in same order and the value of *terminal_prompt_checkall* should be set to *True* if all the values in `terminal_initial_prompt` are expected to be matched and set to *False* if any one login prompt is to be matched.  **Configuration:**   - Variable: ansible_terminal_initial_answer |
| **terminal_initial_prompt**  list / elements=string | A single regex pattern or a sequence of patterns to evaluate the expected prompt at the time of initial login to the remote host.  **Configuration:**   - Variable: ansible_terminal_initial_prompt |
| **terminal_initial_prompt_checkall**  boolean | By default the value is set to *False* and any one of the prompts mentioned in `terminal_initial_prompt` option is matched it won’t check for other prompts. When set to *True* it will check for all the prompts mentioned in `terminal_initial_prompt` option in the given order and all the prompts should be received from remote host if not it will result in timeout.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - Variable: ansible_terminal_initial_prompt_checkall |
| **terminal_stderr_re**  list / elements=dictionary | This option provides the regex pattern and optional flags to match the error string from the received response chunk. This option accepts `pattern` and `flags` keys. The value of `pattern` is a python regex pattern to match the response and the value of `flags` is the value accepted by *flags* argument of *re.compile* python method to control the way regex is matched with the response, for example *‘re.I’*.  **Configuration:**   - Variable: ansible_terminal_stderr_re |
| **terminal_stdout_re**  list / elements=dictionary | A single regex pattern or a sequence of patterns along with optional flags to match the command prompt from the received response chunk. This option accepts `pattern` and `flags` keys. The value of `pattern` is a python regex pattern to match the response and the value of `flags` is the value accepted by *flags* argument of *re.compile* python method to control the way regex is matched with the response, for example *‘re.I’*.  **Configuration:**   - Variable: ansible_terminal_stdout_re |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)

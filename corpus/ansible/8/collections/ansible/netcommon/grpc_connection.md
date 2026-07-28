---
collection: ansible
version: "8"
title: "ansible.netcommon.grpc connection – Provides a persistent connection using the gRPC protocol"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/grpc_connection.html
fetched_at: 2026-07-28T01:09:16+00:00
---
# ansible.netcommon.grpc connection – Provides a persistent connection using the gRPC protocol

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
> see [Requirements](grpc_connection.md#ansible-collections-ansible-netcommon-grpc-connection-requirements) for details.
>
> To use it in a playbook, specify: `ansible.netcommon.grpc`.

New in ansible.netcommon 3.1.0

- [Synopsis](grpc_connection.md#synopsis)
- [Requirements](grpc_connection.md#requirements)
- [Parameters](grpc_connection.md#parameters)

## [Synopsis](grpc_connection.md#id1)

- This connection plugin provides a connection to remote devices over gRPC and is typically used with devices for sending and receiving RPC calls over gRPC framework.
- Note this connection plugin requires the grpcio python library to be installed on the local Ansible controller.

## [Requirements](grpc_connection.md#id2)

The below requirements are needed on the local controller node that executes this connection.

- grpcio
- protobuf

## [Parameters](grpc_connection.md#id3)

| Parameter | Comments |
| --- | --- |
| **certificate_chain_file**  string | The PEM encoded certificate chain file used to create a SSL-enabled channel. If the value is None, no certificate chain is used.  **Configuration:**   - INI entry:  ```YAML+Jinja   [grpc_connection]   certificate_chain_file = VALUE   ``` - Environment variable: [`ANSIBLE_CERTIFICATE_CHAIN_FILE`](../../environment_variables.md#envvar-ANSIBLE_CERTIFICATE_CHAIN_FILE) - Variable: ansible_certificate_chain_file |
| **grpc_type**  string | This option indicates the grpc type and it can be used in place of network_os. (example cisco.iosxr.iosxr)  **Default:** `false`  **Configuration:**   - INI entry:  ```YAML+Jinja   [grpc_connection]   type = false   ``` - Environment variable: [`ANSIBLE_GRPC_CONNECTION_TYPE`](../../environment_variables.md#envvar-ANSIBLE_GRPC_CONNECTION_TYPE) - Variable: ansible_grpc_connection_type |
| **host**  string | Specifies the remote device FQDN or IP address to establish the gRPC connection to.  **Default:** `"inventory_hostname"`  **Configuration:**   - Variable: ansible_host |
| **import_modules**  boolean | Reduce CPU usage and network module execution time by enabling direct execution. Instead of the module being packaged and executed by the shell, it will be directly executed by the Ansible control node using the same python interpreter as the Ansible process. Note- Incompatible with `asynchronous mode`. Note- Python 3 and Ansible 2.9.16 or greater required. Note- With Ansible 2.9.x fully qualified modules names are required in tasks.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [ansible_network]   import_modules = true   ``` - Environment variable: [`ANSIBLE_NETWORK_IMPORT_MODULES`](../../environment_variables.md#envvar-ANSIBLE_NETWORK_IMPORT_MODULES) - Variable: ansible_network_import_modules |
| **network_os**  string | Configures the device platform network operating system. This value is used to load a device specific grpc plugin to communicate with the remote device.  **Configuration:**   - Variable: ansible_network_os |
| **password**  string | Configures the user password used to authenticate to the remote device when first establishing the gRPC connection.  **Configuration:**   - Variable: ansible_password - Variable: ansible_ssh_pass |
| **persistent_command_timeout**  integer | Configures, in seconds, the amount of time to wait for a command to return from the remote device. If this timer is exceeded before the command returns, the connection plugin will raise an exception and close.  **Default:** `30`  **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   command_timeout = 30   ``` - Environment variable: [`ANSIBLE_PERSISTENT_COMMAND_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_PERSISTENT_COMMAND_TIMEOUT) - Variable: ansible_command_timeout |
| **persistent_connect_timeout**  integer | Configures, in seconds, the amount of time to wait when trying to initially establish a persistent connection. If this value expires before the connection to the remote device is completed, the connection will fail.  **Default:** `30`  **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   connect_timeout = 30   ``` - Environment variable: [`ANSIBLE_PERSISTENT_CONNECT_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_PERSISTENT_CONNECT_TIMEOUT) - Variable: ansible_connect_timeout |
| **persistent_log_messages**  boolean | This flag will enable logging the command executed and response received from target device in the ansible log file. For this option to work ‘log_path’ ansible configuration option is required to be set to a file path with write access.  Be sure to fully understand the security implications of enabling this option as it could create a security vulnerability by logging sensitive information in log file.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [persistent_connection]   log_messages = false   ``` - Environment variable: [`ANSIBLE_PERSISTENT_LOG_MESSAGES`](../../environment_variables.md#envvar-ANSIBLE_PERSISTENT_LOG_MESSAGES) - Variable: ansible_persistent_log_messages |
| **port**  integer | Specifies the port on the remote device that listens for connections when establishing the gRPC connection. If None only the `host` part will be used.  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   remote_port = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_PORT`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_PORT) - Variable: ansible_port |
| **private_key_file**  string | The PEM encoded private key file used to authenticate to the remote device when first establishing the grpc connection.  **Configuration:**   - INI entry:  ```YAML+Jinja   [grpc_connection]   private_key_file = VALUE   ``` - Environment variable: [`ANSIBLE_PRIVATE_KEY_FILE`](../../../reference_appendices/config.md#envvar-ANSIBLE_PRIVATE_KEY_FILE) - Variable: ansible_private_key_file |
| **remote_user**  string | The username used to authenticate to the remote device when the gRPC connection is first established. If the remote_user is not specified, the connection will use the username of the logged in user.  Can be configured from the CLI via the `--user` or `-u` options.  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   remote_user = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_USER) - Variable: ansible_user |
| **root_certificates_file**  string | The PEM encoded root certificate file used to create a SSL-enabled channel, if the value is None it reads the root certificates from a default location chosen by gRPC at runtime.  **Configuration:**   - INI entry:  ```YAML+Jinja   [grpc_connection]   root_certificates_file = VALUE   ``` - Environment variable: [`ANSIBLE_ROOT_CERTIFICATES_FILE`](../../environment_variables.md#envvar-ANSIBLE_ROOT_CERTIFICATES_FILE) - Variable: ansible_root_certificates_file |
| **ssl_target_name_override**  string | The option overrides SSL target name used for SSL host name checking. The name used for SSL host name checking will be the target parameter (assuming that the secure channel is an SSL channel). If this parameter is specified and the underlying is not an SSL channel, it will just be ignored.  **Configuration:**   - INI entry:  ```YAML+Jinja   [grpc_connection]   ssl_target_name_override = VALUE   ``` - Environment variable: [`ANSIBLE_GPRC_SSL_TARGET_NAME_OVERRIDE`](../../environment_variables.md#envvar-ANSIBLE_GPRC_SSL_TARGET_NAME_OVERRIDE) - Variable: ansible_grpc_ssl_target_name_override |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)

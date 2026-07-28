---
collection: ansible
version: "8"
title: "ansible.builtin.winrm connection – Run tasks over Microsoft’s WinRM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/winrm_connection.html
fetched_at: 2026-07-28T01:05:16+00:00
---
# ansible.builtin.winrm connection – Run tasks over Microsoft’s WinRM

> **Note:**
>
> This connection plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `winrm`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.winrm` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same connection plugin name.

- [Synopsis](winrm_connection.md#synopsis)
- [Requirements](winrm_connection.md#requirements)
- [Parameters](winrm_connection.md#parameters)

## [Synopsis](winrm_connection.md#id1)

- Run commands or put/fetch on a target via WinRM
- This plugin allows extra arguments to be passed that are supported by the protocol but not explicitly defined here. They should take the form of variables declared with the following pattern `ansible_winrm_<option>`.

## [Requirements](winrm_connection.md#id2)

The below requirements are needed on the local controller node that executes this connection.

- pywinrm (python library)

## [Parameters](winrm_connection.md#id3)

| Parameter | Comments |
| --- | --- |
| **connection_timeout**  integer | Despite its name, sets both the ‘operation’ and ‘read’ timeout settings for the WinRM connection.  The operation timeout belongs to the WS-Man layer and runs on the winRM-service on the managed windows host.  The read timeout belongs to the underlying python Request call (http-layer) and runs on the ansible controller.  The operation timeout sets the WS-Man ‘Operation timeout’ that runs on the managed windows host. The operation timeout specifies how long a command will run on the winRM-service before it sends the message ‘WinRMOperationTimeoutError’ back to the client. The client (silently) ignores this message and starts a new instance of the operation timeout, waiting for the command to finish (long running commands).  The read timeout sets the client HTTP-request timeout and specifies how long the client (ansible controller) will wait for data from the server to come back over the HTTP-connection (timeout for waiting for in-between messages from the server). When this timer expires, an exception will be thrown and the ansible connection will be terminated with the error message ‘Read timed out’  To avoid the above exception to be thrown, the read timeout will be set to 10 seconds higher than the WS-Man operation timeout, thus make the connection more robust on networks with long latency and/or many hops between server and client network wise.  Setting the difference bewteen the operation and the read timeout to 10 seconds alligns it to the defaults used in the winrm-module and the PSRP-module which also uses 10 seconds (30 seconds for read timeout and 20 seconds for operation timeout)  Corresponds to the `operation_timeout_sec` and `read_timeout_sec` args in pywinrm so avoid setting these vars with this one.  The default value is whatever is set in the installed version of pywinrm.  **Configuration:**   - Variable: ansible_winrm_connection_timeout |
| **kerberos_command**  string | kerberos command to use to request a authentication ticket  **Default:** `"kinit"`  **Configuration:**   - Variable: ansible_winrm_kinit_cmd |
| **kerberos_mode**  string | kerberos usage mode.  The managed option means Ansible will obtain kerberos ticket.  While the manual one means a ticket must already have been obtained by the user.  If having issues with Ansible freezing when trying to obtain the Kerberos ticket, you can either set this to `manual` and obtain it outside Ansible or install `pexpect` through pip and try again.  **Choices:**   - `"managed"` - `"manual"`   **Configuration:**   - Variable: ansible_winrm_kinit_mode |
| **kinit_args**  string  *added in ansible-core 2.11* | Extra arguments to pass to `kinit` when getting the Kerberos authentication ticket.  By default no extra arguments are passed into `kinit` unless *ansible_winrm_kerberos_delegation* is also set. In that case `-f` is added to the `kinit` args so a forwardable ticket is retrieved.  If set, the args will overwrite any existing defaults for `kinit`, including `-f` for a delegated ticket.  **Configuration:**   - Variable: ansible_winrm_kinit_args |
| **kinit_env_vars**  list / elements=string  *added in ansible-core 2.12* | A list of environment variables to pass through to `kinit` when getting the Kerberos authentication ticket.  By default no environment variables are passed through and `kinit` is run with a blank slate.  The environment variable `KRB5CCNAME` cannot be specified here as it’s used to store the temp Kerberos ticket used by WinRM.  **Default:** `[]`  **Configuration:**   - INI entry:  ```YAML+Jinja   [winrm]   kinit_env_vars =   ``` - Variable: ansible_winrm_kinit_env_vars |
| **path**  string | URI path to connect to  **Default:** `"/wsman"`  **Configuration:**   - Variable: ansible_winrm_path |
| **pipelining**  boolean | Pipelining reduces the number of connection operations required to execute a module on the remote server, by executing many Ansible modules without actual file transfers.  This can result in a very significant performance improvement when enabled.  However this can conflict with privilege escalation (become). For example, when using sudo operations you must first disable ‘requiretty’ in the sudoers file for the target hosts, which is why this feature is disabled by default.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   pipelining = false   ```  ```YAML+Jinja   [connection]   pipelining = false   ``` - Environment variable: [`ANSIBLE_PIPELINING`](../../../reference_appendices/config.md#envvar-ANSIBLE_PIPELINING) - Variable: ansible_pipelining |
| **port**  integer | port for winrm to connect on remote target  The default is the https (5986) port, if using http it should be 5985  **Default:** `5986`  **Configuration:**   - Variable: ansible_port - Variable: ansible_winrm_port - Keyword: port |
| **remote_addr**  string | Address of the windows machine  **Default:** `"inventory_hostname"`  **Configuration:**   - Variable: inventory_hostname - Variable: ansible_host - Variable: ansible_winrm_host |
| **remote_password**  aliases: password  string | Authentication password for the `remote_user`. Can be supplied as CLI option.  **Configuration:**   - Variable: ansible_password - Variable: ansible_winrm_pass - Variable: ansible_winrm_password |
| **remote_user**  string | The user to log in as to the Windows machine  **Configuration:**   - Variable: ansible_user - Variable: ansible_winrm_user - Keyword: remote_user |
| **scheme**  string | URI scheme to use  If not set, then will default to `https` or `http` if *port* is `5985`.  **Choices:**   - `"http"` - `"https"`   **Configuration:**   - Variable: ansible_winrm_scheme |
| **transport**  list / elements=string | List of winrm transports to attempt to use (ssl, plaintext, kerberos, etc)  If None (the default) the plugin will try to automatically guess the correct list  The choices available depend on your version of pywinrm  **Configuration:**   - Variable: ansible_winrm_transport |

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)

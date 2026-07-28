---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_command module – Run TMSH and BASH commands on F5 devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_command_module.html
fetched_at: 2026-07-27T17:26:19+00:00
---
# f5networks.f5_modules.bigip_command module – Run TMSH and BASH commands on F5 devices

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_command`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_command_module.md#synopsis)
- [Parameters](bigip_command_module.md#parameters)
- [Notes](bigip_command_module.md#notes)
- [Examples](bigip_command_module.md#examples)
- [Return Values](bigip_command_module.md#return-values)

## [Synopsis](bigip_command_module.md#id1)

- Sends a TMSH or BASH command to a BIG-IP node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
- This module is **not** idempotent, nor will it ever be. It is intended as a stop-gap measure to satisfy automation requirements until such a time as a real module has been developed to configure in the way you need.
- If you are using this module, we recommend also filing an issue to have a **real** module created for your needs.

## [Parameters](bigip_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **chdir**  string | Change into this directory before running the command. |
| **commands**  any / required | The commands to send to the remote BIG-IP device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired.  Only `tmsh` commands are supported. If you are piping or adding additional logic that is outside of `tmsh` (such as grep’ing, awk’ing or other shell related logic that are not `tmsh`), this behavior is not supported. |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditional, the interval indicates how to long to wait before trying the command again.  Default: `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all`, then all conditionals in the *wait_for* must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  Choices:   - `"any"` - `"all"` ← (default) |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **ssh_keyfile**  path | Specifies the SSH keyfile to use to authenticate the connection to the remote device. This argument is only used for *cli* transports.  You may omit this option by setting the environment variable `ANSIBLE_NET_SSH_KEYFILE`. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **retries**  integer | Specifies the number of retries a command should be tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditionals.  Default: `10` |
| **wait_for**  aliases: waitfor  list / elements=string | Specifies what to evaluate from the output of the command and what conditionals to apply. This argument will cause the task to wait for a particular conditional to be true before moving forward. If the conditional is not true by the configured retries, the task fails. See the examples. |
| **warn**  boolean | Whether the module should raise warnings related to command idempotency or not.  Note that the F5 Ansible developers specifically leave this on to make you aware that your usage of this module may be better served by official F5 Ansible modules. This module should always be used as a last resort.  Choices:   - `false` - `true` ← (default) |

## [Notes](bigip_command_module.md#id3)

> **Note:**
>
> - When running this module in an HA environment via SSH connection and using a role other than `admin` or `root`, you may see a `Change Pending` status, even if you did not make any changes. This is being tracked with ID429869.
> - When using the bigip_command module with the REST API, there are a number of places regex is used internally to escape characters such as quotation marks. If your TMSH command contains regex characters itself, such as datagroup wildcards `*`, then a large amount of escape characters may be needed.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_command_module.md#id4)

```yaml+jinja
- name: run show version on remote devices
  bigip_command:
    commands: show sys version
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  delegate_to: localhost

- name: run show version and check to see if output contains BIG-IP
  bigip_command:
    commands: show sys version
    wait_for: result[0] contains BIG-IP
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  register: result
  delegate_to: localhost

- name: run multiple commands on remote nodes
  bigip_command:
    commands:
      - show sys version
      - list ltm virtual
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  delegate_to: localhost

- name: run multiple commands and evaluate the output
  bigip_command:
    commands:
      - show sys version
      - list ltm virtual
    wait_for:
      - result[0] contains BIG-IP
      - result[1] contains my-vs
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  register: result
  delegate_to: localhost

- name: tmsh prefixes will automatically be handled
  bigip_command:
    commands:
      - show sys version
      - tmsh list ltm virtual
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  delegate_to: localhost

- name: Delete all LTM nodes in Partition1, assuming no dependencies exist
  bigip_command:
    commands:
      - delete ltm node all
    chdir: Partition1
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  delegate_to: localhost

- name: Command that contains wildcard character to be passed to tmsh
  bigip_command:
    commands:
      - modify ltm data-group internal dg_string records add { "my test\\\\\\\*string"  { data "value" }}
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed.  Returned: failed  Sample: `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands.  Returned: always  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list.  Returned: always  Sample: `[["...", "..."], ["..."], ["..."]]` |
| **warn**  boolean | Whether or not to raise warnings about modification commands.  Returned: changed  Sample: `true` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

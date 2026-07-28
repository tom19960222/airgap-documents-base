---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_command module – Run arbitrary commands on an Juniper JUNOS device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_command_module.html
fetched_at: 2026-07-27T17:54:13+00:00
---
# junipernetworks.junos.junos_command module – Run arbitrary commands on an Juniper JUNOS device

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_command_module.md#ansible-collections-junipernetworks-junos-junos-command-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_command`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_command_module.md#synopsis)
- [Requirements](junos_command_module.md#requirements)
- [Parameters](junos_command_module.md#parameters)
- [Notes](junos_command_module.md#notes)
- [Examples](junos_command_module.md#examples)
- [Return Values](junos_command_module.md#return-values)

## [Synopsis](junos_command_module.md#id1)

- Sends an arbitrary set of commands to an JUNOS node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_command_module.md#id2)

The below requirements are needed on the host that executes this module.

- jxmlease
- ncclient (>=v0.5.2)

## [Parameters](junos_command_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=string | The commands to send to the remote junos device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of *retries* has been exceeded. |
| **display**  aliases: format, output  string | Encoding scheme to use when serializing output from the device. This handles how to properly understand the output and apply the conditionals path to the result set. For *rpcs* argument default display is `xml` and for *commands* argument default display is `text`. Value `set` is applicable only for fetching configuration from device.  Choices:   - `"text"` - `"json"` - `"xml"` - `"set"` |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditional, the interval indicates how to long to wait before trying the command again.  Default: `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the *wait_for* must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  Choices:   - `"any"` - `"all"` ← (default) |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` or `connection: netconf`.  For more information please see the [Junos OS Platform Options guide](../network/user_guide/platform_junos.md).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. The port value will default to the well known SSH port of 22 (for `transport=cli`) or port 830 (for `transport=netconf`) device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` - `"netconf"` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **retries**  integer | Specifies the number of retries a command should be tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditionals.  Default: `10` |
| **rpcs**  list / elements=string | The `rpcs` argument accepts a list of RPCs to be executed over a netconf session and the results from the RPC execution is return to the playbook via the modules results dictionary. |
| **wait_for**  aliases: waitfor  list / elements=string | Specifies what to evaluate from the output of the command and what conditionals to apply. This argument will cause the task to wait for a particular conditional to be true before moving forward. If the conditional is not true by the configured retries, the task fails. See examples. |

## [Notes](junos_command_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Recommended connection is `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - This module also works with `network_cli` connections and with `local` connections for legacy playbooks.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_command_module.md#id5)

```yaml+jinja
- name: run show version on remote devices
  junipernetworks.junos.junos_command:
    commands: show version

- name: run show version and check to see if output contains Juniper
  junipernetworks.junos.junos_command:
    commands: show version
    wait_for: result[0] contains Juniper

- name: run multiple commands on remote nodes
  junipernetworks.junos.junos_command:
    commands:
    - show version
    - show interfaces

- name: run multiple commands and evaluate the output
  junipernetworks.junos.junos_command:
    commands:
    - show version
    - show interfaces
    wait_for:
    - result[0] contains Juniper
    - result[1] contains Loopback0

- name: run commands and specify the output format
  junipernetworks.junos.junos_command:
    commands: show version
    display: json

- name: run rpc on the remote device
  junipernetworks.junos.junos_command:
    commands: show configuration
    display: set

- name: run rpc on the remote device
  junipernetworks.junos.junos_command:
    rpcs: get-software-information
```

## [Return Values](junos_command_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  Returned: failed  Sample: `["...", "..."]` |
| **output**  list / elements=string | The set of transformed xml to json format from the commands responses  Returned: If the *display* is in `xml` format.  Sample: `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  Returned: always apart from low level errors (such as action plugin)  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  Returned: always apart from low level errors (such as action plugin)  Sample: `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)

---
collection: ansible
version: "6"
title: "community.network.cnos_conditional_template module – Manage switch configuration using templates based on condition on devices running Lenovo CNOS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/cnos_conditional_template_module.html
fetched_at: 2026-07-27T17:18:06+00:00
---
# community.network.cnos_conditional_template module – Manage switch configuration using templates based on condition on devices running Lenovo CNOS

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.cnos_conditional_template`.

- [Synopsis](cnos_conditional_template_module.md#synopsis)
- [Parameters](cnos_conditional_template_module.md#parameters)
- [Notes](cnos_conditional_template_module.md#notes)
- [Examples](cnos_conditional_template_module.md#examples)
- [Return Values](cnos_conditional_template_module.md#return-values)

## [Synopsis](cnos_conditional_template_module.md#id1)

- This module allows you to work with the running configuration of a switch. It provides a way to execute a set of CNOS commands on a switch by evaluating the current running configuration and executing the commands only if the specific settings have not been already configured. The configuration source can be a set of commands or a template written in the Jinja2 templating language. This module functions the same as the cnos_template module. The only exception is that the following inventory variable can be specified. [“condition = <flag string>”] When this inventory variable is specified as the variable of a task, the template is executed for the network element that matches the flag string. Usually, templates are used when commands are the same across a group of network devices. When there is a requirement to skip the execution of the template on one or more devices, it is recommended to use this module. This module uses SSH to manage network device configuration.

## [Parameters](cnos_conditional_template_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commandfile**  string / required | This specifies the path to the CNOS command file which needs to be applied. This usually comes from the commands folder. Generally this file is the output of the variables applied on a template file. So this command is preceded by a template module. The command file must contain the Ansible keyword {{ inventory_hostname }} and the condition flag in its filename to ensure that the command file is unique for each switch and condition. If this is omitted, the command file will be overwritten during iteration. For example, commandfile=./commands/clos_leaf_bgp_ {{ inventory_hostname }}_LP21_commands.txt |
| **condition**  string / required | If you specify condition=<flag string> in the inventory file against any device, the template execution is done for that device in case it matches the flag setting for that task. |
| **deviceType**  string / required | This specifies the type of device where the method is executed. The choices NE1072T,NE1032,NE1032T,NE10032,NE2572 are added since Ansible 2.4. The choice NE0152T is added since 2.8  Choices:   - `"g8272_cnos"` - `"g8296_cnos"` - `"g8332_cnos"` - `"NE0152T"` - `"NE1072T"` - `"NE1032"` - `"NE1032T"` - `"NE10032"` - `"NE2572"` |
| **enablePassword**  string | Configures the password used to enter Global Configuration command mode on the switch. If the switch does not request this password, the parameter is ignored.While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |
| **flag**  string / required | If a task needs to be executed, you have to set the flag the same as it is specified in the inventory for that device. |
| **host**  string / required | This is the variable used to search the hosts file at /etc/ansible/hosts and identify the IP address of the device on which the template is going to be applied. Usually the Ansible keyword {{ inventory_hostname }} is specified in the playbook as an abstraction of the group of network elements that need to be configured. |
| **outputfile**  string / required | This specifies the file path where the output of each command execution is saved. Each command that is specified in the merged template file and each response from the device are saved here. Usually the location is the results folder, but you can choose another location based on your write permission. |
| **password**  string / required | Configures the password used to authenticate the connection to the remote device. The value of the password parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |
| **username**  string / required | Configures the username used to authenticate the connection to the remote device. The value of the username parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |

## [Notes](cnos_conditional_template_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage Lenovo Network devices see <https://www.ansible.com/ansible-lenovo>.

## [Examples](cnos_conditional_template_module.md#id4)

```yaml+jinja
Tasks : The following are examples of using the module
 cnos_conditional_template. These are written in the main.yml file of the
 tasks directory.
---
- name: Applying CLI template on VLAG Tier1 Leaf Switch1
  community.network.cnos_conditional_template:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/vlag_1tier_leaf_switch1_
                  {{ inventory_hostname }}_output.txt"
      condition: "{{ hostvars[inventory_hostname]['condition']}}"
      flag: "leaf_switch1"
      commandfile: "./commands/vlag_1tier_leaf_switch1_
                    {{ inventory_hostname }}_commands.txt"
      stp_mode1: "disable"
      port_range1: "17,18,29,30"
      portchannel_interface_number1: 1001
      portchannel_mode1: active
      slot_chassis_number1: 1/48
      switchport_mode1: trunk
```

## [Return Values](cnos_conditional_template_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success or failure message  Returned: always  Sample: `"Template Applied."` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)

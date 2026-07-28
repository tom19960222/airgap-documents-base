---
collection: ansible
version: "8"
title: "community.network.cnos_reload module – Perform switch restart on devices running Lenovo CNOS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/cnos_reload_module.html
fetched_at: 2026-07-28T01:56:16+00:00
---
# community.network.cnos_reload module – Perform switch restart on devices running Lenovo CNOS

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.cnos_reload`.

- [Synopsis](cnos_reload_module.md#synopsis)
- [Parameters](cnos_reload_module.md#parameters)
- [Notes](cnos_reload_module.md#notes)
- [Examples](cnos_reload_module.md#examples)
- [Return Values](cnos_reload_module.md#return-values)

## [Synopsis](cnos_reload_module.md#id1)

- This module allows you to restart the switch using the current startup configuration. The module is usually invoked after the running configuration has been saved over the startup configuration. This module uses SSH to manage network device configuration. The results of the operation can be viewed in results directory.

Aliases: network.cnos.cnos_reload

## [Parameters](cnos_reload_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **deviceType**  string / required | This specifies the type of device where the method is executed. The choices NE1072T,NE1032,NE1032T,NE10032,NE2572 are added since Ansible 2.4. The choice NE0152T is added since 2.8  **Choices:**   - `"g8272_cnos"` - `"g8296_cnos"` - `"g8332_cnos"` - `"NE0152T"` - `"NE1072T"` - `"NE1032"` - `"NE1032T"` - `"NE10032"` - `"NE2572"` |
| **enablePassword**  string | Configures the password used to enter Global Configuration command mode on the switch. If the switch does not request this password, the parameter is ignored.While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |
| **host**  string / required | This is the variable used to search the hosts file at /etc/ansible/hosts and identify the IP address of the device on which the template is going to be applied. Usually the Ansible keyword {{ inventory_hostname }} is specified in the playbook as an abstraction of the group of network elements that need to be configured. |
| **outputfile**  string / required | This specifies the file path where the output of each command execution is saved. Each command that is specified in the merged template file and each response from the device are saved here. Usually the location is the results folder, but you can choose another location based on your write permission. |
| **password**  string / required | Configures the password used to authenticate the connection to the remote device. The value of the password parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |
| **username**  string / required | Configures the username used to authenticate the connection to the remote device. The value of the username parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |

## [Notes](cnos_reload_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage Lenovo Network devices see <https://www.ansible.com/ansible-lenovo>.

## [Examples](cnos_reload_module.md#id4)

```yaml+jinja
Tasks : The following are examples of using the module cnos_reload. These are
 written in the main.yml file of the tasks directory.
---
- name: Test Reload
  community.network.cnos_reload:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_reload_{{ inventory_hostname }}_output.txt"
```

## [Return Values](cnos_reload_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success or failure message  **Returned:** always  **Sample:** `"Device is Reloading. Please wait..."` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)

---
collection: ansible
version: "6"
title: "community.network.cnos_vlag module – Manage VLAG resources and attributes on devices running Lenovo CNOS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/cnos_vlag_module.html
fetched_at: 2026-07-27T17:18:19+00:00
---
# community.network.cnos_vlag module – Manage VLAG resources and attributes on devices running Lenovo CNOS

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
> To use it in a playbook, specify: `community.network.cnos_vlag`.

- [Synopsis](cnos_vlag_module.md#synopsis)
- [Parameters](cnos_vlag_module.md#parameters)
- [Notes](cnos_vlag_module.md#notes)
- [Examples](cnos_vlag_module.md#examples)
- [Return Values](cnos_vlag_module.md#return-values)

## [Synopsis](cnos_vlag_module.md#id1)

- This module allows you to work with virtual Link Aggregation Groups (vLAG) related configurations. The operators used are overloaded to ensure control over switch vLAG configurations. Apart from the regular device connection related attributes, there are four vLAG arguments which are overloaded variables that will perform further configurations. They are vlagArg1, vlagArg2, vlagArg3, and vlagArg4. For more details on how to use these arguments, see [Overloaded Variables]. This module uses SSH to manage network device configuration. The results of the operation will be placed in a directory named ‘results’ that must be created by the user in their local directory to where the playbook is run.

## [Parameters](cnos_vlag_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **deviceType**  string / required | This specifies the type of device where the method is executed. The choices NE1072T,NE1032,NE1032T,NE10032,NE2572 are added since Ansible 2.4. The choice NE0152T is added since 2.8  Choices:   - `"g8272_cnos"` - `"g8296_cnos"` - `"g8332_cnos"` - `"NE0152T"` - `"NE1072T"` - `"NE1032"` - `"NE1032T"` - `"NE10032"` - `"NE2572"` |
| **enablePassword**  string | Configures the password used to enter Global Configuration command mode on the switch. If the switch does not request this password, the parameter is ignored.While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |
| **host**  string / required | This is the variable used to search the hosts file at /etc/ansible/hosts and identify the IP address of the device on which the template is going to be applied. Usually the Ansible keyword {{ inventory_hostname }} is specified in the playbook as an abstraction of the group of network elements that need to be configured. |
| **outputfile**  string / required | This specifies the file path where the output of each command execution is saved. Each command that is specified in the merged template file and each response from the device are saved here. Usually the location is the results folder, but you can choose another location based on your write permission. |
| **password**  string / required | Configures the password used to authenticate the connection to the remote device. The value of the password parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |
| **username**  string / required | Configures the username used to authenticate the connection to the remote device. The value of the username parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |
| **vlagArg1**  string / required | This is an overloaded vlag first argument. Usage of this argument can be found is the User Guide referenced above.  Choices:   - `"enable"` - `"auto-recovery"` - `"config-consistency"` - `"isl"` - `"mac-address-table"` - `"peer-gateway"` - `"priority"` - `"startup-delay"` - `"tier-id"` - `"vrrp"` - `"instance"` - `"hlthchk"` |
| **vlagArg2**  string | This is an overloaded vlag second argument. Usage of this argument can be found is the User Guide referenced above.  Choices:   - `"Interval in seconds"` - `"disable or strict"` - `"Port Aggregation Number"` - `"VLAG priority"` - `"Delay time in seconds"` - `"VLAG tier-id value"` - `"VLAG instance number"` - `"keepalive-attempts"` - `"keepalive-interval"` - `"retry-interval"` - `"peer-ip"` |
| **vlagArg3**  string | This is an overloaded vlag third argument. Usage of this argument can be found is the User Guide referenced above.  Choices:   - `"enable or port-aggregation"` - `"Number of keepalive attempts"` - `"Interval in seconds"` - `"Interval in seconds"` - `"VLAG health check peer IP4 address"` |
| **vlagArg4**  string | This is an overloaded vlag fourth argument. Usage of this argument can be found is the User Guide referenced above.  Choices:   - `"Port Aggregation Number"` - `"default or management"` |

## [Notes](cnos_vlag_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage Lenovo Network devices see <https://www.ansible.com/ansible-lenovo>.

## [Examples](cnos_vlag_module.md#id4)

```yaml+jinja
Tasks : The following are examples of using the module cnos_vlag. These are
        written in the main.yml file of the tasks directory.
---
- name: Test Vlag  - enable
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "enable"

- name: Test Vlag - autorecovery
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "auto-recovery"
      vlagArg2: 266

- name: Test Vlag - config-consistency
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "config-consistency"
      vlagArg2: "strict"

- name: Test Vlag - isl
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "isl"
      vlagArg2: 23

- name: Test Vlag  - mac-address-table
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "mac-address-table"

- name: Test Vlag - peer-gateway
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "peer-gateway"

- name: Test Vlag - priority
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "priority"
      vlagArg2: 1313

- name: Test Vlag - startup-delay
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "startup-delay"
      vlagArg2: 323

- name: Test Vlag  - tier-id
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "tier-id"
      vlagArg2: 313

- name: Test Vlag - vrrp
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "vrrp"

- name: Test Vlag - instance
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "instance"
      vlagArg2: 33
      vlagArg3: 333

- name: Test Vlag - instance2
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "instance"
      vlagArg2: "33"

- name: Test Vlag  - keepalive-attempts
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "hlthchk"
      vlagArg2: "keepalive-attempts"
      vlagArg3: 13

- name: Test Vlag - keepalive-interval
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "hlthchk"
      vlagArg2: "keepalive-interval"
      vlagArg3: 131

- name: Test Vlag - retry-interval
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "hlthchk"
      vlagArg2: "retry-interval"
      vlagArg3: 133

- name: Test Vlag - peer ip
  community.network.cnos_vlag:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "hlthchk"
      vlagArg2: "peer-ip"
      vlagArg3: "1.2.3.4"
```

## [Return Values](cnos_vlag_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success or failure message  Returned: always  Sample: `"vLAG configurations accomplished"` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)

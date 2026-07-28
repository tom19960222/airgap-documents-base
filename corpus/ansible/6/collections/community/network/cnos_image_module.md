---
collection: ansible
version: "6"
title: "community.network.cnos_image module – Perform firmware upgrade/download from a remote server on devices running Lenovo CNOS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/cnos_image_module.html
fetched_at: 2026-07-27T17:18:09+00:00
---
# community.network.cnos_image module – Perform firmware upgrade/download from a remote server on devices running Lenovo CNOS

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
> To use it in a playbook, specify: `community.network.cnos_image`.

- [Synopsis](cnos_image_module.md#synopsis)
- [Parameters](cnos_image_module.md#parameters)
- [Notes](cnos_image_module.md#notes)
- [Examples](cnos_image_module.md#examples)
- [Return Values](cnos_image_module.md#return-values)

## [Synopsis](cnos_image_module.md#id1)

- This module allows you to work with switch firmware images. It provides a way to download a firmware image to a network device from a remote server using FTP, SFTP, TFTP, or SCP. The first step is to create a directory from where the remote server can be reached. The next step is to provide the full file path of the image’s location. Authentication details required by the remote server must be provided as well. By default, this method makes the newly downloaded firmware image the active image, which will be used by the switch during the next restart. This module uses SSH to manage network device configuration. The results of the operation will be placed in a directory named ‘results’ that must be created by the user in their local directory to where the playbook is run.

## [Parameters](cnos_image_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **deviceType**  string / required | This specifies the type of device where the method is executed. The choices NE1072T,NE1032,NE1032T,NE10032,NE2572 are added since Ansible 2.4. The choice NE0152T is added since 2.8  Choices:   - `"g8272_cnos"` - `"g8296_cnos"` - `"g8332_cnos"` - `"NE0152T"` - `"NE1072T"` - `"NE1032"` - `"NE1032T"` - `"NE10032"` - `"NE2572"` |
| **enablePassword**  string | Configures the password used to enter Global Configuration command mode on the switch. If the switch does not request this password, the parameter is ignored.While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |
| **host**  string / required | This is the variable used to search the hosts file at /etc/ansible/hosts and identify the IP address of the device on which the template is going to be applied. Usually the Ansible keyword {{ inventory_hostname }} is specified in the playbook as an abstraction of the group of network elements that need to be configured. |
| **imgpath**  string / required | This specifies the full file path of the image located on the remote server. In case the relative path is used as the variable value, the root folder for the user of the server needs to be specified. |
| **imgtype**  string / required | This specifies the firmware image type to be downloaded  Choices:   - `"all"` - `"boot"` - `"os"` - `"onie"` |
| **outputfile**  string / required | This specifies the file path where the output of each command execution is saved. Each command that is specified in the merged template file and each response from the device are saved here. Usually the location is the results folder, but you can choose another location based on your write permission. |
| **password**  string / required | Configures the password used to authenticate the connection to the remote device. The value of the password parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |
| **protocol**  string / required | This refers to the protocol used by the network device to interact with the remote server from where to download the firmware image. The choices are FTP, SFTP, TFTP, or SCP. Any other protocols will result in error. If this parameter is not specified there is no default value to be used.  Choices:   - `"SFTP"` - `"SCP"` - `"FTP"` - `"TFTP"` |
| **serverip**  string / required | This specifies the IP Address of the remote server from where the software image will be downloaded. |
| **serverpassword**  string | Specify the password for the server relating to the protocol used |
| **serverusername**  string / required | Specify the username for the server relating to the protocol used |
| **username**  string / required | Configures the username used to authenticate the connection to the remote device. The value of the username parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used. |

## [Notes](cnos_image_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage Lenovo Network devices see <https://www.ansible.com/ansible-lenovo>.

## [Examples](cnos_image_module.md#id4)

```yaml+jinja
Tasks : The following are examples of using the module cnos_image. These are
  written in the main.yml file of the tasks directory.
---
- name: Test Image transfer
  community.network.cnos_image:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_image_{{ inventory_hostname }}_output.txt"
      protocol: "sftp"
      serverip: "10.241.106.118"
      imgpath: "/root/cnos_images/G8272-10.1.0.112.img"
      imgtype: "os"
      serverusername: "root"
      serverpassword: "root123"

- name: Test Image tftp
  community.network.cnos_image:
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/test_image_{{ inventory_hostname }}_output.txt"
      protocol: "tftp"
      serverip: "10.241.106.118"
      imgpath: "/anil/G8272-10.2.0.34.img"
      imgtype: "os"
      serverusername: "root"
      serverpassword: "root123"
```

## [Return Values](cnos_image_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success or failure message  Returned: always  Sample: `"Image file transferred to device"` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)

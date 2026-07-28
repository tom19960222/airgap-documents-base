---
collection: ansible
version: "8"
title: "community.vmware.vmware_vm_shell module – Run commands in a VMware guest operating system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_vm_shell_module.html
fetched_at: 2026-07-28T02:01:20+00:00
---
# community.vmware.vmware_vm_shell module – Run commands in a VMware guest operating system

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_vm_shell`.

- [Synopsis](vmware_vm_shell_module.md#synopsis)
- [Parameters](vmware_vm_shell_module.md#parameters)
- [Notes](vmware_vm_shell_module.md#notes)
- [Examples](vmware_vm_shell_module.md#examples)
- [Return Values](vmware_vm_shell_module.md#return-values)

## [Synopsis](vmware_vm_shell_module.md#id1)

- Module allows user to run common system administration commands in the guest operating system.

## [Parameters](vmware_vm_shell_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | The cluster hosting the virtual machine.  If set, it will help to speed up virtual machine search. |
| **datacenter**  string | The datacenter hosting the virtual machine.  If set, it will help to speed up virtual machine search. |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest or create the new guest.  The folder should include the datacenter. ESX’s datacenter is ha-datacenter.  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **timeout**  integer | Timeout in seconds.  If set to positive integers, then `wait_for_process` will honor this parameter and will exit after this timeout.  **Default:** `3600` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **vm_id**  string / required | Name of the virtual machine to work with. |
| **vm_id_type**  string | The VMware identification method by which the virtual machine will be identified.  **Choices:**   - `"uuid"` - `"instance_uuid"` - `"dns_name"` - `"inventory_path"` - `"vm_name"` ← (default) |
| **vm_password**  string / required | The password used to login-in to the virtual machine. |
| **vm_shell**  string / required | The absolute path to the program to start.  On Linux, shell is executed via bash. |
| **vm_shell_args**  string | The argument to the program.  The characters which must be escaped to the shell also be escaped on the command line provided.  **Default:** `" "` |
| **vm_shell_cwd**  string | The current working directory of the application from which it will be run. |
| **vm_shell_env**  list / elements=string | Comma separated list of environment variable, specified in the guest OS notation. |
| **vm_username**  string / required | The user to login-in to the virtual machine. |
| **wait_for_process**  boolean | If set to `true`, module will wait for process to complete in the given virtual machine.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](vmware_vm_shell_module.md#id3)

> **Note:**
>
> - Only the first match against vm_id is used, even if there are multiple matches.
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vm_shell_module.md#id4)

```yaml+jinja
- name: Run command inside a virtual machine
  community.vmware.vmware_vm_shell:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: "/{{datacenter}}/vm"
    vm_id: "{{ vm_name }}"
    vm_username: root
    vm_password: superSecret
    vm_shell: /bin/echo
    vm_shell_args: " $var >> myFile "
    vm_shell_env:
      - "PATH=/bin"
      - "VAR=test"
    vm_shell_cwd: "/tmp"
  delegate_to: localhost
  register: shell_command_output

- name: Run command inside a virtual machine with wait and timeout
  community.vmware.vmware_vm_shell:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: "/{{datacenter}}/vm"
    vm_id: NameOfVM
    vm_username: root
    vm_password: superSecret
    vm_shell: /bin/sleep
    vm_shell_args: 100
    wait_for_process: true
    timeout: 2000
  delegate_to: localhost
  register: shell_command_with_wait_timeout

- name: Change user password in the guest machine
  community.vmware.vmware_vm_shell:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: "/{{datacenter}}/vm"
    vm_id: "{{ vm_name }}"
    vm_username: sample
    vm_password: old_password
    vm_shell: "/bin/echo"
    vm_shell_args: "-e 'old_password\nnew_password\nnew_password' | passwd sample > /tmp/$$.txt 2>&1"
  delegate_to: localhost

- name: Change hostname of guest machine
  community.vmware.vmware_vm_shell:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: "/{{datacenter}}/vm"
    vm_id: "{{ vm_name }}"
    vm_username: testUser
    vm_password: SuperSecretPassword
    vm_shell: "/usr/bin/hostnamectl"
    vm_shell_args: "set-hostname new_hostname > /tmp/$$.txt 2>&1"
  delegate_to: localhost
```

## [Return Values](vmware_vm_shell_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **results**  dictionary | metadata about the new process after completion with wait_for_process  **Returned:** on success  **Sample:** `{"cmd_line": "\"/bin/sleep\" 1", "end_time": "2018-04-26T05:03:21+00:00", "exit_code": 0, "name": "sleep", "owner": "dev1", "start_time": "2018-04-26T05:03:19+00:00", "uuid": "564db1e2-a3ff-3b0e-8b77-49c25570bb66"}` |

### Authors

- Ritesh Khadgaray (@ritzk)
- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)

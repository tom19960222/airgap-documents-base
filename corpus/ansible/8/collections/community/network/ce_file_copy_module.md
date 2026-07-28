---
collection: ansible
version: "8"
title: "community.network.ce_file_copy module – Copy a file to a remote cloudengine device over SCP on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_file_copy_module.html
fetched_at: 2026-07-28T01:55:26+00:00
---
# community.network.ce_file_copy module – Copy a file to a remote cloudengine device over SCP on HUAWEI CloudEngine switches.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](ce_file_copy_module.md#ansible-collections-community-network-ce-file-copy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.ce_file_copy`.

- [Synopsis](ce_file_copy_module.md#synopsis)
- [Requirements](ce_file_copy_module.md#requirements)
- [Parameters](ce_file_copy_module.md#parameters)
- [Notes](ce_file_copy_module.md#notes)
- [Examples](ce_file_copy_module.md#examples)
- [Return Values](ce_file_copy_module.md#return-values)

## [Synopsis](ce_file_copy_module.md#id1)

- Copy a file to a remote cloudengine device over SCP on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_file_copy

## [Requirements](ce_file_copy_module.md#id2)

The below requirements are needed on the host that executes this module.

- paramiko

## [Parameters](ce_file_copy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **file_system**  string | The remote file system of the device. If omitted, devices that support a *file_system* parameter will use their default values. File system indicates the storage medium and can be set to as follows, 1) `flash` is root directory of the flash memory on the master MPU. 2) `slave#flash` is root directory of the flash memory on the slave MPU. If no slave MPU exists, this drive is unavailable. 3) `chassis ID/slot number#flash` is root directory of the flash memory on a device in a stack. For example, `1/5#flash` indicates the flash memory whose chassis ID is 1 and slot number is 5.  **Default:** `"flash:"` |
| **local_file**  string / required | Path to local file. Local directory must exist. The maximum length of *local_file* is `4096`. |
| **remote_file**  string | Remote file path of the copy. Remote directories must exist. If omitted, the name of the local file will be used. The maximum length of *remote_file* is `4096`. |

## [Notes](ce_file_copy_module.md#id4)

> **Note:**
>
> - The feature must be enabled with feature scp-server.
> - If the file is already present, no transfer will take place.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_file_copy_module.md#id5)

```yaml+jinja
- name: File copy test
  hosts: cloudengine
  connection: local
  gather_facts: false
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: "Copy a local file to remote device"
    community.network.ce_file_copy:
      local_file: /usr/vrpcfg.cfg
      remote_file: /vrpcfg.cfg
      file_system: 'flash:'
      provider: "{{ cli }}"
```

## [Return Values](ce_file_copy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **local_file**  string | The path of the local file.  **Returned:** always  **Sample:** `"/usr/work/vrpcfg.zip"` |
| **remote_file**  string | The path of the remote file.  **Returned:** always  **Sample:** `"/vrpcfg.zip"` |
| **transfer_result**  string | information about transfer result.  **Returned:** always  **Sample:** `"The local file has been successfully transferred to the device."` |

### Authors

- Zhou Zhijin (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)

---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svcinfo_command module – This module implements SSH Client which helps to run svcinfo CLI command on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svcinfo_command_module.html
fetched_at: 2026-07-28T02:35:45+00:00
---
# ibm.storage_virtualize.ibm_svcinfo_command module – This module implements SSH Client which helps to run svcinfo CLI command on IBM Storage Virtualize family systems

> **Note:**
>
> This module is part of the [ibm.storage_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/storage_virtualize/) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.storage_virtualize`.
>
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svcinfo_command`.

New in ibm.storage_virtualize 1.2.0

- [Synopsis](ibm_svcinfo_command_module.md#synopsis)
- [Parameters](ibm_svcinfo_command_module.md#parameters)
- [Examples](ibm_svcinfo_command_module.md#examples)

## [Synopsis](ibm_svcinfo_command_module.md#id1)

- Runs single svcinfo CLI command on IBM Storage Virtualize family systems. Filter options like filtervalue or pipe ‘|’ with grep, awk, and others are not supported in the command in this module. Paramiko must be installed to use this module.

## [Parameters](ibm_svcinfo_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **command**  string | Single svcinfo CLI command to be executed on Storage Virtualize system. Each command must start with svcinfo keyword. |
| **key_filename**  string | SSH client private key filename. By default, `~/.ssh/id_rsa` is used. |
| **log_path**  string | Path of debug log file. |
| **password**  string / required | Password for the Storage Virtualize system. |
| **username**  string / required | Username for the Storage Virtualize system. |
| **usesshkey**  string | For key-pair based SSH connection, set this field as `'yes'`. Provide full path of keyfile in key_filename field. If not provided, default path of SSH key is used.  **Choices:**   - `"yes"` - `"no"` ← (default) |

## [Examples](ibm_svcinfo_command_module.md#id3)

```yaml+jinja
- name: Run svcinfo CLI command using SSH client with password
  ibm.storage_virtualize.ibm_svcinfo_command:
    command: "svcinfo lsuser {{user}}"
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/ansible.log
- name: Run svcinfo CLI command using passwordless SSH Client
  ibm.storage_virtualize.ibm_svcinfo_command:
    command: "svcinfo lsuser"
    usesshkey: "yes"
    clustername: "{{clustername}}"
    username: "{{username}}"
    password:
    log_path: /tmp/ansible.log
```

### Authors

- Shilpi Jain (@Shilpi-Jain1)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)

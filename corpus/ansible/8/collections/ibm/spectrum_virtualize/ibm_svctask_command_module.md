---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_svctask_command module – This module implements SSH Client which helps to run svctask CLI command(s) on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_svctask_command_module.html
fetched_at: 2026-07-28T02:35:12+00:00
---
# ibm.spectrum_virtualize.ibm_svctask_command module – This module implements SSH Client which helps to run svctask CLI command(s) on IBM Spectrum Virtualize family storage systems

> **Note:**
>
> This module is part of the [ibm.spectrum_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/spectrum_virtualize/) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.spectrum_virtualize`.
>
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svctask_command`.

New in ibm.spectrum_virtualize 1.2.0

- [Synopsis](ibm_svctask_command_module.md#synopsis)
- [Parameters](ibm_svctask_command_module.md#parameters)
- [Examples](ibm_svctask_command_module.md#examples)

## [Synopsis](ibm_svctask_command_module.md#id1)

- Runs svctask CLI command(s) on IBM Spectrum Virtualize Family storage systems. In case any svctask command fails while running this module, then the module stops processing further commands in the list. Paramiko must be installed to use this module.

## [Parameters](ibm_svctask_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **command**  list / elements=string | A list containing svctask CLI commands to be executed on storage.  Each command must start with ‘svctask’ keyword. |
| **key_filename**  string | SSH client private key filename. By default, ~/.ssh/id_rsa is used. |
| **log_path**  string | Path of debug log file. |
| **password**  string / required | Password for the Spectrum Virtualize storage system. |
| **username**  string / required | Username for the Spectrum Virtualize storage system. |
| **usesshkey**  string | For key-pair based SSH connection, set this field as “yes”. Provide full path of key in key_filename field. If not provided, default path of SSH key is used.  **Choices:**   - `"yes"` - `"no"` ← (default) |

## [Examples](ibm_svctask_command_module.md#id3)

```yaml+jinja
- name: Run svctask CLI commands using SSH client with password
  ibm.spectrum_virtualize.ibm_svctask_command:
    command: [
        "svctask mkvdisk -name {{ volname }} -mdiskgrp '{{ pool }}' -easytier '{{ easy_tier }}' -size {{ size }} -unit {{ unit }}",
        "svctask rmvdisk {{ volname }}"
    ]
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/ansible.log
- name: Run svctask CLI command using passwordless SSH Client
  ibm.spectrum_virtualize.ibm_svctask_command:
    command: [
        "svctask mkvdisk -name vol0 -mdiskgrp pool0 -easytier off -size 1 -unit gb",
        "svctask rmvdisk vol0"
    ]
    clustername: "{{clustername}}"
    username: "{{username}}"
    password:
    usesshkey: yes
    log_path: /tmp/ansible.log
```

### Authors

- Shilpi Jain (@Shilpi-Jain1)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)

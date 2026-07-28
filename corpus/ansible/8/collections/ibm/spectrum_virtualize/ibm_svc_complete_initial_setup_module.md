---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_svc_complete_initial_setup module – This module completes the initial setup configuration for LMC systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_svc_complete_initial_setup_module.html
fetched_at: 2026-07-28T02:34:48+00:00
---
# ibm.spectrum_virtualize.ibm_svc_complete_initial_setup module – This module completes the initial setup configuration for LMC systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_complete_initial_setup`.

New in ibm.spectrum_virtualize 1.8.0

- [Synopsis](ibm_svc_complete_initial_setup_module.md#synopsis)
- [Parameters](ibm_svc_complete_initial_setup_module.md#parameters)
- [Notes](ibm_svc_complete_initial_setup_module.md#notes)
- [Examples](ibm_svc_complete_initial_setup_module.md#examples)

## [Synopsis](ibm_svc_complete_initial_setup_module.md#id1)

- It disables the GUI setup wizard for LMC systems.
- It is recommended to run this module after using ibm_svc_initial_setup module for intial setup configuration.
- This module works on SSH. Paramiko must be installed to use this module.

## [Parameters](ibm_svc_complete_initial_setup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **log_path**  string | Path of debug log file. |
| **password**  string / required | Password for the Spectrum Virtualize storage system. |
| **username**  string / required | Username for the Spectrum Virtualize storage system. |

## [Notes](ibm_svc_complete_initial_setup_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_complete_initial_setup_module.md#id4)

```yaml+jinja
- name: complete intial setup
  ibm.spectrum_virtualize.ibm_svc_complete_initial_setup:
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
```

### Authors

- Shilpi Jain(@Shilpi-J)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)

---
collection: ansible
version: "8"
title: "ibm.qradar.deploy module – Trigger a qradar configuration deployment"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/qradar/deploy_module.html
fetched_at: 2026-07-28T02:34:31+00:00
---
# ibm.qradar.deploy module – Trigger a qradar configuration deployment

> **Note:**
>
> This module is part of the [ibm.qradar collection](https://galaxy.ansible.com/ui/repo/published/ibm/qradar/) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.qradar`.
>
> To use it in a playbook, specify: `ibm.qradar.deploy`.

New in ibm.qradar 1.0.0

- [Synopsis](deploy_module.md#synopsis)
- [Parameters](deploy_module.md#parameters)
- [Notes](deploy_module.md#notes)
- [Examples](deploy_module.md#examples)

## [Synopsis](deploy_module.md#id1)

- This module allows for INCREMENTAL or FULL deployments

Aliases: qradar_deploy

## [Parameters](deploy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **type**  string | Type of deployment  **Choices:**   - `"INCREMENTAL"` ← (default) - `"FULL"` |

## [Notes](deploy_module.md#id3)

> **Note:**
>
> - This module does not support check mode because the QRadar REST API does not offer stateful inspection of configuration deployments

## [Examples](deploy_module.md#id4)

```yaml+jinja
- name: run an incremental deploy
  ibm.qradar.deploy:
    type: INCREMENTAL
```

### Authors

- Ansible Security Automation Team (@maxamillion) <<https://github.com/ansible-security>>

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.qradar/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.qradar)

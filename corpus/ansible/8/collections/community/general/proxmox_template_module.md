---
collection: ansible
version: "8"
title: "community.general.proxmox_template module – Management of OS templates in Proxmox VE cluster"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/proxmox_template_module.html
fetched_at: 2026-07-28T01:49:24+00:00
---
# community.general.proxmox_template module – Management of OS templates in Proxmox VE cluster

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](proxmox_template_module.md#ansible-collections-community-general-proxmox-template-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox_template`.

- [Synopsis](proxmox_template_module.md#synopsis)
- [Requirements](proxmox_template_module.md#requirements)
- [Parameters](proxmox_template_module.md#parameters)
- [Attributes](proxmox_template_module.md#attributes)
- [Notes](proxmox_template_module.md#notes)
- [Examples](proxmox_template_module.md#examples)

## [Synopsis](proxmox_template_module.md#id1)

- allows you to upload/delete templates in Proxmox VE cluster

Aliases: cloud.misc.proxmox_template

## [Requirements](proxmox_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- requests

## [Parameters](proxmox_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use [`PROXMOX_PASSWORD`](../../environment_variables.md#envvar-PROXMOX_PASSWORD) environment variable. |
| **api_token_id**  string  *added in community.general 1.3.0* | Specify the token ID.  Requires `proxmoxer>=1.1.0` to work. |
| **api_token_secret**  string  *added in community.general 1.3.0* | Specify the token secret.  Requires `proxmoxer>=1.1.0` to work. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **content_type**  string | Content type.  Required only for `state=present`.  **Choices:**   - `"vztmpl"` ← (default) - `"iso"` |
| **force**  boolean | It can only be used with `state=present`, existing template will be overwritten.  **Choices:**   - `false` ← (default) - `true` |
| **node**  string | Proxmox VE node on which to operate. |
| **src**  path | Path to uploaded file.  Required only for `state=present`. |
| **state**  string | Indicate desired state of the template.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **storage**  string | Target storage.  **Default:** `"local"` |
| **template**  string | The template name.  Required for `state=absent` to delete a template.  Required for `state=present` to download an appliance container template (pveam). |
| **timeout**  integer | Timeout for operations.  **Default:** `30` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](proxmox_template_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](proxmox_template_module.md#id5)

> **Note:**
>
> - Requires `proxmoxer` and `requests` modules on host. Those modules can be installed with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - `proxmoxer` >= 1.2.0 requires `requests_toolbelt` to upload files larger than 256 MB.

## [Examples](proxmox_template_module.md#id6)

```yaml+jinja
- name: Upload new openvz template with minimal options
  community.general.proxmox_template:
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    src: ~/ubuntu-14.04-x86_64.tar.gz

- name: >
    Upload new openvz template with minimal options use environment
    PROXMOX_PASSWORD variable(you should export it before)
  community.general.proxmox_template:
    node: uk-mc02
    api_user: root@pam
    api_host: node1
    src: ~/ubuntu-14.04-x86_64.tar.gz

- name: Upload new openvz template with all options and force overwrite
  community.general.proxmox_template:
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    storage: local
    content_type: vztmpl
    src: ~/ubuntu-14.04-x86_64.tar.gz
    force: true

- name: Delete template with minimal options
  community.general.proxmox_template:
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    template: ubuntu-14.04-x86_64.tar.gz
    state: absent

- name: Download proxmox appliance container template
  community.general.proxmox_template:
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    storage: local
    content_type: vztmpl
    template: ubuntu-20.04-standard_20.04-1_amd64.tar.gz
```

### Authors

- Sergei Antipov (@UnderGreen)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

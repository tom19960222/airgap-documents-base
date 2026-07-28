---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_ssh_key_info module – Gather infos about your Hetzner Cloud ssh_keys."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_ssh_key_info_module.html
fetched_at: 2026-07-28T02:34:13+00:00
---
# hetzner.hcloud.hcloud_ssh_key_info module – Gather infos about your Hetzner Cloud ssh_keys.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/ui/repo/published/hetzner/hcloud/) (version 1.16.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_ssh_key_info_module.md#ansible-collections-hetzner-hcloud-hcloud-ssh-key-info-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_ssh_key_info`.

- [Synopsis](hcloud_ssh_key_info_module.md#synopsis)
- [Requirements](hcloud_ssh_key_info_module.md#requirements)
- [Parameters](hcloud_ssh_key_info_module.md#parameters)
- [See Also](hcloud_ssh_key_info_module.md#see-also)
- [Examples](hcloud_ssh_key_info_module.md#examples)
- [Return Values](hcloud_ssh_key_info_module.md#return-values)

## [Synopsis](hcloud_ssh_key_info_module.md#id1)

- Gather facts about your Hetzner Cloud ssh_keys.
- This module was called `hcloud_ssh_key_facts` before Ansible 2.9, returning `ansible_facts` and `hcloud_ssh_key_facts`. Note that the [hetzner.hcloud.hcloud_ssh_key_info](hcloud_ssh_key_info_module.md#ansible-collections-hetzner-hcloud-hcloud-ssh-key-info-module) module no longer returns `ansible_facts` and the value was renamed to `hcloud_ssh_key_info`!

Aliases: hcloud_ssh_key_facts

## [Requirements](hcloud_ssh_key_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_ssh_key_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **fingerprint**  string | The fingerprint of the ssh key you want to get. |
| **id**  integer | The ID of the ssh key you want to get. |
| **label_selector**  string | The label selector for the ssh key you want to get. |
| **name**  string | The name of the ssh key you want to get. |

## [See Also](hcloud_ssh_key_info_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_ssh_key_info_module.md#id5)

```yaml+jinja
- name: Gather hcloud sshkey infos
  hcloud_ssh_key_info:
  register: output
- name: Print the gathered infos
  debug:
    var: output.hcloud_ssh_key_info
```

## [Return Values](hcloud_ssh_key_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_ssh_key_info**  complex | The ssh key instances  **Returned:** Always |
| **fingerprint**  string | Fingerprint of the ssh key  **Returned:** always  **Sample:** `"0e:e0:bd:c7:2d:1f:69:49:94:44:91:f1:19:fd:35:f3"` |
| **id**  integer | Numeric identifier of the ssh_key  **Returned:** always  **Sample:** `1937415` |
| **labels**  dictionary | User-defined labels (key-value pairs)  **Returned:** always |
| **name**  string | Name of the ssh_key  **Returned:** always  **Sample:** `"my-ssh-key"` |
| **public_key**  string | The actual public key  **Returned:** always  **Sample:** `"ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGpl/tnk74nnQJxxLAtutUApUZMRJxryKh7VXkNbd4g9 john@example.com"` |

### Authors

- Christopher Schmitt (@cschmitt-hcloud)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)

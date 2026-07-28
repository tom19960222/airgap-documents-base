---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_ssh_key module – Create and manage ssh keys on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_ssh_key_module.html
fetched_at: 2026-07-27T17:49:53+00:00
---
# hetzner.hcloud.hcloud_ssh_key module – Create and manage ssh keys on the Hetzner Cloud.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/hetzner/hcloud) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_ssh_key_module.md#ansible-collections-hetzner-hcloud-hcloud-ssh-key-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_ssh_key`.

- [Synopsis](hcloud_ssh_key_module.md#synopsis)
- [Requirements](hcloud_ssh_key_module.md#requirements)
- [Parameters](hcloud_ssh_key_module.md#parameters)
- [See Also](hcloud_ssh_key_module.md#see-also)
- [Examples](hcloud_ssh_key_module.md#examples)
- [Return Values](hcloud_ssh_key_module.md#return-values)

## [Synopsis](hcloud_ssh_key_module.md#id1)

- Create, update and manage ssh keys on the Hetzner Cloud.

## [Requirements](hcloud_ssh_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0

## [Parameters](hcloud_ssh_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **fingerprint**  string | The Fingerprint of the Hetzner Cloud ssh_key to manage.  Only required if no ssh_key *id* or *name* is given. |
| **id**  integer | The ID of the Hetzner Cloud ssh_key to manage.  Only required if no ssh_key *name* is given |
| **labels**  dictionary | User-defined labels (key-value pairs) |
| **name**  string | The Name of the Hetzner Cloud ssh_key to manage.  Only required if no ssh_key *id* is given or a ssh_key does not exist. |
| **public_key**  string | The Public Key to add.  Required if ssh_key does not exist. |
| **state**  string | State of the ssh_key.  Choices:   - `"absent"` - `"present"` ← (default) |

## [See Also](hcloud_ssh_key_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_ssh_key_module.md#id5)

```yaml+jinja
- name: Create a basic ssh_key
  hcloud_ssh_key:
    name: my-ssh_key
    public_key: "ssh-rsa AAAjjk76kgf...Xt"
    state: present

- name: Create a ssh_key with labels
  hcloud_ssh_key:
    name: my-ssh_key
    public_key: "ssh-rsa AAAjjk76kgf...Xt"
    labels:
        key: value
        mylabel: 123
    state: present

- name: Ensure the ssh_key is absent (remove if needed)
  hcloud_ssh_key:
    name: my-ssh_key
    state: absent
```

## [Return Values](hcloud_ssh_key_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_ssh_key**  complex | The ssh_key instance  Returned: Always |
| **fingerprint**  string | Fingerprint of the ssh_key  Returned: Always  Sample: `"b7:2f:30:a0:2f:6c:58:6c:21:04:58:61:ba:06:3b:2f"` |
| **id**  integer | ID of the ssh_key  Returned: Always  Sample: `12345` |
| **labels**  dictionary | User-defined labels (key-value pairs)  Returned: Always  Sample: `{"key": "value", "mylabel": 123}` |
| **name**  string | Name of the ssh_key  Returned: Always  Sample: `"my-ssh-key"` |
| **public_key**  string | Public key of the ssh_key  Returned: Always  Sample: `"ssh-rsa AAAjjk76kgf...Xt"` |

### Authors

- Lukas Kaemmerling (@LKaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)

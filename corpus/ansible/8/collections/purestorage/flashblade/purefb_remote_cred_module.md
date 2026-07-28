---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_remote_cred module – Create, modify and delete FlashBlade object store remote credentials"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_remote_cred_module.html
fetched_at: 2026-07-28T02:52:15+00:00
---
# purestorage.flashblade.purefb_remote_cred module – Create, modify and delete FlashBlade object store remote credentials

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flashblade/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_remote_cred_module.md#ansible-collections-purestorage-flashblade-purefb-remote-cred-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_remote_cred`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_remote_cred_module.md#synopsis)
- [Requirements](purefb_remote_cred_module.md#requirements)
- [Parameters](purefb_remote_cred_module.md#parameters)
- [Notes](purefb_remote_cred_module.md#notes)
- [Examples](purefb_remote_cred_module.md#examples)

## [Synopsis](purefb_remote_cred_module.md#id1)

- Create, modify and delete object store remote credentials
- You must have a correctly configured remote array or target
- This module is **not** idempotent when updating existing remote credentials

## [Requirements](purefb_remote_cred_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_remote_cred_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  string | Access Key ID of the S3 target |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **name**  string / required | The name of the credential |
| **secret**  string | Secret Access Key for the S3 or Azure target |
| **state**  string | Define state of remote credential  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **target**  string / required | Define whether to initialize the S3 bucket |

## [Notes](purefb_remote_cred_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_remote_cred_module.md#id5)

```yaml+jinja
- name: Create remote credential
  purestorage.flashblade.purefb_remote_cred:
    name: cred1
    access_key: "3794fb12c6204e19195f"
    secret: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    target: target1
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete remote credential
  purestorage.flashblade.purefb_remote_cred:
    name: cred1
    target: target1
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)

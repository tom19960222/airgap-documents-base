---
collection: ansible
version: "8"
title: "purestorage.fusion.fusion_hap module – Manage host access policies in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/fusion/fusion_hap_module.html
fetched_at: 2026-07-28T02:52:33+00:00
---
# purestorage.fusion.fusion_hap module – Manage host access policies in Pure Storage Fusion

> **Note:**
>
> This module is part of the [purestorage.fusion collection](https://galaxy.ansible.com/ui/repo/published/purestorage/fusion/) (version 1.6.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.fusion`.
> You need further requirements to be able to use this module,
> see [Requirements](fusion_hap_module.md#ansible-collections-purestorage-fusion-fusion-hap-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_hap`.

New in purestorage.fusion 1.0.0

- [Synopsis](fusion_hap_module.md#synopsis)
- [Requirements](fusion_hap_module.md#requirements)
- [Parameters](fusion_hap_module.md#parameters)
- [Notes](fusion_hap_module.md#notes)
- [Examples](fusion_hap_module.md#examples)

## [Synopsis](fusion_hap_module.md#id1)

- Create or delete host access policies in Pure Storage Fusion.

## [Requirements](fusion_hap_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8
- purefusion

## [Parameters](fusion_hap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Access token for Fusion Service  Defaults to the set environment variable under FUSION_ACCESS_TOKEN |
| **display_name**  string | The human name of the host access policy. |
| **host_password**  string | CURRENTLY NOT SUPPORTED.  Sets the host password for CHAP authentication.  Password length between 12 and 255 characters.  To clear the username/password pair use `clear` as the password. |
| **host_user**  string | CURRENTLY NOT SUPPORTED.  Sets the host user name for CHAP authentication.  Required with *host_password*.  To clear the username/password pair use `clear` as the password. |
| **iqn**  string | IQN for the host access policy. |
| **issuer_id**  aliases: app_id  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_ISSUER_ID |
| **name**  string / required | The name of the host access policy. |
| **nqn**  string | CURRENTLY NOT SUPPORTED.  NQN for the host access policy. |
| **personality**  string | Define which operating system the host is.  **Choices:**   - `"linux"` ← (default) - `"windows"` - `"hpux"` - `"vms"` - `"aix"` - `"esxi"` - `"solaris"` - `"hitachi-vsp"` - `"oracle-vm-server"` |
| **private_key_file**  aliases: key_file  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **private_key_password**  string | Password of the encrypted private key file |
| **state**  string | Define whether the host access policy should exist or not.  When removing host access policy all connected volumes must have been previously disconnected.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **target_password**  string | CURRENTLY NOT SUPPORTED.  Sets the target password for CHAP authentication.  Password length between 12 and 255 characters.  To clear the username/password pair use `clear` as the password. |
| **target_user**  string | CURRENTLY NOT SUPPORTED.  Sets the target user name for CHAP authentication.  Required with *target_password*.  To clear the username/password pair use `clear` as the password. |
| **wwns**  list / elements=string | CURRENTLY NOT SUPPORTED.  List of wwns for the host access policy. |

## [Notes](fusion_hap_module.md#id4)

> **Note:**
>
> - Supports `check mode`.
> - Setting passwords is not an idempotent action.
> - Only iSCSI transport is currently supported.
> - iSCSI CHAP is not yet supported.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_ISSUER_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *issuer_id* and *private_key_file* arguments are not passed to the module directly
> - If you want to use access token for authentication, you must use `FUSION_ACCESS_TOKEN` environment variable if *access_token* argument is not passed to the module directly

## [Examples](fusion_hap_module.md#id5)

```yaml+jinja
- name: Create new AIX host access policy
  purestorage.fusion.fusion_hap:
    name: foo
    personality: aix
    iqn: "iqn.2005-03.com.RedHat:linux-host1"
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"

- name: Delete host access policy
  purestorage.fusion.fusion_hap:
    name: foo
    state: absent
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)

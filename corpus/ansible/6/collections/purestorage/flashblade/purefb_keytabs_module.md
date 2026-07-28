---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_keytabs module – Manage FlashBlade Kerberos Keytabs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_keytabs_module.html
fetched_at: 2026-07-28T00:18:50+00:00
---
# purestorage.flashblade.purefb_keytabs module – Manage FlashBlade Kerberos Keytabs

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/purestorage/flashblade) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_keytabs_module.md#ansible-collections-purestorage-flashblade-purefb-keytabs-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_keytabs`.

New in purestorage.flashblade 1.6.0

- [Synopsis](purefb_keytabs_module.md#synopsis)
- [Requirements](purefb_keytabs_module.md#requirements)
- [Parameters](purefb_keytabs_module.md#parameters)
- [Notes](purefb_keytabs_module.md#notes)
- [Examples](purefb_keytabs_module.md#examples)
- [Return Values](purefb_keytabs_module.md#return-values)

## [Synopsis](purefb_keytabs_module.md#id1)

- Manage Kerberos Keytabs for FlashBlades

## [Requirements](purefb_keytabs_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_keytabs_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **filetype**  string | Format of the keytab file  Choices:   - `"binary"` - `"base64"` |
| **keytab_file**  string | Name of file holding Keytab |
| **name**  string | Name of the Keytab  Must include prefix and suffix |
| **prefix**  string | Only required for *import* or *rotate*  Prefix to use for naming the files slots  Specifying a file entry prefix is required because a single keytab file can contain multiple keytab entries in multiple slots.  If not provided for *import* the current AD Account name will be used. |
| **state**  string | Manage Kerberos Keytabs  Choices:   - `"absent"` - `"import"` ← (default) - `"export"` - `"rotate"` |

## [Notes](purefb_keytabs_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_keytabs_module.md#id5)

```yaml+jinja
- name: Import a binary keytab
  purestorage.flashblade.purefb_keytabs:
    state: import
    prefix: example
    keytab_file: pure_krb.keytab
    filetype: binary
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6

- name: Import a base64 keytab
  purestorage.flashblade.purefb_keytabs:
    state: import
    prefix: example
    keytab_file: pure_krb.keytab.mime
    filetype: base64
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6

- name: Export a keytab
  purestorage.flashblade.purefb_keytabs:
    state: export
    name: example.3
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
  register: download_file

- name: Delete a keytab
  purestorage.flashblade.purefb_keytabs:
    state: absent
    name: example.3
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6

- name: Rotate current AD account keytabs
  purestorage.flashblade.purefb_keytabs:
    state: rotate
    fb_url: 10.10.10.2

- name: Rotate AD account keytabs by creating new series
  purestorage.flashblade.purefb_keytabs:
    state: rotate
    name: next_prefix
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
```

## [Return Values](purefb_keytabs_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **download_file**  string | Name of file containing exported keytab  Returned: When using *export* option  Sample: `"/tmp/pure_krb8939478070214877726.keytab"` |

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)

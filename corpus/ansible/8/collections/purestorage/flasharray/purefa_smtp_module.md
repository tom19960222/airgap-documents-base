---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_smtp module – Configure FlashArray SMTP settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_smtp_module.html
fetched_at: 2026-07-28T02:51:25+00:00
---
# purestorage.flasharray.purefa_smtp module – Configure FlashArray SMTP settings

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_smtp_module.md#ansible-collections-purestorage-flasharray-purefa-smtp-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_smtp`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_smtp_module.md#synopsis)
- [Requirements](purefa_smtp_module.md#requirements)
- [Parameters](purefa_smtp_module.md#parameters)
- [Notes](purefa_smtp_module.md#notes)
- [Examples](purefa_smtp_module.md#examples)

## [Synopsis](purefa_smtp_module.md#id1)

- Set or erase configuration for the SMTP settings.
- If username/password are set this will always force a change as there is no way to see if the password is differnet from the current SMTP configuration.
- Pure Storage Ansible Team (@sdodsley) <[pure-ansible-team@purestorage.com](mailto:pure-ansible-team%40purestorage.com)>

## [Requirements](purefa_smtp_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_smtp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **password**  string | The SMTP password. |
| **relay_host**  string | IPv4 or IPv6 address or FQDN. A port number may be appended. |
| **sender_domain**  string | Domain name. |
| **state**  string | Set or delete SMTP configuration  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **user**  string | The SMTP username. |

## [Notes](purefa_smtp_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_smtp_module.md#id5)

```yaml+jinja
- name: Delete exisitng SMTP settings
  purestorage.flasharray.purefa_smtp:
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: Set SMTP settings
  purestorage.flasharray.purefa_smtp:
    sender_domain: purestorage.com
    password: account_password
    user: smtp_account
    relay_host: 10.2.56.78:2345
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)

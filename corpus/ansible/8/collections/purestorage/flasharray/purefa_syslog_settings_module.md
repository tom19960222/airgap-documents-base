---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_syslog_settings module – Manage FlashArray syslog servers settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_syslog_settings_module.html
fetched_at: 2026-07-28T02:51:30+00:00
---
# purestorage.flasharray.purefa_syslog_settings module – Manage FlashArray syslog servers settings

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
> see [Requirements](purefa_syslog_settings_module.md#ansible-collections-purestorage-flasharray-purefa-syslog-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_syslog_settings`.

New in purestorage.flasharray 1.10.0

- [Synopsis](purefa_syslog_settings_module.md#synopsis)
- [Requirements](purefa_syslog_settings_module.md#requirements)
- [Parameters](purefa_syslog_settings_module.md#parameters)
- [Notes](purefa_syslog_settings_module.md#notes)
- [Examples](purefa_syslog_settings_module.md#examples)

## [Synopsis](purefa_syslog_settings_module.md#id1)

- Manage FlashArray syslog servers settings

## [Requirements](purefa_syslog_settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_syslog_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **ca_certificate**  string | The text of the CA certificate for condifured syslog servers.  Includes the “—–BEGIN CERTIFICATE—–” and “—–END CERTIFICATE—–” lines  Does not exceed 3000 characters in length  To delete the existing CA certifcate use the special string `DELETE` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **severity**  string | Logging severity threshold for which events will be forwarded to the configured syslog servers.  **Choices:**   - `"debug"` - `"info"` ← (default) - `"notice"` |
| **tls_audit**  boolean | If messages that are necessary in order to audit TLS negotiations performed by the array are forwared to the syslog servers.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](purefa_syslog_settings_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_syslog_settings_module.md#id5)

```yaml+jinja
- name: Change syslog servers settings
  purestorage.flasharray.purefa_syslog_servers:
    tls_audit: false
    severity: debug
    ca_certificate: "{{lookup('file', 'example.crt') }}"
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete existing CA certifcate for syslog servers settings
  purestorage.flasharray.purefa_syslog_servers:
    ca_certificate: DELETE
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)

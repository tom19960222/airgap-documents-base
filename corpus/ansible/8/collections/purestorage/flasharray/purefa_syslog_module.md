---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_syslog module – Configure Pure Storage FlashArray syslog settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_syslog_module.html
fetched_at: 2026-07-28T02:51:30+00:00
---
# purestorage.flasharray.purefa_syslog module – Configure Pure Storage FlashArray syslog settings

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
> see [Requirements](purefa_syslog_module.md#ansible-collections-purestorage-flasharray-purefa-syslog-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_syslog`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_syslog_module.md#synopsis)
- [Requirements](purefa_syslog_module.md#requirements)
- [Parameters](purefa_syslog_module.md#parameters)
- [Notes](purefa_syslog_module.md#notes)
- [Examples](purefa_syslog_module.md#examples)

## [Synopsis](purefa_syslog_module.md#id1)

- Configure syslog configuration for Pure Storage FlashArrays.
- Add or delete an individual syslog server to the existing list of serves.

## [Requirements](purefa_syslog_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_syslog_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string / required | Syslog server address. This field supports IPv4, IPv6 or FQDN. An invalid IP addresses will cause the module to fail. No validation is performed for FQDNs. |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **name**  string | A user-specified name. The name must be locally unique and cannot be changed.  Only applicable with FlashArrays running Purity//FA 6.0 or higher. |
| **port**  string | Port at which the server is listening. If no port is specified the system will use 514 |
| **protocol**  string / required | Protocol which server uses  **Choices:**   - `"tcp"` - `"tls"` - `"udp"` |
| **state**  string | Create or delete syslog servers configuration  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefa_syslog_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_syslog_module.md#id5)

```yaml+jinja
- name: Delete exisitng syslog server entries
  purestorage.flasharray.purefa_syslog:
    address: syslog1.com
    protocol: tcp
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Set array syslog servers
  purestorage.flasharray.purefa_syslog:
    state: present
    address: syslog1.com
    protocol: udp
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

---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_vnc module – Enable or Disable VNC port for installed apps"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_vnc_module.html
fetched_at: 2026-07-28T00:18:35+00:00
---
# purestorage.flasharray.purefa_vnc module – Enable or Disable VNC port for installed apps

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/purestorage/flasharray) (version 1.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_vnc_module.md#ansible-collections-purestorage-flasharray-purefa-vnc-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_vnc`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_vnc_module.md#synopsis)
- [Requirements](purefa_vnc_module.md#requirements)
- [Parameters](purefa_vnc_module.md#parameters)
- [Notes](purefa_vnc_module.md#notes)
- [Examples](purefa_vnc_module.md#examples)
- [Return Values](purefa_vnc_module.md#return-values)

## [Synopsis](purefa_vnc_module.md#id1)

- Enablke or Disable VNC access for installed apps

## [Requirements](purefa_vnc_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_vnc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **name**  string / required | Name od app |
| **state**  string | Define state of VNC  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](purefa_vnc_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_vnc_module.md#id5)

```yaml+jinja
- name: Enable VNC for application test
  purestorage.flasharray.purefa_vnc:
    name: test
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Disable VNC for application test
  purestorage.flasharray.purefa_vnc:
    name: test
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

## [Return Values](purefa_vnc_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vnc**  dictionary | VNC port information for application  Returned: success |
| **index**  integer | Application index number  Returned: success |
| **name**  string | Application name  Returned: success |
| **status**  string | Status of application  Returned: success  Sample: `"healthy"` |
| **version**  string | Application version installed  Returned: success  Sample: `"5.2.1"` |
| **vnc**  dictionary | IP address and port number for VNC connection  Returned: success  Sample: `["10.21.200.34:5900"]` |

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
[Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
[Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
[Communication](index.md#communication-for-purestorage-flasharray)

---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_snmp_agent module – Configure the FlashArray SNMP Agent"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_snmp_agent_module.html
fetched_at: 2026-07-28T02:51:27+00:00
---
# purestorage.flasharray.purefa_snmp_agent module – Configure the FlashArray SNMP Agent

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
> see [Requirements](purefa_snmp_agent_module.md#ansible-collections-purestorage-flasharray-purefa-snmp-agent-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_snmp_agent`.

New in purestorage.flasharray 1.16.0

- [Synopsis](purefa_snmp_agent_module.md#synopsis)
- [Requirements](purefa_snmp_agent_module.md#requirements)
- [Parameters](purefa_snmp_agent_module.md#parameters)
- [Notes](purefa_snmp_agent_module.md#notes)
- [Examples](purefa_snmp_agent_module.md#examples)

## [Synopsis](purefa_snmp_agent_module.md#id1)

- Manage the *localhost* SNMP Agent on a Pure Storage FlashArray.
- This module is not idempotent and will always modify the SNMP Agent due to hidden parameters that cannot be compared to the task parameters.

## [Requirements](purefa_snmp_agent_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_snmp_agent_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **auth_passphrase**  string | SNMP v3 only. Passphrade used by Purity//FA to authenticate the array wit hthe specified managers.  Must be between 8 and 63 non-space ASCII characters. |
| **auth_protocol**  string | SNMP v3 only. Encryption protocol to use  To remove the privacy and auth protocols set *state* to *absent* with *version* set to *v3*  **Choices:**   - `"MD5"` - `"SHA"` |
| **community**  string | SNMP v2c only. Manager community ID under which Purity//FA is to communicate with the specified managers.  To remove the string set *state* to *absent* with *version* set to *v2c* |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **privacy_passphrase**  string | SNMP v3 only. Passphrase to encrypt SNMP messages. Must be between 8 and 63 non-space ASCII characters. |
| **privacy_protocol**  string | SNMP v3 only. Encryption protocol to use  To remove the privacy and auth protocols set *state* to *absent* with *version* set to *v3*  **Choices:**   - `"AES"` - `"DES"` |
| **state**  string | Used to set or clear the SNMP v2c community string or the SNMP v3 auth and privacy protocols.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **user**  string | SNMP v3 only. User ID which must be between 1 and 32 characters. |
| **version**  string | Version of SNMP protocol to use for the manager.  **Choices:**   - `"v2c"` ← (default) - `"v3"` |

## [Notes](purefa_snmp_agent_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_snmp_agent_module.md#id5)

```yaml+jinja
- name: Clear SNMP agent v2c community string
  purestorage.flasharray.purefa_snmp_agent:
    version: v2c
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: Clear SNMP agent v3 auth and privacy protocols
  purestorage.flasharray.purefa_snmp_agent:
    version: v3
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: Update v2c SNMP agent
  puretorage.flasharray.purefa_snmp_agent:
    version: v2c
    community: public
    host: 10.21.22.23
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: Update v3 SNMP manager
  puretorage.flasharray.purefa_snmp_agent:
    version: v3
    auth_protocol: MD5
    auth_passphrase: password
    host: 10.21.22.23
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

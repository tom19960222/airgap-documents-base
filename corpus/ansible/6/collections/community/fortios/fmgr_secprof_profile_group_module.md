---
collection: ansible
version: "6"
title: "community.fortios.fmgr_secprof_profile_group module – Manage security profiles within FortiManager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/fortios/fmgr_secprof_profile_group_module.html
fetched_at: 2026-07-27T17:07:50+00:00
---
# community.fortios.fmgr_secprof_profile_group module – Manage security profiles within FortiManager

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/community/fortios) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_secprof_profile_group`.

- [Synopsis](fmgr_secprof_profile_group_module.md#synopsis)
- [Parameters](fmgr_secprof_profile_group_module.md#parameters)
- [Notes](fmgr_secprof_profile_group_module.md#notes)
- [Examples](fmgr_secprof_profile_group_module.md#examples)
- [Return Values](fmgr_secprof_profile_group_module.md#return-values)

## [Synopsis](fmgr_secprof_profile_group_module.md#id1)

- Manage security profile group which allows you to create a group of security profiles and apply that to a policy.

## [Parameters](fmgr_secprof_profile_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  Default: `"root"` |
| **application_list**  string | Name of an existing Application list. |
| **av_profile**  string | Name of an existing Antivirus profile. |
| **dlp_sensor**  string | Name of an existing DLP sensor. |
| **dnsfilter_profile**  string | Name of an existing DNS filter profile. |
| **icap_profile**  string | Name of an existing ICAP profile. |
| **ips_sensor**  string | Name of an existing IPS sensor. |
| **mms_profile**  string | Name of an existing MMS profile. |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values.  Choices:   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **name**  string | Profile group name. |
| **profile_protocol_options**  string | Name of an existing Protocol options profile. |
| **spamfilter_profile**  string | Name of an existing Spam filter profile. |
| **ssh_filter_profile**  string | Name of an existing SSH filter profile. |
| **ssl_ssh_profile**  string | Name of an existing SSL SSH profile. |
| **voip_profile**  string | Name of an existing VoIP profile. |
| **waf_profile**  string | Name of an existing Web application firewall profile. |
| **webfilter_profile**  string | Name of an existing Web filter profile. |

## [Notes](fmgr_secprof_profile_group_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_secprof_profile_group_module.md#id4)

```yaml+jinja
- name: DELETE Profile
  community.fortios.fmgr_secprof_profile_group:
    name: "Ansible_TEST_Profile_Group"
    mode: "delete"

- name: CREATE Profile
  community.fortios.fmgr_secprof_profile_group:
    name: "Ansible_TEST_Profile_Group"
    mode: "set"
    av_profile: "Ansible_AV_Profile"
    profile_protocol_options: "default"
```

## [Return Values](fmgr_secprof_profile_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  Returned: always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.fortios)

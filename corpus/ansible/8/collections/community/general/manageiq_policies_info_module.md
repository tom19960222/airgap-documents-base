---
collection: ansible
version: "8"
title: "community.general.manageiq_policies_info module – Listing of resource policy_profiles in ManageIQ"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/manageiq_policies_info_module.html
fetched_at: 2026-07-28T01:47:49+00:00
---
# community.general.manageiq_policies_info module – Listing of resource policy_profiles in ManageIQ

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](manageiq_policies_info_module.md#ansible-collections-community-general-manageiq-policies-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.manageiq_policies_info`.

New in community.general 5.8.0

- [Synopsis](manageiq_policies_info_module.md#synopsis)
- [Requirements](manageiq_policies_info_module.md#requirements)
- [Parameters](manageiq_policies_info_module.md#parameters)
- [Attributes](manageiq_policies_info_module.md#attributes)
- [Examples](manageiq_policies_info_module.md#examples)
- [Return Values](manageiq_policies_info_module.md#return-values)

## [Synopsis](manageiq_policies_info_module.md#id1)

- The manageiq_policies module supports listing policy_profiles in ManageIQ.

Aliases: remote_management.manageiq.manageiq_policies_info

## [Requirements](manageiq_policies_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- manageiq-client <https://github.com/ManageIQ/manageiq-api-client-python/>

## [Parameters](manageiq_policies_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **manageiq_connection**  dictionary | ManageIQ connection configuration information. |
| **ca_cert**  aliases: ca_bundle_path  string | The path to a CA bundle file or directory with certificates. |
| **password**  string | ManageIQ password. `MIQ_PASSWORD` environment variable if set. Otherwise, required if no token is passed in. |
| **token**  string | ManageIQ token. `MIQ_TOKEN` environment variable if set. Otherwise, required if no username or password is passed in. |
| **url**  string | ManageIQ environment URL. `MIQ_URL` environment variable if set. Otherwise, it is required to pass it. |
| **username**  string | ManageIQ username. `MIQ_USERNAME` environment variable if set. Otherwise, required if no token is passed in. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests.  **Choices:**   - `false` - `true` ← (default) |
| **resource_id**  integer | The ID of the resource to obtain the profile for.  Must be specified if `resource_name` is not set. Both options are mutually exclusive. |
| **resource_name**  string | The name of the resource to obtain the profile for.  Must be specified if `resource_id` is not set. Both options are mutually exclusive. |
| **resource_type**  string / required | The type of the resource to obtain the profile for.  **Choices:**   - `"provider"` - `"host"` - `"vm"` - `"blueprint"` - `"category"` - `"cluster"` - `"data store"` - `"group"` - `"resource pool"` - `"service"` - `"service template"` - `"template"` - `"tenant"` - `"user"` |

## [Attributes](manageiq_policies_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](manageiq_policies_info_module.md#id5)

```yaml+jinja
- name: List current policy_profile and policies for a provider in ManageIQ
  community.general.manageiq_policies_info:
    resource_name: 'EngLab'
    resource_type: 'provider'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
  register: result
```

## [Return Values](manageiq_policies_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **profiles**  list / elements=dictionary | List current policy_profile and policies for a provider in ManageIQ.  **Returned:** always  **Sample:** `[{"policies": [{"active": true, "description": "OpenSCAP", "name": "openscap policy"}, {"active": "true,", "description": "Analyse incoming container images", "name": "analyse incoming container images"}, {"active": true, "description": "Schedule compliance after smart state analysis", "name": "schedule compliance after smart state analysis"}], "profile_description": "OpenSCAP profile", "profile_name": "openscap profile"}]` |

### Authors

- Alexei Znamensky (@russoz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

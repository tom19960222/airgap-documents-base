---
collection: ansible
version: "6"
title: "community.general.manageiq_policies module – Management of resource policy_profiles in ManageIQ"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/manageiq_policies_module.html
fetched_at: 2026-07-27T17:10:47+00:00
---
# community.general.manageiq_policies module – Management of resource policy_profiles in ManageIQ

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](manageiq_policies_module.md#ansible-collections-community-general-manageiq-policies-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.manageiq_policies`.

- [Synopsis](manageiq_policies_module.md#synopsis)
- [Requirements](manageiq_policies_module.md#requirements)
- [Parameters](manageiq_policies_module.md#parameters)
- [Examples](manageiq_policies_module.md#examples)
- [Return Values](manageiq_policies_module.md#return-values)

## [Synopsis](manageiq_policies_module.md#id1)

- The manageiq_policies module supports adding and deleting policy_profiles in ManageIQ.

## [Requirements](manageiq_policies_module.md#id2)

The below requirements are needed on the host that executes this module.

- manageiq-client <https://github.com/ManageIQ/manageiq-api-client-python/>

## [Parameters](manageiq_policies_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **manageiq_connection**  dictionary | ManageIQ connection configuration information. |
| **ca_cert**  aliases: ca_bundle_path  string | The path to a CA bundle file or directory with certificates. defaults to None. |
| **password**  string | ManageIQ password. `MIQ_PASSWORD` env var if set. otherwise, required if no token is passed in. |
| **token**  string | ManageIQ token. `MIQ_TOKEN` env var if set. otherwise, required if no username or password is passed in. |
| **url**  string | ManageIQ environment url. `MIQ_URL` env var if set. otherwise, it is required to pass it. |
| **username**  string | ManageIQ username. `MIQ_USERNAME` env var if set. otherwise, required if no token is passed in. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests. defaults to True.  Choices:   - `false` - `true` ← (default) |
| **policy_profiles**  list / elements=dictionary | List of dictionaries, each includes the policy_profile `name` key.  Required if *state* is `present` or `absent`. |
| **resource_id**  integer  added in community.general 2.2.0 | The ID of the resource to which the profile should be [un]assigned.  Must be specified if *resource_name* is not set. Both options are mutually exclusive. |
| **resource_name**  string | The name of the resource to which the profile should be [un]assigned.  Must be specified if *resource_id* is not set. Both options are mutually exclusive. |
| **resource_type**  string / required | The type of the resource to which the profile should be [un]assigned.  Choices:   - `"provider"` - `"host"` - `"vm"` - `"blueprint"` - `"category"` - `"cluster"` - `"data store"` - `"group"` - `"resource pool"` - `"service"` - `"service template"` - `"template"` - `"tenant"` - `"user"` |
| **state**  string | `absent` - policy_profiles should not exist,  `present` - policy_profiles should exist,  `list` - list current policy_profiles and policies.  Choices:   - `"absent"` - `"present"` ← (default) - `"list"` |

## [Examples](manageiq_policies_module.md#id4)

```yaml+jinja
- name: Assign new policy_profile for a provider in ManageIQ
  community.general.manageiq_policies:
    resource_name: 'EngLab'
    resource_type: 'provider'
    policy_profiles:
      - name: openscap profile
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Unassign a policy_profile for a provider in ManageIQ
  community.general.manageiq_policies:
    state: absent
    resource_name: 'EngLab'
    resource_type: 'provider'
    policy_profiles:
      - name: openscap profile
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: List current policy_profile and policies for a provider in ManageIQ
  community.general.manageiq_policies:
    state: list
    resource_name: 'EngLab'
    resource_type: 'provider'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false
```

## [Return Values](manageiq_policies_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **manageiq_policies**  dictionary | List current policy_profile and policies for a provider in ManageIQ  Returned: always  Sample: `{"changed": false, "profiles": [{"policies": [{"active": true, "description": "OpenSCAP", "name": "openscap policy"}, {"active": true, "description": "Analyse incoming container images", "name": "analyse incoming container images"}, {"active": true, "description": "Schedule compliance after smart state analysis", "name": "schedule compliance after smart state analysis"}], "profile_description": "OpenSCAP profile", "profile_name": "openscap profile"}]}` |

### Authors

- Daniel Korn (@dkorn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

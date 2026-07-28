---
collection: ansible
version: "6"
title: "community.general.manageiq_alert_profiles module – Configuration of alert profiles for ManageIQ"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/manageiq_alert_profiles_module.html
fetched_at: 2026-07-27T17:10:45+00:00
---
# community.general.manageiq_alert_profiles module – Configuration of alert profiles for ManageIQ

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
> see [Requirements](manageiq_alert_profiles_module.md#ansible-collections-community-general-manageiq-alert-profiles-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.manageiq_alert_profiles`.

- [Synopsis](manageiq_alert_profiles_module.md#synopsis)
- [Requirements](manageiq_alert_profiles_module.md#requirements)
- [Parameters](manageiq_alert_profiles_module.md#parameters)
- [Examples](manageiq_alert_profiles_module.md#examples)

## [Synopsis](manageiq_alert_profiles_module.md#id1)

- The manageiq_alert_profiles module supports adding, updating and deleting alert profiles in ManageIQ.

## [Requirements](manageiq_alert_profiles_module.md#id2)

The below requirements are needed on the host that executes this module.

- manageiq-client <https://github.com/ManageIQ/manageiq-api-client-python/>

## [Parameters](manageiq_alert_profiles_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alerts**  list / elements=string | List of alert descriptions to assign to this profile.  Required if state is “present” |
| **manageiq_connection**  dictionary | ManageIQ connection configuration information. |
| **ca_cert**  aliases: ca_bundle_path  string | The path to a CA bundle file or directory with certificates. defaults to None. |
| **password**  string | ManageIQ password. `MIQ_PASSWORD` env var if set. otherwise, required if no token is passed in. |
| **token**  string | ManageIQ token. `MIQ_TOKEN` env var if set. otherwise, required if no username or password is passed in. |
| **url**  string | ManageIQ environment url. `MIQ_URL` env var if set. otherwise, it is required to pass it. |
| **username**  string | ManageIQ username. `MIQ_USERNAME` env var if set. otherwise, required if no token is passed in. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests. defaults to True.  Choices:   - `false` - `true` ← (default) |
| **name**  string | The unique alert profile name in ManageIQ.  Required when state is “absent” or “present”. |
| **notes**  string | Optional notes for this profile |
| **resource_type**  string | The resource type for the alert profile in ManageIQ. Required when state is “present”.  Choices:   - `"Vm"` - `"ContainerNode"` - `"MiqServer"` - `"Host"` - `"Storage"` - `"EmsCluster"` - `"ExtManagementSystem"` - `"MiddlewareServer"` |
| **state**  string | absent - alert profile should not exist,  present - alert profile should exist,  Choices:   - `"absent"` - `"present"` ← (default) |

## [Examples](manageiq_alert_profiles_module.md#id4)

```yaml+jinja
- name: Add an alert profile to ManageIQ
  community.general.manageiq_alert_profiles:
    state: present
    name: Test profile
    resource_type: ContainerNode
    alerts:
      - Test Alert 01
      - Test Alert 02
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Delete an alert profile from ManageIQ
  community.general.manageiq_alert_profiles:
    state: absent
    name: Test profile
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false
```

### Authors

- Elad Alfassa (@elad661)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

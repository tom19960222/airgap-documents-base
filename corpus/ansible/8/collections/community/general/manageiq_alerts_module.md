---
collection: ansible
version: "8"
title: "community.general.manageiq_alerts module – Configuration of alerts in ManageIQ"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/manageiq_alerts_module.html
fetched_at: 2026-07-28T01:47:46+00:00
---
# community.general.manageiq_alerts module – Configuration of alerts in ManageIQ

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
> see [Requirements](manageiq_alerts_module.md#ansible-collections-community-general-manageiq-alerts-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.manageiq_alerts`.

- [Synopsis](manageiq_alerts_module.md#synopsis)
- [Requirements](manageiq_alerts_module.md#requirements)
- [Parameters](manageiq_alerts_module.md#parameters)
- [Attributes](manageiq_alerts_module.md#attributes)
- [Examples](manageiq_alerts_module.md#examples)

## [Synopsis](manageiq_alerts_module.md#id1)

- The manageiq_alerts module supports adding, updating and deleting alerts in ManageIQ.

Aliases: remote_management.manageiq.manageiq_alerts

## [Requirements](manageiq_alerts_module.md#id2)

The below requirements are needed on the host that executes this module.

- manageiq-client <https://github.com/ManageIQ/manageiq-api-client-python/>

## [Parameters](manageiq_alerts_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | The unique alert description in ManageIQ.  Required when state is “absent” or “present”. |
| **enabled**  boolean | Enable or disable the alert. Required if state is “present”.  **Choices:**   - `false` - `true` |
| **expression**  dictionary | The alert expression for ManageIQ.  Can either be in the “Miq Expression” format or the “Hash Expression format”.  Required if state is “present”. |
| **expression_type**  string | Expression type.  **Choices:**   - `"hash"` ← (default) - `"miq"` |
| **manageiq_connection**  dictionary | ManageIQ connection configuration information. |
| **ca_cert**  aliases: ca_bundle_path  string | The path to a CA bundle file or directory with certificates. |
| **password**  string | ManageIQ password. `MIQ_PASSWORD` environment variable if set. Otherwise, required if no token is passed in. |
| **token**  string | ManageIQ token. `MIQ_TOKEN` environment variable if set. Otherwise, required if no username or password is passed in. |
| **url**  string | ManageIQ environment URL. `MIQ_URL` environment variable if set. Otherwise, it is required to pass it. |
| **username**  string | ManageIQ username. `MIQ_USERNAME` environment variable if set. Otherwise, required if no token is passed in. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests.  **Choices:**   - `false` - `true` ← (default) |
| **options**  dictionary | Additional alert options, such as notification type and frequency |
| **resource_type**  string | The entity type for the alert in ManageIQ. Required when state is “present”.  **Choices:**   - `"Vm"` - `"ContainerNode"` - `"MiqServer"` - `"Host"` - `"Storage"` - `"EmsCluster"` - `"ExtManagementSystem"` - `"MiddlewareServer"` |
| **state**  string | absent - alert should not exist,  present - alert should exist,  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](manageiq_alerts_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](manageiq_alerts_module.md#id5)

```yaml+jinja
- name: Add an alert with a "hash expression" to ManageIQ
  community.general.manageiq_alerts:
    state: present
    description: Test Alert 01
    options:
      notifications:
        email:
          to: ["example@example.com"]
          from: "example@example.com"
    resource_type: ContainerNode
    expression:
        eval_method: hostd_log_threshold
        mode: internal
        options: {}
    enabled: true
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Add an alert with a "miq expression" to ManageIQ
  community.general.manageiq_alerts:
    state: present
    description: Test Alert 02
    options:
      notifications:
        email:
          to: ["example@example.com"]
          from: "example@example.com"
    resource_type: Vm
    expression_type: miq
    expression:
        and:
          - CONTAINS:
              tag: Vm.managed-environment
              value: prod
          - not:
            CONTAINS:
              tag: Vm.host.managed-environment
              value: prod
    enabled: true
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Delete an alert from ManageIQ
  community.general.manageiq_alerts:
    state: absent
    description: Test Alert 01
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false
```

### Authors

- Elad Alfassa (@elad661)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

---
collection: ansible
version: "8"
title: "community.vmware.vmware_vcenter_statistics module – Configures statistics on a vCenter server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_vcenter_statistics_module.html
fetched_at: 2026-07-28T02:01:17+00:00
---
# community.vmware.vmware_vcenter_statistics module – Configures statistics on a vCenter server

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_vcenter_statistics`.

- [Synopsis](vmware_vcenter_statistics_module.md#synopsis)
- [Parameters](vmware_vcenter_statistics_module.md#parameters)
- [Notes](vmware_vcenter_statistics_module.md#notes)
- [Examples](vmware_vcenter_statistics_module.md#examples)
- [Return Values](vmware_vcenter_statistics_module.md#return-values)

## [Synopsis](vmware_vcenter_statistics_module.md#id1)

- This module can be used to configure the vCenter server statistics.
- The remaining settings can be configured with the module `vmware_vcenter_settings`.

## [Parameters](vmware_vcenter_statistics_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **interval_past_day**  dictionary | Settings for vCenter server past day statistic collection. |
| **enabled**  boolean | Past day statistics collection enabled.  **Choices:**   - `false` - `true` ← (default) |
| **interval_minutes**  integer | Interval duration in minutes.  **Choices:**   - `1` - `2` - `3` - `4` - `5` ← (default) |
| **level**  integer | Statistics level.  **Choices:**   - `1` ← (default) - `2` - `3` - `4` |
| **save_for_days**  integer | Save for value in days.  **Choices:**   - `1` ← (default) - `2` - `3` - `4` - `5` |
| **interval_past_month**  dictionary | Settings for vCenter server past month statistic collection. |
| **enabled**  boolean | Past month statistics collection enabled.  **Choices:**   - `false` - `true` ← (default) |
| **interval_hours**  integer | Interval duration in hours.  **Choices:**   - `2` ← (default) |
| **level**  integer | Statistics level.  **Choices:**   - `1` ← (default) - `2` - `3` - `4` |
| **save_for_months**  integer | Save for value in months.  **Choices:**   - `1` ← (default) |
| **interval_past_week**  dictionary | Settings for vCenter server past week statistic collection. |
| **enabled**  boolean | Past week statistics collection enabled.  **Choices:**   - `false` - `true` ← (default) |
| **interval_minutes**  integer | Interval duration in minutes.  **Choices:**   - `30` ← (default) |
| **level**  integer | Statistics level.  **Choices:**   - `1` ← (default) - `2` - `3` - `4` |
| **save_for_weeks**  integer | Save for value in weeks.  **Choices:**   - `1` ← (default) |
| **interval_past_year**  dictionary | Settings for vCenter server past month statistic collection. |
| **enabled**  boolean | Past month statistics collection enabled.  **Choices:**   - `false` - `true` ← (default) |
| **interval_days**  integer | Interval duration in days.  **Choices:**   - `1` ← (default) |
| **level**  integer | Statistics level.  **Choices:**   - `1` ← (default) - `2` - `3` - `4` |
| **save_for_years**  integer | Save for value in years.  **Choices:**   - `1` ← (default) - `2` - `3` - `4` - `5` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_vcenter_statistics_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vcenter_statistics_module.md#id4)

```yaml+jinja
- name: Configure vCenter statistics
  community.vmware.vmware_vcenter_statistics:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    interval_past_day:
      enabled: true
      interval_minutes: 5
      save_for_days: 1
      level: 1
    interval_past_week:
      enabled: true
      level: 1
    interval_past_month:
      enabled: true
      level: 1
    interval_past_year:
      enabled: true
      save_for_years: 1
      level: 1
  delegate_to: localhost
```

## [Return Values](vmware_vcenter_statistics_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **results**  dictionary | metadata about vCenter statistics settings  **Returned:** always  **Sample:** `{"changed": false, "msg": "vCenter statistics already configured properly", "past_day_enabled": true, "past_day_interval": 5, "past_day_level": 1, "past_day_save_for": 1, "past_month_enabled": true, "past_month_interval": 2, "past_month_level": 1, "past_month_save_for": 1, "past_week_enabled": true, "past_week_interval": 30, "past_week_level": 1, "past_week_save_for": 1, "past_year_enabled": true, "past_year_interval": 1, "past_year_level": 1, "past_year_save_for": 1}` |

### Authors

- Christian Kotte (@ckotte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)

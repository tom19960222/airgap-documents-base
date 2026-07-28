---
collection: ansible
version: "8"
title: "community.general.timezone module – Configure timezone setting"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/timezone_module.html
fetched_at: 2026-07-28T01:50:58+00:00
---
# community.general.timezone module – Configure timezone setting

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.timezone`.

- [Synopsis](timezone_module.md#synopsis)
- [Parameters](timezone_module.md#parameters)
- [Attributes](timezone_module.md#attributes)
- [Notes](timezone_module.md#notes)
- [Examples](timezone_module.md#examples)
- [Return Values](timezone_module.md#return-values)

## [Synopsis](timezone_module.md#id1)

- This module configures the timezone setting, both of the system clock and of the hardware clock. If you want to set up the NTP, use [ansible.builtin.service](../../ansible/builtin/service_module.md#ansible-collections-ansible-builtin-service-module) module.
- It is recommended to restart `crond` after changing the timezone, otherwise the jobs may run at the wrong time.
- Several different tools are used depending on the OS/Distribution involved. For Linux it can use `timedatectl` or edit `/etc/sysconfig/clock` or `/etc/timezone` and `hwclock`. On SmartOS, `sm-set-timezone`, for macOS, `systemsetup`, for BSD, `/etc/localtime` is modified. On AIX, `chtz` is used.
- Make sure that the zoneinfo files are installed with the appropriate OS package, like `tzdata` (usually always installed, when not using a minimal installation like Alpine Linux).
- As of Ansible 2.3 support was added for SmartOS and BSDs.
- As of Ansible 2.4 support was added for macOS.
- As of Ansible 2.9 support was added for AIX 6.1+
- Windows and HPUX are not supported, please let us know if you find any other OS/distro in which this fails.

Aliases: system.timezone

## [Parameters](timezone_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hwclock**  aliases: rtc  string | Whether the hardware clock is in UTC or in local timezone.  Default is to keep current setting.  Note that this option is recommended not to change and may fail to configure, especially on virtual environments such as AWS.  **At least one of name and hwclock are required.**  *Only used on Linux.*  **Choices:**   - `"local"` - `"UTC"` |
| **name**  string | Name of the timezone for the system clock.  Default is to keep current setting.  **At least one of name and hwclock are required.** |

## [Attributes](timezone_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](timezone_module.md#id4)

> **Note:**
>
> - On SmartOS the `sm-set-timezone` utility (part of the smtools package) is required to set the zone timezone
> - On AIX only Olson/tz database timezones are usable (POSIX is not supported). - An OS reboot is also required on AIX for the new timezone setting to take effect.

## [Examples](timezone_module.md#id5)

```yaml+jinja
- name: Set timezone to Asia/Tokyo
  community.general.timezone:
    name: Asia/Tokyo
```

## [Return Values](timezone_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff**  complex | The differences about the given arguments.  **Returned:** success |
| **after**  dictionary | The values after change  **Returned:** success |
| **before**  dictionary | The values before change  **Returned:** success |

### Authors

- Shinichi TAMURA (@tmshn)
- Jasper Lievisse Adriaanse (@jasperla)
- Indrajit Raychaudhuri (@indrajitr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_firewall_schedule module – Manage BIG-IP AFM schedule configurations"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_firewall_schedule_module.html
fetched_at: 2026-07-27T17:26:45+00:00
---
# f5networks.f5_modules.bigip_firewall_schedule module – Manage BIG-IP AFM schedule configurations

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_firewall_schedule`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_firewall_schedule_module.md#synopsis)
- [Parameters](bigip_firewall_schedule_module.md#parameters)
- [Notes](bigip_firewall_schedule_module.md#notes)
- [Examples](bigip_firewall_schedule_module.md#examples)
- [Return Values](bigip_firewall_schedule_module.md#return-values)

## [Synopsis](bigip_firewall_schedule_module.md#id1)

- Manage BIG-IP AFM (Avanced Firewall Manager) schedule configurations.

## [Parameters](bigip_firewall_schedule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **daily_hour_end**  string | Specifies the time of day the rule will stop being used.  When not defined, the default of `24:00` is used when creating a new schedule.  The time zone is always assumed to be UTC and values must be provided as `HH:MM` using 24hour clock format. |
| **daily_hour_start**  string | Specifies the time of day the rule will start to be in use.  The value must be a time before `daily_hour_end`.  When not defined, the default of `0:00` is used when creating a new schedule.  When the value is set to `all-day` both `daily_hour_end` and `daily_hour_start` are reset to their respective defaults.  The time zone is always assumed to be UTC and values must be provided as `HH:MM` using 24hour clock format. |
| **date_valid_end**  string | Specifies the end date/time this schedule will apply to the rule.  The date must be after `date_valid_start`  When not defined, the default of `indefinite` is used when creating a new schedule.  The time zone is always assumed to be UTC.  The datetime format should always be in `YYYY-MM-DD:HH:MM:SS` format. |
| **date_valid_start**  string | Specifies the start date/time this schedule will apply to the rule.  When not defined the default of `epoch` is used when creating a new schedule.  The time zone is always assumed to be UTC.  The datetime format should always be in `YYYY-MM-DD:HH:MM:SS` format. |
| **days_of_week**  list / elements=string | Specifies which days of the week the rule will be applied.  When not defined, the default value of `all` is used when creating a new schedule.  The `all` value is mutually exclusive with other choices.  Choices:   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` - `"all"` |
| **description**  string | Specifies the user defined description text. |
| **name**  string / required | Specifies the name of the AFM schedule configuration. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource is removed.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_firewall_schedule_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_firewall_schedule_module.md#id4)

```yaml+jinja
- name: Create a 6 hour two day schedule, no start/end date
  bigip_firewall_schedule:
    name: barfoo
    daily_hour_start: 13:00
    daily_hour_end: 19:00
    days_of_week:
      - monday
      - tuesday
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a seven day schedule with start/end date
  bigip_firewall_schedule:
    name: foobar
    date_valid_start: "{{ lookup('pipe','date +%Y-%m-%d:%H:%M:%S') }}"
    date_valid_end: "{{ lookup('pipe','date -d \"now + 7 days\" +%Y-%m-%d:%H:%M:%S') }}"
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Modify created schedule to all-day
  bigip_firewall_schedule:
    name: barfoo
    daily_hour_start: all-day
    days_of_week:
      - monday
      - tuesday
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Modify a schedule to have no end date
  bigip_firewall_schedule:
    name: foobar
    date_valid_start: "{{ lookup('pipe','date +%Y-%m-%d:%H:%M:%S') }}"
    date_valid_end: "indefinite"
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove created schedule
  bigip_firewall_schedule:
    name: foobar
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_firewall_schedule_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **daily_hour_end**  string | The time of day the rule will stop being used.  Returned: changed  Sample: `"18:00"` |
| **daily_hour_start**  string | The time of day the rule will start to be in use.  Returned: changed  Sample: `"13:00"` |
| **date_valid_end**  string | The end date/time schedule will apply to the rule.  Returned: changed  Sample: `"2019-03-11:15:30:00"` |
| **date_valid_start**  string | The start date/time schedule will apply to the rule.  Returned: changed  Sample: `"2019-03-01:15:30:00"` |
| **days_of_week**  list / elements=string | The days of the week the rule will be applied.  Returned: changed  Sample: `["monday", "tuesday"]` |
| **description**  string | The user defined description text.  Returned: changed  Sample: `"Foo is bar"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

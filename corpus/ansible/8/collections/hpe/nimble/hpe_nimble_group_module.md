---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_group module – Manage the HPE Nimble Storage group"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_group_module.html
fetched_at: 2026-07-28T02:34:20+00:00
---
# hpe.nimble.hpe_nimble_group module – Manage the HPE Nimble Storage group

> **Note:**
>
> This module is part of the [hpe.nimble collection](https://galaxy.ansible.com/ui/repo/published/hpe/nimble/) (version 1.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hpe.nimble`.
> You need further requirements to be able to use this module,
> see [Requirements](hpe_nimble_group_module.md#ansible-collections-hpe-nimble-hpe-nimble-group-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_group`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_group_module.md#synopsis)
- [Requirements](hpe_nimble_group_module.md#requirements)
- [Parameters](hpe_nimble_group_module.md#parameters)
- [Notes](hpe_nimble_group_module.md#notes)
- [Examples](hpe_nimble_group_module.md#examples)

## [Synopsis](hpe_nimble_group_module.md#id1)

- Manage an HPE Nimble Storage group on an Nimble Storage array.

## [Requirements](hpe_nimble_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alarms**  boolean | Whether alarm feature is enabled.  **Choices:**   - `false` - `true` |
| **alert_from_email_addrs**  string | From email address to use while sending emails. Case insensitive email address. |
| **alert_min_level**  string | Minimum level of alert to be notified.  **Choices:**   - `"info"` - `"notice"` - `"warning"` - `"critical"` |
| **alert_to_email_addrs**  string | Comma-separated list of email addresses to receive emails. Comma separated email list. |
| **allow_analytics_gui**  boolean | Specify whether to allow HPE Nimble Storage to use Google Analytics in the GUI. HPE Nimble Storage uses Google Analytics to gather data related to GUI usage. The data gathered is used to evaluate and improve the product.  **Choices:**   - `false` - `true` |
| **allow_support_tunnel**  boolean | Whether to allow support tunnel.  **Choices:**   - `false` - `true` |
| **auto_switchover**  boolean | Whether automatic switchover of Group management services feature is enabled.  **Choices:**   - `false` - `true` |
| **autoclean_unmanaged_snapshots**  boolean | Whether autoclean unmanaged snapshots feature is enabled.  **Choices:**   - `false` - `true` |
| **autoclean_unmanaged_snapshots_ttl_unit**  integer | Unit for unmanaged snapshot time to live. |
| **autosupport**  boolean | Whether to send autosupport.  **Choices:**   - `false` - `true` |
| **cc_mode**  boolean | Enable or disable Common Criteria mode.  **Choices:**   - `false` - `true` |
| **change_name**  string | Change name of the existing group. |
| **check_migrate**  boolean | Check if the group Management Service can be migrated to the group Management Service backup array.  **Choices:**   - `false` - `true` |
| **date**  integer | Unix epoch time local to the group. Seconds since last epoch. Example- 3400. |
| **default_iscsi_target_scope**  string | Newly created volumes are exported under iSCSI Group Target or iSCSI Volume Target.  **Choices:**   - `"volume"` - `"group"` |
| **default_volume_limit**  integer | Default limit for a volume space usage as a percentage of volume size. Volume will be taken offline/made non-writable on exceeding its limit. Percentage as integer from 0 to 100. |
| **dns_servers**  list / elements=dictionary | IP addresses for this group’s dns servers. |
| **domain_name**  string | Domain name for this group. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. |
| **fc_enabled**  boolean | Whether FC is enabled on this group.  **Choices:**   - `false` - `true` |
| **force**  boolean | Can be used with halt or merge flag. Halt remaining arrays when one or more is unreachable. Ignore warnings and forcibly merge specified group with this group.  **Choices:**   - `false` ← (default) - `true` |
| **group_snapshot_ttl**  integer | Snapshot Time-to-live(TTL) configured at group level for automatic deletion of unmanaged snapshots. Value 0 indicates unlimited TTL. |
| **group_target_enabled**  boolean | Is group_target enabled on this group.  **Choices:**   - `false` - `true` |
| **group_target_name**  string | Iscsi target name for this group. String of up to 255 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for the group target name. |
| **halt**  boolean | Halt all arrays in the group.  **Choices:**   - `false` - `true` |
| **host**  string / required | HPE Nimble Storage IP address. |
| **iscsi_enabled**  boolean | Whether iSCSI is enabled on this group.  **Choices:**   - `false` - `true` |
| **isns_enabled**  boolean | Whether iSNS is enabled.  **Choices:**   - `false` - `true` |
| **isns_port**  integer | Port number for iSNS Server. Positive integer value up to 65535 representing TCP/IP port. |
| **isns_server**  string | Hostname or IP Address of iSNS Server. |
| **level**  string | Level of the test alert.  **Choices:**   - `"info"` - `"notice"` - `"warning"` - `"critical"` |
| **login_banner_after_auth**  boolean | Should the banner be displayed before the user credentials are prompted or after prompting the user credentials.  **Choices:**   - `false` - `true` |
| **login_banner_message**  string | The message for the login banner that is displayed during user login activity. String upto 2048 characters. |
| **login_banner_reset**  string | This will reset the banner to the version of the installed NOS. When login_banner_after_auth is specified, login_banner_reset can not be set to true. |
| **merge**  boolean | Perform group merge with the specified group.  **Choices:**   - `false` - `true` |
| **migrate**  boolean | Migrate the group Management Service to the current group Management Service backup array.  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the group. |
| **ntp_server**  string | Either IP address or hostname of the NTP server for this group. Plain string. |
| **password**  string / required | HPE Nimble Storage password. |
| **proxy_password**  string | Password to authenticate with HTTP Proxy Server. |
| **proxy_port**  integer | Proxy Port of HTTP Proxy Server. Integer value between 0-65535 representing TCP/IP port. |
| **proxy_server**  string | Hostname or IP Address of HTTP Proxy Server. Setting this attribute to an empty string will unset all proxy settings. |
| **proxy_username**  string | Username to authenticate with HTTP Proxy Server. HTTP proxy server username, string up to 255 characters, special  characters ([, ], `, ;, ampersand, tab, space, newline) are not allowed. |
| **reboot**  boolean | Reboot all arrays in the group.  **Choices:**   - `false` - `true` |
| **repl_throttle_list**  list / elements=dictionary | All the replication bandwidth limits on the system. All the throttles for the partner. |
| **send_alert_to_support**  boolean | Whether to send alert to Support.  **Choices:**   - `false` - `true` |
| **skip_secondary_mgmt_ip**  boolean | Skip check for secondary management IP address.  **Choices:**   - `false` - `true` |
| **smtp_auth_enabled**  boolean | Whether SMTP Server requires authentication.  **Choices:**   - `false` - `true` |
| **smtp_auth_password**  string | Password to authenticate with SMTP Server. |
| **smtp_auth_username**  string | Username to authenticate with SMTP Server. |
| **smtp_encrypt_type**  string | Level of encryption for SMTP.  **Choices:**   - `"none"` - `"starttls"` - `"ssl"` |
| **smtp_port**  integer | Port number of SMTP Server. |
| **snmp_community**  string | Community string to be used with SNMP. |
| **snmp_get_enabled**  boolean | Whether to accept SNMP get commands.  **Choices:**   - `false` - `true` |
| **snmp_get_port**  integer | Port number to which SNMP get requests should be sent. |
| **snmp_sys_contact**  string | Name of the SNMP administrator. Plain string. |
| **snmp_sys_location**  string | Location of the group. Plain string. |
| **snmp_trap_enabled**  boolean | Whether to enable SNMP traps.  **Choices:**   - `false` - `true` |
| **snmp_trap_host**  string | Hostname or IP Address to send SNMP traps. |
| **snmp_trap_port**  integer | Port number of SNMP trap host. |
| **src_group_ip**  string | IP address of the source group. |
| **src_group_name**  string | Name of the source group. |
| **src_passphrase**  string | Source group encryption passphrase. Encryption passphrase. String with size from 8 to 64 printable characters. |
| **src_password**  string | Password of the source group. |
| **src_username**  string | Username of the source group. |
| **state**  string / required | The group operation.  **Choices:**   - `"present"` - `"absent"` |
| **syslogd_enabled**  boolean | Is syslogd enabled on this system.  **Choices:**   - `false` - `true` |
| **syslogd_port**  integer | Port number for syslogd server. |
| **syslogd_server**  string | Hostname of the syslogd server. |
| **tdz_enabled**  boolean | Is Target Driven Zoning (TDZ) enabled on this group.  **Choices:**   - `false` - `true` |
| **tdz_prefix**  string | Target Driven Zoning (TDZ) prefix for peer zones created by TDZ. |
| **test_alert**  boolean | Generate a test alert.  **Choices:**   - `false` - `true` |
| **timezone**  string | Timezone in which this group is located. Plain string. |
| **tlsv1_enabled**  boolean | Enable or disable TLSv1.0 and TLSv1.1.  **Choices:**   - `false` - `true` |
| **user_inactivity_timeout**  integer | The amount of time in seconds that the user session is inactive before timing out. User inactivity timeout in second, valid range is from 1 to 43200. |
| **username**  string / required | HPE Nimble Storage user name. |
| **validate_merge**  boolean | Perform group merge validation.  **Choices:**   - `false` - `true` |
| **vss_validation_timeout**  integer | The amount of time in seconds to validate Microsoft VSS application synchronization before timing out. VSS validation timeout in second, valid range is from 1 to 3600. |
| **vvol_enabled**  boolean | Are vVol enabled on this group.  **Choices:**   - `false` - `true` |

## [Notes](hpe_nimble_group_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_group_module.md#id5)

```yaml+jinja
- name: Update group
  hpe.nimble.hpe_nimble_group:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    send_alert_to_support: "{{ send_alert_to_support }}"
    alert_to_email_addrs: "{{ alert_to_email_addrs }}"
    state: "present"

- name: Reboot group
  hpe.nimble.hpe_nimble_group:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: "present"
    reboot: true

- name: Halt group
  hpe.nimble.hpe_nimble_group:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: "present"
    halt: true

- name: Validate merge group
  hpe.nimble.hpe_nimble_group:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    src_group_ip: "{{ src_group_ip }}"
    src_password: "{{ src_password }}"
    skip_secondary_mgmt_ip: "{{ skip_secondary_mgmt_ip }}"
    src_passphrase: "{{ src_passphrase }}"
    state: "present"
    validate_merge: true

- name: Merge group
  hpe.nimble.hpe_nimble_group:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    src_group_ip: "{{ src_group_ip }}"
    src_password: "{{ src_password }}"
    skip_secondary_mgmt_ip: "{{ skip_secondary_mgmt_ip }}"
    src_passphrase: "{{ src_passphrase }}"
    state: "present"
    merge: true

- name: Test alert group
  hpe.nimble.hpe_nimble_group:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    level: "{{ level }}"
    state: "present"
    test_alert: true

- name: Migrate group
  hpe.nimble.hpe_nimble_group:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: "present"
    migrate: true

- name: Check migrate group
  hpe.nimble.hpe_nimble_group:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: "present"
    check_migrate: true
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)

---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_ntp module – Manage NTP configuration on SONiC."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_ntp_module.html
fetched_at: 2026-07-28T02:03:44+00:00
---
# dellemc.enterprise_sonic.sonic_ntp module – Manage NTP configuration on SONiC.

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_ntp`.

New in dellemc.enterprise_sonic 2.0.0

- [Synopsis](sonic_ntp_module.md#synopsis)
- [Parameters](sonic_ntp_module.md#parameters)
- [Examples](sonic_ntp_module.md#examples)
- [Return Values](sonic_ntp_module.md#return-values)

## [Synopsis](sonic_ntp_module.md#id1)

- This module provides configuration management of NTP for devices running SONiC.

## [Parameters](sonic_ntp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies NTP related configurations. |
| **enable_ntp_auth**  boolean | Enable or disable NTP authentication.  **Choices:**   - `false` - `true` |
| **ntp_keys**  list / elements=dictionary | List of NTP authentication keys. |
| **encrypted**  boolean | NTP authentication key_value is encrypted.  encrypted can not be deleted.  When “state” is “merged”, “encrypted” is required.  **Choices:**   - `false` - `true` |
| **key_id**  integer / required | NTP authentication key identifier. |
| **key_type**  string | NTP authentication key type.  key_type can not be deleted.  When “state” is “merged”, “key_type” is required.  **Choices:**   - `"NTP_AUTH_SHA1"` - `"NTP_AUTH_MD5"` - `"NTP_AUTH_SHA2_256"` |
| **key_value**  string | NTP authentication key value.  key_value can not be deleted.  When “state” is “merged”, “key_value” is required. |
| **servers**  list / elements=dictionary | List of NTP servers.  minpoll and maxpoll are required to be configured together. |
| **address**  string / required | IPv4/IPv6 address or host name of NTP server. |
| **key_id**  integer | NTP authentication key used by server.  Key_id can not be deleted. |
| **maxpoll**  integer | Maximum poll interval to poll NTP server.  maxpoll can not be deleted. |
| **minpoll**  integer | Minimum poll interval to poll NTP server.  minpoll can not be deleted. |
| **prefer**  boolean | Indicates whether this server should be preferred.  prefer can not be deleted.  **Choices:**   - `false` - `true` |
| **source_interfaces**  list / elements=string | List of names of NTP source interfaces. |
| **trusted_keys**  list / elements=integer | List of trusted NTP authentication keys. |
| **vrf**  string | VRF name on which NTP is enabled. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Examples](sonic_ntp_module.md#id3)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
#sonic# show ntp server
#----------------------------------------------------------------------------
#NTP Servers                     minpoll maxpoll Prefer Authentication key ID
#----------------------------------------------------------------------------
#10.11.0.1                       6       10      False
#10.11.0.2                       5       9       False
#dell.com                        6       9       False
#dell.org                        7       10      True
#
- name: Delete NTP server configuration
  sonic_ntp:
    config:
      servers:
        - address: 10.11.0.2
        - address: dell.org
    state: deleted

# After state:
# ------------
#
#sonic# show ntp server
#----------------------------------------------------------------------------
#NTP Servers                     minpoll maxpoll Prefer Authentication key ID
#----------------------------------------------------------------------------
#10.11.0.1                       6       10      False
#dell.com                        6       9       False
#
#
# Using deleted
#
# Before state:
# -------------
#
#sonic# show ntp global
#----------------------------------------------
#NTP Global Configuration
#----------------------------------------------
#NTP source-interfaces:  Ethernet0, Ethernet4, Ethernet8, Ethernet16
#
- name: Delete NTP source-interface configuration
  sonic_ntp:
    config:
      source_interfaces:
        - Ethernet8
        - Ethernet16
    state: deleted

# After state:
# ------------
#
#sonic# show ntp global
#----------------------------------------------
#NTP Global Configuration
#----------------------------------------------
#NTP source-interfaces:  Ethernet0, Ethernet4
#
#
# Using deleted
#
# Before state:
# -------------
#
#sonic# show running-configuration | grep ntp
#ntp authentication-key 8 sha1 U2FsdGVkX1/NpJrdOeyMeUHEkSohY6azY9VwbAqXRTY= encrypted
#ntp authentication-key 10 md5 U2FsdGVkX1/Gxds/5pscCvIKbVngGaKka4SQineS51Y= encrypted
#ntp authentication-key 20 sha2-256 U2FsdGVkX1/eAzKj1teKhYWD7tnzOsYOijGeFAT0rKM= encrypted
#
- name: Delete NTP key configuration
  sonic_ntp:
    config:
      ntp_keys:
        - key_id: 10
        - key_id: 20
    state: deleted
#
# After state:
# ------------
#
#sonic# show running-configuration | grep ntp
#ntp authentication-key 8 sha1 U2FsdGVkX1/NpJrdOeyMeUHEkSohY6azY9VwbAqXRTY= encrypted
#
#
# Using merged
#
# Before state:
# -------------
#
#sonic# show ntp server
#----------------------------------------------------------------------------
#NTP Servers                     minpoll maxpoll Prefer Authentication key ID
#----------------------------------------------------------------------------
#10.11.0.1                       6       10      False
#dell.com                        6       9       False
#
- name: Merge NTP server configuration
  sonic_ntp:
    config:
      servers:
        - address: 10.11.0.2
          minpoll: 5
        - address: dell.org
          minpoll: 7
          maxpoll: 10
          prefer: true
    state: merged

# After state:
# ------------
#
#sonic# show ntp server
#----------------------------------------------------------------------------
#NTP Servers                     minpoll maxpoll Prefer Authentication key ID
#----------------------------------------------------------------------------
#10.11.0.1                       6       10      Flase
#10.11.0.2                       5       10      Flase
#dell.com                        6       9       Flase
#dell.org                        7       10      True
#
#
# Using merged
#
# Before state:
# -------------
#
#sonic# show ntp global
#----------------------------------------------
#NTP Global Configuration
#----------------------------------------------
#NTP source-interfaces:  Ethernet0, Ethernet4
#
- name: Merge NTP source-interface configuration
  sonic_ntp:
    config:
      source_interfaces:
        - Ethernet8
        - Ethernet16
    state: merged

# After state:
# ------------
#
#sonic# show ntp global
#----------------------------------------------
#NTP Global Configuration
#----------------------------------------------
#NTP source-interfaces:  Ethernet0, Ethernet4, Ethernet8, Ethernet16
#
#
# Using merged
#
# Before state:
# -------------
#
#sonic# show running-configuration | grep ntp
#ntp authentication-key 8 sha1 U2FsdGVkX1/NpJrdOeyMeUHEkSohY6azY9VwbAqXRTY= encrypted
#
- name: Merge NTP key configuration
  sonic_ntp:
    config:
      ntp_keys:
        - key_id: 10
          key_type: NTP_AUTH_MD5
          key_value: dellemc10
          encrypted: false
        - key_id: 20
          key_type: NTP_AUTH_SHA2_256
          key_value: dellemc20
          encrypted: false
    state: merged
#
# After state:
# ------------
#
#sonic# show running-configuration | grep ntp
#ntp authentication-key 8 sha1 U2FsdGVkX1/NpJrdOeyMeUHEkSohY6azY9VwbAqXRTY= encrypted
#ntp authentication-key 10 md5 U2FsdGVkX1/Gxds/5pscCvIKbVngGaKka4SQineS51Y= encrypted
#ntp authentication-key 20 sha2-256 U2FsdGVkX1/eAzKj1teKhYWD7tnzOsYOijGeFAT0rKM= encrypted
#
# Using replaced
#
# Before state:
# -------------
#
#sonic# show ntp server
#----------------------------------------------------------------------------
#NTP Servers                     minpoll maxpoll Prefer Authentication key ID
#----------------------------------------------------------------------------
#10.11.0.1                       6       10      False
#dell.com                        6       9       False
#
- name: Replace NTP server configuration
  sonic_ntp:
    config:
      servers:
        - address: 10.11.0.2
          minpoll: 5
          maxpoll: 9
        - address: dell.com
          minpoll: 7
          maxpoll: 10
          prefer: true
    state: replaced
#
# After state:
# ------------
#
#sonic# show ntp server
#----------------------------------------------------------------------------
#NTP Servers                     minpoll maxpoll Prefer Authentication key ID
#----------------------------------------------------------------------------
#10.11.0.1                       6       10      False
#10.11.0.2                       5       9       False
#dell.com                        7       10      True
#
# Using overridden
#
# Before state:
# -------------
#
#sonic# show ntp server
#----------------------------------------------------------------------------
#NTP Servers                     minpoll maxpoll Prefer Authentication key ID
#----------------------------------------------------------------------------
#10.11.0.1                       6       10      False
#dell.com                        6       9       False
#
#sonic# show ntp global
#----------------------------------------------
#NTP Global Configuration
#----------------------------------------------
#NTP source-interfaces:  Ethernet0, Ethernet4
#
- name: Overridden NTP configuration
  sonic_ntp:
    config:
      servers:
        - address: 10.11.0.2
          minpoll: 5
        - address: dell.com
          minpoll: 7
          maxpoll: 10
          prefer: true
    state: overridden
#
# After state:
# ------------
#
# After state:
# ------------
#
#sonic# show ntp server
#----------------------------------------------------------------------------
#NTP Servers                     minpoll maxpoll Prefer Authentication key ID
#----------------------------------------------------------------------------
#10.11.0.2                       5       10      False
#dell.com                        7       10      True
#
#sonic# show ntp global
#
```

## [Return Values](sonic_ntp_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- 13. Zhang (@mingjunzhang2019)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)

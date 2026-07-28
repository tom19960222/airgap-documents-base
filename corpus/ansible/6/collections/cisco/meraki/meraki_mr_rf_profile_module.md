---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_mr_rf_profile module – Manage RF profiles for Meraki wireless networks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_mr_rf_profile_module.html
fetched_at: 2026-07-27T17:00:23+00:00
---
# cisco.meraki.meraki_mr_rf_profile module – Manage RF profiles for Meraki wireless networks

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/cisco/meraki) (version 2.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
>
> To use it in a playbook, specify: `cisco.meraki.meraki_mr_rf_profile`.

- [Synopsis](meraki_mr_rf_profile_module.md#synopsis)
- [Parameters](meraki_mr_rf_profile_module.md#parameters)
- [Notes](meraki_mr_rf_profile_module.md#notes)
- [Examples](meraki_mr_rf_profile_module.md#examples)
- [Return Values](meraki_mr_rf_profile_module.md#return-values)

## [Synopsis](meraki_mr_rf_profile_module.md#id1)

- Allows for configuration of radio frequency (RF) profiles in Meraki MR wireless networks.

## [Parameters](meraki_mr_rf_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ap_band_settings**  dictionary | Settings that will be enabled if selectionType is set to ‘ap’. |
| **band_steering_enabled**  boolean | Steers client to most open band.  Choices:   - `false` - `true` |
| **mode**  aliases: band_operation_mode  string | Sets which RF band the AP will support.  Choices:   - `"2.4ghz"` - `"5ghz"` - `"dual"` |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **band_selection_type**  string | Sets whether band selection is assigned per access point or SSID.  This param is required on creation.  Choices:   - `"ssid"` - `"ap"` |
| **client_balancing_enabled**  boolean | Steers client to best available access point.  Choices:   - `false` - `true` |
| **five_ghz_settings**  dictionary | Settings related to 5Ghz band. |
| **channel_width**  string | Sets channel width (MHz) for 5Ghz band.  Choices:   - `"auto"` - `"20"` - `"40"` - `"80"` |
| **max_power**  integer | Sets max power (dBm) of 5Ghz band.  Can be integer between 8 and 30. |
| **min_bitrate**  integer | Sets minimum bitrate (Mbps) of 5Ghz band.  Choices:   - `6` - `9` - `12` - `18` - `24` - `36` - `48` - `54` |
| **min_power**  integer | Sets minmimum power (dBm) of 5Ghz band.  Can be integer between 8 and 30. |
| **rxsop**  integer | The RX-SOP level controls the sensitivity of the radio.  It is strongly recommended to use RX-SOP only after consulting a wireless expert.  RX-SOP can be configured in the range of -65 to -95 (dBm). |
| **valid_auto_channels**  list / elements=integer | Sets valid auto channels for 5Ghz band.  Choices:   - `36` - `40` - `44` - `48` - `52` - `56` - `60` - `64` - `100` - `104` - `108` - `112` - `116` - `120` - `124` - `128` - `132` - `136` - `140` - `144` - `149` - `153` - `157` - `161` - `165` |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **min_bitrate_type**  string | Type of minimum bitrate.  Choices:   - `"band"` - `"ssid"` |
| **name**  string | The unique name of the new profile.  This param is required on creation. |
| **net_id**  string | ID of network. |
| **net_name**  string | Name of network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **profile_id**  aliases: id  string | Unique identifier of existing RF profile. |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **state**  string | Query, edit, or delete wireless RF profile settings.  Choices:   - `"present"` ← (default) - `"query"` - `"absent"` |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **two_four_ghz_settings**  dictionary | Settings related to 2.4Ghz band |
| **ax_enabled**  boolean | Determines whether ax radio on 2.4Ghz band is on or off.  Choices:   - `false` - `true` |
| **max_power**  integer | Sets max power (dBm) of 2.4Ghz band.  Can be integer between 5 and 30. |
| **min_bitrate**  float | Sets minimum bitrate (Mbps) of 2.4Ghz band.  Choices:   - `1.0` - `2.0` - `5.5` - `6.0` - `9.0` - `11.0` - `12.0` - `18.0` - `24.0` - `36.0` - `48.0` - `54.0` |
| **min_power**  integer | Sets minmimum power (dBm) of 2.4Ghz band.  Can be integer between 5 and 30. |
| **rxsop**  integer | The RX-SOP level controls the sensitivity of the radio.  It is strongly recommended to use RX-SOP only after consulting a wireless expert.  RX-SOP can be configured in the range of -65 to -95 (dBm). |
| **valid_auto_channels**  list / elements=integer | Sets valid auto channels for 2.4Ghz band.  Choices:   - `1` - `6` - `11` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_mr_rf_profile_module.md#id3)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mr_rf_profile_module.md#id4)

```yaml+jinja
- name: Create RF profile in check mode
  meraki_mr_rf_profile:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    name: Test Profile
    band_selection_type: ap
    client_balancing_enabled: True
    ap_band_settings:
        mode: dual
        band_steering_enabled: true
    five_ghz_settings:
      max_power: 10
      min_bitrate: 12
      min_power: 8
      rxsop: -65
      channel_width: 20
      valid_auto_channels:
        - 36
        - 40
        - 44
    two_four_ghz_settings:
      max_power: 10
      min_bitrate: 12
      min_power: 8
      rxsop: -65
      ax_enabled: false
      valid_auto_channels:
        - 1
  delegate_to: localhost

- name: Query all RF profiles
  meraki_mr_rf_profile:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: query
  delegate_to: localhost

- name: Query one RF profile by ID
  meraki_mr_rf_profile:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: query
    profile_id: '{{ profile_id }}'
  delegate_to: localhost

- name: Update profile
  meraki_mr_rf_profile:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    profile_id: 12345
    band_selection_type: ap
    client_balancing_enabled: True
    ap_band_settings:
        mode: dual
        band_steering_enabled: true
    five_ghz_settings:
      max_power: 10
      min_bitrate: 12
      min_power: 8
      rxsop: -65
      channel_width: 20
      valid_auto_channels:
        - 36
        - 44
    two_four_ghz_settings:
      max_power: 10
      min_bitrate: 12
      min_power: 8
      rxsop: -75
      ax_enabled: false
      valid_auto_channels:
        - 1
  delegate_to: localhost

- name: Delete RF profile
  meraki_mr_rf_profile:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: absent
    profile_id: 12345
  delegate_to: localhost
```

## [Return Values](meraki_mr_rf_profile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | List of wireless RF profile settings.  Returned: success |
| **ap_band_settings**  complex | Settings that will be enabled if selectionType is set to ‘ap’.  Returned: success |
| **band_steering_enabled**  boolean | Steers client to most open band.  Returned: success  Sample: `true` |
| **mode**  string | Sets which RF band the AP will support.  Returned: success  Sample: `"dual"` |
| **band_selection_type**  string | Sets whether band selection is assigned per access point or SSID.  This param is required on creation.  Returned: success  Sample: `"ap"` |
| **client_balancing_enabled**  boolean | Steers client to best available access point.  Returned: success  Sample: `true` |
| **five_ghz_settings**  complex | Settings related to 5Ghz band.  Returned: success |
| **channel_width**  string | Sets channel width (MHz) for 5Ghz band.  Returned: success  Sample: `"auto"` |
| **max_power**  integer | Sets max power (dBm) of 5Ghz band.  Can be integer between 8 and 30.  Returned: success  Sample: `12` |
| **min_bitrate**  integer | Sets minimum bitrate (Mbps) of 5Ghz band.  Returned: success  Sample: `6` |
| **min_power**  integer | Sets minmimum power (dBm) of 5Ghz band.  Can be integer between 8 and 30.  Returned: success  Sample: `12` |
| **rxsop**  integer | The RX-SOP level controls the sensitivity of the radio.  Returned: success  Sample: `-70` |
| **valid_auto_channels**  list / elements=string | Sets valid auto channels for 5Ghz band.  Returned: success |
| **id**  string | Unique identifier of existing RF profile.  Returned: success  Sample: `"12345"` |
| **min_bitrate_type**  string | Type of minimum bitrate.  Returned: success  Sample: `"ssid"` |
| **name**  string | The unique name of the new profile.  This param is required on creation.  Returned: success  Sample: `"Guest RF profile"` |
| **two_four_ghz_settings**  complex | Settings related to 2.4Ghz band  Returned: success |
| **ax_enabled**  boolean | Determines whether ax radio on 2.4Ghz band is on or off.  Returned: success  Sample: `true` |
| **max_power**  integer | Sets max power (dBm) of 2.4Ghz band.  Returned: success  Sample: `12` |
| **min_bitrate**  float | Sets minimum bitrate (Mbps) of 2.4Ghz band.  Returned: success  Sample: `5.5` |
| **min_power**  integer | Sets minmimum power (dBm) of 2.4Ghz band.  Returned: success  Sample: `12` |
| **rxsop**  integer | The RX-SOP level controls the sensitivity of the radio.  Returned: success  Sample: `-70` |
| **valid_auto_channels**  list / elements=string | Sets valid auto channels for 2.4Ghz band.  Returned: success  Sample: `["6"]` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)

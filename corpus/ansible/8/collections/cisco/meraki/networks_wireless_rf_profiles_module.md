---
collection: ansible
version: "8"
title: "cisco.meraki.networks_wireless_rf_profiles module – Resource module for networks _wireless _rfprofiles"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_wireless_rf_profiles_module.html
fetched_at: 2026-07-28T01:35:45+00:00
---
# cisco.meraki.networks_wireless_rf_profiles module – Resource module for networks _wireless _rfprofiles

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/ui/repo/published/cisco/meraki/) (version 2.17.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
> You need further requirements to be able to use this module,
> see [Requirements](networks_wireless_rf_profiles_module.md#ansible-collections-cisco-meraki-networks-wireless-rf-profiles-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_wireless_rf_profiles`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_wireless_rf_profiles_module.md#synopsis)
- [Requirements](networks_wireless_rf_profiles_module.md#requirements)
- [Parameters](networks_wireless_rf_profiles_module.md#parameters)
- [Notes](networks_wireless_rf_profiles_module.md#notes)
- [See Also](networks_wireless_rf_profiles_module.md#see-also)
- [Examples](networks_wireless_rf_profiles_module.md#examples)
- [Return Values](networks_wireless_rf_profiles_module.md#return-values)

## [Synopsis](networks_wireless_rf_profiles_module.md#id1)

- Manage operations create, update and delete of the resource networks _wireless _rfprofiles.
- Creates new RF profile for this network.
- Delete a RF Profile.
- Updates specified RF profile for this network.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_wireless_rf_profiles_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_wireless_rf_profiles_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **apBandSettings**  dictionary | Settings that will be enabled if selectionType is set to ‘ap’. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. Defaults to dual. |
| **bandSteeringEnabled**  boolean | Steers client to most open band. Can be either true or false. Defaults to true.  **Choices:**   - `false` - `true` |
| **bandSelectionType**  string | Band selection can be set to either ‘ssid’ or ‘ap’. This param is required on creation. |
| **clientBalancingEnabled**  boolean | Steers client to best available access point. Can be either true or false. Defaults to true.  **Choices:**   - `false` - `true` |
| **fiveGhzSettings**  dictionary | Settings related to 5Ghz band. |
| **channelWidth**  string | Sets channel width (MHz) for 5Ghz band. Can be one of ‘auto’, ‘20’, ‘40’ or ‘80’. Defaults to auto. |
| **maxPower**  integer | Sets max power (dBm) of 5Ghz band. Can be integer between 2 and 30. Defaults to 30. |
| **minBitrate**  integer | Sets min bitrate (Mbps) of 5Ghz band. Can be one of ‘6’, ‘9’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. Defaults to 12. |
| **minPower**  integer | Sets min power (dBm) of 5Ghz band. Can be integer between 2 and 30. Defaults to 8. |
| **rxsop**  integer | The RX-SOP level controls the sensitivity of the radio. It is strongly recommended to use RX-SOP only after consulting a wireless expert. RX-SOP can be configured in the range of -65 to -95 (dBm). A value of null will reset this to the default. |
| **validAutoChannels**  list / elements=integer | Sets valid auto channels for 5Ghz band. Can be one of ‘36’, ‘40’, ‘44’, ‘48’, ‘52’, ‘56’, ‘60’, ‘64’, ‘100’, ‘104’, ‘108’, ‘112’, ‘116’, ‘120’, ‘124’, ‘128’, ‘132’, ‘136’, ‘140’, ‘144’, ‘149’, ‘153’, ‘157’, ‘161’ or ‘165’.Defaults to 36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 149, 153, 157, 161, 165. |
| **meraki_action_batch_retry_wait_time**  integer | meraki_action_batch_retry_wait_time (integer), action batch concurrency error retry wait time  **Default:** `60` |
| **meraki_api_key**  string / required | meraki_api_key (string), API key generated in dashboard; can also be set as an environment variable MERAKI_DASHBOARD_API_KEY |
| **meraki_base_url**  string | meraki_base_url (string), preceding all endpoint resources  **Default:** `"https://api.meraki.com/api/v1"` |
| **meraki_be_geo_id**  string | meraki_be_geo_id (string), optional partner identifier for API usage tracking; can also be set as an environment variable BE_GEO_ID  **Default:** `""` |
| **meraki_caller**  string | meraki_caller (string), optional identifier for API usage tracking; can also be set as an environment variable MERAKI_PYTHON_SDK_CALLER  **Default:** `""` |
| **meraki_certificate_path**  string | meraki_certificate_path (string), path for TLS/SSL certificate verification if behind local proxy  **Default:** `""` |
| **meraki_inherit_logging_config**  boolean | meraki_inherit_logging_config (boolean), Inherits your own logger instance  **Choices:**   - `false` ← (default) - `true` |
| **meraki_log_file_prefix**  string | meraki_log_file_prefix (string), log file name appended with date and timestamp  **Default:** `"meraki_api_"` |
| **meraki_log_path**  string | log_path (string), path to output log; by default, working directory of script if not specified  **Default:** `""` |
| **meraki_maximum_retries**  integer | meraki_maximum_retries (integer), retry up to this many times when encountering 429s or other server-side errors  **Default:** `2` |
| **meraki_nginx_429_retry_wait_time**  integer | meraki_nginx_429_retry_wait_time (integer), Nginx 429 retry wait time  **Default:** `60` |
| **meraki_output_log**  boolean | meraki_output_log (boolean), create an output log file?  **Choices:**   - `false` - `true` ← (default) |
| **meraki_print_console**  boolean | meraki_print_console (boolean), print logging output to console?  **Choices:**   - `false` - `true` ← (default) |
| **meraki_requests_proxy**  string | meraki_requests_proxy (string), proxy server and port, if needed, for HTTPS  **Default:** `""` |
| **meraki_retry_4xx_error**  boolean | meraki_retry_4xx_error (boolean), retry if encountering other 4XX error (besides 429)?  **Choices:**   - `false` ← (default) - `true` |
| **meraki_retry_4xx_error_wait_time**  integer | meraki_retry_4xx_error_wait_time (integer), other 4XX error retry wait time  **Default:** `60` |
| **meraki_simulate**  boolean | meraki_simulate (boolean), simulate POST/PUT/DELETE calls to prevent changes?  **Choices:**   - `false` ← (default) - `true` |
| **meraki_single_request_timeout**  integer | meraki_single_request_timeout (integer), maximum number of seconds for each API call  **Default:** `60` |
| **meraki_suppress_logging**  boolean | meraki_suppress_logging (boolean), disable all logging? you’re on your own then!  **Choices:**   - `false` ← (default) - `true` |
| **meraki_use_iterator_for_get_pages**  boolean | meraki_use_iterator_for_get_pages (boolean), list\* methods will return an iterator with each object instead of a complete list with all items  **Choices:**   - `false` ← (default) - `true` |
| **meraki_wait_on_rate_limit**  boolean | meraki_wait_on_rate_limit (boolean), retry if 429 rate limit error encountered?  **Choices:**   - `false` - `true` ← (default) |
| **minBitrateType**  string | Minimum bitrate can be set to either ‘band’ or ‘ssid’. Defaults to band. |
| **name**  string | The name of the new profile. Must be unique. This param is required on creation. |
| **networkId**  string | NetworkId path parameter. Network ID. |
| **perSsidSettings**  dictionary | Per-SSID radio settings by number. |
| **0**  dictionary | Settings for SSID 0. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **1**  dictionary | Settings for SSID 1. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **10**  dictionary | Settings for SSID 10. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **11**  dictionary | Settings for SSID 11. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **12**  dictionary | Settings for SSID 12. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **13**  dictionary | Settings for SSID 13. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **14**  dictionary | Settings for SSID 14. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **2**  dictionary | Settings for SSID 2. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **3**  dictionary | Settings for SSID 3. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **4**  dictionary | Settings for SSID 4. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **5**  dictionary | Settings for SSID 5. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **6**  dictionary | Settings for SSID 6. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **7**  dictionary | Settings for SSID 7. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **8**  dictionary | Settings for SSID 8. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **9**  dictionary | Settings for SSID 9. |
| **bandOperationMode**  string | Choice between ‘dual’, ‘2.4ghz’ or ‘5ghz’. |
| **bandSteeringEnabled**  boolean | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.  **Choices:**   - `false` - `true` |
| **minBitrate**  float | Sets min bitrate (Mbps) of this SSID. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. |
| **rfProfileId**  string | RfProfileId path parameter. Rf profile ID. |
| **sixGhzSettings**  dictionary | Settings related to 6Ghz band. |
| **channelWidth**  string | Sets channel width (MHz) for 6Ghz band. Can be one of ‘0’, ‘20’, ‘40’, ‘80’ or ‘160’. Defaults to 0. |
| **maxPower**  integer | Sets max power (dBm) of 6Ghz band. Can be integer between 2 and 30. Defaults to 30. |
| **minBitrate**  integer | Sets min bitrate (Mbps) of 6Ghz band. Can be one of ‘6’, ‘9’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. Defaults to 12. |
| **minPower**  integer | Sets min power (dBm) of 6Ghz band. Can be integer between 2 and 30. Defaults to 8. |
| **rxsop**  integer | The RX-SOP level controls the sensitivity of the radio. It is strongly recommended to use RX-SOP only after consulting a wireless expert. RX-SOP can be configured in the range of -65 to -95 (dBm). A value of null will reset this to the default. |
| **validAutoChannels**  list / elements=integer | Sets valid auto channels for 6Ghz band. Can be one of ‘1’, ‘5’, ‘9’, ‘13’, ‘17’, ‘21’, ‘25’, ‘29’, ‘33’, ‘37’, ‘41’, ‘45’, ‘49’, ‘53’, ‘57’, ‘61’, ‘65’, ‘69’, ‘73’, ‘77’, ‘81’, ‘85’, ‘89’, ‘93’, ‘97’, ‘101’, ‘105’, ‘109’, ‘113’, ‘117’, ‘121’, ‘125’, ‘129’, ‘133’, ‘137’, ‘141’, ‘145’, ‘149’, ‘153’, ‘157’, ‘161’, ‘165’, ‘169’, ‘173’, ‘177’, ‘181’, ‘185’, ‘189’, ‘193’, ‘197’, ‘201’, ‘205’, ‘209’, ‘213’, ‘217’, ‘221’, ‘225’, ‘229’ or ‘233’.Defaults to 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101, 105, 109, 113, 117, 121, 125, 129, 133, 137, 141, 145, 149, 153, 157, 161, 165, 169, 173, 177, 181, 185, 189, 193, 197, 201, 205, 209, 213, 217, 221, 225, 229, 233. |
| **transmission**  dictionary | Settings related to radio transmission. |
| **enabled**  boolean | Toggle for radio transmission. When false, radios will not transmit at all.  **Choices:**   - `false` - `true` |
| **twoFourGhzSettings**  dictionary | Settings related to 2.4Ghz band. |
| **axEnabled**  boolean | Determines whether ax radio on 2.4Ghz band is on or off. Can be either true or false. If false, we highly recommend disabling band steering. Defaults to true.  **Choices:**   - `false` - `true` |
| **maxPower**  integer | Sets max power (dBm) of 2.4Ghz band. Can be integer between 2 and 30. Defaults to 30. |
| **minBitrate**  float | Sets min bitrate (Mbps) of 2.4Ghz band. Can be one of ‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’. Defaults to 11. |
| **minPower**  integer | Sets min power (dBm) of 2.4Ghz band. Can be integer between 2 and 30. Defaults to 5. |
| **rxsop**  integer | The RX-SOP level controls the sensitivity of the radio. It is strongly recommended to use RX-SOP only after consulting a wireless expert. RX-SOP can be configured in the range of -65 to -95 (dBm). A value of null will reset this to the default. |
| **validAutoChannels**  list / elements=integer | Sets valid auto channels for 2.4Ghz band. Can be one of ‘1’, ‘6’ or ‘11’. Defaults to 1, 6, 11. |

## [Notes](networks_wireless_rf_profiles_module.md#id4)

> **Note:**
>
> - SDK Method used are wireless.Wireless.create_network_wireless_rf_profile, wireless.Wireless.delete_network_wireless_rf_profile, wireless.Wireless.update_network_wireless_rf_profile,
> - Paths used are post /networks/{networkId}/wireless/rfProfiles, delete /networks/{networkId}/wireless/rfProfiles/{rfProfileId}, put /networks/{networkId}/wireless/rfProfiles/{rfProfileId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_wireless_rf_profiles_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for wireless createNetworkWirelessRfProfile](https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-rf-profile)
> :   Complete reference of the createNetworkWirelessRfProfile API.
>
> [Cisco Meraki documentation for wireless deleteNetworkWirelessRfProfile](https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-rf-profile)
> :   Complete reference of the deleteNetworkWirelessRfProfile API.
>
> [Cisco Meraki documentation for wireless updateNetworkWirelessRfProfile](https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-rf-profile)
> :   Complete reference of the updateNetworkWirelessRfProfile API.

## [Examples](networks_wireless_rf_profiles_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.networks_wireless_rf_profiles:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: present
    apBandSettings:
      bandOperationMode: dual
      bandSteeringEnabled: true
    bandSelectionType: ap
    clientBalancingEnabled: true
    fiveGhzSettings:
      channelWidth: auto
      maxPower: 30
      minBitrate: 12
      minPower: 8
      rxsop: -95
      validAutoChannels:
      - 36
      - 40
      - 44
      - 48
      - 52
      - 56
      - 60
      - 64
      - 100
      - 104
      - 108
      - 112
      - 116
      - 120
      - 124
      - 128
      - 132
      - 136
      - 140
      - 144
      - 149
      - 153
      - 157
      - 161
      - 165
    minBitrateType: band
    name: Main Office
    networkId: string
    perSsidSettings:
      '0':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '1':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '10':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '11':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '12':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '13':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '14':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '2':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '3':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '4':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '5':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '6':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '7':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '8':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '9':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
    sixGhzSettings:
      channelWidth: auto
      maxPower: 30
      minBitrate: 12
      minPower: 8
      rxsop: -95
      validAutoChannels:
      - 1
      - 5
      - 9
      - 13
      - 17
      - 21
      - 25
      - 29
      - 33
      - 37
      - 41
      - 45
      - 49
      - 53
      - 57
      - 61
      - 65
      - 69
      - 73
      - 77
      - 81
      - 85
      - 89
      - 93
      - 97
      - 101
      - 105
      - 109
      - 113
      - 117
      - 121
      - 125
      - 129
      - 133
      - 137
      - 141
      - 145
      - 149
      - 153
      - 157
      - 161
      - 165
      - 169
      - 173
      - 177
      - 181
      - 185
      - 189
      - 193
      - 197
      - 201
      - 205
      - 209
      - 213
      - 217
      - 221
      - 225
      - 229
      - 233
    transmission:
      enabled: true
    twoFourGhzSettings:
      axEnabled: true
      maxPower: 30
      minBitrate: 11
      minPower: 5
      rxsop: -95
      validAutoChannels:
      - 1
      - 6
      - 11

- name: Update by id
  cisco.meraki.networks_wireless_rf_profiles:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: present
    apBandSettings:
      bandOperationMode: dual
      bandSteeringEnabled: true
    bandSelectionType: ap
    clientBalancingEnabled: true
    fiveGhzSettings:
      channelWidth: auto
      maxPower: 30
      minBitrate: 12
      minPower: 8
      rxsop: -95
      validAutoChannels:
      - 36
      - 40
      - 44
      - 48
      - 52
      - 56
      - 60
      - 64
      - 100
      - 104
      - 108
      - 112
      - 116
      - 120
      - 124
      - 128
      - 132
      - 136
      - 140
      - 144
      - 149
      - 153
      - 157
      - 161
      - 165
    minBitrateType: band
    name: '1234'
    networkId: string
    perSsidSettings:
      '0':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '1':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '10':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '11':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '12':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '13':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '14':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '2':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '3':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '4':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '5':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '6':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '7':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '8':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
      '9':
        bandOperationMode: dual
        bandSteeringEnabled: true
        minBitrate: 11
    rfProfileId: string
    sixGhzSettings:
      channelWidth: auto
      maxPower: 30
      minBitrate: 12
      minPower: 8
      rxsop: -95
      validAutoChannels:
      - 1
      - 5
      - 9
      - 13
      - 17
      - 21
      - 25
      - 29
      - 33
      - 37
      - 41
      - 45
      - 49
      - 53
      - 57
      - 61
      - 65
      - 69
      - 73
      - 77
      - 81
      - 85
      - 89
      - 93
      - 97
      - 101
      - 105
      - 109
      - 113
      - 117
      - 121
      - 125
      - 129
      - 133
      - 137
      - 141
      - 145
      - 149
      - 153
      - 157
      - 161
      - 165
      - 169
      - 173
      - 177
      - 181
      - 185
      - 189
      - 193
      - 197
      - 201
      - 205
      - 209
      - 213
      - 217
      - 221
      - 225
      - 229
      - 233
    transmission:
      enabled: true
    twoFourGhzSettings:
      axEnabled: true
      maxPower: 30
      minBitrate: 11
      minPower: 5
      rxsop: -95
      validAutoChannels:
      - 1
      - 6
      - 11

- name: Delete by id
  cisco.meraki.networks_wireless_rf_profiles:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: absent
    networkId: string
    rfProfileId: string
```

## [Return Values](networks_wireless_rf_profiles_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{"apBandSettings": {"bandOperationMode": "string", "bandSteeringEnabled": true}, "bandSelectionType": "string", "clientBalancingEnabled": true, "fiveGhzSettings": {"channelWidth": "string", "maxPower": 0, "minBitrate": 0, "minPower": 0, "rxsop": 0, "validAutoChannels": [0]}, "id": "string", "minBitrateType": "string", "name": "string", "networkId": "string", "perSsidSettings": {"0": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "1": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "10": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "11": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "12": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "13": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "14": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "2": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "3": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "4": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "5": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "6": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "7": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "8": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}, "9": {"bandOperationMode": "string", "bandSteeringEnabled": true, "minBitrate": 0, "name": "string"}}, "transmission": {"enabled": true}, "twoFourGhzSettings": {"axEnabled": true, "maxPower": 0, "minBitrate": 0, "minPower": 0, "rxsop": 0, "validAutoChannels": [0]}}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)

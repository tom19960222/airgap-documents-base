---
collection: ansible
version: "8"
title: "cisco.meraki.networks_sensor_alerts_profiles module – Resource module for networks _sensor _alerts _profiles"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_sensor_alerts_profiles_module.html
fetched_at: 2026-07-28T01:34:20+00:00
---
# cisco.meraki.networks_sensor_alerts_profiles module – Resource module for networks _sensor _alerts _profiles

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
> see [Requirements](networks_sensor_alerts_profiles_module.md#ansible-collections-cisco-meraki-networks-sensor-alerts-profiles-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_sensor_alerts_profiles`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_sensor_alerts_profiles_module.md#synopsis)
- [Requirements](networks_sensor_alerts_profiles_module.md#requirements)
- [Parameters](networks_sensor_alerts_profiles_module.md#parameters)
- [Notes](networks_sensor_alerts_profiles_module.md#notes)
- [See Also](networks_sensor_alerts_profiles_module.md#see-also)
- [Examples](networks_sensor_alerts_profiles_module.md#examples)
- [Return Values](networks_sensor_alerts_profiles_module.md#return-values)

## [Synopsis](networks_sensor_alerts_profiles_module.md#id1)

- Manage operations create, update and delete of the resource networks _sensor _alerts _profiles.
- Creates a sensor alert profile for a network.
- Deletes a sensor alert profile from a network.
- Updates a sensor alert profile for a network.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_sensor_alerts_profiles_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_sensor_alerts_profiles_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **conditions**  list / elements=dictionary | List of conditions that will cause the profile to send an alert. |
| **direction**  string | If ‘above’, an alert will be sent when a sensor reads above the threshold. If ‘below’, an alert will be sent when a sensor reads below the threshold. Only applicable for temperature and humidity thresholds. |
| **duration**  integer | Length of time in seconds that the triggering state must persist before an alert is sent. Available options are 0 seconds, 1 minute, 2 minutes, 3 minutes, 4 minutes, 5 minutes, 10 minutes, 15 minutes, 30 minutes, and 1 hour. Default is 0. |
| **metric**  string | The type of sensor metric that will be monitored for changes. Available metrics are door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water. |
| **threshold**  dictionary | Threshold for sensor readings that will cause an alert to be sent. This object should contain a single property key matching the condition’s ‘metric’ value. |
| **door**  dictionary | Door open threshold. ‘open’ must be provided and set to true. |
| **open**  boolean | Alerting threshold for a door open event. Must be set to true.  **Choices:**   - `false` - `true` |
| **humidity**  dictionary | Humidity threshold. One of ‘relativePercentage’ or ‘quality’ must be provided. |
| **quality**  string | Alerting threshold as a qualitative humidity level. |
| **relativePercentage**  integer | Alerting threshold in %RH. |
| **indoorAirQuality**  dictionary | Indoor air quality score threshold. One of ‘score’ or ‘quality’ must be provided. |
| **quality**  string | Alerting threshold as a qualitative indoor air quality level. |
| **score**  integer | Alerting threshold as indoor air quality score. |
| **noise**  dictionary | Noise threshold. ‘ambient’ must be provided. |
| **ambient**  dictionary | Ambient noise threshold. One of ‘level’ or ‘quality’ must be provided. |
| **level**  integer | Alerting threshold as adjusted decibels. |
| **quality**  string | Alerting threshold as a qualitative ambient noise level. |
| **pm25**  dictionary | PM2.5 concentration threshold. One of ‘concentration’ or ‘quality’ must be provided. |
| **concentration**  integer | Alerting threshold as PM2.5 parts per million. |
| **quality**  string | Alerting threshold as a qualitative PM2.5 level. |
| **temperature**  dictionary | Temperature threshold. One of ‘celsius’, ‘fahrenheit’, or ‘quality’ must be provided. |
| **celsius**  float | Alerting threshold in degrees Celsius. |
| **fahrenheit**  float | Alerting threshold in degrees Fahrenheit. |
| **quality**  string | Alerting threshold as a qualitative temperature level. |
| **tvoc**  dictionary | TVOC concentration threshold. One of ‘concentration’ or ‘quality’ must be provided. |
| **concentration**  integer | Alerting threshold as TVOC micrograms per cubic meter. |
| **quality**  string | Alerting threshold as a qualitative TVOC level. |
| **water**  dictionary | Water detection threshold. ‘present’ must be provided and set to true. |
| **present**  boolean | Alerting threshold for a water detection event. Must be set to true.  **Choices:**   - `false` - `true` |
| **id**  string | Id path parameter. |
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
| **name**  string | Name of the sensor alert profile. |
| **networkId**  string | NetworkId path parameter. Network ID. |
| **recipients**  dictionary | List of recipients that will recieve the alert. |
| **emails**  list / elements=string | A list of emails that will receive information about the alert. |
| **httpServerIds**  list / elements=string | A list of webhook endpoint IDs that will receive information about the alert. |
| **smsNumbers**  list / elements=string | A list of SMS numbers that will receive information about the alert. |
| **schedule**  dictionary | The sensor schedule to use with the alert profile. |
| **id**  string | ID of the sensor schedule to use with the alert profile. If not defined, the alert profile will be active at all times. |
| **serials**  list / elements=string | List of device serials assigned to this sensor alert profile. |

## [Notes](networks_sensor_alerts_profiles_module.md#id4)

> **Note:**
>
> - SDK Method used are sensor.Sensor.create_network_sensor_alerts_profile, sensor.Sensor.delete_network_sensor_alerts_profile, sensor.Sensor.update_network_sensor_alerts_profile,
> - Paths used are post /networks/{networkId}/sensor/alerts/profiles, delete /networks/{networkId}/sensor/alerts/profiles/{id}, put /networks/{networkId}/sensor/alerts/profiles/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_sensor_alerts_profiles_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for sensor createNetworkSensorAlertsProfile](https://developer.cisco.com/meraki/api-v1/#!create-network-sensor-alerts-profile)
> :   Complete reference of the createNetworkSensorAlertsProfile API.
>
> [Cisco Meraki documentation for sensor deleteNetworkSensorAlertsProfile](https://developer.cisco.com/meraki/api-v1/#!delete-network-sensor-alerts-profile)
> :   Complete reference of the deleteNetworkSensorAlertsProfile API.
>
> [Cisco Meraki documentation for sensor updateNetworkSensorAlertsProfile](https://developer.cisco.com/meraki/api-v1/#!update-network-sensor-alerts-profile)
> :   Complete reference of the updateNetworkSensorAlertsProfile API.

## [Examples](networks_sensor_alerts_profiles_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.networks_sensor_alerts_profiles:
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
    conditions:
    - direction: above
      duration: 60
      metric: temperature
      threshold:
        door:
          open: true
        humidity:
          quality: inadequate
          relativePercentage: 65
        indoorAirQuality:
          quality: fair
          score: 80
        noise:
          ambient:
            level: 120
            quality: poor
        pm25:
          concentration: 90
          quality: fair
        temperature:
          celsius: 20.5
          fahrenheit: 70
          quality: good
        tvoc:
          concentration: 400
          quality: poor
        water:
          present: true
    name: My Sensor Alert Profile
    networkId: string
    recipients:
      emails:
      - miles@meraki.com
      httpServerIds:
      - aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M=
      smsNumbers:
      - '+15555555555'
    schedule:
      id: '5'
    serials:
    - Q234-ABCD-0001
    - Q234-ABCD-0002
    - Q234-ABCD-0003

- name: Update by id
  cisco.meraki.networks_sensor_alerts_profiles:
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
    conditions:
    - direction: above
      duration: 60
      metric: temperature
      threshold:
        door:
          open: true
        humidity:
          quality: inadequate
          relativePercentage: 65
        indoorAirQuality:
          quality: fair
          score: 80
        noise:
          ambient:
            level: 120
            quality: poor
        pm25:
          concentration: 90
          quality: fair
        temperature:
          celsius: 20.5
          fahrenheit: 70
          quality: good
        tvoc:
          concentration: 400
          quality: poor
        water:
          present: true
    id: string
    name: My Sensor Alert Profile
    networkId: string
    recipients:
      emails:
      - miles@meraki.com
      httpServerIds:
      - aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M=
      smsNumbers:
      - '+15555555555'
    schedule:
      id: '5'
    serials:
    - Q234-ABCD-0001
    - Q234-ABCD-0002
    - Q234-ABCD-0003

- name: Delete by id
  cisco.meraki.networks_sensor_alerts_profiles:
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
    id: string
    networkId: string
```

## [Return Values](networks_sensor_alerts_profiles_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{"conditions": [{"direction": "string", "duration": 0, "metric": "string", "threshold": {"door": {"open": true}, "humidity": {"quality": "string", "relativePercentage": 0}, "indoorAirQuality": {"quality": "string", "score": 0}, "noise": {"ambient": {"level": 0, "quality": "string"}}, "pm25": {"concentration": 0, "quality": "string"}, "temperature": {"celsius": 0, "fahrenheit": 0, "quality": "string"}, "tvoc": {"concentration": 0, "quality": "string"}, "water": {"present": true}}}], "name": "string", "profileId": "string", "recipients": {"emails": ["string"], "httpServerIds": ["string"], "smsNumbers": ["string"]}, "schedule": {"id": "string", "name": "string"}, "serials": ["string"]}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)

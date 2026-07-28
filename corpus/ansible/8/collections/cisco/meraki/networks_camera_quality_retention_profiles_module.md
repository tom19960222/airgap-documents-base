---
collection: ansible
version: "8"
title: "cisco.meraki.networks_camera_quality_retention_profiles module – Resource module for networks _camera _qualityretentionprofiles"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_camera_quality_retention_profiles_module.html
fetched_at: 2026-07-28T01:33:38+00:00
---
# cisco.meraki.networks_camera_quality_retention_profiles module – Resource module for networks _camera _qualityretentionprofiles

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
> see [Requirements](networks_camera_quality_retention_profiles_module.md#ansible-collections-cisco-meraki-networks-camera-quality-retention-profiles-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_camera_quality_retention_profiles`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_camera_quality_retention_profiles_module.md#synopsis)
- [Requirements](networks_camera_quality_retention_profiles_module.md#requirements)
- [Parameters](networks_camera_quality_retention_profiles_module.md#parameters)
- [Notes](networks_camera_quality_retention_profiles_module.md#notes)
- [See Also](networks_camera_quality_retention_profiles_module.md#see-also)
- [Examples](networks_camera_quality_retention_profiles_module.md#examples)
- [Return Values](networks_camera_quality_retention_profiles_module.md#return-values)

## [Synopsis](networks_camera_quality_retention_profiles_module.md#id1)

- Manage operations create, update and delete of the resource networks _camera _qualityretentionprofiles.
- Creates new quality retention profile for this network.
- Delete an existing quality retention profile for this network.
- Update an existing quality retention profile for this network.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_camera_quality_retention_profiles_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_camera_quality_retention_profiles_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **audioRecordingEnabled**  boolean | Whether or not to record audio. Can be either true or false. Defaults to false.  **Choices:**   - `false` - `true` |
| **cloudArchiveEnabled**  boolean | Create redundant video backup using Cloud Archive. Can be either true or false. Defaults to false.  **Choices:**   - `false` - `true` |
| **maxRetentionDays**  integer | The maximum number of days for which the data will be stored, or ‘null’ to keep data until storage space runs out. If the former, it can be one of 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 30, 60, 90 days. |
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
| **motionBasedRetentionEnabled**  boolean | Deletes footage older than 3 days in which no motion was detected. Can be either true or false. Defaults to false. This setting does not apply to MV2 cameras.  **Choices:**   - `false` - `true` |
| **motionDetectorVersion**  integer | The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2. |
| **name**  string | The name of the new profile. Must be unique. This parameter is required. |
| **networkId**  string | NetworkId path parameter. Network ID. |
| **qualityRetentionProfileId**  string | QualityRetentionProfileId path parameter. Quality retention profile ID. |
| **restrictedBandwidthModeEnabled**  boolean | Disable features that require additional bandwidth such as Motion Recap. Can be either true or false. Defaults to false. This setting does not apply to MV2 cameras.  **Choices:**   - `false` - `true` |
| **scheduleId**  string | Schedule for which this camera will record video, or ‘null’ to always record. |
| **videoSettings**  dictionary | Video quality and resolution settings for all the camera models. |
| **MV12/MV22/MV72**  dictionary | Quality and resolution for MV12/MV22/MV72 camera models. |
| **quality**  string | Quality of the camera. Can be one of ‘Standard’, ‘Enhanced’ or ‘High’. |
| **resolution**  string | Resolution of the camera. Can be one of ‘1280x720’ or ‘1920x1080’. |
| **MV12WE**  dictionary | Quality and resolution for MV12WE camera models. |
| **quality**  string | Quality of the camera. Can be one of ‘Standard’, ‘Enhanced’ or ‘High’. |
| **resolution**  string | Resolution of the camera. Can be one of ‘1280x720’ or ‘1920x1080’. |
| **MV13**  dictionary | Quality and resolution for MV13 camera models. |
| **quality**  string | Quality of the camera. Can be one of ‘Standard’, ‘Enhanced’ or ‘High’. |
| **resolution**  string | Resolution of the camera. Can be one of ‘1080x1080’ or ‘2688x1512’. |
| **MV21/MV71**  dictionary | Quality and resolution for MV21/MV71 camera models. |
| **quality**  string | Quality of the camera. Can be one of ‘Standard’, ‘Enhanced’ or ‘High’. |
| **resolution**  string | Resolution of the camera. Can be one of ‘1280x720’. |
| **MV22X/MV72X**  dictionary | Quality and resolution for MV22X/MV72X camera models. |
| **quality**  string | Quality of the camera. Can be one of ‘Standard’, ‘Enhanced’ or ‘High’. |
| **resolution**  string | Resolution of the camera. Can be one of ‘1280x720’, ‘1920x1080’ or ‘2688x1512’. |
| **MV32**  dictionary | Quality and resolution for MV32 camera models. |
| **quality**  string | Quality of the camera. Can be one of ‘Standard’, ‘Enhanced’ or ‘High’. |
| **resolution**  string | Resolution of the camera. Can be one of ‘1080x1080’ or ‘2058x2058’. |
| **MV33**  dictionary | Quality and resolution for MV33 camera models. |
| **quality**  string | Quality of the camera. Can be one of ‘Standard’, ‘Enhanced’ or ‘High’. |
| **resolution**  string | Resolution of the camera. Can be one of ‘1080x1080’ or ‘2112x2112’. |
| **MV52**  dictionary | Quality and resolution for MV52 camera models. |
| **quality**  string | Quality of the camera. Can be one of ‘Standard’, ‘Enhanced’ or ‘High’. |
| **resolution**  string | Resolution of the camera. Can be one of ‘1280x720’, ‘1920x1080’, ‘2688x1512’ or ‘3840x2160’. |
| **MV63**  dictionary | Quality and resolution for MV63 camera models. |
| **quality**  string | Quality of the camera. Can be one of ‘Standard’, ‘Enhanced’ or ‘High’. |
| **resolution**  string | Resolution of the camera. Can be one of ‘1920x1080’ or ‘2688x1512’. |
| **MV63X**  dictionary | Quality and resolution for MV63X camera models. |
| **quality**  string | Quality of the camera. Can be one of ‘Standard’, ‘Enhanced’ or ‘High’. |
| **resolution**  string | Resolution of the camera. Can be one of ‘1920x1080’, ‘2688x1512’ or ‘3840x2160’. |
| **MV93**  dictionary | Quality and resolution for MV93 camera models. |
| **quality**  string | Quality of the camera. Can be one of ‘Standard’, ‘Enhanced’ or ‘High’. |
| **resolution**  string | Resolution of the camera. Can be one of ‘1080x1080’ or ‘2112x2112’. |
| **MV93X**  dictionary | Quality and resolution for MV93X camera models. |
| **quality**  string | Quality of the camera. Can be one of ‘Standard’, ‘Enhanced’ or ‘High’. |
| **resolution**  string | Resolution of the camera. Can be one of ‘1080x1080’, ‘2112x2112’ or ‘2880x2880’. |

## [Notes](networks_camera_quality_retention_profiles_module.md#id4)

> **Note:**
>
> - SDK Method used are camera.Camera.create_network_camera_quality_retention_profile, camera.Camera.delete_network_camera_quality_retention_profile, camera.Camera.update_network_camera_quality_retention_profile,
> - Paths used are post /networks/{networkId}/camera/qualityRetentionProfiles, delete /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}, put /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_camera_quality_retention_profiles_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for camera createNetworkCameraQualityRetentionProfile](https://developer.cisco.com/meraki/api-v1/#!create-network-camera-quality-retention-profile)
> :   Complete reference of the createNetworkCameraQualityRetentionProfile API.
>
> [Cisco Meraki documentation for camera deleteNetworkCameraQualityRetentionProfile](https://developer.cisco.com/meraki/api-v1/#!delete-network-camera-quality-retention-profile)
> :   Complete reference of the deleteNetworkCameraQualityRetentionProfile API.
>
> [Cisco Meraki documentation for camera updateNetworkCameraQualityRetentionProfile](https://developer.cisco.com/meraki/api-v1/#!update-network-camera-quality-retention-profile)
> :   Complete reference of the updateNetworkCameraQualityRetentionProfile API.

## [Examples](networks_camera_quality_retention_profiles_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.networks_camera_quality_retention_profiles:
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
    name: Sample quality retention profile
    networkId: string

- name: Update by id
  cisco.meraki.networks_camera_quality_retention_profiles:
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
    audioRecordingEnabled: true
    cloudArchiveEnabled: true
    maxRetentionDays: 0
    motionBasedRetentionEnabled: true
    motionDetectorVersion: 0
    name: string
    networkId: string
    qualityRetentionProfileId: string
    restrictedBandwidthModeEnabled: true
    scheduleId: string
    videoSettings:
      MV12/MV22/MV72:
        quality: string
        resolution: string
      MV12WE:
        quality: string
        resolution: string
      MV13:
        quality: string
        resolution: string
      MV21/MV71:
        quality: string
        resolution: string
      MV22X/MV72X:
        quality: string
        resolution: string
      MV32:
        quality: string
        resolution: string
      MV33:
        quality: string
        resolution: string
      MV52:
        quality: string
        resolution: string
      MV63:
        quality: string
        resolution: string
      MV63X:
        quality: string
        resolution: string
      MV93:
        quality: string
        resolution: string
      MV93X:
        quality: string
        resolution: string

- name: Delete by id
  cisco.meraki.networks_camera_quality_retention_profiles:
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
    qualityRetentionProfileId: string
```

## [Return Values](networks_camera_quality_retention_profiles_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)

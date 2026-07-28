---
collection: ansible
version: "8"
title: "cisco.meraki.organizations_config_templates_switch_profiles_ports module – Resource module for organizations _configtemplates _switch _profiles _ports"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/organizations_config_templates_switch_profiles_ports_module.html
fetched_at: 2026-07-28T01:36:39+00:00
---
# cisco.meraki.organizations_config_templates_switch_profiles_ports module – Resource module for organizations _configtemplates _switch _profiles _ports

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
> see [Requirements](organizations_config_templates_switch_profiles_ports_module.md#ansible-collections-cisco-meraki-organizations-config-templates-switch-profiles-ports-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.organizations_config_templates_switch_profiles_ports`.

New in cisco.meraki 2.16.0

- [Synopsis](organizations_config_templates_switch_profiles_ports_module.md#synopsis)
- [Requirements](organizations_config_templates_switch_profiles_ports_module.md#requirements)
- [Parameters](organizations_config_templates_switch_profiles_ports_module.md#parameters)
- [Notes](organizations_config_templates_switch_profiles_ports_module.md#notes)
- [See Also](organizations_config_templates_switch_profiles_ports_module.md#see-also)
- [Examples](organizations_config_templates_switch_profiles_ports_module.md#examples)
- [Return Values](organizations_config_templates_switch_profiles_ports_module.md#return-values)

## [Synopsis](organizations_config_templates_switch_profiles_ports_module.md#id1)

- Manage operation update of the resource organizations _configtemplates _switch _profiles _ports.
- Update a switch profile port.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](organizations_config_templates_switch_profiles_ports_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](organizations_config_templates_switch_profiles_ports_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accessPolicyNumber**  integer | The number of a custom access policy to configure on the switch profile port. Only applicable when ‘accessPolicyType’ is ‘Custom access policy’. |
| **accessPolicyType**  string | The type of the access policy of the switch profile port. Only applicable to access ports. Can be one of ‘Open’, ‘Custom access policy’, ‘MAC allow list’ or ‘Sticky MAC allow list’. |
| **allowedVlans**  string | The VLANs allowed on the switch profile port. Only applicable to trunk ports. |
| **configTemplateId**  string | ConfigTemplateId path parameter. Config template ID. |
| **daiTrusted**  boolean | If true, ARP packets for this port will be considered trusted, and Dynamic ARP Inspection will allow the traffic.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | The status of the switch profile port.  **Choices:**   - `false` - `true` |
| **flexibleStackingEnabled**  boolean | For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.  **Choices:**   - `false` - `true` |
| **isolationEnabled**  boolean | The isolation status of the switch profile port.  **Choices:**   - `false` - `true` |
| **linkNegotiation**  string | The link speed for the switch profile port. |
| **macAllowList**  list / elements=string | Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when ‘accessPolicyType’ is ‘MAC allow list’. |
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
| **name**  string | The name of the switch profile port. |
| **organizationId**  string | OrganizationId path parameter. Organization ID. |
| **poeEnabled**  boolean | The PoE status of the switch profile port.  **Choices:**   - `false` - `true` |
| **portId**  string | PortId path parameter. Port ID. |
| **portScheduleId**  string | The ID of the port schedule. A value of null will clear the port schedule. |
| **profile**  dictionary | Profile attributes. |
| **enabled**  boolean | When enabled, override this port’s configuration with a port profile.  **Choices:**   - `false` - `true` |
| **id**  string | When enabled, the ID of the port profile used to override the port’s configuration. |
| **iname**  string | When enabled, the IName of the profile. |
| **profileId**  string | ProfileId path parameter. Profile ID. |
| **rstpEnabled**  boolean | The rapid spanning tree protocol status.  **Choices:**   - `false` - `true` |
| **stickyMacAllowList**  list / elements=string | The initial list of MAC addresses for sticky Mac allow list. Only applicable when ‘accessPolicyType’ is ‘Sticky MAC allow list’. |
| **stickyMacAllowListLimit**  integer | The maximum number of MAC addresses for sticky MAC allow list. Only applicable when ‘accessPolicyType’ is ‘Sticky MAC allow list’. |
| **stormControlEnabled**  boolean | The storm control status of the switch profile port.  **Choices:**   - `false` - `true` |
| **stpGuard**  string | The state of the STP guard (‘disabled’, ‘root guard’, ‘bpdu guard’ or ‘loop guard’). |
| **tags**  list / elements=string | The list of tags of the switch profile port. |
| **type**  string | The type of the switch profile port (‘trunk’ or ‘access’). |
| **udld**  string | The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only. |
| **vlan**  integer | The VLAN of the switch profile port. A null value will clear the value set for trunk ports. |
| **voiceVlan**  integer | The voice VLAN of the switch profile port. Only applicable to access ports. |

## [Notes](organizations_config_templates_switch_profiles_ports_module.md#id4)

> **Note:**
>
> - SDK Method used are switch.Switch.update_organization_config_template_switch_profile_port,
> - Paths used are put /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](organizations_config_templates_switch_profiles_ports_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for switch updateOrganizationConfigTemplateSwitchProfilePort](https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template-switch-profile-port)
> :   Complete reference of the updateOrganizationConfigTemplateSwitchProfilePort API.

## [Examples](organizations_config_templates_switch_profiles_ports_module.md#id6)

```yaml+jinja
- name: Update by id
  cisco.meraki.organizations_config_templates_switch_profiles_ports:
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
    accessPolicyNumber: 2
    accessPolicyType: Sticky MAC allow list
    allowedVlans: 1,3,5-10
    configTemplateId: string
    daiTrusted: false
    enabled: true
    flexibleStackingEnabled: true
    isolationEnabled: false
    linkNegotiation: Auto negotiate
    macAllowList:
    - 34:56:fe:ce:8e:b0
    - 34:56:fe:ce:8e:b1
    name: My switch port
    organizationId: string
    poeEnabled: true
    portId: string
    portScheduleId: '1234'
    profile:
      enabled: false
      id: '1284392014819'
      iname: iname
    profileId: string
    rstpEnabled: true
    stickyMacAllowList:
    - 34:56:fe:ce:8e:b0
    - 34:56:fe:ce:8e:b1
    stickyMacAllowListLimit: 5
    stormControlEnabled: true
    stpGuard: disabled
    tags:
    - tag1
    - tag2
    type: access
    udld: Alert only
    vlan: 10
    voiceVlan: 20
```

## [Return Values](organizations_config_templates_switch_profiles_ports_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{"accessPolicyNumber": 0, "accessPolicyType": "string", "allowedVlans": "string", "daiTrusted": true, "enabled": true, "flexibleStackingEnabled": true, "isolationEnabled": true, "linkNegotiation": "string", "linkNegotiationCapabilities": ["string"], "macAllowList": ["string"], "name": "string", "poeEnabled": true, "portId": "string", "portScheduleId": "string", "profile": {"enabled": true, "id": "string", "iname": "string"}, "rstpEnabled": true, "stickyMacAllowList": ["string"], "stickyMacAllowListLimit": 0, "stormControlEnabled": true, "stpGuard": "string", "tags": ["string"], "type": "string", "udld": "string", "vlan": 0, "voiceVlan": 0}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)

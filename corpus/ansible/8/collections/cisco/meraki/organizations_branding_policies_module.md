---
collection: ansible
version: "8"
title: "cisco.meraki.organizations_branding_policies module – Resource module for organizations _brandingpolicies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/organizations_branding_policies_module.html
fetched_at: 2026-07-28T01:36:25+00:00
---
# cisco.meraki.organizations_branding_policies module – Resource module for organizations _brandingpolicies

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
> see [Requirements](organizations_branding_policies_module.md#ansible-collections-cisco-meraki-organizations-branding-policies-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.organizations_branding_policies`.

New in cisco.meraki 2.16.0

- [Synopsis](organizations_branding_policies_module.md#synopsis)
- [Requirements](organizations_branding_policies_module.md#requirements)
- [Parameters](organizations_branding_policies_module.md#parameters)
- [Notes](organizations_branding_policies_module.md#notes)
- [See Also](organizations_branding_policies_module.md#see-also)
- [Examples](organizations_branding_policies_module.md#examples)
- [Return Values](organizations_branding_policies_module.md#return-values)

## [Synopsis](organizations_branding_policies_module.md#id1)

- Manage operations create, update and delete of the resource organizations _brandingpolicies.
- Add a new branding policy to an organization.
- Delete a branding policy.
- Update a branding policy.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](organizations_branding_policies_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](organizations_branding_policies_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **adminSettings**  dictionary | Settings for describing which kinds of admins this policy applies to. |
| **appliesTo**  string | Which kinds of admins this policy applies to. Can be one of ‘All organization admins’, ‘All enterprise admins’, ‘All network admins’, ‘All admins of networks…’, ‘All admins of networks tagged…’, ‘Specific admins…’, ‘All admins’ or ‘All SAML admins’. |
| **values**  list / elements=string | If ‘appliesTo’ is set to one of ‘Specific admins…’, ‘All admins of networks…’ or ‘All admins of networks tagged…’, then you must specify this ‘values’ property to provide the set of entities to apply the branding policy to. For ‘Specific admins…’, specify an array of admin IDs. For ‘All admins of networks…’, specify an array of network IDs and/or configuration template IDs. For ‘All admins of networks tagged…’, specify an array of tag names. |
| **brandingPolicyId**  string | BrandingPolicyId path parameter. Branding policy ID. |
| **customLogo**  dictionary | Properties describing the custom logo attached to the branding policy. |
| **enabled**  boolean | Whether or not there is a custom logo enabled.  **Choices:**   - `false` - `true` |
| **image**  dictionary | Properties for setting the image. |
| **contents**  string | The file contents (a base 64 encoded string) of your new logo. |
| **format**  string | The format of the encoded contents. Supported formats are ‘png’, ‘gif’, and jpg’. |
| **enabled**  boolean | Boolean indicating whether this policy is enabled.  **Choices:**   - `false` - `true` |
| **helpSettings**  dictionary | Settings for describing the modifications to various Help page features. Each property in this object accepts one of ‘default or inherit’ (do not modify functionality), ‘hide’ (remove the section from Dashboard), or ‘show’ (always show the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on Dashboard; see the documentation for each property to see the allowed values. Each property defaults to ‘default or inherit’ when not provided. |
| **apiDocsSubtab**  string | The ‘Help -> API docs’ subtab where a detailed description of the Dashboard API is listed. Can be one of ‘default or inherit’, ‘hide’ or ‘show’. |
| **casesSubtab**  string | The ‘Help -> Cases’ Dashboard subtab on which Cisco Meraki support cases for this organization can be managed. Can be one of ‘default or inherit’, ‘hide’ or ‘show’. |
| **ciscoMerakiProductDocumentation**  string | The ‘Product Manuals’ section of the ‘Help -> Get Help’ subtab. Can be one of ‘default or inherit’, ‘hide’, ‘show’, or a replacement custom HTML string. |
| **communitySubtab**  string | The ‘Help -> Community’ subtab which provides a link to Meraki Community. Can be one of ‘default or inherit’, ‘hide’ or ‘show’. |
| **dataProtectionRequestsSubtab**  string | The ‘Help -> Data protection requests’ Dashboard subtab on which requests to delete, restrict, or export end-user data can be audited. Can be one of ‘default or inherit’, ‘hide’ or ‘show’. |
| **firewallInfoSubtab**  string | The ‘Help -> Firewall info’ subtab where necessary upstream firewall rules for communication to the Cisco Meraki cloud are listed. Can be one of ‘default or inherit’, ‘hide’ or ‘show’. |
| **getHelpSubtab**  string | The ‘Help -> Get Help’ subtab on which Cisco Meraki KB, Product Manuals, and Support/Case Information are displayed. Note that if this subtab is hidden, branding customizations for the KB on ‘Get help’, Cisco Meraki product documentation, and support contact info will not be visible. Can be one of ‘default or inherit’, ‘hide’ or ‘show’. |
| **getHelpSubtabKnowledgeBaseSearch**  string | The KB search box which appears on the Help page. Can be one of ‘default or inherit’, ‘hide’, ‘show’, or a replacement custom HTML string. |
| **hardwareReplacementsSubtab**  string | The ‘Help -> Replacement info’ subtab where important information regarding device replacements is detailed. Can be one of ‘default or inherit’, ‘hide’ or ‘show’. |
| **helpTab**  string | The Help tab, under which all support information resides. If this tab is hidden, no other ‘Help’ branding customizations will be visible. Can be one of ‘default or inherit’, ‘hide’ or ‘show’. |
| **helpWidget**  string | The ‘Help Widget’ is a support widget which provides access to live chat, documentation links, Sales contact info, and other contact avenues to reach Meraki Support. Can be one of ‘default or inherit’, ‘hide’ or ‘show’. |
| **newFeaturesSubtab**  string | The ‘Help -> New features’ subtab where new Dashboard features are detailed. Can be one of ‘default or inherit’, ‘hide’ or ‘show’. |
| **smForums**  string | The ‘SM Forums’ subtab which links to community-based support for Cisco Meraki Systems Manager. Only configurable for organizations that contain Systems Manager networks. Can be one of ‘default or inherit’, ‘hide’ or ‘show’. |
| **supportContactInfo**  string | The ‘Contact Meraki Support’ section of the ‘Help -> Get Help’ subtab. Can be one of ‘default or inherit’, ‘hide’, ‘show’, or a replacement custom HTML string. |
| **universalSearchKnowledgeBaseSearch**  string | The universal search box always visible on Dashboard will, by default, present results from the Meraki KB. This configures whether these Meraki KB results should be returned. Can be one of ‘default or inherit’, ‘hide’ or ‘show’. |
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
| **name**  string | Name of the Dashboard branding policy. |
| **organizationId**  string | OrganizationId path parameter. Organization ID. |

## [Notes](organizations_branding_policies_module.md#id4)

> **Note:**
>
> - SDK Method used are organizations.Organizations.create_organization_branding_policy, organizations.Organizations.delete_organization_branding_policy, organizations.Organizations.update_organization_branding_policy,
> - Paths used are post /organizations/{organizationId}/brandingPolicies, delete /organizations/{organizationId}/brandingPolicies/{brandingPolicyId}, put /organizations/{organizationId}/brandingPolicies/{brandingPolicyId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](organizations_branding_policies_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for organizations createOrganizationBrandingPolicy](https://developer.cisco.com/meraki/api-v1/#!create-organization-branding-policy)
> :   Complete reference of the createOrganizationBrandingPolicy API.
>
> [Cisco Meraki documentation for organizations deleteOrganizationBrandingPolicy](https://developer.cisco.com/meraki/api-v1/#!delete-organization-branding-policy)
> :   Complete reference of the deleteOrganizationBrandingPolicy API.
>
> [Cisco Meraki documentation for organizations updateOrganizationBrandingPolicy](https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policy)
> :   Complete reference of the updateOrganizationBrandingPolicy API.

## [Examples](organizations_branding_policies_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.organizations_branding_policies:
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
    adminSettings:
      appliesTo: All admins of networks...
      values:
      - N_1234
      - L_5678
    customLogo:
      enabled: true
      image:
        contents: Hyperg26C8F4h8CvcoUqpA==
        format: jpg
    enabled: true
    helpSettings:
      apiDocsSubtab: default or inherit
      casesSubtab: hide
      ciscoMerakiProductDocumentation: show
      communitySubtab: show
      dataProtectionRequestsSubtab: default or inherit
      firewallInfoSubtab: hide
      getHelpSubtab: default or inherit
      getHelpSubtabKnowledgeBaseSearch: <h1>Some custom HTML content</h1>
      hardwareReplacementsSubtab: hide
      helpTab: show
      helpWidget: hide
      newFeaturesSubtab: show
      smForums: hide
      supportContactInfo: show
      universalSearchKnowledgeBaseSearch: hide
    name: My Branding Policy
    organizationId: string

- name: Update by id
  cisco.meraki.organizations_branding_policies:
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
    adminSettings:
      appliesTo: All admins of networks...
      values:
      - N_1234
      - L_5678
    brandingPolicyId: string
    customLogo:
      enabled: true
      image:
        contents: Hyperg26C8F4h8CvcoUqpA==
        format: jpg
    enabled: true
    helpSettings:
      apiDocsSubtab: default or inherit
      casesSubtab: hide
      ciscoMerakiProductDocumentation: show
      communitySubtab: show
      dataProtectionRequestsSubtab: default or inherit
      firewallInfoSubtab: hide
      getHelpSubtab: default or inherit
      getHelpSubtabKnowledgeBaseSearch: <h1>Some custom HTML content</h1>
      hardwareReplacementsSubtab: hide
      helpTab: show
      helpWidget: hide
      newFeaturesSubtab: show
      smForums: hide
      supportContactInfo: show
      universalSearchKnowledgeBaseSearch: hide
    name: My Branding Policy
    organizationId: string

- name: Delete by id
  cisco.meraki.organizations_branding_policies:
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
    brandingPolicyId: string
    organizationId: string
```

## [Return Values](organizations_branding_policies_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{"adminSettings": {"appliesTo": "string", "values": ["string"]}, "customLogo": {"enabled": true, "image": {"preview": {"expiresAt": "string", "url": "string"}}}, "enabled": true, "helpSettings": {"apiDocsSubtab": "string", "casesSubtab": "string", "ciscoMerakiProductDocumentation": "string", "communitySubtab": "string", "dataProtectionRequestsSubtab": "string", "firewallInfoSubtab": "string", "getHelpSubtab": "string", "getHelpSubtabKnowledgeBaseSearch": "string", "hardwareReplacementsSubtab": "string", "helpTab": "string", "helpWidget": "string", "newFeaturesSubtab": "string", "smForums": "string", "supportContactInfo": "string", "universalSearchKnowledgeBaseSearch": "string"}, "name": "string"}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)

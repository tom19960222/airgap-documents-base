---
collection: ansible
version: "6"
title: "cisco.dnac.event_subscription_email_info module – Information module for Event Subscription Email"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/event_subscription_email_info_module.html
fetched_at: 2026-07-27T16:52:02+00:00
---
# cisco.dnac.event_subscription_email_info module – Information module for Event Subscription Email

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/cisco/dnac) (version 6.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](event_subscription_email_info_module.md#ansible-collections-cisco-dnac-event-subscription-email-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.event_subscription_email_info`.

New in cisco.dnac 3.1.0

- [Synopsis](event_subscription_email_info_module.md#synopsis)
- [Requirements](event_subscription_email_info_module.md#requirements)
- [Parameters](event_subscription_email_info_module.md#parameters)
- [Notes](event_subscription_email_info_module.md#notes)
- [See Also](event_subscription_email_info_module.md#see-also)
- [Examples](event_subscription_email_info_module.md#examples)
- [Return Values](event_subscription_email_info_module.md#return-values)

## [Synopsis](event_subscription_email_info_module.md#id1)

- Get all Event Subscription Email.
- Gets the list of email Subscriptions’s based on provided query params.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](event_subscription_email_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](event_subscription_email_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **category**  string | Category query parameter. List of email subscriptions related to the respective category. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **domain**  string | Domain query parameter. List of email subscriptions related to the respective domain. |
| **eventIds**  string | EventIds query parameter. List of email subscriptions related to the respective eventIds (Comma separated event ids). |
| **headers**  dictionary | Additional headers. |
| **limit**  integer | Limit query parameter. The number of Subscriptions’s to limit in the resultset whose default value 10. |
| **name**  string | Name query parameter. List of email subscriptions related to the respective name. |
| **offset**  integer | Offset query parameter. The number of Subscriptions’s to offset in the resultset whose default value 0. |
| **order**  string | Order query parameter. |
| **sortBy**  string | SortBy query parameter. SortBy field name. |
| **subDomain**  string | SubDomain query parameter. List of email subscriptions related to the respective sub-domain. |
| **type**  string | Type query parameter. List of email subscriptions related to the respective type. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](event_subscription_email_info_module.md#id4)

> **Note:**
>
> - SDK Method used are event_management.EventManagement.get_email_event_subscriptions,
> - Paths used are get /dna/intent/api/v1/event/subscription/email,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](event_subscription_email_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Event Management GetEmailEventSubscriptions](https://developer.cisco.com/docs/dna-center/#!get-email-event-subscriptions)
> :   Complete reference of the GetEmailEventSubscriptions API.

## [Examples](event_subscription_email_info_module.md#id6)

```yaml+jinja
- name: Get all Event Subscription Email
  cisco.dnac.event_subscription_email_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    eventIds: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
    domain: string
    subDomain: string
    category: string
    type: string
    name: string
  register: result
```

## [Return Values](event_subscription_email_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `"[\n  {\n    \"version\": \"string\",\n    \"subscriptionId\": \"string\",\n    \"name\": \"string\",\n    \"description\": \"string\",\n    \"subscriptionEndpoints\": [\n      {\n        \"instanceId\": \"string\",\n        \"subscriptionDetails\": {\n          \"connectorType\": \"string\",\n          \"instanceId\": \"string\",\n          \"name\": \"string\",\n          \"description\": \"string\",\n          \"fromEmailAddress\": \"string\",\n          \"toEmailAddresses\": [\n            \"string\"\n          ],\n          \"subject\": \"string\"\n        },\n        \"connectorType\": \"string\"\n      }\n    ],\n    \"filter\": {\n      \"eventIds\": [\n        \"string\"\n      ],\n      \"others\": [\n        \"string\"\n      ],\n      \"domainsSubdomains\": [\n        {\n          \"domain\": \"string\",\n          \"subDomains\": [\n            \"string\"\n          ]\n        }\n      ],\n      \"types\": [\n        \"string\"\n      ],\n      \"categories\": [\n        \"string\"\n      ],\n      \"severities\": [\n        \"string\"\n      ],\n      \"sources\": [\n        \"string\"\n      ],\n      \"siteIds\": [\n        \"string\"\n      ]\n    },\n    \"isPrivate\": true,\n    \"tenantId\": \"string\"\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)

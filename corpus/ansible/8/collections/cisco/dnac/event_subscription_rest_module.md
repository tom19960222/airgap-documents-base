---
collection: ansible
version: "8"
title: "cisco.dnac.event_subscription_rest module – Resource module for Event Subscription Rest"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/event_subscription_rest_module.html
fetched_at: 2026-07-28T01:22:36+00:00
---
# cisco.dnac.event_subscription_rest module – Resource module for Event Subscription Rest

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/ui/repo/published/cisco/dnac/) (version 6.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](event_subscription_rest_module.md#ansible-collections-cisco-dnac-event-subscription-rest-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.event_subscription_rest`.

New in cisco.dnac 3.1.0

- [Synopsis](event_subscription_rest_module.md#synopsis)
- [Requirements](event_subscription_rest_module.md#requirements)
- [Parameters](event_subscription_rest_module.md#parameters)
- [Notes](event_subscription_rest_module.md#notes)
- [See Also](event_subscription_rest_module.md#see-also)
- [Examples](event_subscription_rest_module.md#examples)
- [Return Values](event_subscription_rest_module.md#return-values)

## [Synopsis](event_subscription_rest_module.md#id1)

- Manage operations create and update of the resource Event Subscription Rest.
- Create Rest/Webhook Subscription Endpoint for list of registered events.
- Update Rest/Webhook Subscription Endpoint for list of registered events.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](event_subscription_rest_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](event_subscription_rest_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **payload**  list / elements=dictionary | Event Subscription Rest’s payload. |
| **description**  string | Description. |
| **filter**  dictionary | Event Subscription Rest’s filter. |
| **categories**  list / elements=string | Categories. |
| **domainsSubdomains**  list / elements=dictionary | Event Subscription Rest’s domainsSubdomains. |
| **domain**  string | Domain. |
| **subDomains**  list / elements=string | Sub Domains. |
| **eventIds**  list / elements=string | Event Ids (Comma separated event ids). |
| **severities**  list / elements=string | Severities. |
| **siteIds**  list / elements=string | Site Ids. |
| **sources**  list / elements=string | Sources. |
| **types**  list / elements=string | Types. |
| **name**  string | Name. |
| **subscriptionEndpoints**  list / elements=dictionary | Event Subscription Rest’s subscriptionEndpoints. |
| **instanceId**  string | (From Get Rest/Webhook Subscription Details –> pick instanceId). |
| **subscriptionDetails**  dictionary | Event Subscription Rest’s subscriptionDetails. |
| **connectorType**  string | Connector Type (Must be REST). |
| **subscriptionId**  string | Subscription Id (Unique UUID). |
| **version**  string | Version. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](event_subscription_rest_module.md#id4)

> **Note:**
>
> - SDK Method used are event_management.EventManagement.create_rest_webhook_event_subscription, event_management.EventManagement.update_rest_webhook_event_subscription,
> - Paths used are post /dna/intent/api/v1/event/subscription/rest, put /dna/intent/api/v1/event/subscription/rest,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](event_subscription_rest_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Event Management CreateRestWebhookEventSubscription](https://developer.cisco.com/docs/dna-center/#!create-rest-webhook-event-subscription)
> :   Complete reference of the CreateRestWebhookEventSubscription API.
>
> [Cisco DNA Center documentation for Event Management UpdateRestWebhookEventSubscription](https://developer.cisco.com/docs/dna-center/#!update-rest-webhook-event-subscription)
> :   Complete reference of the UpdateRestWebhookEventSubscription API.

## [Examples](event_subscription_rest_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.event_subscription_rest:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - description: string
      filter:
        categories:
        - string
        domainsSubdomains:
        - domain: string
          subDomains:
          - string
        eventIds:
        - string
        severities:
        - string
        siteIds:
        - string
        sources:
        - string
        types:
        - string
      name: string
      subscriptionEndpoints:
      - instanceId: string
        subscriptionDetails:
          connectorType: string
      subscriptionId: string
      version: string

- name: Update all
  cisco.dnac.event_subscription_rest:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - description: string
      filter:
        categories:
        - string
        domainsSubdomains:
        - domain: string
          subDomains:
          - string
        eventIds:
        - string
        severities:
        - string
        siteIds:
        - string
        sources:
        - string
        types:
        - string
      name: string
      subscriptionEndpoints:
      - instanceId: string
        subscriptionDetails:
          connectorType: string
      subscriptionId: string
      version: string
```

## [Return Values](event_subscription_rest_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"statusUri": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)

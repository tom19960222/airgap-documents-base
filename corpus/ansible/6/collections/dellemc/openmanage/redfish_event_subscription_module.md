---
collection: ansible
version: "6"
title: "dellemc.openmanage.redfish_event_subscription module – Manage Redfish Subscriptions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/redfish_event_subscription_module.html
fetched_at: 2026-07-27T17:25:54+00:00
---
# dellemc.openmanage.redfish_event_subscription module – Manage Redfish Subscriptions

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/dellemc/openmanage) (version 5.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](redfish_event_subscription_module.md#ansible-collections-dellemc-openmanage-redfish-event-subscription-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.redfish_event_subscription`.

New in dellemc.openmanage 4.1.0

- [Synopsis](redfish_event_subscription_module.md#synopsis)
- [Requirements](redfish_event_subscription_module.md#requirements)
- [Parameters](redfish_event_subscription_module.md#parameters)
- [Notes](redfish_event_subscription_module.md#notes)
- [Examples](redfish_event_subscription_module.md#examples)
- [Return Values](redfish_event_subscription_module.md#return-values)

## [Synopsis](redfish_event_subscription_module.md#id1)

- This module allows to add or delete Redfish Event subscriptions.

## [Requirements](redfish_event_subscription_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](redfish_event_subscription_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseuri**  string / required | IP address of the target out-of-band controller. For example- <ipaddress>:<port>. |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **destination**  string / required | The HTTPS URI of the destination to send events.  HTTPS is required. |
| **event_format_type**  string | Specifies the format type of the event to be subscribed.  `Event` used to subscribe for Event format type.  `MetricReport` used to subscribe for the metrics report format type.  Choices:   - `"Event"` ← (default) - `"MetricReport"` |
| **event_type**  string | Specifies the event type to be subscribed.  `Alert` used to subscribe for alert.  `MetricReport` used to subscribe for the metrics report.  Choices:   - `"Alert"` ← (default) - `"MetricReport"` |
| **password**  string / required | Password of the target out-of-band controller. |
| **state**  string | `present` adds new event subscription.  `absent` deletes event subscription with the specified *destination*.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | Username of the target out-of-band controller. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](redfish_event_subscription_module.md#id4)

> **Note:**
>
> - *event_type* needs to be `MetricReport` and *event_format_type* needs to be `MetricReport` for metrics subscription.
> - *event_type* needs to be `Alert` and *event_format_type* needs to be `Event` for event subscription.
> - Modifying a subscription is not supported.
> - Context is always set to RedfishEvent.
> - This module supports `check_mode`.

## [Examples](redfish_event_subscription_module.md#id5)

```yaml+jinja
---
- name: Add Redfish metric subscription
  redfish_event_subscription:
    baseuri: "192.168.0.1"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    destination: "https://192.168.1.100:8188"
    event_type: MetricReport
    event_format_type: MetricReport
    state: present

- name: Add Redfish alert subscription
  redfish_event_subscription:
    baseuri: "192.168.0.1"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    destination: "https://server01.example.com:8188"
    event_type: Alert
    event_format_type: Event
    state: present

- name: Delete Redfish subscription with a specified destination
  redfish_event_subscription:
    baseuri: "192.168.0.1"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    destination: "https://server01.example.com:8188"
    state: absent
```

## [Return Values](redfish_event_subscription_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of http error.  Returned: on http error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to complete the operation because the JSON data format entered is invalid.", "Resolution": "Do the following and the retry the operation: 1) Enter the correct JSON data format and retry the operation. 2) Make sure that no syntax error is present in JSON data format. 3) Make sure that a duplicate key is not present in JSON data format.", "Severity": "Critical"}, {"Message": "The request body submitted was malformed JSON and could not be parsed by the receiving service.", "Resolution": "Ensure that the request body is valid JSON and resubmit the request.", "Severity": "Critical"}], "code": "Base.1.2.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the task.  Returned: always  Sample: `"Successfully added the subscription."` |
| **status**  dictionary | Returns subscription object created  Returned: on adding subscription successfully  Sample: `{"@Message.ExtendedInfo": [{"Message": "The resource has been created successfully", "MessageArgs": [], "MessageArgs@odata.count": 0, "MessageId": "Base.1.7.Created", "RelatedProperties": [], "RelatedProperties@odata.count": 0, "Resolution": "None", "Severity": "OK"}, {"Message": "A new resource is successfully created.", "MessageArgs": [], "MessageArgs@odata.count": 0, "MessageId": "IDRAC.2.2.SYS414", "RelatedProperties": [], "RelatedProperties@odata.count": 0, "Resolution": "No response action is required.", "Severity": "Informational"}], "Actions": {"#EventDestination.ResumeSubscription": {"target": "/redfish/v1/EventService/Subscriptions/5d432f36-81f4-11eb-9dc0-2cea7ff7ff9a/Actions/EventDestination.ResumeSubscription"}}, "Context": "RedfishEvent", "DeliveryRetryPolicy": "RetryForever", "Description": "Event Subscription Details", "Destination": "https://192.168.1.100:8188", "EventFormatType": "Event", "EventTypes": ["Alert"], "EventTypes@odata.count": 1, "HttpHeaders": [], "HttpHeaders@odata.count": 0, "Id": "5d432f36-81f4-11eb-9dc0-2cea7ff7ff9a", "MetricReportDefinitions": [], "MetricReportDefinitions@odata.count": 0, "Name": "EventSubscription 5d432f36-81f4-11eb-9dc0-2cea7ff7ff9a", "OriginResources": [], "OriginResources@odata.count": 0, "Protocol": "Redfish", "Status": {"Health": "OK", "HealthRollup": "OK", "State": "Enabled"}, "SubscriptionType": "RedfishEvent"}` |

### Authors

- Trevor Squillario (@TrevorSquillario)
- Sachin Apagundi (@sachin-apa)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)

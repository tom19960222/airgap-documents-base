---
collection: ansible
version: "8"
title: "cisco.ise.device_administration_local_exception_rules module – Resource module for Device Administration Local Exception Rules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/device_administration_local_exception_rules_module.html
fetched_at: 2026-07-28T01:28:01+00:00
---
# cisco.ise.device_administration_local_exception_rules module – Resource module for Device Administration Local Exception Rules

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/ui/repo/published/cisco/ise/) (version 2.6.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](device_administration_local_exception_rules_module.md#ansible-collections-cisco-ise-device-administration-local-exception-rules-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.device_administration_local_exception_rules`.

New in cisco.ise 1.0.0

- [Synopsis](device_administration_local_exception_rules_module.md#synopsis)
- [Requirements](device_administration_local_exception_rules_module.md#requirements)
- [Parameters](device_administration_local_exception_rules_module.md#parameters)
- [Notes](device_administration_local_exception_rules_module.md#notes)
- [See Also](device_administration_local_exception_rules_module.md#see-also)
- [Examples](device_administration_local_exception_rules_module.md#examples)
- [Return Values](device_administration_local_exception_rules_module.md#return-values)

## [Synopsis](device_administration_local_exception_rules_module.md#id1)

- Manage operations create, update and delete of the resource Device Administration Local Exception Rules.
- Device Admin - Create local authorization exception rule.
- Device Admin - Delete local exception rule.
- Device Admin - Update local exception rule.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](device_administration_local_exception_rules_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](device_administration_local_exception_rules_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=string | Command sets enforce the specified list of commands that can be executed by a device administrator. |
| **id**  string | Id path parameter. Rule id. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_single_request_timeout**  integer  *added in cisco.ise 3.0.0* | Timeout (in seconds) for RESTful HTTP requests.  **Default:** `60` |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  *added in cisco.ise 1.1.0* | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  **Choices:**   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  *added in cisco.ise 3.0.0* | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  **Choices:**   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  **Default:** `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  **Choices:**   - `false` - `true` ← (default) |
| **link**  dictionary | Device Administration Local Exception Rules’s link. |
| **href**  string | Device Administration Local Exception Rules’s href. |
| **rel**  string | Device Administration Local Exception Rules’s rel. |
| **type**  string | Device Administration Local Exception Rules’s type. |
| **policyId**  string | PolicyId path parameter. Policy id. |
| **profile**  string | Device admin profiles control the initial login session of the device administrator. |
| **rule**  dictionary | Common attributes in rule authentication/authorization. |
| **condition**  dictionary | Device Administration Local Exception Rules’s condition. |
| **attributeId**  string | Dictionary attribute id (Optional), used for additional verification. |
| **attributeName**  string | Dictionary attribute name. |
| **attributeValue**  string | <ul><li>Attribute value for condition</li> <li>Value type is specified in dictionary object</li> <li>if multiple values allowed is specified in dictionary object</li></ul>. |
| **children**  list / elements=dictionary | In case type is andBlock or orBlock addtional conditions will be aggregated under this logical (OR/AND) condition. |
| **conditionType**  string | <ul><li>Inidicates whether the record is the condition itself(data) or a logical(or,and) aggregation</li> <li>Data type enum(reference,single) indicates than “conditonId” OR “ConditionAttrs” fields should contain condition data but not both</li> <li>Logical aggreation(and,or) enum indicates that additional conditions are present under the children field</li></ul>. |
| **isNegate**  boolean | Indicates whereas this condition is in negate mode.  **Choices:**   - `false` - `true` |
| **link**  dictionary | Device Administration Local Exception Rules’s link. |
| **href**  string | Device Administration Local Exception Rules’s href. |
| **rel**  string | Device Administration Local Exception Rules’s rel. |
| **type**  string | Device Administration Local Exception Rules’s type. |
| **conditionType**  string | <ul><li>Inidicates whether the record is the condition itself(data) or a logical(or,and) aggregation</li> <li>Data type enum(reference,single) indicates than “conditonId” OR “ConditionAttrs” fields should contain condition data but not both</li> <li>Logical aggreation(and,or) enum indicates that additional conditions are present under the children field</li></ul>. |
| **datesRange**  dictionary | <p>Defines for which date/s TimeAndDate condition will be matched or NOT matched if used in exceptionDates prooperty<br> Options are - Date range, for specific date, the same date should be used for start/end date <br> Default - no specific dates<br> In order to reset the dates to have no specific dates Date format - yyyy-mm-dd (MM = month, dd = day, yyyy = year)</p>. |
| **endDate**  string | Device Administration Local Exception Rules’s endDate. |
| **startDate**  string | Device Administration Local Exception Rules’s startDate. |
| **datesRangeException**  dictionary | <p>Defines for which date/s TimeAndDate condition will be matched or NOT matched if used in exceptionDates prooperty<br> Options are - Date range, for specific date, the same date should be used for start/end date <br> Default - no specific dates<br> In order to reset the dates to have no specific dates Date format - yyyy-mm-dd (MM = month, dd = day, yyyy = year)</p>. |
| **endDate**  string | Device Administration Local Exception Rules’s endDate. |
| **startDate**  string | Device Administration Local Exception Rules’s startDate. |
| **description**  string | Condition description. |
| **dictionaryName**  string | Dictionary name. |
| **dictionaryValue**  string | Dictionary value. |
| **hoursRange**  dictionary | <p>Defines for which hours a TimeAndDate condition will be matched or not matched if used in exceptionHours property<br> Time foramt - hh mm ( h = hour , mm = minutes ) <br> Default - All Day </p>. |
| **endTime**  string | Device Administration Local Exception Rules’s endTime. |
| **startTime**  string | Device Administration Local Exception Rules’s startTime. |
| **hoursRangeException**  dictionary | <p>Defines for which hours a TimeAndDate condition will be matched or not matched if used in exceptionHours property<br> Time foramt - hh mm ( h = hour , mm = minutes ) <br> Default - All Day </p>. |
| **endTime**  string | Device Administration Local Exception Rules’s endTime. |
| **startTime**  string | Device Administration Local Exception Rules’s startTime. |
| **id**  string | Device Administration Local Exception Rules’s id. |
| **isNegate**  boolean | Indicates whereas this condition is in negate mode.  **Choices:**   - `false` - `true` |
| **link**  dictionary | Device Administration Local Exception Rules’s link. |
| **href**  string | Device Administration Local Exception Rules’s href. |
| **rel**  string | Device Administration Local Exception Rules’s rel. |
| **type**  string | Device Administration Local Exception Rules’s type. |
| **name**  string | Condition name. |
| **operator**  string | Equality operator. |
| **weekDays**  list / elements=string | <p>Defines for which days this condition will be matched<br> Days format - Arrays of WeekDay enums <br> Default - List of All week days</p>. |
| **weekDaysException**  list / elements=string | <p>Defines for which days this condition will NOT be matched<br> Days format - Arrays of WeekDay enums <br> Default - Not enabled</p>. |
| **default**  boolean | Indicates if this rule is the default one.  **Choices:**   - `false` - `true` |
| **hitCounts**  integer | The amount of times the rule was matched. |
| **id**  string | The identifier of the rule. |
| **name**  string | Rule name, Valid characters are alphanumerics, underscore, hyphen, space, period, parentheses. |
| **rank**  integer | The rank(priority) in relation to other rules. Lower rank is higher priority. |
| **state**  string | The state that the rule is in. A disabled rule cannot be matched. |

## [Notes](device_administration_local_exception_rules_module.md#id4)

> **Note:**
>
> - SDK Method used are device_administration_authorization_exception_rules.DeviceAdministrationAuthorizationExceptionRules.create_device_admin_local_exception_rule, device_administration_authorization_exception_rules.DeviceAdministrationAuthorizationExceptionRules.delete_device_admin_local_exception_rule_by_id, device_administration_authorization_exception_rules.DeviceAdministrationAuthorizationExceptionRules.update_device_admin_local_exception_rule_by_id,
> - Paths used are post /device-admin/policy-set/{policyId}/exception, delete /device-admin/policy-set/{policyId}/exception/{id}, put /device-admin/policy-set/{policyId}/exception/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](device_administration_local_exception_rules_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for Device Administration - Authorization Exception Rules](https://developer.cisco.com/docs/identity-services-engine/v1/#!policy-openapi)
> :   Complete reference of the Device Administration - Authorization Exception Rules API.

## [Examples](device_administration_local_exception_rules_module.md#id6)

```yaml+jinja
- name: Create
  cisco.ise.device_administration_local_exception_rules:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    commands:
    - string
    link:
      href: string
      rel: string
      type: string
    policyId: string
    profile: string
    rule:
      condition:
        attributeId: string
        attributeName: string
        attributeValue: string
        children:
        - conditionType: string
          isNegate: true
          link:
            href: string
            rel: string
            type: string
        conditionType: string
        datesRange:
          endDate: string
          startDate: string
        datesRangeException:
          endDate: string
          startDate: string
        description: string
        dictionaryName: string
        dictionaryValue: string
        hoursRange:
          endTime: string
          startTime: string
        hoursRangeException:
          endTime: string
          startTime: string
        id: string
        isNegate: true
        link:
          href: string
          rel: string
          type: string
        name: string
        operator: string
        weekDays:
        - string
        weekDaysException:
        - string
      default: true
      hitCounts: 0
      id: string
      name: string
      rank: 0
      state: string

- name: Update by id
  cisco.ise.device_administration_local_exception_rules:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    commands:
    - string
    id: string
    link:
      href: string
      rel: string
      type: string
    policyId: string
    profile: string
    rule:
      condition:
        attributeId: string
        attributeName: string
        attributeValue: string
        children:
        - conditionType: string
          isNegate: true
          link:
            href: string
            rel: string
            type: string
        conditionType: string
        datesRange:
          endDate: string
          startDate: string
        datesRangeException:
          endDate: string
          startDate: string
        description: string
        dictionaryName: string
        dictionaryValue: string
        hoursRange:
          endTime: string
          startTime: string
        hoursRangeException:
          endTime: string
          startTime: string
        id: string
        isNegate: true
        link:
          href: string
          rel: string
          type: string
        name: string
        operator: string
        weekDays:
        - string
        weekDaysException:
        - string
      default: true
      hitCounts: 0
      id: string
      name: string
      rank: 0
      state: string

- name: Delete by id
  cisco.ise.device_administration_local_exception_rules:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
    policyId: string
```

## [Return Values](device_administration_local_exception_rules_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"commands": ["string"], "link": {"href": "string", "rel": "string", "type": "string"}, "profile": "string", "rule": {"condition": {"attributeId": "string", "attributeName": "string", "attributeValue": "string", "children": [{"conditionType": "string", "isNegate": true, "link": {"href": "string", "rel": "string", "type": "string"}}], "conditionType": "string", "datesRange": {"endDate": "string", "startDate": "string"}, "datesRangeException": {"endDate": "string", "startDate": "string"}, "description": "string", "dictionaryName": "string", "dictionaryValue": "string", "hoursRange": {"endTime": "string", "startTime": "string"}, "hoursRangeException": {"endTime": "string", "startTime": "string"}, "id": "string", "isNegate": true, "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "operator": "string", "weekDays": ["string"], "weekDaysException": ["string"]}, "default": true, "hitCounts": 0, "id": "string", "name": "string", "rank": 0, "state": "string"}}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"response": {"commands": ["string"], "link": {"href": "string", "rel": "string", "type": "string"}, "profile": "string", "rule": {"condition": {"attributeId": "string", "attributeName": "string", "attributeValue": "string", "children": [{"conditionType": "string", "isNegate": true, "link": {"href": "string", "rel": "string", "type": "string"}}], "conditionType": "string", "datesRange": {"endDate": "string", "startDate": "string"}, "datesRangeException": {"endDate": "string", "startDate": "string"}, "description": "string", "dictionaryName": "string", "dictionaryValue": "string", "hoursRange": {"endTime": "string", "startTime": "string"}, "hoursRangeException": {"endTime": "string", "startTime": "string"}, "id": "string", "isNegate": true, "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "operator": "string", "weekDays": ["string"], "weekDaysException": ["string"]}, "default": true, "hitCounts": 0, "id": "string", "name": "string", "rank": 0, "state": "string"}}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)

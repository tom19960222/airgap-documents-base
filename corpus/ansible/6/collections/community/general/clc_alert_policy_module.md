---
collection: ansible
version: "6"
title: "community.general.clc_alert_policy module – Create or Delete Alert Policies at CenturyLink Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/clc_alert_policy_module.html
fetched_at: 2026-07-27T17:08:24+00:00
---
# community.general.clc_alert_policy module – Create or Delete Alert Policies at CenturyLink Cloud

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](clc_alert_policy_module.md#ansible-collections-community-general-clc-alert-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.clc_alert_policy`.

- [Synopsis](clc_alert_policy_module.md#synopsis)
- [Requirements](clc_alert_policy_module.md#requirements)
- [Parameters](clc_alert_policy_module.md#parameters)
- [Notes](clc_alert_policy_module.md#notes)
- [Examples](clc_alert_policy_module.md#examples)
- [Return Values](clc_alert_policy_module.md#return-values)

## [Synopsis](clc_alert_policy_module.md#id1)

- An Ansible module to Create or Delete Alert Policies at CenturyLink Cloud.

## [Requirements](clc_alert_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python = 2.7
- requests >= 2.5.0
- clc-sdk

## [Parameters](clc_alert_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alert_recipients**  list / elements=string | A list of recipient email ids to notify the alert. This is required for state ‘present’ |
| **alias**  string / required | The alias of your CLC Account |
| **duration**  string | The length of time in minutes that the condition must exceed the threshold. This is required for state ‘present’ |
| **id**  string | The alert policy id. This is mutually exclusive with name |
| **metric**  string | The metric on which to measure the condition that will trigger the alert. This is required for state ‘present’  Choices:   - `"cpu"` - `"memory"` - `"disk"` |
| **name**  string | The name of the alert policy. This is mutually exclusive with id |
| **state**  string | Whether to create or delete the policy.  Choices:   - `"present"` ← (default) - `"absent"` |
| **threshold**  integer | The threshold that will trigger the alert when the metric equals or exceeds it. This is required for state ‘present’ This number represents a percentage and must be a value between 5.0 - 95.0 that is a multiple of 5.0 |

## [Notes](clc_alert_policy_module.md#id4)

> **Note:**
>
> - To use this module, it is required to set the below environment variables which enables access to the Centurylink Cloud - CLC_V2_API_USERNAME, the account login id for the centurylink cloud - CLC_V2_API_PASSWORD, the account password for the centurylink cloud
> - Alternatively, the module accepts the API token and account alias. The API token can be generated using the CLC account login and password via the HTTP api call @ <https://api.ctl.io/v2/authentication/login> - CLC_V2_API_TOKEN, the API token generated from <https://api.ctl.io/v2/authentication/login> - CLC_ACCT_ALIAS, the account alias associated with the centurylink cloud
> - Users can set CLC_V2_API_URL to specify an endpoint for pointing to a different CLC environment.

## [Examples](clc_alert_policy_module.md#id5)

```yaml+jinja
# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

---
- name: Create Alert Policy Example
  hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - name: Create an Alert Policy for disk above 80% for 5 minutes
      community.general.clc_alert_policy:
        alias: wfad
        name: 'alert for disk > 80%'
        alert_recipients:
            - test1@centurylink.com
            - test2@centurylink.com
        metric: 'disk'
        duration: '00:05:00'
        threshold: 80
        state: present
      register: policy

    - name: Debug
      ansible.builtin.debug: var=policy

- name: Delete Alert Policy Example
  hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - name: Delete an Alert Policy
      community.general.clc_alert_policy:
        alias: wfad
        name: 'alert for disk > 80%'
        state: absent
      register: policy

    - name: Debug
      ansible.builtin.debug: var=policy
```

## [Return Values](clc_alert_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **policy**  dictionary | The alert policy information  Returned: success  Sample: `{"actions": [{"action": "email", "settings": {"recipients": ["user1@domain.com", "user1@domain.com"]}}], "id": "ba54ac54a60d4a4f1ed6d48c1ce240a7", "links": [{"href": "/v2/alertPolicies/alias/ba54ac54a60d4a4fb1d6d48c1ce240a7", "rel": "self", "verbs": ["GET", "DELETE", "PUT"]}], "name": "test_alert", "triggers": [{"duration": "00:05:00", "metric": "disk", "threshold": 80.0}]}` |

### Authors

- CLC Runner (@clc-runner)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

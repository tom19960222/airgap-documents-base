---
collection: ansible
version: "6"
title: "community.general.clc_aa_policy module – Create or Delete Anti Affinity Policies at CenturyLink Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/clc_aa_policy_module.html
fetched_at: 2026-07-27T17:08:23+00:00
---
# community.general.clc_aa_policy module – Create or Delete Anti Affinity Policies at CenturyLink Cloud

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
> see [Requirements](clc_aa_policy_module.md#ansible-collections-community-general-clc-aa-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.clc_aa_policy`.

- [Synopsis](clc_aa_policy_module.md#synopsis)
- [Requirements](clc_aa_policy_module.md#requirements)
- [Parameters](clc_aa_policy_module.md#parameters)
- [Notes](clc_aa_policy_module.md#notes)
- [Examples](clc_aa_policy_module.md#examples)
- [Return Values](clc_aa_policy_module.md#return-values)

## [Synopsis](clc_aa_policy_module.md#id1)

- An Ansible module to Create or Delete Anti Affinity Policies at CenturyLink Cloud.

## [Requirements](clc_aa_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python = 2.7
- requests >= 2.5.0
- clc-sdk

## [Parameters](clc_aa_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **location**  string / required | Datacenter in which the policy lives/should live. |
| **name**  string / required | The name of the Anti Affinity Policy. |
| **state**  string | Whether to create or delete the policy.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](clc_aa_policy_module.md#id4)

> **Note:**
>
> - To use this module, it is required to set the below environment variables which enables access to the Centurylink Cloud - CLC_V2_API_USERNAME, the account login id for the centurylink cloud - CLC_V2_API_PASSWORD, the account password for the centurylink cloud
> - Alternatively, the module accepts the API token and account alias. The API token can be generated using the CLC account login and password via the HTTP api call @ <https://api.ctl.io/v2/authentication/login> - CLC_V2_API_TOKEN, the API token generated from <https://api.ctl.io/v2/authentication/login> - CLC_ACCT_ALIAS, the account alias associated with the centurylink cloud
> - Users can set CLC_V2_API_URL to specify an endpoint for pointing to a different CLC environment.

## [Examples](clc_aa_policy_module.md#id5)

```yaml+jinja
# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

---
- name: Create AA Policy
  hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - name: Create an Anti Affinity Policy
      community.general.clc_aa_policy:
        name: Hammer Time
        location: UK3
        state: present
      register: policy

    - name: Debug
      ansible.builtin.debug:
        var: policy

- name: Delete AA Policy
  hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - name: Delete an Anti Affinity Policy
      community.general.clc_aa_policy:
        name: Hammer Time
        location: UK3
        state: absent
      register: policy

    - name: Debug
      ansible.builtin.debug:
        var: policy
```

## [Return Values](clc_aa_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **policy**  dictionary | The anti affinity policy information  Returned: success  Sample: `{"id": "1a28dd0988984d87b9cd61fa8da15424", "links": [{"href": "/v2/antiAffinityPolicies/wfad/1a28dd0988984d87b9cd61fa8da15424", "rel": "self", "verbs": ["GET", "DELETE", "PUT"]}, {"href": "/v2/datacenters/wfad/UC1", "id": "uc1", "name": "UC1 - US West (Santa Clara)", "rel": "location"}], "location": "UC1", "name": "test_aa_policy"}` |

### Authors

- CLC Runner (@clc-runner)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

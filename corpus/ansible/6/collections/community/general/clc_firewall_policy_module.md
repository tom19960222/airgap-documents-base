---
collection: ansible
version: "6"
title: "community.general.clc_firewall_policy module – Create/delete/update firewall policies"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/clc_firewall_policy_module.html
fetched_at: 2026-07-27T17:08:25+00:00
---
# community.general.clc_firewall_policy module – Create/delete/update firewall policies

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
> see [Requirements](clc_firewall_policy_module.md#ansible-collections-community-general-clc-firewall-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.clc_firewall_policy`.

- [Synopsis](clc_firewall_policy_module.md#synopsis)
- [Requirements](clc_firewall_policy_module.md#requirements)
- [Parameters](clc_firewall_policy_module.md#parameters)
- [Notes](clc_firewall_policy_module.md#notes)
- [Examples](clc_firewall_policy_module.md#examples)
- [Return Values](clc_firewall_policy_module.md#return-values)

## [Synopsis](clc_firewall_policy_module.md#id1)

- Create or delete or update firewall policies on Centurylink Cloud

## [Requirements](clc_firewall_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python = 2.7
- requests >= 2.5.0
- clc-sdk

## [Parameters](clc_firewall_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **destination**  list / elements=string | The list of destination addresses for traffic on the terminating firewall. This is required when state is ‘present’ |
| **destination_account_alias**  string | CLC alias for the destination account |
| **enabled**  string | Whether the firewall policy is enabled or disabled  Choices:   - `"True"` ← (default) - `"False"` |
| **firewall_policy_id**  string | Id of the firewall policy. This is required to update or delete an existing firewall policy |
| **location**  string / required | Target datacenter for the firewall policy |
| **ports**  list / elements=string | The list of ports associated with the policy. TCP and UDP can take in single ports or port ranges.  Example: `['any', 'icmp', 'TCP/123', 'UDP/123', 'TCP/123-456', 'UDP/123-456']`. |
| **source**  list / elements=string | The list of source addresses for traffic on the originating firewall. This is required when state is ‘present’ |
| **source_account_alias**  string / required | CLC alias for the source account |
| **state**  string | Whether to create or delete the firewall policy  Choices:   - `"present"` ← (default) - `"absent"` |
| **wait**  string | Whether to wait for the provisioning tasks to finish before returning.  Default: `"True"` |

## [Notes](clc_firewall_policy_module.md#id4)

> **Note:**
>
> - To use this module, it is required to set the below environment variables which enables access to the Centurylink Cloud - CLC_V2_API_USERNAME, the account login id for the centurylink cloud - CLC_V2_API_PASSWORD, the account password for the centurylink cloud
> - Alternatively, the module accepts the API token and account alias. The API token can be generated using the CLC account login and password via the HTTP api call @ <https://api.ctl.io/v2/authentication/login> - CLC_V2_API_TOKEN, the API token generated from <https://api.ctl.io/v2/authentication/login> - CLC_ACCT_ALIAS, the account alias associated with the centurylink cloud
> - Users can set CLC_V2_API_URL to specify an endpoint for pointing to a different CLC environment.

## [Examples](clc_firewall_policy_module.md#id5)

```yaml+jinja
---
- name: Create Firewall Policy
  hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - name: Create / Verify an Firewall Policy at CenturyLink Cloud
      clc_firewall:
        source_account_alias: WFAD
        location: VA1
        state: present
        source: 10.128.216.0/24
        destination: 10.128.216.0/24
        ports: Any
        destination_account_alias: WFAD

- name: Delete Firewall Policy
  hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - name: Delete an Firewall Policy at CenturyLink Cloud
      clc_firewall:
        source_account_alias: WFAD
        location: VA1
        state: absent
        firewall_policy_id: c62105233d7a4231bd2e91b9c791e43e1
```

## [Return Values](clc_firewall_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **firewall_policy**  dictionary | The fire wall policy information  Returned: success  Sample: `{"destination": ["10.1.1.0/24", "10.2.2.0/24"], "destinationAccount": "wfad", "enabled": true, "id": "fc36f1bfd47242e488a9c44346438c05", "links": [{"href": "http://api.ctl.io/v2-experimental/firewallPolicies/wfad/uc1/fc36f1bfd47242e488a9c44346438c05", "rel": "self", "verbs": ["GET", "PUT", "DELETE"]}], "ports": ["any"], "source": ["10.1.1.0/24", "10.2.2.0/24"], "status": "active"}` |
| **firewall_policy_id**  string | The fire wall policy id  Returned: success  Sample: `"fc36f1bfd47242e488a9c44346438c05"` |

### Authors

- CLC Runner (@clc-runner)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

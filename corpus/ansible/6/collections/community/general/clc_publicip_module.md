---
collection: ansible
version: "6"
title: "community.general.clc_publicip module – Add and Delete public ips on servers in CenturyLink Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/clc_publicip_module.html
fetched_at: 2026-07-27T17:08:28+00:00
---
# community.general.clc_publicip module – Add and Delete public ips on servers in CenturyLink Cloud

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
> see [Requirements](clc_publicip_module.md#ansible-collections-community-general-clc-publicip-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.clc_publicip`.

- [Synopsis](clc_publicip_module.md#synopsis)
- [Requirements](clc_publicip_module.md#requirements)
- [Parameters](clc_publicip_module.md#parameters)
- [Notes](clc_publicip_module.md#notes)
- [Examples](clc_publicip_module.md#examples)
- [Return Values](clc_publicip_module.md#return-values)

## [Synopsis](clc_publicip_module.md#id1)

- An Ansible module to add or delete public ip addresses on an existing server or servers in CenturyLink Cloud.

## [Requirements](clc_publicip_module.md#id2)

The below requirements are needed on the host that executes this module.

- python = 2.7
- requests >= 2.5.0
- clc-sdk

## [Parameters](clc_publicip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ports**  list / elements=integer | A list of ports to expose. This is required when state is ‘present’ |
| **protocol**  string | The protocol that the public IP will listen for.  Choices:   - `"TCP"` ← (default) - `"UDP"` - `"ICMP"` |
| **server_ids**  list / elements=string / required | A list of servers to create public ips on. |
| **state**  string | Determine whether to create or delete public IPs. If present module will not create a second public ip if one already exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **wait**  boolean | Whether to wait for the tasks to finish before returning.  Choices:   - `false` - `true` ← (default) |

## [Notes](clc_publicip_module.md#id4)

> **Note:**
>
> - To use this module, it is required to set the below environment variables which enables access to the Centurylink Cloud - CLC_V2_API_USERNAME, the account login id for the centurylink cloud - CLC_V2_API_PASSWORD, the account password for the centurylink cloud
> - Alternatively, the module accepts the API token and account alias. The API token can be generated using the CLC account login and password via the HTTP api call @ <https://api.ctl.io/v2/authentication/login> - CLC_V2_API_TOKEN, the API token generated from <https://api.ctl.io/v2/authentication/login> - CLC_ACCT_ALIAS, the account alias associated with the centurylink cloud
> - Users can set CLC_V2_API_URL to specify an endpoint for pointing to a different CLC environment.

## [Examples](clc_publicip_module.md#id5)

```yaml+jinja
# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

- name: Add Public IP to Server
  hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - name: Create Public IP For Servers
      community.general.clc_publicip:
        protocol: TCP
        ports:
          - 80
        server_ids:
          - UC1TEST-SVR01
          - UC1TEST-SVR02
        state: present
      register: clc

    - name: Debug
      ansible.builtin.debug:
        var: clc

- name: Delete Public IP from Server
  hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - name: Create Public IP For Servers
      community.general.clc_publicip:
        server_ids:
          - UC1TEST-SVR01
          - UC1TEST-SVR02
        state: absent
      register: clc

    - name: Debug
      ansible.builtin.debug:
        var: clc
```

## [Return Values](clc_publicip_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **server_ids**  list / elements=string | The list of server ids that are changed  Returned: success  Sample: `["UC1TEST-SVR01", "UC1TEST-SVR02"]` |

### Authors

- CLC Runner (@clc-runner)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

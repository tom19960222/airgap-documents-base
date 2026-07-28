---
collection: ansible
version: "6"
title: "community.general.clc_loadbalancer module – Create, Delete shared loadbalancers in CenturyLink Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/clc_loadbalancer_module.html
fetched_at: 2026-07-27T17:08:26+00:00
---
# community.general.clc_loadbalancer module – Create, Delete shared loadbalancers in CenturyLink Cloud

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
> see [Requirements](clc_loadbalancer_module.md#ansible-collections-community-general-clc-loadbalancer-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.clc_loadbalancer`.

- [Synopsis](clc_loadbalancer_module.md#synopsis)
- [Requirements](clc_loadbalancer_module.md#requirements)
- [Parameters](clc_loadbalancer_module.md#parameters)
- [Notes](clc_loadbalancer_module.md#notes)
- [Examples](clc_loadbalancer_module.md#examples)
- [Return Values](clc_loadbalancer_module.md#return-values)

## [Synopsis](clc_loadbalancer_module.md#id1)

- An Ansible module to Create, Delete shared loadbalancers in CenturyLink Cloud.

## [Requirements](clc_loadbalancer_module.md#id2)

The below requirements are needed on the host that executes this module.

- python = 2.7
- requests >= 2.5.0
- clc-sdk

## [Parameters](clc_loadbalancer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alias**  string / required | The alias of your CLC Account |
| **description**  string | A description for the loadbalancer |
| **location**  string / required | The location of the datacenter where the load balancer resides in |
| **method**  string | -The balancing method for the load balancer pool  Choices:   - `"leastConnection"` - `"roundRobin"` |
| **name**  string / required | The name of the loadbalancer |
| **nodes**  list / elements=dictionary | A list of nodes that needs to be added to the load balancer pool  Default: `[]` |
| **persistence**  string | The persistence method for the load balancer  Choices:   - `"standard"` - `"sticky"` |
| **port**  string | Port to configure on the public-facing side of the load balancer pool  Choices:   - `"80"` - `"443"` |
| **state**  string | Whether to create or delete the load balancer pool  Choices:   - `"present"` ← (default) - `"absent"` - `"port_absent"` - `"nodes_present"` - `"nodes_absent"` |
| **status**  string | The status of the loadbalancer  Choices:   - `"enabled"` ← (default) - `"disabled"` |

## [Notes](clc_loadbalancer_module.md#id4)

> **Note:**
>
> - To use this module, it is required to set the below environment variables which enables access to the Centurylink Cloud - CLC_V2_API_USERNAME, the account login id for the centurylink cloud - CLC_V2_API_PASSWORD, the account password for the centurylink cloud
> - Alternatively, the module accepts the API token and account alias. The API token can be generated using the CLC account login and password via the HTTP api call @ <https://api.ctl.io/v2/authentication/login> - CLC_V2_API_TOKEN, the API token generated from <https://api.ctl.io/v2/authentication/login> - CLC_ACCT_ALIAS, the account alias associated with the centurylink cloud
> - Users can set CLC_V2_API_URL to specify an endpoint for pointing to a different CLC environment.

## [Examples](clc_loadbalancer_module.md#id5)

```yaml+jinja
# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples
- name: Create Loadbalancer
  hosts: localhost
  connection: local
  tasks:
    - name: Actually Create things
      community.general.clc_loadbalancer:
        name: test
        description: test
        alias: TEST
        location: WA1
        port: 443
        nodes:
          - ipAddress: 10.11.22.123
            privatePort: 80
        state: present

- name: Add node to an existing loadbalancer pool
  hosts: localhost
  connection: local
  tasks:
    - name: Actually Create things
      community.general.clc_loadbalancer:
        name: test
        description: test
        alias: TEST
        location: WA1
        port: 443
        nodes:
          - ipAddress: 10.11.22.234
            privatePort: 80
        state: nodes_present

- name: Remove node from an existing loadbalancer pool
  hosts: localhost
  connection: local
  tasks:
    - name: Actually Create things
      community.general.clc_loadbalancer:
        name: test
        description: test
        alias: TEST
        location: WA1
        port: 443
        nodes:
          - ipAddress: 10.11.22.234
            privatePort: 80
        state: nodes_absent

- name: Delete LoadbalancerPool
  hosts: localhost
  connection: local
  tasks:
    - name: Actually Delete things
      community.general.clc_loadbalancer:
        name: test
        description: test
        alias: TEST
        location: WA1
        port: 443
        nodes:
          - ipAddress: 10.11.22.123
            privatePort: 80
        state: port_absent

- name: Delete Loadbalancer
  hosts: localhost
  connection: local
  tasks:
    - name: Actually Delete things
      community.general.clc_loadbalancer:
        name: test
        description: test
        alias: TEST
        location: WA1
        port: 443
        nodes:
          - ipAddress: 10.11.22.123
            privatePort: 80
        state: absent
```

## [Return Values](clc_loadbalancer_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **loadbalancer**  dictionary | The load balancer result object from CLC  Returned: success  Sample: `{"description": "test-lb", "id": "ab5b18cb81e94ab9925b61d1ca043fb5", "ipAddress": "66.150.174.197", "links": [{"href": "/v2/sharedLoadBalancers/wfad/wa1/ab5b18cb81e94ab9925b61d1ca043fb5", "rel": "self", "verbs": ["GET", "PUT", "DELETE"]}, {"href": "/v2/sharedLoadBalancers/wfad/wa1/ab5b18cb81e94ab9925b61d1ca043fb5/pools", "rel": "pools", "verbs": ["GET", "POST"]}], "name": "test-lb", "pools": [], "status": "enabled"}` |

### Authors

- CLC Runner (@clc-runner)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

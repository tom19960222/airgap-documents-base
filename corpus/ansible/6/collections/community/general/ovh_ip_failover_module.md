---
collection: ansible
version: "6"
title: "community.general.ovh_ip_failover module – Manage OVH IP failover address"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ovh_ip_failover_module.html
fetched_at: 2026-07-27T17:11:37+00:00
---
# community.general.ovh_ip_failover module – Manage OVH IP failover address

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
> see [Requirements](ovh_ip_failover_module.md#ansible-collections-community-general-ovh-ip-failover-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ovh_ip_failover`.

- [Synopsis](ovh_ip_failover_module.md#synopsis)
- [Requirements](ovh_ip_failover_module.md#requirements)
- [Parameters](ovh_ip_failover_module.md#parameters)
- [Notes](ovh_ip_failover_module.md#notes)
- [Examples](ovh_ip_failover_module.md#examples)

## [Synopsis](ovh_ip_failover_module.md#id1)

- Manage OVH (French European hosting provider) IP Failover Address. For now, this module can only be used to move an ip failover (or failover block) between services

## [Requirements](ovh_ip_failover_module.md#id2)

The below requirements are needed on the host that executes this module.

- ovh >= 0.4.8

## [Parameters](ovh_ip_failover_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **application_key**  string / required | The applicationKey to use |
| **application_secret**  string / required | The application secret to use |
| **consumer_key**  string / required | The consumer key to use |
| **endpoint**  string / required | The endpoint to use ( for instance ovh-eu) |
| **name**  string / required | The IP address to manage (can be a single IP like 1.1.1.1 or a block like 1.1.1.1/28 ) |
| **service**  string / required | The name of the OVH service this IP address should be routed |
| **timeout**  integer | The timeout in seconds used to wait for a task to be completed. Default is 120 seconds.  Default: `120` |
| **wait_completion**  boolean | If true, the module will wait for the IP address to be moved. If false, exit without waiting. The taskId will be returned in module output  Choices:   - `false` - `true` ← (default) |
| **wait_task_completion**  integer | If not 0, the module will wait for this task id to be completed. Use wait_task_completion if you want to wait for completion of a previously executed task with wait_completion=false. You can execute this module repeatedly on a list of failover IPs using wait_completion=false (see examples)  Default: `0` |

## [Notes](ovh_ip_failover_module.md#id4)

> **Note:**
>
> - Uses the python OVH Api <https://github.com/ovh/python-ovh>. You have to create an application (a key and secret) with a consummer key as described into <https://docs.ovh.com/gb/en/customer/first-steps-with-ovh-api/>

## [Examples](ovh_ip_failover_module.md#id5)

```yaml+jinja
# Route an IP address 1.1.1.1 to the service ns666.ovh.net
- community.general.ovh_ip_failover:
    name: 1.1.1.1
    service: ns666.ovh.net
    endpoint: ovh-eu
    application_key: yourkey
    application_secret: yoursecret
    consumer_key: yourconsumerkey
- community.general.ovh_ip_failover:
    name: 1.1.1.1
    service: ns666.ovh.net
    endpoint: ovh-eu
    wait_completion: false
    application_key: yourkey
    application_secret: yoursecret
    consumer_key: yourconsumerkey
  register: moved
- community.general.ovh_ip_failover:
    name: 1.1.1.1
    service: ns666.ovh.net
    endpoint: ovh-eu
    wait_task_completion: "{{moved.taskId}}"
    application_key: yourkey
    application_secret: yoursecret
    consumer_key: yourconsumerkey
```

### Authors

- Pascal HERAUD (@pascalheraud)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

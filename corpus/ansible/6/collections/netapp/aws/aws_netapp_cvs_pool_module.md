---
collection: ansible
version: "6"
title: "netapp.aws.aws_netapp_cvs_pool module – NetApp AWS Cloud Volumes Service Manage Pools."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/aws/aws_netapp_cvs_pool_module.html
fetched_at: 2026-07-27T17:55:48+00:00
---
# netapp.aws.aws_netapp_cvs_pool module – NetApp AWS Cloud Volumes Service Manage Pools.

> **Note:**
>
> This module is part of the [netapp.aws collection](https://galaxy.ansible.com/netapp/aws) (version 21.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.aws`.
>
> To use it in a playbook, specify: `netapp.aws.aws_netapp_cvs_pool`.

New in netapp.aws 2.9.0

- [Synopsis](aws_netapp_cvs_pool_module.md#synopsis)
- [Parameters](aws_netapp_cvs_pool_module.md#parameters)
- [Notes](aws_netapp_cvs_pool_module.md#notes)
- [Examples](aws_netapp_cvs_pool_module.md#examples)

## [Synopsis](aws_netapp_cvs_pool_module.md#id1)

- Create, Update, Delete Pool on AWS Cloud Volumes Service.

## [Parameters](aws_netapp_cvs_pool_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | The access key to authenticate with the AWSCVS Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the AWSCVS Web Services Proxy or Embedded Web Services API. |
| **feature_flags**  dictionary  added in netapp.aws 21.6.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored.  trace_apis can be set to true to enable tracing, data is written to /tmp/um_apis.log. |
| **from_name**  string | rename the existing pool name ( The human readable name of the Pool )  *from_name* is the existing name, and *name* the new name  can be used with update operation |
| **name**  string / required | pool name ( The human readable name of the Pool )  name can be used for create, update and delete operations |
| **region**  string / required | The region to which the Pool is associated. |
| **secret_key**  string / required | The secret_key to authenticate with the AWSCVS Web Services Proxy or Embedded Web Services API. |
| **serviceLevel**  string | The service level of the Pool  can be used with pool create, update operations  Choices:   - `"basic"` - `"standard"` - `"extreme"` |
| **sizeInBytes**  integer | Size of the Pool in bytes  can be used with pool create, update operations  minimum value is 4000000000000 bytes |
| **state**  string / required | Whether the specified pool should exist or not.  Choices:   - `"present"` - `"absent"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |
| **vendorID**  string | A vendor ID for the Pool. E.g. an ID allocated by a vendor service for the Pool.  can be used with pool create, update operations  must be unique |

## [Notes](aws_netapp_cvs_pool_module.md#id3)

> **Note:**
>
> - The modules prefixed with aws\_cvs\_netapp are built to Manage AWS Cloud Volumes Service .

## [Examples](aws_netapp_cvs_pool_module.md#id4)

```yaml+jinja
- name: Create a new Pool
  aws_netapp_cvs_pool:
    state: present
    name: TestPoolBB12
    serviceLevel: extreme
    sizeInBytes: 4000000000000
    vendorID: ansiblePoolTestVendorBB12
    region: us-east-1
    api_url: cds-aws-bundles.netapp.com
    api_key: MyAPiKey
    secret_key: MySecretKey

- name: Delete a Pool
  aws_netapp_cvs_pool:
    state: absent
    name: TestPoolBB7
    region: us-east-1
    api_url: cds-aws-bundles.netapp.com
    api_key: MyAPiKey
    secret_key: MySecretKey

- name: Update a Pool
  aws_netapp_cvs_pool:
    state: present
    from_name: TestPoolBB12
    name: Mynewpool7
    vendorID: ansibleVendorMynewpool15
    serviceLevel: extreme
    sizeInBytes: 4000000000000
    region: us-east-1
    api_url: cds-aws-bundles.netapp.com
    api_key: MyAPiKey
    secret_key: MySecretKey
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.aws/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.aws)

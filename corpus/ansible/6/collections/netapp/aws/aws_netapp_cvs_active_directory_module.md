---
collection: ansible
version: "6"
title: "netapp.aws.aws_netapp_cvs_active_directory module – NetApp AWS CloudVolumes Service Manage Active Directory."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/aws/aws_netapp_cvs_active_directory_module.html
fetched_at: 2026-07-27T17:55:46+00:00
---
# netapp.aws.aws_netapp_cvs_active_directory module – NetApp AWS CloudVolumes Service Manage Active Directory.

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
> To use it in a playbook, specify: `netapp.aws.aws_netapp_cvs_active_directory`.

New in netapp.aws 2.9.0

- [Synopsis](aws_netapp_cvs_active_directory_module.md#synopsis)
- [Parameters](aws_netapp_cvs_active_directory_module.md#parameters)
- [Notes](aws_netapp_cvs_active_directory_module.md#notes)
- [Examples](aws_netapp_cvs_active_directory_module.md#examples)

## [Synopsis](aws_netapp_cvs_active_directory_module.md#id1)

- Create, Update, Delete ActiveDirectory on AWS Cloud Volumes Service.

## [Parameters](aws_netapp_cvs_active_directory_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | The access key to authenticate with the AWSCVS Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the AWSCVS Web Services Proxy or Embedded Web Services API. |
| **DNS**  string | DNS server address for the Active Directory domain  Required when `state=present`  Required when `state=present`, to modify ActiveDirectory properties. |
| **domain**  string | Name of the Active Directory domain |
| **feature_flags**  dictionary  added in netapp.aws 21.6.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored.  trace_apis can be set to true to enable tracing, data is written to /tmp/um_apis.log. |
| **netBIOS**  string | NetBIOS name of the server. |
| **password**  string | Password of the Active Directory domain administrator  Required when `state=present`, to modify ActiveDirectory properties |
| **region**  string / required | The region to which the Active Directory credentials are associated. |
| **secret_key**  string / required | The secret_key to authenticate with the AWSCVS Web Services Proxy or Embedded Web Services API. |
| **state**  string / required | Whether the specified ActiveDirectory should exist or not.  Choices:   - `"present"` - `"absent"` |
| **username**  string | Username of the Active Directory domain administrator |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_netapp_cvs_active_directory_module.md#id3)

> **Note:**
>
> - The modules prefixed with aws\_cvs\_netapp are built to Manage AWS Cloud Volumes Service .

## [Examples](aws_netapp_cvs_active_directory_module.md#id4)

```yaml+jinja
- name: Create Active Directory
  aws_netapp_cvs_active_directory.py:
    state: present
    region: us-east-1
    DNS: 101.102.103.123
    domain: mydomain.com
    password: netapp1!
    netBIOS: testing
    username: user1
    api_url : My_CVS_Hostname
    api_key: My_API_Key
    secret_key : My_Secret_Key

- name: Update Active Directory
  aws_netapp_cvs_active_directory.py:
    state: present
    region: us-east-1
    DNS: 101.102.103.123
    domain: mydomain.com
    password: netapp2!
    netBIOS: testingBIOS
    username: user2
    api_url : My_CVS_Hostname
    api_key: My_API_Key
    secret_key : My_Secret_Key

- name: Delete Active Directory
  aws_netapp_cvs_active_directory.py:
    state: absent
    region: us-east-1
    domain: mydomain.com
    api_url : My_CVS_Hostname
    api_key: My_API_Key
    secret_key : My_Secret_Key
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.aws/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.aws)

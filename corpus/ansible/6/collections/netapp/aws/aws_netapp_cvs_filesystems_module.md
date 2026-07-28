---
collection: ansible
version: "6"
title: "netapp.aws.aws_netapp_cvs_filesystems module – NetApp AWS Cloud Volumes Service Manage FileSystem."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/aws/aws_netapp_cvs_filesystems_module.html
fetched_at: 2026-07-27T17:55:47+00:00
---
# netapp.aws.aws_netapp_cvs_filesystems module – NetApp AWS Cloud Volumes Service Manage FileSystem.

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
> To use it in a playbook, specify: `netapp.aws.aws_netapp_cvs_filesystems`.

New in netapp.aws 2.9.0

- [Synopsis](aws_netapp_cvs_filesystems_module.md#synopsis)
- [Parameters](aws_netapp_cvs_filesystems_module.md#parameters)
- [Notes](aws_netapp_cvs_filesystems_module.md#notes)
- [Examples](aws_netapp_cvs_filesystems_module.md#examples)

## [Synopsis](aws_netapp_cvs_filesystems_module.md#id1)

- Create, Update, Delete fileSystem on AWS Cloud Volumes Service.

## [Parameters](aws_netapp_cvs_filesystems_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | The access key to authenticate with the AWSCVS Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the AWSCVS Web Services Proxy or Embedded Web Services API. |
| **creationToken**  string / required | Name of the filesystem |
| **exportPolicy**  dictionary | The policy rules to export the filesystem |
| **rules**  list / elements=dictionary | Set of rules to export the filesystem  Requires allowedClients, access and protocol |
| **allowedClients**  string | Comma separated list of ip address blocks of the clients to access the fileSystem  Each address block contains the starting IP address and size for the block |
| **cifs**  boolean | Enable or disable cifs filesystem  Choices:   - `false` - `true` |
| **nfsv3**  boolean | Enable or disable nfsv3 fileSystem  Choices:   - `false` - `true` |
| **nfsv4**  boolean | Enable or disable nfsv4 filesystem  Choices:   - `false` - `true` |
| **ruleIndex**  integer | Index number of the rule |
| **unixReadOnly**  boolean | Should fileSystem have read only permission or not  Choices:   - `false` - `true` |
| **unixReadWrite**  boolean | Should fileSystem have read write permission or not  Choices:   - `false` - `true` |
| **feature_flags**  dictionary  added in netapp.aws 21.6.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored.  trace_apis can be set to true to enable tracing, data is written to /tmp/um_apis.log. |
| **quotaInBytes**  integer | Size of the filesystem  Required for create |
| **region**  string / required | The region to which the filesystem belongs to. |
| **secret_key**  string / required | The secret_key to authenticate with the AWSCVS Web Services Proxy or Embedded Web Services API. |
| **serviceLevel**  string | Service Level of a filesystem.  Choices:   - `"standard"` - `"premium"` - `"extreme"` |
| **state**  string / required | Whether the specified fileSystem should exist or not.  Choices:   - `"present"` - `"absent"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_netapp_cvs_filesystems_module.md#id3)

> **Note:**
>
> - The modules prefixed with aws\_cvs\_netapp are built to Manage AWS Cloud Volumes Service .

## [Examples](aws_netapp_cvs_filesystems_module.md#id4)

```yaml+jinja
- name: Create FileSystem
  aws_netapp_cvs_filesystems:
    state: present
    region: us-east-1
    creationToken: newVolume-1
    exportPolicy:
        rules:
          - allowedClients: 172.16.0.4
            cifs: False
            nfsv3: True
            nfsv4: True
            ruleIndex: 1
            unixReadOnly: True
            unixReadWrite: False
    quotaInBytes: 100000000000
    api_url : cds-aws-bundles.netapp.com:8080
    api_key: My_API_Key
    secret_key : My_Secret_Key

- name: Update FileSystem
  aws_netapp_cvs_filesystems:
     state: present
     region: us-east-1
     creationToken: newVolume-1
     exportPolicy:
         rules:
           - allowedClients: 172.16.0.4
             cifs: False
             nfsv3: True
             nfsv4: True
             ruleIndex: 1
             unixReadOnly: True
             unixReadWrite: False
     quotaInBytes: 200000000000
     api_url : cds-aws-bundles.netapp.com:8080
     api_key: My_API_Key
     secret_key : My_Secret_Key

- name: Delete FileSystem
  aws_netapp_cvs_filesystems:
     state: present
     region: us-east-1
     creationToken: newVolume-1
     quotaInBytes: 100000000000
     api_url : cds-aws-bundles.netapp.com:8080
     api_key: My_API_Key
     secret_key : My_Secret_Key
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.aws/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.aws)

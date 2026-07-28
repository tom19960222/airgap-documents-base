---
collection: ansible
version: "8"
title: "netapp.aws.aws_netapp_cvs_snapshots module – NetApp AWS Cloud Volumes Service Manage Snapshots."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/aws/aws_netapp_cvs_snapshots_module.html
fetched_at: 2026-07-28T02:41:00+00:00
---
# netapp.aws.aws_netapp_cvs_snapshots module – NetApp AWS Cloud Volumes Service Manage Snapshots.

> **Note:**
>
> This module is part of the [netapp.aws collection](https://galaxy.ansible.com/ui/repo/published/netapp/aws/) (version 21.7.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.aws`.
>
> To use it in a playbook, specify: `netapp.aws.aws_netapp_cvs_snapshots`.

New in netapp.aws 2.9.0

- [Synopsis](aws_netapp_cvs_snapshots_module.md#synopsis)
- [Parameters](aws_netapp_cvs_snapshots_module.md#parameters)
- [Notes](aws_netapp_cvs_snapshots_module.md#notes)
- [Examples](aws_netapp_cvs_snapshots_module.md#examples)

## [Synopsis](aws_netapp_cvs_snapshots_module.md#id1)

- Create, Update, Delete Snapshot on AWS Cloud Volumes Service.

## [Parameters](aws_netapp_cvs_snapshots_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | The access key to authenticate with the AWSCVS Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the AWSCVS Web Services Proxy or Embedded Web Services API. |
| **feature_flags**  dictionary  *added in netapp.aws 21.6.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored.  trace_apis can be set to true to enable tracing, data is written to /tmp/um_apis.log. |
| **fileSystemId**  string | Name or Id of the filesystem.  Required for create operation |
| **from_name**  string | ID or Name of the snapshot to rename.  Required to create an snapshot called ‘name’ by renaming ‘from_name’. |
| **name**  string / required | Name of the snapshot |
| **region**  string / required | The region to which the snapshot belongs to. |
| **secret_key**  string / required | The secret_key to authenticate with the AWSCVS Web Services Proxy or Embedded Web Services API. |
| **state**  string / required | Whether the specified snapshot should exist or not.  **Choices:**   - `"present"` - `"absent"` |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](aws_netapp_cvs_snapshots_module.md#id3)

> **Note:**
>
> - The modules prefixed with aws\_cvs\_netapp are built to Manage AWS Cloud Volumes Service .

## [Examples](aws_netapp_cvs_snapshots_module.md#id4)

```yaml+jinja
- name: Create Snapshot
  aws_netapp_cvs_snapshots:
    state: present
    region: us-east-1
    name: testSnapshot
    fileSystemId: testVolume
    api_url : cds-aws-bundles.netapp.com
    api_key: myApiKey
    secret_key : mySecretKey

- name: Update Snapshot
  aws_netapp_cvs_snapshots:
    state: present
    region: us-east-1
    name: testSnapshot - renamed
    from_name: testSnapshot
    fileSystemId: testVolume
    api_url : cds-aws-bundles.netapp.com
    api_key: myApiKey
    secret_key : mySecretKey

- name: Delete Snapshot
  aws_netapp_cvs_snapshots:
    state: absent
    region: us-east-1
    name: testSnapshot
    api_url : cds-aws-bundles.netapp.com
    api_key: myApiKey
    secret_key : mySecretKey
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.aws/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.aws)

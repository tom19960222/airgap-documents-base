---
collection: ansible
version: "6"
title: "netapp.storagegrid.na_sg_grid_traffic_classes module – Manage Traffic Classification Policy configuration on StorageGRID."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/storagegrid/na_sg_grid_traffic_classes_module.html
fetched_at: 2026-07-28T00:13:42+00:00
---
# netapp.storagegrid.na_sg_grid_traffic_classes module – Manage Traffic Classification Policy configuration on StorageGRID.

> **Note:**
>
> This module is part of the [netapp.storagegrid collection](https://galaxy.ansible.com/netapp/storagegrid) (version 21.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.storagegrid`.
>
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_grid_traffic_classes`.

New in netapp.storagegrid 21.10.0

- [Synopsis](na_sg_grid_traffic_classes_module.md#synopsis)
- [Parameters](na_sg_grid_traffic_classes_module.md#parameters)
- [Notes](na_sg_grid_traffic_classes_module.md#notes)
- [Examples](na_sg_grid_traffic_classes_module.md#examples)
- [Return Values](na_sg_grid_traffic_classes_module.md#return-values)

## [Synopsis](na_sg_grid_traffic_classes_module.md#id1)

- Create, Update, Delete Traffic Classification Policies on NetApp StorageGRID.

## [Parameters](na_sg_grid_traffic_classes_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **description**  string | Description of the Traffic Classification Policy. |
| **limits**  list / elements=dictionary | Optional limits to impose on client requests matched by this traffic class.  Only one of each limit type can be specified. |
| **type**  string / required | The type of limit to apply.  `aggregateBandwidthIn` - The maximum combined upload bandwidth in bytes/second of all concurrent requests that match this policy.  `aggregateBandwidthOut` - The maximum combined download bandwidth in bytes/second of all concurrent requests that match this policy.  `concurrentReadRequests` - The maximum number of download requests that can be in progress at the same time.  `concurrentWriteRequests` - The maximum number of upload requests that can be in progress at the same time.  `readRequestRate` - The maximum number of download requests that can be started each second.  `writeRequestRate` - The maximum number of download requests that can be started each second.  `perRequestBandwidthIn` - The maximum upload bandwidth in bytes/second allowed for each request that matches this policy.  `perRequestBandwidthOut` - The maximum download bandwidth in bytes/second allowed for each request that matches this policy.  Choices:   - `"aggregateBandwidthIn"` - `"aggregateBandwidthOut"` - `"concurrentReadRequests"` - `"concurrentWriteRequests"` - `"readRequestRate"` - `"writeRequestRate"` - `"perRequestBandwidthIn"` - `"perRequestBandwidthOut"` |
| **value**  integer / required | The limit to apply.  Limit values are type specific. |
| **matchers**  list / elements=dictionary | A set of parameters to match.  The traffic class will match requests where any of these matchers match. |
| **inverse**  boolean | If *true*, entities that match the value are excluded.  Choices:   - `false` ← (default) - `true` |
| **members**  list / elements=string / required | A list of members to match on. |
| **type**  string / required | The attribute of the request to match.  `bucket` - The S3 bucket (or Swift container) being accessed.  `bucket-regex` - A regular expression to evaluate against the S3 bucket (or Swift container) being accessed.  `cidr` - Matches if the client request source IP is in the specified IPv4 CIDR (RFC4632).  `tenant` - Matches if the S3 bucket (or Swift container) is owned by the tenant account with this ID.  Choices:   - `"bucket"` - `"bucket-regex"` - `"cidr"` - `"endpoint"` - `"tenant"` |
| **name**  string | Name of the Traffic Classification Policy. |
| **policy_id**  string | Traffic Classification Policy ID.  May be used for modify or delete operation. |
| **state**  string | Whether the specified Traffic Classification Policy should exist.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_sg_grid_traffic_classes_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_grid_traffic_classes_module.md#id4)

```yaml+jinja
- name: create Traffic Classification Policy with bandwidth limit on buckets
  netapp.storagegrid.na_sg_grid_traffic_classes:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    name: Traffic-Policy1
    matchers:
      - type: bucket
        members: bucket1,anotherbucket
    limits:
      - type: aggregateBandwidthOut
        value: 100000000

- name: create Traffic Classification Policy with bandwidth limits except for specific tenant account
  netapp.storagegrid.na_sg_grid_traffic_classes:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    name: Fabricpool-Policy
    description: "Limit all to 500MB/s except FabricPool tenant"
    matchers:
      - type: tenant
        inverse: True
        members: 12345678901234567890
    limits:
      - type: aggregateBandwidthIn
        value: 50000000
      - type: aggregateBandwidthOut
        value: 50000000

- name: rename Traffic Classification Policy
  netapp.storagegrid.na_sg_grid_traffic_classes:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    policy_id: 00000000-0000-0000-0000-000000000000
    name: Traffic-Policy1-New-Name
    matchers:
      - type: bucket
        members: bucket1,anotherbucket
    limits:
      - type: aggregateBandwidthOut
        value: 100000000

- name: delete Traffic Classification Policy
  netapp.storagegrid.na_sg_grid_traffic_classes:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: absent
    name: Traffic-Policy1
```

## [Return Values](na_sg_grid_traffic_classes_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  dictionary | Returns information about the StorageGRID Traffic Classification Policy.  Returned: success  Sample: `{"description": "Traffic Classification Policy 1", "id": "6b2946e6-7fed-40d0-9262-8e922580aba7", "limits": [{"type": "aggregateBandwidthOut", "value": 100000000}], "matchers": [{"inverse": false, "members": ["192.168.50.0/24"], "type": "cidr"}, {"inverse": false, "members": ["mybucket1", "mybucket2"], "type": "bucket"}], "name": "Traffic-Policy1"}` |

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)

---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_image_store module – Manages CloudStack Image Stores."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_image_store_module.html
fetched_at: 2026-07-28T00:15:28+00:00
---
# ngine_io.cloudstack.cs_image_store module – Manages CloudStack Image Stores.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ngine_io/cloudstack) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_image_store_module.md#ansible-collections-ngine-io-cloudstack-cs-image-store-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_image_store`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_image_store_module.md#synopsis)
- [Requirements](cs_image_store_module.md#requirements)
- [Parameters](cs_image_store_module.md#parameters)
- [Notes](cs_image_store_module.md#notes)
- [Examples](cs_image_store_module.md#examples)
- [Return Values](cs_image_store_module.md#return-values)

## [Synopsis](cs_image_store_module.md#id1)

- Deploy, remove, recreate CloudStack Image Stores.

## [Requirements](cs_image_store_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_image_store_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **force_recreate**  boolean | Set to `yes` if you’re changing an existing Image Store.  This will force the recreation of the Image Store.  Recreation might fail if there are snapshots present on the Image Store. Delete them before running the recreation.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | The ID of the Image Store. Required when deleting a Image Store. |
| **provider**  string | The image store provider name. Required when creating a new Image Store |
| **state**  string | Stage of the Image Store  Choices:   - `"present"` ← (default) - `"absent"` |
| **url**  string | The URL for the Image Store.  Required when *state=present*. |
| **zone**  string / required | The Zone name for the Image Store. |

## [Notes](cs_image_store_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_image_store_module.md#id5)

```yaml+jinja
- name: Add a Image Store (NFS)
  ngine_io.cloudstack.cs_image_store:
    zone: zone-01
    name: nfs-01
    provider: NFS
    url: nfs://192.168.21.16/exports/secondary

# Change the NFS share URL and force a Image Store recreation
- name: Change the NFS url
  ngine_io.cloudstack.cs_image_store:
    zone: zone-01
    name: nfs-01
    provider: NFS
    force_recreate: yes
    url: nfs://192.168.21.10/shares/secondary

- name: delete the image store
  ngine_io.cloudstack.cs_image_store:
    name: nfs-01
    zone: zone-01
    state: absent
```

## [Return Values](cs_image_store_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | the ID of the image store  Returned: success  Sample: `"feb11a84-a093-45eb-b84d-7f680313c40b"` |
| **name**  string | the name of the image store  Returned: success  Sample: `"nfs-01"` |
| **protocol**  string | the protocol of the image store  Returned: success  Sample: `"nfs"` |
| **provider_name**  string | the provider name of the image store  Returned: success  Sample: `"NFS"` |
| **scope**  string | the scope of the image store  Returned: success  Sample: `"ZONE"` |
| **url**  string | the url of the image store  Returned: success  Sample: `"nfs://192.168.21.16/exports/secondary"` |
| **zone**  string | the Zone name of the image store  Returned: success  Sample: `"zone-01"` |

### Authors

- Patryk Cichy (@PatTheSilent)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)

---
collection: ansible
version: "6"
title: "openstack.cloud.volume_info module – Retrive information about volumes"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/volume_info_module.html
fetched_at: 2026-07-28T00:17:15+00:00
---
# openstack.cloud.volume_info module – Retrive information about volumes

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/openstack/cloud) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](volume_info_module.md#ansible-collections-openstack-cloud-volume-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.volume_info`.

- [Synopsis](volume_info_module.md#synopsis)
- [Requirements](volume_info_module.md#requirements)
- [Parameters](volume_info_module.md#parameters)
- [Notes](volume_info_module.md#notes)
- [Examples](volume_info_module.md#examples)
- [Return Values](volume_info_module.md#return-values)

## [Synopsis](volume_info_module.md#id1)

- Get information about block storage in openstack

## [Requirements](volume_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](volume_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **all_projects**  boolean | Whether return the volumes in all projects  Choices:   - `false` - `true` |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **details**  boolean | Whether to provide additional information about volumes  Choices:   - `false` - `true` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string | Name of the volume as a string. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **status**  string | Value of the status of the volume so that you can filter on “available” for example |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](volume_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](volume_info_module.md#id5)

```yaml+jinja
- openstack.cloud.volume_info:

- openstack.cloud.volume_info:
    name: myvolume

- openstack.cloud.volume_info:
    all_projects: true

- openstack.cloud.volume_info:
    all_projects: true
    details: true
```

## [Return Values](volume_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **volumes**  list / elements=dictionary | Volumes in project  Returned: always  Sample: `[{"attachments": [], "availability_zone": "nova", "consistency_group_id": null, "created_at": "2017-11-15T10:51:19.000000", "description": "", "extended_replication_status": null, "host": null, "id": "103ac6ed-527f-4781-8484-7ff4467e34f5", "image_id": null, "is_bootable": true, "is_encrypted": false, "links": [{"href": "https://...", "rel": "self"}, {"href": "https://...", "rel": "bookmark"}], "location": {"cloud": "cloud", "project": {"domain_id": null, "domain_name": "Default", "id": "cfe04702154742fc964d9403c691c76e", "name": "username"}, "region_name": "regionOne", "zone": "nova"}, "metadata": {"readonly": "False"}, "migration_id": null, "migration_status": null, "name": "", "project_id": "cab34702154a42fc96ed9403c691c76e", "replication_driver_data": null, "replication_status": "disabled", "size": 9, "snapshot_id": null, "source_volume_id": null, "status": "available", "volume_image_metadata": {"checksum": "a14e113deeee3a3392462f167ed28cb5", "container_format": "bare", "disk_format": "raw", "family": "centos-7", "image_id": "afcf3320-1bf8-4a9a-a24d-5abd639a6e33", "image_name": "CentOS-7-x86_64-GenericCloud-1708", "latest": "centos-7-latest", "min_disk": "0", "min_ram": "0", "official": "True", "official-image": "True", "size": "8589934592"}, "volume_type": null}]` |

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

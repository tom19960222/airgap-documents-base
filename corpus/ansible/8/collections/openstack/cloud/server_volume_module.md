---
collection: ansible
version: "8"
title: "openstack.cloud.server_volume module – Attach/Detach Volumes from OpenStack VM’s"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/server_volume_module.html
fetched_at: 2026-07-28T02:48:52+00:00
---
# openstack.cloud.server_volume module – Attach/Detach Volumes from OpenStack VM’s

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/ui/repo/published/openstack/cloud/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](server_volume_module.md#ansible-collections-openstack-cloud-server-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.server_volume`.

- [Synopsis](server_volume_module.md#synopsis)
- [Requirements](server_volume_module.md#requirements)
- [Parameters](server_volume_module.md#parameters)
- [Notes](server_volume_module.md#notes)
- [Examples](server_volume_module.md#examples)
- [Return Values](server_volume_module.md#return-values)

## [Synopsis](server_volume_module.md#id1)

- Attach or Detach volumes from OpenStack VM’s

## [Requirements](server_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](server_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **device**  string | Device you want to attach. Defaults to auto finding a device name. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **server**  string / required | Name or ID of server you want to attach a volume to |
| **state**  string | Should the resource be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **volume**  string / required | Name or id of volume you want to attach to a server |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](server_volume_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](server_volume_module.md#id5)

```yaml+jinja
- name: Attaches a volume to a compute host
  openstack.cloud.server_volume:
    state: present
    cloud: mordred
    server: Mysql-server
    volume: mysql-data
    device: /dev/vdb
```

## [Return Values](server_volume_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **volume**  dictionary | Volume that was just attached  **Returned:** On success when *state* is present |
| **attachments**  list / elements=string | Instance attachment information. If this volume is attached to a server instance, the attachments list includes the UUID of the attached server, an attachment UUID, the name of the attached host, if any, the volume UUID, the device, and the device UUID. Otherwise, this list is empty.  **Returned:** success |
| **availability_zone**  string | The name of the availability zone.  **Returned:** success |
| **consistency_group_id**  string | The UUID of the consistency group.  **Returned:** success |
| **created_at**  string | The date and time when the resource was created.  **Returned:** success |
| **description**  string | The volume description.  **Returned:** success |
| **extended_replication_status**  string | Extended replication status on this volume.  **Returned:** success |
| **group_id**  string | The ID of the group.  **Returned:** success |
| **host**  string | The volume’s current back-end.  **Returned:** success |
| **id**  string | The UUID of the volume.  **Returned:** success |
| **image_id**  string | Image on which the volume was based  **Returned:** success |
| **is_bootable**  string | Enables or disables the bootable attribute. You can boot an instance from a bootable volume.  **Returned:** success |
| **is_encrypted**  boolean | If true, this volume is encrypted.  **Returned:** success |
| **metadata**  dictionary | A metadata object. Contains one or more metadata key and value pairs that are associated with the volume.  **Returned:** success |
| **migration_id**  string | The volume ID that this volume name on the backend is based on.  **Returned:** success |
| **migration_status**  string | The status of this volume migration (None means that a migration is not currently in progress).  **Returned:** success |
| **name**  string | The volume name.  **Returned:** success |
| **project_id**  string | The project ID which the volume belongs to.  **Returned:** success |
| **replication_driver_data**  string | Data set by the replication driver  **Returned:** success |
| **replication_status**  string | The volume replication status.  **Returned:** success |
| **scheduler_hints**  dictionary | Scheduler hints for the volume  **Returned:** success |
| **size**  integer | The size of the volume, in gibibytes (GiB).  **Returned:** success |
| **snapshot_id**  string | To create a volume from an existing snapshot, specify the UUID of the volume snapshot. The volume is created in same availability zone and with same size as the snapshot.  **Returned:** success |
| **source_volume_id**  string | The UUID of the source volume. The API creates a new volume with the same size as the source volume unless a larger size is requested.  **Returned:** success |
| **status**  string | The volume status.  **Returned:** success |
| **updated_at**  string | The date and time when the resource was updated.  **Returned:** success |
| **user_id**  string | The UUID of the user.  **Returned:** success |
| **volume_image_metadata**  dictionary | List of image metadata entries. Only included for volumes that were created from an image, or from a snapshot of a volume originally created from an image.  **Returned:** success |
| **volume_type**  string | The associated volume type name for the volume.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

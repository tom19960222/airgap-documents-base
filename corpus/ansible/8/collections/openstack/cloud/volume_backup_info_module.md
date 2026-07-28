---
collection: ansible
version: "8"
title: "openstack.cloud.volume_backup_info module – Get Backups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/volume_backup_info_module.html
fetched_at: 2026-07-28T02:49:03+00:00
---
# openstack.cloud.volume_backup_info module – Get Backups

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
> see [Requirements](volume_backup_info_module.md#ansible-collections-openstack-cloud-volume-backup-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.volume_backup_info`.

- [Synopsis](volume_backup_info_module.md#synopsis)
- [Requirements](volume_backup_info_module.md#requirements)
- [Parameters](volume_backup_info_module.md#parameters)
- [Notes](volume_backup_info_module.md#notes)
- [Examples](volume_backup_info_module.md#examples)
- [Return Values](volume_backup_info_module.md#return-values)

## [Synopsis](volume_backup_info_module.md#id1)

- Get Backup info from the Openstack cloud.

## [Requirements](volume_backup_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](volume_backup_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string | Name of the Backup. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **volume**  string | Name or ID of the volume. |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](volume_backup_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](volume_backup_info_module.md#id5)

```yaml+jinja
- name: Get all backups
  openstack.cloud.volume_backup_info:

- name: Get backup 'my_fake_backup'
  openstack.cloud.volume_backup_info:
    name: my_fake_backup
```

## [Return Values](volume_backup_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **volume_backups**  list / elements=dictionary | List of dictionaries describing volume backups.  **Returned:** always. |
| **availability_zone**  string | Backup availability zone.  **Returned:** success |
| **container**  string | The container name.  **Returned:** success |
| **created_at**  string | Backup creation time.  **Returned:** success |
| **data_timestamp**  string | The time when the data on the volume was first saved. If it is a backup from volume, it will be the same as `created_at` for a backup. If it is a backup from a snapshot, it will be the same as created_at for the snapshot.  **Returned:** success |
| **description**  string | Backup desciption.  **Returned:** success |
| **fail_reason**  string | Backup fail reason.  **Returned:** success |
| **force**  boolean | Force backup.  **Returned:** success |
| **has_dependent_backups**  boolean | If this value is true, there are other backups depending on this backup.  **Returned:** success |
| **id**  string | Unique UUID.  **Returned:** success  **Sample:** `"39007a7e-ee4f-4d13-8283-b4da2e037c69"` |
| **is_incremental**  boolean | Backup incremental property.  **Returned:** success |
| **links**  list / elements=string | A list of links associated with this volume.  **Returned:** success |
| **metadata**  dictionary | Backup metadata.  **Returned:** success |
| **name**  string | Backup Name.  **Returned:** success |
| **object_count**  integer | backup object count.  **Returned:** success |
| **project_id**  string | The UUID of the owning project.  **Returned:** success |
| **size**  integer | The size of the volume, in gibibytes (GiB).  **Returned:** success |
| **snapshot_id**  string | Snapshot ID.  **Returned:** success |
| **status**  string | Backup status.  **Returned:** success |
| **updated_at**  string | Backup update time.  **Returned:** success |
| **user_id**  string | The UUID of the project owner.  **Returned:** success |
| **volume_id**  string | Volume ID.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

---
collection: ansible
version: "6"
title: "openstack.cloud.volume_snapshot module – Create/Delete Cinder Volume Snapshots"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/volume_snapshot_module.html
fetched_at: 2026-07-28T00:17:16+00:00
---
# openstack.cloud.volume_snapshot module – Create/Delete Cinder Volume Snapshots

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
> see [Requirements](volume_snapshot_module.md#ansible-collections-openstack-cloud-volume-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.volume_snapshot`.

- [Synopsis](volume_snapshot_module.md#synopsis)
- [Requirements](volume_snapshot_module.md#requirements)
- [Parameters](volume_snapshot_module.md#parameters)
- [Notes](volume_snapshot_module.md#notes)
- [Examples](volume_snapshot_module.md#examples)
- [Return Values](volume_snapshot_module.md#return-values)

## [Synopsis](volume_snapshot_module.md#id1)

- Create or Delete cinder block storage volume snapshots

## [Requirements](volume_snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](volume_snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **display_description**  aliases: description  string | String describing the snapshot |
| **display_name**  aliases: name  string / required | Name of the snapshot |
| **force**  boolean | Allows or disallows snapshot of a volume to be created when the volume is attached to an instance.  Choices:   - `false` ← (default) - `true` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **volume**  string / required | The volume name or id to create/delete the snapshot |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](volume_snapshot_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](volume_snapshot_module.md#id5)

```yaml+jinja
# Creates a snapshot on volume 'test_volume'
- name: create and delete snapshot
  hosts: localhost
  tasks:
  - name: create snapshot
    openstack.cloud.volume_snapshot:
      state: present
      cloud: mordred
      availability_zone: az2
      display_name: test_snapshot
      volume: test_volume
  - name: delete snapshot
    openstack.cloud.volume_snapshot:
      state: absent
      cloud: mordred
      availability_zone: az2
      display_name: test_snapshot
      volume: test_volume
```

## [Return Values](volume_snapshot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **snapshot**  dictionary | The snapshot instance after the change  Returned: success  Sample: `{"display_name": "test_snapshot", "id": "837aca54-c0ee-47a2-bf9a-35e1b4fdac0c", "name": "test_snapshot", "size": 2, "status": "available", "volume_id": "ec646a7c-6a35-4857-b38b-808105a24be6"}` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

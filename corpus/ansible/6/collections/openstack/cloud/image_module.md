---
collection: ansible
version: "6"
title: "openstack.cloud.image module – Add/Delete images from OpenStack Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/image_module.html
fetched_at: 2026-07-28T00:16:44+00:00
---
# openstack.cloud.image module – Add/Delete images from OpenStack Cloud

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
> see [Requirements](image_module.md#ansible-collections-openstack-cloud-image-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.image`.

- [Synopsis](image_module.md#synopsis)
- [Requirements](image_module.md#requirements)
- [Parameters](image_module.md#parameters)
- [Notes](image_module.md#notes)
- [Examples](image_module.md#examples)

## [Synopsis](image_module.md#id1)

- Add or Remove images from the OpenStack Image Repository

## [Requirements](image_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](image_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **checksum**  string | The checksum of the image |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **container_format**  string | The format of the container  Choices:   - `"ami"` - `"aki"` - `"ari"` - `"bare"` ← (default) - `"ovf"` - `"ova"` - `"docker"` |
| **disk_format**  string | The format of the disk that is getting uploaded  Choices:   - `"ami"` - `"ari"` - `"aki"` - `"vhd"` - `"vmdk"` - `"raw"` - `"qcow2"` ← (default) - `"vdi"` - `"iso"` - `"vhdx"` - `"ploop"` |
| **filename**  string | The path to the file which has to be uploaded |
| **id**  string | The ID of the image when uploading an image |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **is_public**  boolean | Whether the image can be accessed publicly. Note that publicizing an image requires admin role by default.  Choices:   - `false` ← (default) - `true` |
| **kernel**  string | The name of an existing kernel image that will be associated with this image |
| **min_disk**  integer | The minimum disk space (in GB) required to boot this image |
| **min_ram**  integer | The minimum ram (in MB) required to boot this image |
| **name**  string / required | The name of the image when uploading - or the name/ID of the image if deleting |
| **project**  aliases: owner  string | The name or ID of the project owning the image |
| **project_domain**  string | The domain the project owning the image belongs to  May be used to identify a unique project when providing a name to the project argument and multiple projects with such name exist |
| **properties**  dictionary | Additional properties to be associated with this image  Default: `{}` |
| **protected**  boolean | Prevent image from being deleted  Choices:   - `false` ← (default) - `true` |
| **ramdisk**  string | The name of an existing ramdisk image that will be associated with this image |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | List of tags to be applied to the image  Default: `[]` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **volume**  string | ID of a volume to create an image from.  The volume must be in AVAILABLE state. |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](image_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](image_module.md#id5)

```yaml+jinja
# Upload an image from a local file named cirros-0.3.0-x86_64-disk.img
- openstack.cloud.image:
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: passme
      project_name: admin
      openstack.cloud.identity_user_domain_name: Default
      openstack.cloud.project_domain_name: Default
    name: cirros
    container_format: bare
    disk_format: qcow2
    state: present
    filename: cirros-0.3.0-x86_64-disk.img
    kernel: cirros-vmlinuz
    ramdisk: cirros-initrd
    tags:
      - custom
    properties:
      cpu_arch: x86_64
      distro: ubuntu

# Create image from volume attached to an instance
- name: create volume snapshot
  openstack.cloud.volume_snapshot:
    auth:
      "{{ auth }}"
    display_name: myvol_snapshot
    volume: myvol
    force: yes
  register: myvol_snapshot

- name: create volume from snapshot
  openstack.cloud.volume:
    auth:
      "{{ auth }}"
    size: "{{ myvol_snapshot.snapshot.size }}"
    snapshot_id: "{{ myvol_snapshot.snapshot.id }}"
    display_name: myvol_snapshot_volume
    wait: yes
  register: myvol_snapshot_volume

- name: create image from volume snapshot
  openstack.cloud.image:
    auth:
      "{{ auth }}"
    volume: "{{ myvol_snapshot_volume.volume.id }}"
    name: myvol_image
```

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

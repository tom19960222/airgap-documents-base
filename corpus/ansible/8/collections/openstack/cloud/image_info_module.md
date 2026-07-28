---
collection: ansible
version: "8"
title: "openstack.cloud.image_info module – Fetch images from OpenStack image (Glance) service."
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/image_info_module.html
fetched_at: 2026-07-28T02:48:01+00:00
---
# openstack.cloud.image_info module – Fetch images from OpenStack image (Glance) service.

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
> see [Requirements](image_info_module.md#ansible-collections-openstack-cloud-image-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.image_info`.

- [Synopsis](image_info_module.md#synopsis)
- [Requirements](image_info_module.md#requirements)
- [Parameters](image_info_module.md#parameters)
- [Notes](image_info_module.md#notes)
- [Examples](image_info_module.md#examples)
- [Return Values](image_info_module.md#return-values)

## [Synopsis](image_info_module.md#id1)

- Fetch images from OpenStack image (Glance) service.

## [Requirements](image_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](image_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **filters**  aliases: properties  dictionary | Dict of properties of the images used for query |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  aliases: image  string | Name or ID of the image |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](image_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](image_info_module.md#id5)

```yaml+jinja
- name: Gather previously created image named image1
  openstack.cloud.image_info:
    cloud: devstack-admin
    image: image1

- name: List all images
  openstack.cloud.image_info:

- name: Retrieve and filter images
  openstack.cloud.image_info:
    filters:
      is_protected: False
```

## [Return Values](image_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **images**  list / elements=dictionary | List of dictionaries describing matching images.  **Returned:** always |
| **architecture**  string | The CPU architecture that must be supported by the hypervisor.  **Returned:** success |
| **checksum**  string | Checksum for the image.  **Returned:** success |
| **container_format**  string | Container format of the image.  **Returned:** success |
| **created_at**  string | Image created at timestamp.  **Returned:** success |
| **direct_url**  string | URL to access the image file kept in external store.  **Returned:** success |
| **disk_format**  string | Disk format of the image.  **Returned:** success |
| **file**  string | The URL for the virtual machine image file.  **Returned:** success |
| **filters**  dictionary | Additional properties associated with the image.  **Returned:** success |
| **has_auto_disk_config**  boolean | If root partition on disk is automatically resized before the instance boots.  **Returned:** success |
| **hash_algo**  string | The algorithm used to compute a secure hash of the image data.  **Returned:** success |
| **hash_value**  string | The hexdigest of the secure hash of the image data computed using the algorithm whose name is the value of the os_hash_algo property.  **Returned:** success |
| **hw_cpu_cores**  string | Used to pin the virtual CPUs (vCPUs) of instances to the host’s physical CPU cores (pCPUs).  **Returned:** success |
| **hw_cpu_policy**  string | The hexdigest of the secure hash of the image data.  **Returned:** success |
| **hw_cpu_sockets**  string | Preferred number of sockets to expose to the guest.  **Returned:** success |
| **hw_cpu_thread_policy**  string | Defines how hardware CPU threads in a simultaneous multithreading-based (SMT) architecture be used.  **Returned:** success |
| **hw_cpu_threads**  string | The preferred number of threads to expose to the guest.  **Returned:** success |
| **hw_disk_bus**  string | Specifies the type of disk controller to attach disk devices to.  **Returned:** success |
| **hw_machine_type**  string | Enables booting an ARM system using the specified machine type.  **Returned:** success |
| **hw_qemu_guest_agent**  string | A string boolean, which if ‘true’, QEMU guest agent will be exposed to the instance.  **Returned:** success |
| **hw_rng_model**  string | Adds a random-number generator device to the image’s instances.  **Returned:** success |
| **hw_scsi_model**  string | Enables the use of VirtIO SCSI (virtio-scsi) to provide block device access for compute instances.  **Returned:** success |
| **hw_video_model**  string | The video image driver used.  **Returned:** success |
| **hw_video_ram**  string | Maximum RAM for the video image.  **Returned:** success |
| **hw_vif_model**  string | Specifies the model of virtual network interface device to use.  **Returned:** success |
| **hw_watchdog_action**  string | Enables a virtual hardware watchdog device that carries out the specified action if the server hangs.  **Returned:** success |
| **hypervisor_type**  string | The hypervisor type.  **Returned:** success |
| **id**  string | Unique UUID.  **Returned:** success |
| **instance_type_rxtx_factor**  string | Optional property allows created servers to have a different bandwidth cap than that defined in the network they are attached to.  **Returned:** success |
| **instance_uuid**  string | For snapshot images, this is the UUID of the server used to create this image.  **Returned:** success |
| **is_hidden**  boolean | Controls whether an image is displayed in the default image-list response  **Returned:** success |
| **is_hw_boot_menu_enabled**  boolean | Enables the BIOS bootmenu.  **Returned:** success |
| **is_hw_vif_multiqueue_enabled**  boolean | Enables the virtio-net multiqueue feature.  **Returned:** success |
| **is_protected**  boolean | Image protected flag.  **Returned:** success |
| **kernel_id**  string | The ID of an image stored in the Image service that should be used as the kernel when booting an AMI-style image.  **Returned:** success |
| **locations**  string | A list of URLs to access the image file in external store.  **Returned:** success |
| **metadata**  string | The location metadata.  **Returned:** success |
| **min_disk**  integer | Min amount of disk space required for this image.  **Returned:** success |
| **min_ram**  integer | Min amount of RAM required for this image.  **Returned:** success |
| **name**  string | Name given to the image.  **Returned:** success |
| **needs_config_drive**  boolean | Specifies whether the image needs a config drive.  **Returned:** success |
| **needs_secure_boot**  boolean | Whether Secure Boot is needed.  **Returned:** success |
| **os_admin_user**  string | The operating system admin username.  **Returned:** success |
| **os_command_line**  string | The kernel command line to be used by libvirt driver.  **Returned:** success |
| **os_distro**  string | The common name of the operating system distribution in lowercase.  **Returned:** success |
| **os_require_quiesce**  string | If true, require quiesce on snapshot via QEMU guest agent.  **Returned:** success |
| **os_shutdown_timeout**  string | Time for graceful shutdown.  **Returned:** success |
| **os_type**  string | The operating system installed on the image.  **Returned:** success |
| **os_version**  string | The operating system version as specified by the distributor.  **Returned:** success |
| **owner**  string | Owner for the image.  **Returned:** success |
| **owner_id**  string | The ID of the owner, or project, of the image.  **Returned:** success |
| **ramdisk_id**  string | The ID of image stored in the Image service that should be used as the ramdisk when booting an AMI-style image.  **Returned:** success |
| **schema**  string | URL for the schema describing a virtual machine image.  **Returned:** success |
| **size**  integer | Size of the image.  **Returned:** success |
| **status**  string | Image status.  **Returned:** success |
| **store**  string | Glance will attempt to store the disk image data in the backing store indicated by the value of the header.  **Returned:** success |
| **tags**  list / elements=string | List of tags assigned to the image  **Returned:** success |
| **updated_at**  string | Image updated at timestamp.  **Returned:** success |
| **url**  string | URL to access the image file kept in external store.  **Returned:** success |
| **virtual_size**  string | The virtual size of the image.  **Returned:** success |
| **visibility**  string | Indicates who has access to the image.  **Returned:** success |
| **vm_mode**  string | The virtual machine mode.  **Returned:** success |
| **vmware_adaptertype**  string | The virtual SCSI or IDE controller used by the hypervisor.  **Returned:** success |
| **vmware_ostype**  string | Operating system installed in the image.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

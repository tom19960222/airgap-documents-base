---
collection: ansible
version: "6"
title: "openstack.cloud.image_info module – Retrieve information about an image within OpenStack."
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/image_info_module.html
fetched_at: 2026-07-28T00:16:44+00:00
---
# openstack.cloud.image_info module – Retrieve information about an image within OpenStack.

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

- Retrieve information about a image image from OpenStack.
- This module was called `openstack.cloud.image_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [openstack.cloud.image_info](image_info_module.md#ansible-collections-openstack-cloud-image-info-module) module no longer returns `ansible_facts`!

## [Requirements](image_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](image_info_module.md#id3)

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
| **filters**  aliases: properties  dictionary | Dict of properties of the images used for query |
| **image**  string | Name or ID of the image |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](image_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](image_info_module.md#id5)

```yaml+jinja
- name: Gather information about a previously created image named image1
  openstack.cloud.image_info:
    auth:
      auth_url: https://identity.example.com
      username: user
      password: password
      project_name: someproject
    image: image1
  register: result

- name: Show openstack information
  debug:
    msg: "{{ result.image }}"

# Show all available Openstack images
- name: Retrieve all available Openstack images
  openstack.cloud.image_info:
  register: result

- name: Show images
  debug:
    msg: "{{ result.image }}"

# Show images matching requested properties
- name: Retrieve images having properties with desired values
  openstack.cloud.image_facts:
    filters:
      some_property: some_value
      OtherProp: OtherVal

- name: Show images
  debug:
    msg: "{{ result.image }}"
```

## [Return Values](image_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **openstack_images**  complex | has all the openstack information about the image  Returned: always, but can be null |
| **checksum**  string | Checksum for the image.  Returned: success |
| **container_format**  string | Container format of the image.  Returned: success |
| **created_at**  string | Image created at timestamp.  Returned: success |
| **direct_url**  string | URL to access the image file kept in external store.  Returned: success |
| **disk_format**  string | Disk format of the image.  Returned: success |
| **file**  string | The URL for the virtual machine image file.  Returned: success |
| **id**  string | Unique UUID.  Returned: success |
| **is_protected**  boolean | Image protected flag.  Returned: success |
| **locations**  string | A list of URLs to access the image file in external store.  Returned: success |
| **metadata**  string | The location metadata.  Returned: success |
| **min_disk**  integer | Min amount of disk space required for this image.  Returned: success |
| **min_ram**  integer | Min amount of RAM required for this image.  Returned: success |
| **name**  string | Name given to the image.  Returned: success |
| **os_hidden**  boolean | Controls whether an image is displayed in the default image-list response  Returned: success |
| **owner**  string | Owner for the image.  Returned: success |
| **schema**  string | URL for the schema describing a virtual machine image.  Returned: success |
| **size**  integer | Size of the image.  Returned: success |
| **status**  string | Image status.  Returned: success |
| **tags**  list / elements=string | List of tags assigned to the image  Returned: success |
| **updated_at**  string | Image updated at timestamp.  Returned: success |
| **virtual_size**  string | The virtual size of the image.  Returned: success |
| **visibility**  string | Indicates who has access to the image.  Returned: success |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

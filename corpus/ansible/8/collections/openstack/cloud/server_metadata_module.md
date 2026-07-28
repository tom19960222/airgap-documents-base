---
collection: ansible
version: "8"
title: "openstack.cloud.server_metadata module – Add/Update/Delete Metadata in Compute Instances from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/server_metadata_module.html
fetched_at: 2026-07-28T02:48:51+00:00
---
# openstack.cloud.server_metadata module – Add/Update/Delete Metadata in Compute Instances from OpenStack

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
> see [Requirements](server_metadata_module.md#ansible-collections-openstack-cloud-server-metadata-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.server_metadata`.

- [Synopsis](server_metadata_module.md#synopsis)
- [Requirements](server_metadata_module.md#requirements)
- [Parameters](server_metadata_module.md#parameters)
- [Notes](server_metadata_module.md#notes)
- [Examples](server_metadata_module.md#examples)
- [Return Values](server_metadata_module.md#return-values)

## [Synopsis](server_metadata_module.md#id1)

- Add, Update or Remove metadata in compute instances from OpenStack.

## [Requirements](server_metadata_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](server_metadata_module.md#id3)

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
| **metadata**  aliases: meta  dictionary / required | A list of key value pairs that should be provided as a metadata to the instance or a string containing a list of key-value pairs. Eg: meta: “key1=value1,key2=value2”  Note that when *state* is `true`, metadata already existing on the server will not be cleared. |
| **name**  aliases: server  string / required | Name of the instance to update the metadata |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](server_metadata_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](server_metadata_module.md#id5)

```yaml+jinja
# Creates or updates hostname=test1 as metadata of the server instance vm1
# Note that existing keys will not be cleared
- name: add metadata to instance
  openstack.cloud.server_metadata:
      state: present
      cloud: "{{ cloud }}"
      name: vm1
      metadata:
          hostname: test1
          group: group1

# Removes the keys under meta from the instance named vm1
- name: delete metadata from instance
  openstack.cloud.server_metadata:
        state: absent
        cloud: "{{ cloud }}"
        name: vm1
        meta:
            hostname:
            group:
            public_keys:
```

## [Return Values](server_metadata_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **server**  dictionary | Dictionary describing the server that was updated.  **Returned:** On success when *state* is ‘present’. |
| **access_ipv4**  string | IPv4 address that should be used to access this server. May be automatically set by the provider.  **Returned:** success |
| **access_ipv6**  string | IPv6 address that should be used to access this server. May be automatically set by the provider.  **Returned:** success |
| **addresses**  dictionary | A dictionary of addresses this server can be accessed through. The dictionary contains keys such as ‘private’ and ‘public’, each containing a list of dictionaries for addresses of that type. The addresses are contained in a dictionary with keys ‘addr’ and ‘version’, which is either 4 or 6 depending on the protocol of the IP address.  **Returned:** success |
| **admin_password**  string | When a server is first created, it provides the administrator password.  **Returned:** success |
| **attached_volumes**  list / elements=string | A list of an attached volumes. Each item in the list contains at least an ‘id’ key to identify the specific volumes.  **Returned:** success |
| **availability_zone**  string | The name of the availability zone this server is a part of.  **Returned:** success |
| **block_device_mapping**  string | Enables fine grained control of the block device mapping for an instance. This is typically used for booting servers from volumes.  **Returned:** success |
| **compute_host**  string | The name of the compute host on which this instance is running. Appears in the response for administrative users only.  **Returned:** success |
| **config_drive**  string | Indicates whether or not a config drive was used for this server.  **Returned:** success |
| **created_at**  string | Timestamp of when the server was created.  **Returned:** success |
| **description**  string | The description of the server. Before microversion 2.19 this was set to the server name.  **Returned:** success |
| **disk_config**  string | The disk configuration. Either AUTO or MANUAL.  **Returned:** success |
| **flavor**  dictionary | The flavor property as returned from server.  **Returned:** success |
| **flavor_id**  string | The flavor reference, as a ID or full URL, for the flavor to use for this server.  **Returned:** success |
| **has_config_drive**  string | Indicates whether a configuration drive enables metadata injection. Not all cloud providers enable this feature.  **Returned:** success |
| **host_id**  string | An ID representing the host of this server.  **Returned:** success |
| **host_status**  string | The host status.  **Returned:** success |
| **hostname**  string | The hostname set on the instance when it is booted. By default, it appears in the response for administrative users only.  **Returned:** success |
| **hypervisor_hostname**  string | The hypervisor host name. Appears in the response for administrative users only.  **Returned:** success |
| **id**  string | ID of the server.  **Returned:** success |
| **image**  dictionary | The image property as returned from server.  **Returned:** success |
| **image_id**  string | The image reference, as a ID or full URL, for the image to use for this server.  **Returned:** success |
| **instance_name**  string | The instance name. The Compute API generates the instance name from the instance name template. Appears in the response for administrative users only.  **Returned:** success |
| **is_locked**  boolean | The locked status of the server  **Returned:** success |
| **kernel_id**  string | The UUID of the kernel image when using an AMI. Will be null if not. By default, it appears in the response for administrative users only.  **Returned:** success |
| **key_name**  string | The name of an associated keypair.  **Returned:** success |
| **launch_index**  integer | When servers are launched via multiple create, this is the sequence in which the servers were launched. By default, it appears in the response for administrative users only.  **Returned:** success |
| **launched_at**  string | The timestamp when the server was launched.  **Returned:** success |
| **links**  string | A list of dictionaries holding links relevant to this server.  **Returned:** success |
| **max_count**  string | The maximum number of servers to create.  **Returned:** success |
| **metadata**  dictionary | List of tag strings.  **Returned:** success |
| **min_count**  string | The minimum number of servers to create.  **Returned:** success |
| **name**  string | Name of the server  **Returned:** success |
| **networks**  string | A networks object. Required parameter when there are multiple networks defined for the tenant. When you do not specify the networks parameter, the server attaches to the only network created for the current tenant.  **Returned:** success |
| **power_state**  string | The power state of this server.  **Returned:** success |
| **progress**  integer | While the server is building, this value represents the percentage of completion. Once it is completed, it will be 100.  **Returned:** success |
| **project_id**  string | The ID of the project this server is associated with.  **Returned:** success |
| **ramdisk_id**  string | The UUID of the ramdisk image when using an AMI. Will be null if not. By default, it appears in the response for administrative users only.  **Returned:** success |
| **reservation_id**  string | The reservation id for the server. This is an id that can be useful in tracking groups of servers created with multiple create, that will all have the same reservation_id. By default, it appears in the response for administrative users only.  **Returned:** success |
| **root_device_name**  string | The root device name for the instance By default, it appears in the response for administrative users only.  **Returned:** success |
| **scheduler_hints**  dictionary | The dictionary of data to send to the scheduler.  **Returned:** success |
| **security_groups**  list / elements=dictionary | A list of applicable security groups. Each group contains keys for: description, name, id, and rules.  **Returned:** success |
| **server_groups**  list / elements=string | The UUIDs of the server groups to which the server belongs. Currently this can contain at most one entry.  **Returned:** success |
| **status**  string | The state this server is in. Valid values include ‘ACTIVE’, ‘BUILDING’, ‘DELETED’, ‘ERROR’, ‘HARD_REBOOT’, ‘PASSWORD’, ‘PAUSED’, ‘REBOOT’, ‘REBUILD’, ‘RESCUED’, ‘RESIZED’, ‘REVERT_RESIZE’, ‘SHUTOFF’, ‘SOFT_DELETED’, ‘STOPPED’, ‘SUSPENDED’, ‘UNKNOWN’, or ‘VERIFY_RESIZE’.  **Returned:** success |
| **tags**  list / elements=string | A list of associated tags.  **Returned:** success |
| **task_state**  string | The task state of this server.  **Returned:** success |
| **terminated_at**  string | The timestamp when the server was terminated (if it has been).  **Returned:** success |
| **trusted_image_certificates**  list / elements=string | A list of trusted certificate IDs, that were used during image signature verification to verify the signing certificate.  **Returned:** success |
| **updated_at**  string | Timestamp of when this server was last updated.  **Returned:** success |
| **user_data**  string | Configuration information or scripts to use upon launch. Base64 encoded.  **Returned:** success |
| **user_id**  string | The ID of the owners of this server.  **Returned:** success |
| **vm_state**  string | The VM state of this server.  **Returned:** success |
| **volumes**  list / elements=string | Same as attached_volumes.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

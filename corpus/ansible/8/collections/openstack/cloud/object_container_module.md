---
collection: ansible
version: "8"
title: "openstack.cloud.object_container module – Manage a Swift container."
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/object_container_module.html
fetched_at: 2026-07-28T02:48:23+00:00
---
# openstack.cloud.object_container module – Manage a Swift container.

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
> see [Requirements](object_container_module.md#ansible-collections-openstack-cloud-object-container-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.object_container`.

- [Synopsis](object_container_module.md#synopsis)
- [Requirements](object_container_module.md#requirements)
- [Parameters](object_container_module.md#parameters)
- [Notes](object_container_module.md#notes)
- [Examples](object_container_module.md#examples)
- [Return Values](object_container_module.md#return-values)

## [Synopsis](object_container_module.md#id1)

- Create, update and delete a Swift container.

## [Requirements](object_container_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](object_container_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **delete_metadata_keys**  aliases: keys  list / elements=string | Keys from *metadata* to be deleted.  *metadata* has precedence over *delete_metadata_keys*: If any key is present in both options, then it will be created or updated, not deleted.  Metadata keys are case-insensitive. |
| **delete_with_all_objects**  boolean | Whether the container should be deleted recursively, i.e. including all of its objects.  If *delete_with_all_objects* is set to `false`, an attempt to delete a container which contains objects will fail.  **Choices:**   - `false` ← (default) - `true` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **metadata**  dictionary | Key value pairs to be set as metadata on the container.  Both custom and system metadata can be set.  Custom metadata are keys and values defined by the user.  *metadata* is the same as setting properties in openstackclient with `openstack container set --property ...`.  Metadata keys are case-insensitive. |
| **name**  aliases: container  string / required | Name (and ID) of a Swift container. |
| **read_ACL**  string | The ACL that grants read access.  For example, use `.r:*,.rlistings` for public access and `''` for private access. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Whether the object should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |
| **write_ACL**  string | The ACL that grants write access. |

## [Notes](object_container_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](object_container_module.md#id5)

```yaml+jinja
- name: Create empty container with public access
  openstack.cloud.object_container:
    name: "new-container"
    state: present
    read_ACL: ".r:*,.rlistings"

- name: Set metadata for container
  openstack.cloud.object_container:
    name: "new-container"
    metadata:
      'Cache-Control': 'no-cache'
      'foo': 'bar'

- name: Delete metadata keys of a container
  openstack.cloud.object_container:
    name: "new-container"
    delete_metadata_keys:
      - foo

- name: Delete container
  openstack.cloud.object_container:
    name: "new-container"
    state: absent

- name: Delete container and all its objects
  openstack.cloud.object_container:
    name: "new-container"
    delete_with_all_objects: true
    state: absent
```

## [Return Values](object_container_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **container**  dictionary | Dictionary describing the Swift container.  **Returned:** On success when *state* is `present`. |
| **bytes**  integer | The total number of bytes that are stored in Object Storage for the container.  **Returned:** success  **Sample:** `5449` |
| **bytes_used**  integer | The count of bytes used in total.  **Returned:** success  **Sample:** `5449` |
| **content_type**  string | The MIME type of the list of names.  **Returned:** success |
| **count**  integer | The number of objects in the container.  **Returned:** success  **Sample:** `1` |
| **history_location**  string | Enables versioning on the container.  **Returned:** success |
| **id**  string | The ID of the container. Equals *name*.  **Returned:** success  **Sample:** `"otc"` |
| **if_none_match**  string | In combination with `Expect: 100-Continue`, specify an `If-None-Match: *` header to query whether the server already has a copy of the object before any data is sent.  **Returned:** success |
| **is_content_type_detected**  boolean | If set to `true`, Object Storage guesses the content type based on the file extension and ignores the value sent in the Content-Type header, if present.  **Returned:** success |
| **is_newest**  boolean | If set to True, Object Storage queries all replicas to return the most recent one. If you omit this header, Object Storage responds faster after it finds one valid replica. Because setting this header to True is more expensive for the back end, use it only when it is absolutely needed.  **Returned:** success |
| **meta_temp_url_key**  string | The secret key value for temporary URLs. If not set, this header is not returned by this operation.  **Returned:** success |
| **meta_temp_url_key_2**  string | A second secret key value for temporary URLs. If not set, this header is not returned by this operation.  **Returned:** success |
| **name**  string | The name of the container.  **Returned:** success  **Sample:** `"otc"` |
| **object_count**  integer | The number of objects.  **Returned:** success  **Sample:** `1` |
| **read_ACL**  string | The ACL that grants read access. If not set, this header is not returned by this operation.  **Returned:** success |
| **storage_policy**  string | Storage policy used by the container. It is not possible to change policy of an existing container.  **Returned:** success |
| **sync_key**  string | The secret key for container synchronization. If not set, this header is not returned by this operation.  **Returned:** success |
| **sync_to**  string | The destination for container synchronization. If not set, this header is not returned by this operation.  **Returned:** success |
| **timestamp**  string | The timestamp of the transaction.  **Returned:** success |
| **versions_location**  string | Enables versioning on this container. The value is the name of another container. You must UTF-8-encode and then URL-encode the name before you include it in the header. To disable versioning, set the header to an empty string.  **Returned:** success |
| **write_ACL**  string | The ACL that grants write access. If not set, this header is not returned by this operation.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

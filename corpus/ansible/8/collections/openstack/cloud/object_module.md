---
collection: ansible
version: "8"
title: "openstack.cloud.object module – Create or delete Swift objects in OpenStack clouds"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/object_module.html
fetched_at: 2026-07-28T02:48:20+00:00
---
# openstack.cloud.object module – Create or delete Swift objects in OpenStack clouds

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
> see [Requirements](object_module.md#ansible-collections-openstack-cloud-object-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.object`.

- [Synopsis](object_module.md#synopsis)
- [Requirements](object_module.md#requirements)
- [Parameters](object_module.md#parameters)
- [Notes](object_module.md#notes)
- [Examples](object_module.md#examples)
- [Return Values](object_module.md#return-values)

## [Synopsis](object_module.md#id1)

- Create or delete Swift objects in OpenStack clouds

## [Requirements](object_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](object_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **container**  string / required | The name (and ID) of the container in which to create the object in.  This container will not be created if it does not exist already. |
| **data**  string | The content to upload to the object.  Mutually exclusive with *filename*.  This attribute cannot be updated. |
| **filename**  string | The path to the local file whose contents will be uploaded.  Mutually exclusive with *data*. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string / required | Name (and ID) of the object. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Whether the object should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](object_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](object_module.md#id5)

```yaml+jinja
- name: Create a object named 'fstab' in the 'config' container
  openstack.cloud.object:
    cloud: mordred
    container: config
    filename: /etc/fstab
    name: fstab
    state: present

- name: Delete a container called config and all of its contents
  openstack.cloud.object:
    cloud: rax-iad
    container: config
    state: absent
```

## [Return Values](object_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Dictionary describing the object.  **Returned:** On success when *state* is `present`. |
| **accept_ranges**  string | The type of ranges that the object accepts.  **Returned:** success |
| **access_control_allow_origin**  string | CORS for RAX (deviating from standard)  **Returned:** success |
| **content_disposition**  string | If set, specifies the override behavior for the browser. For example, this header might specify that the browser use a download program to save this file rather than show the file, which is the default. If not set, this header is not returned by this operation.  **Returned:** success |
| **content_encoding**  string | If set, the value of the Content-Encoding metadata. If not set, this header is not returned by this operation.  **Returned:** success |
| **content_length**  string | HEAD operations do not return content. However, in this operation the value in the Content-Length header is not the size of the response body. Instead it contains the size of the object, in bytes.  **Returned:** success |
| **content_type**  integer | The MIME type of the object.  **Returned:** success |
| **copy_from**  string | If set, this is the name of an object used to create the new object by copying the X-Copy-From object. The value is in form {container}/{object}. You must UTF-8-encode and then URL-encode the names of the container and object before you include them in the header. Using PUT with X-Copy-From has the same effect as using the COPY operation to copy an object.  **Returned:** success |
| **delete_after**  integer | Specifies the number of seconds after which the object is removed. Internally, the Object Storage system stores this value in the X-Delete-At metadata item.  **Returned:** success |
| **delete_at**  string | If set, the time when the object will be deleted by the system in the format of a UNIX Epoch timestamp. If not set, this header is not returned by this operation.  **Returned:** success |
| **etag**  string | For objects smaller than 5 GB, this value is the MD5 checksum of the object content. The value is not quoted. For manifest objects, this value is the MD5 checksum of the concatenated string of MD5 checksums and ETags for each of the segments in the manifest, and not the MD5 checksum of the content that was downloaded. Also the value is enclosed in double-quote characters. You are strongly recommended to compute the MD5 checksum of the response body as it is received and compare this value with the one in the ETag header. If they differ, the content was corrupted, so retry the operation.  **Returned:** success |
| **expires_at**  string | Used with temporary URLs to specify the expiry time of the signature. For more information about temporary URLs, see OpenStack Object Storage API v1 Reference.  **Returned:** success |
| **id**  string | ID of the object. Equal to `name`.  **Returned:** success |
| **if_match**  list / elements=string | See <http://www.ietf.org/rfc/rfc2616.txt>.  **Returned:** success |
| **if_modified_since**  string | See <http://www.ietf.org/rfc/rfc2616.txt>.  **Returned:** success |
| **if_none_match**  list / elements=string | In combination with `Expect: 100-Continue`, specify an `If-None-Match: *` header to query whether the server already has a copy of the object before any data is sent.  **Returned:** success |
| **if_unmodified_since**  string | See <http://www.ietf.org/rfc/rfc2616.txt>.  **Returned:** success |
| **is_content_type_detected**  boolean | If set to true, Object Storage guesses the content type based on the file extension and ignores the value sent in the Content-Type header, if present.  **Returned:** success |
| **is_newest**  boolean | If set to True, Object Storage queries all replicas to return the most recent one. If you omit this header, Object Storage responds faster after it finds one valid replica. Because setting this header to True is more expensive for the back end, use it only when it is absolutely needed.  **Returned:** success |
| **is_static_large_object**  boolean | Set to True if this object is a static large object manifest object.  **Returned:** success |
| **last_modified_at**  string | The date and time that the object was created or the last time that the metadata was changed.  **Returned:** success |
| **manifest**  string | If present, this is a dynamic large object manifest object. The value is the container and object name prefix of the segment objects in the form container/prefix.  **Returned:** success |
| **multipart_manifest**  string | If you include the multipart-manifest=get query parameter and the object is a large object, the object contents are not returned. Instead, the manifest is returned in the X-Object-Manifest response header for dynamic large objects or in the response body for static large objects.  **Returned:** success |
| **name**  string | Name of the object.  **Returned:** success |
| **object_manifest**  string | If set, to this is a dynamic large object manifest object. The value is the container and object name prefix of the segment objects in the form container/prefix.  **Returned:** success |
| **range**  dictionary | TODO.  **Returned:** success |
| **signature**  string | Used with temporary URLs to sign the request. For more information about temporary URLs, see OpenStack Object Storage API v1 Reference.  **Returned:** success |
| **symlink_target**  string | If present, this is a symlink object. The value is the relative path of the target object in the format <container>/<object>.  **Returned:** success |
| **symlink_target_account**  string | If present, and X-Symlink-Target is present, then this is a cross-account symlink to an object in the account specified in the value.  **Returned:** success |
| **timestamp**  string | The timestamp of the transaction.  **Returned:** success |
| **transfer_encoding**  string | Set to chunked to enable chunked transfer encoding. If used, do not set the Content-Length header to a non-zero value.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

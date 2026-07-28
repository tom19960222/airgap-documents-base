---
collection: ansible
version: "6"
title: "openstack.cloud.server_metadata module – Add/Update/Delete Metadata in Compute Instances from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/server_metadata_module.html
fetched_at: 2026-07-28T00:17:08+00:00
---
# openstack.cloud.server_metadata module – Add/Update/Delete Metadata in Compute Instances from OpenStack

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

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](server_metadata_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Availability zone in which to create the snapshot. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **meta**  dictionary / required | A list of key value pairs that should be provided as a metadata to the instance or a string containing a list of key-value pairs. Eg: meta: “key1=value1,key2=value2” |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **server**  aliases: name  string / required | Name of the instance to update the metadata |
| **state**  string | Should the resource be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](server_metadata_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](server_metadata_module.md#id5)

```yaml+jinja
# Creates or updates hostname=test1 as metadata of the server instance vm1
- name: add metadata to compute instance
  hosts: localhost
  tasks:
  - name: add metadata to instance
    openstack.cloud.server_metadata:
        state: present
        auth:
            auth_url: https://openstack-api.example.com:35357/v2.0/
            username: admin
            password: admin
            project_name: admin
        name: vm1
        meta:
            hostname: test1
            group: group1

# Removes the keys under meta from the instance named vm1
- name: delete metadata from compute instance
  hosts: localhost
  tasks:
  - name: delete metadata from instance
    openstack.cloud.server_metadata:
        state: absent
        auth:
            auth_url: https://openstack-api.example.com:35357/v2.0/
            username: admin
            password: admin
            project_name: admin
        name: vm1
        meta:
            hostname:
            group:
```

## [Return Values](server_metadata_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **metadata**  dictionary | The metadata of compute instance after the change  Returned: success  Sample: `{"key1": "value1", "key2": "value2"}` |
| **server_id**  string | The compute instance id where the change was made  Returned: success  Sample: `"324c4e91-3e03-4f62-9a4d-06119a8a8d16"` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

---
collection: ansible
version: "8"
title: "openstack.cloud.baremetal_node_action module – Activate/Deactivate Bare Metal nodes from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/baremetal_node_action_module.html
fetched_at: 2026-07-28T01:04:23+00:00
---
# openstack.cloud.baremetal_node_action module – Activate/Deactivate Bare Metal nodes from OpenStack

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
> see [Requirements](baremetal_node_action_module.md#ansible-collections-openstack-cloud-baremetal-node-action-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.baremetal_node_action`.

- [Synopsis](baremetal_node_action_module.md#synopsis)
- [Requirements](baremetal_node_action_module.md#requirements)
- [Parameters](baremetal_node_action_module.md#parameters)
- [Notes](baremetal_node_action_module.md#notes)
- [Examples](baremetal_node_action_module.md#examples)

## [Synopsis](baremetal_node_action_module.md#id1)

- Deploy to Bare Metal nodes controlled by Ironic.

## [Requirements](baremetal_node_action_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](baremetal_node_action_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **config_drive**  any | A configdrive file or HTTP(S) URL that will be passed along to the node. |
| **deploy**  boolean | Indicates if the resource should be deployed. Allows for deployment logic to be disengaged and control of the node power or maintenance state to be changed.  **Choices:**   - `false` - `true` ← (default) |
| **instance_info**  dictionary | Definition of the instance information which is used to deploy the node. This information is only required when *state* is set to `present` or `on`. |
| **image_checksum**  string | The checksum of image_source. |
| **image_disk_format**  string | The type of image that has been requested to be deployed. |
| **image_source**  string | An HTTP(S) URL where the image can be retrieved from. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **maintenance**  boolean | Set node into maintenance mode.  The power state as controlled with *power* will not be changed when maintenance mode of a node is changed.  **Choices:**   - `false` - `true` |
| **maintenance_reason**  string | A string expression regarding the reason a node is in a maintenance mode. |
| **name**  aliases: id, uuid  string / required | Name or ID of the Bare Metal node. |
| **power**  string | A setting to allow power state to be asserted allowing nodes that are not yet deployed to be powered on, and nodes that are deployed to be powered off.  *power* can be `present`, `absent`, `maintenance`, `on` or `off`.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"maintenance"` - `"on"` - `"off"` |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Indicates desired state of the resource.  *state* can be `present`, `absent`, `maintenance`, `on` or `off`.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"maintenance"` - `"on"` - `"off"` |
| **timeout**  integer | Number of seconds to wait for the node activation or deactivation to complete.  **Default:** `1800` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](baremetal_node_action_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](baremetal_node_action_module.md#id5)

```yaml+jinja
# Activate a node by booting an image with a configdrive attached
- openstack.cloud.baremetal_node_action:
    instance_info:
      image_source: "http://192.168.1.1/deploy_image.img"
      image_checksum: "356a6b55ecc511a20c33c946c4e678af"
      image_disk_format: "qcow"
    delegate_to: localhost
    deploy: true
    cloud: "openstack"
    config_drive: "http://192.168.1.1/host-configdrive.iso"
    maintenance: false
    power: present
    uuid: "d44666e1-35b3-4f6b-acb0-88ab7052da69"
    state: present

# Activate a node by booting an image with a configdrive json object
- openstack.cloud.baremetal_node_action:
    auth_type: None
    auth:
        endpoint: "http://192.168.1.1:6385/"
    id: "d44666e1-35b3-4f6b-acb0-88ab7052da69"
    config_drive:
      meta_data:
        hostname: node1
        public_keys:
          default: ssh-rsa AAA...BBB==
    delegate_to: localhost
    instance_info:
      image_source: "http://192.168.1.1/deploy_image.img"
      image_checksum: "356a6b55ecc511a20c33c946c4e678af"
      image_disk_format: "qcow"
```

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

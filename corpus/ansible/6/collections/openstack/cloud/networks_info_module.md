---
collection: ansible
version: "6"
title: "openstack.cloud.networks_info module – Retrieve information about one or more OpenStack networks."
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/networks_info_module.html
fetched_at: 2026-07-28T00:16:52+00:00
---
# openstack.cloud.networks_info module – Retrieve information about one or more OpenStack networks.

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
> see [Requirements](networks_info_module.md#ansible-collections-openstack-cloud-networks-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.networks_info`.

- [Synopsis](networks_info_module.md#synopsis)
- [Requirements](networks_info_module.md#requirements)
- [Parameters](networks_info_module.md#parameters)
- [Notes](networks_info_module.md#notes)
- [Examples](networks_info_module.md#examples)
- [Return Values](networks_info_module.md#return-values)

## [Synopsis](networks_info_module.md#id1)

- Retrieve information about one or more networks from OpenStack.
- This module was called `openstack.cloud.networks_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [openstack.cloud.networks_info](networks_info_module.md#ansible-collections-openstack-cloud-networks-info-module) module no longer returns `ansible_facts`!

## [Requirements](networks_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](networks_info_module.md#id3)

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
| **filters**  dictionary | A dictionary of meta data to use for further filtering. Elements of this dictionary may be additional dictionaries. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string | Name or ID of the Network |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](networks_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](networks_info_module.md#id5)

```yaml+jinja
- name: Gather information about previously created networks
  openstack.cloud.networks_info:
    auth:
      auth_url: https://identity.example.com
      username: user
      password: password
      project_name: someproject
  register: result

- name: Show openstack networks
  debug:
    msg: "{{ result.openstack_networks }}"

- name: Gather information about a previously created network by name
  openstack.cloud.networks_info:
    auth:
      auth_url: https://identity.example.com
      username: user
      password: password
      project_name: someproject
    name:  network1
  register: result

- name: Show openstack networks
  debug:
    msg: "{{ result.openstack_networks }}"

- name: Gather information about a previously created network with filter
  # Note: name and filters parameters are Not mutually exclusive
  openstack.cloud.networks_info:
    auth:
      auth_url: https://identity.example.com
      username: user
      password: password
      project_name: someproject
    filters:
      tenant_id: 55e2ce24b2a245b09f181bf025724cbe
      subnets:
        - 057d4bdf-6d4d-4728-bb0f-5ac45a6f7400
        - 443d4dc0-91d4-4998-b21c-357d10433483
  register: result

- name: Show openstack networks
  debug:
    msg: "{{ result.openstack_networks }}"
```

## [Return Values](networks_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **openstack_networks**  complex | has all the openstack information about the networks  Returned: always, but can be null |
| **id**  string | Unique UUID.  Returned: success |
| **name**  string | Name given to the network.  Returned: success |
| **shared**  boolean | Network shared flag.  Returned: success |
| **status**  string | Network status.  Returned: success |
| **subnets**  list / elements=string | Subnet(s) included in this network.  Returned: success |
| **tenant_id**  string | Tenant id associated with this network.  Returned: success |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

---
collection: ansible
version: "6"
title: "openstack.cloud.floating_ip_info module – Get information about floating ips"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/floating_ip_info_module.html
fetched_at: 2026-07-28T00:16:36+00:00
---
# openstack.cloud.floating_ip_info module – Get information about floating ips

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
> see [Requirements](floating_ip_info_module.md#ansible-collections-openstack-cloud-floating-ip-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.floating_ip_info`.

- [Synopsis](floating_ip_info_module.md#synopsis)
- [Requirements](floating_ip_info_module.md#requirements)
- [Parameters](floating_ip_info_module.md#parameters)
- [Notes](floating_ip_info_module.md#notes)
- [Examples](floating_ip_info_module.md#examples)
- [Return Values](floating_ip_info_module.md#return-values)

## [Synopsis](floating_ip_info_module.md#id1)

- Get a generator of floating ips.

## [Requirements](floating_ip_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](floating_ip_info_module.md#id3)

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
| **description**  string | The description of a floating IP. |
| **fixed_ip_address**  string | The fixed IP address associated with a floating IP address. |
| **floating_ip_address**  string | The IP address of a floating IP. |
| **floating_network**  string | The name or id of the network associated with a floating IP. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **port**  string | The name or id of the port to which a floating IP is associated. |
| **project_id**  string | The ID of the project a floating IP is associated with. |
| **region_name**  string | Name of the region. |
| **router**  string | The name or id of an associated router. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **status**  string | The status of a floating IP, which can be ``ACTIVE``or ``DOWN``.  Choices:   - `"active"` - `"down"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](floating_ip_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](floating_ip_info_module.md#id5)

```yaml+jinja
# Getting all floating ips
- openstack.cloud.floating_ip_info:
  register: fips

# Getting fip by associated fixed IP address.
- openstack.cloud.floating_ip_info:
    fixed_ip_address: 192.168.10.8
  register: fip

# Getting fip by associated router.
- openstack.cloud.floating_ip_info:
    router: my-router
  register: fip
```

## [Return Values](floating_ip_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **floating_ips**  complex | The floating ip objects list.  Returned: On Success. |
| **created_at**  string | Timestamp at which the floating IP was assigned.  Returned: success |
| **description**  string | The description of a floating IP.  Returned: success |
| **dns_domain**  string | The DNS domain.  Returned: success |
| **dns_name**  string | The DNS name.  Returned: success |
| **fixed_ip_address**  string | The fixed IP address associated with a floating IP address.  Returned: success |
| **floating_ip_address**  string | The IP address of a floating IP.  Returned: success |
| **floating_network_id**  string | The id of the network associated with a floating IP.  Returned: success |
| **id**  string | Id of the floating ip.  Returned: success |
| **name**  string | Name of the floating ip.  Returned: success |
| **port_details**  string | The details of the port that this floating IP associates with. Present if ``fip-port-details`` extension is loaded.  Returned: success |
| **port_id**  string | The port ID floating ip associated with.  Returned: success |
| **project_id**  string | The ID of the project this floating IP is associated with.  Returned: success |
| **qos_policy_id**  string | The ID of the QoS policy attached to the floating IP.  Returned: success |
| **revision_number**  string | Revision number.  Returned: success |
| **router_id**  string | The id of the router floating ip associated with.  Returned: success |
| **status**  string | The status of a floating IP, which can be ``ACTIVE``or ``DOWN``. Can be ‘ACTIVE’ and ‘DOWN’.  Returned: success |
| **subnet_id**  string | The id of the subnet the floating ip associated with.  Returned: success |
| **tags**  string | List of tags.  Returned: success |
| **updated_at**  string | Timestamp at which the floating IP was last updated.  Returned: success |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)

---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_network_offering module – Manages network offerings on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_network_offering_module.html
fetched_at: 2026-07-28T00:15:37+00:00
---
# ngine_io.cloudstack.cs_network_offering module – Manages network offerings on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ngine_io/cloudstack) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_network_offering_module.md#ansible-collections-ngine-io-cloudstack-cs-network-offering-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_network_offering`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_network_offering_module.md#synopsis)
- [Requirements](cs_network_offering_module.md#requirements)
- [Parameters](cs_network_offering_module.md#parameters)
- [Notes](cs_network_offering_module.md#notes)
- [Examples](cs_network_offering_module.md#examples)
- [Return Values](cs_network_offering_module.md#return-values)

## [Synopsis](cs_network_offering_module.md#id1)

- Create, update, enable, disable and remove network offerings.

## [Requirements](cs_network_offering_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_network_offering_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **availability**  string | The availability of network offering. Default value is Optional |
| **conserve_mode**  boolean | Whether the network offering has IP conserve mode enabled.  Choices:   - `false` - `true` |
| **details**  list / elements=dictionary | Network offering details in key/value pairs.  with service provider as a value |
| **display_text**  string | Display text of the network offerings. |
| **domains**  aliases: domain  list / elements=string  added in ngine_io.cloudstack 2.2.0 | List of domains the network offering is related to.  Use `public` for public offerings. |
| **egress_default_policy**  string | Whether the default egress policy is allow or to deny.  Choices:   - `"allow"` - `"deny"` |
| **for_vpc**  boolean | Whether the offering is meant to be used for VPC or not.  Choices:   - `false` - `true` |
| **guest_ip_type**  string | Guest type of the network offering.  Choices:   - `"Shared"` - `"Isolated"` |
| **keepalive_enabled**  boolean | If true keepalive will be turned on in the loadbalancer.  At the time of writing this has only an effect on haproxy.  the mode http and httpclose options are unset in the haproxy conf file.  Choices:   - `false` - `true` |
| **max_connections**  integer | Maximum number of concurrent connections supported by the network offering. |
| **name**  string / required | The name of the network offering. |
| **network_rate**  integer | Data transfer rate in megabits per second allowed. |
| **persistent**  boolean | True if network offering supports persistent networks  defaulted to false if not specified  Choices:   - `false` - `true` |
| **service_capabilities**  aliases: service_capability  list / elements=string | Desired service capabilities as part of network offering. |
| **service_offering**  string | The service offering name or ID used by virtual router provider. |
| **service_providers**  aliases: service_provider  list / elements=dictionary | Provider to service mapping.  If not specified, the provider for the service will be mapped to the default provider on the physical network. |
| **specify_ip_ranges**  boolean | Whether the network offering supports specifying IP ranges.  Defaulted to `no` by the API if not specified.  Choices:   - `false` - `true` |
| **specify_vlan**  boolean | Whether the network offering supports vlans or not.  Choices:   - `false` - `true` |
| **state**  string | State of the network offering.  Choices:   - `"enabled"` - `"present"` ← (default) - `"disabled"` - `"absent"` |
| **supported_services**  aliases: supported_service  list / elements=string | Services supported by the network offering.  A list of one or more items from the choice list.  Choices:   - `"Dns"` - `"PortForwarding"` - `"Dhcp"` - `"SourceNat"` - `"UserData"` - `"Firewall"` - `"StaticNat"` - `"Vpn"` - `"Lb"` |
| **tags**  aliases: tag  list / elements=string  added in ngine_io.cloudstack 2.2.0 | List of tags. Tags are a list of strings.  To delete all tags, set an empty list e.g. *tags: []*. |
| **traffic_type**  string | The traffic type for the network offering.  Default: `"Guest"` |
| **zones**  aliases: zone  list / elements=string  added in ngine_io.cloudstack 2.2.0 | List of zones the network offering is related to.  Use `all` for all zones offering. |

## [Notes](cs_network_offering_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_network_offering_module.md#id5)

```yaml+jinja
- name: Create a network offering and enable it
  ngine_io.cloudstack.cs_network_offering:
    name: my_network_offering
    display_text: network offering description
    state: enabled
    guest_ip_type: Isolated
    supported_services: [ Dns, PortForwarding, Dhcp, SourceNat, UserData, Firewall, StaticNat, Vpn, Lb ]
    service_providers:
      - { service: 'dns', provider: 'virtualrouter' }
      - { service: 'dhcp', provider: 'virtualrouter' }

- name: Remove a network offering
  ngine_io.cloudstack.cs_network_offering:
    name: my_network_offering
    state: absent
```

## [Return Values](cs_network_offering_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **availability**  string | The availability of network offering.  Returned: success  Sample: `"Optional"` |
| **display_text**  string | The display text of the network offering.  Returned: success  Sample: `"My network offering"` |
| **domains**  list / elements=string  added in ngine_io.cloudstack 2.2.0 | List of domains associated with the network offering.  Returned: success  Sample: `["public"]` |
| **egress_default_policy**  string | Default egress policy.  Returned: success  Sample: `"allow"` |
| **for_vpc**  boolean | Whether the offering is meant to be used for VPC or not.  Returned: success  Sample: `false` |
| **guest_ip_type**  string | Guest type of the network offering.  Returned: success  Sample: `"Isolated"` |
| **id**  string | UUID of the network offering.  Returned: success  Sample: `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **is_default**  boolean | Whether network offering is the default offering or not.  Returned: success  Sample: `false` |
| **is_persistent**  boolean | Whether persistent networks are supported or not.  Returned: success  Sample: `false` |
| **max_connections**  integer | The maximum number of concurrent connections to be handled by LB.  Returned: success  Sample: `300` |
| **name**  string | The name of the network offering.  Returned: success  Sample: `"MyCustomNetworkOffering"` |
| **network_rate**  integer | The network traffic transfer ate in Mbit/s.  Returned: success  Sample: `200` |
| **service_offering_id**  string | The service offering ID.  Returned: success  Sample: `"c5f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **state**  string | The state of the network offering.  Returned: success  Sample: `"Enabled"` |
| **tags**  list / elements=string  added in ngine_io.cloudstack 2.2.0 | List of tags associated with the network offering.  Returned: success  Sample: `["tag1", "tag2"]` |
| **traffic_type**  string | The traffic type.  Returned: success  Sample: `"Guest"` |
| **zones**  list / elements=string  added in ngine_io.cloudstack 2.2.0 | List of zones associated with the network offering.  Returned: success  Sample: `["all"]` |

### Authors

- David Passante (@dpassante)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)

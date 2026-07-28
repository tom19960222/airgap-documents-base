---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_network module – Manages networks on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_network_module.html
fetched_at: 2026-07-28T00:15:35+00:00
---
# ngine_io.cloudstack.cs_network module – Manages networks on Apache CloudStack based clouds.

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
> see [Requirements](cs_network_module.md#ansible-collections-ngine-io-cloudstack-cs-network-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_network`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_network_module.md#synopsis)
- [Requirements](cs_network_module.md#requirements)
- [Parameters](cs_network_module.md#parameters)
- [Notes](cs_network_module.md#notes)
- [Examples](cs_network_module.md#examples)
- [Return Values](cs_network_module.md#return-values)

## [Synopsis](cs_network_module.md#id1)

- Create, update, restart and delete networks.

## [Requirements](cs_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the network is related to. |
| **acl**  string | The name of the access control list for the VPC network tier. |
| **acl_type**  string | Access control type for the network.  If not specified, Cloudstack will default to `account` for isolated networks  and `domain` for shared networks.  Only considered on create.  Choices:   - `"account"` - `"domain"` |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **cidr_ipv6**  string | CIDR of IPv6 network, must be at least /64.  Only considered on create. |
| **clean_up**  boolean | Cleanup old network elements.  Only considered on *state=restarted*.  Choices:   - `false` ← (default) - `true` |
| **display_text**  string | Display text of the network.  If not specified, *name* will be used as *display_text*. |
| **domain**  string | Domain the network is related to. |
| **end_ip**  string | The ending IPv4 address of the network belongs to.  If not specified, value of *start_ip* is used.  Only considered on create. |
| **end_ipv6**  string | The ending IPv6 address of the network belongs to.  If not specified, value of *start_ipv6* is used.  Only considered on create. |
| **gateway**  string | The gateway of the network.  Required for shared networks and isolated networks when it belongs to a VPC.  Only considered on create. |
| **gateway_ipv6**  string | The gateway of the IPv6 network.  Required for shared networks.  Only considered on create. |
| **isolated_pvlan**  string | The isolated private VLAN for this network. |
| **name**  string / required | Name (case sensitive) of the network. |
| **netmask**  string | The netmask of the network.  Required for shared networks and isolated networks when it belongs to a VPC.  Only considered on create. |
| **network_domain**  string | The network domain. |
| **network_offering**  string | Name of the offering for the network.  Required if *state=present*. |
| **poll_async**  boolean | Poll async jobs until job has finished.  Choices:   - `false` - `true` ← (default) |
| **project**  string | Name of the project the network to be deployed in. |
| **start_ip**  string | The beginning IPv4 address of the network belongs to.  Only considered on create. |
| **start_ipv6**  string | The beginning IPv6 address of the network belongs to.  Only considered on create. |
| **state**  string | State of the network.  Choices:   - `"present"` ← (default) - `"absent"` - `"restarted"` |
| **subdomain_access**  boolean | Defines whether to allow subdomains to use networks dedicated to their parent domain(s).  Should be used with *acl_type=domain*.  Only considered on create.  Choices:   - `false` - `true` |
| **tags**  aliases: tag  list / elements=dictionary | List of tags. Tags are a list of dictionaries having keys *key* and *value*.  To delete all tags, set a empty list e.g. *tags: []*. |
| **vlan**  string | The ID or VID of the network. |
| **vpc**  string | Name of the VPC of the network. |
| **zone**  string / required | Name of the zone in which the network should be deployed. |

## [Notes](cs_network_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_network_module.md#id5)

```yaml+jinja
- name: Create a network
  ngine_io.cloudstack.cs_network:
    name: my network
    zone: gva-01
    network_offering: DefaultIsolatedNetworkOfferingWithSourceNatService
    network_domain: example.com

- name: Create a network with start and end IP
  ngine_io.cloudstack.cs_network:
    name: Private Network
    network_offering: PrivNet
    start_ip: 10.12.9.10
    end_ip: 10.12.9.100
    netmask: 255.255.255.0
    zone: gva-01

- name: Create a VPC tier
  ngine_io.cloudstack.cs_network:
    name: my VPC tier 1
    zone: gva-01
    vpc: my VPC
    network_offering: DefaultIsolatedNetworkOfferingForVpcNetworks
    gateway: 10.43.0.1
    netmask: 255.255.255.0
    acl: my web acl

- name: Update a network
  ngine_io.cloudstack.cs_network:
    name: my network
    zone: zone01
    display_text: network of domain example.local
    network_domain: example.local

- name: Restart a network with clean up
  ngine_io.cloudstack.cs_network:
    name: my network
    zone: zone01
    clean_up: yes
    state: restarted

- name: Remove a network
  ngine_io.cloudstack.cs_network:
    name: my network
    zone: zone01
    state: absent
```

## [Return Values](cs_network_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the network is related to.  Returned: success  Sample: `"example account"` |
| **acl**  string | Name of the access control list for the VPC network tier.  Returned: success  Sample: `"My ACL"` |
| **acl_id**  string | ID of the access control list for the VPC network tier.  Returned: success  Sample: `"dfafcd55-0510-4b8c-b6c5-b8cedb4cfd88"` |
| **acl_type**  string | Access type of the network (Domain, Account).  Returned: success  Sample: `"Account"` |
| **broadcast_domain_type**  string | Broadcast domain type of the network.  Returned: success  Sample: `"Vlan"` |
| **cidr**  string | IPv4 network CIDR.  Returned: success  Sample: `"10.101.64.0/24"` |
| **cidr_ipv6**  string | IPv6 network CIDR.  Returned: if available  Sample: `"2001:db8::/64"` |
| **display_text**  string | Display text of the network.  Returned: success  Sample: `"web project"` |
| **dns1**  string | IP address of the 1st nameserver.  Returned: success  Sample: `"1.2.3.4"` |
| **dns2**  string | IP address of the 2nd nameserver.  Returned: success  Sample: `"1.2.3.4"` |
| **domain**  string | Domain the network is related to.  Returned: success  Sample: `"ROOT"` |
| **gateway**  string | IPv4 gateway.  Returned: success  Sample: `"10.101.64.1"` |
| **gateway_ipv6**  string | IPv6 gateway.  Returned: if available  Sample: `"2001:db8::1"` |
| **id**  string | UUID of the network.  Returned: success  Sample: `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **is_persistent**  boolean | Whether the network is persistent or not.  Returned: success  Sample: `false` |
| **is_system**  boolean | Whether the network is system related or not.  Returned: success  Sample: `false` |
| **name**  string | Name of the network.  Returned: success  Sample: `"web project"` |
| **netmask**  string | IPv4 netmask.  Returned: success  Sample: `"255.255.255.0"` |
| **network_domain**  string | The network domain  Returned: success  Sample: `"example.local"` |
| **network_offering**  string | The network offering name.  Returned: success  Sample: `"DefaultIsolatedNetworkOfferingWithSourceNatService"` |
| **network_offering_availability**  string | The availability of the network offering the network is created from  Returned: success  Sample: `"Optional"` |
| **network_offering_conserve_mode**  boolean | Whether the network offering has IP conserve mode enabled or not.  Returned: success  Sample: `false` |
| **network_offering_display_text**  string | The network offering display text.  Returned: success  Sample: `"Offering for Isolated Vpc networks with Source Nat service enabled"` |
| **project**  string | Name of project.  Returned: success  Sample: `"Production"` |
| **state**  string | State of the network (Allocated, Implemented, Setup).  Returned: success  Sample: `"Allocated"` |
| **tags**  list / elements=string | List of resource tags associated with the network.  Returned: success  Sample: `["[ { \"key\": \"foo\"", " \"value\": \"bar\" } ]"]` |
| **traffic_type**  string | Traffic type of the network.  Returned: success  Sample: `"Guest"` |
| **type**  string | Type of the network.  Returned: success  Sample: `"Isolated"` |
| **vpc**  string | Name of the VPC.  Returned: if available  Sample: `"My VPC"` |
| **zone**  string | Name of zone.  Returned: success  Sample: `"ch-gva-2"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)

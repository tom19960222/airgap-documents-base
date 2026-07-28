---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_vpn_customer_gateway module – Manages site-to-site VPN customer gateway configurations on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_vpn_customer_gateway_module.html
fetched_at: 2026-07-28T00:15:56+00:00
---
# ngine_io.cloudstack.cs_vpn_customer_gateway module – Manages site-to-site VPN customer gateway configurations on Apache CloudStack based clouds.

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
> see [Requirements](cs_vpn_customer_gateway_module.md#ansible-collections-ngine-io-cloudstack-cs-vpn-customer-gateway-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_vpn_customer_gateway`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_vpn_customer_gateway_module.md#synopsis)
- [Requirements](cs_vpn_customer_gateway_module.md#requirements)
- [Parameters](cs_vpn_customer_gateway_module.md#parameters)
- [Notes](cs_vpn_customer_gateway_module.md#notes)
- [Examples](cs_vpn_customer_gateway_module.md#examples)
- [Return Values](cs_vpn_customer_gateway_module.md#return-values)

## [Synopsis](cs_vpn_customer_gateway_module.md#id1)

- Create, update and remove VPN customer gateways.

## [Requirements](cs_vpn_customer_gateway_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_vpn_customer_gateway_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the VPN customer gateway is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **cidrs**  aliases: cidr  list / elements=string | List of guest CIDRs behind the gateway.  Required if *state=present*. |
| **domain**  string | Domain the VPN customer gateway is related to. |
| **dpd**  boolean | Enable Dead Peer Detection.  Disabled per default by the API on creation if not set.  Choices:   - `false` - `true` |
| **esp_lifetime**  integer | Lifetime in seconds of phase 2 VPN connection.  Defaulted to 3600 by the API on creation if not set. |
| **esp_policy**  string | ESP policy in the format e.g. `aes256-sha1;modp1536`.  Required if *state=present*. |
| **force_encap**  boolean | Force encapsulation for NAT traversal.  Disabled per default by the API on creation if not set.  Choices:   - `false` - `true` |
| **gateway**  string | Public IP address of the gateway.  Required if *state=present*. |
| **ike_lifetime**  integer | Lifetime in seconds of phase 1 VPN connection.  Defaulted to 86400 by the API on creation if not set. |
| **ike_policy**  string | IKE policy in the format e.g. `aes256-sha1;modp1536`.  Required if *state=present*. |
| **ipsec_psk**  string | IPsec Preshared-Key.  Cannot contain newline or double quotes.  Required if *state=present*. |
| **name**  string / required | Name of the gateway. |
| **poll_async**  boolean | Poll async jobs until job has finished.  Choices:   - `false` - `true` ← (default) |
| **project**  string | Name of the project the VPN gateway is related to. |
| **state**  string | State of the VPN customer gateway.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](cs_vpn_customer_gateway_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_vpn_customer_gateway_module.md#id5)

```yaml+jinja
- name: Create a vpn customer gateway
  ngine_io.cloudstack.cs_vpn_customer_gateway:
    name: my vpn customer gateway
    cidrs:
    - 192.168.123.0/24
    - 192.168.124.0/24
    esp_policy: aes256-sha1;modp1536
    gateway: 10.10.1.1
    ike_policy: aes256-sha1;modp1536
    ipsec_psk: "S3cr3Tk3Y"

- name: Remove a vpn customer gateway
  ngine_io.cloudstack.cs_vpn_customer_gateway:
    name: my vpn customer gateway
    state: absent
```

## [Return Values](cs_vpn_customer_gateway_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the VPN customer gateway is related to.  Returned: success  Sample: `"example account"` |
| **cidrs**  list / elements=string | List of CIDRs of this customer gateway.  Returned: success  Sample: `["10.10.10.0/24"]` |
| **domain**  string | Domain the VPN customer gateway is related to.  Returned: success  Sample: `"example domain"` |
| **dpd**  boolean | Whether dead pear detection is enabled or not.  Returned: success  Sample: `true` |
| **esp_lifetime**  integer | Lifetime in seconds of phase 2 VPN connection.  Returned: success  Sample: `86400` |
| **esp_policy**  string | IKE policy of the VPN customer gateway.  Returned: success  Sample: `"aes256-sha1;modp1536"` |
| **force_encap**  boolean | Whether encapsulation for NAT traversal is enforced or not.  Returned: success  Sample: `true` |
| **gateway**  string | IP address of the VPN customer gateway.  Returned: success  Sample: `"10.100.212.10"` |
| **id**  string | UUID of the VPN customer gateway.  Returned: success  Sample: `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **ike_lifetime**  integer | Lifetime in seconds of phase 1 VPN connection.  Returned: success  Sample: `86400` |
| **ike_policy**  string | ESP policy of the VPN customer gateway.  Returned: success  Sample: `"aes256-sha1;modp1536"` |
| **name**  string | Name of this customer gateway.  Returned: success  Sample: `"my vpn customer gateway"` |
| **project**  string | Name of project the VPN customer gateway is related to.  Returned: success  Sample: `"Production"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)

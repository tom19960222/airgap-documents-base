---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_mx_vlan module – Manage VLANs in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_mx_vlan_module.html
fetched_at: 2026-07-27T17:00:40+00:00
---
# cisco.meraki.meraki_mx_vlan module – Manage VLANs in the Meraki cloud

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/cisco/meraki) (version 2.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
>
> To use it in a playbook, specify: `cisco.meraki.meraki_mx_vlan`.

- [Synopsis](meraki_mx_vlan_module.md#synopsis)
- [Parameters](meraki_mx_vlan_module.md#parameters)
- [Notes](meraki_mx_vlan_module.md#notes)
- [Examples](meraki_mx_vlan_module.md#examples)
- [Return Values](meraki_mx_vlan_module.md#return-values)

## [Synopsis](meraki_mx_vlan_module.md#id1)

- Create, edit, query, or delete VLANs in a Meraki environment.

## [Parameters](meraki_mx_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **appliance_ip**  string | IP address of appliance.  Address must be within subnet specified in `subnet` parameter. |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **dhcp_boot_filename**  string | Filename to boot from for DHCP boot |
| **dhcp_boot_next_server**  string | DHCP boot option to direct boot clients to the server to load boot file from. |
| **dhcp_boot_options_enabled**  boolean | Enable DHCP boot options  Choices:   - `false` - `true` |
| **dhcp_handling**  string | How to handle DHCP packets on network.  Choices:   - `"Run a DHCP server"` - `"Relay DHCP to another server"` - `"Do not respond to DHCP requests"` - `"none"` - `"server"` - `"relay"` |
| **dhcp_lease_time**  string | DHCP lease timer setting  Choices:   - `"30 minutes"` - `"1 hour"` - `"4 hours"` - `"12 hours"` - `"1 day"` - `"1 week"` |
| **dhcp_options**  list / elements=dictionary | List of DHCP option values |
| **code**  integer | DHCP option number. |
| **type**  string | Type of value for DHCP option.  Choices:   - `"text"` - `"ip"` - `"hex"` - `"integer"` |
| **value**  string | Value for DHCP option. |
| **dhcp_relay_server_ips**  list / elements=string | IP addresses to forward DHCP packets to. |
| **dns_nameservers**  string | Semi-colon delimited list of DNS IP addresses.  Specify one of the following options for preprogrammed DNS entries opendns, google_dns, upstream_dns |
| **fixed_ip_assignments**  list / elements=dictionary | Static IP address assignments to be distributed via DHCP by MAC address. |
| **ip**  string | IP address for fixed IP assignment binding. |
| **mac**  string | MAC address for fixed IP assignment binding. |
| **name**  string | Descriptive name of IP assignment binding. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **name**  aliases: vlan_name  string | Name of VLAN. |
| **net_id**  string | ID of network which VLAN is in or should be in. |
| **net_name**  aliases: network  string | Name of network which VLAN is in or should be in. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **reserved_ip_range**  list / elements=dictionary | IP address ranges which should be reserve and not distributed via DHCP. |
| **comment**  string | Description of IP addresses reservation |
| **end**  string | Last IP address of reserved IP address range, inclusive. |
| **start**  string | First IP address of reserved IP address range, inclusive. |
| **state**  string | Specifies whether object should be queried, created/modified, or removed.  Choices:   - `"absent"` - `"present"` - `"query"` ← (default) |
| **subnet**  string | CIDR notation of network subnet. |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |
| **vlan_id**  integer | ID number of VLAN.  ID should be between 1-4096. |
| **vpn_nat_subnet**  string | The translated VPN subnet if VPN and VPN subnet translation are enabled on the VLAN. |

## [Notes](meraki_mx_vlan_module.md#id3)

> **Note:**
>
> - Meraki’s API will return an error if VLANs aren’t enabled on a network. VLANs are returned properly if VLANs are enabled on a network.
> - Some of the options are likely only used for developers within Meraki.
> - Meraki’s API defaults to networks having VLAN support disabled and there is no way to enable VLANs support in the API. VLAN support must be enabled manually.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mx_vlan_module.md#id4)

```yaml+jinja
- name: Query all VLANs in a network.
  meraki_vlan:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    state: query
  delegate_to: localhost

- name: Query information about a single VLAN by ID.
  meraki_vlan:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    vlan_id: 2
    state: query
  delegate_to: localhost

- name: Create a VLAN.
  meraki_vlan:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    state: present
    vlan_id: 2
    name: TestVLAN
    subnet: 192.0.1.0/24
    appliance_ip: 192.0.1.1
  delegate_to: localhost

- name: Update a VLAN.
  meraki_vlan:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    state: present
    vlan_id: 2
    name: TestVLAN
    subnet: 192.0.1.0/24
    appliance_ip: 192.168.250.2
    fixed_ip_assignments:
      - mac: "13:37:de:ad:be:ef"
        ip: 192.168.250.10
        name: fixed_ip
    reserved_ip_range:
      - start: 192.168.250.10
        end: 192.168.250.20
        comment: reserved_range
    dns_nameservers: opendns
  delegate_to: localhost

- name: Enable DHCP on VLAN with options
  meraki_vlan:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    vlan_id: 2
    name: TestVLAN
    subnet: 192.168.250.0/24
    appliance_ip: 192.168.250.2
    dhcp_handling: server
    dhcp_lease_time: 1 hour
    dhcp_boot_options_enabled: false
    dhcp_options:
      - code: 5
        type: ip
        value: 192.0.1.1
  delegate_to: localhost

- name: Delete a VLAN.
  meraki_vlan:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    state: absent
    vlan_id: 2
  delegate_to: localhost
```

## [Return Values](meraki_mx_vlan_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response**  complex | Information about the organization which was created or modified  Returned: success |
| **appliance_ip**  string | IP address of Meraki appliance in the VLAN  Returned: success  Sample: `"192.0.1.1"` |
| **dhcp_boot_filename**  string | Filename for boot file.  Returned: success  Sample: `"boot.txt"` |
| **dhcp_boot_next_server**  string | DHCP boot option to direct boot clients to the server to load the boot file from.  Returned: success  Sample: `"192.0.1.2"` |
| **dhcp_boot_options_enabled**  boolean | Whether DHCP boot options are enabled.  Returned: success  Sample: `false` |
| **dhcp_handling**  string | Status of DHCP server on VLAN.  Returned: success  Sample: `"Run a DHCP server"` |
| **dhcp_lease_time**  string | DHCP lease time when server is active.  Returned: success  Sample: `"1 day"` |
| **dhcp_options**  complex | DHCP options.  Returned: success |
| **code**  integer | Code for DHCP option.  Integer between 2 and 254.  Returned: success  Sample: `43` |
| **type**  string | Type for DHCP option.  Choices are `text`, `ip`, `hex`, `integer`.  Returned: success  Sample: `"text"` |
| **value**  string | Value for the DHCP option.  Returned: success  Sample: `"192.0.1.2"` |
| **dnsnamservers**  string | IP address or Meraki defined DNS servers which VLAN should use by default  Returned: success  Sample: `"upstream_dns"` |
| **fixed_ip_assignments**  complex | List of MAC addresses which have IP addresses assigned.  Returned: success |
| **macaddress**  complex | MAC address which has IP address assigned to it. Key value is the actual MAC address.  Returned: success |
| **ip**  string | IP address which is assigned to the MAC address.  Returned: success  Sample: `"192.0.1.4"` |
| **name**  string | Descriptive name for binding.  Returned: success  Sample: `"fixed_ip"` |
| **id**  integer | VLAN ID number.  Returned: success  Sample: `2` |
| **name**  string | Descriptive name of VLAN.  Returned: success  Sample: `"TestVLAN"` |
| **networkId**  string | ID number of Meraki network which VLAN is associated to.  Returned: success  Sample: `"N_12345"` |
| **reserved_ip_ranges**  complex | List of IP address ranges which are reserved for static assignment.  Returned: success |
| **comment**  string | Description for IP address reservation.  Returned: success  Sample: `"reserved_range"` |
| **end**  string | Last IP address in reservation range.  Returned: success  Sample: `"192.0.1.10"` |
| **start**  string | First IP address in reservation range.  Returned: success  Sample: `"192.0.1.5"` |
| **subnet**  string | CIDR notation IP subnet of VLAN.  Returned: success  Sample: `"192.0.1.0/24"` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)

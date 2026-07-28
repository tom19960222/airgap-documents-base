---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_mx_third_party_vpn_peers module – Manage third party (IPSec) VPN peers for MX devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_mx_third_party_vpn_peers_module.html
fetched_at: 2026-07-27T17:00:39+00:00
---
# cisco.meraki.meraki_mx_third_party_vpn_peers module – Manage third party (IPSec) VPN peers for MX devices

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
> To use it in a playbook, specify: `cisco.meraki.meraki_mx_third_party_vpn_peers`.

- [Synopsis](meraki_mx_third_party_vpn_peers_module.md#synopsis)
- [Parameters](meraki_mx_third_party_vpn_peers_module.md#parameters)
- [Notes](meraki_mx_third_party_vpn_peers_module.md#notes)
- [Examples](meraki_mx_third_party_vpn_peers_module.md#examples)
- [Return Values](meraki_mx_third_party_vpn_peers_module.md#return-values)

## [Synopsis](meraki_mx_third_party_vpn_peers_module.md#id1)

- Create, edit, query, or delete third party VPN peers in a Meraki environment.

## [Parameters](meraki_mx_third_party_vpn_peers_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **peers**  list / elements=dictionary | The list of VPN peers. |
| **ike_version**  string | The IKE version to be used for the IPsec VPN peer configuration.  Choices:   - `"1"` ← (default) - `"2"` |
| **ipsec_policies**  dictionary | Custom IPSec policies for the VPN peer. If not included and a preset has not been chosen, the default preset for IPSec policies will be used. |
| **child_auth_algo**  list / elements=string | This is the authentication algorithms to be used in Phase 2.  Choices:   - `"sha256"` - `"sha1"` - `"md5"` |
| **child_cipher_algo**  list / elements=string | This is the cipher algorithms to be used in Phase 2.  Choices:   - `"aes256"` - `"aes192"` - `"aes128"` - `"tripledes"` - `"des"` - `"null"` |
| **child_lifetime**  integer | The lifetime of the Phase 2 SA in seconds. |
| **child_pfs_group**  list / elements=string | This is the Diffie-Hellman group to be used for Perfect Forward Secrecy in Phase 2.  Choices:   - `"disabled"` - `"group14"` - `"group5"` - `"group2"` - `"group1"` |
| **ike_auth_algo**  list / elements=string | This is the authentication algorithm to be used in Phase 1.  Choices:   - `"sha256"` - `"sha1"` - `"md5"` |
| **ike_cipher_algo**  list / elements=string | This is the cipher algorithm to be used in Phase 1.  Choices:   - `"aes256"` - `"aes192"` - `"aes128"` - `"tripledes"` - `"des"` |
| **ike_diffie_hellman_group**  list / elements=string | This is the Diffie-Hellman group to be used in Phase 1.  Choices:   - `"group14"` - `"group5"` - `"group2"` - `"group1"` |
| **ike_lifetime**  integer | The lifetime of the Phase 1 SA in seconds. |
| **ike_prf_algo**  list / elements=string | This is the pseudo-random function to be used in IKE_SA.  Choices:   - `"prfsha256"` - `"prfsha1"` - `"prfmd5"` - `"default"` |
| **ipsec_policies_preset**  string | Specifies IPsec preset values. If this is provided, the ‘ipsecPolicies’ parameter is ignored.  Choices:   - `"default"` - `"aws"` - `"azure"` |
| **name**  string | The name of the VPN peer.  Required when state is present. |
| **network_tags**  list / elements=string | A list of network tags that will connect with this peer. If not included, the default is [‘all’]. |
| **private_subnets**  list / elements=string | The list of the private subnets of the VPN peer.  Required when state is present. |
| **public_ip**  string | The public IP of the VPN peer.  Required when state is present. |
| **remote_id**  string | The remote ID is used to identify the connecting VPN peer. This can either be a valid IPv4 Address, FQDN or User FQDN. |
| **secret**  string | The shared secret with the VPN peer.  Required when state is present. |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **state**  string | Specifies whether object should be queried, created/modified, or removed.  Choices:   - `"absent"` - `"present"` - `"query"` ← (default) |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_mx_third_party_vpn_peers_module.md#id3)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mx_third_party_vpn_peers_module.md#id4)

```yaml+jinja
- name: Query all VPN peers
  meraki_mx_third_party_vpn_peers:
    auth_key: abc123
    state: query
    org_name: orgName

- name: Create VPN peer with an IPsec policy
  meraki_mx_third_party_vpn_peers:
    auth_key: abc123
    state: present
    org_name: orgName
    peers:
      - name: "Test peer"
        public_ip: "198.51.100.1"
        secret: "s3cret"
        private_subnets:
          - "192.0.2.0/24"
        ike_version: "2"
        network_tags:
          - none
        remote_id: "192.0.2.0"
        ipsec_policies:
          child_lifetime: 600
          ike_lifetime: 600
          child_auth_algo:
            - "md5"
          child_cipher_algo:
            - "tripledes"
            - "aes192"
          child_pfs_group:
            - "disabled"
          ike_auth_algo:
            - "sha256"
          ike_cipher_algo:
            - "tripledes"
          ike_diffie_hellman_group:
            - "group2"
          ike_prf_algo:
            - "prfmd5"
```

## [Return Values](meraki_mx_third_party_vpn_peers_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response**  complex | Information about the organization which was created or modified  Returned: success |
| **appliance_ip**  string | IP address of Meraki appliance in the VLAN  Returned: success  Sample: `"192.0.1.1"` |
| **dnsnamservers**  string | IP address or Meraki defined DNS servers which VLAN should use by default  Returned: success  Sample: `"upstream_dns"` |
| **peers**  complex | The list of VPN peers.  Returned: success |
| **ike_version**  string | The IKE version to be used for the IPsec VPN peer configuration.  Returned: success  Sample: `"1"` |
| **ipsec_policies**  complex | Custom IPSec policies for the VPN peer.  Returned: success |
| **child_auth_algo**  list / elements=string | This is the authentication algorithms to be used in Phase 2.  Returned: success  Sample: `["sha1"]` |
| **child_cipher_algo**  list / elements=string | This is the cipher algorithms to be used in Phase 2.  Returned: success  Sample: `["aes192"]` |
| **child_lifetime**  string | The lifetime of the Phase 2 SA in seconds.  Returned: success  Sample: `"60"` |
| **child_pfs_group**  list / elements=string | This is the Diffie-Hellman group to be used for Perfect Forward Secrecy in Phase 2.  Returned: success  Sample: `["group14"]` |
| **ike_auth_algo**  list / elements=string | This is the authentication algorithm to be used in Phase 1.  Returned: success  Sample: `["sha1"]` |
| **ike_cipher_algo**  list / elements=string | This is the cipher algorithm to be used in Phase 1.  Returned: success  Sample: `["aes128"]` |
| **ike_diffie_hellman_group**  list / elements=string | This is the Diffie-Hellman group to be used in Phase 1.  Returned: success  Sample: `["group14"]` |
| **ike_lifetime**  string | The lifetime of the Phase 1 SA in seconds.  Returned: success  Sample: `"60"` |
| **ike_prf_algo**  list / elements=string | This is the pseudo-random function to be used in IKE_SA.  Returned: success  Sample: `["prfmd5"]` |
| **ipsec_policies_preset**  string | Preconfigured IPsec settings.  Returned: success  Sample: `"aws"` |
| **name**  string | The name of the VPN peer.  Returned: success  Sample: `"MyVPNPeer"` |
| **network_tags**  list / elements=string | A list of network tags that will connect with this peer.  Returned: success  Sample: `["all"]` |
| **private_subnets**  list / elements=string | The list of the private subnets of the VPN peer.  Returned: success  Sample: `["192.0.2.0/24"]` |
| **public_ip**  string | The public IP of the VPN peer.  Returned: success  Sample: `"198.51.100.1"` |
| **remote_id**  string | The remote ID is used to identify the connecting VPN peer.  Returned: success  Sample: `"s3cret"` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)

---
collection: ansible
version: "6"
title: "community.network.netscaler_gslb_site module – Manage gslb site entities in Netscaler."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/netscaler_gslb_site_module.html
fetched_at: 2026-07-27T17:19:02+00:00
---
# community.network.netscaler_gslb_site module – Manage gslb site entities in Netscaler.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](netscaler_gslb_site_module.md#ansible-collections-community-network-netscaler-gslb-site-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.netscaler_gslb_site`.

- [Synopsis](netscaler_gslb_site_module.md#synopsis)
- [Requirements](netscaler_gslb_site_module.md#requirements)
- [Parameters](netscaler_gslb_site_module.md#parameters)
- [Notes](netscaler_gslb_site_module.md#notes)
- [Examples](netscaler_gslb_site_module.md#examples)
- [Return Values](netscaler_gslb_site_module.md#return-values)

## [Synopsis](netscaler_gslb_site_module.md#id1)

- Manage gslb site entities in Netscaler.

## [Requirements](netscaler_gslb_site_module.md#id2)

The below requirements are needed on the host that executes this module.

- nitro python sdk

## [Parameters](netscaler_gslb_site_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **clip**  string | Cluster IP address. Specify this parameter to connect to the remote cluster site for GSLB auto-sync. Note: The cluster IP address is defined when creating the cluster. |
| **metricexchange**  string | Exchange metrics with other sites. Metrics are exchanged by using Metric Exchange Protocol (MEP). The appliances in the GSLB setup exchange health information once every second.  If you disable metrics exchange, you can use only static load balancing methods (such as round robin, static proximity, or the hash-based methods), and if you disable metrics exchange when a dynamic load balancing method (such as least connection) is in operation, the appliance falls back to round robin. Also, if you disable metrics exchange, you must use a monitor to determine the state of GSLB services. Otherwise, the service is marked as DOWN.  Choices:   - `"enabled"` - `"disabled"` |
| **naptrreplacementsuffix**  string | The naptr replacement suffix configured here will be used to construct the naptr replacement field in NAPTR record.  Minimum length = 1 |
| **nitro_pass**  string / required | The password with which to authenticate to the netscaler node. |
| **nitro_protocol**  string | Which protocol to use when accessing the nitro API objects.  Choices:   - `"http"` ← (default) - `"https"` |
| **nitro_timeout**  float | Time in seconds until a timeout error is thrown when establishing a new session with Netscaler  Default: `310.0` |
| **nitro_user**  string / required | The username with which to authenticate to the netscaler node. |
| **nsip**  string / required | The ip address of the netscaler appliance where the nitro API calls will be made.  The port can be specified with the colon (:). E.g. 192.168.1.1:555. |
| **nwmetricexchange**  string | Exchange, with other GSLB sites, network metrics such as round-trip time (RTT), learned from communications with various local DNS (LDNS) servers used by clients. RTT information is used in the dynamic RTT load balancing method, and is exchanged every 5 seconds.  Choices:   - `"enabled"` - `"disabled"` |
| **parentsite**  string | Parent site of the GSLB site, in a parent-child topology. |
| **publicclip**  string | IP address to be used to globally access the remote cluster when it is deployed behind a NAT. It can be same as the normal cluster IP address. |
| **publicip**  string | Public IP address for the local site. Required only if the appliance is deployed in a private address space and the site has a public IP address hosted on an external firewall or a NAT device.  Minimum length = 1 |
| **save_config**  boolean | If `yes` the module will save the configuration on the netscaler node if it makes any changes.  The module will not save the configuration on the netscaler node if it made no changes.  Choices:   - `false` - `true` ← (default) |
| **sessionexchange**  string | Exchange persistent session entries with other GSLB sites every five seconds.  Choices:   - `"enabled"` - `"disabled"` |
| **siteipaddress**  string | IP address for the GSLB site. The GSLB site uses this IP address to communicate with other GSLB sites. For a local site, use any IP address that is owned by the appliance (for example, a SNIP or MIP address, or the IP address of the ADNS service).  Minimum length = 1 |
| **sitename**  string | Name for the GSLB site. Must begin with an ASCII alphanumeric or underscore `_` character, and must contain only ASCII alphanumeric, underscore `_`, hash `#`, period `.`, space , colon `:`, at `@`, equals `=`, and hyphen `-` characters. Cannot be changed after the virtual server is created.  Minimum length = 1 |
| **sitetype**  string | Type of site to create. If the type is not specified, the appliance automatically detects and sets the type on the basis of the IP address being assigned to the site. If the specified site IP address is owned by the appliance (for example, a MIP address or SNIP address), the site is a local site. Otherwise, it is a remote site.  Choices:   - `"REMOTE"` - `"LOCAL"` |
| **state**  string | The state of the resource being configured by the module on the netscaler node.  When present the resource will be created if needed and configured according to the module’s parameters.  When absent the resource will be deleted from the netscaler node.  Choices:   - `"absent"` - `"present"` ← (default) |
| **triggermonitor**  string | Specify the conditions under which the GSLB service must be monitored by a monitor, if one is bound. Available settings function as follows:  \* `ALWAYS` - Monitor the GSLB service at all times.  \* `MEPDOWN` - Monitor the GSLB service only when the exchange of metrics through the Metrics Exchange Protocol (MEP) is disabled.  `MEPDOWN_SVCDOWN` - Monitor the service in either of the following situations:  \* The exchange of metrics through MEP is disabled.  \* The exchange of metrics through MEP is enabled but the status of the service, learned through metrics exchange, is DOWN.  Choices:   - `"ALWAYS"` - `"MEPDOWN"` - `"MEPDOWN_SVCDOWN"` |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](netscaler_gslb_site_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Citrix NetScaler Network devices see <https://www.ansible.com/ansible-netscaler>.

## [Examples](netscaler_gslb_site_module.md#id5)

```yaml+jinja
- name: Setup gslb site
  delegate_to: localhost
  community.network.netscaler_gslb_site:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

    sitename: gslb-site-1
    siteipaddress: 192.168.1.1
    sitetype: LOCAL
    publicip: 192.168.1.1
    metricexchange: enabled
    nwmetricexchange: enabled
    sessionexchange: enabled
    triggermonitor: ALWAYS
```

## [Return Values](netscaler_gslb_site_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff**  dictionary | List of differences between the actual configured object and the configuration specified in the module  Returned: failure  Sample: `{"targetlbvserver": "difference. ours: (str) server1 other: (str) server2"}` |
| **loglines**  list / elements=string | list of logged messages by the module  Returned: always  Sample: `["['message 1'", " 'message 2']"]` |
| **msg**  string | Message detailing the failure reason  Returned: failure  Sample: `"Action does not exist"` |

### Authors

- George Nikolopoulos (@giorgos-nikolopoulos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)

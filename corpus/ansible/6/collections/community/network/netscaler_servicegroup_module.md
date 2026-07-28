---
collection: ansible
version: "6"
title: "community.network.netscaler_servicegroup module – Manage service group configuration in Netscaler"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/netscaler_servicegroup_module.html
fetched_at: 2026-07-27T17:19:08+00:00
---
# community.network.netscaler_servicegroup module – Manage service group configuration in Netscaler

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
> see [Requirements](netscaler_servicegroup_module.md#ansible-collections-community-network-netscaler-servicegroup-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.netscaler_servicegroup`.

- [Synopsis](netscaler_servicegroup_module.md#synopsis)
- [Requirements](netscaler_servicegroup_module.md#requirements)
- [Parameters](netscaler_servicegroup_module.md#parameters)
- [Notes](netscaler_servicegroup_module.md#notes)
- [Examples](netscaler_servicegroup_module.md#examples)
- [Return Values](netscaler_servicegroup_module.md#return-values)

## [Synopsis](netscaler_servicegroup_module.md#id1)

- Manage service group configuration in Netscaler.
- This module is intended to run either on the ansible control node or a bastion (jumpserver) with access to the actual netscaler instance.

## [Requirements](netscaler_servicegroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- nitro python sdk

## [Parameters](netscaler_servicegroup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **appflowlog**  string | Enable logging of AppFlow information for the specified service group.  Choices:   - `"enabled"` - `"disabled"` |
| **autoscale**  string | Auto scale option for a servicegroup.  Choices:   - `"DISABLED"` - `"DNS"` - `"POLICY"` |
| **cacheable**  boolean | Use the transparent cache redirection virtual server to forward the request to the cache server.  Note: Do not set this parameter if you set the Cache Type.  Choices:   - `false` - `true` |
| **cachetype**  string | Cache type supported by the cache server.  Choices:   - `"TRANSPARENT"` - `"REVERSE"` - `"FORWARD"` |
| **cip**  string | Insert the Client IP header in requests forwarded to the service.  Choices:   - `"enabled"` - `"disabled"` |
| **cipheader**  string | Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If client IP insertion is enabled, and the client IP header is not specified, the value of Client IP Header parameter or the value set by the set ns config command is used as client’s IP header name.  Minimum length = 1 |
| **cka**  boolean | Enable client keep-alive for the service group.  Choices:   - `false` - `true` |
| **clttimeout**  string | Time, in seconds, after which to terminate an idle client connection.  Minimum value = `0`  Maximum value = `31536000` |
| **cmp**  boolean | Enable compression for the specified service.  Choices:   - `false` - `true` |
| **comment**  string | Any information about the service group. |
| **disabled**  boolean | When set to `yes` the service group state will be set to DISABLED.  When set to `no` the service group state will be set to ENABLED.  Note that due to limitations of the underlying NITRO API a `disabled` state change alone does not cause the module result to report a changed status.  Choices:   - `false` ← (default) - `true` |
| **downstateflush**  string | Flush all active transactions associated with all the services in the service group whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.  Choices:   - `"enabled"` - `"disabled"` |
| **graceful**  boolean | Wait for all existing connections to the service to terminate before shutting down the service.  Choices:   - `false` - `true` |
| **healthmonitor**  boolean | Monitor the health of this service. Available settings function as follows:  `yes` - Send probes to check the health of the service.  `no` - Do not send probes to check the health of the service. With the NO option, the appliance shows the service as UP at all times.  Choices:   - `false` - `true` |
| **httpprofilename**  string | Name of the HTTP profile that contains HTTP configuration settings for the service group.  Minimum length = 1  Maximum length = 127 |
| **maxbandwidth**  string | Maximum bandwidth, in Kbps, allocated for all the services in the service group.  Minimum value = `0`  Maximum value = `4294967287` |
| **maxclient**  string | Maximum number of simultaneous open connections for the service group.  Minimum value = `0`  Maximum value = `4294967294` |
| **maxreq**  string | Maximum number of requests that can be sent on a persistent connection to the service group.  Note: Connection requests beyond this value are rejected.  Minimum value = `0`  Maximum value = `65535` |
| **memberport**  string | member port. |
| **monitorbindings**  string | A list of monitornames to bind to this service  Note that the monitors must have already been setup possibly using the [community.network.netscaler_lb_monitor](netscaler_lb_monitor_module.md#ansible-collections-community-network-netscaler-lb-monitor-module) module or some other method |
| **monitorname**  string | The monitor name to bind to this servicegroup. |
| **weight**  string | Weight to assign to the binding between the monitor and servicegroup. |
| **monthreshold**  string | Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.  Minimum value = `0`  Maximum value = `65535` |
| **netprofile**  string | Network profile for the service group.  Minimum length = 1  Maximum length = 127 |
| **nitro_pass**  string / required | The password with which to authenticate to the netscaler node. |
| **nitro_protocol**  string | Which protocol to use when accessing the nitro API objects.  Choices:   - `"http"` ← (default) - `"https"` |
| **nitro_timeout**  float | Time in seconds until a timeout error is thrown when establishing a new session with Netscaler  Default: `310.0` |
| **nitro_user**  string / required | The username with which to authenticate to the netscaler node. |
| **nsip**  string / required | The ip address of the netscaler appliance where the nitro API calls will be made.  The port can be specified with the colon (:). E.g. 192.168.1.1:555. |
| **pathmonitor**  boolean | Path monitoring for clustering.  Choices:   - `false` - `true` |
| **pathmonitorindv**  boolean | Individual Path monitoring decisions.  Choices:   - `false` - `true` |
| **rtspsessionidremap**  boolean | Enable RTSP session ID mapping for the service group.  Choices:   - `false` - `true` |
| **save_config**  boolean | If `yes` the module will save the configuration on the netscaler node if it makes any changes.  The module will not save the configuration on the netscaler node if it made no changes.  Choices:   - `false` - `true` ← (default) |
| **servicegroupname**  string | Name of the service group. Must begin with an ASCII alphabetic or underscore `_` character, and must contain only ASCII alphanumeric, underscore `_`, hash `#`, period `.`, space , colon `:`, at `@`, equals `=`, and hyphen `-` characters. Can be changed after the name is created.  Minimum length = 1 |
| **servicemembers**  string | A list of dictionaries describing each service member of the service group. |
| **customserverid**  string | The identifier for this IP:Port pair.  Used when the persistency type is set to Custom Server ID. |
| **hashid**  string | The hash identifier for the service.  This must be unique for each service.  This parameter is used by hash based load balancing methods.  Minimum value = `1` |
| **ip**  string | IP address of the service. Must not overlap with an existing server entity defined by name. |
| **port**  string | Server port number.  Range `1` - `65535`  \* in CLI is represented as 65535 in NITRO API |
| **serverid**  string | The identifier for the service.  This is used when the persistency type is set to Custom Server ID. |
| **servername**  string | Name of the server to which to bind the service group.  The server must already be configured as a named server.  Minimum length = 1 |
| **state**  string | Initial state of the service after binding.  Choices:   - `"enabled"` - `"disabled"` |
| **weight**  string | Weight to assign to the servers in the service group.  Specifies the capacity of the servers relative to the other servers in the load balancing configuration.  The higher the weight, the higher the percentage of requests sent to the service.  Minimum value = `1`  Maximum value = `100` |
| **servicetype**  string | Protocol used to exchange data with the service.  Choices:   - `"HTTP"` - `"FTP"` - `"TCP"` - `"UDP"` - `"SSL"` - `"SSL_BRIDGE"` - `"SSL_TCP"` - `"DTLS"` - `"NNTP"` - `"RPCSVR"` - `"DNS"` - `"ADNS"` - `"SNMP"` - `"RTSP"` - `"DHCPRA"` - `"ANY"` - `"SIP_UDP"` - `"SIP_TCP"` - `"SIP_SSL"` - `"DNS_TCP"` - `"ADNS_TCP"` - `"MYSQL"` - `"MSSQL"` - `"ORACLE"` - `"RADIUS"` - `"RADIUSListener"` - `"RDP"` - `"DIAMETER"` - `"SSL_DIAMETER"` - `"TFTP"` - `"SMPP"` - `"PPTP"` - `"GRE"` - `"SYSLOGTCP"` - `"SYSLOGUDP"` - `"FIX"` - `"SSL_FIX"` |
| **sp**  boolean | Enable surge protection for the service group.  Choices:   - `false` - `true` |
| **state**  string | The state of the resource being configured by the module on the netscaler node.  When present the resource will be created if needed and configured according to the module’s parameters.  When absent the resource will be deleted from the netscaler node.  Choices:   - `"absent"` - `"present"` ← (default) |
| **svrtimeout**  string | Time, in seconds, after which to terminate an idle server connection.  Minimum value = `0`  Maximum value = `31536000` |
| **tcpb**  boolean | Enable TCP buffering for the service group.  Choices:   - `false` - `true` |
| **tcpprofilename**  string | Name of the TCP profile that contains TCP configuration settings for the service group.  Minimum length = 1  Maximum length = 127 |
| **useproxyport**  boolean | Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection.  Note: This parameter is available only when the Use Source IP `usip` parameter is set to `yes`.  Choices:   - `false` - `true` |
| **usip**  boolean | Use client’s IP address as the source IP address when initiating connection to the server. With the NO setting, which is the default, a mapped IP (MIP) address or subnet IP (SNIP) address is used as the source IP address to initiate server side connections.  Choices:   - `false` - `true` |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](netscaler_servicegroup_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Citrix NetScaler Network devices see <https://www.ansible.com/ansible-netscaler>.

## [Examples](netscaler_servicegroup_module.md#id5)

```yaml+jinja
# The LB Monitors monitor-1 and monitor-2 must already exist
# Service members defined by C(ip) must not redefine an existing server's ip address.
# Service members defined by C(servername) must already exist.

- name: Setup http service with ip members
  delegate_to: localhost
  community.network.netscaler_servicegroup:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

    state: present

    servicegroupname: service-group-1
    servicetype: HTTP
    servicemembers:
      - ip: 10.78.78.78
        port: 80
        weight: 50
      - ip: 10.79.79.79
        port: 80
        weight: 40
      - servername: server-1
        port: 80
        weight: 10

    monitorbindings:
      - monitorname: monitor-1
        weight: 50
      - monitorname: monitor-2
        weight: 50
```

## [Return Values](netscaler_servicegroup_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff**  dictionary | List of differences between the actual configured object and the configuration specified in the module  Returned: failure  Sample: `{"clttimeout": "difference. ours: (float) 10.0 other: (float) 20.0"}` |
| **loglines**  list / elements=string | list of logged messages by the module  Returned: always  Sample: `["message 1", "message 2"]` |
| **msg**  string | Message detailing the failure reason  Returned: failure  Sample: `"Action does not exist"` |

### Authors

- George Nikolopoulos (@giorgos-nikolopoulos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)

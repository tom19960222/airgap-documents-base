---
collection: ansible
version: "8"
title: "community.network.netscaler_service module – Manage service configuration in Netscaler"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/netscaler_service_module.html
fetched_at: 2026-07-28T01:57:12+00:00
---
# community.network.netscaler_service module – Manage service configuration in Netscaler

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](netscaler_service_module.md#ansible-collections-community-network-netscaler-service-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.netscaler_service`.

- [Synopsis](netscaler_service_module.md#synopsis)
- [Requirements](netscaler_service_module.md#requirements)
- [Parameters](netscaler_service_module.md#parameters)
- [Notes](netscaler_service_module.md#notes)
- [Examples](netscaler_service_module.md#examples)
- [Return Values](netscaler_service_module.md#return-values)

## [Synopsis](netscaler_service_module.md#id1)

- Manage service configuration in Netscaler.
- This module allows the creation, deletion and modification of Netscaler services.
- This module is intended to run either on the ansible control node or a bastion (jumpserver) with access to the actual netscaler instance.
- This module supports check mode.

Aliases: network.netscaler.netscaler_service

## [Requirements](netscaler_service_module.md#id2)

The below requirements are needed on the host that executes this module.

- nitro python sdk

## [Parameters](netscaler_service_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accessdown**  boolean | Use Layer 2 mode to bridge the packets sent to this service if it is marked as DOWN. If the service is DOWN, and this parameter is disabled, the packets are dropped.  **Choices:**   - `false` ← (default) - `true` |
| **appflowlog**  string | Enable logging of AppFlow information.  **Choices:**   - `"enabled"` - `"disabled"` |
| **cacheable**  boolean | Use the transparent cache redirection virtual server to forward requests to the cache server.  Note: Do not specify this parameter if you set the Cache Type parameter.  **Choices:**   - `false` ← (default) - `true` |
| **cachetype**  string | Cache type supported by the cache server.  **Choices:**   - `"TRANSPARENT"` - `"REVERSE"` - `"FORWARD"` |
| **cip**  string | Before forwarding a request to the service, insert an HTTP header with the client’s IPv4 or IPv6 address as its value. Used if the server needs the client’s IP address for security, accounting, or other purposes, and setting the Use Source IP parameter is not a viable option.  **Choices:**   - `"enabled"` - `"disabled"` |
| **cipheader**  string | Name for the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If you set the Client IP parameter, and you do not specify a name for the header, the appliance uses the header name specified for the global Client IP Header parameter (the cipHeader parameter in the set ns param CLI command or the Client IP Header parameter in the Configure HTTP Parameters dialog box at System > Settings > Change HTTP parameters). If the global Client IP Header parameter is not specified, the appliance inserts a header with the name “client-ip.”.  Minimum length = 1 |
| **cka**  boolean | Enable client keep-alive for the service.  **Choices:**   - `false` - `true` |
| **cleartextport**  string | Port to which clear text data must be sent after the appliance decrypts incoming SSL traffic. Applicable to transparent SSL services.  Minimum value = 1 |
| **clttimeout**  string | Time, in seconds, after which to terminate an idle client connection.  Minimum value = 0  Maximum value = 31536000 |
| **cmp**  boolean | Enable compression for the service.  **Choices:**   - `false` - `true` |
| **comment**  string | Any information about the service. |
| **customserverid**  string | Unique identifier for the service. Used when the persistency type for the virtual server is set to Custom Server ID.  **Default:** `"None"` |
| **disabled**  boolean | When set to `yes` the service state will be set to DISABLED.  When set to `no` the service state will be set to ENABLED.  Note that due to limitations of the underlying NITRO API a `disabled` state change alone does not cause the module result to report a changed status.  **Choices:**   - `false` ← (default) - `true` |
| **dnsprofilename**  string | Name of the DNS profile to be associated with the service. DNS profile properties will applied to the transactions processed by a service. This parameter is valid only for ADNS and ADNS-TCP services.  Minimum length = 1  Maximum length = 127 |
| **downstateflush**  string | Flush all active transactions associated with a service whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.  **Choices:**   - `"enabled"` - `"disabled"` |
| **graceful**  boolean | Shut down gracefully, not accepting any new connections, and disabling the service when all of its connections are closed.  **Choices:**   - `false` ← (default) - `true` |
| **hashid**  string | A numerical identifier that can be used by hash based load balancing methods. Must be unique for each service.  Minimum value = 1 |
| **healthmonitor**  boolean | Monitor the health of this service  **Choices:**   - `false` - `true` ← (default) |
| **httpprofilename**  string | Name of the HTTP profile that contains HTTP configuration settings for the service.  Minimum length = 1  Maximum length = 127 |
| **ip**  string | IP to assign to the service.  Minimum length = 1 |
| **ipaddress**  string | The new IP address of the service. |
| **maxbandwidth**  string | Maximum bandwidth, in Kbps, allocated to the service.  Minimum value = 0  Maximum value = 4294967287 |
| **maxclient**  string | Maximum number of simultaneous open connections to the service.  Minimum value = 0  Maximum value = 4294967294 |
| **maxreq**  string | Maximum number of requests that can be sent on a persistent connection to the service.  Note: Connection requests beyond this value are rejected.  Minimum value = 0  Maximum value = 65535 |
| **monitor_bindings**  string | A list of load balancing monitors to bind to this service.  Each monitor entry is a dictionary which may contain the following options.  Note that if not using the built in monitors they must first be setup. |
| **dup_state**  string | State of the monitor.  The state setting for a monitor of a given type affects all monitors of that type.  For example, if an HTTP monitor is enabled, all HTTP monitors on the appliance are (or remain) enabled.  If an HTTP monitor is disabled, all HTTP monitors on the appliance are disabled.  **Choices:**   - `"enabled"` - `"disabled"` |
| **dup_weight**  string | Weight to assign to the binding between the monitor and service. |
| **monitorname**  string | Name of the monitor. |
| **weight**  string | Weight to assign to the binding between the monitor and service. |
| **monthreshold**  string | Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.  Minimum value = 0  Maximum value = 65535 |
| **name**  string | Name for the service. Must begin with an ASCII alphabetic or underscore `_` character, and must contain only ASCII alphanumeric, underscore `_`, hash `#`, period `.`, space , colon `:`, at `@`, equals `=`, and hyphen `-` characters. Cannot be changed after the service has been created.  Minimum length = 1 |
| **netprofile**  string | Network profile to use for the service.  Minimum length = 1  Maximum length = 127 |
| **nitro_pass**  string / required | The password with which to authenticate to the netscaler node. |
| **nitro_protocol**  string | Which protocol to use when accessing the nitro API objects.  **Choices:**   - `"http"` ← (default) - `"https"` |
| **nitro_timeout**  float | Time in seconds until a timeout error is thrown when establishing a new session with Netscaler  **Default:** `310.0` |
| **nitro_user**  string / required | The username with which to authenticate to the netscaler node. |
| **nsip**  string / required | The ip address of the netscaler appliance where the nitro API calls will be made.  The port can be specified with the colon (:). E.g. 192.168.1.1:555. |
| **pathmonitor**  string | Path monitoring for clustering. |
| **pathmonitorindv**  string | Individual Path monitoring decisions. |
| **port**  string | Port number of the service.  Range 1 - 65535  \* in CLI is represented as 65535 in NITRO API |
| **processlocal**  string | By turning on this option packets destined to a service in a cluster will not under go any steering. Turn this option for single packet request response mode or when the upstream device is performing a proper RSS for connection based distribution.  **Choices:**   - `"enabled"` - `"disabled"` |
| **rtspsessionidremap**  boolean | Enable RTSP session ID mapping for the service.  **Choices:**   - `false` ← (default) - `true` |
| **save_config**  boolean | If `yes` the module will save the configuration on the netscaler node if it makes any changes.  The module will not save the configuration on the netscaler node if it made no changes.  **Choices:**   - `false` - `true` ← (default) |
| **serverid**  string | The identifier for the service. This is used when the persistency type is set to Custom Server ID. |
| **servername**  string | Name of the server that hosts the service.  Minimum length = 1 |
| **servicetype**  string | Protocol in which data is exchanged with the service.  **Choices:**   - `"HTTP"` - `"FTP"` - `"TCP"` - `"UDP"` - `"SSL"` - `"SSL_BRIDGE"` - `"SSL_TCP"` - `"DTLS"` - `"NNTP"` - `"RPCSVR"` - `"DNS"` - `"ADNS"` - `"SNMP"` - `"RTSP"` - `"DHCPRA"` - `"ANY"` - `"SIP_UDP"` - `"SIP_TCP"` - `"SIP_SSL"` - `"DNS_TCP"` - `"ADNS_TCP"` - `"MYSQL"` - `"MSSQL"` - `"ORACLE"` - `"RADIUS"` - `"RADIUSListener"` - `"RDP"` - `"DIAMETER"` - `"SSL_DIAMETER"` - `"TFTP"` - `"SMPP"` - `"PPTP"` - `"GRE"` - `"SYSLOGTCP"` - `"SYSLOGUDP"` - `"FIX"` - `"SSL_FIX"` |
| **sp**  boolean | Enable surge protection for the service.  **Choices:**   - `false` - `true` |
| **state**  string | The state of the resource being configured by the module on the netscaler node.  When present the resource will be created if needed and configured according to the module’s parameters.  When absent the resource will be deleted from the netscaler node.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **svrtimeout**  string | Time, in seconds, after which to terminate an idle server connection.  Minimum value = 0  Maximum value = 31536000 |
| **tcpb**  boolean | Enable TCP buffering for the service.  **Choices:**   - `false` - `true` |
| **tcpprofilename**  string | Name of the TCP profile that contains TCP configuration settings for the service.  Minimum length = 1  Maximum length = 127 |
| **td**  string | Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.  Minimum value = 0  Maximum value = 4094 |
| **useproxyport**  boolean | Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection.  Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES.  **Choices:**   - `false` - `true` |
| **usip**  boolean | Use the client’s IP address as the source IP address when initiating a connection to the server. When creating a service, if you do not set this parameter, the service inherits the global Use Source IP setting (available in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes > Configure Modes dialog box). However, you can override this setting after you create the service.  **Choices:**   - `false` - `true` |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](netscaler_service_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Citrix NetScaler Network devices see <https://www.ansible.com/ansible-netscaler>.

## [Examples](netscaler_service_module.md#id5)

```yaml+jinja
# Monitor monitor-1 must have been already setup

- name: Setup http service
  gather_facts: false
  delegate_to: localhost
  community.network.netscaler_service:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

    state: present

    name: service-http-1
    servicetype: HTTP
    ipaddress: 10.78.0.1
    port: 80

    monitor_bindings:
      - monitor-1
```

## [Return Values](netscaler_service_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff**  dictionary | A dictionary with a list of differences between the actual configured object and the configuration specified in the module  **Returned:** failure  **Sample:** `{"clttimeout": "difference. ours: (float) 10.0 other: (float) 20.0"}` |
| **loglines**  list / elements=string | list of logged messages by the module  **Returned:** always  **Sample:** `["['message 1'", " 'message 2']"]` |

### Authors

- George Nikolopoulos (@giorgos-nikolopoulos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)

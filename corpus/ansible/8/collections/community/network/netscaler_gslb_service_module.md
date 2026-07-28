---
collection: ansible
version: "8"
title: "community.network.netscaler_gslb_service module – Manage gslb service entities in Netscaler."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/netscaler_gslb_service_module.html
fetched_at: 2026-07-28T01:57:06+00:00
---
# community.network.netscaler_gslb_service module – Manage gslb service entities in Netscaler.

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
> see [Requirements](netscaler_gslb_service_module.md#ansible-collections-community-network-netscaler-gslb-service-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.netscaler_gslb_service`.

- [Synopsis](netscaler_gslb_service_module.md#synopsis)
- [Requirements](netscaler_gslb_service_module.md#requirements)
- [Parameters](netscaler_gslb_service_module.md#parameters)
- [Notes](netscaler_gslb_service_module.md#notes)
- [Examples](netscaler_gslb_service_module.md#examples)
- [Return Values](netscaler_gslb_service_module.md#return-values)

## [Synopsis](netscaler_gslb_service_module.md#id1)

- Manage gslb service entities in Netscaler.

Aliases: network.netscaler.netscaler_gslb_service

## [Requirements](netscaler_gslb_service_module.md#id2)

The below requirements are needed on the host that executes this module.

- nitro python sdk

## [Parameters](netscaler_gslb_service_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **appflowlog**  string | Enable logging appflow flow information.  **Choices:**   - `"enabled"` - `"disabled"` |
| **cip**  string | In the request that is forwarded to the GSLB service, insert a header that stores the client’s IP address. Client IP header insertion is used in connection-proxy based site persistence.  **Choices:**   - `"enabled"` - `"disabled"` |
| **cipheader**  string | Name for the HTTP header that stores the client’s IP address. Used with the Client IP option. If client IP header insertion is enabled on the service and a name is not specified for the header, the NetScaler appliance uses the name specified by the cipHeader parameter in the set ns param command or, in the GUI, the Client IP Header parameter in the Configure HTTP Parameters dialog box.  Minimum length = 1 |
| **clttimeout**  string | Idle time, in seconds, after which a client connection is terminated. Applicable if connection proxy based site persistence is used.  Minimum value = 0  Maximum value = 31536000 |
| **cnameentry**  string | Canonical name of the GSLB service. Used in CNAME-based GSLB.  Minimum length = 1 |
| **comment**  string | Any comments that you might want to associate with the GSLB service. |
| **downstateflush**  string | Flush all active transactions associated with the GSLB service when its state transitions from UP to DOWN. Do not enable this option for services that must complete their transactions. Applicable if connection proxy based site persistence is used.  **Choices:**   - `"enabled"` - `"disabled"` |
| **hashid**  string | Unique hash identifier for the GSLB service, used by hash based load balancing methods.  Minimum value = `1` |
| **healthmonitor**  boolean | Monitor the health of the GSLB service.  **Choices:**   - `false` - `true` |
| **ipaddress**  string | IP address for the GSLB service. Should represent a load balancing, content switching, or VPN virtual server on the NetScaler appliance, or the IP address of another load balancing device. |
| **maxaaausers**  string | Maximum number of SSL VPN users that can be logged on concurrently to the VPN virtual server that is represented by this GSLB service. A GSLB service whose user count reaches the maximum is not considered when a GSLB decision is made, until the count drops below the maximum.  Minimum value = `0`  Maximum value = `65535` |
| **maxbandwidth**  string | Integer specifying the maximum bandwidth allowed for the service. A GSLB service whose bandwidth reaches the maximum is not considered when a GSLB decision is made, until its bandwidth consumption drops below the maximum. |
| **maxclient**  string | The maximum number of open connections that the service can support at any given time. A GSLB service whose connection count reaches the maximum is not considered when a GSLB decision is made, until the connection count drops below the maximum.  Minimum value = `0`  Maximum value = `4294967294` |
| **monitor_bindings**  string | Bind monitors to this gslb service |
| **monitor_name**  string | Monitor name. |
| **weight**  string | Weight to assign to the monitor-service binding.  A larger number specifies a greater weight.  Contributes to the monitoring threshold, which determines the state of the service.  Minimum value = `1`  Maximum value = `100` |
| **monthreshold**  string | Monitoring threshold value for the GSLB service. If the sum of the weights of the monitors that are bound to this GSLB service and are in the UP state is not equal to or greater than this threshold value, the service is marked as DOWN.  Minimum value = `0`  Maximum value = `65535` |
| **nitro_pass**  string / required | The password with which to authenticate to the netscaler node. |
| **nitro_protocol**  string | Which protocol to use when accessing the nitro API objects.  **Choices:**   - `"http"` ← (default) - `"https"` |
| **nitro_timeout**  float | Time in seconds until a timeout error is thrown when establishing a new session with Netscaler  **Default:** `310.0` |
| **nitro_user**  string / required | The username with which to authenticate to the netscaler node. |
| **nsip**  string / required | The ip address of the netscaler appliance where the nitro API calls will be made.  The port can be specified with the colon (:). E.g. 192.168.1.1:555. |
| **port**  string | Port on which the load balancing entity represented by this GSLB service listens.  Minimum value = 1  Range 1 - 65535  \* in CLI is represented as 65535 in NITRO API |
| **publicip**  string | The public IP address that a NAT device translates to the GSLB service’s private IP address. Optional. |
| **publicport**  string | The public port associated with the GSLB service’s public IP address. The port is mapped to the service’s private port number. Applicable to the local GSLB service. Optional. |
| **save_config**  boolean | If `yes` the module will save the configuration on the netscaler node if it makes any changes.  The module will not save the configuration on the netscaler node if it made no changes.  **Choices:**   - `false` - `true` ← (default) |
| **servername**  string | Name of the server hosting the GSLB service.  Minimum length = 1 |
| **servicename**  string | Name for the GSLB service. Must begin with an ASCII alphanumeric or underscore `_` character, and must contain only ASCII alphanumeric, underscore `_`, hash `#`, period `.`, space, colon `:`, at `@`, equals `=`, and hyphen `-` characters. Can be changed after the GSLB service is created.  Minimum length = 1 |
| **servicetype**  string | Type of service to create.  **Choices:**   - `"HTTP"` - `"FTP"` - `"TCP"` - `"UDP"` - `"SSL"` - `"SSL_BRIDGE"` - `"SSL_TCP"` - `"NNTP"` - `"ANY"` - `"SIP_UDP"` - `"SIP_TCP"` - `"SIP_SSL"` - `"RADIUS"` - `"RDP"` - `"RTSP"` - `"MYSQL"` - `"MSSQL"` - `"ORACLE"` |
| **sitename**  string | Name of the GSLB site to which the service belongs.  Minimum length = 1 |
| **sitepersistence**  string | Use cookie-based site persistence. Applicable only to `HTTP` and `SSL` GSLB services.  **Choices:**   - `"ConnectionProxy"` - `"HTTPRedirect"` - `"NONE"` |
| **siteprefix**  string | The site’s prefix string. When the service is bound to a GSLB virtual server, a GSLB site domain is generated internally for each bound service-domain pair by concatenating the site prefix of the service and the name of the domain. If the special string NONE is specified, the site-prefix string is unset. When implementing HTTP redirect site persistence, the NetScaler appliance redirects GSLB requests to GSLB services by using their site domains. |
| **state**  string | The state of the resource being configured by the module on the netscaler node.  When present the resource will be created if needed and configured according to the module’s parameters.  When absent the resource will be deleted from the netscaler node.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](netscaler_gslb_service_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Citrix NetScaler Network devices see <https://www.ansible.com/ansible-netscaler>.

## [Examples](netscaler_gslb_service_module.md#id5)

```yaml+jinja
- name: Setup gslb service 2

  delegate_to: localhost
  register: result
  check_mode: "{{ check_mode }}"

  community.network.netscaler_gslb_service:
    operation: present

    servicename: gslb-service-2
    cnameentry: example.com
    sitename: gslb-site-1
```

## [Return Values](netscaler_gslb_service_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff**  dictionary | List of differences between the actual configured object and the configuration specified in the module  **Returned:** failure  **Sample:** `{"targetlbvserver": "difference. ours: (str) server1 other: (str) server2"}` |
| **loglines**  list / elements=string | list of logged messages by the module  **Returned:** always  **Sample:** `["['message 1'", " 'message 2']"]` |
| **msg**  string | Message detailing the failure reason  **Returned:** failure  **Sample:** `"Action does not exist"` |

### Authors

- George Nikolopoulos (@giorgos-nikolopoulos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)

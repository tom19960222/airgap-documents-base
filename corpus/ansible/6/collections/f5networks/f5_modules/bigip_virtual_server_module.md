---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_virtual_server module – Manage LTM virtual servers on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_virtual_server_module.html
fetched_at: 2026-07-27T17:28:02+00:00
---
# f5networks.f5_modules.bigip_virtual_server module – Manage LTM virtual servers on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_virtual_server`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_virtual_server_module.md#synopsis)
- [Parameters](bigip_virtual_server_module.md#parameters)
- [Notes](bigip_virtual_server_module.md#notes)
- [Examples](bigip_virtual_server_module.md#examples)
- [Return Values](bigip_virtual_server_module.md#return-values)

## [Synopsis](bigip_virtual_server_module.md#id1)

- Manage LTM virtual servers on a BIG-IP system.

## [Parameters](bigip_virtual_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address_translation**  boolean | When `enabled`, specifies the system translates the address of the virtual server.  When `disabled`, specifies the system uses the address without translation.  This option is useful when the system is load balancing devices that have the same IP address.  When creating a new virtual server, the default is `enabled`.  Choices:   - `false` - `true` |
| **auto_last_hop**  string  added in f5networks.f5_modules 1.13.0 | Allows the BIG-IP system to track the source MAC address of incoming connections and return traffic from pools to the source MAC address, regardless of the routing table.  Choices:   - `"default"` - `"enabled"` - `"disabled"` |
| **bypass_module_checks**  boolean  added in f5networks.f5_modules 1.3.0 | Disables all built-in module verification checks that require BIG-IP device calls. Using this option cuts down on the number of REST calls made by this module. The trade off is that most parameters are sent as is, which requires extra care when defining them.  The device is the final source of truth for such configurations, usable in cases where speed is preferred over accuracy.  If set to `yes`, the module ignores the value op `check_profiles` parameter.  This parameter can be used when creating new or updating existing resources.  Choices:   - `false` ← (default) - `true` |
| **check_profiles**  boolean  added in f5networks.f5_modules 1.2.0 | Specifies whether the client and server SSL profiles specified by the user should be verified to be correct against the existing profiles. This is useful in cases where a large number of profiles are being added at once.  Not recommended for common use. In case of duplicate profiles, or erroneous profiles, the BIG-IP throws an error.  Choices:   - `false` - `true` ← (default) |
| **clone_pools**  list / elements=dictionary | Specifies a pool or list of pools that the virtual server uses to replicate either client-side or server-side traffic.  Typically this option is used for intrusion detection. |
| **context**  string / required | The context option for a clone pool to replicate either client-side or server-side traffic.  Choices:   - `"clientside"` - `"serverside"` |
| **pool_name**  string / required | The pool name to which the server replicates the traffic.  Only pools created on the Common partition or on the same partition as the virtual server can be used.  Referencing a pool on the Common partition needs to be done in the full path format, for example, `/Common/pool_name`. |
| **default_persistence_profile**  string | Default profile which manages the session persistence.  If you want to remove the existing default persistence profile, specify an empty value; `""`. See the documentation for an example.  When `type` is `dhcp`, this parameter is ignored. |
| **description**  string | Virtual server description. |
| **destination**  aliases: address, ip  string | Destination IP of the virtual server.  Required when `state` is `present` and the virtual server does not exist.  When `type` is `internal`, this parameter is ignored. For all other types, it is required.  Destination can also be specified as a name for an existing Virtual Address. |
| **disabled_vlans**  list / elements=string | List of VLANs to be disabled. If the partition is not specified in the VLAN, the `partition` option of this module is used.  This parameter is mutually exclusive with the `enabled_vlans` parameters. |
| **enabled_vlans**  list / elements=string | List of VLANs to enable. When a VLAN named `all` is used, all VLANs will be allowed. VLANs can be specified with or without the leading partition. If the partition is not specified in the VLAN, the `partition` option of this module is used.  This parameter is mutually exclusive with the `disabled_vlans` parameter. |
| **fallback_persistence_profile**  string | Specifies the persistence profile you want the system to use if it cannot use the specified default persistence profile.  If you want to remove the existing fallback persistence profile, specify an empty value; `""`. See the documentation for an example.  When `type` is `dhcp`, this parameter is ignored. |
| **firewall_enforced_policy**  string | Applies the specified AFM policy to the virtual in an enforcing way.  When creating a new virtual, if this parameter is not specified, the enforced policy is disabled. |
| **firewall_staged_policy**  string | Applies the specified AFM policy to the virtual in an enforcing way.  A staged policy shows the results of the policy rules in the log, while not actually applying the rules to traffic.  When creating a new virtual, if this parameter is not specified, the staged policy is disabled. |
| **insert_metadata**  boolean | When set to `no`, the module does not set metadata on the device.  Currently there is a limitation that non-admin users cannot set metadata on the object, despite being able to create and modify virtual server objects. Setting this option to `no` allows such users to use this module to manage virtual server objects on the device.  Attempting to change `state` on Virtual Server that belongs to an iAPP with strict updates enabled will result in error message returned by device, unless `insert_metadata` parameter is set to `no`.  Choices:   - `false` - `true` ← (default) |
| **ip_intelligence_policy**  string | Specifies the IP intelligence policy applied to the virtual server.  This parameter requires a valid BIG-IP security module is provisioned, such as ASM or AFM. |
| **ip_protocol**  string | Specifies a network protocol name you want the system to use to direct traffic on this virtual server.  When creating a new virtual server, if this parameter is not specified, the default is `tcp`.  The Protocol setting is not available when you select Performance (HTTP) as the `Type`.  The value of this argument can be specified in either its numeric value, or in a select number of named values. Refer to `choices` for examples.  For a list of valid IP protocol numbers, refer to <https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers>.  When `type` is `dhcp`, this module forces the `ip_protocol` parameter to `17` (UDP).  Choices:   - `"ah"` - `"any"` - `"bna"` - `"esp"` - `"etherip"` - `"gre"` - `"icmp"` - `"ipencap"` - `"ipv6"` - `"ipv6-auth"` - `"ipv6-crypt"` - `"ipv6-icmp"` - `"isp-ip"` - `"mux"` - `"ospf"` - `"sctp"` - `"tcp"` - `"udp"` - `"udplite"` |
| **irules**  aliases: all_rules  list / elements=string | Specifies a list of rules to be applied in priority order.  If you want to remove existing iRules, specify a single empty value; `""`. See the documentation for an example.  The order in which iRules are specified does matter, so a list that contains the same list elements but in a different order in the playbook will make changes on the device.  When `type` is `dhcp`, `stateless`, `reject`, or `internal`, this parameter is ignored. |
| **mask**  string | Specifies the destination address network mask. This parameter works with IPv4 and IPv6 addresses.  This is an optional parameter which can be specified when creating or updating virtual server.  If `destination` is set in CIDR notation format and `mask` is provided, the `mask` parameter takes precedence.  If you specify a catchall destination (for example, `0.0.0.0` for IPv4, `::` for IPv6) the mask parameter is set to `any` or `any6` respectively.  When the `destination` is not in CIDR notation and a `mask` is not specified, `255.255.255.255` or `ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff` is set for IPv4 and IPv6 addresses respectively.  When `destination` is provided in CIDR notation format and a `mask` is not specified, the mask parameter is inferred from `destination`.  When `destination` is provided as a virtual address name, and a `mask` is not specified, the mask will be `None`, allowing device set it with its internal defaults. |
| **metadata**  any | Arbitrary key/value pairs you can attach to a virtual server. This is useful in situations where you want to annotate a virtual to be managed by Ansible.  Key names are stored as strings; this includes names that are numbers.  Values for all of the keys are stored as strings; this includes values that are numbers.  Data is persisted, not ephemeral. |
| **mirror**  boolean | Specifies the system mirrors connections on each member of a redundant pair.  When creating a new virtual server, if this parameter is not specified, the default is `disabled`.  Choices:   - `false` - `true` |
| **name**  aliases: vs  string / required | Virtual server name. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **policies**  aliases: all_policies  list / elements=string | Specifies the policies for the virtual server.  When `type` is `dhcp`, `reject`, or `internal`, this parameter is ignored. |
| **pool**  string | Default pool for the virtual server.  If you want to remove the existing pool, specify an empty value; `""`. See the documentation for an example.  When creating a new virtual server, and `type` is `stateless`, this parameter is required.  If `type` is `stateless`, the `pool` must not have any members which define a `rate_limit`. |
| **port**  string | Port of the virtual server. Required when `state` is `present` and the virtual server does not exist.  If you do not want to specify a particular port, use the value `0`. This means the virtual server listens on any port.  When `type` is `dhcp`, this module forces the `port` parameter to `67`.  When `type` is `internal`, this module forces the `port` parameter to `0`.  In addition to specifying a port number, a select number of service names may also be provided.  The string `ftp` may be substituted for for port `21`.  The string `http` may be substituted for for port `80`.  The string `https` may be substituted for for port `443`.  The string `telnet` may be substituted for for port `23`.  The string `smtp` may be substituted for for port `25`.  The string `snmp` may be substituted for for port `161`.  The string `snmp-trap` may be substituted for for port `162`.  The string `ssh` may be substituted for for port `22`.  The string `tftp` may be substituted for for port `69`.  The string `isakmp` may be substituted for for port `500`.  The string `mqtt` may be substituted for for port `1883`.  The string `mqtt-tls` may be substituted for for port `8883`. |
| **port_translation**  boolean | When `enabled`, specifies the system translates the port of the virtual server.  When `disabled`, specifies the system uses the port without translation. Turning off port translation for a virtual server is useful if you want to use the virtual server to load balance connections to any service.  When creating a new virtual server, the default is `enabled`.  Choices:   - `false` - `true` |
| **profiles**  aliases: all_profiles  any | List of profiles (HTTP, ClientSSL, ServerSSL, etc) to apply to both sides of the connection (client-side and server-side).  If you only want to apply a particular profile to the client-side of the connection, specify `client-side` for the profile’s `context`.  If you only want to apply a particular profile to the server-side of the connection, specify `server-side` for the profile’s `context`.  If `context` is not provided, it will default to `all`.  If you want to remove a profile from the list of profiles currently active on the virtual, simply remove it from the `profiles` list. See examples for an illustration of this.  If you want to add a profile to the list of profiles currently active on the virtual, simply add it to the `profiles` list. See examples for an illustration of this.  **Profiles are important**. This module will fail to configure a BIG-IP if you mix up your profiles, or if you attempt to set an IP protocol which your current, or new, profiles do not support. Both this module, and BIG-IP, will report an error if this is incorrect, resembling `lists profiles incompatible with its protocol`.  If you are unsure what the correct profile combinations are, we suggest having a BIG-IP available in which you can make changes and copy what the correct combinations are.  To use `http2` in full proxy to enable `HTTP MRF Router` option seen in the GUI you need to assign `/Common/httprouter` profile with `context` set to `all`. See the bottom of examples section below. |
| **context**  string | The side of the connection on which the profile should be applied.  Choices:   - `"all"` ← (default) - `"server-side"` - `"client-side"` |
| **name**  string | Name of the profile.  This must be specified if a context is specified.  If this is not specified, it is assumed the profile item is only a name of a profile. |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **rate_limit**  integer | Virtual server rate limit (connections-per-second). Setting this to `0` disables the limit.  The valid value range is `0` - `4294967295`. |
| **rate_limit_dst_mask**  integer | Specifies a mask, in bits, to be applied to the destination address as part of the rate limiting.  The default value is `0`, which is equivalent to using the entire address - `32` in IPv4, or `128` in IPv6.  The valid value range is `0` - `4294967295`. |
| **rate_limit_mode**  string | Indicates whether the rate limit is applied per virtual object, per source address, per destination address, or some combination thereof.  The default value is `object`, which does not use the source or destination address as part of the key.  Choices:   - `"object"` ← (default) - `"object-source"` - `"object-destination"` - `"object-source-destination"` - `"destination"` - `"source"` - `"source-destination"` |
| **rate_limit_src_mask**  integer | Specifies a mask, in bits, to be applied to the source address as part of the rate limiting.  The default value is `0`, which is equivalent to using the entire address - `32` in IPv4, or `128` in IPv6.  The valid value range is `0` - `4294967295`. |
| **security_log_profiles**  list / elements=string | Specifies the log profile applied to the virtual server.  To make use of this feature, the AFM module must be licensed and provisioned.  The `Log all requests` and `Log illegal requests` are mutually exclusive and therefore, this module raises an error if the two are specified together. |
| **security_nat_policy**  dictionary | Specify the Firewall NAT policies for the virtual server.  You can specify one or more NAT policies to use.  The most specific policy is used. For example, if you specify the virtual server should use the device policy and the route domain policy, the route domain policy overrides the device policy. |
| **policy**  string | Specifies the policy to apply a NAT policy directly to the virtual server.  The virtual server NAT policy is the most specific, and overrides a route domain and device policy, if specified.  To remove the policy, specify an empty string value. |
| **use_device_policy**  boolean | Specifies the virtual server uses the device NAT policy, as specified in the Firewall Options.  The device policy is used if no route domain or virtual server NAT setting is specified.  Choices:   - `false` - `true` |
| **use_route_domain_policy**  boolean | Specifies the virtual server uses the route domain policy, as specified in the Route Domain Security settings.  When specified, the route domain policy overrides the device policy, and is overridden by a virtual server policy.  Choices:   - `false` - `true` |
| **service_down_immediate_action**  string  added in f5networks.f5_modules 1.16.0 | Specifies the immediate action to take upon the receipt of the initial SYN packet if the availability status of the virtual server is Offline or Unavailable.  Supported for virtual servers with a Type of `standard` and Protocol of `TCP`.  Choices:   - `"none"` - `"reset"` - `"drop"` |
| **snat**  string | Source network address policy.  When `type` is `dhcp`, `reject`, or `internal`, this parameter is ignored.  The name of a SNAT pool (like “/Common/snat_pool_name”) can be specified to enable SNAT with the specific pool.  To remove SNAT, specify the word `none`.  To specify automap, use the word `automap`. |
| **source**  string | Specifies an IP address or network from which the virtual server accepts traffic.  The virtual server accepts clients only from one of these IP addresses.  For this setting to function effectively, specify a value other than 0.0.0.0/0 or ::/0 (that is, any/0, any6/0).  In order to maximize the utility of this setting, specify the most specific address prefixes covering all customer addresses and no others.  Specify the IP address in Classless Inter-Domain Routing (CIDR) format; address/prefix, where the prefix length is in bits. For example, for IPv4, 10.0.0.1/32 or 10.0.0.0/24, and for IPv6, ffe1::0020/64 or 2001:ed8:77b5:2:10:10:100:42/64. |
| **source_port**  string | Specifies whether the system preserves the source port of the connection.  When creating a new virtual server, if this parameter is not specified, the default is `preserve`.  Choices:   - `"preserve"` - `"preserve-strict"` - `"change"` |
| **state**  string | The virtual server state. If `absent`, deletes the virtual server if it exists. If `present`, creates the virtual server and enables it. If `enabled`, enables the virtual server if it exists. If `disabled`, creates the virtual server if needed, and sets the state to `disabled`.  Attempting to change `state` on a virtual server that belongs to an iAPP with strict updates enabled will result in an error message returned by device, unless `insert_metadata` parameter is set to `no`.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |
| **type**  string | Specifies the network service provided by this virtual server.  When creating a new virtual server, if this parameter is not provided, the default is `standard`.  This value cannot be changed after it is set.  When `standard`, specifies a virtual server that directs client traffic to a load balancing pool, and is the most basic type of virtual server. When you first create the virtual server, you assign an existing default pool to it. From then on, the virtual server automatically directs traffic to that default pool.  When `forwarding-l2`, specifies a virtual server that shares the same IP address as a node in an associated VLAN.  When `forwarding-ip`, specifies a virtual server like other virtual servers, except the virtual server has no pool members to load balance. The virtual server simply forwards the packet directly to the destination IP address specified in the client request.  When `performance-http`, specifies a virtual server with which you associate a Fast HTTP profile. Together, the virtual server and profile increase the speed at which the virtual server processes HTTP requests.  When `performance-l4`, specifies a virtual server with which you associate a Fast L4 profile. Together, the virtual server and profile increase the speed at which the virtual server processes layer 4 requests.  When `stateless`, specifies a virtual server that accepts traffic matching the virtual server address and load balances the packet to the pool members without attempting to match the packet to a pre-existing connection in the connection table. New connections are immediately removed from the connection table. This addresses the requirement for one-way UDP traffic that needs to be processed at very high throughput levels, for example, load balancing syslog traffic to a pool of syslog servers. Stateless virtual servers are not suitable for processing traffic requiring stateful tracking, such as TCP traffic. Stateless virtual servers do not support iRules, persistence, connection mirroring, rateshaping, or SNAT automap.  When `reject`, specifies the BIG-IP system rejects any traffic destined for the virtual server IP address.  When `dhcp`, specifies a virtual server that relays Dynamic Host Control Protocol (DHCP) client requests for an IP address to one or more DHCP servers, and provides DHCP server responses with an available IP address for the client.  When `internal`, specifies a virtual server that supports modification of HTTP requests and responses. Internal virtual servers enable the use of ICAP (Internet Content Adaptation Protocol) servers to modify HTTP requests and responses by creating and applying an ICAP profile and adding Request Adapt or Response Adapt profiles to the virtual server.  When `message-routing`, specifies a virtual server that uses a SIP application protocol and functions in accordance with a SIP session profile and SIP router profile.  Choices:   - `"standard"` ← (default) - `"forwarding-l2"` - `"forwarding-ip"` - `"performance-http"` - `"performance-l4"` - `"stateless"` - `"reject"` - `"dhcp"` - `"internal"` - `"message-routing"` |

## [Notes](bigip_virtual_server_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_virtual_server_module.md#id4)

```yaml+jinja
- name: Modify Port of the Virtual Server
  bigip_virtual_server:
    state: present
    partition: Common
    name: my-virtual-server
    port: 8080
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost

- name: Delete virtual server
  bigip_virtual_server:
    state: absent
    partition: Common
    name: my-virtual-server
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost

- name: Add virtual server
  bigip_virtual_server:
    state: present
    partition: Common
    name: my-virtual-server
    destination: 10.10.10.10
    port: 443
    pool: my-pool
    snat: Automap
    description: Test Virtual Server
    profiles:
      - http
      - fix
      - name: clientssl
        context: server-side
      - name: ilx
        context: client-side
    policies:
      - my-ltm-policy-for-asm
      - ltm-uri-policy
      - ltm-policy-2
      - ltm-policy-3
    enabled_vlans:
      - /Common/vlan2
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost

- name: Add FastL4 virtual server
  bigip_virtual_server:
    destination: 1.1.1.1
    name: fastl4_vs
    port: 80
    profiles:
      - fastL4
    state: present
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost

- name: Add iRules to the Virtual Server
  bigip_virtual_server:
    name: my-virtual-server
    irules:
      - irule1
      - irule2
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove one iRule from the Virtual Server
  bigip_virtual_server:
    name: my-virtual-server
    irules:
      - irule2
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove all iRules from the Virtual Server
  bigip_virtual_server:
    name: my-virtual-server
    irules: ""
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove pool from the Virtual Server
  bigip_virtual_server:
    name: my-virtual-server
    pool: ""
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost

- name: Add metadata to virtual
  bigip_virtual_server:
    name: my-virtual-server
    partition: Common
    metadata:
      ansible: 2.4
      updated_at: 2017-12-20T17:50:46Z
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add virtual with two profiles
  bigip_virtual_server:
    name: my-virtual-server
    partition: Common
    profiles:
      - http
      - tcp
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove HTTP profile from previous virtual
  bigip_virtual_server:
    name: my-virtual-server
    partition: Common
    profiles:
      - tcp
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add the HTTP profile back to the previous virtual
  bigip_virtual_server:
    name: my-virtual-server
    partition: Common
    profiles:
      - http
      - tcp
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add virtual server with rate limit
  bigip_virtual_server:
    state: present
    partition: Common
    name: my-virtual-server
    destination: 10.10.10.10
    port: 443
    pool: my-pool
    snat: Automap
    description: Test Virtual Server
    profiles:
      - http
      - fix
      - name: clientssl
        context: server-side
      - name: ilx
        context: client-side
    policies:
      - my-ltm-policy-for-asm
      - ltm-uri-policy
      - ltm-policy-2
      - ltm-policy-3
    enabled_vlans:
      - /Common/vlan2
    rate_limit: 400
    rate_limit_mode: destination
    rate_limit_dst_mask: 32
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost

- name: Add FastL4 virtual server with clone_pools
  bigip_virtual_server:
    destination: 1.1.1.1
    name: fastl4_vs
    port: 80
    profiles:
      - fastL4
    state: present
    clone_pools:
      - pool_name: FooPool
        context: clientside
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost

- name: Add virtual with MRF router option set
  bigip_virtual_server:
    name: my-virtual-server
    destination: 10.10.10.10
    port: 443
    partition: Common
    profiles:
      - http
      - tcp
      - name: noneg-ssl
        context: client-side
      - name: http2
        context: client-side
      - name: httprouter
        context: all
    provider:
      server: lb.mydomain.net
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_virtual_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address_translation**  boolean | The new value specifying whether address translation is on or off.  Returned: changed  Sample: `true` |
| **auto_last_hop**  string | Specifies the autoLasthop value of the virtual server  Returned: changed  Sample: `"enabled"` |
| **clone_pools**  list / elements=string | Pools to which virtual server copies traffic.  Returned: changed  Sample: `[{"context": "clientside", "pool_name": "/Common/Pool1"}]` |
| **default_persistence_profile**  string | Default persistence profile set on the virtual server.  Returned: changed  Sample: `"/Common/dest_addr"` |
| **description**  string | New description of the virtual server.  Returned: changed  Sample: `"This is my description"` |
| **destination**  string | Destination of the virtual server.  Returned: changed  Sample: `"1.1.1.1"` |
| **disabled**  boolean | Whether the virtual server is disabled or not.  Returned: changed  Sample: `true` |
| **disabled_vlans**  list / elements=string | List of VLANs that the virtual is disabled for.  Returned: changed  Sample: `["/Common/vlan1", "/Common/vlan2"]` |
| **enabled**  boolean | Whether the virtual server is enabled or not.  Returned: changed  Sample: `false` |
| **enabled_vlans**  list / elements=string | List of VLANs that the virtual is enabled for.  Returned: changed  Sample: `["/Common/vlan5", "/Common/vlan6"]` |
| **fallback_persistence_profile**  string | Fallback persistence profile set on the virtual server.  Returned: changed  Sample: `"/Common/source_addr"` |
| **firewall_enforced_policy**  string | The new enforcing firewall policy.  Returned: changed  Sample: `"/Common/my-enforced-fw"` |
| **firewall_staged_policy**  string | The new staging firewall policy.  Returned: changed  Sample: `"/Common/my-staged-fw"` |
| **ip_intelligence_policy**  string | The new IP Intelligence Policy assigned to the virtual.  Returned: changed  Sample: `"/Common/ip-intelligence"` |
| **ip_protocol**  integer | The new value of the IP protocol.  Returned: changed  Sample: `6` |
| **irules**  list / elements=string | iRules set on the virtual server.  Returned: changed  Sample: `["/Common/irule1", "/Common/irule2"]` |
| **metadata**  dictionary | The new value of the virtual.  Returned: changed  Sample: `{"key1": "foo", "key2": "bar"}` |
| **mirror**  boolean | Specifies the system mirrors connections on each member of a redundant pair.  Returned: changed  Sample: `true` |
| **policies**  list / elements=string | List of policies attached to the virtual.  Returned: changed  Sample: `["/Common/policy1", "/Common/policy2"]` |
| **pool**  string | Pool the virtual server is attached to.  Returned: changed  Sample: `"/Common/my-pool"` |
| **port**  integer | Port the virtual server is configured to listen on.  Returned: changed  Sample: `80` |
| **port_translation**  boolean | The new value specifying whether port translation is on or off.  Returned: changed  Sample: `true` |
| **profiles**  list / elements=string | List of profiles set on the virtual server.  Returned: changed  Sample: `[{"context": "server-side", "name": "tcp"}, {"context": "client-side", "name": "tcp-legacy"}]` |
| **rate_limit**  integer | The maximum number of connections per second allowed for a virtual server.  Returned: changed  Sample: `5000` |
| **rate_limit_dst_mask**  integer | Specifies a mask, in bits, to be applied to the destination address as part of the rate limiting.  Returned: changed  Sample: `32` |
| **rate_limit_mode**  string | Sets the type of rate limiting to be used on the virtual server.  Returned: changed  Sample: `"object-source"` |
| **rate_limit_src_mask**  integer | Specifies a mask, in bits, to be applied to the source address as part of the rate limiting.  Returned: changed  Sample: `32` |
| **security_log_profiles**  list / elements=string | The new list of security log profiles.  Returned: changed  Sample: `["/Common/profile1", "/Common/profile2"]` |
| **service_down_immediate_action**  string | Action to take upon the receipt of the initial SYN packet if server is Offline or Unavailable.  Returned: changed  Sample: `"drop"` |
| **snat**  string | SNAT setting of the virtual server.  Returned: changed  Sample: `"Automap"` |
| **source**  string | Source address set on the virtual server, in CIDR format.  Returned: changed  Sample: `"1.2.3.4/32"` |
| **source_port**  string | Specifies whether the system preserves the source port of the connection.  Returned: changed  Sample: `"change"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)
- Nitin Khanna (@nitinthewiz)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

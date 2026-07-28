---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_wanprof_system_sdwan module – Configure redundant internet connections using SD-WAN"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_wanprof_system_sdwan_module.html
fetched_at: 2026-07-28T02:22:27+00:00
---
# fortinet.fortimanager.fmgr_wanprof_system_sdwan module – Configure redundant internet connections using SD-WAN

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_wanprof_system_sdwan`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_wanprof_system_sdwan_module.md#synopsis)
- [Parameters](fmgr_wanprof_system_sdwan_module.md#parameters)
- [Notes](fmgr_wanprof_system_sdwan_module.md#notes)
- [Examples](fmgr_wanprof_system_sdwan_module.md#examples)
- [Return Values](fmgr_wanprof_system_sdwan_module.md#return-values)

## [Synopsis](fmgr_wanprof_system_sdwan_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_wanprof_system_sdwan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **wanprof**  string / required | the parameter (wanprof) in requested url |
| **wanprof_system_sdwan**  dictionary | the top level parameters set |
| **app-perf-log-period**  integer | Time interval in seconds that applicationperformance logs are generated |
| **duplication**  list / elements=dictionary | no description |
| **dstaddr**  any | (list or str) Destination address or address group names. |
| **dstaddr6**  any | (list or str) Destination address6 or address6 group names. |
| **dstintf**  any | (list or str) Outgoing |
| **id**  integer | Duplication rule ID |
| **packet-de-duplication**  string | Enable/disable discarding of packets that have been duplicated.  **Choices:**   - `"disable"` - `"enable"` |
| **packet-duplication**  string | Configure packet duplication method.  **Choices:**   - `"disable"` - `"force"` - `"on-demand"` |
| **service**  any | (list or str) Service and service group name. |
| **service-id**  any | (list or str) SD-WAN service rule ID list. |
| **sla-match-service**  string | Enable/disable packet duplication matching health-check SLAs in service rule.  **Choices:**   - `"disable"` - `"enable"` |
| **srcaddr**  any | (list or str) Source address or address group names. |
| **srcaddr6**  any | (list or str) Source address6 or address6 group names. |
| **srcintf**  any | (list or str) Incoming |
| **duplication-max-num**  integer | Maximum number of interface members a packet is duplicated in the SD-WAN zone |
| **fail-alert-interfaces**  any | (list) no description |
| **fail-detect**  string | Enable/disable SD-WAN Internet connection status checking  **Choices:**   - `"disable"` - `"enable"` |
| **health-check**  list / elements=dictionary | no description |
| **_dynamic-server**  string | no description |
| **addr-mode**  string | Address mode  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **class-id**  string | Traffic class ID. |
| **detect-mode**  string | The mode determining how to detect the server.  **Choices:**   - `"active"` - `"passive"` - `"prefer-passive"` - `"remote"` - `"agent-based"` |
| **diffservcode**  string | Differentiated services code point |
| **dns-match-ip**  string | Response IP expected from DNS server if the protocol is DNS. |
| **dns-request-domain**  string | Fully qualified domain name to resolve for the DNS probe. |
| **embed-measured-health**  string | Enable/disable embedding measured health information.  **Choices:**   - `"disable"` - `"enable"` |
| **failtime**  integer | Number of failures before server is considered lost |
| **ftp-file**  string | Full path and file name on the FTP server to download for FTP health-check to probe. |
| **ftp-mode**  string | FTP mode.  **Choices:**   - `"passive"` - `"port"` |
| **ha-priority**  integer | HA election priority |
| **http-agent**  string | String in the http-agent field in the HTTP header. |
| **http-get**  string | URL used to communicate with the server if the protocol if the protocol is HTTP. |
| **http-match**  string | Response string expected from the server if the protocol is HTTP. |
| **interval**  integer | Status check interval in milliseconds, or the time between attempting to connect to the server |
| **members**  any | (list or str) Member sequence number list. |
| **mos-codec**  string | Codec to use for MOS calculation  **Choices:**   - `"g711"` - `"g722"` - `"g729"` |
| **name**  string | Status check or health check name. |
| **packet-size**  integer | Packet size of a twamp test session, |
| **password**  any | (list) no description |
| **port**  integer | Port number used to communicate with the server over the selected protocol |
| **probe-count**  integer | Number of most recent probes that should be used to calculate latency and jitter |
| **probe-packets**  string | Enable/disable transmission of probe packets.  **Choices:**   - `"disable"` - `"enable"` |
| **probe-timeout**  integer | Time to wait before a probe packet is considered lost |
| **protocol**  string | Protocol used to determine if the FortiGate can communicate with the server.  **Choices:**   - `"ping"` - `"tcp-echo"` - `"udp-echo"` - `"http"` - `"twamp"` - `"ping6"` - `"dns"` - `"tcp-connect"` - `"ftp"` - `"https"` |
| **quality-measured-method**  string | Method to measure the quality of tcp-connect.  **Choices:**   - `"half-close"` - `"half-open"` |
| **recoverytime**  integer | Number of successful responses received before server is considered recovered |
| **security-mode**  string | Twamp controller security mode.  **Choices:**   - `"none"` - `"authentication"` |
| **server**  any | (list) no description |
| **sla**  list / elements=dictionary | no description |
| **id**  integer | SLA ID. |
| **jitter-threshold**  integer | Jitter for SLA to make decision in milliseconds. |
| **latency-threshold**  integer | Latency for SLA to make decision in milliseconds. |
| **link-cost-factor**  list / elements=string | no description  **Choices:**   - `"latency"` - `"jitter"` - `"packet-loss"` - `"mos"` |
| **mos-threshold**  string | Minimum Mean Opinion Score for SLA to be marked as pass. |
| **packetloss-threshold**  integer | Packet loss for SLA to make decision in percentage. |
| **priority-in-sla**  integer | Value to be distributed into routing table when in-sla |
| **priority-out-sla**  integer | Value to be distributed into routing table when out-sla |
| **sla-fail-log-period**  integer | Time interval in seconds that SLA fail log messages will be generated |
| **sla-id-redistribute**  integer | Select the ID from the SLA sub-table. |
| **sla-pass-log-period**  integer | Time interval in seconds that SLA pass log messages will be generated |
| **source**  string | Source IP address used in the health-check packet to the server. |
| **source6**  string | Source IPv6 addressused in the health-check packet to server. |
| **system-dns**  string | Enable/disable system DNS as the probe server.  **Choices:**   - `"disable"` - `"enable"` |
| **threshold-alert-jitter**  integer | Alert threshold for jitter |
| **threshold-alert-latency**  integer | Alert threshold for latency |
| **threshold-alert-packetloss**  integer | Alert threshold for packet loss |
| **threshold-warning-jitter**  integer | Warning threshold for jitter |
| **threshold-warning-latency**  integer | Warning threshold for latency |
| **threshold-warning-packetloss**  integer | Warning threshold for packet loss |
| **update-cascade-interface**  string | Enable/disable update cascade interface.  **Choices:**   - `"disable"` - `"enable"` |
| **update-static-route**  string | Enable/disable updating the static route.  **Choices:**   - `"disable"` - `"enable"` |
| **user**  string | The user name to access probe server. |
| **vrf**  integer | Virtual Routing Forwarding ID. |
| **load-balance-mode**  string | Algorithm or mode to use for load balancing Internet traffic to SD-WAN members.  **Choices:**   - `"source-ip-based"` - `"weight-based"` - `"usage-based"` - `"source-dest-ip-based"` - `"measured-volume-based"` |
| **members**  list / elements=dictionary | no description |
| **_dynamic-member**  string | no description |
| **comment**  string | Comments. |
| **cost**  integer | Cost of this interface for services in SLA mode |
| **gateway**  string | The default gateway for this interface. |
| **gateway6**  string | IPv6 gateway. |
| **ingress-spillover-threshold**  integer | Ingress spillover threshold for this interface |
| **interface**  string | Interface name. |
| **preferred-source**  string | Preferred source of route for this member. |
| **priority**  integer | Priority of the interface |
| **priority6**  integer | Priority of the interface for IPv6 |
| **seq-num**  integer | Sequence number |
| **source**  string | Source IP address used in the health-check packet to the server. |
| **source6**  string | Source IPv6 address used in the health-check packet to the server. |
| **spillover-threshold**  integer | Egress spillover threshold for this interface |
| **status**  string | Enable/disable this interface in the SD-WAN.  **Choices:**   - `"disable"` - `"enable"` |
| **volume-ratio**  integer | Measured volume ratio |
| **weight**  integer | Weight of this interface for weighted load balancing. |
| **zone**  string | Zone name. |
| **neighbor**  list / elements=dictionary | no description |
| **health-check**  string | SD-WAN health-check name. |
| **ip**  string | IP/IPv6 address of neighbor. |
| **member**  any | (list or str) Member sequence number. |
| **minimum-sla-meet-members**  integer | Minimum number of members which meet SLA when the neighbor is preferred. |
| **mode**  string | What metric to select the neighbor.  **Choices:**   - `"sla"` - `"speedtest"` |
| **role**  string | Role of neighbor.  **Choices:**   - `"primary"` - `"secondary"` - `"standalone"` |
| **service-id**  string | SD-WAN service ID to work with the neighbor. |
| **sla-id**  integer | SLA ID. |
| **neighbor-hold-boot-time**  integer | Waiting period in seconds when switching from the primary neighbor to the secondary neighbor from the neighbor start. |
| **neighbor-hold-down**  string | Enable/disable hold switching from the secondary neighbor to the primary neighbor.  **Choices:**   - `"disable"` - `"enable"` |
| **neighbor-hold-down-time**  integer | Waiting period in seconds when switching from the secondary neighbor to the primary neighbor when hold-down is disabled. |
| **service**  list / elements=dictionary | no description |
| **addr-mode**  string | Address mode  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **agent-exclusive**  string | Set/unset the service as agent use exclusively.  **Choices:**   - `"disable"` - `"enable"` |
| **bandwidth-weight**  integer | Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1. |
| **default**  string | Enable/disable use of SD-WAN as default service.  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-forward**  string | Enable/disable forward traffic DSCP tag.  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-forward-tag**  string | Forward traffic DSCP tag. |
| **dscp-reverse**  string | Enable/disable reverse traffic DSCP tag.  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-reverse-tag**  string | Reverse traffic DSCP tag. |
| **dst**  any | (list or str) Destination address name. |
| **dst-negate**  string | Enable/disable negation of destination address match.  **Choices:**   - `"disable"` - `"enable"` |
| **dst6**  any | (list or str) Destination address6 name. |
| **end-port**  integer | End destination port number. |
| **end-src-port**  integer | End source port number. |
| **gateway**  string | Enable/disable SD-WAN service gateway.  **Choices:**   - `"disable"` - `"enable"` |
| **groups**  any | (list or str) User groups. |
| **hash-mode**  string | Hash algorithm for selected priority members for load balance mode.  **Choices:**   - `"round-robin"` - `"source-ip-based"` - `"source-dest-ip-based"` - `"inbandwidth"` - `"outbandwidth"` - `"bibandwidth"` |
| **health-check**  any | (list or str) Health check list. |
| **hold-down-time**  integer | Waiting period in seconds when switching from the back-up member to the primary member |
| **id**  integer | SD-WAN rule ID |
| **input-device**  any | (list or str) Source interface name. |
| **input-device-negate**  string | Enable/disable negation of input device match.  **Choices:**   - `"disable"` - `"enable"` |
| **input-zone**  any | (list) no description |
| **internet-service**  string | Enable/disable use of Internet service for application-based load balancing.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-app-ctrl**  any | (list) no description |
| **internet-service-app-ctrl-category**  any | (list) no description |
| **internet-service-app-ctrl-group**  any | (list or str) Application control based Internet Service group list. |
| **internet-service-custom**  any | (list or str) Custom Internet service name list. |
| **internet-service-custom-group**  any | (list or str) Custom Internet Service group list. |
| **internet-service-group**  any | (list or str) Internet Service group list. |
| **internet-service-name**  any | (list or str) Internet service name list. |
| **jitter-weight**  integer | Coefficient of jitter in the formula of custom-profile-1. |
| **latency-weight**  integer | Coefficient of latency in the formula of custom-profile-1. |
| **link-cost-factor**  string | Link cost factor.  **Choices:**   - `"latency"` - `"jitter"` - `"packet-loss"` - `"inbandwidth"` - `"outbandwidth"` - `"bibandwidth"` - `"custom-profile-1"` |
| **link-cost-threshold**  integer | Percentage threshold change of link cost values that will result in policy route regeneration |
| **load-balance**  string | Enable/disable load-balance.  **Choices:**   - `"disable"` - `"enable"` |
| **minimum-sla-meet-members**  integer | Minimum number of members which meet SLA. |
| **mode**  string | Control how the SD-WAN rule sets the priority of interfaces in the SD-WAN.  **Choices:**   - `"auto"` - `"manual"` - `"priority"` - `"sla"` - `"load-balance"` |
| **name**  string | SD-WAN rule name. |
| **packet-loss-weight**  integer | Coefficient of packet-loss in the formula of custom-profile-1. |
| **passive-measurement**  string | Enable/disable passive measurement based on the service criteria.  **Choices:**   - `"disable"` - `"enable"` |
| **priority-members**  any | (list or str) Member sequence number list. |
| **priority-zone**  any | (list or str) no description |
| **protocol**  integer | Protocol number. |
| **quality-link**  integer | Quality grade. |
| **role**  string | Service role to work with neighbor.  **Choices:**   - `"primary"` - `"secondary"` - `"standalone"` |
| **route-tag**  integer | IPv4 route map route-tag. |
| **shortcut**  string | Enable/disable shortcut for this service.  **Choices:**   - `"disable"` - `"enable"` |
| **shortcut-stickiness**  string | Enable/disable shortcut-stickiness of ADVPN.  **Choices:**   - `"disable"` - `"enable"` |
| **sla**  list / elements=dictionary | no description |
| **health-check**  string | SD-WAN health-check. |
| **id**  integer | SLA ID. |
| **sla-compare-method**  string | Method to compare SLA value for SLA mode.  **Choices:**   - `"order"` - `"number"` |
| **sla-stickiness**  string | Enable/disable SLA stickiness  **Choices:**   - `"disable"` - `"enable"` |
| **src**  any | (list or str) Source address name. |
| **src-negate**  string | Enable/disable negation of source address match.  **Choices:**   - `"disable"` - `"enable"` |
| **src6**  any | (list or str) Source address6 name. |
| **standalone-action**  string | Enable/disable service when selected neighbor role is standalone while service role is not standalone.  **Choices:**   - `"disable"` - `"enable"` |
| **start-port**  integer | Start destination port number. |
| **start-src-port**  integer | Start source port number. |
| **status**  string | Enable/disable SD-WAN service.  **Choices:**   - `"disable"` - `"enable"` |
| **tie-break**  string | Method of selecting member if more than one meets the SLA.  **Choices:**   - `"zone"` - `"cfg-order"` - `"fib-best-match"` - `"input-device"` |
| **tos**  string | Type of service bit pattern. |
| **tos-mask**  string | Type of service evaluated bits. |
| **use-shortcut-sla**  string | Enable/disable use of ADVPN shortcut for quality comparison.  **Choices:**   - `"disable"` - `"enable"` |
| **users**  any | (list or str) User name. |
| **zone-mode**  string | Enable/disable zone mode.  **Choices:**   - `"disable"` - `"enable"` |
| **speedtest-bypass-routing**  string | Enable/disable bypass routing when speedtest on a SD-WAN member.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable SD-WAN.  **Choices:**   - `"disable"` - `"enable"` |
| **zone**  list / elements=dictionary | no description |
| **minimum-sla-meet-members**  integer | Minimum number of members which meet SLA when the neighbor is preferred. |
| **name**  string | Zone name. |
| **service-sla-tie-break**  string | Method of selecting member if more than one meets the SLA.  **Choices:**   - `"cfg-order"` - `"fib-best-match"` - `"input-device"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_wanprof_system_sdwan_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_wanprof_system_sdwan_module.md#id4)

```yaml+jinja
- hosts: fortimanager-inventory
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
    - name: Configure redundant internet connections using SD-WAN
      fmgr_wanprof_system_sdwan:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        wanprof: <your own value>
        wanprof_system_sdwan:
          duplication:
            -
              dstaddr: <list or string>
              dstaddr6: <list or string>
              dstintf: <list or string>
              id: <integer>
              packet-de-duplication: <value in [disable, enable]>
              packet-duplication: <value in [disable, force, on-demand]>
              service: <list or string>
              srcaddr: <list or string>
              srcaddr6: <list or string>
              srcintf: <list or string>
              service-id: <list or string>
              sla-match-service: <value in [disable, enable]>
          duplication-max-num: <integer>
          fail-detect: <value in [disable, enable]>
          health-check:
            -
              _dynamic-server: <string>
              addr-mode: <value in [ipv4, ipv6]>
              diffservcode: <string>
              dns-match-ip: <string>
              dns-request-domain: <string>
              failtime: <integer>
              ftp-file: <string>
              ftp-mode: <value in [passive, port]>
              ha-priority: <integer>
              http-agent: <string>
              http-get: <string>
              http-match: <string>
              interval: <integer>
              members: <list or string>
              name: <string>
              packet-size: <integer>
              password: <list or string>
              port: <integer>
              probe-count: <integer>
              probe-packets: <value in [disable, enable]>
              probe-timeout: <integer>
              protocol: <value in [ping, tcp-echo, udp-echo, ...]>
              quality-measured-method: <value in [half-close, half-open]>
              recoverytime: <integer>
              security-mode: <value in [none, authentication]>
              server: <list or string>
              sla:
                -
                  id: <integer>
                  jitter-threshold: <integer>
                  latency-threshold: <integer>
                  link-cost-factor:
                    - latency
                    - jitter
                    - packet-loss
                    - mos
                  packetloss-threshold: <integer>
                  mos-threshold: <string>
                  priority-in-sla: <integer>
                  priority-out-sla: <integer>
              sla-fail-log-period: <integer>
              sla-pass-log-period: <integer>
              system-dns: <value in [disable, enable]>
              threshold-alert-jitter: <integer>
              threshold-alert-latency: <integer>
              threshold-alert-packetloss: <integer>
              threshold-warning-jitter: <integer>
              threshold-warning-latency: <integer>
              threshold-warning-packetloss: <integer>
              update-cascade-interface: <value in [disable, enable]>
              update-static-route: <value in [disable, enable]>
              user: <string>
              detect-mode: <value in [active, passive, prefer-passive, ...]>
              mos-codec: <value in [g711, g722, g729]>
              source: <string>
              vrf: <integer>
              embed-measured-health: <value in [disable, enable]>
              sla-id-redistribute: <integer>
              class-id: <string>
              source6: <string>
          load-balance-mode: <value in [source-ip-based, weight-based, usage-based, ...]>
          members:
            -
              _dynamic-member: <string>
              comment: <string>
              cost: <integer>
              gateway: <string>
              gateway6: <string>
              ingress-spillover-threshold: <integer>
              interface: <string>
              priority: <integer>
              seq-num: <integer>
              source: <string>
              source6: <string>
              spillover-threshold: <integer>
              status: <value in [disable, enable]>
              volume-ratio: <integer>
              weight: <integer>
              zone: <string>
              priority6: <integer>
              preferred-source: <string>
          neighbor:
            -
              health-check: <string>
              ip: <string>
              member: <list or string>
              role: <value in [primary, secondary, standalone]>
              sla-id: <integer>
              minimum-sla-meet-members: <integer>
              mode: <value in [sla, speedtest]>
              service-id: <string>
          neighbor-hold-boot-time: <integer>
          neighbor-hold-down: <value in [disable, enable]>
          neighbor-hold-down-time: <integer>
          service:
            -
              addr-mode: <value in [ipv4, ipv6]>
              bandwidth-weight: <integer>
              default: <value in [disable, enable]>
              dscp-forward: <value in [disable, enable]>
              dscp-forward-tag: <string>
              dscp-reverse: <value in [disable, enable]>
              dscp-reverse-tag: <string>
              dst: <list or string>
              dst-negate: <value in [disable, enable]>
              dst6: <list or string>
              end-port: <integer>
              gateway: <value in [disable, enable]>
              groups: <list or string>
              hash-mode: <value in [round-robin, source-ip-based, source-dest-ip-based, ...]>
              health-check: <list or string>
              hold-down-time: <integer>
              id: <integer>
              input-device: <list or string>
              input-device-negate: <value in [disable, enable]>
              internet-service: <value in [disable, enable]>
              internet-service-app-ctrl: <list or integer>
              internet-service-app-ctrl-group: <list or string>
              internet-service-custom: <list or string>
              internet-service-custom-group: <list or string>
              internet-service-group: <list or string>
              internet-service-name: <list or string>
              jitter-weight: <integer>
              latency-weight: <integer>
              link-cost-factor: <value in [latency, jitter, packet-loss, ...]>
              link-cost-threshold: <integer>
              minimum-sla-meet-members: <integer>
              mode: <value in [auto, manual, priority, ...]>
              name: <string>
              packet-loss-weight: <integer>
              priority-members: <list or string>
              protocol: <integer>
              quality-link: <integer>
              role: <value in [primary, secondary, standalone]>
              route-tag: <integer>
              sla:
                -
                  health-check: <string>
                  id: <integer>
              sla-compare-method: <value in [order, number]>
              src: <list or string>
              src-negate: <value in [disable, enable]>
              src6: <list or string>
              standalone-action: <value in [disable, enable]>
              start-port: <integer>
              status: <value in [disable, enable]>
              tos: <string>
              tos-mask: <string>
              users: <list or string>
              tie-break: <value in [zone, cfg-order, fib-best-match, ...]>
              use-shortcut-sla: <value in [disable, enable]>
              input-zone: <list or string>
              internet-service-app-ctrl-category: <list or integer>
              passive-measurement: <value in [disable, enable]>
              priority-zone: <list or string>
              agent-exclusive: <value in [disable, enable]>
              shortcut: <value in [disable, enable]>
              shortcut-stickiness: <value in [disable, enable]>
              end-src-port: <integer>
              load-balance: <value in [disable, enable]>
              sla-stickiness: <value in [disable, enable]>
              start-src-port: <integer>
              zone-mode: <value in [disable, enable]>
          status: <value in [disable, enable]>
          zone:
            -
              name: <string>
              service-sla-tie-break: <value in [cfg-order, fib-best-match, input-device]>
              minimum-sla-meet-members: <integer>
          speedtest-bypass-routing: <value in [disable, enable]>
          fail-alert-interfaces: <list or string>
          app-perf-log-period: <integer>
```

## [Return Values](fmgr_wanprof_system_sdwan_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)

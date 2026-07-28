---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_wanprof_system_virtualwanlink_healthcheck module – SD-WAN status checking or health checking."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_wanprof_system_virtualwanlink_healthcheck_module.html
fetched_at: 2026-07-28T02:22:34+00:00
---
# fortinet.fortimanager.fmgr_wanprof_system_virtualwanlink_healthcheck module – SD-WAN status checking or health checking.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_wanprof_system_virtualwanlink_healthcheck`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#synopsis)
- [Parameters](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#parameters)
- [Notes](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#notes)
- [Examples](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#examples)
- [Return Values](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#return-values)

## [Synopsis](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#id2)

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
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **wanprof**  string / required | the parameter (wanprof) in requested url |
| **wanprof_system_virtualwanlink_healthcheck**  dictionary | the top level parameters set |
| **_dynamic-server**  string | no description |
| **addr-mode**  string | Address mode  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **diffservcode**  string | Differentiated services code point |
| **dns-request-domain**  string | Fully qualified domain name to resolve for the DNS probe. |
| **failtime**  integer | Number of failures before server is considered lost |
| **ha-priority**  integer | HA election priority |
| **http-agent**  string | String in the http-agent field in the HTTP header. |
| **http-get**  string | URL used to communicate with the server if the protocol if the protocol is HTTP. |
| **http-match**  string | Response string expected from the server if the protocol is HTTP. |
| **internet-service-id**  string | Internet service ID. |
| **interval**  integer | Status check interval, or the time between attempting to connect to the server |
| **members**  any | (list or str) Member sequence number list. |
| **name**  string / required | Status check or health check name. |
| **packet-size**  integer | Packet size of a twamp test session, |
| **password**  any | (list) no description |
| **port**  integer | Port number used to communicate with the server over the selected protocol. |
| **probe-count**  integer | Number of most recent probes that should be used to calculate latency and jitter |
| **probe-packets**  string | Enable/disable transmission of probe packets.  **Choices:**   - `"disable"` - `"enable"` |
| **probe-timeout**  integer | Time to wait before a probe packet is considered lost |
| **protocol**  string | Protocol used to determine if the FortiGate can communicate with the server.  **Choices:**   - `"ping"` - `"tcp-echo"` - `"udp-echo"` - `"http"` - `"twamp"` - `"ping6"` - `"dns"` |
| **recoverytime**  integer | Number of successful responses received before server is considered recovered |
| **security-mode**  string | Twamp controller security mode.  **Choices:**   - `"none"` - `"authentication"` |
| **server**  any | (list) no description |
| **sla**  list / elements=dictionary | no description |
| **id**  integer | SLA ID. |
| **jitter-threshold**  integer | Jitter for SLA to make decision in milliseconds. |
| **latency-threshold**  integer | Latency for SLA to make decision in milliseconds. |
| **link-cost-factor**  list / elements=string | no description  **Choices:**   - `"latency"` - `"jitter"` - `"packet-loss"` |
| **packetloss-threshold**  integer | Packet loss for SLA to make decision in percentage. |
| **sla-fail-log-period**  integer | Time interval in seconds that SLA fail log messages will be generated |
| **sla-pass-log-period**  integer | Time interval in seconds that SLA pass log messages will be generated |
| **system-dns**  string | Enable/disable system DNS as the probe server.  **Choices:**   - `"disable"` - `"enable"` |
| **threshold-alert-jitter**  integer | Alert threshold for jitter |
| **threshold-alert-latency**  integer | Alert threshold for latency |
| **threshold-alert-packetloss**  integer | Alert threshold for packet loss |
| **threshold-warning-jitter**  integer | Warning threshold for jitter |
| **threshold-warning-latency**  integer | Warning threshold for latency |
| **threshold-warning-packetloss**  integer | Warning threshold for packet loss |
| **timeout**  integer | How long to wait before not receiving a reply from the server to consider the connetion attempt a failure |
| **update-cascade-interface**  string | Enable/disable update cascade interface.  **Choices:**   - `"disable"` - `"enable"` |
| **update-static-route**  string | Enable/disable updating the static route.  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#id4)

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
    - name: SD-WAN status checking or health checking.
      fmgr_wanprof_system_virtualwanlink_healthcheck:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        wanprof: <your own value>
        state: <value in [present, absent]>
        wanprof_system_virtualwanlink_healthcheck:
          _dynamic-server: <string>
          addr-mode: <value in [ipv4, ipv6]>
          failtime: <integer>
          http-agent: <string>
          http-get: <string>
          http-match: <string>
          interval: <integer>
          members: <list or string>
          name: <string>
          packet-size: <integer>
          password: <list or string>
          port: <integer>
          protocol: <value in [ping, tcp-echo, udp-echo, ...]>
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
              packetloss-threshold: <integer>
          threshold-alert-jitter: <integer>
          threshold-alert-latency: <integer>
          threshold-alert-packetloss: <integer>
          threshold-warning-jitter: <integer>
          threshold-warning-latency: <integer>
          threshold-warning-packetloss: <integer>
          update-cascade-interface: <value in [disable, enable]>
          update-static-route: <value in [disable, enable]>
          internet-service-id: <string>
          probe-packets: <value in [disable, enable]>
          sla-fail-log-period: <integer>
          sla-pass-log-period: <integer>
          timeout: <integer>
          ha-priority: <integer>
          diffservcode: <string>
          probe-timeout: <integer>
          dns-request-domain: <string>
          probe-count: <integer>
          system-dns: <value in [disable, enable]>
```

## [Return Values](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#id5)

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

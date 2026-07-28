---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_vip6_dynamicmapping_realservers module – Select the real servers that this server load balancing VIP will distribute traffic to."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_vip6_dynamicmapping_realservers_module.html
fetched_at: 2026-07-28T02:13:11+00:00
---
# fortinet.fortimanager.fmgr_firewall_vip6_dynamicmapping_realservers module – Select the real servers that this server load balancing VIP will distribute traffic to.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_vip6_dynamicmapping_realservers`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_firewall_vip6_dynamicmapping_realservers_module.md#synopsis)
- [Parameters](fmgr_firewall_vip6_dynamicmapping_realservers_module.md#parameters)
- [Notes](fmgr_firewall_vip6_dynamicmapping_realservers_module.md#notes)
- [Examples](fmgr_firewall_vip6_dynamicmapping_realservers_module.md#examples)
- [Return Values](fmgr_firewall_vip6_dynamicmapping_realservers_module.md#return-values)

## [Synopsis](fmgr_firewall_vip6_dynamicmapping_realservers_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_vip6_dynamicmapping_realservers_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **dynamic_mapping**  string / required | the parameter (dynamic_mapping) in requested url |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_vip6_dynamicmapping_realservers**  dictionary | the top level parameters set |
| **client-ip**  string | Only clients in this IP range can connect to this real server. |
| **healthcheck**  string | Enable to check the responsiveness of the real server before forwarding traffic.  **Choices:**   - `"disable"` - `"enable"` - `"vip"` |
| **holddown-interval**  integer | Time in seconds that the health check monitor continues to monitor an unresponsive server that should be active. |
| **http-host**  string | HTTP server domain name in HTTP header. |
| **id**  integer / required | Real server ID. |
| **ip**  string | IP address of the real server. |
| **max-connections**  integer | Max number of active connections that can directed to the real server. |
| **monitor**  any | (list or str) no description |
| **port**  integer | Port for communicating with the real server. |
| **status**  string | Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent.  **Choices:**   - `"active"` - `"standby"` - `"disable"` |
| **translate-host**  string | Enable/disable translation of hostname/IP from virtual server to real server.  **Choices:**   - `"disable"` - `"enable"` |
| **weight**  integer | Weight of the real server. |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **vip6**  string / required | the parameter (vip6) in requested url |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_vip6_dynamicmapping_realservers_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_vip6_dynamicmapping_realservers_module.md#id4)

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
    - name: Select the real servers that this server load balancing VIP will distribute traffic to.
      fmgr_firewall_vip6_dynamicmapping_realservers:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        vip6: <your own value>
        dynamic_mapping: <your own value>
        state: <value in [present, absent]>
        firewall_vip6_dynamicmapping_realservers:
          client-ip: <string>
          healthcheck: <value in [disable, enable, vip]>
          holddown-interval: <integer>
          http-host: <string>
          id: <integer>
          ip: <string>
          max-connections: <integer>
          monitor: <list or string>
          port: <integer>
          status: <value in [active, standby, disable]>
          weight: <integer>
          translate-host: <value in [disable, enable]>
```

## [Return Values](fmgr_firewall_vip6_dynamicmapping_realservers_module.md#id5)

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

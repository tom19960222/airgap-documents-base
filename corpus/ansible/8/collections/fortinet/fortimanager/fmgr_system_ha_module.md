---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_ha module – HA configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_ha_module.html
fetched_at: 2026-07-28T02:18:39+00:00
---
# fortinet.fortimanager.fmgr_system_ha module – HA configuration.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_ha`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_ha_module.md#synopsis)
- [Parameters](fmgr_system_ha_module.md#parameters)
- [Notes](fmgr_system_ha_module.md#notes)
- [Examples](fmgr_system_ha_module.md#examples)
- [Return Values](fmgr_system_ha_module.md#return-values)

## [Synopsis](fmgr_system_ha_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_ha_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **system_ha**  dictionary | the top level parameters set |
| **clusterid**  integer | Cluster ID range |
| **failover-mode**  string | HA failover mode.  manual - Manual Failove  vrrp - Use VRRP  **Choices:**   - `"manual"` - `"vrrp"` |
| **file-quota**  integer | File quota in MB |
| **hb-interval**  integer | Heartbeat interval |
| **hb-lost-threshold**  integer | Heartbeat lost threshold |
| **local-cert**  string | set the ha local certificate. |
| **mode**  string | Mode.  standalone - Standalone.  master - Master.  slave - Slave.  **Choices:**   - `"standalone"` - `"master"` - `"slave"` - `"primary"` - `"secondary"` |
| **monitored-interfaces**  list / elements=dictionary | no description |
| **interface-name**  string | Interface name. |
| **monitored-ips**  list / elements=dictionary | no description |
| **id**  integer | Id. |
| **interface**  string | Interface name. |
| **ip**  string | IP address. |
| **password**  any | (list) Group password. |
| **peer**  list / elements=dictionary | Peer. |
| **id**  integer | Id. |
| **ip**  string | IP address of peer. |
| **ip6**  string | IP address |
| **serial-number**  string | Serial number of peer. |
| **status**  string | Peer admin status.  disable - Disable.  enable - Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **priority**  integer | Runtime priority [1 |
| **unicast**  string | Use unitcast for VRRP message.  disable - Disable.  enable - Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **vip**  string | Virtual IP. |
| **vip-interface**  string | vip interface. |
| **vrrp-adv-interval**  integer | VRRP advert interval [1 - 30 seconnds] |
| **vrrp-interface**  string | VRRP and vip interface. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_ha_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_ha_module.md#id4)

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
    - name: HA configuration.
      fmgr_system_ha:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_ha:
          clusterid: <integer>
          file-quota: <integer>
          hb-interval: <integer>
          hb-lost-threshold: <integer>
          mode: <value in [standalone, master, slave, ...]>
          password: <list or string>
          peer:
            -
              id: <integer>
              ip: <string>
              ip6: <string>
              serial-number: <string>
              status: <value in [disable, enable]>
          local-cert: <string>
          failover-mode: <value in [manual, vrrp]>
          monitored-interfaces:
            -
              interface-name: <string>
          monitored-ips:
            -
              id: <integer>
              interface: <string>
              ip: <string>
          priority: <integer>
          unicast: <value in [disable, enable]>
          vip: <string>
          vrrp-adv-interval: <integer>
          vrrp-interface: <string>
          vip-interface: <string>
```

## [Return Values](fmgr_system_ha_module.md#id5)

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

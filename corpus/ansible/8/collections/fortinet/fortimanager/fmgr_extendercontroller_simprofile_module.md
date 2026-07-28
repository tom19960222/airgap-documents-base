---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_extendercontroller_simprofile module – no description"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_extendercontroller_simprofile_module.html
fetched_at: 2026-07-28T02:10:54+00:00
---
# fortinet.fortimanager.fmgr_extendercontroller_simprofile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_extendercontroller_simprofile`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_extendercontroller_simprofile_module.md#synopsis)
- [Parameters](fmgr_extendercontroller_simprofile_module.md#parameters)
- [Notes](fmgr_extendercontroller_simprofile_module.md#notes)
- [Examples](fmgr_extendercontroller_simprofile_module.md#examples)
- [Return Values](fmgr_extendercontroller_simprofile_module.md#return-values)

## [Synopsis](fmgr_extendercontroller_simprofile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_extendercontroller_simprofile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **extendercontroller_simprofile**  dictionary | the top level parameters set |
| **auto-switch_profile**  dictionary | no description |
| **dataplan**  string | Dataplan.  **Choices:**   - `"disable"` - `"enable"` |
| **disconnect**  string | Disconnect.  **Choices:**   - `"disable"` - `"enable"` |
| **disconnect-period**  integer | Disconnect-Period. |
| **disconnect-threshold**  integer | Disconnect-Threshold. |
| **signal**  string | Signal.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Status.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-back**  list / elements=string | Switch-Back.  **Choices:**   - `"time"` - `"timer"` |
| **switch-back-time**  string | Switch-Back-Time. |
| **switch-back-timer**  integer | Switch-Back-Timer. |
| **conn-status**  integer | Conn-Status. |
| **default-sim**  string | Default-Sim.  **Choices:**   - `"sim1"` - `"sim2"` - `"carrier"` - `"cost"` |
| **description**  string | Description. |
| **gps**  string | Gps.  **Choices:**   - `"disable"` - `"enable"` |
| **modem-id**  integer | Modem-Id. |
| **name**  string / required | Name. |
| **preferred-carrier**  string | Preferred-Carrier. |
| **redundant-intf**  string | Redundant-Intf. |
| **redundant-mode**  string | Redundant-Mode.  **Choices:**   - `"disable"` - `"enable"` |
| **sim1-pin**  string | Sim1-Pin.  **Choices:**   - `"disable"` - `"enable"` |
| **sim1-pin-code**  any | (list) Sim1-Pin-Code. |
| **sim2-pin**  string | Sim2-Pin.  **Choices:**   - `"disable"` - `"enable"` |
| **sim2-pin-code**  any | (list) Sim2-Pin-Code. |
| **status**  string | Status.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_extendercontroller_simprofile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_extendercontroller_simprofile_module.md#id4)

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
    - name: no description
      fmgr_extendercontroller_simprofile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        extendercontroller_simprofile:
          auto-switch_profile:
            dataplan: <value in [disable, enable]>
            disconnect: <value in [disable, enable]>
            disconnect-period: <integer>
            disconnect-threshold: <integer>
            signal: <value in [disable, enable]>
            status: <value in [disable, enable]>
            switch-back:
              - time
              - timer
            switch-back-time: <string>
            switch-back-timer: <integer>
          conn-status: <integer>
          default-sim: <value in [sim1, sim2, carrier, ...]>
          description: <string>
          gps: <value in [disable, enable]>
          modem-id: <integer>
          name: <string>
          preferred-carrier: <string>
          redundant-intf: <string>
          redundant-mode: <value in [disable, enable]>
          sim1-pin: <value in [disable, enable]>
          sim1-pin-code: <list or string>
          sim2-pin: <value in [disable, enable]>
          sim2-pin-code: <list or string>
          status: <value in [disable, enable]>
```

## [Return Values](fmgr_extendercontroller_simprofile_module.md#id5)

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

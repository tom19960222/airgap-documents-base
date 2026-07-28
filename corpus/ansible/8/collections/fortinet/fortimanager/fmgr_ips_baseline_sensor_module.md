---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_ips_baseline_sensor module – Configure IPS sensor."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_ips_baseline_sensor_module.html
fetched_at: 2026-07-28T02:14:51+00:00
---
# fortinet.fortimanager.fmgr_ips_baseline_sensor module – Configure IPS sensor.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_ips_baseline_sensor`.

New in fortinet.fortimanager 2.2.0

- [Synopsis](fmgr_ips_baseline_sensor_module.md#synopsis)
- [Parameters](fmgr_ips_baseline_sensor_module.md#parameters)
- [Notes](fmgr_ips_baseline_sensor_module.md#notes)
- [Examples](fmgr_ips_baseline_sensor_module.md#examples)
- [Return Values](fmgr_ips_baseline_sensor_module.md#return-values)

## [Synopsis](fmgr_ips_baseline_sensor_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_ips_baseline_sensor_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **ips_baseline_sensor**  dictionary | the top level parameters set |
| **block-malicious-url**  string | Enable/disable malicious URL blocking.  **Choices:**   - `"disable"` - `"enable"` |
| **comment**  string | Comment. |
| **entries**  list / elements=dictionary | no description |
| **action**  string | Action taken with traffic in which signatures are detected.  **Choices:**   - `"pass"` - `"block"` - `"reset"` - `"default"` |
| **application**  any | (list) no description |
| **cve**  any | (list) no description |
| **exempt-ip**  list / elements=dictionary | no description |
| **dst-ip**  string | Destination IP address and netmask. |
| **id**  integer | Exempt IP ID. |
| **src-ip**  string | Source IP address and netmask. |
| **id**  integer | Rule ID in IPS database |
| **location**  any | (list) no description |
| **log**  string | Enable/disable logging of signatures included in filter.  **Choices:**   - `"disable"` - `"enable"` |
| **log-attack-context**  string | Enable/disable logging of attack context  **Choices:**   - `"disable"` - `"enable"` |
| **log-packet**  string | Enable/disable packet logging.  **Choices:**   - `"disable"` - `"enable"` |
| **os**  any | (list) no description |
| **protocol**  any | (list) no description |
| **quarantine**  string | Quarantine method.  **Choices:**   - `"none"` - `"attacker"` - `"both"` - `"interface"` |
| **quarantine-expiry**  string | Duration of quarantine. |
| **quarantine-log**  string | Enable/disable quarantine logging.  **Choices:**   - `"disable"` - `"enable"` |
| **rate-count**  integer | Count of the rate. |
| **rate-duration**  integer | Duration |
| **rate-mode**  string | Rate limit mode.  **Choices:**   - `"periodical"` - `"continuous"` |
| **rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` - `"dhcp-client-mac"` - `"dns-domain"` |
| **rule**  string | Identifies the predefined or custom IPS signatures to add to the sensor. |
| **severity**  any | (list) no description |
| **status**  string | Status of the signatures included in filter.  **Choices:**   - `"disable"` - `"enable"` - `"default"` |
| **tags**  string | no description |
| **extended-log**  string | Enable/disable extended logging.  **Choices:**   - `"disable"` - `"enable"` |
| **filter**  list / elements=dictionary | no description |
| **action**  string | Action of selected rules.  **Choices:**   - `"pass"` - `"block"` - `"default"` - `"reset"` |
| **application**  any | (list) no description |
| **application(real)**  string | no description |
| **location**  any | (list) no description |
| **location(real)**  string | no description |
| **log**  string | Enable/disable logging of selected rules.  **Choices:**   - `"disable"` - `"enable"` - `"default"` |
| **log-packet**  string | Enable/disable packet logging of selected rules.  **Choices:**   - `"disable"` - `"enable"` - `"default"` |
| **name**  string | Filter name. |
| **os**  any | (list) no description |
| **os(real)**  string | no description |
| **protocol**  any | (list) no description |
| **protocol(real)**  string | no description |
| **quarantine**  string | Quarantine IP or interface.  **Choices:**   - `"none"` - `"attacker"` - `"both"` - `"interface"` |
| **quarantine-expiry**  integer | Duration of quarantine in minute. |
| **quarantine-log**  string | Enable/disable logging of selected quarantine.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  any | (list) no description |
| **severity(real)**  string | no description |
| **status**  string | Selected rules status.  **Choices:**   - `"disable"` - `"enable"` - `"default"` |
| **log**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | Sensor name. |
| **override**  list / elements=dictionary | no description |
| **action**  string | Action of override rule.  **Choices:**   - `"pass"` - `"block"` - `"reset"` |
| **exempt-ip**  list / elements=dictionary | no description |
| **dst-ip**  string | Destination IP address and netmask. |
| **id**  integer | Exempt IP ID. |
| **src-ip**  string | Source IP address and netmask. |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **log-packet**  string | Enable/disable packet logging.  **Choices:**   - `"disable"` - `"enable"` |
| **quarantine**  string | Quarantine IP or interface.  **Choices:**   - `"none"` - `"attacker"` - `"both"` - `"interface"` |
| **quarantine-expiry**  integer | Duration of quarantine in minute. |
| **quarantine-log**  string | Enable/disable logging of selected quarantine.  **Choices:**   - `"disable"` - `"enable"` |
| **rule-id**  integer | Override rule ID. |
| **status**  string | Enable/disable status of override rule.  **Choices:**   - `"disable"` - `"enable"` |
| **replacemsg-group**  string | Replacement message group. |
| **scan-botnet-connections**  string | Block or monitor connections to Botnet servers, or disable Botnet scanning.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_ips_baseline_sensor_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_ips_baseline_sensor_module.md#id4)

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
    - name: Configure IPS sensor.
      fmgr_ips_baseline_sensor:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        ips_baseline_sensor:
          block-malicious-url: <value in [disable, enable]>
          comment: <string>
          entries:
            -
              action: <value in [pass, block, reset, ...]>
              application: <list or string>
              cve: <list or string>
              exempt-ip:
                -
                  dst-ip: <string>
                  id: <integer>
                  src-ip: <string>
              id: <integer>
              location: <list or string>
              log: <value in [disable, enable]>
              log-attack-context: <value in [disable, enable]>
              log-packet: <value in [disable, enable]>
              os: <list or string>
              protocol: <list or string>
              quarantine: <value in [none, attacker, both, ...]>
              quarantine-expiry: <string>
              quarantine-log: <value in [disable, enable]>
              rate-count: <integer>
              rate-duration: <integer>
              rate-mode: <value in [periodical, continuous]>
              rate-track: <value in [none, src-ip, dest-ip, ...]>
              rule: <string>
              severity: <list or string>
              status: <value in [disable, enable, default]>
              tags: <string>
          extended-log: <value in [disable, enable]>
          filter:
            -
              action: <value in [pass, block, default, ...]>
              application: <list or string>
              application(real): <string>
              location: <list or string>
              location(real): <string>
              log: <value in [disable, enable, default]>
              log-packet: <value in [disable, enable, default]>
              name: <string>
              os: <list or string>
              os(real): <string>
              protocol: <list or string>
              protocol(real): <string>
              quarantine: <value in [none, attacker, both, ...]>
              quarantine-expiry: <integer>
              quarantine-log: <value in [disable, enable]>
              severity: <list or string>
              severity(real): <string>
              status: <value in [disable, enable, default]>
          log: <value in [disable, enable]>
          name: <string>
          override:
            -
              action: <value in [pass, block, reset]>
              exempt-ip:
                -
                  dst-ip: <string>
                  id: <integer>
                  src-ip: <string>
              log: <value in [disable, enable]>
              log-packet: <value in [disable, enable]>
              quarantine: <value in [none, attacker, both, ...]>
              quarantine-expiry: <integer>
              quarantine-log: <value in [disable, enable]>
              rule-id: <integer>
              status: <value in [disable, enable]>
          replacemsg-group: <string>
          scan-botnet-connections: <value in [disable, block, monitor]>
```

## [Return Values](fmgr_ips_baseline_sensor_module.md#id5)

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

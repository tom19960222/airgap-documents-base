---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_snmp_user module – SNMP user configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_snmp_user_module.html
fetched_at: 2026-07-28T02:20:23+00:00
---
# fortinet.fortimanager.fmgr_system_snmp_user module – SNMP user configuration.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_snmp_user`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_snmp_user_module.md#synopsis)
- [Parameters](fmgr_system_snmp_user_module.md#parameters)
- [Notes](fmgr_system_snmp_user_module.md#notes)
- [Examples](fmgr_system_snmp_user_module.md#examples)
- [Return Values](fmgr_system_snmp_user_module.md#return-values)

## [Synopsis](fmgr_system_snmp_user_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_snmp_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **system_snmp_user**  dictionary | the top level parameters set |
| **auth-proto**  string | Authentication protocol.  md5 - HMAC-MD5-96 authentication protocol.  sha - HMAC-SHA-96 authentication protocol.  **Choices:**   - `"md5"` - `"sha"` |
| **auth-pwd**  any | (list) Password for authentication protocol. |
| **events**  list / elements=string | SNMP notifications  disk_low - Disk usage too high.  ha_switch - HA switch.  intf_ip_chg - Interface IP address changed.  sys_reboot - System reboot.  cpu_high - CPU usage too high.  mem_low - Available memory is low.  log-alert - Log base alert message.  log-rate - High incoming log rate detected.  log-data-rate - High incoming log data rate detected.  lic-gbday - High licensed log GB/day detected.  lic-dev-quota - High licensed device quota detected.  cpu-high-exclude-nice - CPU usage exclude NICE threshold.  **Choices:**   - `"disk_low"` - `"ha_switch"` - `"intf_ip_chg"` - `"sys_reboot"` - `"cpu_high"` - `"mem_low"` - `"log-alert"` - `"log-rate"` - `"log-data-rate"` - `"lic-gbday"` - `"lic-dev-quota"` - `"cpu-high-exclude-nice"` |
| **name**  string / required | SNMP user name. |
| **notify-hosts**  string | Hosts to send notifications |
| **notify-hosts6**  string | IPv6 hosts to send notifications |
| **priv-proto**  string | Privacy  aes - CFB128-AES-128 symmetric encryption protocol.  des - CBC-DES symmetric encryption protocol.  **Choices:**   - `"aes"` - `"des"` |
| **priv-pwd**  any | (list) Password for privacy |
| **queries**  string | Enable/disable queries for this user.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **query-port**  integer | SNMPv3 query port. |
| **security-level**  string | Security level for message authentication and encryption.  no-auth-no-priv - Message with no authentication and no privacy  auth-no-priv - Message with authentication but no privacy  auth-priv - Message with authentication and privacy  **Choices:**   - `"no-auth-no-priv"` - `"auth-no-priv"` - `"auth-priv"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_snmp_user_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_snmp_user_module.md#id4)

```yaml+jinja
- name: gathering fortimanager facts
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: retrieve all the SNMP users
     fmgr_fact:
       facts:
           selector: 'system_snmp_user'
           params:
               user: 'your_value'

- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: SNMP user configuration.
     fmgr_system_snmp_user:
        bypass_validation: False
        state: present
        system_snmp_user:
           auth-proto: md5 #<value in [md5, sha]>
           auth-pwd: fortinet
           events:
             - disk_low
             - ha_switch
             - intf_ip_chg
             - sys_reboot
             - cpu_high
             - mem_low
             - log-alert
             - log-rate
             - log-data-rate
             - lic-gbday
             - lic-dev-quota
             - cpu-high-exclude-nice
           name: ansible-test-snmpuser
           queries: disable
           security-level: no-auth-no-priv #<value in [no-auth-no-priv, auth-no-priv, auth-priv]>
```

## [Return Values](fmgr_system_snmp_user_module.md#id5)

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

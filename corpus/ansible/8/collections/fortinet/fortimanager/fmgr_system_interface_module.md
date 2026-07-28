---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_interface module – Interface configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_interface_module.html
fetched_at: 2026-07-28T02:18:43+00:00
---
# fortinet.fortimanager.fmgr_system_interface module – Interface configuration.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_interface`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_interface_module.md#synopsis)
- [Parameters](fmgr_system_interface_module.md#parameters)
- [Notes](fmgr_system_interface_module.md#notes)
- [Examples](fmgr_system_interface_module.md#examples)
- [Return Values](fmgr_system_interface_module.md#return-values)

## [Synopsis](fmgr_system_interface_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_interface_module.md#id2)

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
| **system_interface**  dictionary | the top level parameters set |
| **aggregate**  string | Aggregate interface. |
| **alias**  string | Alias. |
| **allowaccess**  list / elements=string | Allow management access to interface.  ping - PING access.  https - HTTPS access.  ssh - SSH access.  snmp - SNMP access.  http - HTTP access.  webservice - Web service access.  https-logging - Logging over HTTPS access.  **Choices:**   - `"ping"` - `"https"` - `"ssh"` - `"snmp"` - `"http"` - `"webservice"` - `"https-logging"` - `"soc-fabric"` - `"fabric"` |
| **description**  string | Description. |
| **interface**  string | Underlying interface name. |
| **ip**  string | IP address of interface. |
| **ipv6**  dictionary | no description |
| **ip6-address**  string | IPv6 address/prefix of interface. |
| **ip6-allowaccess**  list / elements=string | Allow management access to interface.  ping - PING access.  https - HTTPS access.  ssh - SSH access.  snmp - SNMP access.  http - HTTP access.  webservice - Web service access.  https-logging - Logging over HTTPS access.  **Choices:**   - `"ping"` - `"https"` - `"ssh"` - `"snmp"` - `"http"` - `"webservice"` - `"https-logging"` - `"fabric"` |
| **ip6-autoconf**  string | Enable/disable address auto config  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **lacp-mode**  string | LACP mode.  active - Actively use LACP to negotiate 802.  **Choices:**   - `"active"` |
| **lacp-speed**  string | How often the interface sends LACP messages.  slow - Send LACP message every 30 seconds.  fast - Send LACP message every second.  **Choices:**   - `"slow"` - `"fast"` |
| **link-up-delay**  integer | Number of milliseconds to wait before considering a link is up. |
| **lldp**  string | Enable/disable LLDP  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **member**  list / elements=dictionary | no description |
| **interface-name**  string | Physical interface name. |
| **min-links**  integer | Minimum number of aggregated ports that must be up. |
| **min-links-down**  string | Action to take when less than the configured minimum number of links are active.  operational - Set the aggregate operationally down.  administrative - Set the aggregate administratively down.  **Choices:**   - `"operational"` - `"administrative"` |
| **mtu**  integer | Maximum transportation unit |
| **name**  string / required | Interface name. |
| **rating-service-ip**  string | IP address for fgt rating service, must be same subnet with interface ip. |
| **serviceaccess**  list / elements=string | Allow service access to interface.  fgtupdates - FortiGate updates access.  fclupdates - FortiClient updates access.  webfilter-antispam - Web filtering and antispam access.  **Choices:**   - `"fgtupdates"` - `"fclupdates"` - `"webfilter-antispam"` |
| **speed**  string | Speed.  auto - Auto adjust speed.  10full - 10M full-duplex.  10half - 10M half-duplex.  100full - 100M full-duplex.  100half - 100M half-duplex.  1000full - 1000M full-duplex.  10000full - 10000M full-duplex.  **Choices:**   - `"auto"` - `"10full"` - `"10half"` - `"100full"` - `"100half"` - `"1000full"` - `"10000full"` - `"1g/full"` - `"2.5g/full"` - `"5g/full"` - `"10g/full"` - `"14g/full"` - `"20g/full"` - `"25g/full"` - `"40g/full"` - `"50g/full"` - `"56g/full"` - `"100g/full"` - `"1g/half"` |
| **status**  string | Interface status.  down - Interface down.  up - Interface up.  **Choices:**   - `"down"` - `"up"` - `"disable"` - `"enable"` |
| **type**  string | Interface type.  vlan - VLAN interface.  physical - Physical interface.  aggregate - Aggregate interface.  **Choices:**   - `"vlan"` - `"physical"` - `"aggregate"` |
| **update-service-ip**  string | IP address for fgt/fct update service, must be same subnet with interface ip. |
| **vlan-protocol**  string | Ethernet protocol of VLAN.  8021q - IEEE 802.  8021ad - IEEE 802.  **Choices:**   - `"8021q"` - `"8021ad"` |
| **vlanid**  integer | VLAN ID |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_interface_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_interface_module.md#id4)

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
   - name: retrieve all the interfaces
     fmgr_fact:
       facts:
           selector: 'system_interface'
           params:
               interface: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Interface configuration.
     fmgr_system_interface:
        bypass_validation: False
        state: present
        system_interface:
           allowaccess:
             - ping
           ip: '222.222.22.2/24'
           mtu: 1500
           name: port4
           serviceaccess:
             - fgtupdates
           speed: auto #<value in [auto, 10full, 10half, ...]>
           status: up
```

## [Return Values](fmgr_system_interface_module.md#id5)

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

---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping_dhcpserver module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_fsp_vlan_dynamicmapping_dhcpserver_module.html
fetched_at: 2026-07-27T17:32:45+00:00
---
# fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping_dhcpserver module – no description

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/fortinet/fortimanager) (version 2.1.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping_dhcpserver`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_fsp_vlan_dynamicmapping_dhcpserver_module.md#synopsis)
- [Parameters](fmgr_fsp_vlan_dynamicmapping_dhcpserver_module.md#parameters)
- [Notes](fmgr_fsp_vlan_dynamicmapping_dhcpserver_module.md#notes)
- [Examples](fmgr_fsp_vlan_dynamicmapping_dhcpserver_module.md#examples)
- [Return Values](fmgr_fsp_vlan_dynamicmapping_dhcpserver_module.md#return-values)

## [Synopsis](fmgr_fsp_vlan_dynamicmapping_dhcpserver_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_fsp_vlan_dynamicmapping_dhcpserver_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **dynamic_mapping**  string / required | the parameter (dynamic_mapping) in requested url |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **fsp_vlan_dynamicmapping_dhcpserver**  dictionary | the top level parameters set |
| **auto-configuration**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auto-managed-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **conflicted-ip-timeout**  integer | no description |
| **ddns-auth**  string | no description  Choices:   - `"disable"` - `"tsig"` |
| **ddns-key**  string | no description |
| **ddns-keyname**  string | no description |
| **ddns-server-ip**  string | no description |
| **ddns-ttl**  integer | no description |
| **ddns-update**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ddns-update-override**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ddns-zone**  string | no description |
| **default-gateway**  string | no description |
| **dhcp-settings-from-fortiipam**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dns-server1**  string | no description |
| **dns-server2**  string | no description |
| **dns-server3**  string | no description |
| **dns-server4**  string | no description |
| **dns-service**  string | no description  Choices:   - `"default"` - `"specify"` - `"local"` |
| **domain**  string | no description |
| **enable**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **exclude-range**  list / elements=string | description |
| **end-ip**  string | no description |
| **id**  integer | no description |
| **start-ip**  string | no description |
| **filename**  string | no description |
| **forticlient-on-net-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **id**  integer | no description |
| **interface**  string | no description |
| **ip-mode**  string | no description  Choices:   - `"range"` - `"usrgrp"` |
| **ip-range**  list / elements=string | description |
| **end-ip**  string | no description |
| **id**  integer | no description |
| **start-ip**  string | no description |
| **ipsec-lease-hold**  integer | no description |
| **lease-time**  integer | no description |
| **mac-acl-default-action**  string | no description  Choices:   - `"assign"` - `"block"` |
| **netmask**  string | no description |
| **next-server**  string | no description |
| **ntp-server1**  string | no description |
| **ntp-server2**  string | no description |
| **ntp-server3**  string | no description |
| **ntp-service**  string | no description  Choices:   - `"default"` - `"specify"` - `"local"` |
| **option1**  string | description |
| **option2**  string | description |
| **option3**  string | description |
| **option4**  string | no description |
| **option5**  string | no description |
| **option6**  string | no description |
| **options**  list / elements=string | description |
| **code**  integer | no description |
| **id**  integer | no description |
| **ip**  string | description |
| **type**  string | no description  Choices:   - `"hex"` - `"string"` - `"ip"` - `"fqdn"` |
| **value**  string | no description |
| **reserved-address**  list / elements=string | description |
| **action**  string | no description  Choices:   - `"assign"` - `"block"` - `"reserved"` |
| **circuit-id**  string | no description |
| **circuit-id-type**  string | no description  Choices:   - `"hex"` - `"string"` |
| **description**  string | no description |
| **id**  integer | no description |
| **ip**  string | no description |
| **mac**  string | no description |
| **remote-id**  string | no description |
| **remote-id-type**  string | no description  Choices:   - `"hex"` - `"string"` |
| **type**  string | no description  Choices:   - `"mac"` - `"option82"` |
| **server-type**  string | no description  Choices:   - `"regular"` - `"ipsec"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tftp-server**  string | description |
| **timezone**  string | no description  Choices:   - `"00"` - `"01"` - `"02"` - `"03"` - `"04"` - `"05"` - `"06"` - `"07"` - `"08"` - `"09"` - `"10"` - `"11"` - `"12"` - `"13"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"22"` - `"23"` - `"24"` - `"25"` - `"26"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` - `"32"` - `"33"` - `"34"` - `"35"` - `"36"` - `"37"` - `"38"` - `"39"` - `"40"` - `"41"` - `"42"` - `"43"` - `"44"` - `"45"` - `"46"` - `"47"` - `"48"` - `"49"` - `"50"` - `"51"` - `"52"` - `"53"` - `"54"` - `"55"` - `"56"` - `"57"` - `"58"` - `"59"` - `"60"` - `"61"` - `"62"` - `"63"` - `"64"` - `"65"` - `"66"` - `"67"` - `"68"` - `"69"` - `"70"` - `"71"` - `"72"` - `"73"` - `"74"` - `"75"` - `"76"` - `"77"` - `"78"` - `"79"` - `"80"` - `"81"` - `"82"` - `"83"` - `"84"` - `"85"` - `"86"` - `"87"` |
| **timezone-option**  string | no description  Choices:   - `"disable"` - `"default"` - `"specify"` |
| **vci-match**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **vci-string**  string | description |
| **wifi-ac-service**  string | no description  Choices:   - `"specify"` - `"local"` |
| **wifi-ac1**  string | no description |
| **wifi-ac2**  string | no description |
| **wifi-ac3**  string | no description |
| **wins-server1**  string | no description |
| **wins-server2**  string | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **vlan**  string / required | the parameter (vlan) in requested url |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_fsp_vlan_dynamicmapping_dhcpserver_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_fsp_vlan_dynamicmapping_dhcpserver_module.md#id4)

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
     fmgr_fsp_vlan_dynamicmapping_dhcpserver:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        vlan: <your own value>
        dynamic_mapping: <your own value>
        fsp_vlan_dynamicmapping_dhcpserver:
           auto-configuration: <value in [disable, enable]>
           conflicted-ip-timeout: <value of integer>
           ddns-auth: <value in [disable, tsig]>
           ddns-key: <value of string>
           ddns-keyname: <value of string>
           ddns-server-ip: <value of string>
           ddns-ttl: <value of integer>
           ddns-update: <value in [disable, enable]>
           ddns-update-override: <value in [disable, enable]>
           ddns-zone: <value of string>
           default-gateway: <value of string>
           dns-server1: <value of string>
           dns-server2: <value of string>
           dns-server3: <value of string>
           dns-service: <value in [default, specify, local]>
           domain: <value of string>
           enable: <value in [disable, enable]>
           exclude-range:
             -
                 end-ip: <value of string>
                 id: <value of integer>
                 start-ip: <value of string>
           filename: <value of string>
           forticlient-on-net-status: <value in [disable, enable]>
           id: <value of integer>
           interface: <value of string>
           ip-mode: <value in [range, usrgrp]>
           ip-range:
             -
                 end-ip: <value of string>
                 id: <value of integer>
                 start-ip: <value of string>
           ipsec-lease-hold: <value of integer>
           lease-time: <value of integer>
           mac-acl-default-action: <value in [assign, block]>
           netmask: <value of string>
           next-server: <value of string>
           ntp-server1: <value of string>
           ntp-server2: <value of string>
           ntp-server3: <value of string>
           ntp-service: <value in [default, specify, local]>
           option1: <value of string>
           option2: <value of string>
           option3: <value of string>
           option4: <value of string>
           option5: <value of string>
           option6: <value of string>
           options:
             -
                 code: <value of integer>
                 id: <value of integer>
                 ip: <value of string>
                 type: <value in [hex, string, ip, ...]>
                 value: <value of string>
           reserved-address:
             -
                 action: <value in [assign, block, reserved]>
                 circuit-id: <value of string>
                 circuit-id-type: <value in [hex, string]>
                 description: <value of string>
                 id: <value of integer>
                 ip: <value of string>
                 mac: <value of string>
                 remote-id: <value of string>
                 remote-id-type: <value in [hex, string]>
                 type: <value in [mac, option82]>
           server-type: <value in [regular, ipsec]>
           status: <value in [disable, enable]>
           tftp-server: <value of string>
           timezone: <value in [00, 01, 02, ...]>
           timezone-option: <value in [disable, default, specify]>
           vci-match: <value in [disable, enable]>
           vci-string: <value of string>
           wifi-ac1: <value of string>
           wifi-ac2: <value of string>
           wifi-ac3: <value of string>
           wins-server1: <value of string>
           wins-server2: <value of string>
           dns-server4: <value of string>
           wifi-ac-service: <value in [specify, local]>
           auto-managed-status: <value in [disable, enable]>
           dhcp-settings-from-fortiipam: <value in [disable, enable]>
```

## [Return Values](fmgr_fsp_vlan_dynamicmapping_dhcpserver_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **request_url**  string | The full url requested  Returned: always  Sample: `"/sys/login/user"` |
| **response_code**  integer | The status of api request  Returned: always  Sample: `0` |
| **response_message**  string | The descriptive message of the api response  Returned: always  Sample: `"OK."` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
[Homepage](https://fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/tree/galaxy/2.1.7)

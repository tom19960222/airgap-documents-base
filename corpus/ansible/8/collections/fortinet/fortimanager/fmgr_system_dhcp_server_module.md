---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_dhcp_server module – Configure DHCP servers."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_dhcp_server_module.html
fetched_at: 2026-07-28T02:18:24+00:00
---
# fortinet.fortimanager.fmgr_system_dhcp_server module – Configure DHCP servers.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_dhcp_server`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_dhcp_server_module.md#synopsis)
- [Parameters](fmgr_system_dhcp_server_module.md#parameters)
- [Notes](fmgr_system_dhcp_server_module.md#notes)
- [Examples](fmgr_system_dhcp_server_module.md#examples)
- [Return Values](fmgr_system_dhcp_server_module.md#return-values)

## [Synopsis](fmgr_system_dhcp_server_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_dhcp_server_module.md#id2)

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
| **system_dhcp_server**  dictionary | the top level parameters set |
| **auto-configuration**  string | Enable/disable auto configuration.  **Choices:**   - `"disable"` - `"enable"` |
| **auto-managed-status**  string | Enable/disable use of this DHCP server once this interface has been assigned an IP address from FortiIPAM.  **Choices:**   - `"disable"` - `"enable"` |
| **conflicted-ip-timeout**  integer | Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused. |
| **ddns-auth**  string | DDNS authentication mode.  **Choices:**   - `"disable"` - `"tsig"` |
| **ddns-key**  any | (list or str) DDNS update key |
| **ddns-keyname**  string | DDNS update key name. |
| **ddns-server-ip**  string | DDNS server IP. |
| **ddns-ttl**  integer | TTL. |
| **ddns-update**  string | Enable/disable DDNS update for DHCP.  **Choices:**   - `"disable"` - `"enable"` |
| **ddns-update-override**  string | Enable/disable DDNS update override for DHCP.  **Choices:**   - `"disable"` - `"enable"` |
| **ddns-zone**  string | Zone of your domain name |
| **default-gateway**  string | Default gateway IP address assigned by the DHCP server. |
| **dhcp-settings-from-fortiipam**  string | Enable/disable populating of DHCP server settings from FortiIPAM.  **Choices:**   - `"disable"` - `"enable"` |
| **dns-server1**  string | DNS server 1. |
| **dns-server2**  string | DNS server 2. |
| **dns-server3**  string | DNS server 3. |
| **dns-server4**  string | DNS server 4. |
| **dns-service**  string | Options for assigning DNS servers to DHCP clients.  **Choices:**   - `"default"` - `"specify"` - `"local"` |
| **domain**  string | Domain name suffix for the IP addresses that the DHCP server assigns to clients. |
| **exclude-range**  list / elements=dictionary | Exclude-Range. |
| **end-ip**  string | End of IP range. |
| **id**  integer | ID. |
| **lease-time**  integer | Lease time in seconds, 0 means default lease time. |
| **start-ip**  string | Start of IP range. |
| **uci-match**  string | Enable/disable user class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **uci-string**  any | (list) no description |
| **vci-match**  string | Enable/disable vendor class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **vci-string**  any | (list) no description |
| **filename**  string | Name of the boot file on the TFTP server. |
| **forticlient-on-net-status**  string | Enable/disable FortiClient-On-Net service for this DHCP server.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer / required | ID. |
| **interface**  string | DHCP server can assign IP configurations to clients connected to this interface. |
| **ip-mode**  string | Method used to assign client IP.  **Choices:**   - `"range"` - `"usrgrp"` |
| **ip-range**  list / elements=dictionary | Ip-Range. |
| **end-ip**  string | End of IP range. |
| **id**  integer | ID. |
| **lease-time**  integer | Lease time in seconds, 0 means default lease time. |
| **start-ip**  string | Start of IP range. |
| **uci-match**  string | Enable/disable user class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **uci-string**  any | (list) no description |
| **vci-match**  string | Enable/disable vendor class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **vci-string**  any | (list) no description |
| **ipsec-lease-hold**  integer | DHCP over IPsec leases expire this many seconds after tunnel down |
| **lease-time**  integer | Lease time in seconds, 0 means unlimited. |
| **mac-acl-default-action**  string | MAC access control default action  **Choices:**   - `"assign"` - `"block"` |
| **netmask**  string | Netmask assigned by the DHCP server. |
| **next-server**  string | IP address of a server |
| **ntp-server1**  string | NTP server 1. |
| **ntp-server2**  string | NTP server 2. |
| **ntp-server3**  string | NTP server 3. |
| **ntp-service**  string | Options for assigning Network Time Protocol  **Choices:**   - `"default"` - `"specify"` - `"local"` |
| **options**  list / elements=dictionary | Options. |
| **code**  integer | DHCP option code. |
| **id**  integer | ID. |
| **ip**  any | (list) DHCP option IPs. |
| **type**  string | DHCP option type.  **Choices:**   - `"hex"` - `"string"` - `"ip"` - `"fqdn"` |
| **uci-match**  string | Enable/disable user class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **uci-string**  any | (list) no description |
| **value**  string | DHCP option value. |
| **vci-match**  string | Enable/disable vendor class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **vci-string**  any | (list) no description |
| **relay-agent**  string | Relay agent IP. |
| **reserved-address**  list / elements=dictionary | Reserved-Address. |
| **action**  string | Options for the DHCP server to configure the client with the reserved MAC address.  **Choices:**   - `"assign"` - `"block"` - `"reserved"` |
| **circuit-id**  string | Option 82 circuit-ID of the client that will get the reserved IP address. |
| **circuit-id-type**  string | DHCP option type.  **Choices:**   - `"hex"` - `"string"` |
| **description**  string | Description. |
| **id**  integer | ID. |
| **ip**  string | IP address to be reserved for the MAC address. |
| **mac**  string | MAC address of the client that will get the reserved IP address. |
| **remote-id**  string | Option 82 remote-ID of the client that will get the reserved IP address. |
| **remote-id-type**  string | DHCP option type.  **Choices:**   - `"hex"` - `"string"` |
| **type**  string | DHCP reserved-address type.  **Choices:**   - `"mac"` - `"option82"` |
| **server-type**  string | DHCP server can be a normal DHCP server or an IPsec DHCP server.  **Choices:**   - `"regular"` - `"ipsec"` |
| **shared-subnet**  string | Enable/disable shared subnet.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable this DHCP configuration.  **Choices:**   - `"disable"` - `"enable"` |
| **tftp-server**  any | (list) One or more hostnames or IP addresses of the TFTP servers in quotes separated by spaces. |
| **timezone**  string | Select the time zone to be assigned to DHCP clients.  **Choices:**   - `"00"` - `"01"` - `"02"` - `"03"` - `"04"` - `"05"` - `"06"` - `"07"` - `"08"` - `"09"` - `"10"` - `"11"` - `"12"` - `"13"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"22"` - `"23"` - `"24"` - `"25"` - `"26"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` - `"32"` - `"33"` - `"34"` - `"35"` - `"36"` - `"37"` - `"38"` - `"39"` - `"40"` - `"41"` - `"42"` - `"43"` - `"44"` - `"45"` - `"46"` - `"47"` - `"48"` - `"49"` - `"50"` - `"51"` - `"52"` - `"53"` - `"54"` - `"55"` - `"56"` - `"57"` - `"58"` - `"59"` - `"60"` - `"61"` - `"62"` - `"63"` - `"64"` - `"65"` - `"66"` - `"67"` - `"68"` - `"69"` - `"70"` - `"71"` - `"72"` - `"73"` - `"74"` - `"75"` - `"76"` - `"77"` - `"78"` - `"79"` - `"80"` - `"81"` - `"82"` - `"83"` - `"84"` - `"85"` - `"86"` - `"87"` |
| **timezone-option**  string | Options for the DHCP server to set the clients time zone.  **Choices:**   - `"disable"` - `"default"` - `"specify"` |
| **vci-match**  string | Enable/disable vendor class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **vci-string**  any | (list) One or more VCI strings in quotes separated by spaces. |
| **wifi-ac-service**  string | Options for assigning WiFi Access Controllers to DHCP clients  **Choices:**   - `"specify"` - `"local"` |
| **wifi-ac1**  string | WiFi Access Controller 1 IP address |
| **wifi-ac2**  string | WiFi Access Controller 2 IP address |
| **wifi-ac3**  string | WiFi Access Controller 3 IP address |
| **wins-server1**  string | WINS server 1. |
| **wins-server2**  string | WINS server 2. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_dhcp_server_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_dhcp_server_module.md#id4)

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
   - name: retrieve all the DHCP servers
     fmgr_fact:
       facts:
           selector: 'system_dhcp_server'
           params:
               adom: 'ansible'
               server: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure DHCP servers.
     fmgr_system_dhcp_server:
        bypass_validation: False
        adom: ansible
        state: present
        system_dhcp_server:
           auto-configuration: enable #<value in [disable, enable]>
           default-gateway: '222.222.222.1'
           filename: ansible-file
           id: 1
           interface: any
           ip-mode: range #<value in [range, usrgrp]>
           ip-range:
             -
                 end-ip: 222.222.222.22
                 id: 1
                 start-ip: 222.222.222.2
           netmask: 255.255.255.0
           server-type: regular #<value in [regular, ipsec]>
           status: disable #<value in [disable, enable]>
```

## [Return Values](fmgr_system_dhcp_server_module.md#id5)

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

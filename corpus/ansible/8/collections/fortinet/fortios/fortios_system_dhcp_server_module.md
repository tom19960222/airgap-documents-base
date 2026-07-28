---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_dhcp_server module – Configure DHCP servers in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_dhcp_server_module.html
fetched_at: 2026-07-28T02:28:10+00:00
---
# fortinet.fortios.fortios_system_dhcp_server module – Configure DHCP servers in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_system_dhcp_server_module.md#ansible-collections-fortinet-fortios-fortios-system-dhcp-server-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_dhcp_server`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_dhcp_server_module.md#synopsis)
- [Requirements](fortios_system_dhcp_server_module.md#requirements)
- [Parameters](fortios_system_dhcp_server_module.md#parameters)
- [Notes](fortios_system_dhcp_server_module.md#notes)
- [Examples](fortios_system_dhcp_server_module.md#examples)
- [Return Values](fortios_system_dhcp_server_module.md#return-values)

## [Synopsis](fortios_system_dhcp_server_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system_dhcp feature and server category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_dhcp_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_dhcp_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **system_dhcp_server**  dictionary | Configure DHCP servers. |
| **auto_configuration**  string | Enable/disable auto configuration.  **Choices:**   - `"disable"` - `"enable"` |
| **auto_managed_status**  string | Enable/disable use of this DHCP server once this interface has been assigned an IP address from FortiIPAM.  **Choices:**   - `"disable"` - `"enable"` |
| **conflicted_ip_timeout**  integer | Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused. |
| **ddns_auth**  string | DDNS authentication mode.  **Choices:**   - `"disable"` - `"tsig"` |
| **ddns_key**  string | DDNS update key (base 64 encoding). |
| **ddns_keyname**  string | DDNS update key name. |
| **ddns_server_ip**  string | DDNS server IP. |
| **ddns_ttl**  integer | TTL. |
| **ddns_update**  string | Enable/disable DDNS update for DHCP.  **Choices:**   - `"disable"` - `"enable"` |
| **ddns_update_override**  string | Enable/disable DDNS update override for DHCP.  **Choices:**   - `"disable"` - `"enable"` |
| **ddns_zone**  string | Zone of your domain name (ex. DDNS.com). |
| **default_gateway**  string | Default gateway IP address assigned by the DHCP server. |
| **dhcp_settings_from_fortiipam**  string | Enable/disable populating of DHCP server settings from FortiIPAM.  **Choices:**   - `"disable"` - `"enable"` |
| **dns_server1**  string | DNS server 1. |
| **dns_server2**  string | DNS server 2. |
| **dns_server3**  string | DNS server 3. |
| **dns_server4**  string | DNS server 4. |
| **dns_service**  string | Options for assigning DNS servers to DHCP clients.  **Choices:**   - `"local"` - `"default"` - `"specify"` |
| **domain**  string | Domain name suffix for the IP addresses that the DHCP server assigns to clients. |
| **exclude_range**  list / elements=dictionary | Exclude one or more ranges of IP addresses from being assigned to clients. |
| **end_ip**  string | End of IP range. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **lease_time**  integer | Lease time in seconds, 0 means default lease time. |
| **start_ip**  string | Start of IP range. |
| **uci_match**  string | Enable/disable user class identifier (UCI) matching. When enabled only DHCP requests with a matching UCI are served with this range.  **Choices:**   - `"disable"` - `"enable"` |
| **uci_string**  list / elements=dictionary | One or more UCI strings in quotes separated by spaces. |
| **uci_string**  string / required | UCI strings. |
| **vci_match**  string | Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served with this range.  **Choices:**   - `"disable"` - `"enable"` |
| **vci_string**  list / elements=dictionary | One or more VCI strings in quotes separated by spaces. |
| **vci_string**  string / required | VCI strings. |
| **filename**  string | Name of the boot file on the TFTP server. |
| **forticlient_on_net_status**  string | Enable/disable FortiClient-On-Net service for this DHCP server.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **interface**  string | DHCP server can assign IP configurations to clients connected to this interface. Source system.interface.name. |
| **ip_mode**  string | Method used to assign client IP.  **Choices:**   - `"range"` - `"usrgrp"` |
| **ip_range**  list / elements=dictionary | DHCP IP range configuration. |
| **end_ip**  string | End of IP range. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **lease_time**  integer | Lease time in seconds, 0 means default lease time. |
| **start_ip**  string | Start of IP range. |
| **uci_match**  string | Enable/disable user class identifier (UCI) matching. When enabled only DHCP requests with a matching UCI are served with this range.  **Choices:**   - `"disable"` - `"enable"` |
| **uci_string**  list / elements=dictionary | One or more UCI strings in quotes separated by spaces. |
| **uci_string**  string / required | UCI strings. |
| **vci_match**  string | Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served with this range.  **Choices:**   - `"disable"` - `"enable"` |
| **vci_string**  list / elements=dictionary | One or more VCI strings in quotes separated by spaces. |
| **vci_string**  string / required | VCI strings. |
| **ipsec_lease_hold**  integer | DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry). |
| **lease_time**  integer | Lease time in seconds, 0 means unlimited. |
| **mac_acl_default_action**  string | MAC access control default action (allow or block assigning IP settings).  **Choices:**   - `"assign"` - `"block"` |
| **netmask**  string | Netmask assigned by the DHCP server. |
| **next_server**  string | IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from. |
| **ntp_server1**  string | NTP server 1. |
| **ntp_server2**  string | NTP server 2. |
| **ntp_server3**  string | NTP server 3. |
| **ntp_service**  string | Options for assigning Network Time Protocol (NTP) servers to DHCP clients.  **Choices:**   - `"local"` - `"default"` - `"specify"` |
| **options**  list / elements=dictionary | DHCP options. |
| **code**  integer | DHCP option code. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **ip**  list / elements=string | DHCP option IPs. |
| **type**  string | DHCP option type.  **Choices:**   - `"hex"` - `"string"` - `"ip"` - `"fqdn"` |
| **uci_match**  string | Enable/disable user class identifier (UCI) matching. When enabled only DHCP requests with a matching UCI are served with this option.  **Choices:**   - `"disable"` - `"enable"` |
| **uci_string**  list / elements=dictionary | One or more UCI strings in quotes separated by spaces. |
| **uci_string**  string / required | UCI strings. |
| **value**  string | DHCP option value. |
| **vci_match**  string | Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served with this option.  **Choices:**   - `"disable"` - `"enable"` |
| **vci_string**  list / elements=dictionary | One or more VCI strings in quotes separated by spaces. |
| **vci_string**  string / required | VCI strings. |
| **relay_agent**  string | Relay agent IP. |
| **reserved_address**  list / elements=dictionary | Options for the DHCP server to assign IP settings to specific MAC addresses. |
| **action**  string | Options for the DHCP server to configure the client with the reserved MAC address.  **Choices:**   - `"assign"` - `"block"` - `"reserved"` |
| **circuit_id**  string | Option 82 circuit-ID of the client that will get the reserved IP address. |
| **circuit_id_type**  string | DHCP option type.  **Choices:**   - `"hex"` - `"string"` |
| **description**  string | Description. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **ip**  string | IP address to be reserved for the MAC address. |
| **mac**  string | MAC address of the client that will get the reserved IP address. |
| **remote_id**  string | Option 82 remote-ID of the client that will get the reserved IP address. |
| **remote_id_type**  string | DHCP option type.  **Choices:**   - `"hex"` - `"string"` |
| **type**  string | DHCP reserved-address type.  **Choices:**   - `"mac"` - `"option82"` |
| **server_type**  string | DHCP server can be a normal DHCP server or an IPsec DHCP server.  **Choices:**   - `"regular"` - `"ipsec"` |
| **shared_subnet**  string | Enable/disable shared subnet.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable this DHCP configuration.  **Choices:**   - `"disable"` - `"enable"` |
| **tftp_server**  list / elements=dictionary | One or more hostnames or IP addresses of the TFTP servers in quotes separated by spaces. |
| **tftp_server**  string / required | TFTP server. |
| **timezone**  string | Select the time zone to be assigned to DHCP clients.  **Choices:**   - `"01"` - `"02"` - `"03"` - `"04"` - `"05"` - `"81"` - `"06"` - `"07"` - `"08"` - `"09"` - `"10"` - `"11"` - `"12"` - `"13"` - `"74"` - `"14"` - `"77"` - `"15"` - `"87"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"75"` - `"21"` - `"22"` - `"23"` - `"24"` - `"80"` - `"79"` - `"25"` - `"26"` - `"27"` - `"28"` - `"78"` - `"29"` - `"30"` - `"31"` - `"32"` - `"33"` - `"34"` - `"35"` - `"36"` - `"37"` - `"38"` - `"83"` - `"84"` - `"40"` - `"85"` - `"39"` - `"41"` - `"42"` - `"43"` - `"44"` - `"45"` - `"46"` - `"47"` - `"51"` - `"48"` - `"49"` - `"50"` - `"52"` - `"53"` - `"54"` - `"55"` - `"56"` - `"57"` - `"58"` - `"59"` - `"60"` - `"61"` - `"62"` - `"63"` - `"64"` - `"65"` - `"66"` - `"67"` - `"68"` - `"69"` - `"70"` - `"71"` - `"72"` - `"00"` - `"82"` - `"73"` - `"86"` - `"76"` |
| **timezone_option**  string | Options for the DHCP server to set the client”s time zone.  **Choices:**   - `"disable"` - `"default"` - `"specify"` |
| **vci_match**  string | Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served.  **Choices:**   - `"disable"` - `"enable"` |
| **vci_string**  list / elements=dictionary | One or more VCI strings in quotes separated by spaces. |
| **vci_string**  string / required | VCI strings. |
| **wifi_ac1**  string | WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417). |
| **wifi_ac2**  string | WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417). |
| **wifi_ac3**  string | WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417). |
| **wifi_ac_service**  string | Options for assigning WiFi access controllers to DHCP clients.  **Choices:**   - `"specify"` - `"local"` |
| **wins_server1**  string | WINS server 1. |
| **wins_server2**  string | WINS server 2. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_dhcp_server_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the id instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_dhcp_server_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure DHCP servers.
    fortios_system_dhcp_server:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_dhcp_server:
        auto_configuration: "disable"
        auto_managed_status: "disable"
        conflicted_ip_timeout: "1800"
        ddns_auth: "disable"
        ddns_key: "<your_own_value>"
        ddns_keyname: "<your_own_value>"
        ddns_server_ip: "<your_own_value>"
        ddns_ttl: "300"
        ddns_update: "disable"
        ddns_update_override: "disable"
        ddns_zone: "<your_own_value>"
        default_gateway: "<your_own_value>"
        dhcp_settings_from_fortiipam: "disable"
        dns_server1: "<your_own_value>"
        dns_server2: "<your_own_value>"
        dns_server3: "<your_own_value>"
        dns_server4: "<your_own_value>"
        dns_service: "local"
        domain: "<your_own_value>"
        exclude_range:
         -
            end_ip: "<your_own_value>"
            id:  "24"
            lease_time: "0"
            start_ip: "<your_own_value>"
            uci_match: "disable"
            uci_string:
             -
                uci_string: "<your_own_value>"
            vci_match: "disable"
            vci_string:
             -
                vci_string: "<your_own_value>"
        filename: "<your_own_value>"
        forticlient_on_net_status: "disable"
        id:  "35"
        interface: "<your_own_value> (source system.interface.name)"
        ip_mode: "range"
        ip_range:
         -
            end_ip: "<your_own_value>"
            id:  "40"
            lease_time: "0"
            start_ip: "<your_own_value>"
            uci_match: "disable"
            uci_string:
             -
                uci_string: "<your_own_value>"
            vci_match: "disable"
            vci_string:
             -
                vci_string: "<your_own_value>"
        ipsec_lease_hold: "60"
        lease_time: "604800"
        mac_acl_default_action: "assign"
        netmask: "<your_own_value>"
        next_server: "<your_own_value>"
        ntp_server1: "<your_own_value>"
        ntp_server2: "<your_own_value>"
        ntp_server3: "<your_own_value>"
        ntp_service: "local"
        options:
         -
            code: "0"
            id:  "60"
            ip: "<your_own_value>"
            type: "hex"
            uci_match: "disable"
            uci_string:
             -
                uci_string: "<your_own_value>"
            value: "<your_own_value>"
            vci_match: "disable"
            vci_string:
             -
                vci_string: "<your_own_value>"
        relay_agent: "<your_own_value>"
        reserved_address:
         -
            action: "assign"
            circuit_id: "<your_own_value>"
            circuit_id_type: "hex"
            description: "<your_own_value>"
            id:  "76"
            ip: "<your_own_value>"
            mac: "<your_own_value>"
            remote_id: "<your_own_value>"
            remote_id_type: "hex"
            type: "mac"
        server_type: "regular"
        shared_subnet: "disable"
        status: "disable"
        tftp_server:
         -
            tftp_server: "<your_own_value>"
        timezone: "01"
        timezone_option: "disable"
        vci_match: "disable"
        vci_string:
         -
            vci_string: "<your_own_value>"
        wifi_ac_service: "specify"
        wifi_ac1: "<your_own_value>"
        wifi_ac2: "<your_own_value>"
        wifi_ac3: "<your_own_value>"
        wins_server1: "<your_own_value>"
        wins_server2: "<your_own_value>"
```

## [Return Values](fortios_system_dhcp_server_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)

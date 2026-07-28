---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_fortiguard module – Configure FortiGuard services in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_fortiguard_module.html
fetched_at: 2026-07-27T17:44:29+00:00
---
# fortinet.fortios.fortios_system_fortiguard module – Configure FortiGuard services in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_system_fortiguard_module.md#ansible-collections-fortinet-fortios-fortios-system-fortiguard-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_fortiguard`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_fortiguard_module.md#synopsis)
- [Requirements](fortios_system_fortiguard_module.md#requirements)
- [Parameters](fortios_system_fortiguard_module.md#parameters)
- [Notes](fortios_system_fortiguard_module.md#notes)
- [Examples](fortios_system_fortiguard_module.md#examples)
- [Return Values](fortios_system_fortiguard_module.md#return-values)

## [Synopsis](fortios_system_fortiguard_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and fortiguard category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_fortiguard_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_fortiguard_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **system_fortiguard**  dictionary | Configure FortiGuard services. |
| **antispam_cache**  string | Enable/disable FortiGuard antispam request caching. Uses a small amount of memory but improves performance.  Choices:   - `"enable"` - `"disable"` |
| **antispam_cache_mpercent**  integer | Maximum percentage of FortiGate memory the antispam cache is allowed to use (1 - 15). |
| **antispam_cache_ttl**  integer | Time-to-live for antispam cache entries in seconds (300 - 86400). Lower times reduce the cache size. Higher times may improve performance since the cache will have more entries. |
| **antispam_expiration**  integer | Expiration date of the FortiGuard antispam contract. |
| **antispam_force_off**  string | Enable/disable turning off the FortiGuard antispam service.  Choices:   - `"enable"` - `"disable"` |
| **antispam_license**  integer | Interval of time between license checks for the FortiGuard antispam contract. |
| **antispam_timeout**  integer | Antispam query time out (1 - 30 sec). |
| **anycast_sdns_server_ip**  string | IP address of the FortiGuard anycast DNS rating server. |
| **anycast_sdns_server_port**  integer | Port to connect to on the FortiGuard anycast DNS rating server. |
| **auto_firmware_upgrade**  string | Enable/disable automatic patch-level firmware upgrade from FortiGuard. The FortiGate unit searches for new patches only in the same major and minor version.  Choices:   - `"enable"` - `"disable"` |
| **auto_firmware_upgrade_day**  list / elements=string | Allowed day(s) of the week to start automatic patch-level firmware upgrade from FortiGuard.  Choices:   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **auto_firmware_upgrade_end_hour**  integer | End time in the designated time window for automatic patch-level firmware upgrade from FortiGuard in 24 hour time (0 ~ 23). When the end time is smaller than the start time, the end time is interpreted as the next day. The actual upgrade time is selected randomly within the time window. |
| **auto_firmware_upgrade_start_hour**  integer | Start time in the designated time window for automatic patch-level firmware upgrade from FortiGuard in 24 hour time (0 ~ 23). The actual upgrade time is selected randomly within the time window. |
| **auto_join_forticloud**  string | Automatically connect to and login to FortiCloud.  Choices:   - `"enable"` - `"disable"` |
| **ddns_server_ip**  string | IP address of the FortiDDNS server. |
| **ddns_server_ip6**  string | IPv6 address of the FortiDDNS server. |
| **ddns_server_port**  integer | Port used to communicate with FortiDDNS servers. |
| **fortiguard_anycast**  string | Enable/disable use of FortiGuard”s Anycast network.  Choices:   - `"enable"` - `"disable"` |
| **fortiguard_anycast_source**  string | Configure which of Fortinet”s servers to provide FortiGuard services in FortiGuard”s anycast network. Default is Fortinet.  Choices:   - `"fortinet"` - `"aws"` - `"debug"` |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **load_balance_servers**  integer | Number of servers to alternate between as first FortiGuard option. |
| **outbreak_prevention_cache**  string | Enable/disable FortiGuard Virus Outbreak Prevention cache.  Choices:   - `"enable"` - `"disable"` |
| **outbreak_prevention_cache_mpercent**  integer | Maximum percent of memory FortiGuard Virus Outbreak Prevention cache can use (1 - 15%). |
| **outbreak_prevention_cache_ttl**  integer | Time-to-live for FortiGuard Virus Outbreak Prevention cache entries (300 - 86400 sec). |
| **outbreak_prevention_expiration**  integer | Expiration date of FortiGuard Virus Outbreak Prevention contract. |
| **outbreak_prevention_force_off**  string | Turn off FortiGuard Virus Outbreak Prevention service.  Choices:   - `"enable"` - `"disable"` |
| **outbreak_prevention_license**  integer | Interval of time between license checks for FortiGuard Virus Outbreak Prevention contract. |
| **outbreak_prevention_timeout**  integer | FortiGuard Virus Outbreak Prevention time out (1 - 30 sec). |
| **persistent_connection**  string | Enable/disable use of persistent connection to receive update notification from FortiGuard.  Choices:   - `"enable"` - `"disable"` |
| **port**  string | Port used to communicate with the FortiGuard servers.  Choices:   - `"8888"` - `"53"` - `"80"` - `"443"` |
| **protocol**  string | Protocol used to communicate with the FortiGuard servers.  Choices:   - `"udp"` - `"http"` - `"https"` |
| **proxy_password**  string | Proxy user password. |
| **proxy_server_ip**  string | Hostname or IP address of the proxy server. |
| **proxy_server_port**  integer | Port used to communicate with the proxy server. |
| **proxy_username**  string | Proxy user name. |
| **sandbox_inline_scan**  string | Enable/disable FortiCloud Sandbox inline-scan.  Choices:   - `"enable"` - `"disable"` |
| **sandbox_region**  string | FortiCloud Sandbox region. |
| **sdns_options**  list / elements=string | Customization options for the FortiGuard DNS service.  Choices:   - `"include-question-section"` |
| **sdns_server_ip**  list / elements=string | IP address of the FortiGuard DNS rating server. |
| **sdns_server_port**  integer | Port to connect to on the FortiGuard DNS rating server. |
| **service_account_id**  string | Service account ID. |
| **source_ip**  string | Source IPv4 address used to communicate with FortiGuard. |
| **source_ip6**  string | Source IPv6 address used to communicate with FortiGuard. |
| **update_build_proxy**  string | Enable/disable proxy dictionary rebuild.  Choices:   - `"enable"` - `"disable"` |
| **update_extdb**  string | Enable/disable external resource update.  Choices:   - `"enable"` - `"disable"` |
| **update_ffdb**  string | Enable/disable Internet Service Database update.  Choices:   - `"enable"` - `"disable"` |
| **update_server_location**  string | Location from which to receive FortiGuard updates.  Choices:   - `"automatic"` - `"usa"` - `"eu"` - `"any"` |
| **update_uwdb**  string | Enable/disable allowlist update.  Choices:   - `"enable"` - `"disable"` |
| **vdom**  string | FortiGuard Service virtual domain name. Source system.vdom.name. |
| **videofilter_expiration**  integer | Expiration date of the FortiGuard video filter contract. |
| **videofilter_license**  integer | Interval of time between license checks for the FortiGuard video filter contract. |
| **webfilter_cache**  string | Enable/disable FortiGuard web filter caching.  Choices:   - `"enable"` - `"disable"` |
| **webfilter_cache_ttl**  integer | Time-to-live for web filter cache entries in seconds (300 - 86400). |
| **webfilter_expiration**  integer | Expiration date of the FortiGuard web filter contract. |
| **webfilter_force_off**  string | Enable/disable turning off the FortiGuard web filtering service.  Choices:   - `"enable"` - `"disable"` |
| **webfilter_license**  integer | Interval of time between license checks for the FortiGuard web filter contract. |
| **webfilter_timeout**  integer | Web filter query time out (1 - 30 sec). |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_fortiguard_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_fortiguard_module.md#id5)

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
  - name: Configure FortiGuard services.
    fortios_system_fortiguard:
      vdom:  "{{ vdom }}"
      system_fortiguard:
        antispam_cache: "enable"
        antispam_cache_mpercent: "2"
        antispam_cache_ttl: "1800"
        antispam_expiration: "0"
        antispam_force_off: "enable"
        antispam_license: "4294967295"
        antispam_timeout: "7"
        anycast_sdns_server_ip: "<your_own_value>"
        anycast_sdns_server_port: "853"
        auto_firmware_upgrade: "enable"
        auto_firmware_upgrade_day: "sunday"
        auto_firmware_upgrade_end_hour: "4"
        auto_firmware_upgrade_start_hour: "2"
        auto_join_forticloud: "enable"
        ddns_server_ip: "<your_own_value>"
        ddns_server_ip6: "<your_own_value>"
        ddns_server_port: "443"
        fortiguard_anycast: "enable"
        fortiguard_anycast_source: "fortinet"
        interface: "<your_own_value> (source system.interface.name)"
        interface_select_method: "auto"
        load_balance_servers: "1"
        outbreak_prevention_cache: "enable"
        outbreak_prevention_cache_mpercent: "2"
        outbreak_prevention_cache_ttl: "300"
        outbreak_prevention_expiration: "0"
        outbreak_prevention_force_off: "enable"
        outbreak_prevention_license: "4294967295"
        outbreak_prevention_timeout: "7"
        persistent_connection: "enable"
        port: "8888"
        protocol: "udp"
        proxy_password: "<your_own_value>"
        proxy_server_ip: "<your_own_value>"
        proxy_server_port: "0"
        proxy_username: "<your_own_value>"
        sandbox_inline_scan: "enable"
        sandbox_region: "<your_own_value>"
        sdns_options: "include-question-section"
        sdns_server_ip: "<your_own_value>"
        sdns_server_port: "53"
        service_account_id: "<your_own_value>"
        source_ip: "84.230.14.43"
        source_ip6: "<your_own_value>"
        update_build_proxy: "enable"
        update_extdb: "enable"
        update_ffdb: "enable"
        update_server_location: "automatic"
        update_uwdb: "enable"
        vdom: "<your_own_value> (source system.vdom.name)"
        videofilter_expiration: "0"
        videofilter_license: "4294967295"
        webfilter_cache: "enable"
        webfilter_cache_ttl: "3600"
        webfilter_expiration: "0"
        webfilter_force_off: "enable"
        webfilter_license: "4294967295"
        webfilter_timeout: "15"
```

## [Return Values](fortios_system_fortiguard_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)

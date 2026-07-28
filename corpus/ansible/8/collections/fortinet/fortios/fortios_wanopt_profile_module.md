---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_wanopt_profile module – Configure WAN optimization profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_wanopt_profile_module.html
fetched_at: 2026-07-28T02:30:38+00:00
---
# fortinet.fortios.fortios_wanopt_profile module – Configure WAN optimization profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wanopt_profile_module.md#ansible-collections-fortinet-fortios-fortios-wanopt-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wanopt_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wanopt_profile_module.md#synopsis)
- [Requirements](fortios_wanopt_profile_module.md#requirements)
- [Parameters](fortios_wanopt_profile_module.md#parameters)
- [Notes](fortios_wanopt_profile_module.md#notes)
- [Examples](fortios_wanopt_profile_module.md#examples)
- [Return Values](fortios_wanopt_profile_module.md#return-values)

## [Synopsis](fortios_wanopt_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wanopt feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wanopt_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_wanopt_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **wanopt_profile**  dictionary | Configure WAN optimization profiles. |
| **auth_group**  string | Optionally add an authentication group to restrict access to the WAN Optimization tunnel to peers in the authentication group. Source wanopt.auth-group.name. |
| **cifs**  dictionary | Enable/disable CIFS (Windows sharing) WAN Optimization and configure CIFS WAN Optimization features. |
| **byte_caching**  string | Enable/disable byte-caching. Byte caching reduces the amount of traffic by caching file data sent across the WAN and in future serving if from the cache.  **Choices:**   - `"enable"` - `"disable"` |
| **log_traffic**  string | Enable/disable logging.  **Choices:**   - `"enable"` - `"disable"` |
| **port**  integer | Single port number or port number range for CIFS. Only packets with a destination port number that matches this port number or range are accepted by this profile. |
| **prefer_chunking**  string | Select dynamic or fixed-size data chunking for WAN Optimization.  **Choices:**   - `"dynamic"` - `"fix"` |
| **protocol_opt**  string | Select protocol specific optimization or generic TCP optimization.  **Choices:**   - `"protocol"` - `"tcp"` |
| **secure_tunnel**  string | Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).  **Choices:**   - `"enable"` - `"disable"` |
| **status**  string | Enable/disable WAN Optimization.  **Choices:**   - `"enable"` - `"disable"` |
| **tunnel_sharing**  string | Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.  **Choices:**   - `"shared"` - `"express-shared"` - `"private"` |
| **comments**  string | Comment. |
| **ftp**  dictionary | Enable/disable FTP WAN Optimization and configure FTP WAN Optimization features. |
| **byte_caching**  string | Enable/disable byte-caching. Byte caching reduces the amount of traffic by caching file data sent across the WAN and in future serving if from the cache.  **Choices:**   - `"enable"` - `"disable"` |
| **log_traffic**  string | Enable/disable logging.  **Choices:**   - `"enable"` - `"disable"` |
| **port**  integer | Single port number or port number range for FTP. Only packets with a destination port number that matches this port number or range are accepted by this profile. |
| **prefer_chunking**  string | Select dynamic or fixed-size data chunking for WAN Optimization.  **Choices:**   - `"dynamic"` - `"fix"` |
| **protocol_opt**  string | Select protocol specific optimization or generic TCP optimization.  **Choices:**   - `"protocol"` - `"tcp"` |
| **secure_tunnel**  string | Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).  **Choices:**   - `"enable"` - `"disable"` |
| **ssl**  string | Enable/disable SSL/TLS offloading (hardware acceleration) for traffic in this tunnel.  **Choices:**   - `"enable"` - `"disable"` |
| **status**  string | Enable/disable WAN Optimization.  **Choices:**   - `"enable"` - `"disable"` |
| **tunnel_sharing**  string | Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.  **Choices:**   - `"shared"` - `"express-shared"` - `"private"` |
| **http**  dictionary | Enable/disable HTTP WAN Optimization and configure HTTP WAN Optimization features. |
| **byte_caching**  string | Enable/disable byte-caching. Byte caching reduces the amount of traffic by caching file data sent across the WAN and in future serving if from the cache.  **Choices:**   - `"enable"` - `"disable"` |
| **log_traffic**  string | Enable/disable logging.  **Choices:**   - `"enable"` - `"disable"` |
| **port**  integer | Single port number or port number range for HTTP. Only packets with a destination port number that matches this port number or range are accepted by this profile. |
| **prefer_chunking**  string | Select dynamic or fixed-size data chunking for WAN Optimization.  **Choices:**   - `"dynamic"` - `"fix"` |
| **protocol_opt**  string | Select protocol specific optimization or generic TCP optimization.  **Choices:**   - `"protocol"` - `"tcp"` |
| **secure_tunnel**  string | Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).  **Choices:**   - `"enable"` - `"disable"` |
| **ssl**  string | Enable/disable SSL/TLS offloading (hardware acceleration) for traffic in this tunnel.  **Choices:**   - `"enable"` - `"disable"` |
| **ssl_port**  integer | Port on which to expect HTTPS traffic for SSL/TLS offloading. |
| **status**  string | Enable/disable WAN Optimization.  **Choices:**   - `"enable"` - `"disable"` |
| **tunnel_non_http**  string | Configure how to process non-HTTP traffic when a profile configured for HTTP traffic accepts a non-HTTP session. Can occur if an application sends non-HTTP traffic using an HTTP destination port.  **Choices:**   - `"enable"` - `"disable"` |
| **tunnel_sharing**  string | Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.  **Choices:**   - `"shared"` - `"express-shared"` - `"private"` |
| **unknown_http_version**  string | How to handle HTTP sessions that do not comply with HTTP 0.9, 1.0, or 1.1.  **Choices:**   - `"reject"` - `"tunnel"` - `"best-effort"` |
| **mapi**  dictionary | Enable/disable MAPI email WAN Optimization and configure MAPI WAN Optimization features. |
| **byte_caching**  string | Enable/disable byte-caching. Byte caching reduces the amount of traffic by caching file data sent across the WAN and in future serving if from the cache.  **Choices:**   - `"enable"` - `"disable"` |
| **log_traffic**  string | Enable/disable logging.  **Choices:**   - `"enable"` - `"disable"` |
| **port**  integer | Single port number or port number range for MAPI. Only packets with a destination port number that matches this port number or range are accepted by this profile. |
| **secure_tunnel**  string | Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).  **Choices:**   - `"enable"` - `"disable"` |
| **status**  string | Enable/disable WAN Optimization.  **Choices:**   - `"enable"` - `"disable"` |
| **tunnel_sharing**  string | Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.  **Choices:**   - `"shared"` - `"express-shared"` - `"private"` |
| **name**  string / required | Profile name. |
| **tcp**  dictionary | Enable/disable TCP WAN Optimization and configure TCP WAN Optimization features. |
| **byte_caching**  string | Enable/disable byte-caching. Byte caching reduces the amount of traffic by caching file data sent across the WAN and in future serving if from the cache.  **Choices:**   - `"enable"` - `"disable"` |
| **byte_caching_opt**  string | Select whether TCP byte-caching uses system memory only or both memory and disk space.  **Choices:**   - `"mem-only"` - `"mem-disk"` |
| **log_traffic**  string | Enable/disable logging.  **Choices:**   - `"enable"` - `"disable"` |
| **port**  string | Port numbers or port number ranges for TCP. Only packets with a destination port number that matches this port number or range are accepted by this profile. |
| **secure_tunnel**  string | Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).  **Choices:**   - `"enable"` - `"disable"` |
| **ssl**  string | Enable/disable SSL/TLS offloading (hardware acceleration) for traffic in this tunnel.  **Choices:**   - `"enable"` - `"disable"` |
| **ssl_port**  string | Port numbers or port number ranges on which to expect HTTPS traffic for SSL/TLS offloading. |
| **status**  string | Enable/disable WAN Optimization.  **Choices:**   - `"enable"` - `"disable"` |
| **tunnel_sharing**  string | Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.  **Choices:**   - `"shared"` - `"express-shared"` - `"private"` |
| **transparent**  string | Enable/disable transparent mode.  **Choices:**   - `"enable"` - `"disable"` |

## [Notes](fortios_wanopt_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wanopt_profile_module.md#id5)

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
  - name: Configure WAN optimization profiles.
    fortios_wanopt_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wanopt_profile:
        auth_group: "<your_own_value> (source wanopt.auth-group.name)"
        cifs:
            byte_caching: "enable"
            log_traffic: "enable"
            port: "32767"
            prefer_chunking: "dynamic"
            protocol_opt: "protocol"
            secure_tunnel: "enable"
            status: "enable"
            tunnel_sharing: "shared"
        comments: "<your_own_value>"
        ftp:
            byte_caching: "enable"
            log_traffic: "enable"
            port: "32767"
            prefer_chunking: "dynamic"
            protocol_opt: "protocol"
            secure_tunnel: "enable"
            ssl: "enable"
            status: "enable"
            tunnel_sharing: "shared"
        http:
            byte_caching: "enable"
            log_traffic: "enable"
            port: "32767"
            prefer_chunking: "dynamic"
            protocol_opt: "protocol"
            secure_tunnel: "enable"
            ssl: "enable"
            ssl_port: "32767"
            status: "enable"
            tunnel_non_http: "enable"
            tunnel_sharing: "shared"
            unknown_http_version: "reject"
        mapi:
            byte_caching: "enable"
            log_traffic: "enable"
            port: "32767"
            secure_tunnel: "enable"
            status: "enable"
            tunnel_sharing: "shared"
        name: "default_name_44"
        tcp:
            byte_caching: "enable"
            byte_caching_opt: "mem-only"
            log_traffic: "enable"
            port: "<your_own_value>"
            secure_tunnel: "enable"
            ssl: "enable"
            ssl_port: "<your_own_value>"
            status: "enable"
            tunnel_sharing: "shared"
        transparent: "enable"
```

## [Return Values](fortios_wanopt_profile_module.md#id6)

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

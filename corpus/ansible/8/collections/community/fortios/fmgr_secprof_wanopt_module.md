---
collection: ansible
version: "8"
title: "community.fortios.fmgr_secprof_wanopt module – WAN optimization"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_secprof_wanopt_module.html
fetched_at: 2026-07-28T01:44:26+00:00
---
# community.fortios.fmgr_secprof_wanopt module – WAN optimization

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_secprof_wanopt`.

- [Synopsis](fmgr_secprof_wanopt_module.md#synopsis)
- [Parameters](fmgr_secprof_wanopt_module.md#parameters)
- [Notes](fmgr_secprof_wanopt_module.md#notes)
- [Examples](fmgr_secprof_wanopt_module.md#examples)
- [Return Values](fmgr_secprof_wanopt_module.md#return-values)

## [Synopsis](fmgr_secprof_wanopt_module.md#id1)

- Manage WanOpt security profiles in FortiManager via API

## [Parameters](fmgr_secprof_wanopt_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **auth_group**  string | Optionally add an authentication group to restrict access to the WAN Optimization tunnel to peers in the authentication group. |
| **cifs**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **cifs_byte_caching**  string | Enable/disable byte-caching for HTTP. Byte caching reduces the amount of traffic by caching file data sent across the WAN and in future serving if from the cache.  **Choices:**   - `"disable"` - `"enable"` |
| **cifs_log_traffic**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **cifs_port**  string | Single port number or port number range for CIFS. Only packets with a destination port number that matches this port number or range are accepted by this profile. |
| **cifs_prefer_chunking**  string | Select dynamic or fixed-size data chunking for HTTP WAN Optimization.  **Choices:**   - `"dynamic"` - `"fix"` |
| **cifs_secure_tunnel**  string | Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).  **Choices:**   - `"disable"` - `"enable"` |
| **cifs_status**  string | Enable/disable HTTP WAN Optimization.  **Choices:**   - `"disable"` - `"enable"` |
| **cifs_tunnel_sharing**  string | Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.  **Choices:**   - `"private"` - `"shared"` - `"express-shared"` |
| **comments**  string | Comment. |
| **ftp**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **ftp_byte_caching**  string | Enable/disable byte-caching for HTTP. Byte caching reduces the amount of traffic by caching file data sent across the WAN and in future serving if from the cache.  **Choices:**   - `"disable"` - `"enable"` |
| **ftp_log_traffic**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **ftp_port**  string | Single port number or port number range for FTP. Only packets with a destination port number that matches this port number or range are accepted by this profile. |
| **ftp_prefer_chunking**  string | Select dynamic or fixed-size data chunking for HTTP WAN Optimization.  **Choices:**   - `"dynamic"` - `"fix"` |
| **ftp_secure_tunnel**  string | Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).  **Choices:**   - `"disable"` - `"enable"` |
| **ftp_status**  string | Enable/disable HTTP WAN Optimization.  **Choices:**   - `"disable"` - `"enable"` |
| **ftp_tunnel_sharing**  string | Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.  **Choices:**   - `"private"` - `"shared"` - `"express-shared"` |
| **http**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **http_byte_caching**  string | Enable/disable byte-caching for HTTP. Byte caching reduces the amount of traffic by caching file data sent across the WAN and in future serving if from the cache.  **Choices:**   - `"disable"` - `"enable"` |
| **http_log_traffic**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **http_port**  string | Single port number or port number range for HTTP. Only packets with a destination port number that matches this port number or range are accepted by this profile. |
| **http_prefer_chunking**  string | Select dynamic or fixed-size data chunking for HTTP WAN Optimization.  **Choices:**   - `"dynamic"` - `"fix"` |
| **http_secure_tunnel**  string | Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).  **Choices:**   - `"disable"` - `"enable"` |
| **http_ssl**  string | Enable/disable SSL/TLS offloading (hardware acceleration) for HTTPS traffic in this tunnel.  **Choices:**   - `"disable"` - `"enable"` |
| **http_ssl_port**  string | Port on which to expect HTTPS traffic for SSL/TLS offloading. |
| **http_status**  string | Enable/disable HTTP WAN Optimization.  **Choices:**   - `"disable"` - `"enable"` |
| **http_tunnel_non_http**  string | Configure how to process non-HTTP traffic when a profile configured for HTTP traffic accepts a non-HTTP session. Can occur if an application sends non-HTTP traffic using an HTTP destination port.  **Choices:**   - `"disable"` - `"enable"` |
| **http_tunnel_sharing**  string | Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.  **Choices:**   - `"private"` - `"shared"` - `"express-shared"` |
| **http_unknown_http_version**  string | How to handle HTTP sessions that do not comply with HTTP 0.9, 1.0, or 1.1.  **Choices:**   - `"best-effort"` - `"reject"` - `"tunnel"` |
| **mapi**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **mapi_byte_caching**  string | Enable/disable byte-caching for HTTP. Byte caching reduces the amount of traffic by caching file data sent across the WAN and in future serving if from the cache.  **Choices:**   - `"disable"` - `"enable"` |
| **mapi_log_traffic**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **mapi_port**  string | Single port number or port number range for MAPI. Only packets with a destination port number that matches this port number or range are accepted by this profile. |
| **mapi_secure_tunnel**  string | Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).  **Choices:**   - `"disable"` - `"enable"` |
| **mapi_status**  string | Enable/disable HTTP WAN Optimization.  **Choices:**   - `"disable"` - `"enable"` |
| **mapi_tunnel_sharing**  string | Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.  **Choices:**   - `"private"` - `"shared"` - `"express-shared"` |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  **Choices:**   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **name**  string | Profile name. |
| **tcp**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **tcp_byte_caching**  string | Enable/disable byte-caching for HTTP. Byte caching reduces the amount of traffic by caching file data sent across the WAN and in future serving if from the cache.  **Choices:**   - `"disable"` - `"enable"` |
| **tcp_byte_caching_opt**  string | Select whether TCP byte-caching uses system memory only or both memory and disk space.  **Choices:**   - `"mem-only"` - `"mem-disk"` |
| **tcp_log_traffic**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **tcp_port**  string | Single port number or port number range for TCP. Only packets with a destination port number that matches this port number or range are accepted by this profile. |
| **tcp_secure_tunnel**  string | Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).  **Choices:**   - `"disable"` - `"enable"` |
| **tcp_ssl**  string | Enable/disable SSL/TLS offloading.  **Choices:**   - `"disable"` - `"enable"` |
| **tcp_ssl_port**  string | Port on which to expect HTTPS traffic for SSL/TLS offloading. |
| **tcp_status**  string | Enable/disable HTTP WAN Optimization.  **Choices:**   - `"disable"` - `"enable"` |
| **tcp_tunnel_sharing**  string | Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.  **Choices:**   - `"private"` - `"shared"` - `"express-shared"` |
| **transparent**  string | Enable/disable transparent mode.  **Choices:**   - `"disable"` - `"enable"` |

## [Notes](fmgr_secprof_wanopt_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_secprof_wanopt_module.md#id4)

```yaml+jinja
- name: DELETE Profile
  community.fortios.fmgr_secprof_wanopt:
    name: "Ansible_WanOpt_Profile"
    mode: "delete"

- name: Create FMGR_WANOPT_PROFILE
  community.fortios.fmgr_secprof_wanopt:
    mode: "set"
    adom: "root"
    transparent: "enable"
    name: "Ansible_WanOpt_Profile"
    comments: "Created by Ansible"
    cifs: {byte-caching: "enable",
            log-traffic: "enable",
            port: 80,
            prefer-chunking: "dynamic",
            status: "enable",
            tunnel-sharing: "private"}
    ftp: {byte-caching: "enable",
            log-traffic: "enable",
            port: 80,
            prefer-chunking: "dynamic",
            secure-tunnel: "disable",
            status: "enable",
            tunnel-sharing: "private"}
```

## [Return Values](fmgr_secprof_wanopt_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)

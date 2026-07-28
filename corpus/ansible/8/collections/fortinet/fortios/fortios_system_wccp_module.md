---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_wccp module – Configure WCCP in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_wccp_module.html
fetched_at: 2026-07-28T02:29:46+00:00
---
# fortinet.fortios.fortios_system_wccp module – Configure WCCP in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_wccp_module.md#ansible-collections-fortinet-fortios-fortios-system-wccp-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_wccp`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_wccp_module.md#synopsis)
- [Requirements](fortios_system_wccp_module.md#requirements)
- [Parameters](fortios_system_wccp_module.md#parameters)
- [Notes](fortios_system_wccp_module.md#notes)
- [Examples](fortios_system_wccp_module.md#examples)
- [Return Values](fortios_system_wccp_module.md#return-values)

## [Synopsis](fortios_system_wccp_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and wccp category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_wccp_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_wccp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **system_wccp**  dictionary | Configure WCCP. |
| **assignment_bucket_format**  string | Assignment bucket format for the WCCP cache engine.  **Choices:**   - `"wccp-v2"` - `"cisco-implementation"` |
| **assignment_dstaddr_mask**  string | Assignment destination address mask. |
| **assignment_method**  string | Hash key assignment preference.  **Choices:**   - `"HASH"` - `"MASK"` - `"any"` |
| **assignment_srcaddr_mask**  string | Assignment source address mask. |
| **assignment_weight**  integer | Assignment of hash weight/ratio for the WCCP cache engine. |
| **authentication**  string | Enable/disable MD5 authentication.  **Choices:**   - `"enable"` - `"disable"` |
| **cache_engine_method**  string | Method used to forward traffic to the routers or to return to the cache engine.  **Choices:**   - `"GRE"` - `"L2"` |
| **cache_id**  string | IP address known to all routers. If the addresses are the same, use the default 0.0.0.0. |
| **forward_method**  string | Method used to forward traffic to the cache servers.  **Choices:**   - `"GRE"` - `"L2"` - `"any"` |
| **group_address**  string | IP multicast address used by the cache routers. For the FortiGate to ignore multicast WCCP traffic, use the default 0.0.0.0. |
| **password**  string | Password for MD5 authentication. |
| **ports**  list / elements=string | Service ports. |
| **ports_defined**  string | Match method.  **Choices:**   - `"source"` - `"destination"` |
| **primary_hash**  list / elements=string | Hash method.  **Choices:**   - `"src-ip"` - `"dst-ip"` - `"src-port"` - `"dst-port"` |
| **priority**  integer | Service priority. |
| **protocol**  integer | Service protocol. |
| **return_method**  string | Method used to decline a redirected packet and return it to the FortiGate unit.  **Choices:**   - `"GRE"` - `"L2"` - `"any"` |
| **router_id**  string | IP address known to all cache engines. If all cache engines connect to the same FortiGate interface, use the default 0.0.0.0. |
| **router_list**  list / elements=string | IP addresses of one or more WCCP routers. |
| **server_list**  list / elements=string | IP addresses and netmasks for up to four cache servers. |
| **server_type**  string | Cache server type.  **Choices:**   - `"forward"` - `"proxy"` |
| **service_id**  string / required | Service ID. |
| **service_type**  string | WCCP service type used by the cache server for logical interception and redirection of traffic.  **Choices:**   - `"auto"` - `"standard"` - `"dynamic"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_wccp_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_wccp_module.md#id5)

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
  - name: Configure WCCP.
    fortios_system_wccp:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_wccp:
        assignment_bucket_format: "wccp-v2"
        assignment_dstaddr_mask: "<your_own_value>"
        assignment_method: "HASH"
        assignment_srcaddr_mask: "<your_own_value>"
        assignment_weight: "0"
        authentication: "enable"
        cache_engine_method: "GRE"
        cache_id: "<your_own_value>"
        forward_method: "GRE"
        group_address: "<your_own_value>"
        password: "<your_own_value>"
        ports: "<your_own_value>"
        ports_defined: "source"
        primary_hash: "src-ip"
        priority: "0"
        protocol: "0"
        return_method: "GRE"
        router_id: "<your_own_value>"
        router_list: "<your_own_value>"
        server_list: "<your_own_value>"
        server_type: "forward"
        service_id: "<your_own_value>"
        service_type: "auto"
```

## [Return Values](fortios_system_wccp_module.md#id6)

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

---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_dns module – Configure DNS in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_dns_module.html
fetched_at: 2026-07-28T02:28:10+00:00
---
# fortinet.fortios.fortios_system_dns module – Configure DNS in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_dns_module.md#ansible-collections-fortinet-fortios-fortios-system-dns-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_dns`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_dns_module.md#synopsis)
- [Requirements](fortios_system_dns_module.md#requirements)
- [Parameters](fortios_system_dns_module.md#parameters)
- [Notes](fortios_system_dns_module.md#notes)
- [Examples](fortios_system_dns_module.md#examples)
- [Return Values](fortios_system_dns_module.md#return-values)

## [Synopsis](fortios_system_dns_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and dns category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_dns_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_dns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_dns**  dictionary | Configure DNS. |
| **alt_primary**  string | Alternate primary DNS server. This is not used as a failover DNS server. |
| **alt_secondary**  string | Alternate secondary DNS server. This is not used as a failover DNS server. |
| **cache_notfound_responses**  string | Enable/disable response from the DNS server when a record is not in cache.  **Choices:**   - `"disable"` - `"enable"` |
| **dns_cache_limit**  integer | Maximum number of records in the DNS cache. |
| **dns_cache_ttl**  integer | Duration in seconds that the DNS cache retains information. |
| **dns_over_tls**  string | Enable/disable/enforce DNS over TLS.  **Choices:**   - `"disable"` - `"enable"` - `"enforce"` |
| **domain**  list / elements=dictionary | Search suffix list for hostname lookup. |
| **domain**  string / required | DNS search domain list separated by space (maximum 8 domains). |
| **fqdn_cache_ttl**  integer | FQDN cache time to live in seconds (0 - 86400). |
| **fqdn_max_refresh**  integer | FQDN cache maximum refresh time in seconds (3600 - 86400). |
| **fqdn_min_refresh**  integer | FQDN cache minimum refresh time in seconds (10 - 3600). |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **ip6_primary**  string | Primary DNS server IPv6 address. |
| **ip6_secondary**  string | Secondary DNS server IPv6 address. |
| **log**  string | Local DNS log setting.  **Choices:**   - `"disable"` - `"error"` - `"all"` |
| **primary**  string | Primary DNS server IP address. |
| **protocol**  list / elements=string | DNS transport protocols.  **Choices:**   - `"cleartext"` - `"dot"` - `"doh"` |
| **retry**  integer | Number of times to retry (0 - 5). |
| **secondary**  string | Secondary DNS server IP address. |
| **server_hostname**  list / elements=dictionary | DNS server host name list. |
| **hostname**  string / required | DNS server host name list separated by space (maximum 4 domains). |
| **server_select_method**  string | Specify how configured servers are prioritized.  **Choices:**   - `"least-rtt"` - `"failover"` |
| **source_ip**  string | IP address used by the DNS server as its source IP. |
| **ssl_certificate**  string | Name of local certificate for SSL connections. Source certificate.local.name. |
| **timeout**  integer | DNS query timeout interval in seconds (1 - 10). |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_dns_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_dns_module.md#id5)

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
  - name: Configure DNS.
    fortios_system_dns:
      vdom:  "{{ vdom }}"
      system_dns:
        alt_primary: "<your_own_value>"
        alt_secondary: "<your_own_value>"
        cache_notfound_responses: "disable"
        dns_cache_limit: "5000"
        dns_cache_ttl: "1800"
        dns_over_tls: "disable"
        domain:
         -
            domain: "<your_own_value>"
        fqdn_cache_ttl: "0"
        fqdn_max_refresh: "3600"
        fqdn_min_refresh: "60"
        interface: "<your_own_value> (source system.interface.name)"
        interface_select_method: "auto"
        ip6_primary: "<your_own_value>"
        ip6_secondary: "<your_own_value>"
        log: "disable"
        primary: "<your_own_value>"
        protocol: "cleartext"
        retry: "2"
        secondary: "<your_own_value>"
        server_hostname:
         -
            hostname: "myhostname"
        server_select_method: "least-rtt"
        source_ip: "84.230.14.43"
        ssl_certificate: "<your_own_value> (source certificate.local.name)"
        timeout: "5"
```

## [Return Values](fortios_system_dns_module.md#id6)

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

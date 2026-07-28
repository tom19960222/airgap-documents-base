---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_dnsfilter_profile module – Configure DNS domain filter profile in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_dnsfilter_profile_module.html
fetched_at: 2026-07-27T17:40:12+00:00
---
# fortinet.fortios.fortios_dnsfilter_profile module – Configure DNS domain filter profile in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_dnsfilter_profile_module.md#ansible-collections-fortinet-fortios-fortios-dnsfilter-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_dnsfilter_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_dnsfilter_profile_module.md#synopsis)
- [Requirements](fortios_dnsfilter_profile_module.md#requirements)
- [Parameters](fortios_dnsfilter_profile_module.md#parameters)
- [Notes](fortios_dnsfilter_profile_module.md#notes)
- [Examples](fortios_dnsfilter_profile_module.md#examples)
- [Return Values](fortios_dnsfilter_profile_module.md#return-values)

## [Synopsis](fortios_dnsfilter_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify dnsfilter feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_dnsfilter_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_dnsfilter_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **dnsfilter_profile**  dictionary | Configure DNS domain filter profile. |
| **block_action**  string | Action to take for blocked domains.  Choices:   - `"block"` - `"redirect"` - `"block-sevrfail"` |
| **block_botnet**  string | Enable/disable blocking botnet C&C DNS lookups.  Choices:   - `"disable"` - `"enable"` |
| **comment**  string | Comment. |
| **dns_translation**  list / elements=dictionary | DNS translation settings. |
| **addr_type**  string | DNS translation type (IPv4 or IPv6).  Choices:   - `"ipv4"` - `"ipv6"` |
| **dst**  string | IPv4 address or subnet on the external network to substitute for the resolved address in DNS query replies. Can be single IP address or subnet on the external network, but number of addresses must equal number of mapped IP addresses in src. |
| **dst6**  string | IPv6 address or subnet on the external network to substitute for the resolved address in DNS query replies. Can be single IP address or subnet on the external network, but number of addresses must equal number of mapped IP addresses in src6. |
| **id**  integer | ID. |
| **netmask**  string | If src and dst are subnets rather than single IP addresses, enter the netmask for both src and dst. |
| **prefix**  integer | If src6 and dst6 are subnets rather than single IP addresses, enter the prefix for both src6 and dst6 (1 - 128). |
| **src**  string | IPv4 address or subnet on the internal network to compare with the resolved address in DNS query replies. If the resolved address matches, the resolved address is substituted with dst. |
| **src6**  string | IPv6 address or subnet on the internal network to compare with the resolved address in DNS query replies. If the resolved address matches, the resolved address is substituted with dst6. |
| **status**  string | Enable/disable this DNS translation entry.  Choices:   - `"enable"` - `"disable"` |
| **domain_filter**  dictionary | Domain filter settings. |
| **domain_filter_table**  integer | DNS domain filter table ID. Source dnsfilter.domain-filter.id. |
| **external_ip_blocklist**  list / elements=dictionary | One or more external IP block lists. |
| **name**  string | External domain block list name. Source system.external-resource.name. |
| **ftgd_dns**  dictionary | FortiGuard DNS Filter settings. |
| **filters**  list / elements=dictionary | FortiGuard DNS domain filters. |
| **action**  string | Action to take for DNS requests matching the category.  Choices:   - `"block"` - `"monitor"` |
| **category**  integer | Category number. |
| **id**  integer | ID number. |
| **log**  string | Enable/disable DNS filter logging for this DNS profile.  Choices:   - `"enable"` - `"disable"` |
| **options**  list / elements=string | FortiGuard DNS filter options.  Choices:   - `"error-allow"` - `"ftgd-disable"` |
| **log_all_domain**  string | Enable/disable logging of all domains visited (detailed DNS logging).  Choices:   - `"enable"` - `"disable"` |
| **name**  string / required | Profile name. |
| **redirect_portal**  string | IPv4 address of the SDNS redirect portal. |
| **redirect_portal6**  string | IPv6 address of the SDNS redirect portal. |
| **safe_search**  string | Enable/disable Google, Bing, YouTube, Qwant, DuckDuckGo safe search.  Choices:   - `"disable"` - `"enable"` |
| **sdns_domain_log**  string | Enable/disable domain filtering and botnet domain logging.  Choices:   - `"enable"` - `"disable"` |
| **sdns_ftgd_err_log**  string | Enable/disable FortiGuard SDNS rating error logging.  Choices:   - `"enable"` - `"disable"` |
| **youtube_restrict**  string | Set safe search for YouTube restriction level.  Choices:   - `"strict"` - `"moderate"` |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_dnsfilter_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_dnsfilter_profile_module.md#id5)

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
  - name: Configure DNS domain filter profile.
    fortios_dnsfilter_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      dnsfilter_profile:
        block_action: "block"
        block_botnet: "disable"
        comment: "Comment."
        dns_translation:
         -
            addr_type: "ipv4"
            dst: "<your_own_value>"
            dst6: "<your_own_value>"
            id:  "10"
            netmask: "<your_own_value>"
            prefix: "128"
            src: "<your_own_value>"
            src6: "<your_own_value>"
            status: "enable"
        domain_filter:
            domain_filter_table: "0"
        external_ip_blocklist:
         -
            name: "default_name_19 (source system.external-resource.name)"
        ftgd_dns:
            filters:
             -
                action: "block"
                category: "0"
                id:  "24"
                log: "enable"
            options: "error-allow"
        log_all_domain: "enable"
        name: "default_name_28"
        redirect_portal: "<your_own_value>"
        redirect_portal6: "<your_own_value>"
        safe_search: "disable"
        sdns_domain_log: "enable"
        sdns_ftgd_err_log: "enable"
        youtube_restrict: "strict"
```

## [Return Values](fortios_dnsfilter_profile_module.md#id6)

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

---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_dns_database module – Configure DNS databases in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_dns_database_module.html
fetched_at: 2026-07-28T02:28:12+00:00
---
# fortinet.fortios.fortios_system_dns_database module – Configure DNS databases in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_dns_database_module.md#ansible-collections-fortinet-fortios-fortios-system-dns-database-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_dns_database`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_dns_database_module.md#synopsis)
- [Requirements](fortios_system_dns_database_module.md#requirements)
- [Parameters](fortios_system_dns_database_module.md#parameters)
- [Notes](fortios_system_dns_database_module.md#notes)
- [Examples](fortios_system_dns_database_module.md#examples)
- [Return Values](fortios_system_dns_database_module.md#return-values)

## [Synopsis](fortios_system_dns_database_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and dns_database category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_dns_database_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_dns_database_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **system_dns_database**  dictionary | Configure DNS databases. |
| **allow_transfer**  list / elements=string | DNS zone transfer IP address list. |
| **authoritative**  string | Enable/disable authoritative zone.  **Choices:**   - `"enable"` - `"disable"` |
| **contact**  string | Email address of the administrator for this zone. You can specify only the username, such as admin or the full email address, such as [admin@test.com](mailto:admin%40test.com) When using only a username, the domain of the email will be this zone. |
| **dns_entry**  list / elements=dictionary | DNS entry. |
| **canonical_name**  string | Canonical name of the host. |
| **hostname**  string | Name of the host. |
| **id**  integer / required | DNS entry ID. see <a href=’#notes’>Notes</a>. |
| **ip**  string | IPv4 address of the host. |
| **ipv6**  string | IPv6 address of the host. |
| **preference**  integer | DNS entry preference (0 - 65535, highest preference = 0). |
| **status**  string | Enable/disable resource record status.  **Choices:**   - `"enable"` - `"disable"` |
| **ttl**  integer | Time-to-live for this entry (0 to 2147483647 sec). |
| **type**  string | Resource record type.  **Choices:**   - `"A"` - `"NS"` - `"CNAME"` - `"MX"` - `"AAAA"` - `"PTR"` - `"PTR_V6"` |
| **domain**  string | Domain name. |
| **forwarder**  list / elements=string | DNS zone forwarder IP address list. |
| **forwarder6**  string | Forwarder IPv6 address. |
| **ip_master**  string | IP address of master DNS server. Entries in this master DNS server and imported into the DNS zone. |
| **ip_primary**  string | IP address of primary DNS server. Entries in this primary DNS server and imported into the DNS zone. |
| **name**  string / required | Zone name. |
| **primary_name**  string | Domain name of the default DNS server for this zone. |
| **rr_max**  integer | Maximum number of resource records (10 - 65536, 0 means infinite). |
| **source_ip**  string | Source IP for forwarding to DNS server. |
| **source_ip6**  string | IPv6 source IP address for forwarding to DNS server. |
| **status**  string | Enable/disable this DNS zone.  **Choices:**   - `"enable"` - `"disable"` |
| **ttl**  integer | Default time-to-live value for the entries of this DNS zone (0 - 2147483647 sec). |
| **type**  string | Zone type (primary to manage entries directly, secondary to import entries from other zones).  **Choices:**   - `"primary"` - `"secondary"` - `"master"` - `"slave"` |
| **view**  string | Zone view (public to serve public clients, shadow to serve internal clients).  **Choices:**   - `"shadow"` - `"public"` - `"shadow-ztna"` - `"proxy"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_dns_database_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_dns_database_module.md#id5)

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
  - name: Configure DNS databases.
    fortios_system_dns_database:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_dns_database:
        allow_transfer: "<your_own_value>"
        authoritative: "enable"
        contact: "<your_own_value>"
        dns_entry:
         -
            canonical_name: "<your_own_value>"
            hostname: "myhostname"
            id:  "9"
            ip: "<your_own_value>"
            ipv6: "<your_own_value>"
            preference: "10"
            status: "enable"
            ttl: "0"
            type: "A"
        domain: "<your_own_value>"
        forwarder: "<your_own_value>"
        forwarder6: "<your_own_value>"
        ip_master: "<your_own_value>"
        ip_primary: "<your_own_value>"
        name: "default_name_21"
        primary_name: "<your_own_value>"
        rr_max: "16384"
        source_ip: "84.230.14.43"
        source_ip6: "<your_own_value>"
        status: "enable"
        ttl: "86400"
        type: "primary"
        view: "shadow"
```

## [Return Values](fortios_system_dns_database_module.md#id6)

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

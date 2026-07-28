---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_application_list module – Configure application control lists in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_application_list_module.html
fetched_at: 2026-07-28T02:23:22+00:00
---
# fortinet.fortios.fortios_application_list module – Configure application control lists in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_application_list_module.md#ansible-collections-fortinet-fortios-fortios-application-list-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_application_list`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_application_list_module.md#synopsis)
- [Requirements](fortios_application_list_module.md#requirements)
- [Parameters](fortios_application_list_module.md#parameters)
- [Notes](fortios_application_list_module.md#notes)
- [Examples](fortios_application_list_module.md#examples)
- [Return Values](fortios_application_list_module.md#return-values)

## [Synopsis](fortios_application_list_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify application feature and list category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_application_list_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_application_list_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **application_list**  dictionary | Configure application control lists. |
| **app_replacemsg**  string | Enable/disable replacement messages for blocked applications.  **Choices:**   - `"disable"` - `"enable"` |
| **comment**  string | Comments. |
| **control_default_network_services**  string | Enable/disable enforcement of protocols over selected ports.  **Choices:**   - `"disable"` - `"enable"` |
| **deep_app_inspection**  string | Enable/disable deep application inspection.  **Choices:**   - `"disable"` - `"enable"` |
| **default_network_services**  list / elements=dictionary | Default network service entries. |
| **id**  integer / required | Entry ID. see <a href=’#notes’>Notes</a>. |
| **port**  integer | Port number. |
| **services**  list / elements=string | Network protocols.  **Choices:**   - `"http"` - `"ssh"` - `"telnet"` - `"ftp"` - `"dns"` - `"smtp"` - `"pop3"` - `"imap"` - `"snmp"` - `"nntp"` - `"https"` |
| **violation_action**  string | Action for protocols not in the allowlist for selected port.  **Choices:**   - `"pass"` - `"monitor"` - `"block"` |
| **enforce_default_app_port**  string | Enable/disable default application port enforcement for allowed applications.  **Choices:**   - `"disable"` - `"enable"` |
| **entries**  list / elements=dictionary | Application list entries. |
| **action**  string | Pass or block traffic, or reset connection for traffic from this application.  **Choices:**   - `"pass"` - `"block"` - `"reset"` |
| **application**  list / elements=dictionary | ID of allowed applications. |
| **id**  integer / required | Application IDs. see <a href=’#notes’>Notes</a>. |
| **behavior**  list / elements=string | Application behavior filter. |
| **category**  list / elements=dictionary | Category ID list. |
| **id**  integer / required | Application category ID. see <a href=’#notes’>Notes</a>. |
| **exclusion**  list / elements=dictionary | ID of excluded applications. |
| **id**  integer / required | Excluded application IDs. see <a href=’#notes’>Notes</a>. |
| **id**  integer / required | Entry ID. see <a href=’#notes’>Notes</a>. |
| **log**  string | Enable/disable logging for this application list.  **Choices:**   - `"disable"` - `"enable"` |
| **log_packet**  string | Enable/disable packet logging.  **Choices:**   - `"disable"` - `"enable"` |
| **parameters**  list / elements=dictionary | Application parameters. |
| **id**  integer / required | Parameter tuple ID. see <a href=’#notes’>Notes</a>. |
| **members**  list / elements=dictionary | Parameter tuple members. |
| **id**  integer / required | Parameter. see <a href=’#notes’>Notes</a>. |
| **name**  string | Parameter name. |
| **value**  string | Parameter value. |
| **value**  string | Parameter value. |
| **per_ip_shaper**  string | Per-IP traffic shaper. Source firewall.shaper.per-ip-shaper.name. |
| **popularity**  list / elements=string | Application popularity filter (1 - 5, from least to most popular).  **Choices:**   - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` |
| **protocols**  list / elements=string | Application protocol filter. |
| **quarantine**  string | Quarantine method.  **Choices:**   - `"none"` - `"attacker"` |
| **quarantine_expiry**  string | Duration of quarantine. (Format |
| **quarantine_log**  string | Enable/disable quarantine logging.  **Choices:**   - `"disable"` - `"enable"` |
| **rate_count**  integer | Count of the rate. |
| **rate_duration**  integer | Duration (sec) of the rate. |
| **rate_mode**  string | Rate limit mode.  **Choices:**   - `"periodical"` - `"continuous"` |
| **rate_track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` - `"dhcp-client-mac"` - `"dns-domain"` |
| **risk**  list / elements=dictionary | Risk, or impact, of allowing traffic from this application to occur (1 - 5; Low, Elevated, Medium, High, and Critical). |
| **level**  integer / required | Risk, or impact, of allowing traffic from this application to occur (1 - 5; Low, Elevated, Medium, High, and Critical). see <a href=’#notes’>Notes</a>. |
| **session_ttl**  integer | Session TTL (0 = default). |
| **shaper**  string | Traffic shaper. Source firewall.shaper.traffic-shaper.name. |
| **shaper_reverse**  string | Reverse traffic shaper. Source firewall.shaper.traffic-shaper.name. |
| **sub_category**  list / elements=dictionary | Application Sub-category ID list. |
| **id**  integer / required | Application sub-category ID. see <a href=’#notes’>Notes</a>. |
| **technology**  list / elements=string | Application technology filter. |
| **vendor**  list / elements=string | Application vendor filter. |
| **extended_log**  string | Enable/disable extended logging.  **Choices:**   - `"enable"` - `"disable"` |
| **force_inclusion_ssl_di_sigs**  string | Enable/disable forced inclusion of SSL deep inspection signatures.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | List name. |
| **options**  list / elements=string | Basic application protocol signatures allowed by default.  **Choices:**   - `"allow-dns"` - `"allow-icmp"` - `"allow-http"` - `"allow-ssl"` - `"allow-quic"` |
| **other_application_action**  string | Action for other applications.  **Choices:**   - `"pass"` - `"block"` |
| **other_application_log**  string | Enable/disable logging for other applications.  **Choices:**   - `"disable"` - `"enable"` |
| **p2p_black_list**  list / elements=string | P2P applications to be black listed.  **Choices:**   - `"skype"` - `"edonkey"` - `"bittorrent"` |
| **p2p_block_list**  list / elements=string | P2P applications to be block listed.  **Choices:**   - `"skype"` - `"edonkey"` - `"bittorrent"` |
| **replacemsg_group**  string | Replacement message group. Source system.replacemsg-group.name. |
| **unknown_application_action**  string | Pass or block traffic from unknown applications.  **Choices:**   - `"pass"` - `"block"` |
| **unknown_application_log**  string | Enable/disable logging for unknown applications.  **Choices:**   - `"disable"` - `"enable"` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_application_list_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_application_list_module.md#id5)

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
  - name: Configure application control lists.
    fortios_application_list:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      application_list:
        app_replacemsg: "disable"
        comment: "Comments."
        control_default_network_services: "disable"
        deep_app_inspection: "disable"
        default_network_services:
         -
            id:  "8"
            port: "0"
            services: "http"
            violation_action: "pass"
        enforce_default_app_port: "disable"
        entries:
         -
            action: "pass"
            application:
             -
                id:  "16"
            behavior: "<your_own_value>"
            category:
             -
                id:  "19"
            exclusion:
             -
                id:  "21"
            id:  "22"
            log: "disable"
            log_packet: "disable"
            parameters:
             -
                id:  "26"
                members:
                 -
                    id:  "28"
                    name: "default_name_29"
                    value: "<your_own_value>"
                value: "<your_own_value>"
            per_ip_shaper: "<your_own_value> (source firewall.shaper.per-ip-shaper.name)"
            popularity: "1"
            protocols: "<your_own_value>"
            quarantine: "none"
            quarantine_expiry: "<your_own_value>"
            quarantine_log: "disable"
            rate_count: "0"
            rate_duration: "60"
            rate_mode: "periodical"
            rate_track: "none"
            risk:
             -
                level: "<you_own_value>"
            session_ttl: "0"
            shaper: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
            shaper_reverse: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
            sub_category:
             -
                id:  "48"
            technology: "<your_own_value>"
            vendor: "<your_own_value>"
        extended_log: "enable"
        force_inclusion_ssl_di_sigs: "disable"
        name: "default_name_53"
        options: "allow-dns"
        other_application_action: "pass"
        other_application_log: "disable"
        p2p_black_list: "skype"
        p2p_block_list: "skype"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        unknown_application_action: "pass"
        unknown_application_log: "disable"
```

## [Return Values](fortios_application_list_module.md#id6)

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

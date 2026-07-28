---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_wanopt_content_delivery_network_rule module – Configure WAN optimization content delivery network rules in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_wanopt_content_delivery_network_rule_module.html
fetched_at: 2026-07-28T02:30:37+00:00
---
# fortinet.fortios.fortios_wanopt_content_delivery_network_rule module – Configure WAN optimization content delivery network rules in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wanopt_content_delivery_network_rule_module.md#ansible-collections-fortinet-fortios-fortios-wanopt-content-delivery-network-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wanopt_content_delivery_network_rule`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wanopt_content_delivery_network_rule_module.md#synopsis)
- [Requirements](fortios_wanopt_content_delivery_network_rule_module.md#requirements)
- [Parameters](fortios_wanopt_content_delivery_network_rule_module.md#parameters)
- [Notes](fortios_wanopt_content_delivery_network_rule_module.md#notes)
- [Examples](fortios_wanopt_content_delivery_network_rule_module.md#examples)
- [Return Values](fortios_wanopt_content_delivery_network_rule_module.md#return-values)

## [Synopsis](fortios_wanopt_content_delivery_network_rule_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wanopt feature and content_delivery_network_rule category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wanopt_content_delivery_network_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_wanopt_content_delivery_network_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **wanopt_content_delivery_network_rule**  dictionary | Configure WAN optimization content delivery network rules. |
| **category**  string | Content delivery network rule category.  **Choices:**   - `"vcache"` - `"youtube"` |
| **comment**  string | Comment about this CDN-rule. |
| **host_domain_name_suffix**  list / elements=dictionary | Suffix portion of the fully qualified domain name. For example, fortinet.com in “www.fortinet.com”. |
| **name**  string / required | Suffix portion of the fully qualified domain name. |
| **name**  string / required | Name of table. |
| **request_cache_control**  string | Enable/disable HTTP request cache control.  **Choices:**   - `"enable"` - `"disable"` |
| **response_cache_control**  string | Enable/disable HTTP response cache control.  **Choices:**   - `"enable"` - `"disable"` |
| **response_expires**  string | Enable/disable HTTP response cache expires.  **Choices:**   - `"enable"` - `"disable"` |
| **rules**  list / elements=dictionary | WAN optimization content delivery network rule entries. |
| **content_id**  dictionary | Content ID settings. |
| **end_direction**  string | Search direction from end-str match.  **Choices:**   - `"forward"` - `"backward"` |
| **end_skip**  integer | Number of characters in URL to skip after end-str has been matched. |
| **end_str**  string | String from which to end search. |
| **range_str**  string | Name of content ID within the start string and end string. |
| **start_direction**  string | Search direction from start-str match.  **Choices:**   - `"forward"` - `"backward"` |
| **start_skip**  integer | Number of characters in URL to skip after start-str has been matched. |
| **start_str**  string | String from which to start search. |
| **target**  string | Option in HTTP header or URL parameter to match.  **Choices:**   - `"path"` - `"parameter"` - `"referrer"` - `"youtube-map"` - `"youtube-id"` - `"youku-id"` - `"hls-manifest"` - `"dash-manifest"` - `"hls-fragment"` - `"dash-fragment"` |
| **match_entries**  list / elements=dictionary | List of entries to match. |
| **id**  integer / required | Rule ID. see <a href=’#notes’>Notes</a>. |
| **pattern**  list / elements=dictionary | Pattern string for matching target (Referrer or URL pattern). For example, a, a\*c, \*a\*, a\*c\*e, and \*. |
| **string**  string / required | Pattern strings. |
| **target**  string | Option in HTTP header or URL parameter to match.  **Choices:**   - `"path"` - `"parameter"` - `"referrer"` - `"youtube-map"` - `"youtube-id"` - `"youku-id"` |
| **match_mode**  string | Match criteria for collecting content ID.  **Choices:**   - `"all"` - `"any"` |
| **name**  string / required | WAN optimization content delivery network rule name. |
| **skip_entries**  list / elements=dictionary | List of entries to skip. |
| **id**  integer / required | Rule ID. see <a href=’#notes’>Notes</a>. |
| **pattern**  list / elements=dictionary | Pattern string for matching target (Referrer or URL pattern). For example, a, a\*c, \*a\*, a\*c\*e, and \*. |
| **string**  string / required | Pattern strings. |
| **target**  string | Option in HTTP header or URL parameter to match.  **Choices:**   - `"path"` - `"parameter"` - `"referrer"` - `"youtube-map"` - `"youtube-id"` - `"youku-id"` |
| **skip_rule_mode**  string | Skip mode when evaluating skip-rules.  **Choices:**   - `"all"` - `"any"` |
| **status**  string | Enable/disable WAN optimization content delivery network rules.  **Choices:**   - `"enable"` - `"disable"` |
| **text_response_vcache**  string | Enable/disable caching of text responses.  **Choices:**   - `"enable"` - `"disable"` |
| **updateserver**  string | Enable/disable update server.  **Choices:**   - `"enable"` - `"disable"` |

## [Notes](fortios_wanopt_content_delivery_network_rule_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wanopt_content_delivery_network_rule_module.md#id5)

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
  - name: Configure WAN optimization content delivery network rules.
    fortios_wanopt_content_delivery_network_rule:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wanopt_content_delivery_network_rule:
        category: "vcache"
        comment: "Comment about this CDN-rule."
        host_domain_name_suffix:
         -
            name: "default_name_6"
        name: "default_name_7"
        request_cache_control: "enable"
        response_cache_control: "enable"
        response_expires: "enable"
        rules:
         -
            content_id:
                end_direction: "forward"
                end_skip: "0"
                end_str: "<your_own_value>"
                range_str: "<your_own_value>"
                start_direction: "forward"
                start_skip: "0"
                start_str: "<your_own_value>"
                target: "path"
            match_entries:
             -
                id:  "22"
                pattern:
                 -
                    string: "<your_own_value>"
                target: "path"
            match_mode: "all"
            name: "default_name_27"
            skip_entries:
             -
                id:  "29"
                pattern:
                 -
                    string: "<your_own_value>"
                target: "path"
            skip_rule_mode: "all"
        status: "enable"
        text_response_vcache: "enable"
        updateserver: "enable"
```

## [Return Values](fortios_wanopt_content_delivery_network_rule_module.md#id6)

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

---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_videofilter_profile module – Configure VideoFilter profile in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_videofilter_profile_module.html
fetched_at: 2026-07-28T02:30:07+00:00
---
# fortinet.fortios.fortios_videofilter_profile module – Configure VideoFilter profile in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_videofilter_profile_module.md#ansible-collections-fortinet-fortios-fortios-videofilter-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_videofilter_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_videofilter_profile_module.md#synopsis)
- [Requirements](fortios_videofilter_profile_module.md#requirements)
- [Parameters](fortios_videofilter_profile_module.md#parameters)
- [Notes](fortios_videofilter_profile_module.md#notes)
- [Examples](fortios_videofilter_profile_module.md#examples)
- [Return Values](fortios_videofilter_profile_module.md#return-values)

## [Synopsis](fortios_videofilter_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify videofilter feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_videofilter_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_videofilter_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **videofilter_profile**  dictionary | Configure VideoFilter profile. |
| **comment**  string | Comment. |
| **dailymotion**  string | Enable/disable Dailymotion video source.  **Choices:**   - `"enable"` - `"disable"` |
| **default_action**  string | Video filter default action.  **Choices:**   - `"allow"` - `"monitor"` - `"block"` |
| **fortiguard_category**  dictionary | Configure FortiGuard categories. |
| **filters**  list / elements=dictionary | Configure VideoFilter FortiGuard category. |
| **action**  string | VideoFilter action.  **Choices:**   - `"allow"` - `"monitor"` - `"block"` - `"bypass"` |
| **category_id**  integer | Category ID. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **log**  string | Enable/disable logging.  **Choices:**   - `"enable"` - `"disable"` |
| **log**  string | Enable/disable logging.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | Name. |
| **replacemsg_group**  string | Replacement message group. Source system.replacemsg-group.name. |
| **vimeo**  string | Enable/disable Vimeo video source.  **Choices:**   - `"enable"` - `"disable"` |
| **vimeo_restrict**  string | Set Vimeo-restrict (“7” = don”t show mature content, “134” = don”t show unrated and mature content). A value of cookie “content_rating”. |
| **youtube**  string | Enable/disable YouTube video source.  **Choices:**   - `"enable"` - `"disable"` |
| **youtube_channel_filter**  integer | Set YouTube channel filter. Source videofilter.youtube-channel-filter.id. |
| **youtube_restrict**  string | Set YouTube-restrict mode.  **Choices:**   - `"none"` - `"strict"` - `"moderate"` |

## [Notes](fortios_videofilter_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_videofilter_profile_module.md#id5)

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
  - name: Configure VideoFilter profile.
    fortios_videofilter_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      videofilter_profile:
        comment: "Comment."
        dailymotion: "enable"
        default_action: "allow"
        fortiguard_category:
            filters:
             -
                action: "allow"
                category_id: "0"
                id:  "10"
                log: "enable"
        log: "enable"
        name: "default_name_13"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        vimeo: "enable"
        vimeo_restrict: "<your_own_value>"
        youtube: "enable"
        youtube_channel_filter: "0"
        youtube_restrict: "none"
```

## [Return Values](fortios_videofilter_profile_module.md#id6)

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

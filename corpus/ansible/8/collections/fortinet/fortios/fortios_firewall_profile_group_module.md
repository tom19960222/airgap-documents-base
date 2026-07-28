---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_profile_group module – Configure profile groups in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_profile_group_module.html
fetched_at: 2026-07-28T02:24:57+00:00
---
# fortinet.fortios.fortios_firewall_profile_group module – Configure profile groups in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_profile_group_module.md#ansible-collections-fortinet-fortios-fortios-firewall-profile-group-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_profile_group`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_profile_group_module.md#synopsis)
- [Requirements](fortios_firewall_profile_group_module.md#requirements)
- [Parameters](fortios_firewall_profile_group_module.md#parameters)
- [Notes](fortios_firewall_profile_group_module.md#notes)
- [Examples](fortios_firewall_profile_group_module.md#examples)
- [Return Values](fortios_firewall_profile_group_module.md#return-values)

## [Synopsis](fortios_firewall_profile_group_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and profile_group category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_profile_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_profile_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_profile_group**  dictionary | Configure profile groups. |
| **application_list**  string | Name of an existing Application list. Source application.list.name. |
| **av_profile**  string | Name of an existing Antivirus profile. Source antivirus.profile.name. |
| **casb_profile**  string | Name of an existing CASB profile. Source casb.profile.name. |
| **cifs_profile**  string | Name of an existing CIFS profile. Source cifs.profile.name. |
| **dlp_profile**  string | Name of an existing DLP profile. Source dlp.profile.name. |
| **dlp_sensor**  string | Name of an existing DLP sensor. Source dlp.sensor.name. |
| **dnsfilter_profile**  string | Name of an existing DNS filter profile. Source dnsfilter.profile.name. |
| **emailfilter_profile**  string | Name of an existing email filter profile. Source emailfilter.profile.name. |
| **file_filter_profile**  string | Name of an existing file-filter profile. Source file-filter.profile.name. |
| **icap_profile**  string | Name of an existing ICAP profile. Source icap.profile.name. |
| **ips_sensor**  string | Name of an existing IPS sensor. Source ips.sensor.name. |
| **ips_voip_filter**  string | Name of an existing VoIP (ips) profile. Source voip.profile.name. |
| **mms_profile**  string | Name of an existing MMS profile. Source firewall.mms-profile.name. |
| **name**  string / required | Profile group name. |
| **profile_protocol_options**  string | Name of an existing Protocol options profile. Source firewall.profile-protocol-options.name. |
| **sctp_filter_profile**  string | Name of an existing SCTP filter profile. Source sctp-filter.profile.name. |
| **spamfilter_profile**  string | Name of an existing Spam filter profile. Source spamfilter.profile.name. |
| **ssh_filter_profile**  string | Name of an existing SSH filter profile. Source ssh-filter.profile.name. |
| **ssl_ssh_profile**  string | Name of an existing SSL SSH profile. Source firewall.ssl-ssh-profile.name. |
| **videofilter_profile**  string | Name of an existing VideoFilter profile. Source videofilter.profile.name. |
| **virtual_patch_profile**  string | Name of an existing virtual-patch profile. Source virtual-patch.profile.name. |
| **voip_profile**  string | Name of an existing VoIP (voipd) profile. Source voip.profile.name. |
| **waf_profile**  string | Name of an existing Web application firewall profile. Source waf.profile.name. |
| **webfilter_profile**  string | Name of an existing Web filter profile. Source webfilter.profile.name. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_profile_group_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_profile_group_module.md#id5)

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
  - name: Configure profile groups.
    fortios_firewall_profile_group:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_profile_group:
        application_list: "<your_own_value> (source application.list.name)"
        av_profile: "<your_own_value> (source antivirus.profile.name)"
        casb_profile: "<your_own_value> (source casb.profile.name)"
        cifs_profile: "<your_own_value> (source cifs.profile.name)"
        dlp_profile: "<your_own_value> (source dlp.profile.name)"
        dlp_sensor: "<your_own_value> (source dlp.sensor.name)"
        dnsfilter_profile: "<your_own_value> (source dnsfilter.profile.name)"
        emailfilter_profile: "<your_own_value> (source emailfilter.profile.name)"
        file_filter_profile: "<your_own_value> (source file-filter.profile.name)"
        icap_profile: "<your_own_value> (source icap.profile.name)"
        ips_sensor: "<your_own_value> (source ips.sensor.name)"
        ips_voip_filter: "<your_own_value> (source voip.profile.name)"
        mms_profile: "<your_own_value> (source firewall.mms-profile.name)"
        name: "default_name_16"
        profile_protocol_options: "<your_own_value> (source firewall.profile-protocol-options.name)"
        sctp_filter_profile: "<your_own_value> (source sctp-filter.profile.name)"
        spamfilter_profile: "<your_own_value> (source spamfilter.profile.name)"
        ssh_filter_profile: "<your_own_value> (source ssh-filter.profile.name)"
        ssl_ssh_profile: "<your_own_value> (source firewall.ssl-ssh-profile.name)"
        videofilter_profile: "<your_own_value> (source videofilter.profile.name)"
        virtual_patch_profile: "<your_own_value> (source virtual-patch.profile.name)"
        voip_profile: "<your_own_value> (source voip.profile.name)"
        waf_profile: "<your_own_value> (source waf.profile.name)"
        webfilter_profile: "<your_own_value> (source webfilter.profile.name)"
```

## [Return Values](fortios_firewall_profile_group_module.md#id6)

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

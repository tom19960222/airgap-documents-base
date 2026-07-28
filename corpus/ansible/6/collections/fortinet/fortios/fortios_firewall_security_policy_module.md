---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_security_policy module – Configure NGFW IPv4/IPv6 application policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_security_policy_module.html
fetched_at: 2026-07-27T17:41:28+00:00
---
# fortinet.fortios.fortios_firewall_security_policy module – Configure NGFW IPv4/IPv6 application policies in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_security_policy_module.md#ansible-collections-fortinet-fortios-fortios-firewall-security-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_security_policy`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_security_policy_module.md#synopsis)
- [Requirements](fortios_firewall_security_policy_module.md#requirements)
- [Parameters](fortios_firewall_security_policy_module.md#parameters)
- [Notes](fortios_firewall_security_policy_module.md#notes)
- [Examples](fortios_firewall_security_policy_module.md#examples)
- [Return Values](fortios_firewall_security_policy_module.md#return-values)

## [Synopsis](fortios_firewall_security_policy_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and security_policy category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_security_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_security_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_security_policy**  dictionary | Configure NGFW IPv4/IPv6 application policies. |
| **action**  string | Policy action (accept/deny).  Choices:   - `"accept"` - `"deny"` |
| **app_category**  list / elements=dictionary | Application category ID list. |
| **id**  integer | Category IDs. |
| **app_group**  list / elements=dictionary | Application group names. |
| **name**  string | Application group names. Source application.group.name. |
| **application**  list / elements=dictionary | Application ID list. |
| **id**  integer | Application IDs. |
| **application_list**  string | Name of an existing Application list. Source application.list.name. |
| **av_profile**  string | Name of an existing Antivirus profile. Source antivirus.profile.name. |
| **cifs_profile**  string | Name of an existing CIFS profile. Source cifs.profile.name. |
| **comments**  string | Comment. |
| **dlp_profile**  string | Name of an existing DLP profile. Source dlp.profile.name. |
| **dlp_sensor**  string | Name of an existing DLP sensor. Source dlp.sensor.name. |
| **dnsfilter_profile**  string | Name of an existing DNS filter profile. Source dnsfilter.profile.name. |
| **dstaddr**  list / elements=dictionary | Destination IPv4 address name and address group names. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name firewall.vip.name firewall.vipgrp.name system.external-resource .name. |
| **dstaddr4**  list / elements=dictionary | Destination IPv4 address name and address group names. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name firewall.vip.name firewall.vipgrp.name. |
| **dstaddr6**  list / elements=dictionary | Destination IPv6 address name and address group names. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name firewall.vip6.name firewall.vipgrp6.name system .external-resource.name. |
| **dstaddr_negate**  string | When enabled dstaddr specifies what the destination address must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **dstintf**  list / elements=dictionary | Outgoing (egress) interface. |
| **name**  string | Interface name. Source system.interface.name system.zone.name system.sdwan.zone.name. |
| **emailfilter_profile**  string | Name of an existing email filter profile. Source emailfilter.profile.name. |
| **enforce_default_app_port**  string | Enable/disable default application port enforcement for allowed applications.  Choices:   - `"enable"` - `"disable"` |
| **file_filter_profile**  string | Name of an existing file-filter profile. Source file-filter.profile.name. |
| **fsso_groups**  list / elements=dictionary | Names of FSSO groups. |
| **name**  string | Names of FSSO groups. Source user.adgrp.name. |
| **global_label**  string | Label for the policy that appears when the GUI is in Global View mode. |
| **groups**  list / elements=dictionary | Names of user groups that can authenticate with this policy. |
| **name**  string | User group name. Source user.group.name. |
| **icap_profile**  string | Name of an existing ICAP profile. Source icap.profile.name. |
| **internet_service**  string | Enable/disable use of Internet Services for this policy. If enabled, destination address, service and default application port enforcement are not used.  Choices:   - `"enable"` - `"disable"` |
| **internet_service6**  string | Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address, service and default application port enforcement are not used.  Choices:   - `"enable"` - `"disable"` |
| **internet_service6_custom**  list / elements=dictionary | Custom IPv6 Internet Service name. |
| **name**  string | Custom IPv6 Internet Service name. Source . |
| **internet_service6_custom_group**  list / elements=dictionary | Custom IPv6 Internet Service group name. |
| **name**  string | Custom IPv6 Internet Service group name. Source . |
| **internet_service6_group**  list / elements=dictionary | Internet Service group name. |
| **name**  string | Internet Service group name. Source . |
| **internet_service6_name**  list / elements=dictionary | IPv6 Internet Service name. |
| **name**  string | IPv6 Internet Service name. Source . |
| **internet_service6_negate**  string | When enabled internet-service6 specifies what the service must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **internet_service6_src**  string | Enable/disable use of IPv6 Internet Services in source for this policy. If enabled, source address is not used.  Choices:   - `"enable"` - `"disable"` |
| **internet_service6_src_custom**  list / elements=dictionary | Custom IPv6 Internet Service source name. |
| **name**  string | Custom Internet Service name. Source . |
| **internet_service6_src_custom_group**  list / elements=dictionary | Custom Internet Service6 source group name. |
| **name**  string | Custom Internet Service6 group name. Source . |
| **internet_service6_src_group**  list / elements=dictionary | Internet Service6 source group name. |
| **name**  string | Internet Service group name. Source . |
| **internet_service6_src_name**  list / elements=dictionary | IPv6 Internet Service source name. |
| **name**  string | Internet Service name. Source . |
| **internet_service6_src_negate**  string | When enabled internet-service6-src specifies what the service must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **internet_service_custom**  list / elements=dictionary | Custom Internet Service name. |
| **name**  string | Custom Internet Service name. Source firewall.internet-service-custom.name. |
| **internet_service_custom_group**  list / elements=dictionary | Custom Internet Service group name. |
| **name**  string | Custom Internet Service group name. Source firewall.internet-service-custom-group.name. |
| **internet_service_group**  list / elements=dictionary | Internet Service group name. |
| **name**  string | Internet Service group name. Source firewall.internet-service-group.name. |
| **internet_service_id**  list / elements=dictionary | Internet Service ID. |
| **id**  integer | Internet Service ID. Source firewall.internet-service.id. |
| **internet_service_name**  list / elements=dictionary | Internet Service name. |
| **name**  string | Internet Service name. Source firewall.internet-service-name.name. |
| **internet_service_negate**  string | When enabled internet-service specifies what the service must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **internet_service_src**  string | Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.  Choices:   - `"enable"` - `"disable"` |
| **internet_service_src_custom**  list / elements=dictionary | Custom Internet Service source name. |
| **name**  string | Custom Internet Service name. Source firewall.internet-service-custom.name. |
| **internet_service_src_custom_group**  list / elements=dictionary | Custom Internet Service source group name. |
| **name**  string | Custom Internet Service group name. Source firewall.internet-service-custom-group.name. |
| **internet_service_src_group**  list / elements=dictionary | Internet Service source group name. |
| **name**  string | Internet Service group name. Source firewall.internet-service-group.name. |
| **internet_service_src_id**  list / elements=dictionary | Internet Service source ID. |
| **id**  integer | Internet Service ID. Source firewall.internet-service.id. |
| **internet_service_src_name**  list / elements=dictionary | Internet Service source name. |
| **name**  string | Internet Service name. Source firewall.internet-service-name.name. |
| **internet_service_src_negate**  string | When enabled internet-service-src specifies what the service must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **ips_sensor**  string | Name of an existing IPS sensor. Source ips.sensor.name. |
| **learning_mode**  string | Enable to allow everything, but log all of the meaningful data for security information gathering. A learning report will be generated.  Choices:   - `"enable"` - `"disable"` |
| **logtraffic**  string | Enable or disable logging. Log all sessions or security profile sessions.  Choices:   - `"all"` - `"utm"` - `"disable"` |
| **logtraffic_start**  string | Record logs when a session starts.  Choices:   - `"enable"` - `"disable"` |
| **mms_profile**  string | Name of an existing MMS profile. Source firewall.mms-profile.name. |
| **name**  string | Policy name. |
| **nat46**  string | Enable/disable NAT46.  Choices:   - `"enable"` - `"disable"` |
| **nat64**  string | Enable/disable NAT64.  Choices:   - `"enable"` - `"disable"` |
| **policyid**  integer / required | Policy ID. |
| **profile_group**  string | Name of profile group. Source firewall.profile-group.name. |
| **profile_protocol_options**  string | Name of an existing Protocol options profile. Source firewall.profile-protocol-options.name. |
| **profile_type**  string | Determine whether the firewall policy allows security profile groups or single profiles only.  Choices:   - `"single"` - `"group"` |
| **schedule**  string | Schedule name. Source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name. |
| **sctp_filter_profile**  string | Name of an existing SCTP filter profile. Source sctp-filter.profile.name. |
| **send_deny_packet**  string | Enable to send a reply when a session is denied or blocked by a firewall policy.  Choices:   - `"disable"` - `"enable"` |
| **service**  list / elements=dictionary | Service and service group names. |
| **name**  string | Service name. Source firewall.service.custom.name firewall.service.group.name. |
| **service_negate**  string | When enabled service specifies what the service must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **srcaddr**  list / elements=dictionary | Source IPv4 address name and address group names. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name system.external-resource.name. |
| **srcaddr4**  list / elements=dictionary | Source IPv4 address name and address group names. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **srcaddr6**  list / elements=dictionary | Source IPv6 address name and address group names. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name system.external-resource.name. |
| **srcaddr_negate**  string | When enabled srcaddr specifies what the source address must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **srcintf**  list / elements=dictionary | Incoming (ingress) interface. |
| **name**  string | Interface name. Source system.interface.name system.zone.name system.sdwan.zone.name. |
| **ssh_filter_profile**  string | Name of an existing SSH filter profile. Source ssh-filter.profile.name. |
| **ssl_ssh_profile**  string | Name of an existing SSL SSH profile. Source firewall.ssl-ssh-profile.name. |
| **status**  string | Enable or disable this policy.  Choices:   - `"enable"` - `"disable"` |
| **url_category**  list / elements=string | URL categories or groups. |
| **users**  list / elements=dictionary | Names of individual users that can authenticate with this policy. |
| **name**  string | User name. Source user.local.name. |
| **utm_status**  string | Enable security profiles.  Choices:   - `"enable"` - `"disable"` |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **uuid_idx**  integer | uuid-idx |
| **videofilter_profile**  string | Name of an existing VideoFilter profile. Source videofilter.profile.name. |
| **voip_profile**  string | Name of an existing VoIP profile. Source voip.profile.name. |
| **webfilter_profile**  string | Name of an existing Web filter profile. Source webfilter.profile.name. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_security_policy_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_security_policy_module.md#id5)

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
  - name: Configure NGFW IPv4/IPv6 application policies.
    fortios_firewall_security_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_security_policy:
        action: "accept"
        app_category:
         -
            id:  "5"
        app_group:
         -
            name: "default_name_7 (source application.group.name)"
        application:
         -
            id:  "9"
        application_list: "<your_own_value> (source application.list.name)"
        av_profile: "<your_own_value> (source antivirus.profile.name)"
        cifs_profile: "<your_own_value> (source cifs.profile.name)"
        comments: "<your_own_value>"
        dlp_profile: "<your_own_value> (source dlp.profile.name)"
        dlp_sensor: "<your_own_value> (source dlp.sensor.name)"
        dnsfilter_profile: "<your_own_value> (source dnsfilter.profile.name)"
        dstaddr:
         -
            name: "default_name_18 (source firewall.address.name firewall.addrgrp.name firewall.vip.name firewall.vipgrp.name system.external-resource.name)"
        dstaddr_negate: "enable"
        dstaddr4:
         -
            name: "default_name_21 (source firewall.address.name firewall.addrgrp.name firewall.vip.name firewall.vipgrp.name)"
        dstaddr6:
         -
            name: "default_name_23 (source firewall.address6.name firewall.addrgrp6.name firewall.vip6.name firewall.vipgrp6.name system.external-resource
              .name)"
        dstintf:
         -
            name: "default_name_25 (source system.interface.name system.zone.name system.sdwan.zone.name)"
        emailfilter_profile: "<your_own_value> (source emailfilter.profile.name)"
        enforce_default_app_port: "enable"
        file_filter_profile: "<your_own_value> (source file-filter.profile.name)"
        fsso_groups:
         -
            name: "default_name_30 (source user.adgrp.name)"
        global_label: "<your_own_value>"
        groups:
         -
            name: "default_name_33 (source user.group.name)"
        icap_profile: "<your_own_value> (source icap.profile.name)"
        internet_service: "enable"
        internet_service_custom:
         -
            name: "default_name_37 (source firewall.internet-service-custom.name)"
        internet_service_custom_group:
         -
            name: "default_name_39 (source firewall.internet-service-custom-group.name)"
        internet_service_group:
         -
            name: "default_name_41 (source firewall.internet-service-group.name)"
        internet_service_id:
         -
            id:  "43 (source firewall.internet-service.id)"
        internet_service_name:
         -
            name: "default_name_45 (source firewall.internet-service-name.name)"
        internet_service_negate: "enable"
        internet_service_src: "enable"
        internet_service_src_custom:
         -
            name: "default_name_49 (source firewall.internet-service-custom.name)"
        internet_service_src_custom_group:
         -
            name: "default_name_51 (source firewall.internet-service-custom-group.name)"
        internet_service_src_group:
         -
            name: "default_name_53 (source firewall.internet-service-group.name)"
        internet_service_src_id:
         -
            id:  "55 (source firewall.internet-service.id)"
        internet_service_src_name:
         -
            name: "default_name_57 (source firewall.internet-service-name.name)"
        internet_service_src_negate: "enable"
        internet_service6: "enable"
        internet_service6_custom:
         -
            name: "default_name_61 (source )"
        internet_service6_custom_group:
         -
            name: "default_name_63 (source )"
        internet_service6_group:
         -
            name: "default_name_65 (source )"
        internet_service6_name:
         -
            name: "default_name_67 (source )"
        internet_service6_negate: "enable"
        internet_service6_src: "enable"
        internet_service6_src_custom:
         -
            name: "default_name_71 (source )"
        internet_service6_src_custom_group:
         -
            name: "default_name_73 (source )"
        internet_service6_src_group:
         -
            name: "default_name_75 (source )"
        internet_service6_src_name:
         -
            name: "default_name_77 (source )"
        internet_service6_src_negate: "enable"
        ips_sensor: "<your_own_value> (source ips.sensor.name)"
        learning_mode: "enable"
        logtraffic: "all"
        logtraffic_start: "enable"
        mms_profile: "<your_own_value> (source firewall.mms-profile.name)"
        name: "default_name_84"
        nat46: "enable"
        nat64: "enable"
        policyid: "0"
        profile_group: "<your_own_value> (source firewall.profile-group.name)"
        profile_protocol_options: "<your_own_value> (source firewall.profile-protocol-options.name)"
        profile_type: "single"
        schedule: "<your_own_value> (source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name)"
        sctp_filter_profile: "<your_own_value> (source sctp-filter.profile.name)"
        send_deny_packet: "disable"
        service:
         -
            name: "default_name_95 (source firewall.service.custom.name firewall.service.group.name)"
        service_negate: "enable"
        srcaddr:
         -
            name: "default_name_98 (source firewall.address.name firewall.addrgrp.name system.external-resource.name)"
        srcaddr_negate: "enable"
        srcaddr4:
         -
            name: "default_name_101 (source firewall.address.name firewall.addrgrp.name)"
        srcaddr6:
         -
            name: "default_name_103 (source firewall.address6.name firewall.addrgrp6.name system.external-resource.name)"
        srcintf:
         -
            name: "default_name_105 (source system.interface.name system.zone.name system.sdwan.zone.name)"
        ssh_filter_profile: "<your_own_value> (source ssh-filter.profile.name)"
        ssl_ssh_profile: "<your_own_value> (source firewall.ssl-ssh-profile.name)"
        status: "enable"
        url_category: "<your_own_value>"
        users:
         -
            name: "default_name_111 (source user.local.name)"
        utm_status: "enable"
        uuid: "<your_own_value>"
        uuid_idx: "2147483647"
        videofilter_profile: "<your_own_value> (source videofilter.profile.name)"
        voip_profile: "<your_own_value> (source voip.profile.name)"
        webfilter_profile: "<your_own_value> (source webfilter.profile.name)"
```

## [Return Values](fortios_firewall_security_policy_module.md#id6)

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

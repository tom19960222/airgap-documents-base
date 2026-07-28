---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_proxy_policy module – Configure proxy policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_proxy_policy_module.html
fetched_at: 2026-07-28T02:25:00+00:00
---
# fortinet.fortios.fortios_firewall_proxy_policy module – Configure proxy policies in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_proxy_policy_module.md#ansible-collections-fortinet-fortios-fortios-firewall-proxy-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_proxy_policy`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_proxy_policy_module.md#synopsis)
- [Requirements](fortios_firewall_proxy_policy_module.md#requirements)
- [Parameters](fortios_firewall_proxy_policy_module.md#parameters)
- [Notes](fortios_firewall_proxy_policy_module.md#notes)
- [Examples](fortios_firewall_proxy_policy_module.md#examples)
- [Return Values](fortios_firewall_proxy_policy_module.md#return-values)

## [Synopsis](fortios_firewall_proxy_policy_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and proxy_policy category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_proxy_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_proxy_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_proxy_policy**  dictionary | Configure proxy policies. |
| **access_proxy**  list / elements=dictionary | IPv4 access proxy. |
| **name**  string / required | Access Proxy name. Source firewall.access-proxy.name. |
| **access_proxy6**  list / elements=dictionary | IPv6 access proxy. |
| **name**  string / required | Access proxy name. Source firewall.access-proxy6.name. |
| **action**  string | Accept or deny traffic matching the policy parameters.  **Choices:**   - `"accept"` - `"deny"` - `"redirect"` |
| **application_list**  string | Name of an existing Application list. Source application.list.name. |
| **av_profile**  string | Name of an existing Antivirus profile. Source antivirus.profile.name. |
| **block_notification**  string | Enable/disable block notification.  **Choices:**   - `"enable"` - `"disable"` |
| **casb_profile**  string | Name of an existing CASB profile. Source casb.profile.name. |
| **cifs_profile**  string | Name of an existing CIFS profile. Source cifs.profile.name. |
| **comments**  string | Optional comments. |
| **decrypted_traffic_mirror**  string | Decrypted traffic mirror. Source firewall.decrypted-traffic-mirror.name. |
| **detect_https_in_http_request**  string | Enable/disable detection of HTTPS in HTTP request.  **Choices:**   - `"enable"` - `"disable"` |
| **device_ownership**  string | When enabled, the ownership enforcement will be done at policy level.  **Choices:**   - `"enable"` - `"disable"` |
| **disclaimer**  string | Web proxy disclaimer setting: by domain, policy, or user.  **Choices:**   - `"disable"` - `"domain"` - `"policy"` - `"user"` |
| **dlp_profile**  string | Name of an existing DLP profile. Source dlp.profile.name. |
| **dlp_sensor**  string | Name of an existing DLP sensor. Source dlp.sensor.name. |
| **dstaddr**  list / elements=dictionary | Destination address objects. |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name firewall.proxy-addrgrp.name firewall.vip.name firewall.vipgrp.name system.external-resource.name. |
| **dstaddr6**  list / elements=dictionary | IPv6 destination address objects. |
| **name**  string / required | Address name. Source firewall.address6.name firewall.addrgrp6.name firewall.vip6.name firewall.vipgrp6.name system .external-resource.name. |
| **dstaddr_negate**  string | When enabled, destination addresses match against any address EXCEPT the specified destination addresses.  **Choices:**   - `"enable"` - `"disable"` |
| **dstintf**  list / elements=dictionary | Destination interface names. |
| **name**  string / required | Interface name. Source system.interface.name system.zone.name system.sdwan.zone.name. |
| **emailfilter_profile**  string | Name of an existing email filter profile. Source emailfilter.profile.name. |
| **file_filter_profile**  string | Name of an existing file-filter profile. Source file-filter.profile.name. |
| **global_label**  string | Global web-based manager visible label. |
| **groups**  list / elements=dictionary | Names of group objects. |
| **name**  string / required | Group name. Source user.group.name. |
| **http_tunnel_auth**  string | Enable/disable HTTP tunnel authentication.  **Choices:**   - `"enable"` - `"disable"` |
| **icap_profile**  string | Name of an existing ICAP profile. Source icap.profile.name. |
| **internet_service**  string | Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.  **Choices:**   - `"enable"` - `"disable"` |
| **internet_service6**  string | Enable/disable use of Internet Services IPv6 for this policy. If enabled, destination IPv6 address and service are not used.  **Choices:**   - `"enable"` - `"disable"` |
| **internet_service6_custom**  list / elements=dictionary | Custom Internet Service IPv6 name. |
| **name**  string / required | Custom Internet Service IPv6 name. Source firewall.internet-service-custom.name. |
| **internet_service6_custom_group**  list / elements=dictionary | Custom Internet Service IPv6 group name. |
| **name**  string / required | Custom Internet Service IPv6 group name. Source firewall.internet-service-custom-group.name. |
| **internet_service6_group**  list / elements=dictionary | Internet Service IPv6 group name. |
| **name**  string / required | Internet Service IPv6 group name. Source firewall.internet-service-group.name. |
| **internet_service6_name**  list / elements=dictionary | Internet Service IPv6 name. |
| **name**  string / required | Internet Service IPv6 name. Source firewall.internet-service-name.name. |
| **internet_service6_negate**  string | When enabled, Internet Services match against any internet service IPv6 EXCEPT the selected Internet Service IPv6.  **Choices:**   - `"enable"` - `"disable"` |
| **internet_service_custom**  list / elements=dictionary | Custom Internet Service name. |
| **name**  string / required | Custom Internet Service name. Source firewall.internet-service-custom.name. |
| **internet_service_custom_group**  list / elements=dictionary | Custom Internet Service group name. |
| **name**  string / required | Custom Internet Service group name. Source firewall.internet-service-custom-group.name. |
| **internet_service_group**  list / elements=dictionary | Internet Service group name. |
| **name**  string / required | Internet Service group name. Source firewall.internet-service-group.name. |
| **internet_service_id**  list / elements=dictionary | Internet Service ID. |
| **id**  integer / required | Internet Service ID. see <a href=’#notes’>Notes</a>. Source firewall.internet-service.id. |
| **internet_service_name**  list / elements=dictionary | Internet Service name. |
| **name**  string / required | Internet Service name. Source firewall.internet-service-name.name. |
| **internet_service_negate**  string | When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service.  **Choices:**   - `"enable"` - `"disable"` |
| **ips_sensor**  string | Name of an existing IPS sensor. Source ips.sensor.name. |
| **ips_voip_filter**  string | Name of an existing VoIP (ips) profile. Source voip.profile.name. |
| **label**  string | VDOM-specific GUI visible label. |
| **logtraffic**  string | Enable/disable logging traffic through the policy.  **Choices:**   - `"all"` - `"utm"` - `"disable"` |
| **logtraffic_start**  string | Enable/disable policy log traffic start.  **Choices:**   - `"enable"` - `"disable"` |
| **mms_profile**  string | Name of an existing MMS profile. Source firewall.mms-profile.name. |
| **name**  string | Policy name. |
| **policyid**  integer / required | Policy ID. see <a href=’#notes’>Notes</a>. |
| **poolname**  list / elements=dictionary | Name of IP pool object. |
| **name**  string / required | IP pool name. Source firewall.ippool.name. |
| **profile_group**  string | Name of profile group. Source firewall.profile-group.name. |
| **profile_protocol_options**  string | Name of an existing Protocol options profile. Source firewall.profile-protocol-options.name. |
| **profile_type**  string | Determine whether the firewall policy allows security profile groups or single profiles only.  **Choices:**   - `"single"` - `"group"` |
| **proxy**  string | Type of explicit proxy.  **Choices:**   - `"explicit-web"` - `"transparent-web"` - `"ftp"` - `"ssh"` - `"ssh-tunnel"` - `"access-proxy"` - `"wanopt"` |
| **redirect_url**  string | Redirect URL for further explicit web proxy processing. |
| **replacemsg_override_group**  string | Authentication replacement message override group. Source system.replacemsg-group.name. |
| **scan_botnet_connections**  string | Enable/disable scanning of connections to Botnet servers.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  string | Name of schedule object. Source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name. |
| **sctp_filter_profile**  string | Name of an existing SCTP filter profile. Source sctp-filter.profile.name. |
| **service**  list / elements=dictionary | Name of service objects. |
| **name**  string / required | Service name. Source firewall.service.custom.name firewall.service.group.name. |
| **service_negate**  string | When enabled, services match against any service EXCEPT the specified destination services.  **Choices:**   - `"enable"` - `"disable"` |
| **session_ttl**  integer | TTL in seconds for sessions accepted by this policy (0 means use the system ). |
| **spamfilter_profile**  string | Name of an existing Spam filter profile. Source spamfilter.profile.name. |
| **srcaddr**  list / elements=dictionary | Source address objects. |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name firewall.proxy-addrgrp.name system .external-resource.name. |
| **srcaddr6**  list / elements=dictionary | IPv6 source address objects. |
| **name**  string / required | Address name. Source firewall.address6.name firewall.addrgrp6.name system.external-resource.name. |
| **srcaddr_negate**  string | When enabled, source addresses match against any address EXCEPT the specified source addresses.  **Choices:**   - `"enable"` - `"disable"` |
| **srcintf**  list / elements=dictionary | Source interface names. |
| **name**  string / required | Interface name. Source system.interface.name system.zone.name system.sdwan.zone.name. |
| **ssh_filter_profile**  string | Name of an existing SSH filter profile. Source ssh-filter.profile.name. |
| **ssh_policy_redirect**  string | Redirect SSH traffic to matching transparent proxy policy.  **Choices:**   - `"enable"` - `"disable"` |
| **ssl_ssh_profile**  string | Name of an existing SSL SSH profile. Source firewall.ssl-ssh-profile.name. |
| **status**  string | Enable/disable the active status of the policy.  **Choices:**   - `"enable"` - `"disable"` |
| **transparent**  string | Enable to use the IP address of the client to connect to the server.  **Choices:**   - `"enable"` - `"disable"` |
| **users**  list / elements=dictionary | Names of user objects. |
| **name**  string / required | Group name. Source user.local.name user.certificate.name. |
| **utm_status**  string | Enable the use of UTM profiles/sensors/lists.  **Choices:**   - `"enable"` - `"disable"` |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **videofilter_profile**  string | Name of an existing VideoFilter profile. Source videofilter.profile.name. |
| **virtual_patch_profile**  string | Name of an existing virtual-patch profile. Source virtual-patch.profile.name. |
| **voip_profile**  string | Name of an existing VoIP profile. Source voip.profile.name. |
| **waf_profile**  string | Name of an existing Web application firewall profile. Source waf.profile.name. |
| **webcache**  string | Enable/disable web caching.  **Choices:**   - `"enable"` - `"disable"` |
| **webcache_https**  string | Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ssh-profile).  **Choices:**   - `"disable"` - `"enable"` |
| **webfilter_profile**  string | Name of an existing Web filter profile. Source webfilter.profile.name. |
| **webproxy_forward_server**  string | Web proxy forward server name. Source web-proxy.forward-server.name web-proxy.forward-server-group.name. |
| **webproxy_profile**  string | Name of web proxy profile. Source web-proxy.profile.name. |
| **ztna_ems_tag**  list / elements=dictionary | ZTNA EMS Tag names. |
| **name**  string / required | EMS Tag name. Source firewall.address.name firewall.addrgrp.name. |
| **ztna_tags_match_logic**  string | ZTNA tag matching logic.  **Choices:**   - `"or"` - `"and"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_proxy_policy_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the policyid instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_proxy_policy_module.md#id5)

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
  - name: Configure proxy policies.
    fortios_firewall_proxy_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_proxy_policy:
        access_proxy:
         -
            name: "default_name_4 (source firewall.access-proxy.name)"
        access_proxy6:
         -
            name: "default_name_6 (source firewall.access-proxy6.name)"
        action: "accept"
        application_list: "<your_own_value> (source application.list.name)"
        av_profile: "<your_own_value> (source antivirus.profile.name)"
        block_notification: "enable"
        casb_profile: "<your_own_value> (source casb.profile.name)"
        cifs_profile: "<your_own_value> (source cifs.profile.name)"
        comments: "<your_own_value>"
        decrypted_traffic_mirror: "<your_own_value> (source firewall.decrypted-traffic-mirror.name)"
        detect_https_in_http_request: "enable"
        device_ownership: "enable"
        disclaimer: "disable"
        dlp_profile: "<your_own_value> (source dlp.profile.name)"
        dlp_sensor: "<your_own_value> (source dlp.sensor.name)"
        dstaddr:
         -
            name: "default_name_21 (source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name firewall.proxy-addrgrp.name firewall.vip
              .name firewall.vipgrp.name system.external-resource.name)"
        dstaddr_negate: "enable"
        dstaddr6:
         -
            name: "default_name_24 (source firewall.address6.name firewall.addrgrp6.name firewall.vip6.name firewall.vipgrp6.name system.external-resource
              .name)"
        dstintf:
         -
            name: "default_name_26 (source system.interface.name system.zone.name system.sdwan.zone.name)"
        emailfilter_profile: "<your_own_value> (source emailfilter.profile.name)"
        file_filter_profile: "<your_own_value> (source file-filter.profile.name)"
        global_label: "<your_own_value>"
        groups:
         -
            name: "default_name_31 (source user.group.name)"
        http_tunnel_auth: "enable"
        icap_profile: "<your_own_value> (source icap.profile.name)"
        internet_service: "enable"
        internet_service_custom:
         -
            name: "default_name_36 (source firewall.internet-service-custom.name)"
        internet_service_custom_group:
         -
            name: "default_name_38 (source firewall.internet-service-custom-group.name)"
        internet_service_group:
         -
            name: "default_name_40 (source firewall.internet-service-group.name)"
        internet_service_id:
         -
            id:  "42 (source firewall.internet-service.id)"
        internet_service_name:
         -
            name: "default_name_44 (source firewall.internet-service-name.name)"
        internet_service_negate: "enable"
        internet_service6: "enable"
        internet_service6_custom:
         -
            name: "default_name_48 (source firewall.internet-service-custom.name)"
        internet_service6_custom_group:
         -
            name: "default_name_50 (source firewall.internet-service-custom-group.name)"
        internet_service6_group:
         -
            name: "default_name_52 (source firewall.internet-service-group.name)"
        internet_service6_name:
         -
            name: "default_name_54 (source firewall.internet-service-name.name)"
        internet_service6_negate: "enable"
        ips_sensor: "<your_own_value> (source ips.sensor.name)"
        ips_voip_filter: "<your_own_value> (source voip.profile.name)"
        label: "<your_own_value>"
        logtraffic: "all"
        logtraffic_start: "enable"
        mms_profile: "<your_own_value> (source firewall.mms-profile.name)"
        name: "default_name_62"
        policyid: "<you_own_value>"
        poolname:
         -
            name: "default_name_65 (source firewall.ippool.name)"
        profile_group: "<your_own_value> (source firewall.profile-group.name)"
        profile_protocol_options: "<your_own_value> (source firewall.profile-protocol-options.name)"
        profile_type: "single"
        proxy: "explicit-web"
        redirect_url: "<your_own_value>"
        replacemsg_override_group: "<your_own_value> (source system.replacemsg-group.name)"
        scan_botnet_connections: "disable"
        schedule: "<your_own_value> (source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name)"
        sctp_filter_profile: "<your_own_value> (source sctp-filter.profile.name)"
        service:
         -
            name: "default_name_76 (source firewall.service.custom.name firewall.service.group.name)"
        service_negate: "enable"
        session_ttl: "0"
        spamfilter_profile: "<your_own_value> (source spamfilter.profile.name)"
        srcaddr:
         -
            name: "default_name_81 (source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name firewall.proxy-addrgrp.name system
              .external-resource.name)"
        srcaddr_negate: "enable"
        srcaddr6:
         -
            name: "default_name_84 (source firewall.address6.name firewall.addrgrp6.name system.external-resource.name)"
        srcintf:
         -
            name: "default_name_86 (source system.interface.name system.zone.name system.sdwan.zone.name)"
        ssh_filter_profile: "<your_own_value> (source ssh-filter.profile.name)"
        ssh_policy_redirect: "enable"
        ssl_ssh_profile: "<your_own_value> (source firewall.ssl-ssh-profile.name)"
        status: "enable"
        transparent: "enable"
        users:
         -
            name: "default_name_93 (source user.local.name user.certificate.name)"
        utm_status: "enable"
        uuid: "<your_own_value>"
        videofilter_profile: "<your_own_value> (source videofilter.profile.name)"
        virtual_patch_profile: "<your_own_value> (source virtual-patch.profile.name)"
        voip_profile: "<your_own_value> (source voip.profile.name)"
        waf_profile: "<your_own_value> (source waf.profile.name)"
        webcache: "enable"
        webcache_https: "disable"
        webfilter_profile: "<your_own_value> (source webfilter.profile.name)"
        webproxy_forward_server: "<your_own_value> (source web-proxy.forward-server.name web-proxy.forward-server-group.name)"
        webproxy_profile: "<your_own_value> (source web-proxy.profile.name)"
        ztna_ems_tag:
         -
            name: "default_name_106 (source firewall.address.name firewall.addrgrp.name)"
        ztna_tags_match_logic: "or"
```

## [Return Values](fortios_firewall_proxy_policy_module.md#id6)

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

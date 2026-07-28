---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_move module – Move fortimanager defined Object."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_move_module.html
fetched_at: 2026-07-28T02:15:03+00:00
---
# fortinet.fortimanager.fmgr_move module – Move fortimanager defined Object.

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_move`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_move_module.md#synopsis)
- [Parameters](fmgr_move_module.md#parameters)
- [Notes](fmgr_move_module.md#notes)
- [Examples](fmgr_move_module.md#examples)
- [Return Values](fmgr_move_module.md#return-values)

## [Synopsis](fmgr_move_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_move_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Access token of forticloud managed API users, this option is available with FortiManager later than 6.4.0. |
| **move**  dictionary / required | Reorder Two Objects. |
| **action**  string / required | Direction to indicate where to move an object entry.  **Choices:**   - `"after"` - `"before"` |
| **selector**  string / required | Selector of the move object.  **Choices:**   - `"apcfgprofile_commandlist"` - `"application_casi_profile_entries"` - `"application_list_defaultnetworkservices"` - `"application_list_entries"` - `"application_list_entries_parameters"` - `"bonjourprofile_policylist"` - `"casb_profile"` - `"casb_saasapplication"` - `"casb_useractivity"` - `"cifs_profile_filefilter_entries"` - `"dlp_dictionary_entries"` - `"dlp_filepattern_entries"` - `"dlp_profile_rule"` - `"dlp_sensor_entries"` - `"dlp_sensor_filter"` - `"dnsfilter_domainfilter_entries"` - `"dnsfilter_urlfilter_entries"` - `"emailfilter_blockallowlist_entries"` - `"emailfilter_bwl_entries"` - `"emailfilter_bword_entries"` - `"emailfilter_profile_filefilter_entries"` - `"endpointcontrol_fctems"` - `"extendercontroller_extenderprofile_cellular_smsnotification_receiver"` - `"extendercontroller_extenderprofile_lanextension_backhaul"` - `"extensioncontroller_extenderprofile_cellular_smsnotification_receiver"` - `"extensioncontroller_extenderprofile_lanextension_backhaul"` - `"filefilter_profile_rules"` - `"firewall_accessproxy"` - `"firewall_accessproxy6"` - `"firewall_accessproxyvirtualhost"` - `"firewall_carrierendpointbwl_entries"` - `"firewall_casbprofile"` - `"firewall_identitybasedroute"` - `"firewall_profileprotocoloptions_cifs_filefilter_entries"` - `"firewall_service_category"` - `"firewall_service_custom"` - `"firewall_shapingprofile_shapingentries"` - `"firewall_vip"` - `"firewall_vip6"` - `"ips_sensor_entries"` - `"ips_sensor_filter"` - `"mpskprofile_mpskgroup"` - `"mpskprofile_mpskgroup_mpskkey"` - `"pkg_authentication_rule"` - `"pkg_central_dnat"` - `"pkg_central_dnat6"` - `"pkg_firewall_acl"` - `"pkg_firewall_acl6"` - `"pkg_firewall_centralsnatmap"` - `"pkg_firewall_consolidated_policy"` - `"pkg_firewall_dospolicy"` - `"pkg_firewall_dospolicy6"` - `"pkg_firewall_explicitproxypolicy"` - `"pkg_firewall_explicitproxypolicy_identitybasedpolicy"` - `"pkg_firewall_hyperscalepolicy"` - `"pkg_firewall_hyperscalepolicy46"` - `"pkg_firewall_hyperscalepolicy6"` - `"pkg_firewall_hyperscalepolicy64"` - `"pkg_firewall_interfacepolicy"` - `"pkg_firewall_interfacepolicy6"` - `"pkg_firewall_localinpolicy"` - `"pkg_firewall_localinpolicy6"` - `"pkg_firewall_multicastpolicy"` - `"pkg_firewall_multicastpolicy6"` - `"pkg_firewall_policy"` - `"pkg_firewall_policy46"` - `"pkg_firewall_policy6"` - `"pkg_firewall_policy64"` - `"pkg_firewall_proxypolicy"` - `"pkg_firewall_securitypolicy"` - `"pkg_firewall_shapingpolicy"` - `"pkg_user_nacpolicy"` - `"pm_config_pblock_firewall_consolidated_policy"` - `"pm_config_pblock_firewall_policy"` - `"pm_config_pblock_firewall_policy6"` - `"pm_config_pblock_firewall_securitypolicy"` - `"spamfilter_bwl_entries"` - `"spamfilter_bword_entries"` - `"sshfilter_profile_filefilter_entries"` - `"sshfilter_profile_shellcommands"` - `"switchcontroller_dynamicportpolicy_policy"` - `"switchcontroller_managedswitch"` - `"system_sdnconnector_compartmentlist"` - `"system_sdnconnector_externalaccountlist"` - `"system_sdnconnector_externalip"` - `"system_sdnconnector_forwardingrule"` - `"system_sdnconnector_gcpprojectlist"` - `"system_sdnconnector_nic"` - `"system_sdnconnector_nic_ip"` - `"system_sdnconnector_ociregionlist"` - `"system_sdnconnector_route"` - `"system_sdnconnector_routetable"` - `"system_sdnconnector_routetable_route"` - `"user_deviceaccesslist_devicelist"` - `"vap_vlanname"` - `"videofilter_profile_fortiguardcategory_filters"` - `"videofilter_youtubechannelfilter_entries"` - `"vpn_ipsec_fec_mappings"` - `"vpn_ssl_settings_authenticationrule"` - `"vpnsslweb_portal_bookmarkgroup"` - `"vpnsslweb_portal_bookmarkgroup_bookmarks"` - `"vpnsslweb_portal_splitdns"` - `"wanprof_system_sdwan_members"` - `"wanprof_system_sdwan_service"` - `"wanprof_system_sdwan_service_sla"` - `"wanprof_system_sdwan_zone"` - `"wanprof_system_virtualwanlink_members"` - `"wanprof_system_virtualwanlink_service"` - `"wanprof_system_virtualwanlink_service_sla"` - `"webfilter_contentheader_entries"` - `"webfilter_profile_filefilter_entries"` - `"webfilter_urlfilter_entries"` - `"wireless_accesscontrollist_layer3ipv4rules"` - `"wireless_accesscontrollist_layer3ipv6rules"` |
| **self**  dictionary / required | The parameter for each selector. |
| **target**  string / required | Key to the target entry. |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_move_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_move_module.md#id4)

```yaml+jinja
- hosts: fortimanager01
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
    - name: Move a firewall vip object
      fmgr_move:
        move:
          selector: "firewall_vip"
          target: "ansible-test-vip_first"
          action: "before"
          self:
            adom: "root"
            vip: "ansible-test-vip_second"
```

## [Return Values](fmgr_move_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)

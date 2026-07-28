---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_endpoint_control_profile module – Configure FortiClient endpoint control profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_endpoint_control_profile_module.html
fetched_at: 2026-07-27T17:40:23+00:00
---
# fortinet.fortios.fortios_endpoint_control_profile module – Configure FortiClient endpoint control profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_endpoint_control_profile_module.md#ansible-collections-fortinet-fortios-fortios-endpoint-control-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_endpoint_control_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_endpoint_control_profile_module.md#synopsis)
- [Requirements](fortios_endpoint_control_profile_module.md#requirements)
- [Parameters](fortios_endpoint_control_profile_module.md#parameters)
- [Notes](fortios_endpoint_control_profile_module.md#notes)
- [Examples](fortios_endpoint_control_profile_module.md#examples)
- [Return Values](fortios_endpoint_control_profile_module.md#return-values)

## [Synopsis](fortios_endpoint_control_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify endpoint_control feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_endpoint_control_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_endpoint_control_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **endpoint_control_profile**  dictionary | Configure FortiClient endpoint control profiles. |
| **description**  string | Description. |
| **device_groups**  list / elements=dictionary | Device groups. |
| **name**  string | Device group object from available options. Source user.device-group.name user.device-category.name. |
| **forticlient_android_settings**  dictionary | FortiClient settings for Android platform. |
| **disable_wf_when_protected**  string | Enable/disable FortiClient web category filtering when protected by FortiGate.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_advanced_vpn**  string | Enable/disable advanced FortiClient VPN configuration.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_advanced_vpn_buffer**  string | Advanced FortiClient VPN configuration. |
| **forticlient_vpn_provisioning**  string | Enable/disable FortiClient VPN provisioning.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_vpn_settings**  list / elements=dictionary | FortiClient VPN settings. |
| **auth_method**  string | Authentication method.  Choices:   - `"psk"` - `"certificate"` |
| **name**  string | VPN name. |
| **preshared_key**  string | Pre-shared secret for PSK authentication. |
| **remote_gw**  string | IP address or FQDN of the remote VPN gateway. |
| **sslvpn_access_port**  integer | SSL VPN access port (1 - 65535). |
| **sslvpn_require_certificate**  string | Enable/disable requiring SSL VPN client certificate.  Choices:   - `"enable"` - `"disable"` |
| **type**  string | VPN type (IPsec or SSL VPN).  Choices:   - `"ipsec"` - `"ssl"` |
| **forticlient_wf**  string | Enable/disable FortiClient web filtering.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_wf_profile**  string | The FortiClient web filter profile to apply. Source webfilter.profile.name. |
| **forticlient_ios_settings**  dictionary | FortiClient settings for iOS platform. |
| **client_vpn_provisioning**  string | FortiClient VPN provisioning.  Choices:   - `"enable"` - `"disable"` |
| **client_vpn_settings**  list / elements=dictionary | FortiClient VPN settings. |
| **auth_method**  string | Authentication method.  Choices:   - `"psk"` - `"certificate"` |
| **name**  string | VPN name. |
| **preshared_key**  string | Pre-shared secret for PSK authentication. |
| **remote_gw**  string | IP address or FQDN of the remote VPN gateway. |
| **sslvpn_access_port**  integer | SSL VPN access port (1 - 65535). |
| **sslvpn_require_certificate**  string | Enable/disable requiring SSL VPN client certificate.  Choices:   - `"enable"` - `"disable"` |
| **type**  string | VPN type (IPsec or SSL VPN).  Choices:   - `"ipsec"` - `"ssl"` |
| **vpn_configuration_content**  string | Content of VPN configuration. |
| **vpn_configuration_name**  string | Name of VPN configuration. |
| **configuration_content**  string | Content of configuration profile. |
| **configuration_name**  string | Name of configuration profile. |
| **disable_wf_when_protected**  string | Enable/disable FortiClient web category filtering when protected by FortiGate.  Choices:   - `"enable"` - `"disable"` |
| **distribute_configuration_profile**  string | Enable/disable configuration profile (.mobileconfig file) distribution.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_wf**  string | Enable/disable FortiClient web filtering.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_wf_profile**  string | The FortiClient web filter profile to apply. Source webfilter.profile.name. |
| **forticlient_winmac_settings**  dictionary | FortiClient settings for Windows/Mac platform. |
| **av_realtime_protection**  string | Enable/disable FortiClient AntiVirus real-time protection.  Choices:   - `"enable"` - `"disable"` |
| **av_signature_up_to_date**  string | Enable/disable FortiClient AV signature updates.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_application_firewall**  string | Enable/disable the FortiClient application firewall.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_application_firewall_list**  string | FortiClient application firewall rule list. Source application.list.name. |
| **forticlient_av**  string | Enable/disable FortiClient AntiVirus scanning.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_ems_compliance**  string | Enable/disable FortiClient Enterprise Management Server (EMS) compliance.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_ems_compliance_action**  string | FortiClient EMS compliance action.  Choices:   - `"block"` - `"warning"` |
| **forticlient_ems_entries**  list / elements=dictionary | FortiClient EMS entries. |
| **name**  string | FortiClient EMS name. Source endpoint-control.forticlient-ems.name. |
| **forticlient_linux_ver**  string | Minimum FortiClient Linux version. |
| **forticlient_log_upload**  string | Enable/disable uploading FortiClient logs.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_log_upload_level**  string | Select the FortiClient logs to upload.  Choices:   - `"traffic"` - `"vulnerability"` - `"event"` |
| **forticlient_log_upload_server**  string | IP address or FQDN of the server to which to upload FortiClient logs. |
| **forticlient_mac_ver**  string | Minimum FortiClient Mac OS version. |
| **forticlient_minimum_software_version**  string | Enable/disable requiring clients to run FortiClient with a minimum software version number.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_operating_system**  list / elements=dictionary | FortiClient operating system. |
| **id**  integer | Operating system entry ID. |
| **os_name**  string | Customize operating system name or Mac OS format:x.x.x |
| **os_type**  string | Operating system type.  Choices:   - `"custom"` - `"mac-os"` - `"win-7"` - `"win-80"` - `"win-81"` - `"win-10"` - `"win-2000"` - `"win-home-svr"` - `"win-svr-10"` - `"win-svr-2003"` - `"win-svr-2003-r2"` - `"win-svr-2008"` - `"win-svr-2008-r2"` - `"win-svr-2012"` - `"win-svr-2012-r2"` - `"win-sto-svr-2003"` - `"win-vista"` - `"win-xp"` - `"ubuntu-linux"` - `"centos-linux"` - `"redhat-linux"` - `"fedora-linux"` |
| **forticlient_own_file**  list / elements=dictionary | Checking the path and filename of the FortiClient application. |
| **file**  string | File path and name. |
| **id**  integer | File ID. |
| **forticlient_registration_compliance_action**  string | FortiClient registration compliance action.  Choices:   - `"block"` - `"warning"` |
| **forticlient_registry_entry**  list / elements=dictionary | FortiClient registry entry. |
| **id**  integer | Registry entry ID. |
| **registry_entry**  string | Registry entry. |
| **forticlient_running_app**  list / elements=dictionary | Use FortiClient to verify if the listed applications are running on the client. |
| **app_name**  string | Application name. |
| **app_sha256_signature**  string | App”s SHA256 signature. |
| **app_sha256_signature2**  string | App”s SHA256 Signature. |
| **app_sha256_signature3**  string | App”s SHA256 Signature. |
| **app_sha256_signature4**  string | App”s SHA256 Signature. |
| **application_check_rule**  string | Application check rule.  Choices:   - `"present"` - `"absent"` |
| **id**  integer | Application ID. |
| **process_name**  string | Process name. |
| **process_name2**  string | Process name. |
| **process_name3**  string | Process name. |
| **process_name4**  string | Process name. |
| **forticlient_security_posture**  string | Enable/disable FortiClient security posture check options.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_security_posture_compliance_action**  string | FortiClient security posture compliance action.  Choices:   - `"block"` - `"warning"` |
| **forticlient_system_compliance**  string | Enable/disable enforcement of FortiClient system compliance.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_system_compliance_action**  string | Block or warn clients not compliant with FortiClient requirements.  Choices:   - `"block"` - `"warning"` |
| **forticlient_vuln_scan**  string | Enable/disable FortiClient vulnerability scanning.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_vuln_scan_compliance_action**  string | FortiClient vulnerability compliance action.  Choices:   - `"block"` - `"warning"` |
| **forticlient_vuln_scan_enforce**  string | Configure the level of the vulnerability found that causes a FortiClient vulnerability compliance action.  Choices:   - `"critical"` - `"high"` - `"medium"` - `"low"` - `"info"` |
| **forticlient_vuln_scan_enforce_grace**  integer | FortiClient vulnerability scan enforcement grace period (0 - 30 days). |
| **forticlient_vuln_scan_exempt**  string | Enable/disable compliance exemption for vulnerabilities that cannot be patched automatically.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_wf**  string | Enable/disable FortiClient web filtering.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_wf_profile**  string | The FortiClient web filter profile to apply. Source webfilter.profile.name. |
| **forticlient_win_ver**  string | Minimum FortiClient Windows version. |
| **os_av_software_installed**  string | Enable/disable checking for OS recognized AntiVirus software.  Choices:   - `"enable"` - `"disable"` |
| **sandbox_address**  string | FortiSandbox address. |
| **sandbox_analysis**  string | Enable/disable sending files to FortiSandbox for analysis.  Choices:   - `"enable"` - `"disable"` |
| **on_net_addr**  list / elements=dictionary | Addresses for on-net detection. |
| **name**  string | Address object from available options. Source firewall.address.name firewall.addrgrp.name. |
| **profile_name**  string | Profile name. |
| **replacemsg_override_group**  string | Select an endpoint control replacement message override group from available options. Source system.replacemsg-group.name. |
| **src_addr**  list / elements=dictionary | Source addresses. |
| **name**  string | Address object from available options. Source firewall.address.name firewall.addrgrp.name. |
| **user_groups**  list / elements=dictionary | User groups. |
| **name**  string | User group name. Source user.group.name. |
| **users**  list / elements=dictionary | Users. |
| **name**  string | User name. Source user.local.name. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_endpoint_control_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_endpoint_control_profile_module.md#id5)

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
  - name: Configure FortiClient endpoint control profiles.
    fortios_endpoint_control_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      endpoint_control_profile:
        description: "<your_own_value>"
        device_groups:
         -
            name: "default_name_5 (source user.device-group.name user.device-category.name)"
        forticlient_android_settings:
            disable_wf_when_protected: "enable"
            forticlient_advanced_vpn: "enable"
            forticlient_advanced_vpn_buffer: "<your_own_value>"
            forticlient_vpn_provisioning: "enable"
            forticlient_vpn_settings:
             -
                auth_method: "psk"
                name: "default_name_13"
                preshared_key: "<your_own_value>"
                remote_gw: "<your_own_value>"
                sslvpn_access_port: "32767"
                sslvpn_require_certificate: "enable"
                type: "ipsec"
            forticlient_wf: "enable"
            forticlient_wf_profile: "<your_own_value> (source webfilter.profile.name)"
        forticlient_ios_settings:
            client_vpn_provisioning: "enable"
            client_vpn_settings:
             -
                auth_method: "psk"
                name: "default_name_25"
                preshared_key: "<your_own_value>"
                remote_gw: "<your_own_value>"
                sslvpn_access_port: "32767"
                sslvpn_require_certificate: "enable"
                type: "ipsec"
                vpn_configuration_content: "<your_own_value>"
                vpn_configuration_name: "<your_own_value>"
            configuration_content: "<your_own_value>"
            configuration_name: "<your_own_value>"
            disable_wf_when_protected: "enable"
            distribute_configuration_profile: "enable"
            forticlient_wf: "enable"
            forticlient_wf_profile: "<your_own_value> (source webfilter.profile.name)"
        forticlient_winmac_settings:
            av_realtime_protection: "enable"
            av_signature_up_to_date: "enable"
            forticlient_application_firewall: "enable"
            forticlient_application_firewall_list: "<your_own_value> (source application.list.name)"
            forticlient_av: "enable"
            forticlient_ems_compliance: "enable"
            forticlient_ems_compliance_action: "block"
            forticlient_ems_entries:
             -
                name: "default_name_48 (source endpoint-control.forticlient-ems.name)"
            forticlient_linux_ver: "<your_own_value>"
            forticlient_log_upload: "enable"
            forticlient_log_upload_level: "traffic"
            forticlient_log_upload_server: "<your_own_value>"
            forticlient_mac_ver: "<your_own_value>"
            forticlient_minimum_software_version: "enable"
            forticlient_operating_system:
             -
                id:  "56"
                os_name: "<your_own_value>"
                os_type: "custom"
            forticlient_own_file:
             -
                file: "<your_own_value>"
                id:  "61"
            forticlient_registration_compliance_action: "block"
            forticlient_registry_entry:
             -
                id:  "64"
                registry_entry: "<your_own_value>"
            forticlient_running_app:
             -
                app_name: "<your_own_value>"
                app_sha256_signature: "<your_own_value>"
                app_sha256_signature2: "<your_own_value>"
                app_sha256_signature3: "<your_own_value>"
                app_sha256_signature4: "<your_own_value>"
                application_check_rule: "present"
                id:  "73"
                process_name: "<your_own_value>"
                process_name2: "<your_own_value>"
                process_name3: "<your_own_value>"
                process_name4: "<your_own_value>"
            forticlient_security_posture: "enable"
            forticlient_security_posture_compliance_action: "block"
            forticlient_system_compliance: "enable"
            forticlient_system_compliance_action: "block"
            forticlient_vuln_scan: "enable"
            forticlient_vuln_scan_compliance_action: "block"
            forticlient_vuln_scan_enforce: "critical"
            forticlient_vuln_scan_enforce_grace: "15"
            forticlient_vuln_scan_exempt: "enable"
            forticlient_wf: "enable"
            forticlient_wf_profile: "<your_own_value> (source webfilter.profile.name)"
            forticlient_win_ver: "<your_own_value>"
            os_av_software_installed: "enable"
            sandbox_address: "<your_own_value>"
            sandbox_analysis: "enable"
        on_net_addr:
         -
            name: "default_name_94 (source firewall.address.name firewall.addrgrp.name)"
        profile_name: "<your_own_value>"
        replacemsg_override_group: "<your_own_value> (source system.replacemsg-group.name)"
        src_addr:
         -
            name: "default_name_98 (source firewall.address.name firewall.addrgrp.name)"
        user_groups:
         -
            name: "default_name_100 (source user.group.name)"
        users:
         -
            name: "default_name_102 (source user.local.name)"
```

## [Return Values](fortios_endpoint_control_profile_module.md#id6)

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

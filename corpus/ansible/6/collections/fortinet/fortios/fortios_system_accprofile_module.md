---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_accprofile module – Configure access profiles for system administrators in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_accprofile_module.html
fetched_at: 2026-07-27T17:44:03+00:00
---
# fortinet.fortios.fortios_system_accprofile module – Configure access profiles for system administrators in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_accprofile_module.md#ansible-collections-fortinet-fortios-fortios-system-accprofile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_accprofile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_accprofile_module.md#synopsis)
- [Requirements](fortios_system_accprofile_module.md#requirements)
- [Parameters](fortios_system_accprofile_module.md#parameters)
- [Notes](fortios_system_accprofile_module.md#notes)
- [Examples](fortios_system_accprofile_module.md#examples)
- [Return Values](fortios_system_accprofile_module.md#return-values)

## [Synopsis](fortios_system_accprofile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and accprofile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_accprofile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_accprofile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **system_accprofile**  dictionary | Configure access profiles for system administrators. |
| **admintimeout**  integer | Administrator timeout for this access profile (0 - 480 min). |
| **admintimeout_override**  string | Enable/disable overriding the global administrator idle timeout.  Choices:   - `"enable"` - `"disable"` |
| **authgrp**  string | Administrator access to Users and Devices.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **comments**  string | Comment. |
| **ftviewgrp**  string | FortiView.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **fwgrp**  string | Administrator access to the Firewall configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` - `"custom"` |
| **fwgrp_permission**  dictionary | Custom firewall permission. |
| **address**  string | Address Configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **others**  string | Other Firewall Configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **policy**  string | Policy Configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **schedule**  string | Schedule Configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **service**  string | Service Configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **loggrp**  string | Administrator access to Logging and Reporting including viewing log messages.  Choices:   - `"none"` - `"read"` - `"read-write"` - `"custom"` |
| **loggrp_permission**  dictionary | Custom Log & Report permission. |
| **config**  string | Log & Report configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **data_access**  string | Log & Report Data Access.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **report_access**  string | Log & Report Report Access.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **threat_weight**  string | Log & Report Threat Weight.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **name**  string / required | Profile name. |
| **netgrp**  string | Network Configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` - `"custom"` |
| **netgrp_permission**  dictionary | Custom network permission. |
| **cfg**  string | Network Configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **packet_capture**  string | Packet Capture Configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **route_cfg**  string | Router Configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **scope**  string | Scope of admin access: global or specific VDOM(s).  Choices:   - `"vdom"` - `"global"` |
| **secfabgrp**  string | Security Fabric.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **sysgrp**  string | System Configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` - `"custom"` |
| **sysgrp_permission**  dictionary | Custom system permission. |
| **admin**  string | Administrator Users.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **cfg**  string | System Configuration.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **mnt**  string | Maintenance.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **upd**  string | FortiGuard Updates.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **system_diagnostics**  string | Enable/disable permission to run system diagnostic commands.  Choices:   - `"enable"` - `"disable"` |
| **system_execute_ssh**  string | Enable/disable permission to execute SSH commands.  Choices:   - `"enable"` - `"disable"` |
| **system_execute_telnet**  string | Enable/disable permission to execute TELNET commands.  Choices:   - `"enable"` - `"disable"` |
| **utmgrp**  string | Administrator access to Security Profiles.  Choices:   - `"none"` - `"read"` - `"read-write"` - `"custom"` |
| **utmgrp_permission**  dictionary | Custom Security Profile permissions. |
| **antivirus**  string | Antivirus profiles and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **application_control**  string | Application Control profiles and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **data_loss_prevention**  string | DLP profiles and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **dnsfilter**  string | DNS Filter profiles and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **emailfilter**  string | Email Filter and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **endpoint_control**  string | FortiClient Profiles.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **file_filter**  string | File-filter profiles and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **icap**  string | ICAP profiles and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **ips**  string | IPS profiles and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **mmsgtp**  string | UTM permission.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **spamfilter**  string | AntiSpam filter and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **videofilter**  string | Video filter profiles and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **voip**  string | VoIP profiles and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **waf**  string | Web Application Firewall profiles and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **webfilter**  string | Web Filter profiles and settings.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **vpngrp**  string | Administrator access to IPsec, SSL, PPTP, and L2TP VPN.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **wanoptgrp**  string | Administrator access to WAN Opt & Cache.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **wifi**  string | Administrator access to the WiFi controller and Switch controller.  Choices:   - `"none"` - `"read"` - `"read-write"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_accprofile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_accprofile_module.md#id5)

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
  - name: Configure access profiles for system administrators.
    fortios_system_accprofile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_accprofile:
        admintimeout: "10"
        admintimeout_override: "enable"
        authgrp: "none"
        comments: "<your_own_value>"
        ftviewgrp: "none"
        fwgrp: "none"
        fwgrp_permission:
            address: "none"
            others: "none"
            policy: "none"
            schedule: "none"
            service: "none"
        loggrp: "none"
        loggrp_permission:
            config: "none"
            data_access: "none"
            report_access: "none"
            threat_weight: "none"
        name: "default_name_21"
        netgrp: "none"
        netgrp_permission:
            cfg: "none"
            packet_capture: "none"
            route_cfg: "none"
        scope: "vdom"
        secfabgrp: "none"
        sysgrp: "none"
        sysgrp_permission:
            admin: "none"
            cfg: "none"
            mnt: "none"
            upd: "none"
        system_diagnostics: "enable"
        system_execute_ssh: "enable"
        system_execute_telnet: "enable"
        utmgrp: "none"
        utmgrp_permission:
            antivirus: "none"
            application_control: "none"
            data_loss_prevention: "none"
            dnsfilter: "none"
            emailfilter: "none"
            endpoint_control: "none"
            file_filter: "none"
            icap: "none"
            ips: "none"
            mmsgtp: "none"
            spamfilter: "none"
            videofilter: "none"
            voip: "none"
            waf: "none"
            webfilter: "none"
        vpngrp: "none"
        wanoptgrp: "none"
        wifi: "none"
```

## [Return Values](fortios_system_accprofile_module.md#id6)

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

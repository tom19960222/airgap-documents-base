---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_csf module – Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_csf_module.html
fetched_at: 2026-07-28T02:28:05+00:00
---
# fortinet.fortios.fortios_system_csf module – Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_csf_module.md#ansible-collections-fortinet-fortios-fortios-system-csf-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_csf`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_csf_module.md#synopsis)
- [Requirements](fortios_system_csf_module.md#requirements)
- [Parameters](fortios_system_csf_module.md#parameters)
- [Notes](fortios_system_csf_module.md#notes)
- [Examples](fortios_system_csf_module.md#examples)
- [Return Values](fortios_system_csf_module.md#return-values)

## [Synopsis](fortios_system_csf_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and csf category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_csf_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_csf_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_csf**  dictionary | Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate. |
| **accept_auth_by_cert**  string | Accept connections with unknown certificates and ask admin for approval.  **Choices:**   - `"disable"` - `"enable"` |
| **authorization_request_type**  string | Authorization request type.  **Choices:**   - `"serial"` - `"certificate"` |
| **certificate**  string | Certificate. Source certificate.local.name. |
| **configuration_sync**  string | Configuration sync mode.  **Choices:**   - `"default"` - `"local"` |
| **downstream_access**  string | Enable/disable downstream device access to this device”s configuration and data.  **Choices:**   - `"enable"` - `"disable"` |
| **downstream_accprofile**  string | Default access profile for requests from downstream devices. Source system.accprofile.name. |
| **fabric_connector**  list / elements=dictionary | Fabric connector configuration. |
| **accprofile**  string | Override access profile. Source system.accprofile.name. |
| **configuration_write_access**  string | Enable/disable downstream device write access to configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **serial**  string / required | Serial. |
| **vdom**  list / elements=dictionary | Virtual domains that the connector has access to. If none are set, the connector will only have access to the VDOM that it joins the Security Fabric through. |
| **name**  string / required | Virtual domain name. Source system.vdom.name. |
| **fabric_device**  list / elements=dictionary | Fabric device configuration. |
| **access_token**  string | Device access token. |
| **device_ip**  string | Device IP. |
| **device_type**  string | Device type.  **Choices:**   - `"fortimail"` |
| **https_port**  integer | HTTPS port for fabric device. |
| **login**  string | Device login name. |
| **name**  string / required | Device name. |
| **password**  string | Device login password. |
| **fabric_object_unification**  string | Fabric CMDB Object Unification.  **Choices:**   - `"default"` - `"local"` |
| **fabric_workers**  integer | Number of worker processes for Security Fabric daemon. |
| **file_mgmt**  string | Enable/disable Security Fabric daemon file management.  **Choices:**   - `"enable"` - `"disable"` |
| **file_quota**  integer | Maximum amount of memory that can be used by the daemon files (in bytes). |
| **file_quota_warning**  integer | Warn when the set percentage of quota has been used. |
| **fixed_key**  string | Auto-generated fixed key used when this device is the root. (Will automatically be generated if not set.) |
| **forticloud_account_enforcement**  string | Fabric FortiCloud account unification.  **Choices:**   - `"enable"` - `"disable"` |
| **group_name**  string | Security Fabric group name. All FortiGates in a Security Fabric must have the same group name. |
| **group_password**  string | Security Fabric group password. All FortiGates in a Security Fabric must have the same group password. |
| **log_unification**  string | Enable/disable broadcast of discovery messages for log unification.  **Choices:**   - `"disable"` - `"enable"` |
| **management_ip**  string | Management IP address of this FortiGate. Used to log into this FortiGate from another FortiGate in the Security Fabric. |
| **management_port**  integer | Overriding port for management connection (Overrides admin port). |
| **saml_configuration_sync**  string | SAML setting configuration synchronization.  **Choices:**   - `"default"` - `"local"` |
| **status**  string | Enable/disable Security Fabric.  **Choices:**   - `"enable"` - `"disable"` |
| **trusted_list**  list / elements=dictionary | Pre-authorized and blocked security fabric nodes. |
| **action**  string | Security fabric authorization action.  **Choices:**   - `"accept"` - `"deny"` |
| **authorization_type**  string | Authorization type.  **Choices:**   - `"serial"` - `"certificate"` |
| **certificate**  string | Certificate. |
| **downstream_authorization**  string | Trust authorizations by this node”s administrator.  **Choices:**   - `"enable"` - `"disable"` |
| **ha_members**  list / elements=string | HA members. |
| **index**  integer | Index of the downstream in tree. |
| **name**  string / required | Name. |
| **serial**  string | Serial. |
| **upstream**  string | IP/FQDN of the FortiGate upstream from this FortiGate in the Security Fabric. |
| **upstream_ip**  string | IP address of the FortiGate upstream from this FortiGate in the Security Fabric. |
| **upstream_port**  integer | The port number to use to communicate with the FortiGate upstream from this FortiGate in the Security Fabric . |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_csf_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_csf_module.md#id5)

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
  - name: Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
    fortios_system_csf:
      vdom:  "{{ vdom }}"
      system_csf:
        accept_auth_by_cert: "disable"
        authorization_request_type: "serial"
        certificate: "<your_own_value> (source certificate.local.name)"
        configuration_sync: "default"
        downstream_access: "enable"
        downstream_accprofile: "<your_own_value> (source system.accprofile.name)"
        fabric_connector:
         -
            accprofile: "<your_own_value> (source system.accprofile.name)"
            configuration_write_access: "enable"
            serial: "<your_own_value>"
            vdom:
             -
                name: "default_name_14 (source system.vdom.name)"
        fabric_device:
         -
            access_token: "<your_own_value>"
            device_ip: "<your_own_value>"
            device_type: "fortimail"
            https_port: "443"
            login: "<your_own_value>"
            name: "default_name_21"
            password: "<your_own_value>"
        fabric_object_unification: "default"
        fabric_workers: "2"
        file_mgmt: "enable"
        file_quota: "0"
        file_quota_warning: "90"
        fixed_key: "<your_own_value>"
        forticloud_account_enforcement: "enable"
        group_name: "<your_own_value>"
        group_password: "<your_own_value>"
        log_unification: "disable"
        management_ip: "<your_own_value>"
        management_port: "32767"
        saml_configuration_sync: "default"
        status: "enable"
        trusted_list:
         -
            action: "accept"
            authorization_type: "serial"
            certificate: "<your_own_value>"
            downstream_authorization: "enable"
            ha_members: "<your_own_value>"
            index: "0"
            name: "default_name_44"
            serial: "<your_own_value>"
        upstream: "<your_own_value>"
        upstream_ip: "<your_own_value>"
        upstream_port: "8013"
```

## [Return Values](fortios_system_csf_module.md#id6)

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

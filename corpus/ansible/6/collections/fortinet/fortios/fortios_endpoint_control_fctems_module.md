---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_endpoint_control_fctems module – Configure FortiClient Enterprise Management Server (EMS) entries in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_endpoint_control_fctems_module.html
fetched_at: 2026-07-27T17:40:21+00:00
---
# fortinet.fortios.fortios_endpoint_control_fctems module – Configure FortiClient Enterprise Management Server (EMS) entries in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_endpoint_control_fctems_module.md#ansible-collections-fortinet-fortios-fortios-endpoint-control-fctems-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_endpoint_control_fctems`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_endpoint_control_fctems_module.md#synopsis)
- [Requirements](fortios_endpoint_control_fctems_module.md#requirements)
- [Parameters](fortios_endpoint_control_fctems_module.md#parameters)
- [Notes](fortios_endpoint_control_fctems_module.md#notes)
- [Examples](fortios_endpoint_control_fctems_module.md#examples)
- [Return Values](fortios_endpoint_control_fctems_module.md#return-values)

## [Synopsis](fortios_endpoint_control_fctems_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify endpoint_control feature and fctems category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_endpoint_control_fctems_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_endpoint_control_fctems_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **endpoint_control_fctems**  dictionary | Configure FortiClient Enterprise Management Server (EMS) entries. |
| **admin_password**  string | FortiClient EMS admin password. |
| **admin_username**  string | FortiClient EMS admin username. |
| **call_timeout**  integer | FortiClient EMS call timeout in seconds (1 - 180 seconds). |
| **capabilities**  list / elements=string | List of EMS capabilities.  Choices:   - `"fabric-auth"` - `"silent-approval"` - `"websocket"` - `"websocket-malware"` - `"push-ca-certs"` - `"common-tags-api"` - `"tenant-id"` |
| **certificate**  string | FortiClient EMS certificate. Source certificate.remote.name. |
| **cloud_server_type**  string | Cloud server type.  Choices:   - `"production"` - `"alpha"` - `"beta"` |
| **dirty_reason**  string | Dirty Reason for FortiClient EMS.  Choices:   - `"none"` - `"mismatched-ems-sn"` |
| **ems_id**  integer | EMS ID in order (1 - 5) |
| **fortinetone_cloud_authentication**  string | Enable/disable authentication of FortiClient EMS Cloud through FortiCloud account.  Choices:   - `"enable"` - `"disable"` |
| **https_port**  integer | FortiClient EMS HTTPS access port number. (1 - 65535). |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **name**  string | FortiClient Enterprise Management Server (EMS) name. |
| **out_of_sync_threshold**  integer | Outdated resource threshold in seconds (10 - 3600). |
| **preserve_ssl_session**  string | Enable/disable preservation of EMS SSL session connection. Warning, most users should not touch this setting.  Choices:   - `"enable"` - `"disable"` |
| **pull_avatars**  string | Enable/disable pulling avatars from EMS.  Choices:   - `"enable"` - `"disable"` |
| **pull_malware_hash**  string | Enable/disable pulling FortiClient malware hash from EMS.  Choices:   - `"enable"` - `"disable"` |
| **pull_sysinfo**  string | Enable/disable pulling SysInfo from EMS.  Choices:   - `"enable"` - `"disable"` |
| **pull_tags**  string | Enable/disable pulling FortiClient user tags from EMS.  Choices:   - `"enable"` - `"disable"` |
| **pull_vulnerabilities**  string | Enable/disable pulling vulnerabilities from EMS.  Choices:   - `"enable"` - `"disable"` |
| **serial_number**  string | EMS Serial Number. |
| **server**  string | FortiClient EMS FQDN or IPv4 address. |
| **source_ip**  string | REST API call source IP. |
| **status**  string | Enable or disable this EMS configuration.  Choices:   - `"enable"` - `"disable"` |
| **status_check_interval**  integer | FortiClient EMS call timeout in seconds (1 - 120 seconds). |
| **tenant_id**  string | EMS Tenant ID. |
| **websocket_override**  string | Enable/disable override behavior for how this FortiGate unit connects to EMS using a WebSocket connection.  Choices:   - `"disable"` - `"enable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_endpoint_control_fctems_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_endpoint_control_fctems_module.md#id5)

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
  - name: Configure FortiClient Enterprise Management Server (EMS) entries.
    fortios_endpoint_control_fctems:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      endpoint_control_fctems:
        admin_password: "<your_own_value>"
        admin_username: "<your_own_value>"
        call_timeout: "30"
        capabilities: "fabric-auth"
        certificate: "<your_own_value> (source certificate.remote.name)"
        cloud_server_type: "production"
        dirty_reason: "none"
        ems_id: "0"
        fortinetone_cloud_authentication: "enable"
        https_port: "443"
        interface: "<your_own_value> (source system.interface.name)"
        interface_select_method: "auto"
        name: "default_name_15"
        out_of_sync_threshold: "180"
        preserve_ssl_session: "enable"
        pull_avatars: "enable"
        pull_malware_hash: "enable"
        pull_sysinfo: "enable"
        pull_tags: "enable"
        pull_vulnerabilities: "enable"
        serial_number: "<your_own_value>"
        server: "192.168.100.40"
        source_ip: "84.230.14.43"
        status: "enable"
        status_check_interval: "90"
        tenant_id: "<your_own_value>"
        websocket_override: "disable"
```

## [Return Values](fortios_endpoint_control_fctems_module.md#id6)

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

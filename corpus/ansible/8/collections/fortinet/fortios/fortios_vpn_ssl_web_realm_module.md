---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_vpn_ssl_web_realm module – Realm in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_vpn_ssl_web_realm_module.html
fetched_at: 2026-07-28T02:30:30+00:00
---
# fortinet.fortios.fortios_vpn_ssl_web_realm module – Realm in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_vpn_ssl_web_realm_module.md#ansible-collections-fortinet-fortios-fortios-vpn-ssl-web-realm-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_vpn_ssl_web_realm`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_vpn_ssl_web_realm_module.md#synopsis)
- [Requirements](fortios_vpn_ssl_web_realm_module.md#requirements)
- [Parameters](fortios_vpn_ssl_web_realm_module.md#parameters)
- [Notes](fortios_vpn_ssl_web_realm_module.md#notes)
- [Examples](fortios_vpn_ssl_web_realm_module.md#examples)
- [Return Values](fortios_vpn_ssl_web_realm_module.md#return-values)

## [Synopsis](fortios_vpn_ssl_web_realm_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify vpn_ssl_web feature and realm category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_vpn_ssl_web_realm_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_vpn_ssl_web_realm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **vpn_ssl_web_realm**  dictionary | Realm. |
| **login_page**  string | Replacement HTML for SSL-VPN login page. |
| **max_concurrent_user**  integer | Maximum concurrent users (0 - 65535, 0 means unlimited). |
| **nas_ip**  string | IP address used as a NAS-IP to communicate with the RADIUS server. |
| **radius_port**  integer | RADIUS service port number (0 - 65535, 0 means user.radius.radius-port). |
| **radius_server**  string | RADIUS server associated with realm. Source user.radius.name. |
| **url_path**  string / required | URL path to access SSL-VPN login page. |
| **virtual_host**  string | Virtual host name for realm. |
| **virtual_host_only**  string | Enable/disable enforcement of virtual host method for SSL-VPN client access.  **Choices:**   - `"enable"` - `"disable"` |
| **virtual_host_server_cert**  string | Name of the server certificate to used for this realm. Source vpn.certificate.local.name. |

## [Notes](fortios_vpn_ssl_web_realm_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_vpn_ssl_web_realm_module.md#id5)

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
  - name: Realm.
    fortios_vpn_ssl_web_realm:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      vpn_ssl_web_realm:
        login_page: "<your_own_value>"
        max_concurrent_user: "0"
        nas_ip: "<your_own_value>"
        radius_port: "0"
        radius_server: "<your_own_value> (source user.radius.name)"
        url_path: "<your_own_value>"
        virtual_host: "myhostname"
        virtual_host_only: "enable"
        virtual_host_server_cert: "myhostname (source vpn.certificate.local.name)"
```

## [Return Values](fortios_vpn_ssl_web_realm_module.md#id6)

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

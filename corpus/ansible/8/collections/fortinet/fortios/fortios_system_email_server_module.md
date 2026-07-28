---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_email_server module – Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_email_server_module.html
fetched_at: 2026-07-28T02:28:14+00:00
---
# fortinet.fortios.fortios_system_email_server module – Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_email_server_module.md#ansible-collections-fortinet-fortios-fortios-system-email-server-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_email_server`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_email_server_module.md#synopsis)
- [Requirements](fortios_system_email_server_module.md#requirements)
- [Parameters](fortios_system_email_server_module.md#parameters)
- [Notes](fortios_system_email_server_module.md#notes)
- [Examples](fortios_system_email_server_module.md#examples)
- [Return Values](fortios_system_email_server_module.md#return-values)

## [Synopsis](fortios_system_email_server_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and email_server category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_email_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_email_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_email_server**  dictionary | Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features. |
| **authenticate**  string | Enable/disable authentication.  **Choices:**   - `"enable"` - `"disable"` |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **password**  string | SMTP server user password for authentication. |
| **port**  integer | SMTP server port. |
| **reply_to**  string | Reply-To email address. |
| **security**  string | Connection security used by the email server.  **Choices:**   - `"none"` - `"starttls"` - `"smtps"` |
| **server**  string | SMTP server IP address or hostname. |
| **source_ip**  string | SMTP server IPv4 source IP. |
| **source_ip6**  string | SMTP server IPv6 source IP. |
| **ssl_min_proto_version**  string | Minimum supported protocol version for SSL/TLS connections .  **Choices:**   - `"default"` - `"SSLv3"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"TLSv1-3"` |
| **type**  string | Use FortiGuard Message service or custom email server.  **Choices:**   - `"custom"` |
| **username**  string | SMTP server user name for authentication. |
| **validate_server**  string | Enable/disable validation of server certificate.  **Choices:**   - `"enable"` - `"disable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_email_server_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_email_server_module.md#id5)

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
  - name: Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication
     features.
    fortios_system_email_server:
      vdom:  "{{ vdom }}"
      system_email_server:
        authenticate: "enable"
        interface: "<your_own_value> (source system.interface.name)"
        interface_select_method: "auto"
        password: "<your_own_value>"
        port: "25"
        reply_to: "<your_own_value>"
        security: "none"
        server: "192.168.100.40"
        source_ip: "84.230.14.43"
        source_ip6: "<your_own_value>"
        ssl_min_proto_version: "default"
        type: "custom"
        username: "<your_own_value>"
        validate_server: "enable"
```

## [Return Values](fortios_system_email_server_module.md#id6)

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

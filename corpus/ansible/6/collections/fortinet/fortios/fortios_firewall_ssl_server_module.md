---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_ssl_server module – Configure SSL servers in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_ssl_server_module.html
fetched_at: 2026-07-27T17:41:37+00:00
---
# fortinet.fortios.fortios_firewall_ssl_server module – Configure SSL servers in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_ssl_server_module.md#ansible-collections-fortinet-fortios-fortios-firewall-ssl-server-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_ssl_server`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_ssl_server_module.md#synopsis)
- [Requirements](fortios_firewall_ssl_server_module.md#requirements)
- [Parameters](fortios_firewall_ssl_server_module.md#parameters)
- [Notes](fortios_firewall_ssl_server_module.md#notes)
- [Examples](fortios_firewall_ssl_server_module.md#examples)
- [Return Values](fortios_firewall_ssl_server_module.md#return-values)

## [Synopsis](fortios_firewall_ssl_server_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and ssl_server category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_ssl_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_ssl_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_ssl_server**  dictionary | Configure SSL servers. |
| **add_header_x_forwarded_proto**  string | Enable/disable adding an X-Forwarded-Proto header to forwarded requests.  Choices:   - `"enable"` - `"disable"` |
| **ip**  string | IPv4 address of the SSL server. |
| **mapped_port**  integer | Mapped server service port (1 - 65535). |
| **name**  string / required | Server name. |
| **port**  integer | Server service port (1 - 65535). |
| **ssl_algorithm**  string | Relative strength of encryption algorithms accepted in negotiation.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **ssl_cert**  string | Name of certificate for SSL connections to this server . Source vpn.certificate.local.name. |
| **ssl_client_renegotiation**  string | Allow or block client renegotiation by server.  Choices:   - `"allow"` - `"deny"` - `"secure"` |
| **ssl_dh_bits**  string | Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation .  Choices:   - `"768"` - `"1024"` - `"1536"` - `"2048"` |
| **ssl_max_version**  string | Highest SSL/TLS version to negotiate.  Choices:   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_min_version**  string | Lowest SSL/TLS version to negotiate.  Choices:   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_mode**  string | SSL/TLS mode for encryption and decryption of traffic.  Choices:   - `"half"` - `"full"` |
| **ssl_send_empty_frags**  string | Enable/disable sending empty fragments to avoid attack on CBC IV.  Choices:   - `"enable"` - `"disable"` |
| **url_rewrite**  string | Enable/disable rewriting the URL.  Choices:   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_ssl_server_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_ssl_server_module.md#id5)

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
  - name: Configure SSL servers.
    fortios_firewall_ssl_server:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_ssl_server:
        add_header_x_forwarded_proto: "enable"
        ip: "<your_own_value>"
        mapped_port: "80"
        name: "default_name_6"
        port: "443"
        ssl_algorithm: "high"
        ssl_cert: "<your_own_value> (source vpn.certificate.local.name)"
        ssl_client_renegotiation: "allow"
        ssl_dh_bits: "768"
        ssl_max_version: "tls-1.0"
        ssl_min_version: "tls-1.0"
        ssl_mode: "half"
        ssl_send_empty_frags: "enable"
        url_rewrite: "enable"
```

## [Return Values](fortios_firewall_ssl_server_module.md#id6)

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

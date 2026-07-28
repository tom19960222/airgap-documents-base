---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_user_exchange module – Configure MS Exchange server entries in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_user_exchange_module.html
fetched_at: 2026-07-27T17:45:55+00:00
---
# fortinet.fortios.fortios_user_exchange module – Configure MS Exchange server entries in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_user_exchange_module.md#ansible-collections-fortinet-fortios-fortios-user-exchange-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_user_exchange`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_user_exchange_module.md#synopsis)
- [Requirements](fortios_user_exchange_module.md#requirements)
- [Parameters](fortios_user_exchange_module.md#parameters)
- [Notes](fortios_user_exchange_module.md#notes)
- [Examples](fortios_user_exchange_module.md#examples)
- [Return Values](fortios_user_exchange_module.md#return-values)

## [Synopsis](fortios_user_exchange_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify user feature and exchange category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_user_exchange_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_user_exchange_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **user_exchange**  dictionary | Configure MS Exchange server entries. |
| **auth_level**  string | Authentication security level used for the RPC protocol layer.  Choices:   - `"connect"` - `"call"` - `"packet"` - `"integrity"` - `"privacy"` |
| **auth_type**  string | Authentication security type used for the RPC protocol layer.  Choices:   - `"spnego"` - `"ntlm"` - `"kerberos"` |
| **auto_discover_kdc**  string | Enable/disable automatic discovery of KDC IP addresses.  Choices:   - `"enable"` - `"disable"` |
| **connect_protocol**  string | Connection protocol used to connect to MS Exchange service.  Choices:   - `"rpc-over-tcp"` - `"rpc-over-http"` - `"rpc-over-https"` |
| **domain_name**  string | MS Exchange server fully qualified domain name. |
| **http_auth_type**  string | Authentication security type used for the HTTP transport.  Choices:   - `"basic"` - `"ntlm"` |
| **ip**  string | Server IPv4 address. |
| **kdc_ip**  list / elements=dictionary | KDC IPv4 addresses for Kerberos authentication. |
| **ipv4**  string | KDC IPv4 addresses for Kerberos authentication. |
| **name**  string / required | MS Exchange server entry name. |
| **password**  string | Password for the specified username. |
| **server_name**  string | MS Exchange server hostname. |
| **ssl_min_proto_version**  string | Minimum SSL/TLS protocol version for HTTPS transport .  Choices:   - `"default"` - `"SSLv3"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` |
| **username**  string | User name used to sign in to the server. Must have proper permissions for service. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_user_exchange_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_user_exchange_module.md#id5)

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
  - name: Configure MS Exchange server entries.
    fortios_user_exchange:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_exchange:
        auth_level: "connect"
        auth_type: "spnego"
        auto_discover_kdc: "enable"
        connect_protocol: "rpc-over-tcp"
        domain_name: "<your_own_value>"
        http_auth_type: "basic"
        ip: "<your_own_value>"
        kdc_ip:
         -
            ipv4: "<your_own_value>"
        name: "default_name_12"
        password: "<your_own_value>"
        server_name: "<your_own_value>"
        ssl_min_proto_version: "default"
        username: "<your_own_value>"
```

## [Return Values](fortios_user_exchange_module.md#id6)

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

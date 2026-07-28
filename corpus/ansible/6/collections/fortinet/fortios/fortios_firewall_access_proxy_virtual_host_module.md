---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_access_proxy_virtual_host module – Configure Access Proxy virtual hosts in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_access_proxy_virtual_host_module.html
fetched_at: 2026-07-27T17:40:38+00:00
---
# fortinet.fortios.fortios_firewall_access_proxy_virtual_host module – Configure Access Proxy virtual hosts in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_access_proxy_virtual_host_module.md#ansible-collections-fortinet-fortios-fortios-firewall-access-proxy-virtual-host-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_access_proxy_virtual_host`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_access_proxy_virtual_host_module.md#synopsis)
- [Requirements](fortios_firewall_access_proxy_virtual_host_module.md#requirements)
- [Parameters](fortios_firewall_access_proxy_virtual_host_module.md#parameters)
- [Notes](fortios_firewall_access_proxy_virtual_host_module.md#notes)
- [Examples](fortios_firewall_access_proxy_virtual_host_module.md#examples)
- [Return Values](fortios_firewall_access_proxy_virtual_host_module.md#return-values)

## [Synopsis](fortios_firewall_access_proxy_virtual_host_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and access_proxy_virtual_host category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_access_proxy_virtual_host_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_access_proxy_virtual_host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_access_proxy_virtual_host**  dictionary | Configure Access Proxy virtual hosts. |
| **host**  string | The host name. |
| **host_type**  string | Type of host pattern.  Choices:   - `"sub-string"` - `"wildcard"` |
| **name**  string / required | Virtual host name. |
| **replacemsg_group**  string | Access-proxy-virtual-host replacement message override group. Source system.replacemsg-group.name. |
| **ssl_certificate**  string | SSL certificate for this host. Source vpn.certificate.local.name. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_access_proxy_virtual_host_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_access_proxy_virtual_host_module.md#id5)

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
  - name: Configure Access Proxy virtual hosts.
    fortios_firewall_access_proxy_virtual_host:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_access_proxy_virtual_host:
        host: "myhostname"
        host_type: "sub-string"
        name: "default_name_5"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        ssl_certificate: "<your_own_value> (source vpn.certificate.local.name)"
```

## [Return Values](fortios_firewall_access_proxy_virtual_host_module.md#id6)

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

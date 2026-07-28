---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_json_generic module – Config Fortinet’s FortiOS and FortiGate with json generic method."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_json_generic_module.html
fetched_at: 2026-07-27T17:42:06+00:00
---
# fortinet.fortios.fortios_json_generic module – Config Fortinet’s FortiOS and FortiGate with json generic method.

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
> see [Requirements](fortios_json_generic_module.md#ansible-collections-fortinet-fortios-fortios-json-generic-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_json_generic`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_json_generic_module.md#synopsis)
- [Requirements](fortios_json_generic_module.md#requirements)
- [Parameters](fortios_json_generic_module.md#parameters)
- [Notes](fortios_json_generic_module.md#notes)
- [Examples](fortios_json_generic_module.md#examples)
- [Return Values](fortios_json_generic_module.md#return-values)

## [Synopsis](fortios_json_generic_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify json feature and generic category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.4

## [Requirements](fortios_json_generic_module.md#id2)

The below requirements are needed on the host that executes this module.

- fortiosapi>=0.9.8

## [Parameters](fortios_json_generic_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **json_generic**  dictionary | json generic |
| **dictbody**  dictionary | Body with YAML list of key/value format |
| **jsonbody**  string | Body with JSON string format, will always give priority to jsonbody |
| **method**  string / required | HTTP methods  Choices:   - `"GET"` - `"PUT"` - `"POST"` - `"DELETE"` |
| **path**  string / required | URL path, e.g./api/v2/cmdb/firewall/address |
| **specialparams**  string | Extra URL parameters, e.g.start=1&count=10 |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_json_generic_module.md#id4)

> **Note:**
>
> - Requires fortiosapi library developed by Fortinet
> - Run as a local_action in your playbook

## [Examples](fortios_json_generic_module.md#id5)

```yaml+jinja
---
# host
# [fortigates]
# fortigate01 ansible_host=192.168.52.177 ansible_user="admin" ansible_password="admin"

# [fortigates:vars]
# ansible_network_os=fortinet.fortios.fortios

# sample1.yml
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
  - name: test add with string
    fortios_json_generic:
      vdom:  "{{ vdom }}"
      json_generic:
        method: "POST"
        path: "/api/v2/cmdb/firewall/address"
        jsonbody: |
          {
          "name": "111",
          "type": "geography",
          "fqdn": "",
          "country": "AL",
          "comment": "ccc",
          "visibility": "enable",
          "associated-interface": "port1",
          "allow-routing": "disable"
          }
    register: info

  - name: display vars
    debug: msg="{{info}}"

# sample2.yml
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
  - name: test delete
    fortios_json_generic:
      vdom:  "{{ vdom }}"
      json_generic:
        method: "DELETE"
        path: "/api/v2/cmdb/firewall/address/111"
    register: info

  - name: display vars
    debug: msg="{{info}}"

  - name: test add with dict
    fortios_json_generic:
      vdom:  "{{ vdom }}"
      json_generic:
        method: "POST"
        path: "/api/v2/cmdb/firewall/address"
        dictbody:
          name: "111"
          type: "geography"
          fqdn: ""
          country: "AL"
          comment: "ccc"
          visibility: "enable"
          associated-interface: "port1"
          allow-routing: "disable"
    register: info

  - name: display vars
    debug: msg="{{info}}"

  - name: test delete
    fortios_json_generic:
      vdom:  "{{ vdom }}"
      json_generic:
        method: "DELETE"
        path: "/api/v2/cmdb/firewall/address/111"
    register: info

  - name: display vars
    debug: msg="{{info}}"

  - name: test add with string
    fortios_json_generic:
      vdom:  "{{ vdom }}"
      json_generic:
        method: "POST"
        path: "/api/v2/cmdb/firewall/address"
        jsonbody: |
          {
          "name": "111",
          "type": "geography",
          "fqdn": "",
          "country": "AL",
          "comment": "ccc",
          "visibility": "enable",
          "associated-interface": "port1",
          "allow-routing": "disable"
          }
    register: info

  - name: display vars
    debug: msg="{{info}}"

  - name: test speical params
    fortios_json_generic:
      vdom:  "{{ vdom }}"
      json_generic:
        method: "PUT"
        path: "/api/v2/cmdb/firewall/policy/1"
        specialparams: "action=move&after=2"
    register: info

  - name: display vars
    debug: msg="{{info}}"
```

## [Return Values](fortios_json_generic_module.md#id6)

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

- Frank Shen (@frankshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)

---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_generic module – Build and send generic FortiManager API request."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_generic_module.html
fetched_at: 2026-07-27T17:32:59+00:00
---
# fortinet.fortimanager.fmgr_generic module – Build and send generic FortiManager API request.

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/fortinet/fortimanager) (version 2.1.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_generic`.

New in fortinet.fortimanager 2.10

- [Synopsis](fmgr_generic_module.md#synopsis)
- [Parameters](fmgr_generic_module.md#parameters)
- [Notes](fmgr_generic_module.md#notes)
- [Examples](fmgr_generic_module.md#examples)
- [Return Values](fmgr_generic_module.md#return-values)

## [Synopsis](fmgr_generic_module.md#id1)

- This module is for generic fortimanager requests. it receives raw json-rpc data, and sends it to fortimanager, finally returns the response to users.
- This module also rely on fortimanager httpapi plugin as the transport.
- the payload doesn’t include session, the httpapi plugin will automatically fill the session later.
- the username and password is not managed by the module, but by the plugin.

## [Parameters](fmgr_generic_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **json**  string | the raw json-formatted payload to send to fortimanager |
| **method**  string | the method of the json-rpc  it must be in [get, add, set, update, delete, move, clone, exec] |
| **params**  string | the parameter collection. |

## [Notes](fmgr_generic_module.md#id3)

> **Note:**
>
> - two parameters schemes are supported, either in raw json format or in ansible recognnizable top-level parameters format.
> - json is defined as string, user is response for make it json-formatted
> - method and params should be specified by users if ‘json’ is not present
> - if all three parameters are provided, the ‘json’ is preferred.

## [Examples](fmgr_generic_module.md#id4)

```yaml+jinja
- hosts: fortimanager01
  connection: httpapi
  vars:
    adom: "root"
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
    -   name: 'login a user'
        fmgr_generic:
             method: 'exec'
             params:
                - url: 'sys/login/user'
                  data:
                   - user: 'APIUser'
                     passwd: 'Fortinet1!e'
    -   name: 'login another user'
        fmgr_generic:
             json: |
                  {
                   "method":"exec",
                   "params":[
                    {
                         "url":"sys/login/user",
                         "data":[
                            {
                               "user":"APIUser",
                               "passwd":"Fortinet1!"
                            }
                          ]
                     }
                    ]
                  }
```

## [Return Values](fmgr_generic_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  Returned: always |

### Authors

- Link Zheng (@zhengl)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
[Homepage](https://fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/tree/galaxy/2.1.7)

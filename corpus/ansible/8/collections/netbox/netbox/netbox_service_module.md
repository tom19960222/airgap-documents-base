---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_service module – Creates or removes service from NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_service_module.html
fetched_at: 2026-07-28T02:45:27+00:00
---
# netbox.netbox.netbox_service module – Creates or removes service from NetBox

> **Note:**
>
> This module is part of the [netbox.netbox collection](https://galaxy.ansible.com/ui/repo/published/netbox/netbox/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netbox.netbox`.
> You need further requirements to be able to use this module,
> see [Requirements](netbox_service_module.md#ansible-collections-netbox-netbox-netbox-service-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_service`.

New in netbox.netbox 0.1.5

- [Synopsis](netbox_service_module.md#synopsis)
- [Requirements](netbox_service_module.md#requirements)
- [Parameters](netbox_service_module.md#parameters)
- [Notes](netbox_service_module.md#notes)
- [Examples](netbox_service_module.md#examples)

## [Synopsis](netbox_service_module.md#id1)

- Creates or removes service from NetBox

## [Requirements](netbox_service_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_service_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the service configuration |
| **comments**  string  *added in netbox.netbox 3.10.0* | Comments that may include additional information in regards to the service |
| **custom_fields**  dictionary | Must exist in NetBox and in key/value format |
| **description**  string | Service description |
| **device**  any | Specifies on which device the service is running |
| **ipaddresses**  any | Specifies which IPaddresses to associate with service. |
| **name**  string / required | Name of the region to be created |
| **port**  integer | Specifies which port used by service |
| **ports**  list / elements=integer | Specifies which ports used by service (NetBox 2.10 and newer) |
| **protocol**  any / required | Specifies which protocol used by service |
| **tags**  list / elements=any | What tags to add/update |
| **virtual_machine**  any | Specifies on which virtual machine the service is running |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_service_module.md#id4)

> **Note:**
>
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_service_module.md#id5)

```yaml+jinja
- name: "Create netbox service"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create service
      netbox.netbox.netbox_service:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: Test666
          name: node-exporter
          port: 9100
          protocol: TCP
          ipaddresses:
            - address: 127.0.0.1
          tags:
            - prometheus
        state: present

    - name: Delete service
      netbox.netbox.netbox_service:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: Test666
          name: node-exporter
          port: 9100
          protocol: TCP
        state: absent
```

### Authors

- Kulakov Ilya (@TawR1024)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)

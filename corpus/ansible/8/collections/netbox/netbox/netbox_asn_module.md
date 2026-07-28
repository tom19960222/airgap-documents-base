---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_asn module – Create, update or delete ASNs within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_asn_module.html
fetched_at: 2026-07-28T02:44:45+00:00
---
# netbox.netbox.netbox_asn module – Create, update or delete ASNs within NetBox

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
> see [Requirements](netbox_asn_module.md#ansible-collections-netbox-netbox-netbox-asn-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_asn`.

New in netbox.netbox 3.12.0

- [Synopsis](netbox_asn_module.md#synopsis)
- [Requirements](netbox_asn_module.md#requirements)
- [Parameters](netbox_asn_module.md#parameters)
- [Notes](netbox_asn_module.md#notes)
- [Examples](netbox_asn_module.md#examples)
- [Return Values](netbox_asn_module.md#return-values)

## [Synopsis](netbox_asn_module.md#id1)

- Creates, updates or removes ASNs from NetBox

## [Requirements](netbox_asn_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_asn_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the ASN configuration |
| **asn**  integer / required | 32-bit autonomous system number |
| **custom_fields**  dictionary | Must exist in NetBox |
| **description**  string | Description |
| **rir**  any | RIR |
| **tags**  list / elements=any | Any tags that the ASN may need to be associated with |
| **tenant**  any | Tenant |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_asn_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_asn_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create ASN within NetBox with only required information
      netbox.netbox.netbox_asn:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          asn: 1111111111
          rir: RFC1111
          description: test ASN
        state: present

    - name: Delete ASN within netbox
      netbox.netbox.netbox_asn:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          asn: 1111111111
        state: absent
```

## [Return Values](netbox_asn_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **asn**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Andrii Konts (@andrii-konts)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)

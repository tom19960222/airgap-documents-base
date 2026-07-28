---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_export_template module – Creates, updates or deletes export templates within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_export_template_module.html
fetched_at: 2026-07-28T02:45:04+00:00
---
# netbox.netbox.netbox_export_template module – Creates, updates or deletes export templates within NetBox

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
> see [Requirements](netbox_export_template_module.md#ansible-collections-netbox-netbox-netbox-export-template-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_export_template`.

New in netbox.netbox 3.6.0

- [Synopsis](netbox_export_template_module.md#synopsis)
- [Requirements](netbox_export_template_module.md#requirements)
- [Parameters](netbox_export_template_module.md#parameters)
- [Notes](netbox_export_template_module.md#notes)
- [Examples](netbox_export_template_module.md#examples)
- [Return Values](netbox_export_template_module.md#return-values)

## [Synopsis](netbox_export_template_module.md#id1)

- Creates, updates or removes export templates from NetBox

## [Requirements](netbox_export_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_export_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the custom field |
| **as_attachment**  boolean | Download file as attachment  **Choices:**   - `false` - `true` |
| **content_type**  any | The content type to apply this export template to |
| **content_types**  list / elements=any  *added in netbox.netbox 3.10.0* | The content type to apply this export template to (NetBox 3.4+) |
| **description**  string | Description of the export template |
| **file_extension**  string | The file extension of the export template |
| **mime_type**  string | MIME type of the export template |
| **name**  string / required | The name of the export template |
| **template_code**  any / required | Template code of the export template |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_export_template_module.md#id4)

> **Note:**
>
> - This should be ran with connection `local` and hosts `localhost`
> - Use the `!unsafe` data type if you want jinja2 code in template_code

## [Examples](netbox_export_template_module.md#id5)

```yaml+jinja
- name: "Test NetBox custom_link module"
  connection: local
  hosts: localhost
  tasks:
    - name: Create a custom link on device
      netbox.netbox.netbox_export_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          content_type: "dcim.device"
          name: Custom Link
          link_text: "Open Web Management"
          link_url: !unsafe https://{{ obj.name }}.domain.local

    - name: Delete the custom link
      netbox.netbox.netbox_export_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          content_type: "dcim.device"
          name: Custom Link
          link_text: "Open Web Management"
          link_url: !unsafe https://{{ obj.name }}.domain.local
        state: absent
```

## [Return Values](netbox_export_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **custom_link**  dictionary | Serialized object as created/existent/updated/deleted within NetBox  **Returned:** always |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Martin Rødvand (@rodvand)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)

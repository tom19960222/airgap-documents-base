---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_custom_field module – Creates, updates or deletes custom fields within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_custom_field_module.html
fetched_at: 2026-07-28T02:44:57+00:00
---
# netbox.netbox.netbox_custom_field module – Creates, updates or deletes custom fields within NetBox

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
> see [Requirements](netbox_custom_field_module.md#ansible-collections-netbox-netbox-netbox-custom-field-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_custom_field`.

New in netbox.netbox 3.6.0

- [Synopsis](netbox_custom_field_module.md#synopsis)
- [Requirements](netbox_custom_field_module.md#requirements)
- [Parameters](netbox_custom_field_module.md#parameters)
- [Notes](netbox_custom_field_module.md#notes)
- [Examples](netbox_custom_field_module.md#examples)
- [Return Values](netbox_custom_field_module.md#return-values)

## [Synopsis](netbox_custom_field_module.md#id1)

- Creates, updates or removes custom fields from NetBox

## [Requirements](netbox_custom_field_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_custom_field_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the custom field |
| **choices**  list / elements=string | List of available choices (for selection fields) |
| **content_types**  list / elements=any | The content type(s) to apply this custom field to |
| **default**  any | Default value of the custom field |
| **description**  string | Description of the custom field |
| **filter_logic**  any | Filter logic of the custom field |
| **group_name**  string  *added in netbox.netbox 3.10.0* | The group to associate the custom field with |
| **label**  string | Label of the custom field |
| **name**  string / required | Name of the custom field |
| **object_type**  string  *added in netbox.netbox 3.7.0* | The object type of the custom field (if any) |
| **required**  boolean | Whether the custom field is required  **Choices:**   - `false` - `true` |
| **search_weight**  integer  *added in netbox.netbox 3.10.0* | Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored. |
| **type**  string | The type of custom field  **Choices:**   - `"text"` - `"longtext"` - `"integer"` - `"decimal"` - `"boolean"` - `"date"` - `"datetime"` - `"url"` - `"json"` - `"select"` - `"multiselect"` - `"object"` - `"multiobject"` |
| **ui_visibility**  string  *added in netbox.netbox 3.10.0* | The UI visibility of the custom field  **Choices:**   - `"read-write"` - `"read-only"` - `"hidden"` - `"hidden-ifunset"` |
| **validation_maximum**  integer | The maximum allowed value (for numeric fields) |
| **validation_minimum**  integer | The minimum allowed value (for numeric fields) |
| **validation_regex**  string | The regular expression to enforce on text fields |
| **weight**  integer | Fields with higher weights appear lower in a form |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_custom_field_module.md#id4)

> **Note:**
>
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_custom_field_module.md#id5)

```yaml+jinja
- name: "Test NetBox custom_fields module"
  connection: local
  hosts: localhost
  tasks:
    - name: Create a custom field on device and virtual machine
      netbox.netbox.netbox_custom_field:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          content_types:
            - dcim.device
            - virtualization.virtualmachine
          name: A Custom Field
          type: text

    - name: Update the custom field to make it required
      netbox.netbox.netbox_custom_field:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: A Custom Field
          required: yes

    - name: Update the custom field to make it read only
      netbox.netbox.netbox_custom_field:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: A Custom Field
          ui_visibility: read-only

    - name: Delete the custom field
      netbox.netbox.netbox_custom_field:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: A Custom Field
        state: absent
```

## [Return Values](netbox_custom_field_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **custom_field**  dictionary | Serialized object as created/existent/updated/deleted within NetBox  **Returned:** always |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Martin Rødvand (@rodvand)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)

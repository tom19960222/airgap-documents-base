---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_custom_link module – Creates, updates or deletes custom links within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_custom_link_module.html
fetched_at: 2026-07-28T02:44:58+00:00
---
# netbox.netbox.netbox_custom_link module – Creates, updates or deletes custom links within NetBox

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
> see [Requirements](netbox_custom_link_module.md#ansible-collections-netbox-netbox-netbox-custom-link-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_custom_link`.

New in netbox.netbox 3.6.0

- [Synopsis](netbox_custom_link_module.md#synopsis)
- [Requirements](netbox_custom_link_module.md#requirements)
- [Parameters](netbox_custom_link_module.md#parameters)
- [Notes](netbox_custom_link_module.md#notes)
- [Examples](netbox_custom_link_module.md#examples)
- [Return Values](netbox_custom_link_module.md#return-values)

## [Synopsis](netbox_custom_link_module.md#id1)

- Creates, updates or removes custom links from NetBox

## [Requirements](netbox_custom_link_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_custom_link_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the custom field |
| **button_class**  any | Button class for the custom link |
| **content_type**  any | The content type to apply this custom link to |
| **content_types**  list / elements=any  *added in netbox.netbox 3.10.0* | The content type to apply this custom link to (NetBox 3.4+) |
| **enabled**  boolean  *added in netbox.netbox 3.7.0* | Enable/disable custom link  **Choices:**   - `false` - `true` |
| **group_name**  string | The group to associate the custom link with |
| **link_text**  any / required | Link text of the custom link |
| **link_url**  any / required | Link URL of the custom link |
| **name**  string / required | The name of the custom link |
| **new_window**  boolean | Open link in new window  **Choices:**   - `false` - `true` |
| **weight**  integer | Fields with higher weights appear lower in a form |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_custom_link_module.md#id4)

> **Note:**
>
> - This should be ran with connection `local` and hosts `localhost`
> - Use the `!unsafe` data type if you want jinja2 code in link_text or link_url

## [Examples](netbox_custom_link_module.md#id5)

```yaml+jinja
- name: "Test NetBox custom_link module"
  connection: local
  hosts: localhost
  tasks:
    - name: Create a custom link on device
      netbox.netbox.netbox_custom_link:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          content_type: "dcim.device"
          name: Custom Link
          link_text: "Open Web Management"
          link_url: !unsafe https://{{ obj.name }}.domain.local

    - name: Delete the custom link
      netbox.netbox.netbox_custom_link:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          content_type: "dcim.device"
          name: Custom Link
          link_text: "Open Web Management"
          link_url: !unsafe https://{{ obj.name }}.domain.local
        state: absent
```

## [Return Values](netbox_custom_link_module.md#id6)

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

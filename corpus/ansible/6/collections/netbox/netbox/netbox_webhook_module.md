---
collection: ansible
version: "6"
title: "netbox.netbox.netbox_webhook module – Creates, updates or deletes webhook configuration within NetBox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netbox/netbox/netbox_webhook_module.html
fetched_at: 2026-07-28T00:15:15+00:00
---
# netbox.netbox.netbox_webhook module – Creates, updates or deletes webhook configuration within NetBox

> **Note:**
>
> This module is part of the [netbox.netbox collection](https://galaxy.ansible.com/netbox/netbox) (version 3.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netbox.netbox`.
> You need further requirements to be able to use this module,
> see [Requirements](netbox_webhook_module.md#ansible-collections-netbox-netbox-netbox-webhook-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_webhook`.

New in netbox.netbox 3.6.0

- [Synopsis](netbox_webhook_module.md#synopsis)
- [Requirements](netbox_webhook_module.md#requirements)
- [Parameters](netbox_webhook_module.md#parameters)
- [Notes](netbox_webhook_module.md#notes)
- [Examples](netbox_webhook_module.md#examples)
- [Return Values](netbox_webhook_module.md#return-values)

## [Synopsis](netbox_webhook_module.md#id1)

- Creates, updates or removes webhook configuration within NetBox

## [Requirements](netbox_webhook_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_webhook_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the custom field |
| **additional_headers**  string | User-supplied HTTP headers. Supports jinja2 code. |
| **body_template**  string | Body template for webhook. Supports jinja2 code. |
| **ca_file_path**  string | CA certificate file to use for SSL verification |
| **conditions**  string | A set of conditions which determine whether the webhook will be generated. |
| **content_types**  list / elements=any | The content type(s) to apply this webhook to  Required when *state=present* |
| **enabled**  boolean | Enable/disable the webhook.  Choices:   - `false` - `true` |
| **http_content_type**  string | The HTTP content type. |
| **http_method**  any | HTTP method of the webhook. |
| **name**  string / required | Name of the webhook |
| **payload_url**  string | URL for the webhook to use.  Required when *state=present* |
| **secret**  string | Secret key to generate X-Hook-Signature to include in the payload. |
| **ssl_verification**  boolean | Enable ssl verification.  Choices:   - `false` - `true` |
| **type_create**  boolean | Call this webhook when a matching object is created  Choices:   - `false` - `true` |
| **type_delete**  boolean | Call this webhook when a matching object is deleted  Choices:   - `false` - `true` |
| **type_update**  boolean | Call this webhook when a matching object is updated  Choices:   - `false` - `true` |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  Default: `true` |

## [Notes](netbox_webhook_module.md#id4)

> **Note:**
>
> - This should be ran with connection `local` and hosts `localhost`
> - Use `!unsafe` when adding jinja2 code to `additional_headers` or `body_template`

## [Examples](netbox_webhook_module.md#id5)

```yaml+jinja
- name: "Test NetBox webhook module"
  connection: local
  hosts: localhost
  tasks:
    - name: Create a webhook
      netbox_webhook:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          content_types:
            - dcim.device
          name: Example Webhook
          type_create: yes
          payload_url: https://payload.url/
          body_template: !unsafe >-
            {{ data }}

    - name: Update the webhook to run on delete
      netbox_webhook:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Example Webhook
          type_create: yes
          type_delete: yes
          payload_url: https://payload.url/
          body_template: !unsafe >-
            {{ data }}

    - name: Delete the webhook
      netbox_webhook:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Example Webhook
          type_create: yes
          type_delete: yes
          payload_url: https://payload.url/
          body_template: !unsafe >-
            {{ data }}
        state: absent
```

## [Return Values](netbox_webhook_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  Returned: always |
| **webhook**  dictionary | Serialized object as created/existent/updated/deleted within NetBox  Returned: always |

### Authors

- Martin Rødvand (@rodvand)

### Collection links

[Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
[Repository (Sources)](https://github.com/netbox-community/ansible_modules)

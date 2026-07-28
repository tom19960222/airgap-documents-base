---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_config_context module – Creates, updates or deletes configuration contexts within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_config_context_module.html
fetched_at: 2026-07-28T02:44:51+00:00
---
# netbox.netbox.netbox_config_context module – Creates, updates or deletes configuration contexts within NetBox

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
> see [Requirements](netbox_config_context_module.md#ansible-collections-netbox-netbox-netbox-config-context-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_config_context`.

New in netbox.netbox 3.3.0

- [Synopsis](netbox_config_context_module.md#synopsis)
- [Requirements](netbox_config_context_module.md#requirements)
- [Parameters](netbox_config_context_module.md#parameters)
- [Notes](netbox_config_context_module.md#notes)
- [Examples](netbox_config_context_module.md#examples)
- [Return Values](netbox_config_context_module.md#return-values)

## [Synopsis](netbox_config_context_module.md#id1)

- Creates, updates or removes configuration contexts from NetBox

## [Requirements](netbox_config_context_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_config_context_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the configuration context |
| **cluster_groups**  list / elements=string | List of cluster_groups to which configuration context applies |
| **cluster_types**  list / elements=string | List of cluster_types to which configuration context applies |
| **clusters**  list / elements=string | List of clusters to which configuration context applies |
| **data**  dictionary | JSON-formatted configuration context data |
| **description**  string | The description of the configuration context |
| **device_types**  list / elements=string | List of device_types to which configuration context applies |
| **is_active**  boolean | Whether configuration context is active  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the context |
| **platforms**  list / elements=string | List of platforms to which configuration context applies |
| **regions**  list / elements=string | List of regions where configuration context applies |
| **roles**  list / elements=string | List of roles to which configuration context applies |
| **site_groups**  list / elements=string | List of site groups where configuration context applies |
| **sites**  list / elements=string | List of sites where configuration context applies |
| **tags**  list / elements=string | Any tags that the configuration context associates with |
| **tenant_groups**  list / elements=string | List of tenant_groups to which configuration context applies |
| **tenants**  list / elements=string | List of tenants to which configuration context applies |
| **weight**  integer | The weight of the configuration context |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_config_context_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_config_context_module.md#id5)

```yaml+jinja
- name: "Test NetBox config_context module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create config context and apply it to sites euc1-az1, euc1-az2 with the default weight of 1000
      netbox.netbox.netbox_config_context:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "dns_nameservers-quadnine"
          description: "9.9.9.9"
          data: "{ \"dns\": { \"nameservers\": [ \"9.9.9.9\" ] } }"
          sites: [ euc1-az1, euc1-az2 ]

    - name: Detach config context from euc1-az1, euc1-az2 and attach to euc1-az3
      netbox.netbox.netbox_config_context:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "dns_nameservers-quadnine"
          data: "{ \"dns\": { \"nameservers\": [ \"9.9.9.9\" ] } }"
          sites: [ euc1-az3 ]

    - name: Delete config context
      netbox.netbox.netbox_config_context:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "dns_nameservers-quadnine"
          data: "{ \"dns\": { \"nameservers\": [ \"9.9.9.9\" ] } }"
        state: absent
```

## [Return Values](netbox_config_context_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **config_context**  dictionary | Serialized object as created/existent/updated/deleted within NetBox  **Returned:** always |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Pavel Korovin (@pkorovin)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)

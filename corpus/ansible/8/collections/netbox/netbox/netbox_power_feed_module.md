---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_power_feed module – Create, update or delete power feeds within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_power_feed_module.html
fetched_at: 2026-07-28T02:45:15+00:00
---
# netbox.netbox.netbox_power_feed module – Create, update or delete power feeds within NetBox

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
> see [Requirements](netbox_power_feed_module.md#ansible-collections-netbox-netbox-netbox-power-feed-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_power_feed`.

New in netbox.netbox 0.2.3

- [Synopsis](netbox_power_feed_module.md#synopsis)
- [Requirements](netbox_power_feed_module.md#requirements)
- [Parameters](netbox_power_feed_module.md#parameters)
- [Notes](netbox_power_feed_module.md#notes)
- [Examples](netbox_power_feed_module.md#examples)
- [Return Values](netbox_power_feed_module.md#return-values)

## [Synopsis](netbox_power_feed_module.md#id1)

- Creates, updates or removes power feeds from NetBox

## [Requirements](netbox_power_feed_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_power_feed_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the power feed configuration |
| **amperage**  integer | The amperage of the power feed |
| **comments**  string | Comments related to the power feed |
| **custom_fields**  dictionary | must exist in NetBox |
| **description**  string  *added in netbox.netbox 3.10.0* | Description of the power feed |
| **max_utilization**  integer | The maximum permissible draw of the power feed in percent |
| **name**  string / required | The name of the power feed |
| **phase**  string | The phase type of the power feed  **Choices:**   - `"single-phase"` - `"three-phase"` |
| **power_panel**  any / required | The power panel the power feed is terminated on |
| **rack**  any | The rack the power feed is assigned to |
| **status**  string | The status of the power feed  **Choices:**   - `"offline"` - `"active"` - `"planned"` - `"failed"` |
| **supply**  string | The supply type of the power feed  **Choices:**   - `"ac"` - `"dc"` |
| **tags**  list / elements=any | Any tags that the power feed may need to be associated with |
| **type**  string | The type of the power feed  **Choices:**   - `"primary"` - `"redundant"` |
| **voltage**  integer | The voltage of the power feed |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_power_feed_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_power_feed_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create power feed within NetBox with only required information
      netbox.netbox.netbox_power_feed:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Feed
          power_panel: Test Power Panel
        state: present

    - name: Update power feed with other fields
      netbox.netbox.netbox_power_feed:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Feed
          power_panel: Test Power Panel
          status: offline
          type: primary
          supply: ac
          phase: single-phase
          voltage: 230
          amperage: 16
          max_utilization: 80
          comments: normal power feed
        state: present

    - name: Delete power feed within netbox
      netbox.netbox.netbox_power_feed:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Feed
          power_panel: Test Power Panel
        state: absent
```

## [Return Values](netbox_power_feed_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |
| **power_feed**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |

### Authors

- Tobias Groß (@toerb)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)

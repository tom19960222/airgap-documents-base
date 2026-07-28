---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_site module – Creates or removes sites from NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_site_module.html
fetched_at: 2026-07-28T02:45:28+00:00
---
# netbox.netbox.netbox_site module – Creates or removes sites from NetBox

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
> see [Requirements](netbox_site_module.md#ansible-collections-netbox-netbox-netbox-site-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_site`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_site_module.md#synopsis)
- [Requirements](netbox_site_module.md#requirements)
- [Parameters](netbox_site_module.md#parameters)
- [Notes](netbox_site_module.md#notes)
- [Examples](netbox_site_module.md#examples)
- [Return Values](netbox_site_module.md#return-values)

## [Synopsis](netbox_site_module.md#id1)

- Creates or removes sites from NetBox

## [Requirements](netbox_site_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_site_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the site configuration |
| **asn**  integer | The ASN associated with the site |
| **comments**  string | Comments for the site. This can be markdown syntax |
| **contact_email**  string | Contact email for site |
| **contact_name**  string | Name of contact for site |
| **contact_phone**  string | Contact phone number for site |
| **custom_fields**  dictionary | must exist in NetBox |
| **description**  string | The description of the prefix |
| **facility**  string | Data center provider or facility, ex. Equinix NY7 |
| **latitude**  float | Latitude in decimal format |
| **longitude**  float | Longitude in decimal format |
| **name**  string / required | Name of the site to be created |
| **physical_address**  string | Physical address of site |
| **region**  any | The region that the site should be associated with |
| **shipping_address**  string | Shipping address of site |
| **site_group**  any  *added in netbox.netbox 3.3.0* | The site group the site will be associated with (NetBox 2.11+) |
| **slug**  string | URL-friendly unique shorthand |
| **status**  any | Status of the site |
| **tags**  list / elements=any | Any tags that the prefix may need to be associated with |
| **tenant**  any | The tenant the site will be assigned to |
| **time_zone**  string | Timezone associated with the site, ex. America/Denver |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_site_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_site_module.md#id5)

```yaml+jinja
- name: "Test NetBox site module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create site within NetBox with only required information
      netbox.netbox.netbox_site:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test - Colorado
        state: present

    - name: Delete site within netbox
      netbox.netbox.netbox_site:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test - Colorado
        state: absent

    - name: Create site with all parameters
      netbox.netbox.netbox_site:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test - California
          status: Planned
          region: Test Region
          site_group: Test Site Group
          tenant: Test Tenant
          facility: EquinoxCA7
          asn: 65001
          time_zone: America/Los Angeles
          description: This is a test description
          physical_address: Hollywood, CA, 90210
          shipping_address: Hollywood, CA, 90210
          latitude: 10.100000
          longitude: 12.200000
          contact_name: Jenny
          contact_phone: 867-5309
          contact_email: jenny@changednumber.com
          slug: test-california
          comments: ### Placeholder
        state: present
```

## [Return Values](netbox_site_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |
| **site**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** on creation |

### Authors

- Mikhail Yohman (@FragmentedPacket)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)

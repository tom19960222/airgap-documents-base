---
collection: ansible
version: "8"
title: "community.grafana.grafana_organization module – Manage Grafana Organization"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/grafana/grafana_organization_module.html
fetched_at: 2026-07-28T01:53:15+00:00
---
# community.grafana.grafana_organization module – Manage Grafana Organization

> **Note:**
>
> This module is part of the [community.grafana collection](https://galaxy.ansible.com/ui/repo/published/community/grafana/) (version 1.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.grafana`.
>
> To use it in a playbook, specify: `community.grafana.grafana_organization`.

New in community.grafana 1.3.0

- [Synopsis](grafana_organization_module.md#synopsis)
- [Parameters](grafana_organization_module.md#parameters)
- [Examples](grafana_organization_module.md#examples)
- [Return Values](grafana_organization_module.md#return-values)

## [Synopsis](grafana_organization_module.md#id1)

- Create/delete Grafana organization through org API.
- Tested with Grafana v6.5.0

## [Parameters](grafana_organization_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, *client_key* is not required |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If *client_cert* contains both the certificate and key, this option is not required. |
| **name**  string / required | The name of the Grafana Organization. |
| **state**  string | State if the organization should be present in Grafana or not  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url**  aliases: grafana_url  string / required | The Grafana URL. |
| **url_password**  aliases: grafana_password  string | The Grafana password for API authentication.  **Default:** `"admin"` |
| **url_username**  aliases: grafana_user  string | The Grafana user for API authentication.  **Default:** `"admin"` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](grafana_organization_module.md#id3)

```yaml+jinja
---
- name: Create a Grafana organization
  community.grafana.grafana_organization:
    url: "https://grafana.example.com"
    url_username: admin
    url_password: changeme
    name: orgtest
    state: present

- name: Delete a Grafana organization
  community.grafana.grafana_organization:
    url: "https://grafana.example.com"
    url_username: admin
    url_password: changeme
    name: orgtest
    state: absent
```

## [Return Values](grafana_organization_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **org**  complex | Information about the organization  **Returned:** when state present |
| **address**  dictionary | The org address  **Returned:** always  **Sample:** `{"address1": "", "address2": "", "city": "", "country": "", "state": "", "zipCode": ""}` |
| **id**  integer | The org id  **Returned:** always  **Sample:** `[42]` |
| **name**  string | The org name  **Returned:** always  **Sample:** `"['org42']"` |

### Authors

- paytroff (@paytroff)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.grafana/issues)
- [Homepage](https://github.com/ansible-collections/grafana)
- [Repository (Sources)](https://github.com/ansible-collections/community.grafana.git)

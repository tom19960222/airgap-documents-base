---
collection: ansible
version: "8"
title: "community.grafana.grafana_dashboard module – Manage Grafana dashboards"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/grafana/grafana_dashboard_module.html
fetched_at: 2026-07-28T01:53:13+00:00
---
# community.grafana.grafana_dashboard module – Manage Grafana dashboards

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
> To use it in a playbook, specify: `community.grafana.grafana_dashboard`.

New in community.grafana 1.0.0

- [Synopsis](grafana_dashboard_module.md#synopsis)
- [Parameters](grafana_dashboard_module.md#parameters)
- [Examples](grafana_dashboard_module.md#examples)
- [Return Values](grafana_dashboard_module.md#return-values)

## [Synopsis](grafana_dashboard_module.md#id1)

- Create, update, delete, export Grafana dashboards via API.

## [Parameters](grafana_dashboard_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, *client_key* is not required |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If *client_cert* contains both the certificate and key, this option is not required. |
| **commit_message**  aliases: message  string | Set a commit message for the version history.  Only used when `state` is `present`.  `message` alias is deprecated in Ansible 2.10, since it is used internally by Ansible Core Engine. |
| **dashboard_id**  string  *added in community.grafana 1.0.0* | Public Grafana.com dashboard id to import |
| **dashboard_revision**  string  *added in community.grafana 1.0.0* | Revision of the public grafana dashboard to import  **Default:** `"1"` |
| **folder**  string  *added in community.grafana 1.0.0* | The Grafana folder where this dashboard will be imported to.  **Default:** `"General"` |
| **grafana_api_key**  string | The Grafana API key.  If set, `url_username` and `url_password` will be ignored. |
| **org_id**  integer | The Grafana Organisation ID where the dashboard will be imported / exported.  Not used when *grafana_api_key* is set, because the grafana_api_key only belongs to one organisation..  **Default:** `1` |
| **overwrite**  boolean | Override existing dashboard when state is present.  **Choices:**   - `false` ← (default) - `true` |
| **path**  aliases: dashboard_url  string | The path to the json file containing the Grafana dashboard to import or export.  A http URL is also accepted (since 2.10).  Required if `state` is `export` or `present`. |
| **slug**  string | Deprecated since Grafana 5. Use grafana dashboard uid instead.  slug of the dashboard. It’s the friendly url name of the dashboard.  When `state` is `present`, this parameter can override the slug in the meta section of the json file.  If you want to import a json dashboard exported directly from the interface (not from the api), you have to specify the slug parameter because there is no meta section in the exported json. |
| **state**  string | State of the dashboard.  **Choices:**   - `"absent"` - `"export"` - `"present"` ← (default) |
| **uid**  string  *added in community.grafana 1.0.0* | uid of the dashboard to export when `state` is `export` or `absent`. |
| **url**  aliases: grafana_url  string / required | The Grafana URL. |
| **url_password**  aliases: grafana_password  string | The Grafana password for API authentication.  **Default:** `"admin"` |
| **url_username**  aliases: grafana_user  string | The Grafana user for API authentication.  **Default:** `"admin"` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](grafana_dashboard_module.md#id3)

```yaml+jinja
- hosts: localhost
  connection: local
  tasks:
    - name: Import Grafana dashboard foo
      community.grafana.grafana_dashboard:
        grafana_url: http://grafana.company.com
        grafana_api_key: "{{ grafana_api_key }}"
        state: present
        commit_message: Updated by ansible
        overwrite: yes
        path: /path/to/dashboards/foo.json

    - name: Import Grafana dashboard Zabbix
      community.grafana.grafana_dashboard:
        grafana_url: http://grafana.company.com
        grafana_api_key: "{{ grafana_api_key }}"
        folder: zabbix
        dashboard_id: 6098
        dashboard_revision: 1

    - name: Import Grafana dashboard zabbix
      community.grafana.grafana_dashboard:
        grafana_url: http://grafana.company.com
        grafana_api_key: "{{ grafana_api_key }}"
        folder: public
        dashboard_url: https://grafana.com/api/dashboards/6098/revisions/1/download

    - name: Export dashboard
      community.grafana.grafana_dashboard:
        grafana_url: http://grafana.company.com
        grafana_user: "admin"
        grafana_password: "{{ grafana_password }}"
        org_id: 1
        state: export
        uid: "000000653"
        path: "/path/to/dashboards/000000653.json"
```

## [Return Values](grafana_dashboard_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **uid**  string | uid or slug of the created / deleted / exported dashboard.  **Returned:** success  **Sample:** `"51"` |

### Authors

- Thierry Sallé (@seuf)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.grafana/issues)
- [Homepage](https://github.com/ansible-collections/grafana)
- [Repository (Sources)](https://github.com/ansible-collections/community.grafana.git)

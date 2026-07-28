---
collection: ansible
version: "8"
title: "cisco.mso.mso httpapi – MSO Ansible HTTPAPI Plugin."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/mso/mso_httpapi.html
fetched_at: 2026-07-28T01:38:21+00:00
---
# cisco.mso.mso httpapi – MSO Ansible HTTPAPI Plugin.

> **Note:**
>
> This httpapi plugin is part of the [cisco.mso collection](https://galaxy.ansible.com/ui/repo/published/cisco/mso/) (version 2.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.mso`.
>
> To use it in a playbook, specify: `cisco.mso.mso`.

New in cisco.mso 1.2.0

- [Synopsis](mso_httpapi.md#synopsis)
- [Parameters](mso_httpapi.md#parameters)

## [Synopsis](mso_httpapi.md#id1)

- This MSO plugin provides the HTTPAPI transport methods needed to initiate a connection to MSO, send API requests and process the response.

## [Parameters](mso_httpapi.md#id2)

| Parameter | Comments |
| --- | --- |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  **Configuration:**   - Environment variable: [`ANSIBLE_HTTPAPI_LOGIN_DOMAIN`](../../environment_variables.md#envvar-ANSIBLE_HTTPAPI_LOGIN_DOMAIN) - Variable: ansible_httpapi_login_domain |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
- [Homepage](https://cisco.com/go/aci)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

---
collection: ansible
version: "8"
title: "theforeman.foreman.smart_proxy module – Manage Smart Proxies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/smart_proxy_module.html
fetched_at: 2026-07-28T02:56:40+00:00
---
# theforeman.foreman.smart_proxy module – Manage Smart Proxies

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](smart_proxy_module.md#ansible-collections-theforeman-foreman-smart-proxy-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.smart_proxy`.

New in theforeman.foreman 1.4.0

- [Synopsis](smart_proxy_module.md#synopsis)
- [Requirements](smart_proxy_module.md#requirements)
- [Parameters](smart_proxy_module.md#parameters)
- [Attributes](smart_proxy_module.md#attributes)
- [Notes](smart_proxy_module.md#notes)
- [Examples](smart_proxy_module.md#examples)
- [Return Values](smart_proxy_module.md#return-values)

## [Synopsis](smart_proxy_module.md#id1)

- Create, update and delete Smart Proxies

## [Requirements](smart_proxy_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](smart_proxy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **download_policy**  string | The download policy for the Smart Proxy  Only available for Katello installations.  The download policy `background` is deprecated and not available since Katello 4.3.  The download policy `streamed` is available since Katello 4.5.  **Choices:**   - `"background"` - `"immediate"` - `"on_demand"` - `"streamed"` - `"inherit"` |
| **lifecycle_environments**  list / elements=string | Lifecycle Environments synced to the Smart Proxy.  Only available for Katello installations. |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **name**  string / required | Name of the Smart Proxy |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url**  string / required | URL of the Smart Proxy |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](smart_proxy_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Notes](smart_proxy_module.md#id5)

> **Note:**
>
> - Even with *state=present* this module does not install a new Smart Proxy.
> - It can only associate an existing Smart Proxy listening at the specified *url*.
> - Consider using *foreman-installer* to create Smart Proxies.

## [Examples](smart_proxy_module.md#id6)

```yaml+jinja
# Create a local Smart Proxy
- name: "Create Smart Proxy"
  theforeman.foreman.smart_proxy:
    username: "admin"
    password: "changeme"
    server_url: "https://{{ ansible_fqdn }}"
    name: "{{ ansible_fqdn }}"
    url: "https://{{ ansible_fqdn }}:9090"
    download_policy: "immediate"
    lifecycle_environments:
      - "Development"
    organizations:
      - "Default Organization"
    locations:
      - "Default Location"
    state: present
```

## [Return Values](smart_proxy_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **smart_proxies**  list / elements=dictionary | List of smart_proxies.  **Returned:** success |

### Authors

- James Stuart (@jstuart)
- Matthias M Dellweg (@mdellweg)
- Jeffrey van Pelt (@Thulium-Drake)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)

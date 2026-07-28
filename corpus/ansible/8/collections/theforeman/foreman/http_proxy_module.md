---
collection: ansible
version: "8"
title: "theforeman.foreman.http_proxy module – Manage HTTP Proxies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/http_proxy_module.html
fetched_at: 2026-07-28T02:56:07+00:00
---
# theforeman.foreman.http_proxy module – Manage HTTP Proxies

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
> see [Requirements](http_proxy_module.md#ansible-collections-theforeman-foreman-http-proxy-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.http_proxy`.

New in theforeman.foreman 1.1.0

- [Synopsis](http_proxy_module.md#synopsis)
- [Requirements](http_proxy_module.md#requirements)
- [Parameters](http_proxy_module.md#parameters)
- [Attributes](http_proxy_module.md#attributes)
- [Examples](http_proxy_module.md#examples)
- [Return Values](http_proxy_module.md#return-values)

## [Synopsis](http_proxy_module.md#id1)

- Create, update, and delete HTTP Proxies

## [Requirements](http_proxy_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](http_proxy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **name**  string / required | The HTTP Proxy name |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **proxy_password**  string | Password used to authenticate with the HTTP Proxy  When this parameter is set, the module will not be idempotent. |
| **proxy_username**  string | Username used to authenticate with the HTTP Proxy |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url**  string | URL of the HTTP Proxy  Required when creating a new HTTP Proxy. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](http_proxy_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](http_proxy_module.md#id5)

```yaml+jinja
- name: create example.org proxy
  theforeman.foreman.http_proxy:
    name: "example.org"
    url: "http://example.org:3128"
    locations:
      - "Munich"
    organizations:
      - "ACME"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present
```

## [Return Values](http_proxy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **http_proxies**  list / elements=dictionary | List of HTTP proxies.  **Returned:** success |

### Authors

- Evgeni Golov (@evgeni)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)

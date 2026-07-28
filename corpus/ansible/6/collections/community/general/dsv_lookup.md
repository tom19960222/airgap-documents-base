---
collection: ansible
version: "6"
title: "community.general.dsv lookup – Get secrets from Thycotic DevOps Secrets Vault"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/dsv_lookup.html
fetched_at: 2026-07-27T17:15:01+00:00
---
# community.general.dsv lookup – Get secrets from Thycotic DevOps Secrets Vault

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](dsv_lookup.md#ansible-collections-community-general-dsv-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.dsv`.

New in community.general 1.0.0

- [Synopsis](dsv_lookup.md#synopsis)
- [Requirements](dsv_lookup.md#requirements)
- [Terms](dsv_lookup.md#terms)
- [Keyword parameters](dsv_lookup.md#keyword-parameters)
- [Notes](dsv_lookup.md#notes)
- [Examples](dsv_lookup.md#examples)
- [Return Value](dsv_lookup.md#return-value)

## [Synopsis](dsv_lookup.md#id1)

- Uses the Thycotic DevOps Secrets Vault Python SDK to get Secrets from a DSV *tenant* using a *client_id* and *client_secret*.

## [Requirements](dsv_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python-dsv-sdk - <https://pypi.org/project/python-dsv-sdk/>

## [Terms](dsv_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | The path to the secret, e.g. `/staging/servers/web1`. |

## [Keyword parameters](dsv_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.dsv', key1=value1, key2=value2, ...)` and `query('community.general.dsv', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **client_id**  string / required | The client_id with which to request the Access Grant.  Configuration:   - INI entry:  ```YAML+Jinja   [dsv_lookup]   client_id = VALUE   ``` - Environment variable: [`DSV_CLIENT_ID`](../../environment_variables.md#envvar-DSV_CLIENT_ID) |
| **client_secret**  string / required | The client secret associated with the specific *client_id*.  Configuration:   - INI entry:  ```YAML+Jinja   [dsv_lookup]   client_secret = VALUE   ``` - Environment variable: [`DSV_CLIENT_SECRET`](../../environment_variables.md#envvar-DSV_CLIENT_SECRET) |
| **tenant**  string / required | The first format parameter in the default *url_template*.  Configuration:   - INI entry:  ```YAML+Jinja   [dsv_lookup]   tenant = VALUE   ``` - Environment variable: [`DSV_TENANT`](../../environment_variables.md#envvar-DSV_TENANT) |
| **tld**  string | The top-level domain of the tenant; the second format parameter in the default *url_template*.  Default: `"com"`  Configuration:   - INI entry:  ```YAML+Jinja   [dsv_lookup]   tld = com   ``` - Environment variable: [`DSV_TLD`](../../environment_variables.md#envvar-DSV_TLD) |
| **url_template**  string | The path to prepend to the base URL to form a valid REST API request.  Default: `"https://{}.secretsvaultcloud.{}/v1"`  Configuration:   - INI entry:  ```YAML+Jinja   [dsv_lookup]   url_template = https://{}.secretsvaultcloud.{}/v1   ``` - Environment variable: [`DSV_URL_TEMPLATE`](../../environment_variables.md#envvar-DSV_URL_TEMPLATE) |

## [Notes](dsv_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.dsv', term1, term2, key1=value1, key2=value2)` and `query('community.general.dsv', term1, term2, key1=value1, key2=value2)`

## [Examples](dsv_lookup.md#id6)

```yaml+jinja
- hosts: localhost
  vars:
      secret: "{{ lookup('community.general.dsv', '/test/secret') }}"
  tasks:
      - ansible.builtin.debug:
          msg: 'the password is {{ secret["data"]["password"] }}'
```

## [Return Value](dsv_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | One or more JSON responses to `GET /secrets/{path}`.  See <https://dsv.thycotic.com/api/index.html#operation/getSecret>.  Returned: success |

### Authors

- Adam Migus (@amigus)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

---
collection: ansible
version: "8"
title: "community.general.bitwarden_secrets_manager lookup – Retrieve secrets from Bitwarden Secrets Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/bitwarden_secrets_manager_lookup.html
fetched_at: 2026-07-28T01:52:40+00:00
---
# community.general.bitwarden_secrets_manager lookup – Retrieve secrets from Bitwarden Secrets Manager

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](bitwarden_secrets_manager_lookup.md#ansible-collections-community-general-bitwarden-secrets-manager-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.bitwarden_secrets_manager`.

New in community.general 7.2.0

- [Synopsis](bitwarden_secrets_manager_lookup.md#synopsis)
- [Requirements](bitwarden_secrets_manager_lookup.md#requirements)
- [Terms](bitwarden_secrets_manager_lookup.md#terms)
- [Keyword parameters](bitwarden_secrets_manager_lookup.md#keyword-parameters)
- [Notes](bitwarden_secrets_manager_lookup.md#notes)
- [Examples](bitwarden_secrets_manager_lookup.md#examples)
- [Return Value](bitwarden_secrets_manager_lookup.md#return-value)

## [Synopsis](bitwarden_secrets_manager_lookup.md#id1)

- Retrieve secrets from Bitwarden Secrets Manager.

## [Requirements](bitwarden_secrets_manager_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- bws (command line utility)

## [Terms](bitwarden_secrets_manager_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | Secret ID(s) to fetch values for. |

## [Keyword parameters](bitwarden_secrets_manager_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.bitwarden_secrets_manager', key1=value1, key2=value2, ...)` and `query('community.general.bitwarden_secrets_manager', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **bws_access_token**  string / required | The BWS access token to use for this lookup.  **Configuration:**   - Environment variable: [`BWS_ACCESS_TOKEN`](../../environment_variables.md#envvar-BWS_ACCESS_TOKEN) |

## [Notes](bitwarden_secrets_manager_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.bitwarden_secrets_manager', term1, term2, key1=value1, key2=value2)` and `query('community.general.bitwarden_secrets_manager', term1, term2, key1=value1, key2=value2)`

## [Examples](bitwarden_secrets_manager_lookup.md#id6)

```yaml+jinja
- name: Get a secret relying on the BWS_ACCESS_TOKEN environment variable for authentication
  ansible.builtin.debug:
    msg: >-
      {{ lookup("community.general.bitwarden_secrets_manager", "2bc23e48-4932-40de-a047-5524b7ddc972") }}

- name: Get a secret passing an explicit access token for authentication
  ansible.builtin.debug:
    msg: >-
      {{
        lookup(
          "community.general.bitwarden_secrets_manager",
          "2bc23e48-4932-40de-a047-5524b7ddc972",
          bws_access_token="9.4f570d14-4b54-42f5-bc07-60f4450b1db5.YmluYXJ5LXNvbWV0aGluZy0xMjMK:d2h5IGhlbGxvIHRoZXJlCg=="
        )
      }}

- name: Get two different secrets each using a different access token for authentication
  ansible.builtin.debug:
    msg:
      - '{{ lookup("community.general.bitwarden_secrets_manager", "2bc23e48-4932-40de-a047-5524b7ddc972", bws_access_token=token1) }}'
      - '{{ lookup("community.general.bitwarden_secrets_manager", "9d89af4c-eb5d-41f5-bb0f-4ae81215c768", bws_access_token=token2) }}'
  vars:
    token1: "9.4f570d14-4b54-42f5-bc07-60f4450b1db5.YmluYXJ5LXNvbWV0aGluZy0xMjMK:d2h5IGhlbGxvIHRoZXJlCg=="
    token2: "1.69b72797-6ea9-4687-a11e-848e41a30ae6.YW5zaWJsZSBpcyBncmVhdD8K:YW5zaWJsZSBpcyBncmVhdAo="

- name: Get just the value of a secret
  ansible.builtin.debug:
    msg: >-
      {{ lookup("community.general.bitwarden_secrets_manager", "2bc23e48-4932-40de-a047-5524b7ddc972").value }}
```

## [Return Value](bitwarden_secrets_manager_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | List containing one or more secrets.  **Returned:** success |

### Authors

- jantari (@jantari)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

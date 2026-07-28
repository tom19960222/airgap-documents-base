---
collection: ansible
version: "8"
title: "community.general.revbitspss lookup – Get secrets from RevBits PAM server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/revbitspss_lookup.html
fetched_at: 2026-07-28T01:53:00+00:00
---
# community.general.revbitspss lookup – Get secrets from RevBits PAM server

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
> see [Requirements](revbitspss_lookup.md#ansible-collections-community-general-revbitspss-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.revbitspss`.

New in community.general 4.1.0

- [Synopsis](revbitspss_lookup.md#synopsis)
- [Requirements](revbitspss_lookup.md#requirements)
- [Terms](revbitspss_lookup.md#terms)
- [Keyword parameters](revbitspss_lookup.md#keyword-parameters)
- [Notes](revbitspss_lookup.md#notes)
- [Examples](revbitspss_lookup.md#examples)
- [Return Value](revbitspss_lookup.md#return-value)

## [Synopsis](revbitspss_lookup.md#id1)

- Uses the revbits_ansible Python SDK to get Secrets from RevBits PAM Server using API key authentication with the REST API.

## [Requirements](revbitspss_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- revbits_ansible - <https://pypi.org/project/revbits_ansible/>

## [Terms](revbitspss_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | This will be an array of keys for secrets which you want to fetch from RevBits PAM. |

## [Keyword parameters](revbitspss_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.revbitspss', key1=value1, key2=value2, ...)` and `query('community.general.revbitspss', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | This will be the API key for authentication. You can get it from the RevBits PAM secret manager module. |
| **base_url**  string / required | This will be the base URL of the server, for example `https://server-url-here`. |

## [Notes](revbitspss_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.revbitspss', term1, term2, key1=value1, key2=value2)` and `query('community.general.revbitspss', term1, term2, key1=value1, key2=value2)`

## [Examples](revbitspss_lookup.md#id6)

```yaml+jinja
- hosts: localhost
  vars:
      secret: >-
        {{
            lookup(
                'community.general.revbitspss',
                'UUIDPAM', 'DB_PASS',
                base_url='https://server-url-here',
                api_key='API_KEY_GOES_HERE'
            )
        }}
  tasks:
      - ansible.builtin.debug:
          msg: >
            UUIDPAM is {{ (secret['UUIDPAM']) }} and DB_PASS is {{ (secret['DB_PASS']) }}
```

## [Return Value](revbitspss_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | The JSON responses which you can access with defined keys.  If you are fetching secrets named as UUID, PASSWORD it will gives you the dict of all secrets.  **Returned:** success |

### Authors

- RevBits (@RevBits)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

---
collection: ansible
version: "8"
title: "community.skydive.skydive lookup – Query Skydive objects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/skydive/skydive_lookup.html
fetched_at: 2026-07-28T01:59:22+00:00
---
# community.skydive.skydive lookup – Query Skydive objects

> **Note:**
>
> This lookup plugin is part of the [community.skydive collection](https://galaxy.ansible.com/ui/repo/published/community/skydive/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.skydive`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](skydive_lookup.md#ansible-collections-community-skydive-skydive-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.skydive.skydive`.

- [Synopsis](skydive_lookup.md#synopsis)
- [Requirements](skydive_lookup.md#requirements)
- [Keyword parameters](skydive_lookup.md#keyword-parameters)
- [Notes](skydive_lookup.md#notes)
- [Examples](skydive_lookup.md#examples)
- [Return Value](skydive_lookup.md#return-value)

## [Synopsis](skydive_lookup.md#id1)

- Uses the Skydive python REST client to return the queried object from Skydive network analyzer.

## [Requirements](skydive_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- skydive-client

## [Keyword parameters](skydive_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.skydive.skydive', key1=value1, key2=value2, ...)` and `query('community.skydive.skydive', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **filter**  string | a dict object that is used to filter the return objects |
| **provider**  string | A dict object containing connection details. |
| **endpoint**  string / required | Specifies the hostname/address along with the port as `localhost:8082`for connecting to the remote instance of SKYDIVE client over the REST API. |
| **insecure**  boolean | Ignore SSL certification verification.  **Choices:**   - `false` ← (default) - `true` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote instance of SKYDIVE client. |
| **ssl**  boolean | Specifies the ssl parameter that decides if the connection type shall be http or https.  **Choices:**   - `false` ← (default) - `true` |
| **user**  string | Configures the username to use to authenticate the connection to the remote instance of SKYDIVE client. |

## [Notes](skydive_lookup.md#id4)

> **Note:**
>
> - This module must be run locally, which can be achieved by specifying `connection: local`.

## [Examples](skydive_lookup.md#id5)

```yaml+jinja
- name: return skydive metdata if present based on Name
  set_fact:
    skydive_meta: >-
        {{ lookup('community.skydive.skydive', filter={'query': "G.V().Has('Name', 'sumit-VirtualBox')"}) }}

- name: return all the skydive metdata having parameter Name
  set_fact:
    skydive: >-
        {{ lookup('community.skydive.skydive', filter={'query': "G.V().Has('Name')"},
                      provider={'endpoint': 'localhost:8082', 'username': 'admin', 'password': 'password'}) }}
```

## [Return Value](skydive_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | The list of queried object metadata  **Returned:** always |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/skydive/issues)
- [Repository (Sources)](https://github.com/ansible-collections/skydive)

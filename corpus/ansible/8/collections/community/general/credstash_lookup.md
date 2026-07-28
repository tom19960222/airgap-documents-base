---
collection: ansible
version: "8"
title: "community.general.credstash lookup – retrieve secrets from Credstash on AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/credstash_lookup.html
fetched_at: 2026-07-28T01:52:44+00:00
---
# community.general.credstash lookup – retrieve secrets from Credstash on AWS

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
> see [Requirements](credstash_lookup.md#ansible-collections-community-general-credstash-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.credstash`.

- [Synopsis](credstash_lookup.md#synopsis)
- [Requirements](credstash_lookup.md#requirements)
- [Terms](credstash_lookup.md#terms)
- [Keyword parameters](credstash_lookup.md#keyword-parameters)
- [Notes](credstash_lookup.md#notes)
- [Examples](credstash_lookup.md#examples)
- [Return Value](credstash_lookup.md#return-value)

## [Synopsis](credstash_lookup.md#id1)

- Credstash is a small utility for managing secrets using AWS’s KMS and DynamoDB: <https://github.com/fugue/credstash>

## [Requirements](credstash_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- credstash (python library)

## [Terms](credstash_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | term or list of terms to lookup in the credit store |

## [Keyword parameters](credstash_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.credstash', key1=value1, key2=value2, ...)` and `query('community.general.credstash', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **aws_access_key_id**  string | AWS access key ID  **Configuration:**   - Environment variable: [`AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-AWS_ACCESS_KEY_ID) |
| **aws_secret_access_key**  string | AWS access key  **Configuration:**   - Environment variable: [`AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_SECRET_ACCESS_KEY) |
| **aws_session_token**  string | AWS session token  **Configuration:**   - Environment variable: [`AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-AWS_SESSION_TOKEN) |
| **profile_name**  string | AWS profile to use for authentication  **Configuration:**   - Environment variable: [`AWS_PROFILE`](../../environment_variables.md#envvar-AWS_PROFILE) |
| **region**  string | AWS region |
| **table**  string | name of the credstash table to query  **Default:** `"credential-store"` |
| **version**  string | Credstash version  **Default:** `""` |

## [Notes](credstash_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.credstash', term1, term2, key1=value1, key2=value2)` and `query('community.general.credstash', term1, term2, key1=value1, key2=value2)`

## [Examples](credstash_lookup.md#id6)

```yaml+jinja
- name: first use credstash to store your secrets
  ansible.builtin.shell: credstash put my-github-password secure123

- name: "Test credstash lookup plugin -- get my github password"
  ansible.builtin.debug:
    msg: "Credstash lookup! {{ lookup('community.general.credstash', 'my-github-password') }}"

- name: "Test credstash lookup plugin -- get my other password from us-west-1"
  ansible.builtin.debug:
    msg: "Credstash lookup! {{ lookup('community.general.credstash', 'my-other-password', region='us-west-1') }}"

- name: "Test credstash lookup plugin -- get the company's github password"
  ansible.builtin.debug:
    msg: "Credstash lookup! {{ lookup('community.general.credstash', 'company-github-password', table='company-passwords') }}"

- name: Example play using the 'context' feature
  hosts: localhost
  vars:
    context:
      app: my_app
      environment: production
  tasks:

  - name: "Test credstash lookup plugin -- get the password with a context passed as a variable"
    ansible.builtin.debug:
      msg: "{{ lookup('community.general.credstash', 'some-password', context=context) }}"

  - name: "Test credstash lookup plugin -- get the password with a context defined here"
    ansible.builtin.debug:
      msg: "{{ lookup('community.general.credstash', 'some-password', context=dict(app='my_app', environment='production')) }}"
```

## [Return Value](credstash_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | Value(s) stored in Credstash.  **Returned:** success |

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

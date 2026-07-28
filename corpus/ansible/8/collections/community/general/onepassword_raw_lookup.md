---
collection: ansible
version: "8"
title: "community.general.onepassword_raw lookup – fetch an entire item from 1Password"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/onepassword_raw_lookup.html
fetched_at: 2026-07-28T01:52:56+00:00
---
# community.general.onepassword_raw lookup – fetch an entire item from 1Password

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
> see [Requirements](onepassword_raw_lookup.md#ansible-collections-community-general-onepassword-raw-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.onepassword_raw`.

- [Synopsis](onepassword_raw_lookup.md#synopsis)
- [Requirements](onepassword_raw_lookup.md#requirements)
- [Terms](onepassword_raw_lookup.md#terms)
- [Keyword parameters](onepassword_raw_lookup.md#keyword-parameters)
- [Notes](onepassword_raw_lookup.md#notes)
- [Examples](onepassword_raw_lookup.md#examples)
- [Return Value](onepassword_raw_lookup.md#return-value)

## [Synopsis](onepassword_raw_lookup.md#id1)

- [community.general.onepassword_raw](onepassword_raw_lookup.md#ansible-collections-community-general-onepassword-raw-lookup) wraps `op` command line utility to fetch an entire item from 1Password.

## [Requirements](onepassword_raw_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- `op` 1Password command line utility. See <https://support.1password.com/command-line/>

## [Terms](onepassword_raw_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | identifier(s) (UUID, name, or domain; case-insensitive) of item(s) to retrieve. |

## [Keyword parameters](onepassword_raw_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.onepassword_raw', key1=value1, key2=value2, ...)` and `query('community.general.onepassword_raw', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **account_id**  string  *added in community.general 7.5.0* | The account ID to target. |
| **domain**  string  *added in community.general 6.0.0* | Domain of 1Password.  **Default:** `"1password.com"` |
| **master_password**  aliases: vault_password  string | The password used to unlock the specified vault. |
| **secret_key**  string | The secret key used when performing an initial sign in. |
| **section**  string | Item section containing the field to retrieve (case-insensitive). If absent will return first match from any section. |
| **service_account_token**  string  *added in community.general 7.1.0* | The access key for a service account.  Only works with 1Password CLI version 2 or later. |
| **subdomain**  string | The 1Password subdomain to authenticate against. |
| **username**  string | The username used to sign in. |
| **vault**  string | Vault containing the item to retrieve (case-insensitive). If absent will search all vaults. |

## [Notes](onepassword_raw_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.onepassword_raw', term1, term2, key1=value1, key2=value2)` and `query('community.general.onepassword_raw', term1, term2, key1=value1, key2=value2)`
> - This lookup will use an existing 1Password session if one exists. If not, and you have already performed an initial sign in (meaning `~/.op/config exists`), then only the `master_password` is required. You may optionally specify `subdomain` in this scenario, otherwise the last used subdomain will be used by `op`.
> - This lookup can perform an initial login by providing `subdomain`, `username`, `secret_key`, and `master_password`.
> - Can target a specific account by providing the `account_id`.
> - Due to the **very** sensitive nature of these credentials, it is **highly** recommended that you only pass in the minimal credentials needed at any given time. Also, store these credentials in an Ansible Vault using a key that is equal to or greater in strength to the 1Password master password.
> - This lookup stores potentially sensitive data from 1Password as Ansible facts. Facts are subject to caching if enabled, which means this data could be stored in clear text on disk or in a database.
> - Tested with `op` version 2.7.0

## [Examples](onepassword_raw_lookup.md#id6)

```yaml+jinja
- name: Retrieve all data about Wintermute
  ansible.builtin.debug:
    var: lookup('community.general.onepassword_raw', 'Wintermute')

- name: Retrieve all data about Wintermute when not signed in to 1Password
  ansible.builtin.debug:
    var: lookup('community.general.onepassword_raw', 'Wintermute', subdomain='Turing', vault_password='DmbslfLvasjdl')
```

## [Return Value](onepassword_raw_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | field data requested  **Returned:** success |

### Authors

- Scott Buchanan (@scottsb)
- Andrew Zenk (@azenk)
- Sam Doran (@samdoran)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

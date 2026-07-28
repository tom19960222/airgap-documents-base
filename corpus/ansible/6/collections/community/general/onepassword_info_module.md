---
collection: ansible
version: "6"
title: "community.general.onepassword_info module – Gather items from 1Password"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/onepassword_info_module.html
fetched_at: 2026-07-27T17:11:22+00:00
---
# community.general.onepassword_info module – Gather items from 1Password

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](onepassword_info_module.md#ansible-collections-community-general-onepassword-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.onepassword_info`.

- [Synopsis](onepassword_info_module.md#synopsis)
- [Requirements](onepassword_info_module.md#requirements)
- [Parameters](onepassword_info_module.md#parameters)
- [Notes](onepassword_info_module.md#notes)
- [Examples](onepassword_info_module.md#examples)
- [Return Values](onepassword_info_module.md#return-values)

## [Synopsis](onepassword_info_module.md#id1)

- [community.general.onepassword_info](onepassword_info_module.md#ansible-collections-community-general-onepassword-info-module) wraps the `op` command line utility to fetch data about one or more 1Password items.
- A fatal error occurs if any of the items being searched for can not be found.
- Recommend using with the `no_log` option to avoid logging the values of the secrets being retrieved.
- This module was called `onepassword_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [community.general.onepassword_info](onepassword_info_module.md#ansible-collections-community-general-onepassword-info-module) module no longer returns `ansible_facts`! You must now use the `register` option to use the facts in other tasks.

## [Requirements](onepassword_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- `op` 1Password command line utility. See <https://support.1password.com/command-line/>

## [Parameters](onepassword_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_login**  dictionary | A dictionary containing authentication details. If this is set, [community.general.onepassword_info](onepassword_info_module.md#ansible-collections-community-general-onepassword-info-module) will attempt to sign in to 1Password automatically.  Without this option, you must have already logged in via the 1Password CLI before running Ansible.  It is **highly** recommended to store 1Password credentials in an Ansible Vault. Ensure that the key used to encrypt the Ansible Vault is equal to or greater in strength than the 1Password master password. |
| **master_password**  string / required | The master password for your subdomain.  This is always required when specifying `auto_login`. |
| **secret_key**  string | The secret key for your subdomain.  Only required for initial sign in. |
| **subdomain**  string | 1Password subdomain name (<subdomain>.1password.com).  If this is not specified, the most recent subdomain will be used. |
| **username**  string | 1Password username.  Only required for initial sign in. |
| **cli_path**  path | Used to specify the exact path to the `op` command line interface  Default: `"op"` |
| **search_terms**  list / elements=dictionary / required | A list of one or more search terms.  Each search term can either be a simple string or it can be a dictionary for more control.  When passing a simple string, *field* is assumed to be `password`.  When passing a dictionary, the following fields are available. |
| **field**  string | The name of the field to search for within this item (optional, defaults to “password” (or “document” if the item has an attachment). |
| **name**  string | The name of the 1Password item to search for (required). |
| **section**  string | The name of a section within this item containing the specified field (optional, will search all sections if not specified). |
| **vault**  string | The name of the particular 1Password vault to search, useful if your 1Password user has access to multiple vaults (optional). |

## [Notes](onepassword_info_module.md#id4)

> **Note:**
>
> - Tested with `op` version 0.5.5
> - Based on the `onepassword` lookup plugin by Scott Buchanan <[sbuchanan@ri.pn](mailto:sbuchanan%40ri.pn)>.

## [Examples](onepassword_info_module.md#id5)

```yaml+jinja
# Gather secrets from 1Password, assuming there is a 'password' field:
- name: Get a password
  community.general.onepassword_info:
    search_terms: My 1Password item
  delegate_to: localhost
  register: my_1password_item
  no_log: true         # Don't want to log the secrets to the console!

# Gather secrets from 1Password, with more advanced search terms:
- name: Get a password
  community.general.onepassword_info:
    search_terms:
      - name:    My 1Password item
        field:   Custom field name       # optional, defaults to 'password'
        section: Custom section name     # optional, defaults to 'None'
        vault:   Name of the vault       # optional, only necessary if there is more than 1 Vault available
  delegate_to: localhost
  register: my_1password_item
  no_log: true                           # Don't want to log the secrets to the console!

# Gather secrets combining simple and advanced search terms to retrieve two items, one of which we fetch two
# fields. In the first 'password' is fetched, as a field name is not specified (default behaviour) and in the
# second, 'Custom field name' is fetched, as that is specified explicitly.
- name: Get a password
  community.general.onepassword_info:
    search_terms:
      - My 1Password item                # 'name' is optional when passing a simple string...
      - name: My Other 1Password item    # ...but it can also be set for consistency
      - name:    My 1Password item
        field:   Custom field name       # optional, defaults to 'password'
        section: Custom section name     # optional, defaults to 'None'
        vault:   Name of the vault       # optional, only necessary if there is more than 1 Vault available
      - name: A 1Password item with document attachment
  delegate_to: localhost
  register: my_1password_item
  no_log: true                           # Don't want to log the secrets to the console!

- name: Debug a password (for example)
  ansible.builtin.debug:
    msg: "{{ my_1password_item['onepassword']['My 1Password item'] }}"
```

## [Return Values](onepassword_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **onepassword**  dictionary | Dictionary of each 1password item matching the given search terms, shows what would be returned from the third example above.  Returned: success  Sample: `{"A 1Password item with document attachment": {"document": "the contents of the document attached to this item"}, "My 1Password item": {"Custom field name": "the value of this field", "password": "the value of this field"}, "My Other 1Password item": {"password": "the value of this field"}}` |

### Authors

- Ryan Conway (@Rylon)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

---
collection: ansible
version: "8"
title: "community.hashi_vault.vault_login_token filter – Extracts the Vault token from a login or token creation"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/hashi_vault/vault_login_token_filter.html
fetched_at: 2026-07-28T01:53:34+00:00
---
# community.hashi_vault.vault_login_token filter – Extracts the Vault token from a login or token creation

> **Note:**
>
> This filter plugin is part of the [community.hashi_vault collection](https://galaxy.ansible.com/ui/repo/published/community/hashi_vault/) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hashi_vault`.
>
> To use it in a playbook, specify: `community.hashi_vault.vault_login_token`.

New in community.hashi_vault 2.2.0

- [Synopsis](vault_login_token_filter.md#synopsis)
- [Input](vault_login_token_filter.md#input)
- [Keyword parameters](vault_login_token_filter.md#keyword-parameters)
- [Notes](vault_login_token_filter.md#notes)
- [See Also](vault_login_token_filter.md#see-also)
- [Examples](vault_login_token_filter.md#examples)
- [Return Value](vault_login_token_filter.md#return-value)

## [Synopsis](vault_login_token_filter.md#id1)

- Extracts the token value from the structure returned by a Vault token creation operation.

## [Input](vault_login_token_filter.md#id2)

This describes the input of the filter, the value before `| community.hashi_vault.vault_login_token`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | A dictionary matching the structure returned by a login or token creation. |

## [Keyword parameters](vault_login_token_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | community.hashi_vault.vault_login_token(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **optional_field**  string | If this field exists in the input dictionary, then the value of that field is used as the *_input* value.  The default value deals with the difference between the output of lookup plugins, and does not need to be changed in most cases.  See the examples or the Filter guide for more information.  **Default:** `"login"` |

## [Notes](vault_login_token_filter.md#id4)

> **Note:**
>
> - This filter is the same as reading into the *_input* dictionary directly, but it provides semantic meaning and automatically works with the differing output of the modules and lookups. See the Filter guide for more information.

## [See Also](vault_login_token_filter.md#id5)

> **See also:**
>
> [community.hashi_vault.vault_login](vault_login_module.md#ansible-collections-community-hashi-vault-vault-login-module)
> :   Perform a login operation against HashiCorp Vault.
>
> [community.hashi_vault.vault_token_create](vault_token_create_module.md#ansible-collections-community-hashi-vault-vault-token-create-module)
> :   Create a HashiCorp Vault token.
>
> [community.hashi_vault.vault_login](vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup) lookup plugin
> :   Perform a login operation against HashiCorp Vault.
>
> [community.hashi_vault.vault_token_create](vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup) lookup plugin
> :   Create a HashiCorp Vault token.
>
> [Filter Guide](docsite/filter_guide.md#ansible-collections-community-hashi-vault-docsite-filter-guide-vault-login-token)
> :   The `community.hashi_vault` Filter Guide

## [Examples](vault_login_token_filter.md#id6)

```yaml+jinja
- name: Set defaults
  vars:
    ansible_hashi_vault_url: https://vault:9801/
    ansible_hashi_vault_auth_method: userpass
    ansible_hashi_vault_username: user
    ansible_hashi_vault_password: "{{ lookup('env', 'MY_SECRET_PASSWORD') }}"
  module_defaults:
    community.hashi_vault.vault_login:
      url: '{{ ansible_hashi_vault_url }}'
      auth_method: '{{ ansible_hashi_vault_auth_method }}'
      username: '{{ ansible_hashi_vault_username }}'
      password: '{{ ansible_hashi_vault_password }}'
  block:
    - name: Perform a login with a lookup and display the token
      vars:
        login_response: "{{ lookup('community.hashi_vault.vault_login') }}"
      debug:
        msg: "The token is {{ login_response | community.hashi_vault.vault_login_token }}"

    - name: Perform a login with a module
      community.hashi_vault.vault_login:
      register: login_response

    - name: Display the token
      debug:
        msg: "The token is {{ login_response | community.hashi_vault.vault_login_token }}"

- name: Use of optional_field
  vars:
    lookup_login_response: "{{ lookup('community.hashi_vault.vault_login') }}"
    my_data:
      something: somedata
      vault_login: "{{ lookup_login_response }}"

    token_from_param: "{{ my_data | community.hashi_vault.vault_login_token(optional_field='vault_login') }}"
    token_from_deref: "{{ my_data['vault_login'] | community.hashi_vault.vault_login_token }}"
    # if the optional field doesn't exist, the dictionary itself is still checked
    unused_optional: "{{ my_data['vault_login'] | community.hashi_vault.vault_login_token(optional_field='missing') }}"
  block:
    - name: Display the variables
      ansible.builtin.debug:
        var: '{{ item }}'
      loop:
        - my_data
        - token_from_param
        - token_from_deref
        - unused_optional
```

## [Return Value](vault_login_token_filter.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | The token value.  **Returned:** always  **Sample:** `"s.nnrpog4i5gjizr6b8g1inwj3"` |

### Authors

- Brian Scholer (@briantist)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.hashi_vault/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.hashi_vault)
- [Discussion, Q&A, troubleshooting](https://github.com/ansible-collections/community.hashi_vault/discussions)
- [Communication](index.md#communication-for-community-hashi-vault)

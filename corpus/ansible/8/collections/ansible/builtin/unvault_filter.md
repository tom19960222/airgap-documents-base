---
collection: ansible
version: "8"
title: "ansible.builtin.unvault filter – Open an Ansible Vault"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/unvault_filter.html
fetched_at: 2026-07-28T01:08:23+00:00
---
# ansible.builtin.unvault filter – Open an Ansible Vault

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `unvault`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.unvault` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

New in ansible-core 2.12

- [Synopsis](unvault_filter.md#synopsis)
- [Input](unvault_filter.md#input)
- [Positional parameters](unvault_filter.md#positional-parameters)
- [Keyword parameters](unvault_filter.md#keyword-parameters)
- [Notes](unvault_filter.md#notes)
- [Examples](unvault_filter.md#examples)
- [Return Value](unvault_filter.md#return-value)

## [Synopsis](unvault_filter.md#id1)

- Retrieve your information from an encrypted Ansible Vault.

## [Input](unvault_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.unvault`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | Vault string, or an `AnsibleVaultEncryptedUnicode` string object. |

## [Positional parameters](unvault_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.unvault(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **secret**  string / required | Vault secret, the key that lets you open the vault. |

## [Keyword parameters](unvault_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.unvault(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **vault_id**  string | Secret identifier, used internally to try to best match a secret when multiple are provided.  **Default:** `"filter_default"` |

## [Notes](unvault_filter.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | ansible.builtin.unvault(positional1, positional2, key1=value1, key2=value2)`

## [Examples](unvault_filter.md#id6)

```yaml+jinja
# simply decrypt my key from a vault
vars:
  mykey: "{{ myvaultedkey|unvault(passphrase) }} "

- name: save templated unvaulted data
  template: src=dump_template_data.j2 dest=/some/key/clear.txt
  vars:
    template_data: '{{ secretdata|unvault(vaultsecret) }}'
```

## [Return Value](unvault_filter.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | The string that was contained in the vault.  **Returned:** success |

### Authors

- Brian Coca (@bcoca)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)

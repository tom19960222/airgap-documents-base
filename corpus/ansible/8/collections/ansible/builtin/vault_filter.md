---
collection: ansible
version: "8"
title: "ansible.builtin.vault filter – vault your secrets"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/vault_filter.html
fetched_at: 2026-07-28T01:04:58+00:00
---
# ansible.builtin.vault filter – vault your secrets

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `vault`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.vault` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

New in ansible-core 2.12

- [Synopsis](vault_filter.md#synopsis)
- [Input](vault_filter.md#input)
- [Positional parameters](vault_filter.md#positional-parameters)
- [Keyword parameters](vault_filter.md#keyword-parameters)
- [Notes](vault_filter.md#notes)
- [Examples](vault_filter.md#examples)
- [Return Value](vault_filter.md#return-value)

## [Synopsis](vault_filter.md#id1)

- Put your information into an encrypted Ansible Vault.

## [Input](vault_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.vault`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | Data to vault. |

## [Positional parameters](vault_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.vault(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **secret**  string / required | Vault secret, the key that lets you open the vault. |

## [Keyword parameters](vault_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.vault(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **salt**  string | Encryption salt, will be random if not provided.  While providing one makes the resulting encrypted string reproducible, it can lower the security of the vault. |
| **vault_id**  string | Secret identifier, used internally to try to best match a secret when multiple are provided.  **Default:** `"filter_default"` |
| **wrap_object**  boolean | This toggle can force the return of an `AnsibleVaultEncryptedUnicode` string object, when `False`, you get a simple string.  Mostly useful when combining with the `to_yaml` filter to output the ‘inline vault’ format.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](vault_filter.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | ansible.builtin.vault(positional1, positional2, key1=value1, key2=value2)`

## [Examples](vault_filter.md#id6)

```yaml+jinja
# simply encrypt my key in a vault
vars:
  myvaultedkey: "{{ keyrawdata|vault(passphrase) }} "

- name: save templated vaulted data
  template: src=dump_template_data.j2 dest=/some/key/vault.txt
  vars:
    mysalt: '{{2**256|random(seed=inventory_hostname)}}'
    template_data: '{{ secretdata|vault(vaultsecret, salt=mysalt) }}'
```

## [Return Value](vault_filter.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | The vault string that contains the secret data (or `AnsibleVaultEncryptedUnicode` string object).  **Returned:** success |

### Authors

- Brian Coca (@bcoca)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)

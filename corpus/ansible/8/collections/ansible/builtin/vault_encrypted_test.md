---
collection: ansible
version: "8"
title: "ansible.builtin.vault_encrypted test – Is this an encrypted vault"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/vault_encrypted_test.html
fetched_at: 2026-07-28T01:09:02+00:00
---
# ansible.builtin.vault_encrypted test – Is this an encrypted vault

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `vault_encrypted`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.vault_encrypted` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

New in ansible-base 2.10

- [Synopsis](vault_encrypted_test.md#synopsis)
- [Input](vault_encrypted_test.md#input)
- [Examples](vault_encrypted_test.md#examples)
- [Return Value](vault_encrypted_test.md#return-value)

## [Synopsis](vault_encrypted_test.md#id1)

- Verifies if the input is an Ansible vault.

## [Input](vault_encrypted_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.vault_encrypted` or `is not ansible.builtin.vault_encrypted`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | The possible vault. |

## [Examples](vault_encrypted_test.md#id3)

```yaml+jinja
thisisfalse: '{{ "any string" is ansible_vault }}'
thisistrue: '{{ "$ANSIBLE_VAULT;1.2;AES256;dev...." is ansible_vault }}'
```

## [Return Value](vault_encrypted_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the input is a valid ansible vault, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)

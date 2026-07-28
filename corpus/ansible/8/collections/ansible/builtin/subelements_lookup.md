---
collection: ansible
version: "8"
title: "ansible.builtin.subelements lookup – traverse nested key from a list of dictionaries"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/subelements_lookup.html
fetched_at: 2026-07-28T01:04:49+00:00
---
# ansible.builtin.subelements lookup – traverse nested key from a list of dictionaries

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `subelements`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.subelements` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](subelements_lookup.md#synopsis)
- [Terms](subelements_lookup.md#terms)
- [Keyword parameters](subelements_lookup.md#keyword-parameters)
- [Notes](subelements_lookup.md#notes)
- [Examples](subelements_lookup.md#examples)
- [Return Value](subelements_lookup.md#return-value)

## [Synopsis](subelements_lookup.md#id1)

- Subelements walks a list of hashes (aka dictionaries) and then traverses a list with a given (nested sub-)key inside of those records.

## [Terms](subelements_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | tuple of list of dictionaries and dictionary key to extract |

## [Keyword parameters](subelements_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.subelements', key1=value1, key2=value2, ...)` and `query('ansible.builtin.subelements', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **skip_missing**  string | Lookup accepts this flag from a dictionary as optional. See Example section for more information.  If set to `True`, the lookup plugin will skip the lists items that do not contain the given subkey.  If set to `False`, the plugin will yield an error and complain about the missing subkey.  **Default:** `false` |

## [Notes](subelements_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('ansible.builtin.subelements', term1, term2, key1=value1, key2=value2)` and `query('ansible.builtin.subelements', term1, term2, key1=value1, key2=value2)`

## [Examples](subelements_lookup.md#id5)

```yaml+jinja
- name: show var structure as it is needed for example to make sense
  hosts: all
  vars:
    users:
      - name: alice
        authorized:
          - /tmp/alice/onekey.pub
          - /tmp/alice/twokey.pub
        mysql:
            password: mysql-password
            hosts:
              - "%"
              - "127.0.0.1"
              - "::1"
              - "localhost"
            privs:
              - "*.*:SELECT"
              - "DB1.*:ALL"
        groups:
          - wheel
      - name: bob
        authorized:
          - /tmp/bob/id_rsa.pub
        mysql:
            password: other-mysql-password
            hosts:
              - "db1"
            privs:
              - "*.*:SELECT"
              - "DB2.*:ALL"
  tasks:
    - name: Set authorized ssh key, extracting just that data from 'users'
      ansible.posix.authorized_key:
        user: "{{ item.0.name }}"
        key: "{{ lookup('file', item.1) }}"
      with_subelements:
         - "{{ users }}"
         - authorized

    - name: Setup MySQL users, given the mysql hosts and privs subkey lists
      community.mysql.mysql_user:
        name: "{{ item.0.name }}"
        password: "{{ item.0.mysql.password }}"
        host: "{{ item.1 }}"
        priv: "{{ item.0.mysql.privs | join('/') }}"
      with_subelements:
        - "{{ users }}"
        - mysql.hosts

    - name: list groups for users that have them, don't error if groups key is missing
      ansible.builtin.debug: var=item
      loop: "{{ q('ansible.builtin.subelements', users, 'groups', {'skip_missing': True}) }}"
```

## [Return Value](subelements_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | list of subelements extracted  **Returned:** success |

### Authors

- Serge van Ginderachter

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)

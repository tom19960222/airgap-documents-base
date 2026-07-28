---
collection: ansible
version: "8"
title: "community.general.dependent lookup – Composes a list with nested elements of other lists or dicts which can depend on previous loop variables"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/dependent_lookup.html
fetched_at: 2026-07-28T01:52:45+00:00
---
# community.general.dependent lookup – Composes a list with nested elements of other lists or dicts which can depend on previous loop variables

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.dependent`.

New in community.general 3.1.0

- [Synopsis](dependent_lookup.md#synopsis)
- [Terms](dependent_lookup.md#terms)
- [Examples](dependent_lookup.md#examples)
- [Return Value](dependent_lookup.md#return-value)

## [Synopsis](dependent_lookup.md#id1)

- Takes the input lists and returns a list with elements that are lists, dictionaries, or template expressions which evaluate to lists or dicts, composed of the elements of the input evaluated lists and dictionaries.

## [Terms](dependent_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=dictionary / required | A list where the elements are one-element dictionaries, mapping a name to a string, list, or dictionary. The name is the index that is used in the result object. The value is iterated over as described below.  If the value is a list, it is simply iterated over.  If the value is a dictionary, it is iterated over and returned as if they would be processed by the [ansible.builtin.dict2items](../../ansible/builtin/dict2items_filter.md#ansible-collections-ansible-builtin-dict2items-filter) filter.  If the value is a string, it is evaluated as Jinja2 expressions which can access the previously chosen elements with `item.<index_name>`. The result must be a list or a dictionary. |

## [Examples](dependent_lookup.md#id3)

```yaml+jinja
- name: Install/remove public keys for active admin users
  ansible.posix.authorized_key:
    user: "{{ item.admin.key }}"
    key: "{{ lookup('file', item.key.public_key) }}"
    state: "{{ 'present' if item.key.active else 'absent' }}"
  when: item.admin.value.active
  with_community.general.dependent:
    - admin: admin_user_data
    - key: admin_ssh_keys[item.admin.key]
  loop_control:
    # Makes the output readable, so that it doesn't contain the whole subdictionaries and lists
    label: "{{ [item.admin.key, 'active' if item.key.active else 'inactive', item.key.public_key] }}"
  vars:
    admin_user_data:
      admin1:
        name: Alice
        active: true
      admin2:
        name: Bob
        active: true
    admin_ssh_keys:
      admin1:
        - private_key: keys/private_key_admin1.pem
          public_key: keys/private_key_admin1.pub
          active: true
      admin2:
        - private_key: keys/private_key_admin2.pem
          public_key: keys/private_key_admin2.pub
          active: true
        - private_key: keys/private_key_admin2-old.pem
          public_key: keys/private_key_admin2-old.pub
          active: false

- name: Update DNS records
  community.aws.route53:
    zone: "{{ item.zone.key }}"
    record: "{{ item.prefix.key ~ '.' if item.prefix.key else '' }}{{ item.zone.key }}"
    type: "{{ item.entry.key }}"
    ttl: "{{ item.entry.value.ttl | default(3600) }}"
    value: "{{ item.entry.value.value }}"
    state: "{{ 'absent' if (item.entry.value.absent | default(False)) else 'present' }}"
    overwrite: true
  loop_control:
    # Makes the output readable, so that it doesn't contain the whole subdictionaries and lists
    label: |-
        {{ [item.zone.key, item.prefix.key, item.entry.key,
            item.entry.value.ttl | default(3600),
            item.entry.value.absent | default(False), item.entry.value.value] }}
  with_community.general.dependent:
    - zone: dns_setup
    - prefix: item.zone.value
    - entry: item.prefix.value
  vars:
    dns_setup:
      example.com:
        '':
          A:
            value:
            - 1.2.3.4
          AAAA:
            value:
            - "2a01:1:2:3::1"
        'test._domainkey':
          TXT:
            ttl: 300
            value:
            - '"k=rsa; t=s; p=MIGfMA..."'
      example.org:
        'www':
          A:
            value:
            - 1.2.3.4
            - 5.6.7.8
```

## [Return Value](dependent_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | A list composed of dictionaries whose keys are the variable names from the input list.  **Returned:** success  **Sample:** `[{"key1": "a", "key2": "test"}, {"key1": "a", "key2": "foo"}, {"key1": "b", "key2": "bar"}]` |

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

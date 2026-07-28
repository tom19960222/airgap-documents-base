---
collection: ansible
version: "6"
title: "ansible.builtin.ini lookup – read data from an ini file"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/ini_lookup.html
fetched_at: 2026-07-27T16:44:20+00:00
---
# ansible.builtin.ini lookup – read data from an ini file

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `ini` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](ini_lookup.md#synopsis)
- [Terms](ini_lookup.md#terms)
- [Keyword parameters](ini_lookup.md#keyword-parameters)
- [Notes](ini_lookup.md#notes)
- [Examples](ini_lookup.md#examples)
- [Return Value](ini_lookup.md#return-value)

## [Synopsis](ini_lookup.md#id1)

- The ini lookup reads the contents of a file in INI format `key1=value1`. This plugin retrieves the value on the right side after the equal sign `'='` of a given section `[section]`.
- You can also read a property file which - in this case - does not contain section.

## [Terms](ini_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | The key(s) to look up. |

## [Keyword parameters](ini_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.ini', key1=value1, key2=value2, ...)` and `query('ansible.builtin.ini', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **allow_no_value**  aliases: allow_none  boolean  added in ansible-core 2.12 | Read an ini file which contains key without value and without ‘=’ symbol.  Choices:   - `false` ← (default) - `true` |
| **case_sensitive**  string  added in ansible-core 2.12 | Whether key names read from `file` should be case sensitive. This prevents duplicate key errors if keys only differ in case.  Default: `false` |
| **default**  string | Return value if the key is not in the ini file.  Default: `""` |
| **encoding**  string | Text encoding to use.  Default: `"utf-8"` |
| **file**  string | Name of the file to load.  Default: `"ansible.ini"` |
| **re**  boolean | Flag to indicate if the key supplied is a regexp.  Choices:   - `false` ← (default) - `true` |
| **section**  string | Section where to lookup the key.  Default: `"global"` |
| **type**  string | Type of the file. ‘properties’ refers to the Java properties files.  Choices:   - `"ini"` ← (default) - `"properties"` |

## [Notes](ini_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('ansible.builtin.ini', term1, term2, key1=value1, key2=value2)` and `query('ansible.builtin.ini', term1, term2, key1=value1, key2=value2)`

## [Examples](ini_lookup.md#id5)

```yaml+jinja
- ansible.builtin.debug: msg="User in integration is {{ lookup('ansible.builtin.ini', 'user', section='integration', file='users.ini') }}"

- ansible.builtin.debug: msg="User in production  is {{ lookup('ansible.builtin.ini', 'user', section='production',  file='users.ini') }}"

- ansible.builtin.debug: msg="user.name is {{ lookup('ansible.builtin.ini', 'user.name', type='properties', file='user.properties') }}"

- ansible.builtin.debug:
    msg: "{{ item }}"
  loop: "{{ q('ansible.builtin.ini', '.*', section='section1', file='test.ini', re=True) }}"

- name: Read an ini file with allow_no_value
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.ini', 'user', file='mysql.ini', section='mysqld', allow_no_value=True) }}"
```

## [Return Value](ini_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | value(s) of the key(s) in the ini file  Returned: success |

### Authors

- Yannig Perre <yannig.perre(at)gmail.com>

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)

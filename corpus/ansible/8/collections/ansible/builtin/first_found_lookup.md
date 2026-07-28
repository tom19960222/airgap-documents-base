---
collection: ansible
version: "8"
title: "ansible.builtin.first_found lookup – return first file found from list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/first_found_lookup.html
fetched_at: 2026-07-28T01:00:38+00:00
---
# ansible.builtin.first_found lookup – return first file found from list

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `first_found`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.first_found` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](first_found_lookup.md#synopsis)
- [Terms](first_found_lookup.md#terms)
- [Keyword parameters](first_found_lookup.md#keyword-parameters)
- [Notes](first_found_lookup.md#notes)
- [Examples](first_found_lookup.md#examples)
- [Return Value](first_found_lookup.md#return-value)

## [Synopsis](first_found_lookup.md#id1)

- This lookup checks a list of files and paths and returns the full path to the first combination found.
- As all lookups, when fed relative paths it will try use the current task’s location first and go up the chain to the containing locations of role / play / include and so on.
- The list of files has precedence over the paths searched. For example, A task in a role has a ‘file1’ in the play’s relative path, this will be used, ‘file2’ in role’s relative path will not.
- Either a list of files `_terms` or a key `files` with a list of files is required for this plugin to operate.

## [Terms](first_found_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string | A list of file names. |

## [Keyword parameters](first_found_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.first_found', key1=value1, key2=value2, ...)` and `query('ansible.builtin.first_found', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **files**  list / elements=string | A list of file names.  **Default:** `[]` |
| **paths**  list / elements=string | A list of paths in which to look for the files.  **Default:** `[]` |
| **skip**  boolean | When `True`, return an empty list when no files are matched.  This is useful when used with `with_first_found`, as an empty list return to `with_` calls causes the calling task to be skipped.  When used as a template via `lookup` or `query`, setting *skip=True* will \*not\* cause the task to skip. Tasks must handle the empty list return from the template.  When `False` and `lookup` or `query` specifies *errors=’ignore’* all errors (including no file found, but potentially others) return an empty string or an empty list respectively.  When `True` and `lookup` or `query` specifies *errors=’ignore’*, no file found will return an empty list and other potential errors return an empty string or empty list depending on the template call (in other words return values of `lookup` v `query`).  **Choices:**   - `false` ← (default) - `true` |

## [Notes](first_found_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('ansible.builtin.first_found', term1, term2, key1=value1, key2=value2)` and `query('ansible.builtin.first_found', term1, term2, key1=value1, key2=value2)`
> - This lookup can be used in ‘dual mode’, either passing a list of file names or a dictionary that has `files` and `paths`.

## [Examples](first_found_lookup.md#id5)

```yaml+jinja
- name: Set _found_file to the first existing file, raising an error if a file is not found
  ansible.builtin.set_fact:
    _found_file: "{{ lookup('ansible.builtin.first_found', findme) }}"
  vars:
    findme:
      - /path/to/foo.txt
      - bar.txt  # will be looked in files/ dir relative to role and/or play
      - /path/to/biz.txt

- name: Set _found_file to the first existing file, or an empty list if no files found
  ansible.builtin.set_fact:
    _found_file: "{{ lookup('ansible.builtin.first_found', files, paths=['/extra/path'], skip=True) }}"
  vars:
    files:
      - /path/to/foo.txt
      - /path/to/bar.txt

- name: Include tasks only if one of the files exist, otherwise skip the task
  ansible.builtin.include_tasks:
    file: "{{ item }}"
  with_first_found:
    - files:
      - path/tasks.yaml
      - path/other_tasks.yaml
      skip: True

- name: Include tasks only if one of the files exists, otherwise skip
  ansible.builtin.include_tasks: '{{ tasks_file }}'
  when: tasks_file != ""
  vars:
    tasks_file: "{{ lookup('ansible.builtin.first_found', files=['tasks.yaml', 'other_tasks.yaml'], errors='ignore') }}"

- name: |
        copy first existing file found to /some/file,
        looking in relative directories from where the task is defined and
        including any play objects that contain it
  ansible.builtin.copy:
    src: "{{ lookup('ansible.builtin.first_found', findme) }}"
    dest: /some/file
  vars:
    findme:
      - foo
      - "{{ inventory_hostname }}"
      - bar

- name: same copy but specific paths
  ansible.builtin.copy:
    src: "{{ lookup('ansible.builtin.first_found', params) }}"
    dest: /some/file
  vars:
    params:
      files:
        - foo
        - "{{ inventory_hostname }}"
        - bar
      paths:
        - /tmp/production
        - /tmp/staging

- name: INTERFACES | Create Ansible header for /etc/network/interfaces
  ansible.builtin.template:
    src: "{{ lookup('ansible.builtin.first_found', findme)}}"
    dest: "/etc/foo.conf"
  vars:
    findme:
      - "{{ ansible_virtualization_type }}_foo.conf"
      - "default_foo.conf"

- name: read vars from first file found, use 'vars/' relative subdir
  ansible.builtin.include_vars: "{{lookup('ansible.builtin.first_found', params)}}"
  vars:
    params:
      files:
        - '{{ ansible_distribution }}.yml'
        - '{{ ansible_os_family }}.yml'
        - default.yml
      paths:
        - 'vars'
```

## [Return Value](first_found_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=path | path to file found  **Returned:** success |

### Authors

- Seth Vidal

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)

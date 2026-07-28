---
collection: ansible
version: "8"
title: "Merging lists of dictionaries"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/docsite/filter_guide_abstract_informations_merging_lists_of_dictionaries.html
fetched_at: 2026-07-28T03:00:42+00:00
---
# Merging lists of dictionaries

If you have two or more lists of dictionaries and want to combine them into a list of merged dictionaries, where the dictionaries are merged by an attribute, you can use the [community.general.lists_mergeby filter](../lists_mergeby_filter.md#ansible-collections-community-general-lists-mergeby-filter).

> **Note:**
>
> The output of the examples in this section use the YAML callback plugin. Quoting: “Ansible output that can be quite a bit easier to read than the default JSON formatting.” See [the documentation for the community.general.yaml callback plugin](../yaml_callback.md#ansible-collections-community-general-yaml-callback).

Let us use the lists below in the following examples:

```yaml
list1:
  - name: foo
    extra: true
  - name: bar
    extra: false
  - name: meh
    extra: true

list2:
  - name: foo
    path: /foo
  - name: baz
    path: /baz
```

In the example below the lists are merged by the attribute `name`:

```yaml+jinja
list3: "{{ list1|
           community.general.lists_mergeby(list2, 'name') }}"
```

This produces:

```yaml
list3:
- extra: false
  name: bar
- name: baz
  path: /baz
- extra: true
  name: foo
  path: /foo
- extra: true
  name: meh
```

New in version 2.0.0.

It is possible to use a list of lists as an input of the filter:

```yaml+jinja
list3: "{{ [list1, list2]|
           community.general.lists_mergeby('name') }}"
```

This produces the same result as in the previous example:

```yaml
list3:
- extra: false
  name: bar
- name: baz
  path: /baz
- extra: true
  name: foo
  path: /foo
- extra: true
  name: meh
```

The filter also accepts two optional parameters: `recursive` and `list_merge`. This is available since community.general 4.4.0.

**recursive**
:   Is a boolean, default to `false`. Should the [community.general.lists_mergeby](../lists_mergeby_filter.md#ansible-collections-community-general-lists-mergeby-filter) filter recursively merge nested hashes. Note: It does not depend on the value of the `hash_behaviour` setting in `ansible.cfg`.

**list_merge**
:   Is a string, its possible values are `replace` (default), `keep`, `append`, `prepend`, `append_rp` or `prepend_rp`. It modifies the behaviour of [community.general.lists_mergeby](../lists_mergeby_filter.md#ansible-collections-community-general-lists-mergeby-filter) when the hashes to merge contain arrays/lists.

The examples below set `recursive=true` and display the differences among all six options of `list_merge`. Functionality of the parameters is exactly the same as in the filter [ansible.builtin.combine](../../../ansible/builtin/combine_filter.md#ansible-collections-ansible-builtin-combine-filter). See [Combining hashes/dictionaries](../../../ansible/builtin/combine_filter.md#combine-filter) to learn details about these options.

Let us use the lists below in the following examples

```yaml
list1:
  - name: myname01
    param01:
      x: default_value
      y: default_value
      list:
        - default_value
  - name: myname02
    param01: [1, 1, 2, 3]

list2:
  - name: myname01
    param01:
      y: patch_value
      z: patch_value
      list:
        - patch_value
  - name: myname02
    param01: [3, 4, 4, {key: value}]
```

Example `list_merge=replace` (default):

```yaml+jinja
list3: "{{ [list1, list2]|
           community.general.lists_mergeby('name',
                                           recursive=true) }}"
```

This produces:

```yaml
list3:
- name: myname01
  param01:
    list:
    - patch_value
    x: default_value
    y: patch_value
    z: patch_value
- name: myname02
  param01:
  - 3
  - 4
  - 4
  - key: value
```

Example `list_merge=keep`:

```yaml+jinja
list3: "{{ [list1, list2]|
           community.general.lists_mergeby('name',
                                           recursive=true,
                                           list_merge='keep') }}"
```

This produces:

```yaml
list3:
- name: myname01
  param01:
    list:
    - default_value
    x: default_value
    y: patch_value
    z: patch_value
- name: myname02
  param01:
  - 1
  - 1
  - 2
  - 3
```

Example `list_merge=append`:

```yaml+jinja
list3: "{{ [list1, list2]|
           community.general.lists_mergeby('name',
                                           recursive=true,
                                           list_merge='append') }}"
```

This produces:

```yaml
list3:
- name: myname01
  param01:
    list:
    - default_value
    - patch_value
    x: default_value
    y: patch_value
    z: patch_value
- name: myname02
  param01:
  - 1
  - 1
  - 2
  - 3
  - 3
  - 4
  - 4
  - key: value
```

Example `list_merge=prepend`:

```yaml+jinja
list3: "{{ [list1, list2]|
           community.general.lists_mergeby('name',
                                           recursive=true,
                                           list_merge='prepend') }}"
```

This produces:

```yaml
list3:
- name: myname01
  param01:
    list:
    - patch_value
    - default_value
    x: default_value
    y: patch_value
    z: patch_value
- name: myname02
  param01:
  - 3
  - 4
  - 4
  - key: value
  - 1
  - 1
  - 2
  - 3
```

Example `list_merge=append_rp`:

```yaml+jinja
list3: "{{ [list1, list2]|
           community.general.lists_mergeby('name',
                                           recursive=true,
                                           list_merge='append_rp') }}"
```

This produces:

```yaml
list3:
- name: myname01
  param01:
    list:
    - default_value
    - patch_value
    x: default_value
    y: patch_value
    z: patch_value
- name: myname02
  param01:
  - 1
  - 1
  - 2
  - 3
  - 4
  - 4
  - key: value
```

Example `list_merge=prepend_rp`:

```yaml+jinja
list3: "{{ [list1, list2]|
           community.general.lists_mergeby('name',
                                           recursive=true,
                                           list_merge='prepend_rp') }}"
```

This produces:

```yaml
list3:
- name: myname01
  param01:
    list:
    - patch_value
    - default_value
    x: default_value
    y: patch_value
    z: patch_value
- name: myname02
  param01:
  - 3
  - 4
  - 4
  - key: value
  - 1
  - 1
  - 2
```

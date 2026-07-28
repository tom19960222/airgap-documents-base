---
collection: ansible
version: "8"
title: "ansible.builtin.csvfile lookup – read data from a TSV or CSV file"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/csvfile_lookup.html
fetched_at: 2026-07-28T01:08:29+00:00
---
# ansible.builtin.csvfile lookup – read data from a TSV or CSV file

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `csvfile`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.csvfile` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](csvfile_lookup.md#synopsis)
- [Keyword parameters](csvfile_lookup.md#keyword-parameters)
- [Notes](csvfile_lookup.md#notes)
- [Examples](csvfile_lookup.md#examples)
- [Return Value](csvfile_lookup.md#return-value)

## [Synopsis](csvfile_lookup.md#id1)

- The csvfile lookup reads the contents of a file in CSV (comma-separated value) format. The lookup looks for the row where the first column matches keyname (which can be multiple words) and returns the value in the `col` column (default 1, which indexed from 0 means the second column in the file).

## [Keyword parameters](csvfile_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.csvfile', key1=value1, key2=value2, ...)` and `query('ansible.builtin.csvfile', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **col**  string | column to return (0 indexed).  **Default:** `"1"` |
| **default**  string | what to return if the value is not found in the file. |
| **delimiter**  string | field separator in the file, for a tab you can specify `TAB` or `\t`.  **Default:** `"TAB"` |
| **encoding**  string | Encoding (character set) of the used CSV file.  **Default:** `"utf-8"` |
| **file**  string | name of the CSV/TSV file to open.  **Default:** `"ansible.csv"` |

## [Notes](csvfile_lookup.md#id3)

> **Note:**
>
> - The default is for TSV files (tab delimited) not CSV (comma delimited) … yes the name is misleading.
> - As of version 2.11, the search parameter (text that must match the first column of the file) and filename parameter can be multi-word.
> - For historical reasons, in the search keyname, quotes are treated literally and cannot be used around the string unless they appear (escaped as required) in the first column of the file you are parsing.

## [Examples](csvfile_lookup.md#id4)

```yaml+jinja
- name:  Match 'Li' on the first column, return the second column (0 based index)
  ansible.builtin.debug: msg="The atomic number of Lithium is {{ lookup('ansible.builtin.csvfile', 'Li file=elements.csv delimiter=,') }}"

- name: msg="Match 'Li' on the first column, but return the 3rd column (columns start counting after the match)"
  ansible.builtin.debug: msg="The atomic mass of Lithium is {{ lookup('ansible.builtin.csvfile', 'Li file=elements.csv delimiter=, col=2') }}"

- name: Define Values From CSV File, this reads file in one go, but you could also use col= to read each in it's own lookup.
  ansible.builtin.set_fact:
    loop_ip: "{{ csvline[0] }}"
    int_ip: "{{ csvline[1] }}"
    int_mask: "{{ csvline[2] }}"
    int_name: "{{ csvline[3] }}"
    local_as: "{{ csvline[4] }}"
    neighbor_as: "{{ csvline[5] }}"
    neigh_int_ip: "{{ csvline[6] }}"
  vars:
    csvline = "{{ lookup('ansible.builtin.csvfile', bgp_neighbor_ip, file='bgp_neighbors.csv', delimiter=',') }}"
  delegate_to: localhost
```

## [Return Value](csvfile_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | value(s) stored in file column  **Returned:** success |

### Authors

- Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)

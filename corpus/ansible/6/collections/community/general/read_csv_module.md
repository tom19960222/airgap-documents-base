---
collection: ansible
version: "6"
title: "community.general.read_csv module – Read a CSV file"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/read_csv_module.html
fetched_at: 2026-07-27T17:12:35+00:00
---
# community.general.read_csv module – Read a CSV file

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.read_csv`.

- [Synopsis](read_csv_module.md#synopsis)
- [Parameters](read_csv_module.md#parameters)
- [Notes](read_csv_module.md#notes)
- [Examples](read_csv_module.md#examples)
- [Return Values](read_csv_module.md#return-values)

## [Synopsis](read_csv_module.md#id1)

- Read a CSV file and return a list or a dictionary, containing one dictionary per row.

## [Parameters](read_csv_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **delimiter**  string | A one-character string used to separate fields.  When using this parameter, you change the default value used by *dialect*.  The default value depends on the dialect used. |
| **dialect**  string | The CSV dialect to use when parsing the CSV file.  Possible values include `excel`, `excel-tab` or `unix`.  Default: `"excel"` |
| **fieldnames**  list / elements=string | A list of field names for every column.  This is needed if the CSV does not have a header. |
| **key**  string | The column name used as a key for the resulting dictionary.  If `key` is unset, the module returns a list of dictionaries, where each dictionary is a row in the CSV file. |
| **path**  aliases: filename  path / required | The CSV filename to read data from. |
| **skipinitialspace**  boolean | Whether to ignore any whitespaces immediately following the delimiter.  When using this parameter, you change the default value used by *dialect*.  The default value depends on the dialect used.  Choices:   - `false` - `true` |
| **strict**  boolean | Whether to raise an exception on bad CSV input.  When using this parameter, you change the default value used by *dialect*.  The default value depends on the dialect used.  Choices:   - `false` - `true` |
| **unique**  boolean | Whether the `key` used is expected to be unique.  Choices:   - `false` - `true` ← (default) |

## [Notes](read_csv_module.md#id3)

> **Note:**
>
> - Ansible also ships with the `csvfile` lookup plugin, which can be used to do selective lookups in CSV files from Jinja.

## [Examples](read_csv_module.md#id4)

```yaml+jinja
# Example CSV file with header
#
#   name,uid,gid
#   dag,500,500
#   jeroen,501,500

# Read a CSV file and access user 'dag'
- name: Read users from CSV file and return a dictionary
  community.general.read_csv:
    path: users.csv
    key: name
  register: users
  delegate_to: localhost

- ansible.builtin.debug:
    msg: 'User {{ users.dict.dag.name }} has UID {{ users.dict.dag.uid }} and GID {{ users.dict.dag.gid }}'

# Read a CSV file and access the first item
- name: Read users from CSV file and return a list
  community.general.read_csv:
    path: users.csv
  register: users
  delegate_to: localhost

- ansible.builtin.debug:
    msg: 'User {{ users.list.1.name }} has UID {{ users.list.1.uid }} and GID {{ users.list.1.gid }}'

# Example CSV file without header and semi-colon delimiter
#
#   dag;500;500
#   jeroen;501;500

# Read a CSV file without headers
- name: Read users from CSV file and return a list
  community.general.read_csv:
    path: users.csv
    fieldnames: name,uid,gid
    delimiter: ';'
  register: users
  delegate_to: localhost
```

## [Return Values](read_csv_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dict**  dictionary | The CSV content as a dictionary.  Returned: success  Sample: `{"dag": {"gid": 500, "name": "dag", "uid": 500}, "jeroen": {"gid": 500, "name": "jeroen", "uid": 501}}` |
| **list**  list / elements=string | The CSV content as a list.  Returned: success  Sample: `[{"gid": 500, "name": "dag", "uid": 500}, {"gid": 500, "name": "jeroen", "uid": 501}]` |

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

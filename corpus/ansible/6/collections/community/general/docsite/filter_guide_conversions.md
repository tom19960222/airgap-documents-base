---
collection: ansible
version: "6"
title: "Conversions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/docsite/filter_guide_conversions.html
fetched_at: 2026-07-28T00:24:56+00:00
---
# Conversions

## Parsing CSV files

Ansible offers the [community.general.read_csv module](../read_csv_module.md#ansible-collections-community-general-read-csv-module) to read CSV files. Sometimes you need to convert strings to CSV files instead. For this, the `from_csv` filter exists.

```yaml+jinja
- name: "Parse CSV from string"
  debug:
    msg: "{{ csv_string | community.general.from_csv }}"
  vars:
    csv_string: |
      foo,bar,baz
      1,2,3
      you,this,then
```

This produces:

```ansible-output
TASK [Parse CSV from string] **************************************************************
ok: [localhost] => {
    "msg": [
        {
            "bar": "2",
            "baz": "3",
            "foo": "1"
        },
        {
            "bar": "this",
            "baz": "then",
            "foo": "you"
        }
    ]
}
```

The `from_csv` filter has several keyword arguments to control its behavior:

dialect:
:   Dialect of the CSV file. Default is `excel`. Other possible choices are `excel-tab` and `unix`. If one of `delimiter`, `skipinitialspace` or `strict` is specified, `dialect` is ignored.

fieldnames:
:   A set of column names to use. If not provided, the first line of the CSV is assumed to contain the column names.

delimiter:
:   Sets the delimiter to use. Default depends on the dialect used.

skipinitialspace:
:   Set to `true` to ignore space directly after the delimiter. Default depends on the dialect used (usually `false`).

strict:
:   Set to `true` to error out on invalid CSV input.

## Converting to JSON

[JC](https://pypi.org/project/jc/) is a CLI tool and Python library which allows to interpret output of various CLI programs as JSON. It is also available as a filter in community.general. This filter needs the [jc Python library](https://pypi.org/project/jc/) installed on the controller.

```yaml+jinja
- name: Run 'ls' to list files in /
  command: ls /
  register: result

- name: Parse the ls output
  debug:
    msg: "{{ result.stdout | community.general.jc('ls') }}"
```

This produces:

```ansible-output
TASK [Run 'ls' to list files in /] ********************************************************
changed: [localhost]

TASK [Parse the ls output] ****************************************************************
ok: [localhost] => {
    "msg": [
        {
            "filename": "bin"
        },
        {
            "filename": "boot"
        },
        {
            "filename": "dev"
        },
        {
            "filename": "etc"
        },
        {
            "filename": "home"
        },
        {
            "filename": "lib"
        },
        {
            "filename": "proc"
        },
        {
            "filename": "root"
        },
        {
            "filename": "run"
        },
        {
            "filename": "tmp"
        }
    ]
}
```

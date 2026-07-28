---
collection: ansible
version: "8"
title: "community.general.from_csv filter – Converts CSV text input into list of dicts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/from_csv_filter.html
fetched_at: 2026-07-28T01:52:18+00:00
---
# community.general.from_csv filter – Converts CSV text input into list of dicts

> **Note:**
>
> This filter plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.from_csv`.

New in community.general 2.3.0

- [Synopsis](from_csv_filter.md#synopsis)
- [Input](from_csv_filter.md#input)
- [Keyword parameters](from_csv_filter.md#keyword-parameters)
- [Examples](from_csv_filter.md#examples)
- [Return Value](from_csv_filter.md#return-value)

## [Synopsis](from_csv_filter.md#id1)

- Converts CSV text input into list of dictionaries.

## [Input](from_csv_filter.md#id2)

This describes the input of the filter, the value before `| community.general.from_csv`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A string containing a CSV document. |

## [Keyword parameters](from_csv_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | community.general.from_csv(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **delimiter**  string | A one-character string used to separate fields.  When using this parameter, you change the default value used by `dialect`.  The default value depends on the dialect used. |
| **dialect**  string | The CSV dialect to use when parsing the CSV file.  Possible values include `excel`, `excel-tab` or `unix`.  **Default:** `"excel"` |
| **fieldnames**  list / elements=string | A list of field names for every column.  This is needed if the CSV does not have a header. |
| **skipinitialspace**  boolean | Whether to ignore any whitespaces immediately following the delimiter.  When using this parameter, you change the default value used by `dialect`.  The default value depends on the dialect used.  **Choices:**   - `false` - `true` |
| **strict**  boolean | Whether to raise an exception on bad CSV input.  When using this parameter, you change the default value used by `dialect`.  The default value depends on the dialect used.  **Choices:**   - `false` - `true` |

## [Examples](from_csv_filter.md#id4)

```yaml+jinja
- name: Parse a CSV file's contents
  ansible.builtin.debug:
    msg: >-
      {{ csv_data | community.general.from_csv(dialect='unix') }}
  vars:
    csv_data: |
      Column 1,Value
      foo,23
      bar,42
  # Produces the following list of dictionaries:
  #   {
  #     "Column 1": "foo",
  #     "Value": "23",
  #   },
  #   {
  #     "Column 1": "bar",
  #     "Value": "42",
  #   }
```

## [Return Value](from_csv_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | A list with one dictionary per row.  **Returned:** success |

### Authors

- Andrew Pantuso (@Ajpantuso)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

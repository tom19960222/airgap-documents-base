---
collection: ansible
version: "6"
title: "ansible.builtin.find module – Return a list of files based on specific criteria"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/find_module.html
fetched_at: 2026-07-27T16:44:00+00:00
---
# ansible.builtin.find module – Return a list of files based on specific criteria

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `find` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](find_module.md#synopsis)
- [Parameters](find_module.md#parameters)
- [Attributes](find_module.md#attributes)
- [See Also](find_module.md#see-also)
- [Examples](find_module.md#examples)
- [Return Values](find_module.md#return-values)

## [Synopsis](find_module.md#id1)

- Return a list of files based on specific criteria. Multiple criteria are AND’d together.
- For Windows targets, use the [ansible.windows.win_find](../windows/win_find_module.md#ansible-collections-ansible-windows-win-find-module) module instead.

## [Parameters](find_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **age**  string | Select files whose age is equal to or greater than the specified time.  Use a negative age to find files equal to or less than the specified time.  You can choose seconds, minutes, hours, days, or weeks by specifying the first letter of any of those words (e.g., “1w”). |
| **age_stamp**  string | Choose the file property against which we compare age.  Choices:   - `"atime"` - `"ctime"` - `"mtime"` ← (default) |
| **contains**  string | A regular expression or pattern which should be matched against the file content.  Works only when *file_type* is `file`. |
| **depth**  integer | Set the maximum number of levels to descend into.  Setting recurse to `no` will override this value, which is effectively depth 1.  Default is unlimited depth. |
| **excludes**  aliases: exclude  list / elements=string | One or more (shell or regex) patterns, which type is controlled by *use_regex* option.  Items whose basenames match an *excludes* pattern are culled from *patterns* matches. Multiple patterns can be specified using a list. |
| **file_type**  string | Type of file to select.  The ‘link’ and ‘any’ choices were added in Ansible 2.3.  Choices:   - `"any"` - `"directory"` - `"file"` ← (default) - `"link"` |
| **follow**  boolean | Set this to `yes` to follow symlinks in path for systems with python 2.6+.  Choices:   - `false` ← (default) - `true` |
| **get_checksum**  boolean | Set this to `yes` to retrieve a file’s SHA1 checksum.  Choices:   - `false` ← (default) - `true` |
| **hidden**  boolean | Set this to `yes` to include hidden files, otherwise they will be ignored.  Choices:   - `false` ← (default) - `true` |
| **paths**  aliases: name, path  list / elements=string / required | List of paths of directories to search. All paths must be fully qualified. |
| **patterns**  aliases: pattern  list / elements=string | One or more (shell or regex) patterns, which type is controlled by `use_regex` option.  The patterns restrict the list of files to be returned to those whose basenames match at least one of the patterns specified. Multiple patterns can be specified using a list.  The pattern is matched against the file base name, excluding the directory.  When using regexen, the pattern MUST match the ENTIRE file name, not just parts of it. So if you are looking to match all files ending in .default, you’d need to use `.*\.default` as a regexp and not just `\.default`.  This parameter expects a list, which can be either comma separated or YAML. If any of the patterns contain a comma, make sure to put them in a list to avoid splitting the patterns in undesirable ways.  Defaults to `*` when *use_regex=False*, or `.*` when *use_regex=True*.  Default: `[]` |
| **read_whole_file**  boolean  added in ansible-core 2.11 | When doing a `contains` search, determines whether the whole file should be read into memory or if the regex should be applied to the file line-by-line.  Setting this to `true` can have performance and memory implications for large files.  This uses `re.search(`) instead of `re.match(`).  Choices:   - `false` ← (default) - `true` |
| **recurse**  boolean | If target is a directory, recursively descend into the directory looking for files.  Choices:   - `false` ← (default) - `true` |
| **size**  string | Select files whose size is equal to or greater than the specified size.  Use a negative size to find files equal to or less than the specified size.  Unqualified values are in bytes but b, k, m, g, and t can be appended to specify bytes, kilobytes, megabytes, gigabytes, and terabytes, respectively.  Size is not evaluated for directories. |
| **use_regex**  boolean | If `no`, the patterns are file globs (shell).  If `yes`, they are python regexes.  Choices:   - `false` ← (default) - `true` |

## [Attributes](find_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full  since this action does not modify the target it just executes normally during check mode | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platform: posix | Target OS/families that can be operated against |

## [See Also](find_module.md#id4)

> **See also:**
>
> [ansible.windows.win_find](../windows/win_find_module.md#ansible-collections-ansible-windows-win-find-module)
> :   Return a list of files based on specific criteria.

## [Examples](find_module.md#id5)

```yaml+jinja
- name: Recursively find /tmp files older than 2 days
  ansible.builtin.find:
    paths: /tmp
    age: 2d
    recurse: yes

- name: Recursively find /tmp files older than 4 weeks and equal or greater than 1 megabyte
  ansible.builtin.find:
    paths: /tmp
    age: 4w
    size: 1m
    recurse: yes

- name: Recursively find /var/tmp files with last access time greater than 3600 seconds
  ansible.builtin.find:
    paths: /var/tmp
    age: 3600
    age_stamp: atime
    recurse: yes

- name: Find /var/log files equal or greater than 10 megabytes ending with .old or .log.gz
  ansible.builtin.find:
    paths: /var/log
    patterns: '*.old,*.log.gz'
    size: 10m

# Note that YAML double quotes require escaping backslashes but yaml single quotes do not.
- name: Find /var/log files equal or greater than 10 megabytes ending with .old or .log.gz via regex
  ansible.builtin.find:
    paths: /var/log
    patterns: "^.*?\\.(?:old|log\\.gz)$"
    size: 10m
    use_regex: yes

- name: Find /var/log all directories, exclude nginx and mysql
  ansible.builtin.find:
    paths: /var/log
    recurse: no
    file_type: directory
    excludes: 'nginx,mysql'

# When using patterns that contain a comma, make sure they are formatted as lists to avoid splitting the pattern
- name: Use a single pattern that contains a comma formatted as a list
  ansible.builtin.find:
    paths: /var/log
    file_type: file
    use_regex: yes
    patterns: ['^_[0-9]{2,4}_.*.log$']

- name: Use multiple patterns that contain a comma formatted as a YAML list
  ansible.builtin.find:
    paths: /var/log
    file_type: file
    use_regex: yes
    patterns:
      - '^_[0-9]{2,4}_.*.log$'
      - '^[a-z]{1,5}_.*log$'
```

## [Return Values](find_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **examined**  integer | Number of filesystem objects looked at  Returned: success  Sample: `34` |
| **files**  list / elements=string | All matches found with the specified criteria (see stat module for full output of each dictionary)  Returned: success  Sample: `[{"...": "...", "checksum": "16fac7be61a6e4591a33ef4b729c5c3302307523", "mode": "0644", "path": "/var/tmp/test1"}, {"...": "...", "path": "/var/tmp/test2"}]` |
| **matched**  integer | Number of matches  Returned: success  Sample: `14` |
| **skipped_paths**  dictionary  added in ansible-core 2.12 | skipped paths and reasons they were skipped  Returned: success  Sample: `{"/laskdfj": "'/laskdfj' is not a directory"}` |

### Authors

- Brian Coca (@bcoca)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)

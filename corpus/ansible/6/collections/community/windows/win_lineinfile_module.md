---
collection: ansible
version: "6"
title: "community.windows.win_lineinfile module – Ensure a particular line is in a file, or replace an existing line using a back-referenced regular expression"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_lineinfile_module.html
fetched_at: 2026-07-27T17:23:34+00:00
---
# community.windows.win_lineinfile module – Ensure a particular line is in a file, or replace an existing line using a back-referenced regular expression

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_lineinfile`.

- [Synopsis](win_lineinfile_module.md#synopsis)
- [Parameters](win_lineinfile_module.md#parameters)
- [See Also](win_lineinfile_module.md#see-also)
- [Examples](win_lineinfile_module.md#examples)
- [Return Values](win_lineinfile_module.md#return-values)

## [Synopsis](win_lineinfile_module.md#id1)

- This module will search a file for a line, and ensure that it is present or absent.
- This is primarily useful when you want to change a single line in a file only.

## [Parameters](win_lineinfile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backrefs**  boolean | Used with `state=present`. If set, line can contain backreferences (both positional and named) that will get populated if the `regexp` matches. This flag changes the operation of the module slightly; `insertbefore` and `insertafter` will be ignored, and if the `regexp` doesn’t match anywhere in the file, the file will be left unchanged.  If the `regexp` does match, the last matching line will be replaced by the expanded line parameter.  Choices:   - `false` ← (default) - `true` |
| **backup**  boolean | Determine whether a backup should be created.  When set to `yes`, create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  Choices:   - `false` ← (default) - `true` |
| **create**  boolean | Used with `state=present`. If specified, the file will be created if it does not already exist. By default it will fail if the file is missing.  Choices:   - `false` ← (default) - `true` |
| **encoding**  string | Specifies the encoding of the source text file to operate on (and thus what the output encoding will be). The default of `auto` will cause the module to auto-detect the encoding of the source file and ensure that the modified file is written with the same encoding.  An explicit encoding can be passed as a string that is a valid value to pass to the .NET framework System.Text.Encoding.GetEncoding() method - see <https://msdn.microsoft.com/en-us/library/system.text.encoding%28v%3Dvs.110%29.aspx>.  This is mostly useful with `create=yes` if you want to create a new file with a specific encoding. If `create=yes` is specified without a specific encoding, the default encoding (UTF-8, no BOM) will be used.  Default: `"auto"` |
| **insertafter**  string | Used with `state=present`. If specified, the line will be inserted after the last match of specified regular expression. A special value is available; `EOF` for inserting the line at the end of the file.  If specified regular expression has no matches, EOF will be used instead. May not be used with `backrefs`.  Choices:   - `"EOF"` ← (default) - `"*regex*"` |
| **insertbefore**  string | Used with `state=present`. If specified, the line will be inserted before the last match of specified regular expression. A value is available; `BOF` for inserting the line at the beginning of the file.  If specified regular expression has no matches, the line will be inserted at the end of the file. May not be used with `backrefs`.  Choices:   - `"BOF"` - `"*regex*"` |
| **line**  string | Required for `state=present`. The line to insert/replace into the file. If `backrefs` is set, may contain backreferences that will get expanded with the `regexp` capture groups if the regexp matches.  Be aware that the line is processed first on the controller and thus is dependent on yaml quoting rules. Any double quoted line will have control characters, such as ‘\r\n’, expanded. To print such characters literally, use single or no quotes. |
| **newline**  string | Specifies the line separator style to use for the modified file. This defaults to the windows line separator (`\r\n`). Note that the indicated line separator will be used for file output regardless of the original line separator that appears in the input file.  Choices:   - `"unix"` - `"windows"` ← (default) |
| **path**  aliases: dest, destfile, name  path / required | The path of the file to modify.  Note that the Windows path delimiter `\` must be escaped as `\\` when the line is double quoted. |
| **regex**  aliases: regexp  string | The regular expression to look for in every line of the file. For `state=present`, the pattern to replace if found; only the last line found will be replaced. For `state=absent`, the pattern of the line to remove. Uses .NET compatible regular expressions; see <https://msdn.microsoft.com/en-us/library/hs600312%28v%3Dvs.110%29.aspx>. |
| **state**  string | Whether the line should be there or not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **validate**  string | Validation to run before copying into place. Use %s in the command to indicate the current file to validate.  The command is passed securely so shell features like expansion and pipes won’t work. |

## [See Also](win_lineinfile_module.md#id3)

> **See also:**
>
> [ansible.builtin.assemble](../../ansible/builtin/assemble_module.md#ansible-collections-ansible-builtin-assemble-module)
> :   Assemble configuration files from fragments.
>
> [ansible.builtin.lineinfile](../../ansible/builtin/lineinfile_module.md#ansible-collections-ansible-builtin-lineinfile-module)
> :   Manage lines in text files.

## [Examples](win_lineinfile_module.md#id4)

```yaml+jinja
- name: Insert path without converting \r\n
  community.windows.win_lineinfile:
    path: c:\file.txt
    line: c:\return\new

- community.windows.win_lineinfile:
    path: C:\Temp\example.conf
    regex: '^name='
    line: 'name=JohnDoe'

- community.windows.win_lineinfile:
    path: C:\Temp\example.conf
    regex: '^name='
    state: absent

- community.windows.win_lineinfile:
    path: C:\Temp\example.conf
    regex: '^127\.0\.0\.1'
    line: '127.0.0.1 localhost'

- community.windows.win_lineinfile:
    path: C:\Temp\httpd.conf
    regex: '^Listen '
    insertafter: '^#Listen '
    line: Listen 8080

- community.windows.win_lineinfile:
    path: C:\Temp\services
    regex: '^# port for http'
    insertbefore: '^www.*80/tcp'
    line: '# port for http by default'

- name: Create file if it doesn't exist with a specific encoding
  community.windows.win_lineinfile:
    path: C:\Temp\utf16.txt
    create: yes
    encoding: utf-16
    line: This is a utf-16 encoded file

- name: Add a line to a file and ensure the resulting file uses unix line separators
  community.windows.win_lineinfile:
    path: C:\Temp\testfile.txt
    line: Line added to file
    newline: unix

- name: Update a line using backrefs
  community.windows.win_lineinfile:
    path: C:\Temp\example.conf
    backrefs: yes
    regex: '(^name=)'
    line: '$1JohnDoe'
```

## [Return Values](win_lineinfile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup**  string | Name of the backup file that was created.  This is now deprecated, use `backup_file` instead.  Returned: if backup=yes  Sample: `"C:\\Path\\To\\File.txt.11540.20150212-220915.bak"` |
| **backup_file**  string | Name of the backup file that was created.  Returned: if backup=yes  Sample: `"C:\\Path\\To\\File.txt.11540.20150212-220915.bak"` |

### Authors

- Brian Lloyd (@brianlloyd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)

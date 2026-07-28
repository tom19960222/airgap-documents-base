---
collection: ansible
version: "8"
title: "ansible.windows.win_template module – Template a file out to a remote server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_template_module.html
fetched_at: 2026-07-28T01:10:51+00:00
---
# ansible.windows.win_template module – Template a file out to a remote server

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_template`.

- [Synopsis](win_template_module.md#synopsis)
- [Parameters](win_template_module.md#parameters)
- [Notes](win_template_module.md#notes)
- [See Also](win_template_module.md#see-also)
- [Examples](win_template_module.md#examples)
- [Return Values](win_template_module.md#return-values)

## [Synopsis](win_template_module.md#id1)

- Templates are processed by the [Jinja2 templating language](http://jinja.pocoo.org/docs/).
- Documentation on the template formatting can be found in the [Template Designer Documentation](http://jinja.pocoo.org/docs/templates/).
- Additional variables listed below can be used in templates.
- `ansible_managed` (configurable via the `defaults` section of `ansible.cfg`) contains a string which can be used to describe the template name, host, modification time of the template file and the owner uid.
- `template_host` contains the node name of the template’s machine.
- `template_uid` is the numeric user id of the owner.
- `template_path` is the path of the template.
- `template_fullpath` is the absolute path of the template.
- `template_destpath` is the path of the template on the remote system (added in 2.8).
- `template_run_date` is the date that the template was rendered.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](win_template_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | Determine whether a backup should be created.  When set to `true`, create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  **Choices:**   - `false` ← (default) - `true` |
| **block_end_string**  string | The string marking the end of a block.  **Default:** `"%}"` |
| **block_start_string**  string | The string marking the beginning of a block.  **Default:** `"{%"` |
| **dest**  path / required | Location to render the template to on the remote machine. |
| **force**  boolean | Determine when the file is being transferred if the destination already exists.  When set to `true`, replace the remote file when contents are different than the source.  When set to `false`, the file will only be transferred if the destination does not exist.  **Choices:**   - `false` - `true` ← (default) |
| **lstrip_blocks**  boolean | Determine when leading spaces and tabs should be stripped.  When set to `true` leading spaces and tabs are stripped from the start of a line to a block.  This functionality requires Jinja 2.7 or newer.  **Choices:**   - `false` ← (default) - `true` |
| **newline_sequence**  string | Specify the newline sequence to use for templating files.  **Choices:**   - `"\\n"` - `"\\r"` - `"\\r\\n"` ← (default) |
| **output_encoding**  string | Overrides the encoding used to write the template file defined by `dest`.  It defaults to `utf-8`, but any encoding supported by python can be used.  The source template file must always be encoded using `utf-8`, for homogeneity.  **Default:** `"utf-8"` |
| **src**  path / required | Path of a Jinja2 formatted template on the Ansible controller.  This can be a relative or an absolute path.  The file must be encoded with `utf-8` but *output_encoding* can be used to control the encoding of the output template. |
| **trim_blocks**  boolean | Determine when newlines should be removed from blocks.  When set to `true` the first newline after a block is removed (block, not variable tag!).  **Choices:**   - `false` - `true` ← (default) |
| **variable_end_string**  string | The string marking the end of a print statement.  **Default:** `"}}"` |
| **variable_start_string**  string | The string marking the beginning of a print statement.  **Default:** `"{{"` |

## [Notes](win_template_module.md#id3)

> **Note:**
>
> - Including a string that uses a date in the template will result in the template being marked ‘changed’ each time.
> - Also, you can override jinja2 settings by adding a special header to template file. i.e. `#jinja2:variable_start_string:'[%', variable_end_string:'%]', trim_blocks: False` which changes the variable interpolation markers to `[% var %]` instead of `{{ var }}`. This is the best way to prevent evaluation of things that look like, but should not be Jinja2.
> - Using raw/endraw in Jinja2 will not work as you expect because templates in Ansible are recursively evaluated.
> - To find Byte Order Marks in files, use `Format-Hex <file> -Count 16` on Windows, and use `od -a -t x1 -N 16 <file>` on Linux.
> - Beware fetching files from windows machines when creating templates because certain tools, such as Powershell ISE, and regedit’s export facility add a Byte Order Mark as the first character of the file, which can cause tracebacks.
> - You can use the [ansible.windows.win_copy](win_copy_module.md#ansible-collections-ansible-windows-win-copy-module) module with the `content:` option if you prefer the template inline, as part of the playbook.
> - For Linux you can use [ansible.builtin.template](../builtin/template_module.md#ansible-collections-ansible-builtin-template-module) which uses ‘\\n’ as `newline_sequence` by default.

## [See Also](win_template_module.md#id4)

> **See also:**
>
> [ansible.windows.win_copy](win_copy_module.md#ansible-collections-ansible-windows-win-copy-module)
> :   Copies files to remote locations on windows hosts.
>
> [ansible.builtin.copy](../builtin/copy_module.md#ansible-collections-ansible-builtin-copy-module)
> :   Copy files to remote locations.
>
> [ansible.builtin.template](../builtin/template_module.md#ansible-collections-ansible-builtin-template-module)
> :   Template a file out to a target host.

## [Examples](win_template_module.md#id5)

```yaml+jinja
- name: Create a file from a Jinja2 template
  ansible.windows.win_template:
    src: /mytemplates/file.conf.j2
    dest: C:\Temp\file.conf

- name: Create a Unix-style file from a Jinja2 template
  ansible.windows.win_template:
    src: unix/config.conf.j2
    dest: C:\share\unix\config.conf
    newline_sequence: '\n'
    backup: true
```

## [Return Values](win_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | Name of the backup file that was created.  **Returned:** if backup=true  **Sample:** `"C:\\Path\\To\\File.txt.11540.20150212-220915.bak"` |

### Authors

- Jon Hawkesworth (@jhawkesworth)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)

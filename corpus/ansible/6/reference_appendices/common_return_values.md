---
collection: ansible
version: "6"
title: "Return Values"
source_url: https://docs.ansible.com/projects/ansible/6/reference_appendices/common_return_values.html
fetched_at: 2026-07-27T16:39:30+00:00
---
# [Return Values](common_return_values.md#id1)

Topics

- [Return Values](common_return_values.md#return-values)

  - [Common](common_return_values.md#common)

    - [backup_file](common_return_values.md#backup-file)
    - [changed](common_return_values.md#changed)
    - [diff](common_return_values.md#diff)
    - [failed](common_return_values.md#failed)
    - [invocation](common_return_values.md#invocation)
    - [msg](common_return_values.md#msg)
    - [rc](common_return_values.md#rc)
    - [results](common_return_values.md#results)
    - [skipped](common_return_values.md#skipped)
    - [stderr](common_return_values.md#stderr)
    - [stderr_lines](common_return_values.md#stderr-lines)
    - [stdout](common_return_values.md#stdout)
    - [stdout_lines](common_return_values.md#stdout-lines)
  - [Internal use](common_return_values.md#internal-use)

    - [ansible_facts](common_return_values.md#ansible-facts)
    - [exception](common_return_values.md#exception)
    - [warnings](common_return_values.md#warnings)
    - [deprecations](common_return_values.md#deprecations)

Ansible modules normally return a data structure that can be registered into a variable, or seen directly when output by
the ansible program. Each module can optionally document its own unique return values (visible through ansible-doc and on the [main docsite](../index.md#ansible-documentation)).

This document covers return values common to all modules.

> **Note:**
>
> Some of these keys might be set by Ansible itself once it processes the module’s return information.

## [Common](common_return_values.md#id2)

### [backup_file](common_return_values.md#id3)

For those modules that implement backup=no|yes when manipulating files, a path to the backup file created.

> ```console
> "backup_file": "./foo.txt.32729.2020-07-30@06:24:19~"
> ```

### [changed](common_return_values.md#id4)

A boolean indicating if the task had to make changes to the target or delegated host.

> ```console
> "changed": true
> ```

### [diff](common_return_values.md#id5)

Information on differences between the previous and current state. Often a dictionary with entries `before` and `after`, which will then be formatted by the callback plugin to a diff view.

> ```console
> "diff": [
>         {
>             "after": "",
>             "after_header": "foo.txt (content)",
>             "before": "",
>             "before_header": "foo.txt (content)"
>         },
>         {
>             "after_header": "foo.txt (file attributes)",
>             "before_header": "foo.txt (file attributes)"
>         }
> ```

### [failed](common_return_values.md#id6)

A boolean that indicates if the task was failed or not.

> ```console
> "failed": false
> ```

### [invocation](common_return_values.md#id7)

Information on how the module was invoked.

> ```console
> "invocation": {
>         "module_args": {
>             "_original_basename": "foo.txt",
>             "attributes": null,
>             "backup": true,
>             "checksum": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
>             "content": null,
>             "delimiter": null,
>             "dest": "./foo.txt",
>             "directory_mode": null,
>             "follow": false,
>             "force": true,
>             "group": null,
>             "local_follow": null,
>             "mode": "666",
>             "owner": null,
>             "regexp": null,
>             "remote_src": null,
>             "selevel": null,
>             "serole": null,
>             "setype": null,
>             "seuser": null,
>             "src": "/Users/foo/.ansible/tmp/ansible-tmp-1596115458.110205-105717464505158/source",
>             "unsafe_writes": null,
>             "validate": null
>         }
> ```

### [msg](common_return_values.md#id8)

A string with a generic message relayed to the user.

> ```console
> "msg": "line added"
> ```

### [rc](common_return_values.md#id9)

Some modules execute command line utilities or are geared for executing commands directly (raw, shell, command, and so on), this field contains ‘return code’ of these utilities.

> ```console
> "rc": 257
> ```

### [results](common_return_values.md#id10)

If this key exists, it indicates that a loop was present for the task and that it contains a list of the normal module ‘result’ per item.

> ```console
> "results": [
>     {
>         "ansible_loop_var": "item",
>         "backup": "foo.txt.83170.2020-07-30@07:03:05~",
>         "changed": true,
>         "diff": [
>             {
>                 "after": "",
>                 "after_header": "foo.txt (content)",
>                 "before": "",
>                 "before_header": "foo.txt (content)"
>             },
>             {
>                 "after_header": "foo.txt (file attributes)",
>                 "before_header": "foo.txt (file attributes)"
>             }
>         ],
>         "failed": false,
>         "invocation": {
>             "module_args": {
>                 "attributes": null,
>                 "backrefs": false,
>                 "backup": true
>             }
>         },
>         "item": "foo",
>         "msg": "line added"
>     },
>     {
>         "ansible_loop_var": "item",
>         "backup": "foo.txt.83187.2020-07-30@07:03:05~",
>         "changed": true,
>         "diff": [
>             {
>                 "after": "",
>                 "after_header": "foo.txt (content)",
>                 "before": "",
>                 "before_header": "foo.txt (content)"
>             },
>             {
>                 "after_header": "foo.txt (file attributes)",
>                 "before_header": "foo.txt (file attributes)"
>             }
>         ],
>         "failed": false,
>         "invocation": {
>             "module_args": {
>                 "attributes": null,
>                 "backrefs": false,
>                 "backup": true
>             }
>         },
>         "item": "bar",
>         "msg": "line added"
>     }
>     ]
> ```

### [skipped](common_return_values.md#id11)

A boolean that indicates if the task was skipped or not

> ```console
> "skipped": true
> ```

### [stderr](common_return_values.md#id12)

Some modules execute command line utilities or are geared for executing commands directly (raw, shell, command, and so on), this field contains the error output of these utilities.

> ```console
> "stderr": "ls: foo: No such file or directory"
> ```

### [stderr_lines](common_return_values.md#id13)

When stderr is returned we also always provide this field which is a list of strings, one item per line from the original.

> ```console
> "stderr_lines": [
>         "ls: doesntexist: No such file or directory"
>         ]
> ```

### [stdout](common_return_values.md#id14)

Some modules execute command line utilities or are geared for executing commands directly (raw, shell, command, and so on). This field contains the normal output of these utilities.

> ```console
> "stdout": "foo!"
> ```

### [stdout_lines](common_return_values.md#id15)

When stdout is returned, Ansible always provides a list of strings, each containing one item per line from the original output.

> ```console
> "stdout_lines": [
> "foo!"
> ]
> ```

## [Internal use](common_return_values.md#id16)

These keys can be added by modules but will be removed from registered variables; they are ‘consumed’ by Ansible itself.

### [ansible_facts](common_return_values.md#id17)

This key should contain a dictionary which will be appended to the facts assigned to the host. These will be directly accessible and don’t require using a registered variable.

### [exception](common_return_values.md#id18)

This key can contain traceback information caused by an exception in a module. It will only be displayed on high verbosity (-vvv).

### [warnings](common_return_values.md#id19)

This key contains a list of strings that will be presented to the user.

### [deprecations](common_return_values.md#id20)

This key contains a list of dictionaries that will be presented to the user. Keys of the dictionaries are msg and version, values are string, value for the version key can be an empty string.

> **See also:**
>
> [Collection Index](../collections/index.md#list-of-collections)
> :   Browse existing collections, modules, and plugins
>
> [GitHub modules directory](https://github.com/ansible/ansible/tree/devel/lib/ansible/modules)
> :   Browse source of core and extras modules
>
> [Mailing List](https://groups.google.com/group/ansible-devel)
> :   Development mailing list
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels

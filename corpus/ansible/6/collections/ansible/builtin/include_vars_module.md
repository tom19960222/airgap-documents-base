---
collection: ansible
version: "6"
title: "ansible.builtin.include_vars module – Load variables from files, dynamically within a task"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/include_vars_module.html
fetched_at: 2026-07-27T16:42:20+00:00
---
# ansible.builtin.include_vars module – Load variables from files, dynamically within a task

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `include_vars` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](include_vars_module.md#synopsis)
- [Parameters](include_vars_module.md#parameters)
- [Attributes](include_vars_module.md#attributes)
- [See Also](include_vars_module.md#see-also)
- [Examples](include_vars_module.md#examples)
- [Return Values](include_vars_module.md#return-values)

## [Synopsis](include_vars_module.md#id1)

- Loads YAML/JSON variables dynamically from a file or directory, recursively, during task runtime.
- If loading a directory, the files are sorted alphabetically before being loaded.
- This module is also supported for Windows targets.
- To assign included variables to a different host than `inventory_hostname`, use `delegate_to` and set `delegate_facts=yes`.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](include_vars_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **depth**  integer | When using `dir`, this module will, by default, recursively go through each sub directory and load up the variables. By explicitly setting the depth, this module will only go as deep as the depth.  Default: `0` |
| **dir**  path | The directory name from which the variables should be loaded.  If the path is relative and the task is inside a role, it will look inside the role’s vars/ subdirectory.  If the path is relative and not inside a role, it will be parsed relative to the playbook. |
| **extensions**  list / elements=string | List of file extensions to read when using `dir`.  Default: `["json", "yaml", "yml"]` |
| **file**  path | The file name from which variables should be loaded.  If the path is relative, it will look for the file in vars/ subdirectory of a role or relative to playbook. |
| **files_matching**  string | Limit the files that are loaded within any directory to this regular expression. |
| **free-form**  string | This module allows you to specify the ‘file’ option directly without any other options.  There is no ‘free-form’ option, this is just an indicator, see example below. |
| **hash_behaviour**  string  added in ansible-core 2.12 | If set to `merge`, merges existing hash variables instead of overwriting them.  If omitted `null`, the behavior falls back to the global *hash_behaviour* configuration.  Choices:   - `"replace"` - `"merge"` |
| **ignore_files**  list / elements=string | List of file names to ignore. |
| **ignore_unknown_extensions**  boolean  added in Ansible 2.7 | Ignore unknown file extensions within the directory.  This allows users to specify a directory containing vars files that are intermingled with non-vars files extension types (e.g. a directory with a README in it and vars files).  Choices:   - `false` ← (default) - `true` |
| **name**  string | The name of a variable into which assign the included vars.  If omitted (null) they will be made top level vars. |

## [Attributes](include_vars_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: partial  While the action plugin does do some of the work it relies on the core engine to actually create the variables, that part cannot be overriden | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | Support: none | Supports being used with the `async` keyword |
| **become** | Support: none | Is usable alongside become keywords |
| **bypass_host_loop** | Support: none | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **bypass_task_loop** | Support: none | These tasks ignore the `loop` and `with_` keywords |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | Support: none | Uses the target’s configured connection information to execute code on it |
| **core** | Support: partial  While parts of this action are implemented in core, other parts are still available as normal plugins and can be partially overridden | This is a ‘core engine’ feature and is not implemented like most task actions, so it is not overridable in any way via the plugin system. |
| **delegation** | Support: partial  while variable assignment can be delegated to a different host the execution context is always the current inventory_hostname  connection variables, if set at all, would reflect the host it would target, even if we are not connecting at all in this case | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **ignore_conditional** | Support: none | The action is not subject to conditional execution so it will ignore the `when:` keyword |
| **platform** | Platforms: all | Target OS/families that can be operated against |
| **tags** | Support: full | Allows for the ‘tags’ keyword to control the selection of this action for execution |
| **until** | Support: full | Denotes if this action objeys until/retry/poll keywords |

## [See Also](include_vars_module.md#id4)

> **See also:**
>
> [ansible.builtin.set_fact](set_fact_module.md#ansible-collections-ansible-builtin-set-fact-module)
> :   Set host variable(s) and fact(s).
>
> [Controlling where tasks run: delegation and local actions](../../../user_guide/playbooks_delegation.md#playbooks-delegation)
> :   More information related to task delegation.

## [Examples](include_vars_module.md#id5)

```yaml+jinja
- name: Include vars of stuff.yaml into the 'stuff' variable (2.2).
  ansible.builtin.include_vars:
    file: stuff.yaml
    name: stuff

- name: Conditionally decide to load in variables into 'plans' when x is 0, otherwise do not. (2.2)
  ansible.builtin.include_vars:
    file: contingency_plan.yaml
    name: plans
  when: x == 0

- name: Load a variable file based on the OS type, or a default if not found. Using free-form to specify the file.
  ansible.builtin.include_vars: "{{ lookup('ansible.builtin.first_found', params) }}"
  vars:
    params:
      files:
        - '{{ansible_distribution}}.yaml'
        - '{{ansible_os_family}}.yaml'
        - default.yaml
      paths:
        - 'vars'

- name: Bare include (free-form)
  ansible.builtin.include_vars: myvars.yaml

- name: Include all .json and .jsn files in vars/all and all nested directories (2.3)
  ansible.builtin.include_vars:
    dir: vars/all
    extensions:
      - 'json'
      - 'jsn'

- name: Include all default extension files in vars/all and all nested directories and save the output in test. (2.2)
  ansible.builtin.include_vars:
    dir: vars/all
    name: test

- name: Include default extension files in vars/services (2.2)
  ansible.builtin.include_vars:
    dir: vars/services
    depth: 1

- name: Include only files matching bastion.yaml (2.2)
  ansible.builtin.include_vars:
    dir: vars
    files_matching: bastion.yaml

- name: Include all .yaml files except bastion.yaml (2.3)
  ansible.builtin.include_vars:
    dir: vars
    ignore_files:
      - 'bastion.yaml'
    extensions:
      - 'yaml'

- name: Ignore warnings raised for files with unknown extensions while loading (2.7)
  ansible.builtin.include_vars:
    dir: vars
    ignore_unknown_extensions: True
    extensions:
      - ''
      - 'yaml'
      - 'yml'
      - 'json'
```

## [Return Values](include_vars_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_included_var_files**  list / elements=string | A list of files that were successfully included  Returned: success  Sample: `["/path/to/file.json", "/path/to/file.yaml"]` |

### Authors

- Allen Sanabria (@linuxdynasty)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)

---
collection: ansible
version: "8"
title: "ansible.builtin.validate_argument_spec module – Validate role argument specs."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/validate_argument_spec_module.html
fetched_at: 2026-07-28T01:07:48+00:00
---
# ansible.builtin.validate_argument_spec module – Validate role argument specs.

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `validate_argument_spec` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.validate_argument_spec` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

New in ansible-core 2.11

- [Synopsis](validate_argument_spec_module.md#synopsis)
- [Parameters](validate_argument_spec_module.md#parameters)
- [Attributes](validate_argument_spec_module.md#attributes)
- [Examples](validate_argument_spec_module.md#examples)
- [Return Values](validate_argument_spec_module.md#return-values)

## [Synopsis](validate_argument_spec_module.md#id1)

- This module validates role arguments with a defined argument specification.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](validate_argument_spec_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **argument_spec**  string / required | A dictionary like AnsibleModule argument_spec. See [argument spec definition](../../../dev_guide/developing_program_flow_modules.md#argument-spec) |
| **provided_arguments**  string | A dictionary of the arguments that will be validated according to argument_spec |

## [Attributes](validate_argument_spec_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **none** | Supports being used with the `async` keyword |
| **become** | **Support:** **none** | Is usable alongside become keywords |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | **Support:** **none** | Uses the target’s configured connection information to execute code on it |
| **delegation** | **Support:** **none** | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against |

## [Examples](validate_argument_spec_module.md#id4)

```yaml+jinja
- name: verify vars needed for this task file are present when included
  ansible.builtin.validate_argument_spec:
        argument_spec: '{{required_data}}'
  vars:
    required_data:
        # unlike spec file, just put the options in directly
        stuff:
            description: stuff
            type: str
            choices: ['who', 'knows', 'what']
            default: what
        but:
            description: i guess we need one
            type: str
            required: true

- name: verify vars needed for this task file are present when included, with spec from a spec file
  ansible.builtin.validate_argument_spec:
        argument_spec: "{{(lookup('ansible.builtin.file', 'myargspec.yml') | from_yaml )['specname']['options']}}"

- name: verify vars needed for next include and not from inside it, also with params i'll only define there
  block:
    - ansible.builtin.validate_argument_spec:
        argument_spec: "{{lookup('ansible.builtin.file', 'nakedoptions.yml'}}"
        provided_arguments:
            but: "that i can define on the include itself, like in it's `vars:` keyword"

    - name: the include itself
      vars:
        stuff: knows
        but: nobuts!
```

## [Return Values](validate_argument_spec_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **argument_errors**  list / elements=string | A list of arg validation errors.  **Returned:** failure  **Sample:** `["error message 1", "error message 2"]` |
| **argument_spec_data**  dictionary | A dict of the data from the ‘argument_spec’ arg.  **Returned:** failure  **Sample:** `{"some_arg": {"type": "str"}, "some_other_arg": {"required": true, "type": "int"}}` |
| **validate_args_context**  dictionary | A dict of info about where validate_args_spec was used  **Returned:** always  **Sample:** `{"argument_spec_name": "main", "name": "my_role", "path": "/home/user/roles/my_role/", "type": "role"}` |

### Authors

- Ansible Core Team

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)

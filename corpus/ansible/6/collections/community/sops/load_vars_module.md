---
collection: ansible
version: "6"
title: "community.sops.load_vars module – Load sops-encrypted variables from files, dynamically within a task"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/sops/load_vars_module.html
fetched_at: 2026-07-27T17:21:11+00:00
---
# community.sops.load_vars module – Load sops-encrypted variables from files, dynamically within a task

> **Note:**
>
> This module is part of the [community.sops collection](https://galaxy.ansible.com/community/sops) (version 1.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.sops`.
>
> To use it in a playbook, specify: `community.sops.load_vars`.

New in community.sops 0.1.0

- [Synopsis](load_vars_module.md#synopsis)
- [Parameters](load_vars_module.md#parameters)
- [Attributes](load_vars_module.md#attributes)
- [See Also](load_vars_module.md#see-also)
- [Examples](load_vars_module.md#examples)
- [Return Values](load_vars_module.md#return-values)

## [Synopsis](load_vars_module.md#id1)

- Loads sops-encrypted YAML/JSON variables dynamically from a file during task runtime.
- To assign included variables to a different host than `inventory_hostname`, use `delegate_to` and set `delegate_facts=true`.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](load_vars_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **age_key**  string  added in community.sops 1.4.0 | One or more age private keys that can be used to decrypt encrypted files.  Will be set as the `SOPS_AGE_KEY` environment variable when calling sops. |
| **age_keyfile**  path  added in community.sops 1.4.0 | The file containing the age private keys that sops can use to decrypt encrypted files.  Will be set as the `SOPS_AGE_KEY_FILE` environment variable when calling sops.  By default, sops looks for `sops/age/keys.txt` inside your user configuration directory. |
| **aws_access_key_id**  string  added in community.sops 1.0.0 | The AWS access key ID to use for requests to AWS.  Sets the environment variable `AWS_ACCESS_KEY_ID` for the sops call. |
| **aws_profile**  string  added in community.sops 1.0.0 | The AWS profile to use for requests to AWS.  This corresponds to the sops `--aws-profile` option. |
| **aws_secret_access_key**  string  added in community.sops 1.0.0 | The AWS secret access key to use for requests to AWS.  Sets the environment variable `AWS_SECRET_ACCESS_KEY` for the sops call. |
| **aws_session_token**  string  added in community.sops 1.0.0 | The AWS session token to use for requests to AWS.  Sets the environment variable `AWS_SESSION_TOKEN` for the sops call. |
| **config_path**  path  added in community.sops 1.0.0 | Path to the sops configuration file.  If not set, sops will recursively search for the config file starting at the file that is encrypted or decrypted.  This corresponds to the sops `--config` option. |
| **enable_local_keyservice**  boolean  added in community.sops 1.0.0 | Tell sops to use local key service.  This corresponds to the sops `--enable-local-keyservice` option.  Choices:   - `false` ← (default) - `true` |
| **expressions**  string | This option controls how Jinja2 expressions in values in the loaded file are handled.  If set to `ignore`, expressions will not be evaluated, but treated as regular strings.  If set to `evaluate-on-load`, expressions will be evaluated on execution of this module, in other words, when the file is loaded.  Unfortunately, there is no way for non-core modules to handle expressions “unsafe”, in other words, evaluate them only on use. This can only achieved by [ansible.builtin.include_vars](../../ansible/builtin/include_vars_module.md#ansible-collections-ansible-builtin-include-vars-module), which unfortunately cannot handle sops-encrypted files.  Choices:   - `"ignore"` ← (default) - `"evaluate-on-load"` |
| **file**  path | The file name from which variables should be loaded.  If the path is relative, it will look for the file in `vars/` subdirectory of a role or relative to playbook. |
| **keyservice**  list / elements=string  added in community.sops 1.0.0 | Specify key services to use next to the local one.  A key service must be specified in the form `protocol://address`, for example `tcp://myserver.com:5000`.  This corresponds to the sops `--keyservice` option. |
| **name**  string | The name of a variable into which assign the included vars.  If omitted (`null`) they will be made top level vars. |
| **sops_binary**  path  added in community.sops 1.0.0 | Path to the sops binary.  By default uses `sops`. |

## [Attributes](load_vars_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: full | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller. |
| **async** | Support: none  This action runs completely on the controller. | Supports being used with the `async` keyword. |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **facts** | Support: full | Action returns an `ansible_facts` dictionary that will update existing host facts. |

## [See Also](load_vars_module.md#id4)

> **See also:**
>
> [ansible.builtin.set_fact](../../ansible/builtin/set_fact_module.md#ansible-collections-ansible-builtin-set-fact-module)
> :   Set host variable(s) and fact(s).
>
> [ansible.builtin.include_vars](../../ansible/builtin/include_vars_module.md#ansible-collections-ansible-builtin-include-vars-module)
> :   Load variables from files, dynamically within a task.
>
> [Controlling where tasks run: delegation and local actions](../../../user_guide/playbooks_delegation.md#playbooks-delegation)
> :   More information related to task delegation.
>
> [community.sops.sops lookup](sops_lookup.md#ansible-collections-community-sops-sops-lookup)
> :   The sops lookup can be used decrypt sops-encrypted files.
>
> community.sops.decrypt filter
> :   The decrypt filter can be used to descrypt sops-encrypted in-memory data.
>
> [community.sops.sops vars plugin](sops_vars.md#ansible-collections-community-sops-sops-vars)
> :   The sops vars plugin can be used to load sops-encrypted host or group variables.

## [Examples](load_vars_module.md#id5)

```yaml+jinja
- name: Include variables of stuff.sops.yaml into the 'stuff' variable
  community.sops.load_vars:
    file: stuff.sops.yaml
    name: stuff
    expressions: evaluate-on-load  # interpret Jinja2 expressions in stuf.sops.yaml on load-time!

- name: Conditionally decide to load in variables into 'plans' when x is 0, otherwise do not
  community.sops.load_vars:
    file: contingency_plan.sops.yaml
    name: plans
    expressions: ignore  # do not interpret possible Jinja2 expressions
  when: x == 0

- name: Load variables into the global namespace
  community.sops.load_vars:
    file: contingency_plan.sops.yaml
```

## [Return Values](load_vars_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_included_var_files**  list / elements=string | A list of files that were successfully included  Returned: success  Sample: `["/path/to/file.sops.yaml"]` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.sops/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.sops)
[Submit a bug report](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-sops)

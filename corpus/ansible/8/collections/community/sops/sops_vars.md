---
collection: ansible
version: "8"
title: "community.sops.sops vars – Loading sops-encrypted vars files"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/sops/sops_vars.html
fetched_at: 2026-07-28T01:59:27+00:00
---
# community.sops.sops vars – Loading sops-encrypted vars files

> **Note:**
>
> This vars plugin is part of the [community.sops collection](https://galaxy.ansible.com/ui/repo/published/community/sops/) (version 1.6.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.sops`.
>
> To use it in a playbook, specify: `community.sops.sops`.

New in community.sops 0.1.0

- [Synopsis](sops_vars.md#synopsis)
- [Parameters](sops_vars.md#parameters)
- [See Also](sops_vars.md#see-also)

## [Synopsis](sops_vars.md#id1)

- Load encrypted YAML files into corresponding groups/hosts in group_vars/ and host_vars/ directories.
- Files are encrypted prior to reading, making this plugin an effective companion to host_group_vars plugin.
- Files are restricted to .sops.yaml, .sops.yml, .sops.json extensions.
- Hidden files are ignored.

## [Parameters](sops_vars.md#id2)

| Parameter | Comments |
| --- | --- |
| **_disable_vars_plugin_temporarily**  boolean  *added in community.sops 1.3.0* | Temporarily disable this plugin.  Useful if ansible-inventory is supposed to be run without decrypting secrets (in AWX for instance).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - Environment variable: [`SOPS_ANSIBLE_AWX_DISABLE_VARS_PLUGIN_TEMPORARILY`](../../environment_variables.md#envvar-SOPS_ANSIBLE_AWX_DISABLE_VARS_PLUGIN_TEMPORARILY) |
| **_valid_extensions**  list / elements=string | Check all of these extensions when looking for ‘variable’ files which should be YAML or JSON or vaulted versions of these.  This affects vars_files, include_vars, inventory and vars plugins among others.  **Default:** `[".sops.yml", ".sops.yaml", ".sops.json"]` |
| **age_key**  string  *added in community.sops 1.4.0* | One or more age private keys that can be used to decrypt encrypted files.  Will be set as the `SOPS_AGE_KEY` environment variable when calling sops.  **Configuration:**   - Environment variable: [`ANSIBLE_SOPS_AGE_KEY`](../../environment_variables.md#envvar-ANSIBLE_SOPS_AGE_KEY) |
| **age_keyfile**  path  *added in community.sops 1.4.0* | The file containing the age private keys that sops can use to decrypt encrypted files.  Will be set as the `SOPS_AGE_KEY_FILE` environment variable when calling sops.  By default, sops looks for `sops/age/keys.txt` inside your user configuration directory.  **Configuration:**   - INI entry:  ```YAML+Jinja   [community.sops]   age_keyfile = VALUE   ``` - Environment variable: [`ANSIBLE_SOPS_AGE_KEYFILE`](../../environment_variables.md#envvar-ANSIBLE_SOPS_AGE_KEYFILE) |
| **aws_access_key_id**  string  *added in community.sops 1.0.0* | The AWS access key ID to use for requests to AWS.  Sets the environment variable [`AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-AWS_ACCESS_KEY_ID) for the sops call.  **Configuration:**   - INI entry:  ```YAML+Jinja   [community.sops]   aws_access_key_id = VALUE   ```  *added in community.sops 1.2.0* - Environment variable: [`ANSIBLE_SOPS_AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-ANSIBLE_SOPS_AWS_ACCESS_KEY_ID)  *added in community.sops 1.2.0* |
| **aws_profile**  string  *added in community.sops 1.0.0* | The AWS profile to use for requests to AWS.  This corresponds to the sops `--aws-profile` option.  **Configuration:**   - INI entry:  ```YAML+Jinja   [community.sops]   aws_profile = VALUE   ```  *added in community.sops 1.2.0* - Environment variable: [`ANSIBLE_SOPS_AWS_PROFILE`](../../environment_variables.md#envvar-ANSIBLE_SOPS_AWS_PROFILE)  *added in community.sops 1.2.0* |
| **aws_secret_access_key**  string  *added in community.sops 1.0.0* | The AWS secret access key to use for requests to AWS.  Sets the environment variable [`AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_SECRET_ACCESS_KEY) for the sops call.  **Configuration:**   - Environment variable: [`ANSIBLE_SOPS_AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-ANSIBLE_SOPS_AWS_SECRET_ACCESS_KEY)  *added in community.sops 1.2.0* |
| **aws_session_token**  string  *added in community.sops 1.0.0* | The AWS session token to use for requests to AWS.  Sets the environment variable [`AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-AWS_SESSION_TOKEN) for the sops call.  **Configuration:**   - INI entry:  ```YAML+Jinja   [community.sops]   aws_session_token = VALUE   ```  *added in community.sops 1.2.0* - Environment variable: [`ANSIBLE_SOPS_AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-ANSIBLE_SOPS_AWS_SESSION_TOKEN)  *added in community.sops 1.2.0* |
| **cache**  boolean  *added in community.sops 0.2.0* | Whether to cache decrypted files or not.  If the cache is disabled, the files will be decrypted for almost every task. This is very slow!  Only disable caching if you modify the variable files during a playbook run and want the updated result to be available from the next task on.  Note that setting `stage=inventory` has the same effect as setting `cache=true`: the variables will be loaded only once (during inventory loading) and the vars plugin will not be called for every task.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [community.sops]   vars_cache = true   ``` - Environment variable: [`ANSIBLE_VARS_SOPS_PLUGIN_CACHE`](../../environment_variables.md#envvar-ANSIBLE_VARS_SOPS_PLUGIN_CACHE) |
| **config_path**  path  *added in community.sops 1.0.0* | Path to the sops configuration file.  If not set, sops will recursively search for the config file starting at the file that is encrypted or decrypted.  This corresponds to the sops `--config` option.  **Configuration:**   - INI entry:  ```YAML+Jinja   [community.sops]   config_path = VALUE   ```  *added in community.sops 1.2.0* - Environment variable: [`ANSIBLE_SOPS_CONFIG_PATH`](../../environment_variables.md#envvar-ANSIBLE_SOPS_CONFIG_PATH)  *added in community.sops 1.2.0* |
| **enable_local_keyservice**  boolean  *added in community.sops 1.0.0* | Tell sops to use local key service.  This corresponds to the sops `--enable-local-keyservice` option.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [community.sops]   enable_local_keyservice = false   ```  *added in community.sops 1.2.0* - Environment variable: [`ANSIBLE_SOPS_ENABLE_LOCAL_KEYSERVICE`](../../environment_variables.md#envvar-ANSIBLE_SOPS_ENABLE_LOCAL_KEYSERVICE)  *added in community.sops 1.2.0* |
| **keyservice**  list / elements=string  *added in community.sops 1.0.0* | Specify key services to use next to the local one.  A key service must be specified in the form `protocol://address`, for example `tcp://myserver.com:5000`.  This corresponds to the sops `--keyservice` option.  **Configuration:**   - INI entry:  ```YAML+Jinja   [community.sops]   keyservice = VALUE   ```  *added in community.sops 1.2.0* - Environment variable: [`ANSIBLE_SOPS_KEYSERVICE`](../../environment_variables.md#envvar-ANSIBLE_SOPS_KEYSERVICE)  *added in community.sops 1.2.0* |
| **sops_binary**  path  *added in community.sops 1.0.0* | Path to the sops binary.  By default uses `sops`.  **Configuration:**   - INI entry:  ```YAML+Jinja   [community.sops]   binary = VALUE   ```  *added in community.sops 1.2.0* - Environment variable: [`ANSIBLE_SOPS_BINARY`](../../environment_variables.md#envvar-ANSIBLE_SOPS_BINARY)  *added in community.sops 1.2.0* |
| **stage**  string  *added in community.sops 0.2.0* | Control when this vars plugin may be executed.  Setting this option to `all` will run the vars plugin after importing inventory and whenever it is demanded by a task.  Setting this option to `task` will only run the vars plugin whenever it is demanded by a task.  Setting this option to `inventory` will only run the vars plugin after parsing inventory.  If this option is omitted, the global *RUN_VARS_PLUGINS* configuration is used to determine when to execute the vars plugin.  **Choices:**   - `"all"` - `"task"` - `"inventory"`   **Configuration:**   - INI entry:  ```YAML+Jinja   [community.sops]   vars_stage = VALUE   ``` - Environment variable: [`ANSIBLE_VARS_SOPS_PLUGIN_STAGE`](../../environment_variables.md#envvar-ANSIBLE_VARS_SOPS_PLUGIN_STAGE) |

## [See Also](sops_vars.md#id3)

> **See also:**
>
> [community.sops.sops](sops_lookup.md#ansible-collections-community-sops-sops-lookup) lookup plugin
> :   The sops lookup can be used decrypt sops-encrypted files.
>
> [community.sops.decrypt](decrypt_filter.md#ansible-collections-community-sops-decrypt-filter) filter plugin
> :   The decrypt filter can be used to descrypt sops-encrypted in-memory data.
>
> [community.sops.load_vars](load_vars_module.md#ansible-collections-community-sops-load-vars-module)
> :   Load sops-encrypted variables from files, dynamically within a task.

### Authors

- Edoardo Tenani (@endorama)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.sops/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.sops)
- [Submit a bug report](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-sops)

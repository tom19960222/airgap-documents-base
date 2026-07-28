---
collection: ansible
version: "6"
title: "community.sops.sops lookup – Read sops encrypted file contents"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/sops/sops_lookup.html
fetched_at: 2026-07-27T17:21:12+00:00
---
# community.sops.sops lookup – Read sops encrypted file contents

> **Note:**
>
> This lookup plugin is part of the [community.sops collection](https://galaxy.ansible.com/community/sops) (version 1.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.sops`.
>
> To use it in a playbook, specify: `community.sops.sops`.

New in community.sops 0.1.0

- [Synopsis](sops_lookup.md#synopsis)
- [Terms](sops_lookup.md#terms)
- [Keyword parameters](sops_lookup.md#keyword-parameters)
- [Notes](sops_lookup.md#notes)
- [See Also](sops_lookup.md#see-also)
- [Examples](sops_lookup.md#examples)
- [Return Value](sops_lookup.md#return-value)

## [Synopsis](sops_lookup.md#id1)

- This lookup returns the contents from a file on the Ansible controller’s file system.
- This lookup requires the `sops` executable to be available in the controller PATH.

## [Terms](sops_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | Path(s) of files to read. |

## [Keyword parameters](sops_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.sops.sops', key1=value1, key2=value2, ...)` and `query('community.sops.sops', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **age_key**  string  added in community.sops 1.4.0 | One or more age private keys that can be used to decrypt encrypted files.  Will be set as the `SOPS_AGE_KEY` environment variable when calling sops.  Configuration:   - Environment variable: [`ANSIBLE_SOPS_AGE_KEY`](../../environment_variables.md#envvar-ANSIBLE_SOPS_AGE_KEY) - Variable: sops_age_key |
| **age_keyfile**  path  added in community.sops 1.4.0 | The file containing the age private keys that sops can use to decrypt encrypted files.  Will be set as the `SOPS_AGE_KEY_FILE` environment variable when calling sops.  By default, sops looks for `sops/age/keys.txt` inside your user configuration directory.  Configuration:   - INI entry:  ```YAML+Jinja   [community.sops]   age_keyfile = VALUE   ``` - Environment variable: [`ANSIBLE_SOPS_AGE_KEYFILE`](../../environment_variables.md#envvar-ANSIBLE_SOPS_AGE_KEYFILE) - Variable: sops_age_keyfile |
| **aws_access_key_id**  string  added in community.sops 1.0.0 | The AWS access key ID to use for requests to AWS.  Sets the environment variable `AWS_ACCESS_KEY_ID` for the sops call.  Configuration:   - INI entry:  ```YAML+Jinja   [community.sops]   aws_access_key_id = VALUE   ```  added in community.sops 1.2.0 - Environment variable: [`ANSIBLE_SOPS_AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-ANSIBLE_SOPS_AWS_ACCESS_KEY_ID)  added in community.sops 1.2.0 - Variable: sops_aws_access_key_id |
| **aws_profile**  string  added in community.sops 1.0.0 | The AWS profile to use for requests to AWS.  This corresponds to the sops `--aws-profile` option.  Configuration:   - INI entry:  ```YAML+Jinja   [community.sops]   aws_profile = VALUE   ```  added in community.sops 1.2.0 - Environment variable: [`ANSIBLE_SOPS_AWS_PROFILE`](../../environment_variables.md#envvar-ANSIBLE_SOPS_AWS_PROFILE)  added in community.sops 1.2.0 - Variable: sops_aws_profile |
| **aws_secret_access_key**  string  added in community.sops 1.0.0 | The AWS secret access key to use for requests to AWS.  Sets the environment variable `AWS_SECRET_ACCESS_KEY` for the sops call.  Configuration:   - Environment variable: [`ANSIBLE_SOPS_AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-ANSIBLE_SOPS_AWS_SECRET_ACCESS_KEY)  added in community.sops 1.2.0 - Variable: sops_aws_secret_access_key |
| **aws_session_token**  string  added in community.sops 1.0.0 | The AWS session token to use for requests to AWS.  Sets the environment variable `AWS_SESSION_TOKEN` for the sops call.  Configuration:   - INI entry:  ```YAML+Jinja   [community.sops]   aws_session_token = VALUE   ```  added in community.sops 1.2.0 - Environment variable: [`ANSIBLE_SOPS_AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-ANSIBLE_SOPS_AWS_SESSION_TOKEN)  added in community.sops 1.2.0 - Variable: sops_session_token - Variable: sops_aws_session_token  added in community.sops 1.2.0 |
| **base64**  boolean | Base64-encodes the parsed result.  Use this if you want to store binary data in Ansible variables.  Choices:   - `false` ← (default) - `true` |
| **config_path**  path  added in community.sops 1.0.0 | Path to the sops configuration file.  If not set, sops will recursively search for the config file starting at the file that is encrypted or decrypted.  This corresponds to the sops `--config` option.  Configuration:   - INI entry:  ```YAML+Jinja   [community.sops]   config_path = VALUE   ```  added in community.sops 1.2.0 - Environment variable: [`ANSIBLE_SOPS_CONFIG_PATH`](../../environment_variables.md#envvar-ANSIBLE_SOPS_CONFIG_PATH)  added in community.sops 1.2.0 - Variable: sops_config_path |
| **empty_on_not_exist**  boolean | When set to `true`, will not raise an error when a file cannot be found, but return an empty string instead.  Choices:   - `false` ← (default) - `true` |
| **enable_local_keyservice**  boolean  added in community.sops 1.0.0 | Tell sops to use local key service.  This corresponds to the sops `--enable-local-keyservice` option.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [community.sops]   enable_local_keyservice = false   ```  added in community.sops 1.2.0 - Environment variable: [`ANSIBLE_SOPS_ENABLE_LOCAL_KEYSERVICE`](../../environment_variables.md#envvar-ANSIBLE_SOPS_ENABLE_LOCAL_KEYSERVICE)  added in community.sops 1.2.0 - Variable: sops_enable_local_keyservice |
| **input_type**  string | Tell sops how to interpret the encrypted file.  By default, sops will chose the input type from the file extension. If it detects the wrong type for a file, this could result in decryption failing.  Choices:   - `"binary"` - `"json"` - `"yaml"` - `"dotenv"` |
| **keyservice**  list / elements=string  added in community.sops 1.0.0 | Specify key services to use next to the local one.  A key service must be specified in the form `protocol://address`, for example `tcp://myserver.com:5000`.  This corresponds to the sops `--keyservice` option.  Configuration:   - INI entry:  ```YAML+Jinja   [community.sops]   keyservice = VALUE   ```  added in community.sops 1.2.0 - Environment variable: [`ANSIBLE_SOPS_KEYSERVICE`](../../environment_variables.md#envvar-ANSIBLE_SOPS_KEYSERVICE)  added in community.sops 1.2.0 - Variable: sops_keyservice |
| **output_type**  string | Tell sops how to interpret the decrypted file.  By default, sops will chose the output type from the file extension. If it detects the wrong type for a file, this could result in decryption failing.  Choices:   - `"binary"` - `"json"` - `"yaml"` - `"dotenv"` |
| **rstrip**  boolean | Whether to remove trailing newlines and spaces.  Choices:   - `false` - `true` ← (default) |
| **sops_binary**  path  added in community.sops 1.0.0 | Path to the sops binary.  By default uses `sops`.  Configuration:   - INI entry:  ```YAML+Jinja   [community.sops]   binary = VALUE   ```  added in community.sops 1.2.0 - Environment variable: [`ANSIBLE_SOPS_BINARY`](../../environment_variables.md#envvar-ANSIBLE_SOPS_BINARY)  added in community.sops 1.2.0 - Variable: sops_binary |

## [Notes](sops_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.sops.sops', term1, term2, key1=value1, key2=value2)` and `query('community.sops.sops', term1, term2, key1=value1, key2=value2)`
> - This lookup does not understand ‘globbing’ - use the fileglob lookup instead.

## [See Also](sops_lookup.md#id5)

> **See also:**
>
> community.sops.decrypt filter
> :   The decrypt filter can be used to descrypt sops-encrypted in-memory data.
>
> [community.sops.sops vars plugin](sops_vars.md#ansible-collections-community-sops-sops-vars)
> :   The sops vars plugin can be used to load sops-encrypted host or group variables.
>
> [community.sops.load_vars](load_vars_module.md#ansible-collections-community-sops-load-vars-module)
> :   Load sops-encrypted variables from files, dynamically within a task.

## [Examples](sops_lookup.md#id6)

```yaml+jinja
- name: Output secrets to screen (BAD IDEA!)
  ansible.builtin.debug:
    msg: "Content: {{ lookup('community.sops.sops', item) }}"
  loop:
    - sops-encrypted-file.enc.yaml

- name: Add SSH private key
  ansible.builtin.copy:
    # Note that rstrip=false is necessary for some SSH versions to be able to use the key
    content: "{{ lookup('community.sops.sops', user + '-id_rsa', rstrip=false) }}"
    dest: /home/{{ user }}/.ssh/id_rsa
    owner: "{{ user }}"
    group: "{{ user }}"
    mode: 0600
  no_log: true  # avoid content to be written to log

- name: The file file.json is a YAML file, which contains the encryption of binary data
  ansible.builtin.debug:
    msg: "Content: {{ lookup('community.sops.sops', 'file.json', input_type='yaml', output_type='binary') }}"
```

## [Return Value](sops_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | Decrypted file content.  Returned: success |

### Authors

- Edoardo Tenani (@endorama)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.sops/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.sops)
[Submit a bug report](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-sops)

---
collection: ansible
version: "8"
title: "community.sops.decrypt filter – Decrypt sops encrypted data"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/sops/decrypt_filter.html
fetched_at: 2026-07-28T01:59:26+00:00
---
# community.sops.decrypt filter – Decrypt sops encrypted data

> **Note:**
>
> This filter plugin is part of the [community.sops collection](https://galaxy.ansible.com/ui/repo/published/community/sops/) (version 1.6.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.sops`.
>
> To use it in a playbook, specify: `community.sops.decrypt`.

New in community.sops 1.1.0

- [Synopsis](decrypt_filter.md#synopsis)
- [Input](decrypt_filter.md#input)
- [Keyword parameters](decrypt_filter.md#keyword-parameters)
- [See Also](decrypt_filter.md#see-also)
- [Examples](decrypt_filter.md#examples)
- [Return Value](decrypt_filter.md#return-value)

## [Synopsis](decrypt_filter.md#id1)

- Decrypt sops encrypted data.
- Allows to decrypt data that has been provided by an arbitrary source.
- Note that due to Ansible lazy-evaluating expressions, it is better to use [ansible.builtin.set_fact](../../ansible/builtin/set_fact_module.md#ansible-collections-ansible-builtin-set-fact-module) to store the result of an evaluation in a fact to avoid recomputing the value every time the expression is used.

## [Input](decrypt_filter.md#id2)

This describes the input of the filter, the value before `| community.sops.decrypt`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | The data to decrypt. |

## [Keyword parameters](decrypt_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | community.sops.decrypt(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **age_key**  string  *added in community.sops 1.4.0* | One or more age private keys that can be used to decrypt encrypted files.  Will be set as the `SOPS_AGE_KEY` environment variable when calling sops. |
| **age_keyfile**  path  *added in community.sops 1.4.0* | The file containing the age private keys that sops can use to decrypt encrypted files.  Will be set as the `SOPS_AGE_KEY_FILE` environment variable when calling sops.  By default, sops looks for `sops/age/keys.txt` inside your user configuration directory. |
| **aws_access_key_id**  string  *added in community.sops 1.0.0* | The AWS access key ID to use for requests to AWS.  Sets the environment variable [`AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-AWS_ACCESS_KEY_ID) for the sops call. |
| **aws_profile**  string  *added in community.sops 1.0.0* | The AWS profile to use for requests to AWS.  This corresponds to the sops `--aws-profile` option. |
| **aws_secret_access_key**  string  *added in community.sops 1.0.0* | The AWS secret access key to use for requests to AWS.  Sets the environment variable [`AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_SECRET_ACCESS_KEY) for the sops call. |
| **aws_session_token**  string  *added in community.sops 1.0.0* | The AWS session token to use for requests to AWS.  Sets the environment variable [`AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-AWS_SESSION_TOKEN) for the sops call. |
| **config_path**  path  *added in community.sops 1.0.0* | Path to the sops configuration file.  If not set, sops will recursively search for the config file starting at the file that is encrypted or decrypted.  This corresponds to the sops `--config` option. |
| **decode_output**  boolean | Whether to decode the output to bytes.  When `output_type=binary`, and the file isn’t known to contain UTF-8 encoded text, this should better be set to `false` to prevent mangling the data with UTF-8 decoding.  **Choices:**   - `false` - `true` ← (default) |
| **enable_local_keyservice**  boolean  *added in community.sops 1.0.0* | Tell sops to use local key service.  This corresponds to the sops `--enable-local-keyservice` option.  **Choices:**   - `false` ← (default) - `true` |
| **input_type**  string | Tell sops how to interpret the encrypted data.  There is no auto-detection since we do not have a filename. By default sops is told to treat the input as YAML. If that is wrong, please set this option to the correct value.  **Choices:**   - `"binary"` - `"json"` - `"yaml"` ← (default) - `"dotenv"` |
| **keyservice**  list / elements=string  *added in community.sops 1.0.0* | Specify key services to use next to the local one.  A key service must be specified in the form `protocol://address`, for example `tcp://myserver.com:5000`.  This corresponds to the sops `--keyservice` option. |
| **output_type**  string | Tell sops how to interpret the decrypted file.  Please note that the output is always text or bytes, depending on the value of `decode_output`. To parse the resulting JSON or YAML, use corresponding filters such as [ansible.builtin.from_json](../../ansible/builtin/from_json_filter.md#ansible-collections-ansible-builtin-from-json-filter) and [ansible.builtin.from_yaml](../../ansible/builtin/from_yaml_filter.md#ansible-collections-ansible-builtin-from-yaml-filter).  **Choices:**   - `"binary"` - `"json"` - `"yaml"` ← (default) - `"dotenv"` |
| **rstrip**  boolean | Whether to remove trailing newlines and spaces.  **Choices:**   - `false` - `true` ← (default) |
| **sops_binary**  path  *added in community.sops 1.0.0* | Path to the sops binary.  By default uses `sops`. |

## [See Also](decrypt_filter.md#id4)

> **See also:**
>
> [community.sops.sops](sops_lookup.md#ansible-collections-community-sops-sops-lookup) lookup plugin
> :   Read sops encrypted file contents.
>
> [community.sops.sops](sops_vars.md#ansible-collections-community-sops-sops-vars) vars plugin
> :   Loading sops-encrypted vars files.
>
> [community.sops.load_vars](load_vars_module.md#ansible-collections-community-sops-load-vars-module)
> :   Load sops-encrypted variables from files, dynamically within a task.

## [Examples](decrypt_filter.md#id5)

```yaml+jinja
- name: Decrypt file fetched from URL
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Fetch file from URL
      ansible.builtin.uri:
        url: https://raw.githubusercontent.com/getsops/sops/master/functional-tests/res/comments.enc.yaml
        return_content: true
      register: encrypted_content

    - name: Show encrypted data
      debug:
        msg: "{{ encrypted_content.content | ansible.builtin.from_yaml }}"

    - name: Decrypt data and decode decrypted YAML
      set_fact:
        decrypted_data: "{{ encrypted_content.content | community.sops.decrypt | ansible.builtin.from_yaml }}"

    - name: Show decrypted data
      debug:
        msg: "{{ decrypted_data }}"
```

## [Return Value](decrypt_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | Decrypted data as text (`decode_output=true`, default) or binary string (`decode_output=false`).  **Returned:** success |

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.sops/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.sops)
- [Submit a bug report](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-sops)

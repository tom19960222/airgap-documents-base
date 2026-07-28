---
collection: ansible
version: "6"
title: "community.sops.sops_encrypt module – Encrypt data with sops"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/sops/sops_encrypt_module.html
fetched_at: 2026-07-27T17:21:11+00:00
---
# community.sops.sops_encrypt module – Encrypt data with sops

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
> To use it in a playbook, specify: `community.sops.sops_encrypt`.

New in community.sops 0.1.0

- [Synopsis](sops_encrypt_module.md#synopsis)
- [Parameters](sops_encrypt_module.md#parameters)
- [Attributes](sops_encrypt_module.md#attributes)
- [See Also](sops_encrypt_module.md#see-also)
- [Examples](sops_encrypt_module.md#examples)

## [Synopsis](sops_encrypt_module.md#id1)

- Allows to encrypt binary data (Base64 encoded), text data, JSON or YAML data with sops.

## [Parameters](sops_encrypt_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **age**  list / elements=string  added in community.sops 1.4.0 | Age fingerprints to use.  This corresponds to the sops `--age` option. |
| **age_key**  string  added in community.sops 1.4.0 | One or more age private keys that can be used to decrypt encrypted files.  Will be set as the `SOPS_AGE_KEY` environment variable when calling sops. |
| **age_keyfile**  path  added in community.sops 1.4.0 | The file containing the age private keys that sops can use to decrypt encrypted files.  Will be set as the `SOPS_AGE_KEY_FILE` environment variable when calling sops.  By default, sops looks for `sops/age/keys.txt` inside your user configuration directory. |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **aws_access_key_id**  string  added in community.sops 1.0.0 | The AWS access key ID to use for requests to AWS.  Sets the environment variable `AWS_ACCESS_KEY_ID` for the sops call. |
| **aws_profile**  string  added in community.sops 1.0.0 | The AWS profile to use for requests to AWS.  This corresponds to the sops `--aws-profile` option. |
| **aws_secret_access_key**  string  added in community.sops 1.0.0 | The AWS secret access key to use for requests to AWS.  Sets the environment variable `AWS_SECRET_ACCESS_KEY` for the sops call. |
| **aws_session_token**  string  added in community.sops 1.0.0 | The AWS session token to use for requests to AWS.  Sets the environment variable `AWS_SESSION_TOKEN` for the sops call. |
| **azure_kv**  list / elements=string  added in community.sops 1.0.0 | Azure Key Vault URLs to use.  This corresponds to the sops `--azure-kv` option. |
| **config_path**  path  added in community.sops 1.0.0 | Path to the sops configuration file.  If not set, sops will recursively search for the config file starting at the file that is encrypted or decrypted.  This corresponds to the sops `--config` option. |
| **content_binary**  string | The data to encrypt. Must be [Base64 encoded](https://en.wikipedia.org/wiki/Base64) binary data.  Please note that the module might not be idempotent if the data can be parsed as JSON or YAML.  Exactly one of *content_text*, *content_binary*, *content_json* and *content_yaml* must be specified. |
| **content_json**  dictionary | The data to encrypt. Must be a JSON dictionary.  Exactly one of *content_text*, *content_binary*, *content_json* and *content_yaml* must be specified. |
| **content_text**  string | The data to encrypt. Must be a Unicode text.  Please note that the module might not be idempotent if the text can be parsed as JSON or YAML.  Exactly one of *content_text*, *content_binary*, *content_json* and *content_yaml* must be specified. |
| **content_yaml**  dictionary | The data to encrypt. Must be a YAML dictionary.  Please note that Ansible only allows to pass data that can be represented as a JSON dictionary.  Exactly one of *content_text*, *content_binary*, *content_json* and *content_yaml* must be specified. |
| **enable_local_keyservice**  boolean  added in community.sops 1.0.0 | Tell sops to use local key service.  This corresponds to the sops `--enable-local-keyservice` option.  Choices:   - `false` ← (default) - `true` |
| **encrypted_regex**  string  added in community.sops 1.0.0 | Set the encrypted key suffix.  When specified, only keys matching the regular expression will be encrypted.  This corresponds to the sops `--encrypted-regex` option. |
| **encrypted_suffix**  string  added in community.sops 1.0.0 | Override the encrypted key suffix.  When set to an empty string, all keys will be encrypted that are not explicitly marked by *unencrypted_suffix*.  This corresponds to the sops `--encrypted-suffix` option. |
| **encryption_context**  list / elements=string  added in community.sops 1.0.0 | List of KMS encryption context pairs of format `key:value`.  This corresponds to the sops `--encryption-context` option. |
| **force**  boolean | Force rewriting the encrypted file.  Choices:   - `false` ← (default) - `true` |
| **gcp_kms**  list / elements=string  added in community.sops 1.0.0 | GCP KMS resource IDs to use.  This corresponds to the sops `--gcp-kms` option. |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **hc_vault_transit**  list / elements=string  added in community.sops 1.0.0 | HashiCorp Vault key URIs to use.  For example, `https://vault.example.org:8200/v1/transit/keys/dev`.  This corresponds to the sops `--hc-vault-transit` option. |
| **keyservice**  list / elements=string  added in community.sops 1.0.0 | Specify key services to use next to the local one.  A key service must be specified in the form `protocol://address`, for example `tcp://myserver.com:5000`.  This corresponds to the sops `--keyservice` option. |
| **kms**  list / elements=string  added in community.sops 1.0.0 | List of KMS ARNs to use.  This corresponds to the sops `--kms` option. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must either add a leading zero so that Ansible’s YAML parser knows it is an octal number (like `0644` or `01777`) or quote it (like `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number.  Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership. |
| **path**  path / required | The sops encrypt file. |
| **pgp**  list / elements=string  added in community.sops 1.0.0 | PGP fingerprints to use.  This corresponds to the sops `--pgp` option. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **shamir_secret_sharing_threshold**  integer  added in community.sops 1.0.0 | The number of distinct keys required to retrieve the data key with [Shamir’s Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing).  If not set here and in the sops config file, will default to `0`.  This corresponds to the sops `--shamir-secret-sharing-threshold` option. |
| **sops_binary**  path  added in community.sops 1.0.0 | Path to the sops binary.  By default uses `sops`. |
| **unencrypted_regex**  string  added in community.sops 1.0.0 | Set the unencrypted key suffix.  When specified, only keys matching the regular expression will be left unencrypted.  This corresponds to the sops `--unencrypted-regex` option. |
| **unencrypted_suffix**  string  added in community.sops 1.0.0 | Override the unencrypted key suffix.  This corresponds to the sops `--unencrypted-suffix` option. |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  Choices:   - `false` ← (default) - `true` |

## [Attributes](sops_encrypt_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **safe_file_operations** | Support: full | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption. |

## [See Also](sops_encrypt_module.md#id4)

> **See also:**
>
> [community.sops.sops lookup](sops_lookup.md#ansible-collections-community-sops-sops-lookup)
> :   The sops lookup can be used decrypt sops-encrypted files.

## [Examples](sops_encrypt_module.md#id5)

```yaml+jinja
- name: Encrypt a secret text
  community.sops.sops_encrypt:
    path: text-data.sops
    content_text: This is a secret text.

- name: Encrypt the contents of a file
  community.sops.sops_encrypt:
    path: binary-data.sops
    content_binary: "{{ lookup('ansible.builtin.file', '/path/to/file', rstrip=false) | b64encode }}"

- name: Encrypt some datastructure as YAML
  community.sops.sops_encrypt:
    path: stuff.sops.yaml
    content_yaml: "{{ result }}"
```

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.sops/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.sops)
[Submit a bug report](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-sops)

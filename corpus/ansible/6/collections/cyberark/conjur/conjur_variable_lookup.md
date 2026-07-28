---
collection: ansible
version: "6"
title: "cyberark.conjur.conjur_variable lookup – Fetch credentials from CyberArk Conjur."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cyberark/conjur/conjur_variable_lookup.html
fetched_at: 2026-07-27T17:24:43+00:00
---
# cyberark.conjur.conjur_variable lookup – Fetch credentials from CyberArk Conjur.

> **Note:**
>
> This lookup plugin is part of the [cyberark.conjur collection](https://galaxy.ansible.com/cyberark/conjur) (version 1.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cyberark.conjur`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](conjur_variable_lookup.md#ansible-collections-cyberark-conjur-conjur-variable-lookup-requirements) for details.
>
> To use it in a playbook, specify: `cyberark.conjur.conjur_variable`.

New in cyberark.conjur 1.0.2

- [Synopsis](conjur_variable_lookup.md#synopsis)
- [Requirements](conjur_variable_lookup.md#requirements)
- [Terms](conjur_variable_lookup.md#terms)
- [Keyword parameters](conjur_variable_lookup.md#keyword-parameters)
- [Notes](conjur_variable_lookup.md#notes)
- [Examples](conjur_variable_lookup.md#examples)
- [Return Value](conjur_variable_lookup.md#return-value)

## [Synopsis](conjur_variable_lookup.md#id1)

- Retrieves credentials from Conjur using the controlling host’s Conjur identity or environment variables. Environment variables could be CONJUR_ACCOUNT, CONJUR_APPLIANCE_URL, CONJUR_CERT_FILE, CONJUR_AUTHN_LOGIN, CONJUR_AUTHN_API_KEY, CONJUR_AUTHN_TOKEN_FILE Conjur info - <https://www.conjur.org/>.

## [Requirements](conjur_variable_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- The controlling host running Ansible has a Conjur identity. (More: <https://docs.conjur.org/latest/en/Content/Get%20Started/key_concepts/machine_identity.html>)

## [Terms](conjur_variable_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | Variable path |

## [Keyword parameters](conjur_variable_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('cyberark.conjur.conjur_variable', key1=value1, key2=value2, ...)` and `query('cyberark.conjur.conjur_variable', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **as_file**  boolean | Store lookup result in a temporary file and returns the file path. Thus allowing it to be consumed as an ansible file parameter (eg ansible_ssh_private_key_file).  Choices:   - `false` ← (default) - `true` |
| **authn_token_file**  path | Path to the access token file.  Default: `"/var/run/conjur/access-token"`  Configuration:   - INI entry:  ```YAML+Jinja   [conjur,]   authn_token_file = /var/run/conjur/access-token   ``` - Environment variable: [`CONJUR_AUTHN_TOKEN_FILE`](../../environment_variables.md#envvar-CONJUR_AUTHN_TOKEN_FILE) |
| **config_file**  path | Path to the Conjur configuration file. The configuration file is a YAML file.  Default: `"/etc/conjur.conf"`  Configuration:   - INI entry:  ```YAML+Jinja   [conjur,]   config_file_path = /etc/conjur.conf   ``` - Environment variable: [`CONJUR_CONFIG_FILE`](../../environment_variables.md#envvar-CONJUR_CONFIG_FILE) |
| **identity_file**  path | Path to the Conjur identity file. The identity file follows the netrc file format convention.  Default: `"/etc/conjur.identity"`  Configuration:   - INI entry:  ```YAML+Jinja   [conjur,]   identity_file_path = /etc/conjur.identity   ``` - Environment variable: [`CONJUR_IDENTITY_FILE`](../../environment_variables.md#envvar-CONJUR_IDENTITY_FILE) |
| **validate_certs**  boolean | Flag to control SSL certificate validation  Choices:   - `false` - `true` ← (default) |

## [Notes](conjur_variable_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('cyberark.conjur.conjur_variable', term1, term2, key1=value1, key2=value2)` and `query('cyberark.conjur.conjur_variable', term1, term2, key1=value1, key2=value2)`

## [Examples](conjur_variable_lookup.md#id6)

```yaml+jinja
---
  - hosts: localhost
    collections:
      - cyberark.conjur
    tasks:
      - name: Lookup variable in Conjur
        debug:
          msg: "{{ lookup('cyberark.conjur.conjur_variable', '/path/to/secret') }}"
```

## [Return Value](conjur_variable_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | Value stored in Conjur.  Returned: success |

### Authors

- CyberArk BizDev (@cyberark-bizdev)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/cyberark/ansible-conjur-collection/issues)
[Repository (Sources)](https://github.com/cyberark/ansible-conjur-collection)

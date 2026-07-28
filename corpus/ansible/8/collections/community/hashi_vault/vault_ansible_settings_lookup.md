---
collection: ansible
version: "8"
title: "community.hashi_vault.vault_ansible_settings lookup – Returns plugin settings (options)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/hashi_vault/vault_ansible_settings_lookup.html
fetched_at: 2026-07-28T01:53:35+00:00
---
# community.hashi_vault.vault_ansible_settings lookup – Returns plugin settings (options)

> **Note:**
>
> This lookup plugin is part of the [community.hashi_vault collection](https://galaxy.ansible.com/ui/repo/published/community/hashi_vault/) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hashi_vault`.
>
> To use it in a playbook, specify: `community.hashi_vault.vault_ansible_settings`.

New in community.hashi_vault 2.5.0

- [Synopsis](vault_ansible_settings_lookup.md#synopsis)
- [Terms](vault_ansible_settings_lookup.md#terms)
- [Keyword parameters](vault_ansible_settings_lookup.md#keyword-parameters)
- [Notes](vault_ansible_settings_lookup.md#notes)
- [See Also](vault_ansible_settings_lookup.md#see-also)
- [Examples](vault_ansible_settings_lookup.md#examples)
- [Return Value](vault_ansible_settings_lookup.md#return-value)

## [Synopsis](vault_ansible_settings_lookup.md#id1)

- Returns a dictionary of options and their values for a given plugin.
- This is most useful for using plugin settings in modules and `module_defaults`, especially when common settings are set in `ansible.cfg`, in Ansible vars, or via environment variables on the controller.
- Options can be filtered by name, and can include or exclude defaults, unset options, and private options.

## [Terms](vault_ansible_settings_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string | The names of the options to load.  Supports `fnmatch` [style wildcards](https://docs.python.org/3/library/fnmatch.html).  Prepend any name or pattern with `!` to invert the match.  **Default:** `["*"]` |

## [Keyword parameters](vault_ansible_settings_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.hashi_vault.vault_ansible_settings', key1=value1, key2=value2, ...)` and `query('community.hashi_vault.vault_ansible_settings', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **include_default**  boolean | Include options whose value comes from a default.  **Choices:**   - `false` ← (default) - `true` |
| **include_none**  boolean | Include options whose value is `None` (this usually means they are unset).  **Choices:**   - `false` ← (default) - `true` |
| **include_private**  boolean | Include options that begin with underscore `_`.  **Choices:**   - `false` ← (default) - `true` |
| **plugin**  string | The name of the plugin whose options will be returned.  Only lookups are supported.  Short names (without a dot `.`) will be fully qualified with `community.hashi_vault`.  **Default:** `"community.hashi_vault.vault_login"` |

## [Notes](vault_ansible_settings_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.hashi_vault.vault_ansible_settings', term1, term2, key1=value1, key2=value2)` and `query('community.hashi_vault.vault_ansible_settings', term1, term2, key1=value1, key2=value2)`
> - This collection supports some “low precedence” environment variables that get loaded after all other sources, such as `VAULT_ADDR`.
> - These environment variables **are not supported** with this plugin.
> - If you wish to use them, use the [ansible.builtin.env lookup](../../ansible/builtin/env_lookup.md#ansible-collections-ansible-builtin-env-lookup) to load them directly when calling a module or setting `module_defaults`.
> - Similarly, any options that rely on additional processing to fill in their values will not have that done.
> - For example, tokens will not be loaded from the token sink file, auth methods will not have their `validate` methods called.
> - See the examples for workarounds, but consider using Ansible-specific ways of setting these values instead.

## [See Also](vault_ansible_settings_lookup.md#id5)

> **See also:**
>
> [Module defaults](../../../playbook_guide/playbooks_module_defaults.md#module-defaults)
> :   Using the `module_defaults` keyword.

## [Examples](vault_ansible_settings_lookup.md#id6)

```yaml+jinja
### In these examples, we assume an ansible.cfg like this:
# [hashi_vault_collection]
# url = https://config-based-vault.example.com
# retries = 5
### end ansible.cfg

### We assume some environment variables set as well
# ANSIBLE_HASHI_VAULT_URL: https://env-based-vault.example.com
# ANSIBLE_HASHI_VAULT_TOKEN: s.123456789
### end environment variables

# playbook - ansible-core 2.12 and higher
## set defaults for the collection group
- hosts: all
  vars:
    ansible_hashi_vault_auth_method: token
  module_defaults:
    group/community.hashi_vault.vault: "{{ lookup('community.hashi_vault.vault_ansible_settings') }}"
  tasks:
    - name: Get a secret from the remote host with settings from the controller
      community.hashi_vault.vault_kv2_get:
        path: app/some/secret
######

# playbook - ansible any version
## set defaults for a specific module
- hosts: all
  vars:
    ansible_hashi_vault_auth_method: token
  module_defaults:
    community.hashi_vault.vault_kv2_get: "{{ lookup('community.hashi_vault.vault_ansible_settings') }}"
  tasks:
    - name: Get a secret from the remote host with settings from the controller
      community.hashi_vault.vault_kv2_get:
        path: app/some/secret
######

# playbook - ansible any version
## set defaults for several modules
## do not use controller's auth
- hosts: all
  vars:
    ansible_hashi_vault_auth_method: aws_iam
    settings: "{{ lookup('community.hashi_vault.vault_ansible_settings', '*', '!*token*') }}"
  module_defaults:
    community.hashi_vault.vault_kv2_get: '{{ settings }}'
    community.hashi_vault.vault_kv1_get: '{{ settings }}'
  tasks:
    - name: Get a secret from the remote host with some settings from the controller, auth from remote
      community.hashi_vault.vault_kv2_get:
        path: app/some/secret

    - name: Same with kv1
      community.hashi_vault.vault_kv1_get:
        path: app/some/secret
######

# playbook - ansible any version
## set defaults for several modules
## do not use controller's auth
## override returned settings
- hosts: all
  vars:
    ansible_hashi_vault_auth_method: userpass
    plugin_settings: "{{ lookup('community.hashi_vault.vault_ansible_settings', '*', '!*token*') }}"
    overrides:
      auth_method: aws_iam
      retries: '{{ (plugin_settings.retries | int) + 2 }}'
    settings: >-
      {{
        plugin_settings
        | combine(overrides)
      }}
  module_defaults:
    community.hashi_vault.vault_kv2_get: '{{ settings }}'
    community.hashi_vault.vault_kv1_get: '{{ settings }}'
  tasks:
    - name: Get a secret from the remote host with some settings from the controller, auth from remote
      community.hashi_vault.vault_kv2_get:
        path: app/some/secret

    - name: Same with kv1
      community.hashi_vault.vault_kv1_get:
        path: app/some/secret
######

# using a block is similar
- name: Settings
  vars:
    ansible_hashi_vault_auth_method: aws_iam
    settings: "{{ lookup('community.hashi_vault.vault_ansible_settings', '*', '!*token*') }}"
  module_defaults:
    community.hashi_vault.vault_kv2_get: '{{ settings }}'
    community.hashi_vault.vault_kv1_get: '{{ settings }}'
  block:
    - name: Get a secret from the remote host with some settings from the controller, auth from remote
      community.hashi_vault.vault_kv2_get:
        path: app/some/secret

    - name: Same with kv1
      community.hashi_vault.vault_kv1_get:
        path: app/some/secret
#####

# use settings from a different plugin
## when you need settings that are not in the default plugin (vault_login)
- name: Settings
  vars:
    ansible_hashi_vault_engine_mount_point: dept-secrets
    settings: "{{ lookup('community.hashi_vault.vault_ansible_settings', plugin='community.hashi_vault.vault_kv2_get') }}"
  module_defaults:
    community.hashi_vault.vault_kv2_get: '{{ settings }}'
  block:
    - name: Get a secret from the remote host with some settings from the controller, auth from remote
      community.hashi_vault.vault_kv2_get:
        path: app/some/secret
#####

# use settings from a different plugin (on an indivdual call)
## short names assume community.hashi_vault
- name: Settings
  vars:
    ansible_hashi_vault_engine_mount_point: dept-secrets
    settings: "{{ lookup('community.hashi_vault.vault_ansible_settings') }}"
  module_defaults:
    community.hashi_vault.vault_kv2_get: '{{ settings }}'
  block:
    - name: Get a secret from the remote host with some settings from the controller, auth from remote
      community.hashi_vault.vault_kv2_get:
        engine_mount_point: "{{ lookup('community.hashi_vault.vault_ansible_settings', plugin='vault_kv2_get') }}"
        path: app/some/secret
#####

# normally, options with default values are not returned, but can be
- name: Settings
  vars:
    settings: "{{ lookup('community.hashi_vault.vault_ansible_settings') }}"
  module_defaults:
    # we usually want to use the remote host's IAM auth
    community.hashi_vault.vault_kv2_get: >-
      {{
        settings
        | combine({'auth_method': aws_iam})
      }}
  block:
    - name: Use the plugin auth method instead, even if it is the default method
      community.hashi_vault.vault_kv2_get:
        auth_method: "{{ lookup('community.hashi_vault.vault_ansible_settings', 'auth_method', include_default=True) }}"
        path: app/some/secret
#####

# normally, options with None/null values are not returned,
# nor are private options (names begin with underscore _),
# but they can be returned too if desired
- name: Show all plugin settings
  ansible.builtin.debug:
    msg: "{{ lookup('community.hashi_vault.vault_ansible_settings', include_none=True, include_private=True, include_default=True) }}"
#####

# dealing with low-precedence env vars and token sink loading
## here, VAULT_ADDR is usually used with plugins, but that will not work with vault_ansible_settings.
## additionally, the CLI `vault login` is used before running Ansible, so the token sink is usually used, which also will not work.
- hosts: all
  vars:
    plugin_settings: "{{ lookup('community.hashi_vault.vault_ansible_settings', 'url', 'token*', include_default=True) }}"
    overrides:
      url: "{{ plugin_settings.url | default(lookup('ansible.builtin.env', 'VAULT_ADDR')) }}"
      token: >-
        {{
          plugin_settings.token
          | default(
            lookup(
              'ansible.builtin.file',
              (
                plugin_settings.token_path | default(lookup('ansible.builtin.env', 'HOME')),
                plugin_settings.token_file
              ) | path_join
            )
          )
        }}
      auth_method: token
    settings: >-
      {{
        plugin_settings
        | combine(overrides)
      }}
  module_defaults:
    community.hashi_vault.vault_kv2_get: "{{ lookup('community.hashi_vault.vault_ansible_settings') }}"
  tasks:
    - name: Get a secret from the remote host with settings from the controller
      community.hashi_vault.vault_kv2_get:
        path: app/some/secret
#####
```

## [Return Value](vault_ansible_settings_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | A dictionary of the options and their values.  Only a single dictionary will be returned, even with multiple terms.  **Returned:** success  **Sample:** `{"retries": 5, "timeout": 20, "token": "s.jRHAoqElnJDx6J5ExYelCDYR", "url": "https://vault.example.com"}` |

### Authors

- Brian Scholer (@briantist)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.hashi_vault/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.hashi_vault)
- [Discussion, Q&A, troubleshooting](https://github.com/ansible-collections/community.hashi_vault/discussions)
- [Communication](index.md#communication-for-community-hashi-vault)

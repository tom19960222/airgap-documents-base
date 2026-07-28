---
collection: ansible
version: "6"
title: "ansible.builtin.config lookup – Lookup current Ansible configuration values"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/config_lookup.html
fetched_at: 2026-07-27T16:44:18+00:00
---
# ansible.builtin.config lookup – Lookup current Ansible configuration values

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `config` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](config_lookup.md#synopsis)
- [Terms](config_lookup.md#terms)
- [Keyword parameters](config_lookup.md#keyword-parameters)
- [Notes](config_lookup.md#notes)
- [Examples](config_lookup.md#examples)
- [Return Value](config_lookup.md#return-value)

## [Synopsis](config_lookup.md#id1)

- Retrieves the value of an Ansible configuration setting.
- You can use `ansible-config list` to see all available settings.

## [Terms](config_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | The key(s) to look up |

## [Keyword parameters](config_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.config', key1=value1, key2=value2, ...)` and `query('ansible.builtin.config', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **on_missing**  string | action to take if term is missing from config  Error will raise a fatal error  Skip will just ignore the term  Warn will skip over it but issue a warning  Choices:   - `"error"` ← (default) - `"skip"` - `"warn"` |
| **plugin_name**  string  added in ansible-core 2.12 | name of the plugin for which you want to retrieve configuration settings. |
| **plugin_type**  string  added in ansible-core 2.12 | the type of the plugin referenced by ‘plugin_name’ option.  Choices:   - `"become"` - `"cache"` - `"callback"` - `"cliconf"` - `"connection"` - `"httpapi"` - `"inventory"` - `"lookup"` - `"netconf"` - `"shell"` - `"vars"` |

## [Notes](config_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('ansible.builtin.config', term1, term2, key1=value1, key2=value2)` and `query('ansible.builtin.config', term1, term2, key1=value1, key2=value2)`

## [Examples](config_lookup.md#id5)

```yaml+jinja
- name: Show configured default become user
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.config', 'DEFAULT_BECOME_USER')}}"

- name: print out role paths
  ansible.builtin.debug:
    msg: "These are the configured role paths: {{lookup('ansible.builtin.config', 'DEFAULT_ROLES_PATH')}}"

- name: find retry files, skip if missing that key
  ansible.builtin.find:
    paths: "{{lookup('ansible.builtin.config', 'RETRY_FILES_SAVE_PATH')|default(playbook_dir, True)}}"
    patterns: "*.retry"

- name: see the colors
  ansible.builtin.debug: msg="{{item}}"
  loop: "{{lookup('ansible.builtin.config', 'COLOR_OK', 'COLOR_CHANGED', 'COLOR_SKIP', wantlist=True)}}"

- name: skip if bad value in var
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.config', config_in_var, on_missing='skip')}}"
  var:
    config_in_var: UNKNOWN

- name: show remote user and port for ssh connection
  ansible.builtin.debug: msg={{q("ansible.builtin.config", "remote_user", "port", plugin_type="connection", plugin_name="ssh", on_missing='skip')}}

- name: show remote_tmp setting for shell (sh) plugin
  ansible.builtin.debug: msg={{q("ansible.builtin.config", "remote_tmp", plugin_type="shell", plugin_name="sh")}}
```

## [Return Value](config_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  any | value(s) of the key(s) in the config  Returned: success |

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)

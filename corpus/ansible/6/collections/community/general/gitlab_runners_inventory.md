---
collection: ansible
version: "6"
title: "community.general.gitlab_runners inventory – Ansible dynamic inventory plugin for GitLab runners."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/gitlab_runners_inventory.html
fetched_at: 2026-07-27T17:14:47+00:00
---
# community.general.gitlab_runners inventory – Ansible dynamic inventory plugin for GitLab runners.

> **Note:**
>
> This inventory plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](gitlab_runners_inventory.md#ansible-collections-community-general-gitlab-runners-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_runners`.

- [Synopsis](gitlab_runners_inventory.md#synopsis)
- [Requirements](gitlab_runners_inventory.md#requirements)
- [Parameters](gitlab_runners_inventory.md#parameters)
- [Examples](gitlab_runners_inventory.md#examples)

## [Synopsis](gitlab_runners_inventory.md#id1)

- Reads inventories from the GitLab API.
- Uses a YAML configuration file gitlab_runners.[yml|yaml].

## [Requirements](gitlab_runners_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 2.7
- python-gitlab > 1.8.0

## [Parameters](gitlab_runners_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  aliases: private_token, access_token  string | GitLab token for logging in.  Configuration:   - Environment variable: [`GITLAB_API_TOKEN`](../../environment_variables.md#envvar-GITLAB_API_TOKEN)  added in community.general 1.0.0 |
| **compose**  dictionary | Create vars from jinja2 expressions.  Default: `{}` |
| **filter**  string | filter runners from GitLab API  Choices:   - `"active"` - `"paused"` - `"online"` - `"specific"` - `"shared"`   Configuration:   - Environment variable: [`GITLAB_FILTER`](../../environment_variables.md#envvar-GITLAB_FILTER)  added in community.general 1.0.0 |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  Default: `{}` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  Default: `[]` |
| **default_value**  string  added in ansible-core 2.12 | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  Default: `""` |
| **separator**  string | separator used to build the keyed group name  Default: `"_"` |
| **trailing_separator**  boolean  added in ansible-core 2.12 | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  Choices:   - `false` - `true` ← (default) |
| **leading_separator**  boolean  added in ansible-core 2.11 | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  Choices:   - `false` - `true` ← (default) |
| **plugin**  string / required | The name of this plugin, it should always be set to ‘gitlab_runners’ for this plugin to recognize it as it’s own.  Choices:   - `"gitlab_runners"` - `"community.general.gitlab_runners"` |
| **server_url**  string / required | The URL of the GitLab server, with protocol (i.e. http or https).  Configuration:   - Environment variable: [`GITLAB_SERVER_URL`](../../environment_variables.md#envvar-GITLAB_SERVER_URL)  added in community.general 1.0.0 |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  Choices:   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  added in ansible-core 2.11 | Merge extra vars into the available variables for composition (highest precedence).  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **verbose_output**  boolean | Toggle to (not) include all available nodes metadata  Choices:   - `false` - `true` ← (default) |

## [Examples](gitlab_runners_inventory.md#id4)

```yaml+jinja
# gitlab_runners.yml
plugin: community.general.gitlab_runners
host: https://gitlab.com

# Example using constructed features to create groups and set ansible_host
plugin: community.general.gitlab_runners
host: https://gitlab.com
strict: false
keyed_groups:
  # add e.g. amd64 hosts to an arch_amd64 group
  - prefix: arch
    key: 'architecture'
  # add e.g. linux hosts to an os_linux group
  - prefix: os
    key: 'platform'
  # create a group per runner tag
  # e.g. a runner tagged w/ "production" ends up in group "label_production"
  # hint: labels containing special characters will be converted to safe names
  - key: 'tag_list'
    prefix: tag
```

### Authors

- Stefan Heitmüller (@morph027)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

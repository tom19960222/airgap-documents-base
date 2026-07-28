---
collection: ansible
version: "6"
title: "community.general.icinga2 inventory – Icinga2 inventory source"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/icinga2_inventory.html
fetched_at: 2026-07-27T17:14:47+00:00
---
# community.general.icinga2 inventory – Icinga2 inventory source

> **Note:**
>
> This inventory plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.icinga2`.

New in community.general 3.7.0

- [Synopsis](icinga2_inventory.md#synopsis)
- [Parameters](icinga2_inventory.md#parameters)
- [Examples](icinga2_inventory.md#examples)

## [Synopsis](icinga2_inventory.md#id1)

- Get inventory hosts from the Icinga2 API.
- Uses a configuration file as an inventory source, it must end in `.icinga2.yml` or `.icinga2.yaml`.

## [Parameters](icinga2_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **compose**  dictionary  added in community.general 4.4.0 | Create vars from jinja2 expressions.  Default: `{}` |
| **groups**  dictionary  added in community.general 4.4.0 | Add hosts to group based on Jinja2 conditionals.  Default: `{}` |
| **host_filter**  string | An Icinga2 API valid host filter. Leave blank for no filtering |
| **inventory_attr**  string  added in community.general 4.2.0 | Allows the override of the inventory name based on different attributes.  This allows for changing the way limits are used.  The current default, `address`, is sometimes not unique or present. We recommend to use `name` instead.  Choices:   - `"name"` - `"display_name"` - `"address"` ← (default) |
| **keyed_groups**  list / elements=dictionary  added in community.general 4.4.0 | Add hosts to group based on the values of a variable.  Default: `[]` |
| **default_value**  string  added in ansible-core 2.12 | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  Default: `""` |
| **separator**  string | separator used to build the keyed group name  Default: `"_"` |
| **trailing_separator**  boolean  added in ansible-core 2.12 | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  Choices:   - `false` - `true` ← (default) |
| **leading_separator**  boolean  added in ansible-core 2.11 | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  Choices:   - `false` - `true` ← (default) |
| **password**  string / required | Password to query the API. |
| **plugin**  string / required | Name of the plugin.  Choices:   - `"community.general.icinga2"` |
| **strict**  boolean  added in community.general 4.4.0 | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  Choices:   - `false` ← (default) - `true` |
| **url**  string / required | Root URL of Icinga2 API. |
| **use_extra_vars**  boolean  added in ansible-core 2.11 | Merge extra vars into the available variables for composition (highest precedence).  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **user**  string / required | Username to query the API. |
| **validate_certs**  boolean | Enables or disables SSL certificate verification.  Choices:   - `false` - `true` ← (default) |

## [Examples](icinga2_inventory.md#id3)

```yaml+jinja
# my.icinga2.yml
plugin: community.general.icinga2
url: http://localhost:5665
user: ansible
password: secure
host_filter: \"linux-servers\" in host.groups
validate_certs: false
inventory_attr: name
groups:
  # simple name matching
  webservers: inventory_hostname.startswith('web')

  # using icinga2 template
  databaseservers: "'db-template' in (icinga2_attributes.templates|list)"

compose:
  # set all icinga2 attributes to a host variable 'icinga2_attrs'
  icinga2_attrs: icinga2_attributes

  # set 'ansible_user' and 'ansible_port' from icinga2 host vars
  ansible_user: icinga2_attributes.vars.ansible_user
  ansible_port: icinga2_attributes.vars.ansible_port | default(22)
```

### Authors

- Cliff Hults (@BongoEADGC6)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

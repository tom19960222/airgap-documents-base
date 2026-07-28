---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud inventory – Ansible dynamic inventory plugin for the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_inventory.html
fetched_at: 2026-07-28T01:05:45+00:00
---
# hetzner.hcloud.hcloud inventory – Ansible dynamic inventory plugin for the Hetzner Cloud.

> **Note:**
>
> This inventory plugin is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/ui/repo/published/hetzner/hcloud/) (version 1.16.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](hcloud_inventory.md#ansible-collections-hetzner-hcloud-hcloud-inventory-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud`.

- [Synopsis](hcloud_inventory.md#synopsis)
- [Requirements](hcloud_inventory.md#requirements)
- [Parameters](hcloud_inventory.md#parameters)
- [Examples](hcloud_inventory.md#examples)

## [Synopsis](hcloud_inventory.md#id1)

- Reads inventories from the Hetzner Cloud API.
- Uses a YAML configuration file that ends with hcloud.(yml|yaml).

## [Requirements](hcloud_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 3.5
- hcloud-python >= 1.0.0

## [Parameters](hcloud_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **connect_with**  string | Connect to the server using the value from this field. This sets the `ansible_host`  variable to the value indicated, if that value is available. If you need further customization, like falling back to private ipv4 if the server has no public ipv4, you can use `compose` top-level key.  **Choices:**   - `"public_ipv4"` ← (default) - `"public_ipv6"` - `"hostname"` - `"ipv4_dns_ptr"` - `"private_ipv4"` |
| **group**  string | The group all servers are automatically added to.  **Default:** `"hcloud"` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **images**  list / elements=string | Populate inventory with instances with this image name, only available for system images.  **Default:** `[]` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **label_selector**  string | Populate inventory with instances with this label.  **Default:** `""` |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **locations**  list / elements=string | Populate inventory with instances in this location.  **Default:** `[]` |
| **network**  string | Populate inventory with instances which are attached to this network name or ID.  **Default:** `""` |
| **plugin**  string / required | marks this as an instance of the “hcloud” plugin  **Choices:**   - `"hcloud"` - `"hetzner.hcloud.hcloud"` |
| **status**  list / elements=string | Populate inventory with instances with this status.  **Default:** `[]` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **token**  string | The Hetzner Cloud API Token. |
| **token_env**  string | Environment variable to load the Hetzner Cloud API Token from.  **Default:** `"HCLOUD_TOKEN"` |
| **types**  list / elements=string | Populate inventory with instances with this type.  **Default:** `[]` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |

## [Examples](hcloud_inventory.md#id4)

```yaml+jinja
# Minimal example. `HCLOUD_TOKEN` is exposed in environment.
plugin: hcloud

# Example with templated token, e.g. provided through extra vars.
plugin: hcloud
token: "{{ hetzner_apitoken }}"

# Example with locations, types, status and token
plugin: hcloud
token: foobar
locations:
  - nbg1
types:
  - cx11
status:
  - running

# Group by a location with prefix e.g. "hcloud_location_nbg1"
# and image_os_flavor without prefix and separator e.g. "ubuntu"
# and status with prefix e.g. "server_status_running"
plugin: hcloud
keyed_groups:
  - key: location
    prefix: hcloud_location
  - key: image_os_flavor
    separator: ""
  - key: status
    prefix: server_status
```

### Authors

- Lukas Kaemmerling (@lkaemmerling)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)

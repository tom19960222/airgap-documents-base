---
collection: ansible
version: "6"
title: "community.general.scaleway inventory – Scaleway inventory source"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/scaleway_inventory.html
fetched_at: 2026-07-27T17:14:52+00:00
---
# community.general.scaleway inventory – Scaleway inventory source

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
> see [Requirements](scaleway_inventory.md#ansible-collections-community-general-scaleway-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.general.scaleway`.

- [Synopsis](scaleway_inventory.md#synopsis)
- [Requirements](scaleway_inventory.md#requirements)
- [Parameters](scaleway_inventory.md#parameters)
- [Examples](scaleway_inventory.md#examples)

## [Synopsis](scaleway_inventory.md#id1)

- Get inventory hosts from Scaleway.

## [Requirements](scaleway_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- PyYAML

## [Parameters](scaleway_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostnames**  list / elements=string | List of preference about what to use as an hostname.  Choices:   - `"public_ipv4"` ← (default) - `"private_ipv4"` - `"public_ipv6"` - `"hostname"` - `"id"`   Default: `["public_ipv4"]` |
| **oauth_token**  string | Scaleway OAuth token.  If not explicitly defined or in environment variables, it will try to lookup in the scaleway-cli configuration file (`$SCW_CONFIG_PATH`, `$XDG_CONFIG_HOME/scw/config.yaml`, or `~/.config/scw/config.yaml`).  More details on [how to generate token](https://www.scaleway.com/en/docs/generate-api-keys/).  Configuration:   - Environment variable: [`SCW_TOKEN`](../../environment_variables.md#envvar-SCW_TOKEN) - Environment variable: [`SCW_API_KEY`](../../environment_variables.md#envvar-SCW_API_KEY) - Environment variable: [`SCW_OAUTH_TOKEN`](../../environment_variables.md#envvar-SCW_OAUTH_TOKEN) |
| **plugin**  string / required | Token that ensures this is a source file for the ‘scaleway’ plugin.  Choices:   - `"scaleway"` - `"community.general.scaleway"` |
| **regions**  list / elements=string | Filter results on a specific Scaleway region.  Default: `["ams1", "par1", "par2", "waw1"]` |
| **scw_profile**  string  added in community.general 4.4.0 | The config profile to use in config file.  By default uses the one specified as `active_profile` in the config file, or falls back to `default` if that is not defined. |
| **tags**  list / elements=string | Filter results on a specific tag. |
| **variables**  dictionary | Set individual variables: keys are variable names and values are templates. Any value returned by the [Scaleway API](https://developer.scaleway.com/#servers-server-get) can be used. |

## [Examples](scaleway_inventory.md#id4)

```yaml+jinja
# scaleway_inventory.yml file in YAML format
# Example command line: ansible-inventory --list -i scaleway_inventory.yml

# use hostname as inventory_hostname
# use the private IP address to connect to the host
plugin: community.general.scaleway
regions:
  - ams1
  - par1
tags:
  - foobar
hostnames:
  - hostname
variables:
  ansible_host: private_ip
  state: state

# use hostname as inventory_hostname and public IP address to connect to the host
plugin: community.general.scaleway
hostnames:
  - hostname
regions:
  - par1
variables:
  ansible_host: public_ip.address

# Using static strings as variables
plugin: community.general.scaleway
hostnames:
  - hostname
variables:
  ansible_host: public_ip.address
  ansible_connection: "'ssh'"
  ansible_user: "'admin'"
```

### Authors

- Remy Leone (@remyleone)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

---
collection: ansible
version: "6"
title: "community.general.online inventory – Scaleway (previously Online SAS or Online.net) inventory source"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/online_inventory.html
fetched_at: 2026-07-27T17:14:50+00:00
---
# community.general.online inventory – Scaleway (previously Online SAS or Online.net) inventory source

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
> To use it in a playbook, specify: `community.general.online`.

- [Synopsis](online_inventory.md#synopsis)
- [Parameters](online_inventory.md#parameters)
- [Examples](online_inventory.md#examples)

## [Synopsis](online_inventory.md#id1)

- Get inventory hosts from Scaleway (previously Online SAS or Online.net).

## [Parameters](online_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **groups**  list / elements=string | List of groups.  Choices:   - `"location"` - `"offer"` - `"rpn"` |
| **hostnames**  list / elements=string | List of preference about what to use as an hostname.  Choices:   - `"public_ipv4"` ← (default) - `"private_ipv4"` - `"hostname"`   Default: `["public_ipv4"]` |
| **oauth_token**  string / required | Online OAuth token.  Configuration:   - Environment variable: [`ONLINE_TOKEN`](../../environment_variables.md#envvar-ONLINE_TOKEN) - Environment variable: [`ONLINE_API_KEY`](../../environment_variables.md#envvar-ONLINE_API_KEY) - Environment variable: [`ONLINE_OAUTH_TOKEN`](../../environment_variables.md#envvar-ONLINE_OAUTH_TOKEN) |
| **plugin**  string / required | token that ensures this is a source file for the ‘online’ plugin.  Choices:   - `"online"` - `"community.general.online"` |

## [Examples](online_inventory.md#id3)

```yaml+jinja
# online_inventory.yml file in YAML format
# Example command line: ansible-inventory --list -i online_inventory.yml

plugin: community.general.online
hostnames:
  - public_ipv4
groups:
  - location
  - offer
  - rpn
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

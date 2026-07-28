---
collection: ansible
version: "6"
title: "community.general.chef_databag lookup – fetches data from a Chef Databag"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/chef_databag_lookup.html
fetched_at: 2026-07-27T17:14:56+00:00
---
# community.general.chef_databag lookup – fetches data from a Chef Databag

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](chef_databag_lookup.md#ansible-collections-community-general-chef-databag-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.chef_databag`.

- [Synopsis](chef_databag_lookup.md#synopsis)
- [Requirements](chef_databag_lookup.md#requirements)
- [Keyword parameters](chef_databag_lookup.md#keyword-parameters)
- [Examples](chef_databag_lookup.md#examples)
- [Return Value](chef_databag_lookup.md#return-value)

## [Synopsis](chef_databag_lookup.md#id1)

- This is a lookup plugin to provide access to chef data bags using the pychef package. It interfaces with the chef server api using the same methods to find a knife or chef-client config file to load parameters from, starting from either the given base path or the current working directory. The lookup order mirrors the one from Chef, all folders in the base path are walked back looking for the following configuration file in order : .chef/knife.rb, ~/.chef/knife.rb, /etc/chef/client.rb

## [Requirements](chef_databag_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- pychef ([Python library](https://pychef.readthedocs.io), `pip install pychef`)

## [Keyword parameters](chef_databag_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.chef_databag', key1=value1, key2=value2, ...)` and `query('community.general.chef_databag', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **item**  string / required | Item to fetch |
| **name**  string / required | Name of the databag |

## [Examples](chef_databag_lookup.md#id4)

```yaml+jinja
- ansible.builtin.debug:
    msg: "{{ lookup('community.general.chef_databag', 'name=data_bag_name item=data_bag_item') }}"
```

## [Return Value](chef_databag_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | The value from the databag.  Returned: success |

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

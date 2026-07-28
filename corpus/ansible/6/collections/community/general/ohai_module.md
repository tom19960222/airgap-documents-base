---
collection: ansible
version: "6"
title: "community.general.ohai module – Returns inventory data from Ohai"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ohai_module.html
fetched_at: 2026-07-27T17:11:12+00:00
---
# community.general.ohai module – Returns inventory data from *Ohai*

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](ohai_module.md#ansible-collections-community-general-ohai-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ohai`.

- [Synopsis](ohai_module.md#synopsis)
- [Requirements](ohai_module.md#requirements)
- [Examples](ohai_module.md#examples)

## [Synopsis](ohai_module.md#id1)

- Similar to the [community.general.facter](facter_module.md#ansible-collections-community-general-facter-module) module, this runs the *Ohai* discovery program (<https://docs.chef.io/ohai.html>) on the remote host and returns JSON inventory data. *Ohai* data is a bit more verbose and nested than *facter*.

## [Requirements](ohai_module.md#id2)

The below requirements are needed on the host that executes this module.

- ohai

## [Examples](ohai_module.md#id3)

```yaml+jinja
# Retrieve (ohai) data from all Web servers and store in one-file per host
ansible webservers -m ohai --tree=/tmp/ohaidata
```

### Authors

- Ansible Core Team
- Michael DeHaan (@mpdehaan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

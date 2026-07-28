---
collection: ansible
version: "6"
title: "community.general.rhsm_release module – Set or Unset RHSM Release version"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/rhsm_release_module.html
fetched_at: 2026-07-27T17:12:44+00:00
---
# community.general.rhsm_release module – Set or Unset RHSM Release version

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
> see [Requirements](rhsm_release_module.md#ansible-collections-community-general-rhsm-release-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rhsm_release`.

- [Synopsis](rhsm_release_module.md#synopsis)
- [Requirements](rhsm_release_module.md#requirements)
- [Parameters](rhsm_release_module.md#parameters)
- [Notes](rhsm_release_module.md#notes)
- [Examples](rhsm_release_module.md#examples)
- [Return Values](rhsm_release_module.md#return-values)

## [Synopsis](rhsm_release_module.md#id1)

- Sets or unsets the release version used by RHSM repositories.

## [Requirements](rhsm_release_module.md#id2)

The below requirements are needed on the host that executes this module.

- Red Hat Enterprise Linux 6+ with subscription-manager installed

## [Parameters](rhsm_release_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **release**  string / required | RHSM release version to use (use null to unset) |

## [Notes](rhsm_release_module.md#id4)

> **Note:**
>
> - This module will fail on an unregistered system. Use the `redhat_subscription` module to register a system prior to setting the RHSM release.

## [Examples](rhsm_release_module.md#id5)

```yaml+jinja
# Set release version to 7.1
- name: Set RHSM release version
  community.general.rhsm_release:
      release: "7.1"

# Set release version to 6Server
- name: Set RHSM release version
  community.general.rhsm_release:
      release: "6Server"

# Unset release version
- name: Unset RHSM release release
  community.general.rhsm_release:
      release: null
```

## [Return Values](rhsm_release_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **current_release**  string | The current RHSM release version value  Returned: success |

### Authors

- Sean Myers (@seandst)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

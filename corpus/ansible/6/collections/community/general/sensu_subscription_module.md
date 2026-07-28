---
collection: ansible
version: "6"
title: "community.general.sensu_subscription module – Manage Sensu subscriptions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/sensu_subscription_module.html
fetched_at: 2026-07-27T17:13:11+00:00
---
# community.general.sensu_subscription module – Manage Sensu subscriptions

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.sensu_subscription`.

- [Synopsis](sensu_subscription_module.md#synopsis)
- [Parameters](sensu_subscription_module.md#parameters)
- [Examples](sensu_subscription_module.md#examples)
- [Return Values](sensu_subscription_module.md#return-values)

## [Synopsis](sensu_subscription_module.md#id1)

- Manage which *sensu channels* a machine should subscribe to

## [Parameters](sensu_subscription_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | Create a backup file (if yes), including the timestamp information so you  can get the original file back if you somehow clobbered it incorrectly.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | The name of the channel |
| **path**  string | Path to the subscriptions json file  Default: `"/etc/sensu/conf.d/subscriptions.json"` |
| **state**  string | Whether the machine should subscribe or unsubscribe from the channel  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](sensu_subscription_module.md#id3)

```yaml+jinja
# Subscribe to the nginx channel
- name: Subscribe to nginx checks
  community.general.sensu_subscription: name=nginx

# Unsubscribe from the common checks channel
- name: Unsubscribe from common checks
  community.general.sensu_subscription: name=common state=absent
```

## [Return Values](sensu_subscription_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **reasons**  list / elements=string | the reasons why the module changed or did not change something  Returned: success  Sample: `` ["channel subscription was absent and state is `present'"] `` |

### Authors

- Anders Ingemann (@andsens)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

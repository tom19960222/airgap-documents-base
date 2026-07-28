---
collection: ansible
version: "8"
title: "community.general Test (Plugin) Guide"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/docsite/test_guide.html
fetched_at: 2026-07-28T01:44:30+00:00
---
# [community.general Test (Plugin) Guide](test_guide.md#id1)

The [community.general collection](../index.md#plugins-in-community-general) offers currently one test plugin.

Topics

- [community.general Test (Plugin) Guide](test_guide.md#community-general-test-plugin-guide)

  - [Feature Tests](test_guide.md#feature-tests)

## [Feature Tests](test_guide.md#id2)

The [community.general.a_module test](../a_module_test.md#ansible-collections-community-general-a-module-test) allows to check whether a given string refers to an existing module or action plugin. This can be useful in roles, which can use this to ensure that required modules are present ahead of time.

```yaml+jinja
- name: Make sure that community.aws.route53 is available
  assert:
    that:
      - >
        'community.aws.route53' is community.general.a_module

- name: Make sure that community.general.does_not_exist is not a module or action plugin
  assert:
    that:
      - "'community.general.does_not_exist' is not community.general.a_module"
```

New in version 4.0.0.

---
collection: ansible
version: "6"
title: "community.general.hwc_smn_topic module – Creates a resource of SMNTopic in Huaweicloud Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/hwc_smn_topic_module.html
fetched_at: 2026-07-27T17:09:26+00:00
---
# community.general.hwc_smn_topic module – Creates a resource of SMNTopic in Huaweicloud Cloud

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
> see [Requirements](hwc_smn_topic_module.md#ansible-collections-community-general-hwc-smn-topic-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hwc_smn_topic`.

- [Synopsis](hwc_smn_topic_module.md#synopsis)
- [Requirements](hwc_smn_topic_module.md#requirements)
- [Parameters](hwc_smn_topic_module.md#parameters)
- [Notes](hwc_smn_topic_module.md#notes)
- [Examples](hwc_smn_topic_module.md#examples)
- [Return Values](hwc_smn_topic_module.md#return-values)

## [Synopsis](hwc_smn_topic_module.md#id1)

- Represents a SMN notification topic resource.

## [Requirements](hwc_smn_topic_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 2.18.4
- keystoneauth1 >= 3.6.0

## [Parameters](hwc_smn_topic_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **display_name**  string | Topic display name, which is presented as the name of the email sender in an email message. The topic display name contains a maximum of 192 bytes. |
| **domain**  string / required | The name of the Domain to scope to (Identity v3). (currently only domain names are supported, and not domain IDs). |
| **id**  string | The id of resource to be managed. |
| **identity_endpoint**  string / required | The Identity authentication URL. |
| **name**  string / required | Name of the topic to be created. The topic name is a string of 1 to 256 characters. It must contain upper- or lower-case letters, digits, hyphens (-), and underscores `_`, and must start with a letter or digit. |
| **password**  string / required | The password to login with. |
| **project**  string / required | The name of the Tenant (Identity v2) or Project (Identity v3). (currently only project names are supported, and not project IDs). |
| **region**  string | The region to which the project belongs. |
| **state**  string | Whether the given object should exist in Huaweicloud Cloud.  Choices:   - `"present"` ← (default) - `"absent"` |
| **user**  string / required | The user name to login with (currently only user names are supported, and not user IDs). |

## [Notes](hwc_smn_topic_module.md#id4)

> **Note:**
>
> - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT` env variable.
> - For authentication, you can set user using the `ANSIBLE_HWC_USER` env variable.
> - For authentication, you can set password using the `ANSIBLE_HWC_PASSWORD` env variable.
> - For authentication, you can set domain using the `ANSIBLE_HWC_DOMAIN` env variable.
> - For authentication, you can set project using the `ANSIBLE_HWC_PROJECT` env variable.
> - For authentication, you can set region using the `ANSIBLE_HWC_REGION` env variable.
> - Environment variables values will only be used if the playbook values are not set.

## [Examples](hwc_smn_topic_module.md#id5)

```yaml+jinja
- name: Create a smn topic
  community.general.hwc_smn_topic:
      identity_endpoint: "{{ identity_endpoint }}"
      user_name: "{{ user_name }}"
      password: "{{ password }}"
      domain_name: "{{ domain_name }}"
      project_name: "{{ project_name }}"
      region: "{{ region }}"
      name: "ansible_smn_topic_test"
      state: present
```

## [Return Values](hwc_smn_topic_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **create_time**  string | Time when the topic was created.  Returned: success |
| **display_name**  string | Topic display name, which is presented as the name of the email sender in an email message. The topic display name contains a maximum of 192 bytes.  Returned: success |
| **name**  string | Name of the topic to be created. The topic name is a string of 1 to 256 characters. It must contain upper- or lower-case letters, digits, hyphens (-), and underscores `_`, and must start with a letter or digit.  Returned: success |
| **push_policy**  integer | Message pushing policy. 0 indicates that the message sending fails and the message is cached in the queue. 1 indicates that the failed message is discarded.  Returned: success |
| **topic_urn**  string | Resource identifier of a topic, which is unique.  Returned: success |
| **update_time**  string | Time when the topic was updated.  Returned: success |

### Authors

- Huawei Inc. (@huaweicloud)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

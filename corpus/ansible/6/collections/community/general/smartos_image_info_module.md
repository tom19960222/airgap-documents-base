---
collection: ansible
version: "6"
title: "community.general.smartos_image_info module – Get SmartOS image details"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/smartos_image_info_module.html
fetched_at: 2026-07-27T17:13:16+00:00
---
# community.general.smartos_image_info module – Get SmartOS image details

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
> To use it in a playbook, specify: `community.general.smartos_image_info`.

- [Synopsis](smartos_image_info_module.md#synopsis)
- [Parameters](smartos_image_info_module.md#parameters)
- [Examples](smartos_image_info_module.md#examples)

## [Synopsis](smartos_image_info_module.md#id1)

- Retrieve information about all installed images on SmartOS.
- This module was called `smartos_image_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [community.general.smartos_image_info](smartos_image_info_module.md#ansible-collections-community-general-smartos-image-info-module) module no longer returns `ansible_facts`!

## [Parameters](smartos_image_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **filters**  string | Criteria for selecting image. Can be any value from image manifest and ‘published_date’, ‘published’, ‘source’, ‘clones’, and ‘size’. More information can be found at <https://smartos.org/man/1m/imgadm> under ‘imgadm list’. |

## [Examples](smartos_image_info_module.md#id3)

```yaml+jinja
- name: Return information about all installed images
  community.general.smartos_image_info:
  register: result

- name: Return all private active Linux images
  community.general.smartos_image_info:
    filters: "os=linux state=active public=false"
  register: result

- name: Show, how many clones does every image have
  community.general.smartos_image_info:
  register: result

- name: Print information
  ansible.builtin.debug:
    msg: "{{ result.smartos_images[item]['name'] }}-{{ result.smartos_images[item]['version'] }}
         has {{ result.smartos_images[item]['clones'] }} VM(s)"
  with_items: "{{ result.smartos_images.keys() | list }}"

- name: Print information
  ansible.builtin.debug:
    msg: "{{ smartos_images[item]['name'] }}-{{ smartos_images[item]['version'] }}
         has {{ smartos_images[item]['clones'] }} VM(s)"
  with_items: "{{ smartos_images.keys() | list }}"
```

### Authors

- Adam Števko (@xen0l)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)

---
collection: ansible
version: "8"
title: "community.general.librato_annotation module – Create an annotation in librato"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/librato_annotation_module.html
fetched_at: 2026-07-28T01:47:30+00:00
---
# community.general.librato_annotation module – Create an annotation in librato

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.librato_annotation`.

- [Synopsis](librato_annotation_module.md#synopsis)
- [Parameters](librato_annotation_module.md#parameters)
- [Attributes](librato_annotation_module.md#attributes)
- [Examples](librato_annotation_module.md#examples)

## [Synopsis](librato_annotation_module.md#id1)

- Create an annotation event on the given annotation stream :name. If the annotation stream does not exist, it will be created automatically

Aliases: monitoring.librato_annotation

## [Parameters](librato_annotation_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | Librato account api key |
| **description**  string | The description contains extra metadata about a particular annotation  The description should contain specifics on the individual annotation e.g. Deployed 9b562b2 shipped new feature foo! |
| **end_time**  integer | The unix timestamp indicating the time at which the event referenced by this annotation ended  For events that have a duration, this is a useful way to annotate the duration of the event |
| **links**  list / elements=dictionary | See examples |
| **name**  string | The annotation stream name  If the annotation stream does not exist, it will be created automatically |
| **source**  string | A string which describes the originating source of an annotation when that annotation is tracked across multiple members of a population |
| **start_time**  integer | The unix timestamp indicating the time at which the event referenced by this annotation started |
| **title**  string / required | The title of an annotation is a string and may contain spaces  The title should be a short, high-level summary of the annotation e.g. v45 Deployment |
| **user**  string / required | Librato account username |

## [Attributes](librato_annotation_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](librato_annotation_module.md#id4)

```yaml+jinja
- name: Create a simple annotation event with a source
  community.general.librato_annotation:
    user: user@example.com
    api_key: XXXXXXXXXXXXXXXXX
    title: App Config Change
    source: foo.bar
    description: This is a detailed description of the config change

- name: Create an annotation that includes a link
  community.general.librato_annotation:
    user: user@example.com
    api_key: XXXXXXXXXXXXXXXXXX
    name: code.deploy
    title: app code deploy
    description: this is a detailed description of a deployment
    links:
      - rel: example
        href: http://www.example.com/deploy

- name: Create an annotation with a start_time and end_time
  community.general.librato_annotation:
    user: user@example.com
    api_key: XXXXXXXXXXXXXXXXXX
    name: maintenance
    title: Maintenance window
    description: This is a detailed description of maintenance
    start_time: 1395940006
    end_time: 1395954406
```

### Authors

- Seth Edwards (@Sedward)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

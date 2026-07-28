---
collection: ansible
version: "8"
title: "community.general.circonus_annotation module – Create an annotation in circonus"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/circonus_annotation_module.html
fetched_at: 2026-07-28T01:44:58+00:00
---
# community.general.circonus_annotation module – Create an annotation in circonus

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](circonus_annotation_module.md#ansible-collections-community-general-circonus-annotation-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.circonus_annotation`.

- [Synopsis](circonus_annotation_module.md#synopsis)
- [Requirements](circonus_annotation_module.md#requirements)
- [Parameters](circonus_annotation_module.md#parameters)
- [Attributes](circonus_annotation_module.md#attributes)
- [Notes](circonus_annotation_module.md#notes)
- [Examples](circonus_annotation_module.md#examples)
- [Return Values](circonus_annotation_module.md#return-values)

## [Synopsis](circonus_annotation_module.md#id1)

- Create an annotation event with a given category, title and description. Optionally start, end or durations can be provided

Aliases: monitoring.circonus_annotation

## [Requirements](circonus_annotation_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests (either >= 2.0.0 for Python 3, or >= 1.0.0 for Python 2)

## [Parameters](circonus_annotation_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | Circonus API key |
| **category**  string / required | Annotation Category |
| **description**  string / required | Description of annotation |
| **duration**  integer | Duration in seconds of annotation  **Default:** `0` |
| **start**  integer | Unix timestamp of event start  If not specified, it defaults to “now”. |
| **stop**  integer | Unix timestamp of event end  If not specified, it defaults to “now” + `duration`. |
| **title**  string / required | Title of annotation |

## [Attributes](circonus_annotation_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](circonus_annotation_module.md#id5)

> **Note:**
>
> - Check mode isn’t supported.

## [Examples](circonus_annotation_module.md#id6)

```yaml+jinja
- name: Create a simple annotation event with a source, defaults to start and end time of now
  community.general.circonus_annotation:
    api_key: XXXXXXXXXXXXXXXXX
    title: App Config Change
    description: This is a detailed description of the config change
    category: This category groups like annotations

- name: Create an annotation with a duration of 5 minutes and a default start time of now
  community.general.circonus_annotation:
    api_key: XXXXXXXXXXXXXXXXX
    title: App Config Change
    description: This is a detailed description of the config change
    category: This category groups like annotations
    duration: 300

- name: Create an annotation with a start_time and end_time
  community.general.circonus_annotation:
    api_key: XXXXXXXXXXXXXXXXX
    title: App Config Change
    description: This is a detailed description of the config change
    category: This category groups like annotations
    start_time: 1395940006
    end_time: 1395954407
```

## [Return Values](circonus_annotation_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **annotation**  complex | details about the created annotation  **Returned:** success |
| **_cid**  string | annotation identifier  **Returned:** success  **Sample:** `"/annotation/100000"` |
| **_created**  integer | creation timestamp  **Returned:** success  **Sample:** `1502236928` |
| **_last_modified**  integer | last modification timestamp  **Returned:** success  **Sample:** `1502236928` |
| **_last_modified_by**  string | last modified by  **Returned:** success  **Sample:** `"/user/1000"` |
| **category**  string | category of the created annotation  **Returned:** success  **Sample:** `"alerts"` |
| **description**  string | description of the created annotation  **Returned:** success  **Sample:** `"Host is down."` |
| **rel_metrics**  list / elements=string | Array of metrics related to this annotation, each metrics is a string.  **Returned:** success  **Sample:** `["54321_kbps"]` |
| **start**  integer | timestamp, since annotation applies  **Returned:** success  **Sample:** `"Host is down."` |
| **stop**  string | timestamp, since annotation ends  **Returned:** success  **Sample:** `"Host is down."` |
| **title**  string | title of the created annotation  **Returned:** success  **Sample:** `"WARNING"` |

### Authors

- Nick Harring (@NickatEpic)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)

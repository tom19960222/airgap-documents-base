---
collection: ansible
version: "6"
title: "Requesting changes to a collection"
source_url: https://docs.ansible.com/projects/ansible/6/community/reporting_collections.html
fetched_at: 2026-07-27T16:39:46+00:00
---
# Requesting changes to a collection

- [Reporting a bug](reporting_collections.md#reporting-a-bug)

  - [Security bugs](reporting_collections.md#security-bugs)
  - [Bugs in collections](reporting_collections.md#bugs-in-collections)
- [Requesting a feature](reporting_collections.md#requesting-a-feature)

## [Reporting a bug](reporting_collections.md#id1)

### [Security bugs](reporting_collections.md#id2)

Ansible practices responsible disclosure - if this is a security-related bug, email [security@ansible.com](mailto:security%40ansible.com) instead of filing a ticket or posting to any public groups, and you will receive a prompt response.

### [Bugs in collections](reporting_collections.md#id3)

Many bugs only affect a single module or plugin. If you find a bug that affects a module or plugin hosted in a collection, file the bug in the repository of the [collection](../user_guide/collections_using.md#collections):

> 1. Find the collection on [Galaxy](https://galaxy.ansible.com).
> 2. Click on the Issue Tracker link for that collection.
> 3. Follow the contributor guidelines or instructions in the collection repo.

If you are not sure whether a bug is in ansible-core or in a collection, you can report the behavior on the [mailing list or community chat channel first](communication.md#communication).

## [Requesting a feature](reporting_collections.md#id4)

Before you request a feature, check what is [planned for future Ansible Releases](../roadmap/ansible_roadmap_index.md#roadmaps).
The best way to get a feature into an Ansible collection is to [submit a pull request](development_process.md#community-pull-requests), either against ansible-core or against a collection. See also [Requirements to merge your PR](contributing_maintained_collections.md#ansible-collection-merge-requirements).

You can also submit a feature request through opening an issue in the collection repository.
